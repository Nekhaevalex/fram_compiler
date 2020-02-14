import pya

import os




class My_Cell:
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
				print("+ text")
				print(i.text)
				print(i.text_string)
		return pin_map


class Memory_Cell(My_Cell):
	pass