import pya

import os




class My_Cell:
	'''My_Cell class represents a physical device with two represetitives as My_Cell.cell = layout representation and My_Cell.netlist as a netlist '''
	pin_map = []
	"""docstring for ClassName"""
	def __init__(self, cell): #+ netlist
		self.cell = cell
		#self.netlist = netlist


	def place(self,target,t):
		istance = pya.CellInstArray(self.cell.cell_index,t)
		target.insert(insert)
		

	def find_pin_map(self, layer):
		pin_map = []
		for i in self.cell.each_shape(layer):
		#print("===== + 1 =======")
			if (i.is_text()):
				pin_map.append(i)
				#print(i.text) - text object
				#print(i.text_string) - text itself
		return pin_map


	def find_boundary(self,layer=(108,0)): #default layer is PR Bndry
		pass




class Memory_Cell(My_Cell):
	pass