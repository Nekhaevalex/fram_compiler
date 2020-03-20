import pya

import os

from utils import *
from netlist import *




class Module:
	'''Module class represents a physical device with two represetitives as Module.cell = layout representation and Module.netlist as a netlist '''
	pin_map = {}
	placement = "core"
	cells_in_cell = 1
	"""docstring for ClassName"""
	def __init__(self, cell , Config, is_basic_cell = False): #+ netlist
		self.Config = Config
		self.cell = cell
		self.cell_name = cell.name
		self.cells = []
		self.cells.append(cell)
		self.boundary_box = self.find_boundary()
		self.height = self.find_dimensions()[0]
		self.width = self.find_dimensions()[1]
		self.cell_name = self.cell.name
		if is_basic_cell:
			self.netlist_device = Netlist_Device(self.cell_name,self.Config)

		#self.netlist = netlist

	def place(self,target,t):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cell.cell_index(),t)
		target.insert(istance)

	def find_pin_map(self, layers):
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		pin_map = {}
		for layer in layers:
			for i in self.cell.each_shape(layer):
			#print("===== + 1 =======")
				if (i.is_text()):
					pin_map[i.text_string] = i
					#pin_map[i.text_string+'_layer'] 
					#print(i.text) - text object
					#print(i.text_string)# - text itself
		self.pin_map = pin_map
		if (self.Config.debug_level > 2):
			print("Pins of map is:")
			print_pins(pin_map)
		return pin_map



	def find_boundary(self,layer= None): #default layer is PR Bndry
		if (layer == None):
			boundary = self.cell.bbox()
			return boundary
		if (layer != None):
			boundary = self.cell.bbox_per_layer(layer)
			return boundary

	def find_cell_boundary(self , cell , layer = None):
		if (layer == None):
			boundary = cell.bbox()
			return boundary
		if (layer != None):
			boundary = cell.bbox_per_layer(layer)
			return boundary

			
		#return boundary

	def find_dimensions(self, layer = None):
		if (layer == None):
			boundary = self.find_boundary()
			dy = boundary.width()
			dx = boundary.height()
			return(dx,dy)
		else:
			boundary = self.find_boundary(layer)
			boundary = self.find_boundary()
			dx = boundary.width()
			dy = boundary.height()
			return(dx,dy)

	def get_cell_name(self):
		pass




class Memory_Cell(Module):
	pass





class Side_Module():
	cell_name = "sense_amp"
	cells_in_cell = 2
	placement = "bottom"
	pin_map = ({},{})
	connect_to = 'bl'
	connect_with = 'in'
	"""docstring for ClassName"""
	def __init__(self,cells,Config):
		self.Config = Config
		self.cells = cells
		self.boundary_box = ()
		self.netlist_device = Netlist_Device(self.cell_name,self.Config)
		Config.debug_message(2, f"Created Sense_Amp , with start cell {cells[0].name}")

	def find_cell_boundary(self, cell ,layer= None): #default layer is PR Bndry
		k = 0
		if (layer == None):
			boundary = cell.bbox()
		if (layer != None):
			boundary = cell.bbox_per_layer(layer)
		return boundary

	def find_pin_map(self, layers): ## -------------- FIX!----------
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		h = 0
		pin_map = ({},{})
		for cell in self.cells:
			for layer in layers:
				for i in cell.each_shape(layer):
					if (i.is_text()):
						pin_map[h][i.text_string] = i
						#pin_map[i.text_string+'_layer'] 
						#print(i.text) - text object
						#print(i.text_string)# - text itself
			h = h + 1
		if (self.Config.debug_level > 2):
			for this_map in pin_map:
				print("Pins of map is:")
				print_pins(this_map)
		self.pin_map = pin_map
		return pin_map


	def place(self,target,t,mode = 0):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cells[mode].cell_index(),t)
		target.insert(istance)



