import pya

import os




class My_Cell:
	'''My_Cell class represents a physical device with two represetitives as My_Cell.cell = layout representation and My_Cell.netlist as a netlist '''
	pin_map = {}
	"""docstring for ClassName"""
	def __init__(self, cell): #+ netlist
		self.cell = cell
		self.pin_map = self.find_pin_map
		#self.netlist = netlist


	def place(self,target,t):
		istance = pya.CellInstArray(self.cell.cell_index,t)
		target.insert(insert)
		

	def find_pin_map(self, layers):
		'''create dictionary with text klayout.Text objects and its klayout.Point s'''
		pin_map = {}
		for layer in layers:
			for i in self.cell.each_shape(layer):
			#print("===== + 1 =======")
				if (i.is_text()):
					pin_map[i.text_string] = i
					#print(i.text) - text object
					#print(i.text_string) - text itself
		return pin_map


	def find_boundary(self,layer=(0,0)): #default layer is PR Bndry
		if (layer == (0,0)):
			boundary = self.cell.bbox()
			return boundary
		if (layer != (0,0)):
			boundary = self.cell.bbox_per_layer(layer)
			return boundary
		#if(len(self.cell.each_shape(layer)) == 1):
		#	print("only one box")
		#	boundary = self.cell.each_shape(layer)[0]
		#else:
		#	print("more then one layer")

			
		#return boundary




class Memory_Cell(My_Cell):
	pass