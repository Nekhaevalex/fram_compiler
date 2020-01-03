#This is simple array config file


#==========Type of cell

cell_type = "600nm"
#cell_type = "1200nm"
# 600 or 1200 nm cell




#-----------DIMENSIONS FOR THE LAYOUT. NOT AN ACTUAL DIMENTIONS-------------

Xcell_size = 500
Ycell_size = 900

# stable is:
#Xcell_size = 500
#Ycell_size = 1000



#Horizontal size
word_size = 16
#Vertical size
num_words = 16


#output_name = "FRAM_{0}_{1}.gds".format(word_size,num_words)
output_name = "fram_sample"



array_cell = "array_cell.gds"


#-----------------------Tracks---------------------

# width of bitline
bl_width = 130 
# width of wordline
wl_width = 120 
#Width of extra gnd routing
gnd_width = 150


#---------------------------Memory cells  (FOR SIMULATION ONLY NOW!!)

if (cell_type == "600nm"):
	cell_x_size = 5e-07
	cell_y_size = 5e-07

if (cell_type == "1200nm"):
	cell_x_size = 12e-07
	cell_y_size = 12e-07
# polarysation 
p00 = 1e-14   








#---------------------Other setings------------------

# if you need decoders of word line or not (True/False)		
n_decoders = False 		


# if True, will place 2.5V decoders, else (False) will make 1.2 Decoders + converter!
# 1.2 decoders not there anyway!
decoders25 = True

#Estimation is there to place a real sized picture reference to appreciate the small size of a memory chip
estimation = "False" # or "Phox_picture_estimation"



#-----------------------MOS SETTINGS


nmos_width = 400

pmos_width = 400


nmos_length = 280

pmos_length = 280

nmos_placement_width = 250
pmos_placement_width = 250













#-----------------------PDF------------------------- (NOT WORKING YET)



pdf_output = False

#Small numbers can lead to bugs of pdf reader due to large file size
pdf_scale = 500

#Options are: "random"
color_set = "random"






