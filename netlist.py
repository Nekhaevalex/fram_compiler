import pya

import os
import sys
from config import Config




class Fram_Netlist():
	"""docstring for Fram_Netlist"""
	def __init__(self, Config):
		self.Config = Config
		self.netlist = pya.Netlist()
		self.top_circuit = pya.Circuit()
		self.netlist.add(self.top_circuit)
		self.Config.debug_message(2,f'Initialize Netlist')

		self.pmos25 = self.init_device( "pmos25" , ["d","g","s","b"], [ ["L" , 0.28 ] , [ "W" , 0.400] ])
		self.nmos25 = self.init_device( "nmos25" , ["d","g","s","b"], [ ["L" , 0.28 ] , [ "W" , 0.400] ])


		test_device = self.top_circuit.create_device(self.pmos25 , "name")
		self.top_circuit.create_pin("new_pin")
		self.top_circuit.create_net("new_net")


	def init_device(self, name , terminals = None , params = None ):
		device_class  = pya.DeviceClass()
		self.netlist.add(device_class)
		device_class.name = name
		self.Config.debug_message(3 , f"Initialize device {name}")
		if ( params != None ):
			for param in params:
				new_param = pya.DeviceParameterDefinition()
				new_param.name = param[0]
				if ( len(param) != 1 ):
					self.Config.debug_message(3 ,  f"Param = {param[0]}, default_value = {param[1]}")
					new_param.default_value = param[1]
				print(f"id = {new_param.id()}")
				device_class.parameter_definition(new_param.id())

		if (terminals != None ):
			terminals_def = []
			for terminal in terminals:
				new_terminal = pya.DeviceClassTerminalDefinition()
				new_terminal.name = terminal
				terminals_def.append(new_terminal)
				device_class.terminal_definition(new_terminal.id())



		return device_class



	def write_netlist(self):
		netlist_writer = pya.NetlistSpiceWriter()
		self.netlist.write(f"./netlists/{self.Config.output_name}.sp",netlist_writer)
		self.Config.debug_message(1,f"Extracted netlist to ./netlists/{self.Config.output_name}.sp")


