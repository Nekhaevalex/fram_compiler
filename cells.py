import pya

import os

from utils import *
from netlist import *




class Module:
	'''Module class represents a physical device with two represetitives as Module.cell = layout representation and Module.netlist as a netlist '''
	pin_map = {}
	placement = "core"
	cells_in_cell = 1
	"""docstring for ClassName"""
	def __init__(self, cell , Config, is_basic_cell = False , name = None): #+ netlist
		self.Config = Config
		self.cell = cell
		self.cell_name = cell.name
		self.cells = []
		self.cells.append(cell)
		self.boundary_box = self.find_boundary()
		self.height = self.find_dimensions()[0]
		self.width = self.find_dimensions()[1]
		self.cell_name = self.cell.name
		if is_basic_cell:
			self.netlist_device = Netlist_Device(self.cell_name,self.Config)

		#self.netlist = netlist

	def place(self,target,t):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cell.cell_index(),t)
		target.insert(istance)

	def find_pin_map(self, layers):
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		pin_map = {}
		for layer in layers:
			for i in self.cell.each_shape(layer):
			#print("===== + 1 =======")
				if (i.is_text()):
					pin_map[i.text_string] = i
					#pin_map[i.text_string+'_layer'] 
					#print(i.text) - text object
					#print(i.text_string)# - text itself
		self.pin_map = pin_map
		if (self.Config.debug_level > 2):
			print(f"Pins of {self.cell.name} is:")
			print_pins(pin_map)
		return pin_map



	def find_boundary(self,layer= None): #default layer is PR Bndry
		if (layer == None):
			boundary = self.cell.bbox()
			return boundary
		if (layer != None):
			boundary = self.cell.bbox_per_layer(layer)
			return boundary

	def find_cell_boundary(self , cell , layer = None):
		if (layer == None):
			boundary = cell.bbox()
			return boundary
		if (layer != None):
			boundary = cell.bbox_per_layer(layer)
			return boundary

			
		#return boundary

	def find_dimensions(self, layer = None):
		if (layer == None):
			boundary = self.find_boundary()
			dy = boundary.width()
			dx = boundary.height()
			return(dx,dy)
		else:
			boundary = self.find_boundary(layer)
			dx = boundary.width()
			dy = boundary.height()
			return(dx,dy)

	def get_cell_name(self):
		pass




class Memory_Cell(Module):
	cell_name = "memory_cell"





class Side_Module():
	''' Любые боковые боковые модули кроме декодеров (усилители чтения, драйверы) пока размещаются по одному 
	с каждой стороны. Так же на данный момент по умолчанию размещаются зеркальные копии для экономии места.
	Netlist содержиться отельно как переменная класса Netlist_Device (иницируется тут, но написан не тут) (файл netlist.py) '''
	cell_name = "sense_amp"
	cells_in_cell = 2
	placement = "bottom"
	pin_map = ({},{})
	connect_to = 'bl'
	connect_with = 'in'
	def __init__(self,cells , Config, cell_name = "sense_amp" , placement = "bottom", connect_to = "bl", connect_with = "in" ):
		self.Config = Config
		self.cells = cells
		self.cell_name = cell_name
		self.placement = placement
		self.connect_to = connect_to
		self.connect_with = connect_with
		self.cells_in_cell = len(cells)
		self.boundary_box = ()
		self.netlist_device = Netlist_Device(self.cell_name,self.Config)
		Config.debug_message(2, f"Created Sense_Amp , with start cell {cells[0].name}")


	def find_cell_boundary(self, cell ,layer= None): #default layer is PR Bndry
		k = 0
		if (layer == None):
			boundary = cell.bbox()
		if (layer != None):
			boundary = cell.bbox_per_layer(layer)
		return boundary


	def find_pin_map(self, layers): ## -------------- FIX!----------
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		h = 0
		pin_map = ({},{})
		for cell in self.cells:
			for layer in layers:
				for i in cell.each_shape(layer):
					if (i.is_text()):
						pin_map[h][i.text_string] = i
						#pin_map[i.text_string+'_layer'] 
						#print(i.text) - text object
						#print(i.text_string)# - text itself
			h = h + 1
		if (self.Config.debug_level > 2):
			for this_map in pin_map:
				print(f"Pins of {self.cell_name} map is:")
				print_pins(this_map)
		self.pin_map = pin_map
		return pin_map


	def place(self,target,t,mode = 0):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cells[mode].cell_index(),t)
		target.insert(istance)


