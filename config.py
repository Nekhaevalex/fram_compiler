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



	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
