import pya
import os
import sys
import datetime
import random

import inspect

from config import Config
from cells import My_Cell
from layout import My_Layout
import technology


def check_os_content(name ):
	try:
		os.path.isfile(name)
	except Exception:
		print("there is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
		sys.exit("\n \n Terminated dueto error reported above.")
	else:
		print("Imported  \""  + name + "\" !")


'''

def read_cell_from_gds(self,name):

	cell = self.create_cell(name)

	self.check_os_content("./gds_files/" + name + ".gds")

	self.read("./gds_files/" + name + ".gds")
	for j in layout.top_cells():
		if ( j.name == name ):
			cell = j

	
	def find_pin_map(mcell, layer):
		pin_map = []
		for i in mcell.cell.each_shape(layer):
			print(i.is_text?)
			if (i.is_text?):
				pin_map.append(i)
		return pin_map
'''


layout = My_Layout()

layout.dbu = 1

#-----------------layers-----------------------------------

M1 =    layout.layer(31, 0)

M2 =    layout.layer(32, 0)
M3 =    layout.layer(33, 0)
M4 =    layout.layer(34, 0)
M5 =    layout.layer(35, 0)
PO =    layout.layer(17,0)
OD =    layout.layer(6,0)

NW =    layout.layer(3,0)
PP = 	layout.layer(25,0)
NP = 	layout.layer(26,0)
CO =    layout.layer(30,0)
OD_25 = layout.layer(41,0)
M1_pin = layout.layer(131,0)



s = My_Cell(layout.read_cell_from_gds("sense_amp"))

pinmap = s.find_pin_map(M1_pin)

layers = {}
layers["M1"] =    (31, 0)
layers["M2"] =    (32, 0)
layers["M3"] =    (33, 0)
layers["M4"] =    (34, 0)
layers["M5"] =    (35, 0)
layers["PO"] =    (17,0)
layers["OD"] =    (6,0)
layers["NW"] =    (3,0)
layers["PP"] = 	  (25,0)
layers["NP"] = 	  (26,0)
layers["CO"] =    (30,0)
layers["OD_25"] = (41,0)


for key , value in layers.items():
	print(value)


print("=====")
print(layout.layers())

print(layout.layer_dict["M1"])