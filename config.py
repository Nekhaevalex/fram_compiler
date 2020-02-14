import pya

import os


class Config:
	
	# Place for your parameters here.


	#Horizontal size
	word_size = 8
	#Vertical size
	num_words = 8

	# Ferroelectric params

	p00 = 1e-14 


	pdf_output = False


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

	top_driver_vdd_name = "driver_vdd"
	top_driver__gnd_name = "driver_gnd"



	def __init__(self, arg):
		pass