class Mosfet(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		



class Decoder:
	"""docstring for decoders"""
	pin_map = ({},{})
	out_pin_map = {}
	placement = "left"
	connect_to = 'wl'
	connect_with = ('WL0','WL1')
	cells_in_cell = 2
	cells = []

	def __init__(self, Config , design):
		self.Config = Config
		self.addr_n = find_pwr2(self.Config.num_words ,0)
		#self.mosfets = mosfets
		self.design = design
		self.unpack_design()

		self.pre_decoder_cells = self.import_predecoder_cells()

		self.layer_map = self.fram_layout.layer_dict
		self.import_mos_pair() # Import view of p-mos and n-mos merged cell to build a NAND - gate out of them.
		#self.define_mosfets(mosfets)

		self.cells_in_cell = len(self.cells)
		''' User init code starts here '''
		self.init_pre_decoder()
		self.create_decoder_cells()
		#self.add_decoder_cells() # Now called in array core
		''' User init code ends here '''
		self.update_design()

	def create_decoder_cells(self):
		self.create_decoders_gds()
		self.create_decoders_netlist()

	def create_decoders_gds(self):
		'''create_gds_of_decoders'''
		self.vdd_cell = self.fram_layout.create_cell("decoder_vdd")
		self.gnd_cell = self.fram_layout.create_cell("decoder_gnd")

		xpos = 0
		ypos = 0

		t = pya.Trans(xpos,ypos)
		self.pre_decoder.place(self.vdd_cell , t , cell = self.pre_decoder.vdd_cell)
		self.pre_decoder.place(self.gnd_cell , t , cell = self.pre_decoder.gnd_cell)



		#dxpos = self.mos_pair.find_boundary(layer = self.layer_map[self.Config.boundary_layer]).height()
		dxpos = self.mos_pair.find_dimensions(layer = self.layer_map[self.Config.boundary_layer])[0]
		mos_pair_pins = self.mos_pair_pin_map
		


		# simple_path(cell, layer, start, end , width):
		print(f"DEBUG:  dxpos = {dxpos}")
		# For now I'll move decoder manually
		#debug_leveling = (-2770,700)
		debug_leveling = (-2200,0)
		out_y_fix = 0
		xpos = xpos + debug_leveling[0]
		ypos = ypos + debug_leveling[1]

		# Extra routing for the decoder here. (Connect "out_n" with "out_p" at the end):pya
		simple_path(self.vdd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_p"].text.x ,ypos + mos_pair_pins["out_n"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x ,ypos + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])
		simple_path(self.gnd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_p"].text.x ,ypos + mos_pair_pins["out_n"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x ,ypos + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])

		#Connect decoder "out" to  "naddr" of pre-decoder
		simple_path(self.vdd_cell, self.layer_map["M1"], pya.Point(xpos  + mos_pair_pins["out_p"].text.x ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y  ), pya.Point( self.pre_decoder_pin_map["vdd"]["naddr"].text.x , ypos - out_y_fix + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])
		simple_path(self.gnd_cell, self.layer_map["M1"], pya.Point(xpos  + mos_pair_pins["out_p"].text.x ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y  ), pya.Point( self.pre_decoder_pin_map["vdd"]["naddr"].text.x , ypos - out_y_fix + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])
		

		# next line is for decoder OUT routing
		simple_path(self.vdd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_p"].text.x ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x - dxpos * (self.addr_n - 1 )  ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])
		simple_path(self.gnd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_p"].text.x ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x - dxpos * (self.addr_n - 1 )  ,ypos - out_y_fix + mos_pair_pins["out_p"].text.y ) , self.Config.width["min"])
		

		# Adding straps!

		# GND strap conect
		simple_path(self.gnd_cell, self.layer_map["M1"], pya.Point( self.pre_decoder_pin_map["gnd"]["naddr"].text.x ,ypos - out_y_fix + self.mos_pair_gnd_pins["gnd"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x - dxpos * (self.addr_n + 1 )  ,ypos - out_y_fix + self.mos_pair_gnd_pins["gnd"].text.y  ) , self.Config.width["strap"])
		simple_path(self.vdd_cell, self.layer_map["M1"], pya.Point( self.pre_decoder_pin_map["vdd"]["naddr"].text.x ,ypos - out_y_fix + self.mos_pair_vdd_pins["vdd"].text.y ), pya.Point(xpos +  mos_pair_pins["out_p"].text.x - dxpos * (self.addr_n + 1 )  ,ypos - out_y_fix + self.mos_pair_gnd_pins["vdd"].text.y  ) , self.Config.width["strap"])


		#nod_straps = [(self.layer_map["NP"], 460 , 0),(self.layer_map["M1"],200 , 1),(self.layer_map["OD"],200, 1)] #[(layer,width,lenth {0 = long } {1 = short} {2 = inverted long} , ),()]
		#nod_straps_implant = [(self.layer_map["NP"], 460 , 0),(self.layer_map["M1"],200 , 1),(self.layer_map["OD"],200, 1),(self.layer_map["PP"], 460, 2 , 100)]# , True, (PP, 460 , 200)
		#pod_tie_implant = MultipartPath( "pod_tie_implant",pod_pin_layer, pod_pin_size ,*pod_straps_implant)
		#nod_tie_implant = MultipartPath( "nod_tie_implant" , nod_pin_layer, nod_pin_size,*nod_straps_implant) 

		# Adding mos_pair cells itself!
		for i in range(self.addr_n):
			t = pya.Trans(xpos,ypos)
			# Placement to "t" point
			#self.mos_pair.place(self.vdd_cell , t )
			#self.mos_pair.place(self.gnd_cell , t )
			self.mos_pair_vdd.place(self.vdd_cell , t )
			self.mos_pair_gnd.place(self.gnd_cell , t )
			# Connect N mos to N mos
			xpos = xpos - dxpos
			if (i != self.addr_n - 1 ):
				simple_path(self.vdd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_n"].text.x ,ypos + mos_pair_pins["out_n"].text.y ), pya.Point(xpos +  mos_pair_pins["gnd"].text.x + dxpos  ,ypos + mos_pair_pins["out_n"].text.y ) , self.Config.width["min"])
				simple_path(self.gnd_cell, self.layer_map["M1"], pya.Point(xpos + mos_pair_pins["out_n"].text.x ,ypos + mos_pair_pins["out_n"].text.y ), pya.Point(xpos +  mos_pair_pins["gnd"].text.x + dxpos  ,ypos + mos_pair_pins["out_n"].text.y ) , self.Config.width["min"])
			if (i == self.addr_n - 1):
				pass # Add connection to gnd now

		# Add connection to ground:

		

		#self.mos_pair.find_boundary(layer = self.layer_map[self.Config.boundary_layer])

		self.cells.append(self.vdd_cell)
		self.cells.append(self.gnd_cell)

			


	def create_decoders_netlist(self):
		pass

	def import_predecoder_cells(self):
		#def read_module_gds(self,names):
		names = self.Config.pre_decoder
		cells = []
		for name in names:
			cells.append(self.fram_layout.read_cell_from_gds(name))
		return cells


	def init_pre_decoder(self):
		self.pre_decoder_cells = self.import_predecoder_cells()
		self.pre_decoder_name = self.Config.pre_decoder_name
		self.pre_decoder = Pre_Decoder(self.pre_decoder_cells , self.Config) # Старый варик с отдельным классом, пошел в корзину
		self.pre_decoder_pin_map = {"vdd":{},"gnd":{}}
		layers = self.layer_map
		mos_pair_pins = self.pre_decoder.find_pin_map(self.fram_layout.pins_layers)
		self.pre_decoder_pin_map["vdd"] = self.pre_decoder.find_cell_pin_map( self.pre_decoder.vdd_cell , self.fram_layout.pins_layers)
		self.pre_decoder_pin_map["gnd"] = self.pre_decoder.find_cell_pin_map( self.pre_decoder.gnd_cell , self.fram_layout.pins_layers)

	def y_size_check(self, y_size_array):
		""" Если ты это читаешь: знай, я бы хотел бы сделать код и понятнее,
		но к сожалению не уверен что его кто-то когда то будет читать (*((((
		Так что уж лучше написать побыстрее!!!"""
		pass

	def import_mos_pair(self):
		mos_pair_name = self.Config.mos_pair_name
		mos_pair_cell = self.fram_layout.read_cell_from_gds(mos_pair_name)
		#self.mos_pair_netlist = Netlist_Device(mos_pair_name,self.Config)
		self.mos_pair = Module(mos_pair_cell, self.Config ,is_basic_cell = True )
		self.fram_netlist.add_device(self.mos_pair.netlist_device)
		layers = self.layer_map
		self.mos_pair_pin_map = self.mos_pair.find_pin_map(self.fram_layout.pins_layers)

		mos_pair_vdd_name = f"{mos_pair_name}_vdd"
		mos_pair_gnd_name = f"{mos_pair_name}_gnd"
		mos_pair_vdd_cell = self.fram_layout.read_cell_from_gds(mos_pair_vdd_name)
		mos_pair_gnd_cell = self.fram_layout.read_cell_from_gds(mos_pair_gnd_name)
		self.mos_pair_vdd = Module(mos_pair_vdd_cell, self.Config ,is_basic_cell = True )
		self.mos_pair_gnd = Module(mos_pair_gnd_cell, self.Config ,is_basic_cell = True )

		self.mos_pair_gnd_pins = self.mos_pair_gnd.find_pin_map(self.fram_layout.pins_layers)
		self.mos_pair_vdd_pins = self.mos_pair_vdd.find_pin_map(self.fram_layout.pins_layers)
		


	def define_mosfets(self,mosfets):
		''' Get mosfets modules to work with '''
		self.nmos == None
		self.pmos == None
		for mosfet in mosfets:
			if mosfet.name == self.Config.nmos_name :
				self.nmos = mosfet
			elif mosfet.name == self.Config.pmos_name :
				self.pmos = mosfet
		if (self.nmos == None ) or (self.pmos == None ):
			self.Config.warning(getframeinfo(currentframe()))
			self.Config.debug_message(-1,"WRNG_MSG: No pmos or nmos defined in define_mosfets in decoder class.")

	def find_cell_boundary(self, cell ,layer= None): #default layer is PR Bndry
		k = 0
		if (layer == None):
			boundary = cell.bbox()
		if (layer != None):
			boundary = cell.bbox_per_layer(layer)
		return boundary

	def find_pin_map(self, layers): ## -------------- FIX!----------
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		h = 0
		pin_map = ({},{})
		for cell in self.cells:
			for layer in layers:
				for i in cell.each_shape(layer):
					if (i.is_text()):
						pin_map[h][i.text_string] = i
						#pin_map[i.text_string+'_layer'] 
						#print(i.text) - text object
						#print(i.text_string)# - text itself
			h = h + 1
		if (self.Config.debug_level > 2):
			for this_map in pin_map:
				print("Pins of map is:")
				print_pins(this_map)
		self.pin_map = pin_map
		return pin_map


	def place(self,target,t,mode = 0):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cells[mode].cell_index(),t)
		target.insert(istance)

	def unpack_design(self, design = None):
		if (design == None ):
			self.fram_layout = 	self.design.return_layout()
			self.fram_netlist = self.design.return_netlist()
		else:
			self.fram_layout = design.return_layout()
			self.fram_netlist = design.return_netlist()

	def update_design(self):
		design_dict = {"layout" : self.fram_layout , "netlist" : self.fram_netlist }
		self.design.update_design(**design_dict)

	def update_design_from(self, new_source):
		self.design = new_source.design
		self.unpack_design()


class Pre_Decoder:
	vdd_strap = 0
	gnd_strap = 1
	"""Часть пре декодера с усилителями и двумя  NAND gates. Решил вынести в отлельный класс по соображениям компактности кода."""
	def __init__(self, pre_decoder_cells , Config):
		self.Config = Config
		self.name = self.Config.pre_decoder_name
		self.netlist_device = Netlist_Device(self.name , self.Config)
		self.cells = pre_decoder_cells
		self.cells_in_cell = len(self.cells)
		self.get_strap_info()
		self.vdd_cell = self.cells[self.vdd_strap]
		self.gnd_cell = self.cells[self.gnd_strap]

	def get_strap_info(self):
		if ( self.cells[0].name == f"{self.name}_vdd" ) and ( self.cells[1].name == f"{self.name}_gnd" ):
			vdd_strap = 0
			gnd_strap = 1
		elif ( self.cells[1].name == f"{self.name}_vdd" ) and ( self.cells[0].name == f"{self.name}_gnd" ):
			vdd_strap = 1
			gnd_strap = 0
		else:
			self.Config.debug_message(-1," ===== > Could not get strap info! < =====\n")
			self.Config.warning(getframeinfo(currentframe()))

	def place(self,target,t, cell = None ,mode = 0):
		'''Add copy of this cell to {target} cell'''
		if (cell != None) :
			istance = pya.CellInstArray(cell.cell_index(),t)
			target.insert(istance)
		else:
			istance = pya.CellInstArray(self.cells[mode].cell_index(),t)
			target.insert(istance)

	def find_pin_map(self, layers): ## -------------- FIX!----------
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		h = 0
		pin_map = ({},{})
		for cell in self.cells:
			for layer in layers:
				for i in cell.each_shape(layer):
					if (i.is_text()):
						pin_map[h][i.text_string] = i
						#pin_map[i.text_string+'_layer'] 
						#print(i.text) - text object
						#print(i.text_string)# - text itself
			h = h + 1
		if (self.Config.debug_level > 2):
			for this_map in pin_map:
				print("Pins of map is:")
				print_pins(this_map)
		self.pin_map = pin_map
		return pin_map

	def find_cell_pin_map(self, cell , layers):
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		pin_map = {}
		for layer in layers:
			for i in cell.each_shape(layer):
			#print("===== + 1 =======")
				if (i.is_text()):
					pin_map[i.text_string] = i
					#pin_map[i.text_string+'_layer'] 
					#print(i.text) - text object
					#print(i.text_string)# - text itself
		self.pin_map = pin_map
		if (self.Config.debug_level > 2):
			print(f"Pins of {cell.name} map is:")
			print_pins(pin_map)
		return pin_map

