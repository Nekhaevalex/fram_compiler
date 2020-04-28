import pya #Klayout 
import os
import sys
import datetime
import random
import time
from utils import * # Тут хранятся полезные функции которые я иногда юзаю во всех функциях
from cells import * # 
from lvs import * # Запуск LVS сравнения топологии и нетлиста

from layout import My_Layout # Модуль наследованный от klayout.layout с некоторыми полезными плюшками.
from config import Config # Main Config are used by compiler through all of the functions.
from netlist import * # My Netlist class


from design import Design

#  For Debug
from inspect import currentframe, getframeinfo


import technology #Тут храниться специфическая для технологии информация чтобы ее можно было корректировать не трогая код. Думаю это только дебаг фича и нужно придумать что то более классное.
#import sys


class Fram():
	core_cells = []
	"""Main class contain layout (My_Layout) and netlist (Netlist) objcts. Fram itself 
	consists of modules, module is a layout_cell and netlist curciut representation and 
	it's methods"""
	def __init__(self, Config):
		'''Main magic happens here!'''
		self.Config = Config
		self.Config.debug_message(0,f"Starting generating of FRAM array which consists of {Config.num_words} x {Config.word_size} cells. Time is 'add_time'.")
		self.create_design(	self.create_layout() ,	self.init_netlist())
		#self.design = (self.fram_layout , self.fram_netlist)
		self.Config.debug_message(1,f'Starting to check modules source files')
		check_os_content("gds_files")
		check_os_content("netlists")
		#self.memory_cell = Memory_Cell(create_bitline_gdsself.fram_layout.read_cell_from_gds("memory_cell"))
		self.memory_cell = self.read_memory_cell()
		#self.sense_amp = Sense_Amp(sense_amp_cells,Config)
		self.sense_amp = self.read_sense_amp_cell()
		self.top_driver = self.read_top_driver()
		self.Config.debug_message(3,f'All cells ready.. Creating core.')
		self.create_array_core(self.core_cells) # Create array of bitlines
		#self.fram_netlist.write_netlist()
		self.gds_output() # Make output of gds
		self.sp_output()


		self.lvs = LVS(self.Config)

	def read_memory_cell(self):
		memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds(self.Config.fram_bitcell_name) , self.Config , is_basic_cell = True)
		self.core_cells.append(memory_cell)
		return memory_cell

	def create_layout(self):
		self.fram_layout = My_Layout(Config)
		self.pins_layers = self.fram_layout.pins_layers
		return self.fram_layout

	def create_design(self,*args):
		self.design = Design(self.Config, *args)

	def read_sense_amp_cell(self):
		sense_name_1 = self.Config.sense_amp_gnd_name
		sense_name_2 = self.Config.sense_amp_vdd_name
		sense_amp_cells = (self.fram_layout.read_cell_from_gds(sense_name_1) , self.fram_layout.read_cell_from_gds(sense_name_2) )
		sense_amp = Side_Module(sense_amp_cells,self.Config)
		self.core_cells.append(sense_amp)
		return sense_amp

	def read_module_gds(self,names):
		cells = []
		for name in names:
			cells.append(self.fram_layout.read_cell_from_gds(name))
		return cells

	def read_top_driver(self):
		name = "top_driver"
		cells = self.read_module_gds(self.Config.top_driver)
		top_driver = Side_Module(cells,self.Config, cell_name = name , placement = "top", connect_to = "bl", connect_with = "out" )
		self.core_cells.append(top_driver)
		return top_driver

	def create_array_core(self,cells):
		self.array_core = Array_Core( self.design , cells ,  self.Config)
		# TODO !! Fix design instead
		#self.fram_netlist = self.array_core.fram_netlist
		self.core_offset = (self.array_core.x_offset,self.array_core.y_offset)
		self.update_design_from(self.array_core)
		self.Config.debug_message(0,f'Created array of cells!')

	def gds_output(self):
		output_path = "./gds_files/"+ self.Config.output_name+".gds"
		self.fram_layout.write(output_path)
		self.Config.debug_message(0,f'Wow! GDS output file is now created in "{output_path}" !')
		return output_path

	def sp_output(self):
		self.fram_netlist.write_netlist()

	def init_netlist(self):
		self.fram_netlist = Fram_Netlist(self.Config)
		return self.fram_netlist

	def write_netlist(self):
		self.fram_netlist.write_netlist()

	def unpack_design(self, design = None):
		if (design == None ):
			self.fram_layout = 	self.design.return_layout()
			self.fram_netlist = self.design.return_netlist()
		else:
			self.fram_layout = design.return_layout()
			self.fram_netlist = design.return_netlist()

	def update_design_from(self, new_source):
		self.design = new_source.design
		self.unpack_design()

