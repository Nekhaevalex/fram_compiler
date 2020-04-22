import pya

import os
import sys
from config import Config
from utils import *



class Fram_Netlist():
	''' Main netlist class. The same as layout class. But netlist.'''
	devices = []
	subs = []
	lines = []
	type_name = "netlist"
	"""docstring for Fram_Netlist"""
	def __init__(self, Config):
		self.inst_n = 0
		self.Config = Config
		self.source = ""

	def write_netlist(self):
		path = f'./netlists/{self.Config.output_name}.sp'
		'''
		print("-----------------")
		for device in self.devices:
			print(device.name)
		'''
		with open(path ,'w') as output:
			output.write("* Declare basic devices\n")
			for device in self.devices:
				output.write(device.init)
			output.write("* Declare subcurcuits\n")
			for sub in self.subs:
				output.write(sub.init)
			output.write("* Declare instances\n")
			for line in self.lines:
				output.write(line)
		self.Config.debug_message(0,f'Spice netlist output created in "{path}" !')

	def init_sub(self, module ):
		sub = Netlist_Device(self, module.cell_name , self.Config)

	'''
	def add_sub(self, module , terminals ):
		self.source = self.source + module.netlist_device.place_device(self.inst_n ,terminals)
		self.inst_n += 1
	'''

	def add_device( self , device ):
		self.devices.append(device)

	def add_sub( self , sub ):
		self.subs.append(sub)

	def add_inst(self , module , terminals):
		self.lines.append(module.place_inst( self.inst_n , terminals ))
		self.inst_n += 1


class Netlist_Device():
	"""Netlist cuircuit which is read from .sp file initialy gived by user"""
	params = []
	pins = []

	def __init__(self, name , Config , default_params = None):
		self.name = name
		self.Config = Config
		self.default_params = default_params

		self.read_netlist_init_from_file()


		self.Config.debug_message( 3 , f"Created netlist device: {self.name}")

	def read_netlist_init_from_file(self):
		'''Initial read of file netlist and find it's terminals to self.pins '''
		pins = []
		
		with open(f'./netlists/{self.name}.sp','r') as source:
			self.init = source.read()
			source.seek(0)
			lines = source.readlines()

			if ( not self.state_presents(".ENDS", lines , self.name , mode = "0_pos")):
				print(f"Error. No '.ENDS' presented in file '{self.name}'")
				sys_error()
			if ( not self.state_presents(".SUBCKT", lines , self.name , mode = "0_pos")):
				print(f"Error. No '.ENDS' presented in file '{self.name}'")
				sys_error()	

			for line in lines:
				if ( (line[0] != "#") or  (line[0] != "*") or ( (line[0] != "/") and line[1] != "/" ) ):
					words = line.split()
					if ( len(words) > 0 ):
						if ( words[0].upper() == ".SUBCKT") and (len(words)>0) and words[1] == self.name :
							i = 2
							while (i < len(words)):
								pins.append(words[i])
								#print(f"Append pin {words[i]}")
								i += 1

			#print(f"Added netlist:\n {self.init}")
			#print(f"\nwith pins:")
			#print(pins)
			self.pins = pins


	def state_presents(self,state, lines , name , mode = "0_pos"):
		if ( mode == "0_pos" ):
			presents = False
			for line in lines:
				if ( (line[0] != "#") or  (line[0] != "*") or ( (line[0] != "/") and line[1] != "/" ) ):
					words = line.split()
					if (len(words)>0) and ( words[0].upper() == state):
						presents = True
		return presents

	def add_to_netlist(self,n,pins):
		"""
		f"I{n} ("
		for i in range(len(pins)):
			s = s+" "+pins[i]
		s = s+") "+self.name+'\n'
		return s
		"""
		pass

	def place_inst(self, n ,terminals ):
		""" Place an instance of device in format ( 
		mossfet.place_device([("d","net1"),("g","net2"),("s","net3"),("b",gnd)],[(L = 0.27),(W = 1)]]))"""
		src = f"X{n}"
		for terminal in terminals:
			src = f"{src} {terminal}"
		src = f"{src} {self.name}"
		src = f"{src}\n"
		return src

	def find_terminal(self,name):
		pass

	



class Curcuit():
	"""docstring for ClassName"""
	def __init__(self, name , Config , out_terminals , devices):
		self.name = name
		self.Config = Config
		self.out_terminals = out_terminals
		self.devices = devices
		self.init = self.init_sub(self.devices)

	def init_sub(self, devices):
		init_netlist = f".SUBCKT {self.name} "
		for terminal in self.out_terminals:
			init_netlist = f"{init_netlist} {terminal}"
		init_netlist = f"{init_netlist}\n"
		init_netlist = f"{init_netlist}\n.ENDS {self.name}\n"
		return init_netlist

	def place_inst(self, n ,terminals ):
		""" Place an instance of device in format ( 
		mossfet.place_device([("d","net1"),("g","net2"),("s","net3"),("b",gnd)],[(L = 0.27),(W = 1)]]))"""
		src = f"X{n}"
		for terminal in terminals:
			src = f"{src} {terminal}"
		src = f"{src} {self.name}"
		src = f"{src}\n"
		return src
	
	def add_sub():
		pass

	def add_device():
		pass




