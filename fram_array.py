import pya
import os
import sys
import datetime
import random
from utils import *
from cells import *

from layout import My_Layout
from config import Config


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


		self.create_bitline(self.memory_cell,Config) # Create bitline class
		self.create_array_core(self.bitline,Config) # Create array of bitlines


		self.gds_output(Config) # Make output of gds

		


	def create_bitline(self, Memory_Cell , Config ):
		self.bitline = Bitline( self.fram_layout, Memory_Cell , Config )

	def create_array_core(self,Bitline,Config):
		self.array_core = Array_Core( self.fram_layout, Bitline, Config)
		self.core_offset = (self.array_core.x_offset,self.array_core.y_offset)


	def gds_output(self,Config):
		output_path = "./gds_files/"+ Config.output_name+".gds"
		self.fram_layout.write(output_path)
		print(f'Wow! GDS output file is now created in "{output_path}" !')
		return output_path






class Bitline:
	"""Vertical memory  cells array"""
	cell_name = "bitline"



	def __init__(self, layout ,Memory_Cell ,Config):
		self.Config =Config
		self.bitline_cell = My_Cell(layout.create_cell(self.cell_name))
		self.memory_cell = Memory_Cell
		self.layout = layout
		self.layer_map = layout.layer_dict


		xpos = 0

		ypos = 0

		for i in range(0,Config.num_words):
			t = pya.Trans(xpos,ypos)
			Memory_Cell.place(self.bitline_cell.cell, t)
			ypos += Memory_Cell.height

		
		self.y_offset = ypos
		self.bitline_routing()


	def create_gds(self,layout,Memory_Cell,Config):
		pass
	def create_netlist(self):
		pass
	def add_bitline_instance(self,t):
		self.bitline_cell.place(t)

	def bitline_routing(self):
		self.bitline_pinmap = self.memory_cell.find_pin_map([self.layer_map["M1_pin"],self.layer_map["M2_pin"]])

		xpos = self.bitline_pinmap["bl"].text.x
		ypos = self.bitline_pinmap["bl"].text.y

		simple_path(self.bitline_cell.cell, self.layer_map["M1"], pya.Point(xpos,ypos), pya.Point(xpos,self.y_offset) , self.Config.bl_width)
		
class Array_Core:
	"""Multiplying bitlines class"""
	cell_name = "core"
	def __init__(self, layout, Bitline , Config):
		self.layout = layout
		self.array_core_cell = My_Cell(layout.create_cell(self.cell_name))
		self.memory_cell = Bitline.memory_cell
		self.layer_map = self.layout.layer_dict	

		xpos = 0

		ypos = 0

		for i in range (0,Config.word_size):
			t = pya.Trans(xpos,ypos)
			Bitline.bitline_cell.place(self.array_core_cell.cell,t)
			xpos += self.memory_cell.width

		self.x_offset = xpos
		self.y_offset = Bitline.y_offset
		print(f'created core with coordinates as box (0,0) to ({self.x_offset},{self.y_offset})')



	def create_core_gds(self,layout,Bitline,Config):
		pass

	def create_netlist():
		pass
		




# ===================== CODE ============


config = Config()
fram = Fram(config)


		


	



	
