import pya

import os
import sys
from config import Config




class Fram_Netlist():
	"""docstring for Fram_Netlist"""
	def __init__(self, Config):
		self.Config = Config
		self.source = ""


	def write_netlist(self):
		with open(f'./netlists/{self.Config.output_name}.sp','w') as output:
			output.write(self.source)

	def init_sub(self, module ):
		sub = Netlist_Device(self, module.cell_name , self.Config)

	def add_sub(self, sub , terminals ):
		source = source + sub.add_to_netlist( terminals )


class Netlist_Device():
	params = []
	pins = []
	"""docstring for ClassName"""
	def __init__(self, name , Config):
		self.name = name
		self.Config = Config

		self.read_netlist_init_from_file()




	def read_netlist_init_from_file(self):
		pins = []
		with open(f'./netlists/{self.name}.sp','r') as source:
			self.init = source.read()
			source.seek(0)
			lines = source.readlines()
			for  line in lines:
				print(line)
				if ( (line[0] != "#") or  (line[0] != "*") or ( (line[0] != "/") and line[1] != "/" ) ):
					words = line.split()
					if ( len(words[0]) > 0 ):
						if ( words[0] == ".SUBCKT") and (len(words)>0) :
							print(words[0])
							i = 1
							while (i < len(words)):
								pins.append(words[i])
								i += 1

			print(f"Added netlist: {self.init}")
			print(f"with pins:")
			print(pins)
			self.pins = pins

	def add_to_netlist(self,n,pins):
		"""
		f"I{n} ("
		for i in range(len(pins)):
			s = s+" "+pins[i]
		s = s+") "+self.name+'\n'
		return s
		"""
		pass

class Curcuit(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg


