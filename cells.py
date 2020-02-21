import pya

import os




class Module:
	'''Module class represents a physical device with two represetitives as Module.cell = layout representation and Module.netlist as a netlist '''
	pin_map = {}
	placement = "core"
	"""docstring for ClassName"""
	def __init__(self, cell , Config): #+ netlist
		self.cell = cell
		self.boundary_box = self.find_boundary()
		self.height = self.find_dimensions()[0]
		self.width = self.find_dimensions()[1]
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
		return pin_map



	def find_boundary(self,layer= None): #default layer is PR Bndry
		if (layer == None):
			boundary = self.cell.bbox()
			return boundary
		if (layer != None):
			boundary = self.cell.bbox_per_layer(layer)
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





class Sense_Amp():
	cell_name = "sense_amp"
	placement = "bottom"
	"""docstring for ClassName"""
	def __init__(self,cells,Config):
		self.cells = cells
		self.boundary_box = ()
		Config.debug_message(2, f"Created Sense_Amp , with start cell {cells[0].name}")

	def find_boundary(self,layer= None): #default layer is PR Bndry
		k = 0
		for cell in cells:
			if (layer == None):
				boundary[k] = self.cell.bbox()
			if (layer != None):
				boundary[k] = self.cell.bbox_per_layer(layer)
		return boundary

	def find_pin_map(self, layers): ## -------------- FIX!----------
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		h = 0
		pin_map = ({},{})
		for cell in cells:
			for layer in layers:
				for i in self.cell[h].each_shape(layer):
				#print("===== + 1 =======")
					if (i.is_text()):
						pin_map[h][i.text_string] = i
						#pin_map[i.text_string+'_layer'] 
						#print(i.text) - text object
						#print(i.text_string)# - text itself
		self.pin_map = pin_map
		return pin_map


	def place(self,target,t,mode = 0):
		'''Add copy of this cell to {target} cell'''
		istance = pya.CellInstArray(self.cells[mode].cell_index(),t)
		target.insert(istance)
