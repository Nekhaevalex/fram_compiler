import sys
import os

import pya

def print_pins(pin_map):
	for keys,val in pin_map:
		print(f'{keys} = {val}')


def check_os_content(name):
	if (os.path.isdir(name)):
		return 1
	else: 
		print("\n======Error!======\n There is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
		print(f"Try bash: mkdir {name}")
		sys.exit("\n \n Termination due to error reported above.")


def simple_path(cell, layer, start, end , width):
	pth = pya.Path([start,end] , width)
	poly = pth.simple_polygon()
	cell.shapes(layer).insert(poly)