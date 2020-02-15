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






	def create_mycell(self,cell):
		mycell = My_Cell(cell)
		return My_Cell




	def read_cell_from_gds(self,name):

		cell = self.create_cell(name)

		self.check_os_content("./gds_files/" + name + ".gds")

		self.read("./gds_files/" + name + ".gds")
		for j in self.top_cells():
			if ( j.name == name ):
				cell = j
				return j
		



	def init_tec(self):
		try:
			from technology import Technology
			self.technology = Technology()
			self.layer_dict = self.technology.layers  # copy dict to have less troubles acsessing it!
		except:
			print("\n======Error!======\n \"Technology\" file not found! Maybe you miss technology.py")
			sys.exit("\n \n Termination due to error reported above!")





	def check_os_content(self, name ):
		try:
			os.path.isfile(name)
		except Exception:
			print("\n======Error!======\n There is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
			sys.exit("\n \n Termination due to error reported above.")
		else:
			pass