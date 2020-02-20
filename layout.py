import pya

import os
import sys



class My_Layout(pya.Layout):	 
	'''My layout is a child klayout layout class , but have some extended functionality to use 
	in my design. '''
	layer_dict = {} # name layer and layers are reserved as methods of klayout
	dbu = 1
	def __init__(self):
		pya.Layout.__init__(self)
		self.init_tec()
		self.topcell = self.create_cell("TOP")







	def create_mycell(self,cell):
		mycell = My_Cell(cell)
		return mycell




	def read_cell_from_gds(self,name):
		'''Reads gds file and return topcell with name = (name)'''

		cell = self.create_cell(name)

		self.if_file_exists("./gds_files/" + name + ".gds")

		self.read("./gds_files/" + name + ".gds")
		for j in self.top_cells():
			if ( j.name == name ):
				cell = j
				return j


	def read_dual_cell_from_gds(self,names):
		
		cell[0] = self.create_cell(names[0])
		cell[1] = self.create_cell(names[1])


		self.if_file_exists("./gds_files/" + names[0] + ".gds")
		self.if_file_exists("./gds_files/" + names[1] + ".gds")
		n = 0
		for name in names:
			self.read("./gds_files/" + name + ".gds")
			for j in self.top_cells():
				if (j.name == name):
					cell[n] = j
					n = n + 1



	def init_tec(self):
		try:
			from technology import Technology
			self.technology = Technology()
			for layer_key ,value in self.technology.layers.items():
					self.layer_dict[layer_key] = self.layer(value[0],value[1])

		except:
			print("\n======Error in layout.py !======\n \"Technology\" file not found! Maybe you miss technology.py or error in  init_tec() method")
			sys.exit("\n \n Termination due to error reported above!")


	def if_file_exists(self,name):
		if (os.path.isfile(name)):
			return 1
		else: 
			print("\n======Error!======\n There is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
			print(f"Try add: {name}")
			sys.exit("\n \n Termination due to error reported above.")

	def add_big_box(self,layer,coords):
		pass


