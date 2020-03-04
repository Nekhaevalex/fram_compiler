import pya

import os
import sys
from config import Config




class Fram_Netlist():
	"""docstring for Fram_Netlist"""
	def __init__(self, Config):
		self.Config = Config
		
	def write_netlist(self):
		with open(f'./netlists/{self.Config.output_name}.sp','w') as output:
			output.write(self.source)


class Netlist_Device():
	params = []
	"""docstring for ClassName"""
	def __init__(self, name  , Config):
		self.name = name
		self.Config = Config

	def read_netlist_init_from_file(self):
		with open(f'./netlists/{self.name}.sp','r') as source:
			self.init = source.read()
			print(f"Added netlist: {self.init}")

	def add_to_netlist(self)
		pass



class Curcuit(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg
		
		
		


