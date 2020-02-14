import pya

import os



class My_Layout(pya.Layout):

	def __init__(self):
		pya.Layout.__init__(self)




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
		





	def check_os_content(self, name ):
		try:
			os.path.isfile(name)
		except Exception:
			print("there is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
			sys.exit("\n \n Termination due to error reported above.")
		else:
			pass