import pya
import os
import sys
import datetime
import random

import mylayout

import technology
#import sys



class Fram():
	"""Main class contain layout (My_Layout) and netlist (Netlist) olcts"""
	def __init__(self, Config):
		self.Config = Config
		check_os_content(gds_files)
		check_os_content(netlists)

	def create_bitline(self, Memory_Cell , Config ):
		bitline = Bitline(self.layout, Memory_Cell , Config )





class Bitline:
	"""docstring for ClassName"""
	def __init__(self, layout ,Memory_Cell ,Config):
		layout.create_cell()


		xpos = 0

		ypos = 0

		for i in range(0,Config.num_words):
			t = pya.Trans(xpos,ypos)
			Memory_Cell.place(layout.topcell, t)
			xpos += Memory_Cell.height



	def create_gds(offset):
		pass
	def create_netlist():
		pass


		
class Memory_Core:
	"""docstring for ClassName"""
	def __init__(self, arg):
		pass
		


		


	



	