class Array_Core:
	"""Multiplying bitlines class"""
	cell_name = "core"
	cells_placements = {}
	coords = {} # temp coords dict for gds creation
	def __init__(self, design , cells , Config):
		self.design = design
		self.unpack_design()
		self.Config = Config
		self.cells = cells
		
		'''В начале ячеек нет, поэтому помечаю все позиции как вакантные.'''
		for placement in ["top","bottom","left","right"]:
			self.cells_placements[placement] = False

		

		''' FIX THIS SHIT! '''

		self.memory_cell = self.find_cell_in_cells("memory_cell",self.cells)
		self.fram_netlist.add_device(self.memory_cell.netlist_device)
		#self.sense_amp = self.find_cell_in_cells("sense_amp",self.cells)
		'''   !!!!!!!!!    '''
		self.modules = []
		for module in cells:
			if module.cell_name != "memory_cell":
				self.modules.append(module)


		
		self.layer_map = self.fram_layout.layer_dict
		#self.memory_cell = Bitline.memory_cell

		# \/   \/   You may define step from 2 sources: any boundary layer you want (specify layer). Or all cell polygon by default.
		self.X_step = self.define_X_step(cells,self.layer_map[self.Config.boundary_layer]) 
		#self.Y_step = self.define_Y_step(cells)
		self.Y_step = self.memory_cell.height

		#self.bitline = Bitline
		self.bitline_cell = Module(self.fram_layout.create_cell("bitline"),Config)
		self.array_core_cell = Module(self.fram_layout.create_cell(self.cell_name) , Config)
		#self.memory_cell = Bitline.memory_cell
		self.layer_map = self.fram_layout.layer_dict

		#self.X_step = self.memory_cell.width
		
		self.create_core_gds()
		self.create_netlist()



		''' Adding side modules here! '''
		for module in self.modules:
			self.Config.debug_message(4,f"Add side module {module.cell_name}")
			self.add_side_module(module)

		''' Design update '''
		self.design.update_design(self.fram_layout , self.fram_netlist)

		''' Now add decoders'''
		self.add_decoders()

	def unpack_design(self, design = None):
		if (design == None ):
			self.fram_layout = 	self.design.return_layout()
			self.fram_netlist = self.design.return_netlist()
		else:
			self.fram_layout = design.return_layout()
			self.fram_netlist = design.return_netlist()

	def update_design_from(self, design_new):
		self.design = design_new
		self.unpack_design()



	def add_decoders(self):
		self.design.update_design(self.fram_layout , self.fram_netlist)
		self.decoder = Decoder(self.Config , self.design)
		self.update_design_from(self.decoder.design)
		self.unpack_design()
		self.add_decoder_cells_to_layout()




	def find_cells(self, cells):
		for cell in cells:
			if (cell.cell_name == self.Config.fram_bitcell_name):
				self.memory_cell = cell
			if (Cell.cell_name == self.Config.sense_amp_name):
				self.sense_amp = cell

	def define_X_step(self , modules , layer = None):
		'''Определяем сетку по оси Х, меньше которой нельзя размещать ячейки. Определяем путем перебора по всем прямоугольникам в слое layer.
		Можно менять слой в зависимости от того какой слой специфицирован в качестве boundary, так же можно оставить пустым для просмотра по всей ячейке в целом.'''
		dx = []
		for module in modules:
			for cell in module.cells:
				if (layer == None):
					boundary = module.find_cell_boundary(cell)
				else:
					boundary = module.find_cell_boundary(cell,layer)
				dx.append(boundary.width())
				self.Config.debug_message(4,f'dx size of cell {cell.name} is {boundary.width()}')
		X_step = max(dx)
		self.Config.debug_message(3,f'Defines X - size  of {X_step}. By comparing of list {dx}')
		self.fram_layout.X_step = X_step
		return X_step
				
	def define_Y_step(self,modules):
		'''Определяем сетку по оси Y, меньше которой нельзя размещать ячейки. Определяем путем перебора по всем прямоугольникам в слое layer.
		Можно менять слой в зависимости от того какой слой специфицирован в качестве boundary, так же можно оставить пустым для просмотра по всей ячейке в целом.'''
		dy = []
		for module in modules:
			for cell in module.cells:
				boundary = module.find_cell_boundary(cell)	
				dy.append(boundary.width())
		Y_step = max(dy)
		self.fram_layout.Y_step = Y_step
		return Y_step

	def find_cell_in_cells(self,name,cells):
		found = False
		for cell in cells:
			if (cell.cell_name == name):
				new_cell = cell
				self.Config.debug_message(2,f'Cell  {name} added to core cells list.')
				found = True
				return new_cell
		if (found == False):
			self.Config.debug_message(-1,f'===== WARNING! =====\n Fail to find a cell with name {name}.')
			self.Config.warning(getframeinfo(currentframe()))

	def create_core_gds(self):
		''' Отдельная функция для создания топологии ядра'''
		self.init_markers()
		self.create_bitline_gds()

		xpos = 0

		ypos = 0

		for i in range (0,Config.word_size):
			t = pya.Trans(xpos,ypos)
			self.bitline_cell.place(self.array_core_cell.cell,t)
			xpos += self.X_step

		self.x_offset = xpos
		self.add_markers('bl',self.bitline_coords) # !!!
		self.write_line_routing()
		self.core_line_routing("pl","M3","x")
		self.core_line_routing("gnd","M2","x")

		self.Config.debug_message(0,f'Created core (only memory cells) with coordinates as box (0,0) to ({self.x_offset},{self.y_offset})')

	def create_bitline_gds(self):
		xpos = 0

		ypos = 0

		for i in range(0,self.Config.num_words):
			t = pya.Trans(xpos,ypos)
			self.memory_cell.place(self.bitline_cell.cell, t)
			#ypos += Memory_Cell.height
			#text = pya.Text(f"here is the connection# {i}", xpos , ypos)
			ypos += self.Y_step

			#self.bitline_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
		self.y_offset = ypos
		self.bitline_routing()



	def bitline_routing(self):
		self.bitline_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"], self.layer_map["M3_pin"] ])
		
		xpos = self.bitline_pinmap["bl"].text.x 
		ypos = self.bitline_pinmap["bl"].text.y
		self.bitline_coords = ((xpos,ypos) , (xpos, self.y_offset) )
		simple_path(self.bitline_cell.cell, self.layer_map["M1"], pya.Point(xpos,ypos), pya.Point(xpos,self.y_offset) , self.Config.bl_width)

	def write_line_routing(self):
		#self.memory_cell_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"]])
		
		xpos = self.memory_cell_pinmap["wn"].text.x
		ypos = self.memory_cell_pinmap["wn"].text.y
		for i in range (0,self.Config.word_size):
			simple_path(self.array_core_cell.cell, self.layer_map["M2"], pya.Point(xpos,ypos), pya.Point(self.x_offset,ypos) , self.Config.bl_width)
			ypos = ypos + self.Y_step
		if (self.Config.debug_level > 1 ):
			print(f'Complited routing of bitline with end point as ({xpos} , {ypos})')

	def core_line_routing(self, line_name , layer , orient):
		

		xpos = self.bitline_pinmap[line_name].text.x 
		ypos = self.bitline_pinmap[line_name].text.y
		if (orient == "y") :
			self.coords[line_name] = ((xpos,ypos) , (xpos, self.y_offset) )
			for i in range(self.Config.word_size) :
				simple_path(self.array_core_cell.cell, self.layer_map[layer], pya.Point(xpos,ypos), pya.Point(xpos,self.y_offset) , self.Config.width[line_name])
				xpos = xpos + self.X_step
		elif ( orient == "x" ):
			self.coords[line_name] = ((xpos,ypos) , (self.x_offset, ypos) )
			for i in range(self.Config.word_size) :
				simple_path(self.array_core_cell.cell, self.layer_map[layer], pya.Point(xpos,ypos), pya.Point(self.x_offset, ypos) , self.Config.width[line_name])
				ypos = ypos + self.Y_step
		else: 
			print("ERROR in orientation of {line_name}. Fix me")
		
	def update_netlist(self , src):
		self.fram_netlist = src.fram_netlist

	def create_netlist(self):
		self.create_bitline_netlist()
		for i in range(self.Config.word_size):
			self.add_bitline_netlist(i)
		self.Config.debug_message(2,f"Created netlist!\n")
		
	def create_bitline_netlist(self):
		bitline_out_terminals = [f"bl"]
		bl_nets = []
		for i in range(0, self.Config.word_size):
			bl_nets.append(f"bl{i}")
		self.bl_nets = bl_nets
		for i in range(0,self.Config.num_words):
			bitline_out_terminals.append(f"wl{i}")
			bitline_out_terminals.append(f"pl{i}")
		bitline_out_terminals.append("gnd")
		self.bitline_netlist = Curcuit("bitline" , self.Config , bitline_out_terminals, self.memory_cell.netlist_device)
		#self.fram_netlist.add_sub(bitline_netlist)
		#self.bitline_netlist = bitline_netlist

	def add_bitline_netlist(self, bl_n):
		#self.fram_netlist.add_inst(self.bitline_netlist, [])
		bl_net=f"bl{bl_n}"
		wl_nets = []
		pl_nets = []
		for i in range(0,self.Config.num_words):
			wl_nets.append("wl"+str(i))	
			pl_nets.append("pl"+str(i))	
			self.fram_netlist.add_inst(self.memory_cell.netlist_device , [bl_net, wl_nets[i] , pl_nets[i] ,"gnd"])
		self.wl_nets = wl_nets
		self.pl_nets = pl_nets



	def add_side_module (self, module):
		self.add_module_layout(module)
		self.add_module_netlist(module)

		'''
		M1_pin = self.layer_map["M1_pin"]
		bl_pinmap = self.array_core_cell.find_pin_map([M1_pin])
		print_pins(bl_pinmap) # remove
		'''

	def add_decoder_cells_to_layout(self):
		#xpos = self.memory_cell.pin_map["wn"].text.x #- self.decoder.pin_map[0][self.decoder.connect_with[0]].text.x
		#FIX TO : 
		#xpos = self.memory_cell.pin_map[self.decoder.connect_to].text.x - self.decoder.pin_map[self.decoder.connect_with[0]].text.x
		xpos = -10000
		ypos = 0
		mode = 0
		for i in range( int(self.Config.num_words / 2) ):
			t = pya.Trans(xpos , ypos)
			self.decoder.place(self.array_core_cell.cell,t,mode)
			mode = swich_mode(mode)
			ypos = ypos + 2 * self.Y_step

	def add_module_layout(self, module):

		''' Placement  of a module by pin coords '''
		layer_pins = [ self.layer_map["M1_pin"] , self.layer_map["M2_pin"] ]
		module.pin_map = module.find_pin_map(layer_pins)
		print (f"placement of {module.cell_name} = {module.placement}")

		# Проверяю на совпадения с такими же расположениями (чтобы предупредить если два разных модуля будут втыкаться один поверх другого.)

		if (self.cells_placements[module.placement] == True):
			self.Config.debug_message(-1,f'========== WARNING ========= \n \n ')
			self.Config.debug_message(-1,f'''No placement repeat found for "{module.cell_name}" cell. Check that no other sells are placed With the same "module.placement". Parameter. Check output gds for errors.''')


		if (module.placement == "top") or (module.placement == "bottom"):

			if ( module.placement == "bottom" ):
				ypos = - self.Config.module_clearence
			if (module.placement == "top"):
				ypos = self.y_offset + self.Config.module_clearence
			n = 0
			xpos1 = self.end_markers[module.connect_to][0].x - module.pin_map[0][module.connect_with].text.x
			xpos2 = self.end_markers[module.connect_to][0].x - module.pin_map[1][module.connect_with].text.x
			
			y_shift = ypos
			for i in  range(0, self.Config.word_size):
				if (n == 0):
					t = pya.Trans(xpos1,ypos)
					module.place(self.array_core_cell.cell, t , mode =n)
					
				if (n == 1):
					t = pya.Trans(xpos2,ypos)
					module.place(self.array_core_cell.cell, t , mode =n)
				#print(f"n = {n}")
				n = swich_mode(n)
				xpos1 = xpos1 + self.X_step
				xpos2 = xpos2 + self.X_step



			''' Routing of a module '''
			xpos1 = [0,0]
			ypos1 = [0,0]
			xpos2 = [0,0]
			ypos2 = [0,0]
			xpos1[0] = self.end_markers[module.connect_to][0].x
			xpos1[1] = xpos1[0] + self.X_step 
			xpos2 = xpos1
			ypos1[0] = y_shift
			ypos2[0] = self.memory_cell_pinmap[module.connect_to].text.y
			ypos1[1] = y_shift
			ypos2[1] = self.memory_cell_pinmap[module.connect_to].text.y
			print(f"self.X_step = {self.X_step}")
			for i in range(self.Config.word_size//2):
				print(f"({xpos1[0]},{ypos1[0]}) to ({xpos1[0]},{xpos2[0]})")
				for i in range(len(xpos1)):
					simple_path(self.array_core_cell.cell, self.layer_map["M1"], pya.Point(xpos1[i],ypos1[i]), pya.Point( xpos2[i], ypos2[i]) , self.Config.width[module.connect_to])
				xpos1[0] += self.X_step
				xpos1[1] += self.X_step
				xpos2[0] += self.X_step
				xpos2[1] += self.X_step

			# Добавляю указаное положение в добавленные, чтобы если что не городить ячейку на ячейку.

			self.cells_placements[module.placement] = True
 
 			#if (module.cell_name == "sense_amp"):
 			#	pass


			''' example from bitline:

			self.bitline_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"]])
			xpos = self.bitline_pinmap["bl"].text.x 
			ypos = self.bitline_pinmap["bl"].text.y
			self.bitline_coords = ((xpos,ypos) , (xpos, self.y_offset) )
			simple_path(self.bitline_cell.cell, self.layer_map["M1"], pya.Point(xpos,ypos), pya.Point(xpos,self.y_offset) , self.Config.bl_width)
			'''
		
		else:
			self.Config.debug_message(-1,f'========== WARNING ========= \n ')
			self.Config.debug_message(-1,f'''No placement found for "{module.cell_name}" cell. Check cell settings/ Placement should be a parameter (cell.placement) = ["top","bottom","left" etc].
				Skipping "{module.cell_name}" module''')
			self.Config.warning(getframeinfo(currentframe()))


	def add_extra_routing(self, module):
		if (module.placement == "bottom"):
			for i in range(0,self.Config.word_size):
				#a
				pass


	def add_module_netlist(self, module):
		
		self.fram_netlist.add_device(module.netlist_device)

		terminal_pos = find_iterator(module.netlist_device.pins, module.connect_with)

		raw_pins = module.netlist_device.pins

		connect_to_pin_n = None

		for i in range(len(raw_pins)):
			if raw_pins[i] == module.connect_with :
				connect_to_pin_n = i		
		if connect_to_pin_n == None:
			print(f"ERROR in add_module_netlist(self, module): (pins)")

		if ( module.placement == "bottom" ) or ( module.placement == "top" ) :
			for i in range(0,self.Config.word_size):
				new_pins = module.netlist_device.pins
				new_pins[connect_to_pin_n] = f"{module.connect_to}{i}"
				self.fram_netlist.add_inst(module.netlist_device , module.netlist_device.pins)
			
	
		if ( module.placement == "left" ) or ( module.placement == "right" )  :
			for i in range(0,self.Config.num_words):
				new_pins = module.netlist_device.pins
				new_pins[connect_to_pin_n] = f"{module.connect_to}{i}"	
				self.fram_netlist.add_inst(module.netlist_device , module.netlist_device.pins)


	def init_markers(self):
		self.end_markers = {}
		self.begin_markers = {}
		#for name in names:
		#	end_markers
		self.memory_cell_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"], self.layer_map["M3_pin"] ])

	def add_markers(self,name , coords):
		''' ===  Add some text to the tips of the lines and bitlines  ===    '''
		self.end_markers[name] = []
		self.begin_markers[name] = []

		xpos = coords[1][0]
		ypos = coords[1][1]
		for i in range(0, self.Config.word_size):
			if ( self.Config.marker_as_text == True ):
				text = pya.Text(f"end_of_{name}{i}", xpos , ypos)
				#print(f'x = {xpos} , y = {ypos}') #Debug
				self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			self.end_markers[name].append(pya.Point(xpos,ypos))
			xpos = xpos + self.X_step

		xpos = coords[0][0]
		ypos = coords[0][1]
		for i in range(0, self.Config.word_size):
			if (self.Config.marker_as_text):
				text = pya.Text(f"begin_of_{name}{i}", xpos , ypos)
				#print(f'x = {xpos} , y = {ypos}') #Debug
				self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			self.begin_markers[name].append(pya.Point(xpos,ypos))
			xpos = xpos + self.X_step
		#self.bl_begin_markers = bl_begin_markers
		#self.bl_end_markers = bl_end_markers

# ===================== CODE HERE! ============

start_time = time.perf_counter()

config = Config()
fram = Fram(config)

view_gds(config)

end_time = time.perf_counter()

print(f"Compiling in {round(end_time - start_time , 2 )}s")
