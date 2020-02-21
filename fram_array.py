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
	"""Main class contain layout (My_Layout) and netlist (Netlist) olcts"""
	def __init__(self, Config):
		'''Main magic happens here!'''
		self.Config = Config
		self.fram_layout = My_Layout() # main layout!
		check_os_content("gds_files")
		check_os_content("netlists")
		

		self.memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds("memory_cell"))
		sense_amp_cells = ( self.fram_layout.read_cell_from_gds("sense_amp_gnd") , self.fram_layout.read_cell_from_gds("sense_amp_vdd") )
		self.sense_amp = Sense_Amp(sense_amp_cells)

		self.create_bitline(self.memory_cell,Config) # Create bitline class
		self.create_array_core(self.bitline , [self.sense_amp], Config) # Create array of bitlines


		self.gds_output(Config) # Make output of gds

		

	def read_memory_cell(self,name):
		memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds(self.Config.fram_bitcell_name))
		return memory_cell

	def read_sense_amp_cell(self,name):
		pass

	def create_bitline(self, Memory_Cell , Config ):
		self.bitline = Bitline( self.fram_layout, Memory_Cell , Config )

	def create_array_core(self,Bitline,cells,Config):
		self.array_core = Array_Core( self.fram_layout, Bitline, cells ,  Config)
		self.core_offset = (self.array_core.x_offset,self.array_core.y_offset)
		Config.debug_message(0,f'Created array of cells!')


	def gds_output(self,Config):
		output_path = "./gds_files/"+ Config.output_name+".gds"
		self.fram_layout.write(output_path)
		Config.debug_message(0,f'Wow! GDS output file is now created in "{output_path}" !')
		return output_path






class Bitline:
	"""Vertical memory  cells array"""
	cell_name = "bitline"



	def __init__(self, layout ,Memory_Cell ,Config):
		self.Config =Config
		self.bitline_cell = My_Cell(layout.create_cell(self.cell_name))
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




class Array_Core:
	"""Multiplying bitlines class"""
	cell_name = "core"
	def __init__(self, layout, Bitline, cells , Config):
		self.layout = layout
		self.Config = Config
		self.bitline = Bitline
		self.array_core_cell = My_Cell(layout.create_cell(self.cell_name))
		self.memory_cell = Bitline.memory_cell
		self.layer_map = self.layout.layer_dict

		self.sense_amp = self.find_cell_in_cells("sense_amp",cells)

		self.X_step = self.memory_cell.width
		self.Y_step = self.memory_cell.height
		self.create_core_gds(layout,Bitline,Config)




	def find_cell_in_cells(self,name,cells):
		for cell in cells:
			if (cell.cell_name == "name"):
				new_cell = cell
				self.Config.debug_message(2,f'Cell  {name} added to core cells list.')
				return new_cell
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
		Config.debug_message(0,f'Created core with coordinates as box (0,0) to ({self.x_offset},{self.y_offset})')


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


	def add_markers(self):
		''' ===  Add some text to the tips of the lines and bitlines  ===    '''
		xpos = self.bitline.line_coords[1][0]
		ypos = self.bitline.line_coords[1][1]
		for i in range(0, self.Config.word_size):
			text = pya.Text(f"end_of_BL{i}", xpos , ypos)
			#print(f'x = {xpos} , y = {ypos}') #Debug
			self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			xpos = xpos + self.X_step

		xpos = self.bitline.line_coords[0][0]
		ypos = self.bitline.line_coords[0][1]
		for i in range(0, self.Config.word_size):
			text = pya.Text(f"begin_of_BL{i}", xpos , ypos)
			#print(f'x = {xpos} , y = {ypos}') #Debug
			self.array_core_cell.cell.shapes(self.layer_map["M1_pin"]).insert(text)
			xpos = xpos + self.X_step



# ===================== CODE ============


config = Config()
fram = Fram(config)


		


	



	
