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

		self.pmos25 = self.init_device( "pmos25" , [ ["L" , 0.28 ] , [ "W" , 0.400] ])
		self.nmos25 = self.init_device( "nmos25" , [ ["L" , 0.28 ] , [ "W" , 0.400] ])


	def init_device(self, name , params = None ):
		device_class  = pya.DeviceClass()
		device_class.name = name
		if ( params != None ):
			for param in params:
				new_param = pya.DeviceParameterDefinition()
				new_param.name = param[0]
				if ( len(param) != 1 ):
					new_param.default_value = param[1]
			device_class.parameter_definition(new_param)
		return device_class



	def write_netlist(self):
		netlist_writer = pya.NetlistSpiceWriter()
		self.netlist.write(f"./netlists/{self.Config.output_name}.sp",fram_netlist_writer)
		self.Config.debug_message(1,f"Extracted netlist to ./netlists/{self.Config.output_name}.sp")


