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


layout = My_Layout()

layout.dbu = 1



s = My_Cell(layout.read_cell_from_gds("sense_amp"))

pinmap = s.find_pin_map([layout.layer_dict["M1_pin"]])

print(f' Type of pinmap is {type(pinmap)}')







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

print("=====")

for key,value in layout.layer_dict.items():
	print(f"{key} = {value}")
print("==========")


m = My_Cell(layout.read_cell_from_gds("memory_cell"))
pinmap = m.find_pin_map([layout.layer_dict["M1_pin"],layout.layer_dict["M2_pin"]])

for key,value in pinmap.items():
	print(f"{key} = {value}")
