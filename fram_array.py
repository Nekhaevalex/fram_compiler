import pya
import os
import sys
import datetime
import random
from utils import *
from cells import *

from layout import My_Layout
from config import Config

# Debug
from inspect import currentframe, getframeinfo


import technology
#import sys


class Fram():
	"""Main class contain layout (My_Layout) and netlist (Netlist) objcts. Fram itself 
	consists of modules, module is a layout_cell and netlist curciut representation and 
	it's methods"""
	def __init__(self, Config):
		'''Main magic happens here!'''
		self.Config = Config
		self.create_layout()
		self.init_netlist()
		check_os_content("gds_files")
		check_os_content("netlists")
		

		#self.memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds("memory_cell"))
		self.memory_cell = self.read_memory_cell()

		
		#self.sense_amp = Sense_Amp(sense_amp_cells,Config)
		self.sense_amp = self.read_sense_amp_cell()

		self.create_bitline(self.memory_cell,Config) # Create bitline class
		self.create_array_core(self.bitline , [self.memory_cell , self.sense_amp ], Config) # Create array of bitlines


		self.gds_output() # Make output of gds
		

	def read_memory_cell(self):
		memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds(self.Config.fram_bitcell_name) , self.Config)
		return memory_cell


	def create_layout(self):
		self.fram_layout = My_Layout(Config)
		self.pins_layers = self.fram_layout.pins_layers

	def read_sense_amp_cell(self):
		sense_name_1 = self.Config.sense_amp_gnd_name
		sense_name_2 = self.Config.sense_amp_vdd_name
		sense_amp_cells = ( self.fram_layout.read_cell_from_gds(sense_name_1) , self.fram_layout.read_cell_from_gds(sense_name_2) )
		sense_amp = Sense_Amp(sense_amp_cells,self.Config)
		return sense_amp



	def create_bitline(self, Memory_Cell , Config ):
		self.bitline = Bitline( self.fram_layout, self.fram_netlist ,  Memory_Cell , Config )

	def create_array_core(self,Bitline,cells,Config):
		self.array_core = Array_Core( self.fram_layout, self.fram_netlist , Bitline, cells ,  Config)
		self.core_offset = (self.array_core.x_offset,self.array_core.y_offset)
		Config.debug_message(0,f'Created array of cells!')


	def gds_output(self):
		output_path = "./gds_files/"+ self.Config.output_name+".gds"
		self.fram_layout.write(output_path)
		self.Config.debug_message(0,f'Wow! GDS output file is now created in "{output_path}" !')
		return output_path

	def init_netlist(self):
		self.fram_netlist = pya.Netlist()
		self.top_netlist_circuit = pya.Circuit()
		self.fram_netlist.add(self.top_netlist_circuit)
		self.Config.debug_message(2,f'Initialize Netlist')



	def write_netlist(self):
		fram_netlist_writer = pya.NetlistSpiceWriter()
		self.fram_netlist.write(f"./netlists/{self.Config.output_name}.sp",fram_netlist_writer)
		self.Config.debug_message(1,f"Extracted netlist to ./netlists/{self.Config.output_name}.sp")

class Bitline:
	"""Vertical memory  cells array module"""
	cell_name = "bitline"



	def __init__(self, layout, netlist ,Memory_Cell ,Config):
		self.Config =Config
		self.bitline_cell = Module(layout.create_cell(self.cell_name),Config)
		self.memory_cell = Memory_Cell
		self.Y_step = Memory_Cell.height
		self.layout = layout
		self.layer_map = layout.layer_dict

		self.create_gds(layout,Memory_Cell,Config)





	def create_gds(self,layout,Memory_Cell,Config):
		xpos = 0

		ypos = 0

		for i in range(0,Config.num_words):
			t = pya.Trans(xpos,ypos)
			Memory_Cell.place(self.bitline_cell.cell, t)
			#ypos += Memory_Cell.height
			#text = pya.Text(f"here is the connection# {i}", xpos , ypos)
			ypos += self.Y_step

			#self.bitline_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)


		
		self.y_offset = ypos
		self.bitline_routing()
	def create_netlist(self):
		pass
	def add_bitline_instance(self,t):
		self.bitline_cell.place(t)

	def bitline_routing(self):
		self.bitline_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"]])

		xpos = self.bitline_pinmap["bl"].text.x 
		ypos = self.bitline_pinmap["bl"].text.y
		self.line_coords = ((xpos,ypos) , (xpos, self.y_offset) )
		simple_path(self.bitline_cell.cell, self.layer_map["M1"], pya.Point(xpos,ypos), pya.Point(xpos,self.y_offset) , self.Config.bl_width)



	def create_subskct():
		pass


