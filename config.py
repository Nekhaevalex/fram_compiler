import pya

import os


from inspect import currentframe, getframeinfo



class Config:
	# Place for your parameters here.

	debug_level = 5	# >1 for debug, 0 for no printout


	lvs = False
	#Horizontal size
	word_size = 4
	#Vertical size
	num_words = 4

	# Ferroelectric params
	p00 = 1e-14 # Polarization (not working yet) # Default  = 1e-14

	pdf_output = False # Nor working yet

	view_gds = False

	output_name = "fram_sample"

	#Files to look out. No extention needed. Generator will look for example:
	# Filename: cell. ./gds_files/cell.gds ./sp_files/cell.sp
	files = []

	#Here you can specify cell names of all cells represented in ./gds_files and ./sp_files !
	# Notice! All files names and cells names should be the SAME!

	fram_bitcell_name = "memory_cell" 

	#sense amplifighers right and left variant
	sense_amp_name = "sense_amp"

	sense_amp_gnd_name = "sense_amp_gnd"
	sense_amp_vdd_name = "sense_amp_vdd"

	# Top drivers

	top_driver_name = "driver"

	top_driver_vdd_name = "top_driver_vdd"
	top_driver_gnd_name = "top_driver_gnd"

	nmos_name = "nsvt25"
	pmos_name = "psvt25"

	boundary_layer = "None" #Main boundary layer used to find boundary of cells. If left "None" boundary determins automatically


	bl_width = 150 # Default  = 150

	module_clearence = 1000 # Default  = 1000

	# Width settings

	width = {}

	width['bl'] = 150 # Default  = 150
	width['pl'] = 150 # Default  = 150
	width['wl'] = 150 # Default  = 150
	width['gnd'] = 150 # Default  = 150

	layers_with_pins = ["M1_pin","M2_pin","M3_pin"]	
	''' Create markers as: '''
	marker_as_text = False
	marker_as_point = True


	cells_list = ["memory_cell","sense_amp","top_driver"]

	top_driver = ( top_driver_vdd_name , top_driver_gnd_name )

	pre_decoder_name = "decoder_stage"  # Default  = "decoder_stage"
	pre_decoder_vdd_name = "decoder_stage_vdd"
	pre_decoder_gnd_name = "decoder_stage_gnd"
	pre_decoder = ( pre_decoder_vdd_name , pre_decoder_gnd_name)

	mos_pair_name = "mos_pair"


	design_views = ["layout", "netlist"]  # Default  = ["layout", "netlist"]
 
	boundary_layer = "prBnd" # Default  = 'prBnd'

	def __init__(self):
		pass

	def get_layers(self, file = "layers.txt"):
		size_to_read = 0
		with open(file,'r') as text:
			for line in text:
				if (line[0] != '#'):
					# get line here
					word = line.split()
					print(f"word = {word}")

	def debug_message(self, debug_level,debug_message):
		if (self.debug_level > debug_level ):
			print(debug_message)

	def warning(self,frameinfo):
		#frameinfo = getframeinfo(currentframe())
		print(f'This warning rised at file: "{frameinfo.filename}", on line: {frameinfo.lineno}.\nGood luck finding it.\n ===============')