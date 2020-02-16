import pya

import os




class My_Cell:
	'''My_Cell class represents a physical device with two represetitives as My_Cell.cell = layout representation and My_Cell.netlist as a netlist '''
	pin_map = {}
	"""docstring for ClassName"""
	def __init__(self, cell): #+ netlist
		self.cell = cell
		self.boundary_box = self.find_boundary()
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
					#pin_map[i.text_string+'_layer'] 
					#print(i.text) - text object
					#print(i.text_string)# - text itself
		return pin_map

	'''
	def print_pins(self):
		for keys,val in self.pin_map:
			print(f'{keys} = {val}')
	'''


	def find_boundary(self,layer= None): #default layer is PR Bndry
		if (layer == None):
			boundary = self.cell.bbox()
			return boundary
		if (layer != None):
			boundary = self.cell.bbox_per_layer(layer)
			return boundary
		#if(len(self.cell.each_shape(layer)) == 1):
		#	print("only one box")
		#	boundary = self.cell.each_shape(layer)[0]
		#else:
		#	print("more then one layer")

			
		#return boundary

	def find_dimensions(self, layer = None):
		if (layer == None):
			boundary = 0

		else:
			pass



class Memory_Cell(My_Cell):
	pass