class Array_Core:
	"""Multiplying bitlines class"""
	cell_name = "core"
	def __init__(self, layout, netlist , Bitline, cells , Config):
		self.layout = layout
		self.Config = Config
		self.cells = cells
		self.netlist = netlist
		self.memory_cell = Bitline.memory_cell
		self.X_step = self.define_X_step(cells)
		#self.Y_step = self.define_Y_step(cells)
		self.Y_step = self.memory_cell.height


		self.bitline = Bitline
		self.array_core_cell = Module(layout.create_cell(self.cell_name) , Config)
		self.memory_cell = Bitline.memory_cell
		self.layer_map = self.layout.layer_dict

		self.sense_amp = self.find_cell_in_cells("sense_amp",cells)
		

		#self.X_step = self.memory_cell.width
		
		self.create_core_gds(layout,Bitline,Config)






	def define_X_step(self,modules):
		dx = []
		for module in modules:
			for cell in module.cells:
				boundary = module.find_cell_boundary(cell)
				dx.append(boundary.width())
				self.Config.debug_message(4,f'dx size of cell {cell.name} is {boundary.width()}')
		X_step = max(dx)
		self.Config.debug_message(3,f'Defines X - size  of {X_step}. By comparing of list {dx}')
		return X_step
				


	def define_Y_step(self,modules):
		dy = []
		for module in modules:
			for cell in module.cells:
				boundary = module.find_cell_boundary(cell)
				dy.append(boundary.width())
		Y_step = max(dy)
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

	def create_core_gds(self,layout,Bitline,Config):




		xpos = 0

		ypos = 0

		for i in range (0,Config.word_size):
			t = pya.Trans(xpos,ypos)
			Bitline.bitline_cell.place(self.array_core_cell.cell,t)
			xpos += self.X_step




		self.x_offset = xpos
		self.y_offset = Bitline.y_offset
		self.add_markers()
		self.write_line_routing()
		Config.debug_message(0,f'Created core (only memory cells) with coordinates as box (0,0) to ({self.x_offset},{self.y_offset})')
		self.add_side_module(self.sense_amp)

	def create_netlist():
		pass
		
	def write_line_routing(self):
		self.memory_cell_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"]])
		
		xpos = self.memory_cell_pinmap["wn"].text.x
		ypos = self.memory_cell_pinmap["wn"].text.y
		for i in range (0,self.Config.word_size):
			simple_path(self.array_core_cell.cell, self.layer_map["M2"], pya.Point(xpos,ypos), pya.Point(self.x_offset,ypos) , self.Config.bl_width)
			ypos = ypos + self.Y_step
		if (self.Config.debug_level > 1 ):
			print(f'Complited routing of bitline with end point as ({xpos} , {ypos})')




	def add_side_module (self, module):
		self.add_module_layout(module)


		'''
		M1_pin = self.layer_map["M1_pin"]
		bl_pinmap = self.array_core_cell.find_pin_map([M1_pin])
		print_pins(bl_pinmap) # remove
		'''

		

	def add_module_layout(self, module):
		layer_pins = [ self.layer_map["M1_pin"] , self.layer_map["M2_pin"] ]
		module.pin_map = module.find_pin_map(layer_pins)


		if ( module.placement == "bottom" ):
			n = 0
			xpos1 = self.bl_end_markers[0].x - module.pin_map[0]["in"].text.x
			xpos2 = self.bl_end_markers[0].x - module.pin_map[1]["in"].text.x
			print("in pin x = "+str(module.pin_map[n]["in"].text.x)+" ")
			ypos = -1000
			for i in  range(0, self.Config.word_size):
				if (n == 0):
					t = pya.Trans(xpos1,ypos)
					module.place(self.array_core_cell.cell, t , mode =n)
					
				if (n == 1):
					t = pya.Trans(xpos2,ypos)
					module.place(self.array_core_cell.cell, t , mode =n)
				print(f"n = {n}")
				n = swich_mode(n)
				xpos1 = xpos1 + self.X_step
				xpos2 = xpos2 + self.X_step
		else:
			self.Config.debug_message(-1,f'========== WARNING ========= \n ')
			self.Config.warning(getframeinfo(currentframe()))




	def add_markers(self):
		''' ===  Add some text to the tips of the lines and bitlines  ===    '''
		bl_end_markers = []
		bl_begin_markers = []
		xpos = self.bitline.line_coords[1][0]
		ypos = self.bitline.line_coords[1][1]
		for i in range(0, self.Config.word_size):
			if ( self.Config.marker_as_text == True ):
				text = pya.Text(f"end_of_BL{i}", xpos , ypos)
				#print(f'x = {xpos} , y = {ypos}') #Debug
				self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			bl_end_markers.append(pya.Point(xpos,ypos))
			xpos = xpos + self.X_step

		xpos = self.bitline.line_coords[0][0]
		ypos = self.bitline.line_coords[0][1]
		for i in range(0, self.Config.word_size):
			if ( self.Config.marker_as_text ):
				text = pya.Text(f"begin_of_BL{i}", xpos , ypos)
				#print(f'x = {xpos} , y = {ypos}') #Debug
				self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			bl_begin_markers.append(pya.Point(xpos,ypos))
			xpos = xpos + self.X_step
		self.bl_begin_markers = bl_begin_markers
		self.bl_end_markers = bl_end_markers





# ===================== CODE HERE! ============


config = Config()
fram = Fram(config)


		


	



	
