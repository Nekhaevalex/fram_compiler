import pya
import os
import sys
import datetime
import random

import inspect

from config import Config
from cells import *
from layout import *
import technology


import utils





'''
def print_pins(pin_map):
	for keys,val in pin_map.items():
		print(f'{keys} = {val}')


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








#for key , value in layers.items():
#	print(value)



print("=====")

#print(layout.layer_dict["M1"])
'''
print("    NW: ")


b = s.find_boundary(layout.layer_dict["M1"])
print("Box:")
print(b.bottom)
print(b.p1.x)
print(b.p1.y)




b = s.find_boundary()
print("Box:")
print(b.bottom)
print(b.p1.x)
print(b.p1.y)

print("=====")



'''

