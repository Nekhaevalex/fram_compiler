import pya
import os
import datetime
import random



from array_config import *



class My_Cell():
	transistor_lenth = float(nmos_length)/1000
	transistor_width = float(nmos_width)/1000
	dimentions = (10,10)


	def __init__ (self, cell):
		self.cell = cell
		self.cell_index = cell.cell_index()


	

	def place(self,cell,t):
		cell_array = pya.CellInstArray(self.cell_index,t)
		cell.insert(cell_array)

	def add_to_netlist(self, n_inst , pins, param):
		s = "I"+str(n_inst)
		s = " ("
		for i in pins:
			s = s + i + " "
		s = " ) "
		if (len(param) > 0):
			for i in range(param):
				s = s + param[i][0] + "=" + param[i][1]
			s += self.cell.name


		return s
	




class Mos(My_Cell):
	"""docstring for ClassName"""



	def __init__ (self, cell, drain, gate, source, cell_index, width, length):
		self.cell = cell
		self.drain = drain
		self.gate = gate
		self.source = source
		self.width = width
		self.length = length
		self.cell_index = cell_index
		self.w = float(width)/1000
		self.l = float(length)/1000
#	def add_to_netlist (w,l, netlist):
		
	def add_to_netlist(self,n,d,g,s,b, w , l):
		#print("transistor width is: "+str(self.width))
		#print("transistor width is: "+str(self.w))
		s = "M"+str(n)+" ("+d+" "+g+" "+s+" "+b+" ) "+self.cell.name+" w="+str(w)+" l="+str(l)+"\n"
		return s 



class Memory_cell(My_Cell):
	"""docstring for ClassName"""

	p00 = 1e-14

	def __init__ (self, cell, bl_pin, gnd_pin, wn_pin , size ):
		self.cell = cell
		self.cell_index = cell.cell_index()
		self.bl_pin = bl_pin
		self.gnd_pin = gnd_pin
		self.wn_pin = wn_pin
		self.size = size


	def sbskt_def(self, n_mos, bl , wl , pl , gnd  ):

		s = "//Subsercuit   "+ self.cell.name

		s = s + "\nsubckt "+self.cell.name+' '+bl+' '+wl+' '+pl+' '+gnd+"\n"
		s += "M"+str(n_mos)+" ("+bl+" "+wl+" net"+str(n_mos)+" "+gnd+" ) nsvt25 w=0.4 l=0.28\n"
		s += "I0 conder net"+str(n_mos)+' '+pl+"  Ec=1.9 dT=1e-09 l="+size*1e-9+" w="+size*1e-9+" "+str(self.p00)
		s += "ends "+self.cell.name +"\n"

	def add_to_netlist(self,n_inst, bl , wl , pl , gnd ):
		s = "I"+str(n_inst)+" ("+bl+' '+wl+' '+pl+' '+gnd+") "+self.cell.name+"\n"
		return s
		





class Sense_amp(My_Cell):
	"""docstring for ClassName"""

	def __init__ (self, cell, in_pin , cell_index):
		
		self.in_pin = in_pin
		self.cell_index = cell_index
		self.cell = cell


class Top_driver(My_Cell):
	"""docstring for ClassName"""
	top_vdd=  pya.Point( -500, 5350)
	def __init__ (self, cell, out_pin , cell_index):
		
		self.out_pin = out_pin
		self.cell_index = cell_index
		self.cell = cell

	#def sbskt_def(self, n_mos, bl , wl , pl , gnd  ):



class PL_driver(My_Cell):
	"""docstring for ClassName"""
	#top_vdd=  pya.Point( -500, 5350)
	def __init__ (self, cell, out_pin , cell_index):
		self.out_pin = out_pin
		self.cell_index = cell_index
		self.cell = cell
