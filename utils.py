import sys
import os

import pya


""" Other usfull support functions avalible from all of the prjct"""

def print_pins(pin_map):
	for keys,val in pin_map.items():
		print(f'{keys} = {val}')


def check_os_content(name):
	if (os.path.isdir(name)):
		return 1
	else: 
		print("\n======Error!======\n There is no folder/file with the name \""  + name + "\"  terminating compilation. Add file and try again!")
		print(f"Try bash: mkdir {name}")
		sys.exit("\n \n Termination due to error reported above.")


def exit_on_false(state):
	if (state != True ):
		print("\n======Error!======\n")
		sys.exit("\n \n Termination due to error reported above.")

def sys_error():
		print("\n======Error!======\n")
		sys.exit("\n \n Termination due to error reported above.")




def simple_path(cell, layer, start, end , width):
	pth = pya.Path([start,end] , width)
	poly = pth.simple_polygon()
	cell.shapes(layer).insert(poly)


def find_pwr2(n,s):
	if (n % 2 == 0):
		s = s + 1
		return (find_pwr2(n/2,s))
	else:
		return s


def swich_mode(n):
	if (n == 0):
		n = 1
		return n
	if (n == 1):
		n = 0
		return n
	
def find_iterator(list, obj):
	iterator = None
	for i in range(len(list)):
		if list[i] ==  obj:
			iterator = i
	if (iterator == None ):
		print("No object found in list in  method find_iterator(list, obj).\nreturn None")
	return iterator

def view_gds(Config):
	if Config.view_gds == True:
		Config.debug_message(1,f"Opening klayout to check the result.")
		os.system(f"klayout ./gds_files/{Config.output_name}.gds")


def add_inst(self , n , module , terminals):
	module.place_inst( self.n , terminals )

	
	