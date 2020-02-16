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
		self.Config = Config
		self.fram_layout = My_Layout()
		check_os_content("gds_files")
		check_os_content("netlists")
		

		memory_cell = Memory_Cell(self.fram_layout.read_cell_from_gds("memory_cell"))


		self.create_bitline(memory_cell,Config)



	def create_bitline(self, Memory_Cell , Config ):
		self.bitline = Bitline(self.fram_layout, Memory_Cell , Config )







class Bitline:
	"""Vertical cells"""
	cell_name = "bitline"

	def __init__(self, layout ,Memory_Cell ,Config):
		self.bitline_cell = My_Cell(layout.create_cell(self.cell_name))


		xpos = 0

		ypos = 0

		for i in range(0,Config.num_words):
			t = pya.Trans(xpos,ypos)
			Memory_Cell.place(self.bitline_cell.cell, t)
			xpos += Memory_Cell.height




	def create_gds(self,layout,Memory_Cell,Config):
		pass
	def create_netlist(self):
		pass

	def add_bitline_instance(self,t):
		self.bitline_cell.place(t)

		
		
class Array_Core:
	"""Multiplying bitlines"""
	def __init__(self, Bitline , Config):
		pass
		




# ===================== CODE ============


config = Config()
fram = Fram(config)


		


	



	
