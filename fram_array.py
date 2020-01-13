import pya
import os
import datetime
import random
#import sys


from layout_class import *
from cells import *
#from netlist_generator import *


#---------------------Open Config-------------------------
from array_config import *




#--------------------support func------------------

def find_pwr2(n,s):
	if (n % 2 == 0):
		s = s + 1
		return (find_pwr2(n/2,s))
	else:
		return s







def simple_path( start, end , width):
	pth = pya.Path([start,end] , width)
	poly = pth.simple_polygon()
	return poly
#TOP.shapes(M2).insert(poly)





def pwr2(num):

	'states if a number is a power of two'

	return ((num & (num - 1)) == 0) and num > 0


#--------------------class definition-----------------------



'''
class Amp(pya.Cell):
	"""docstring for ClassName"""
	self.in_pin = pya.Point()
	self.ref_pin = pya.Point()
	self.vdd_pin = pya.Point()
	self.gnd_pin = pya.Point()




class Driver(pya.Cell):
	"""docstring for ClassName"""
	self.out_pin = pya.Point()
	self.in_pin = pya.Point()
	self.vdd_pin = pya.Point()
	self.gnd_pin = pya.Point()

'''


#======================CODE BEGINS==========

now = datetime.datetime.now()
print("\n - Compilation started "+now.strftime("%Y-%m-%d %H:%M")+"-\n")

#=======================CHECK===============



if(n_decoders):
	if pwr2(num_words):
		n_decoders = True
		print("decoders ++")
	else:
		if(n_decoders):
			print("====WARNING: Number of words is not a power of 2:=======\n Generation of adress decoders impossible!")
			n_decoders = False









'''
now = datetime.datetime.now()
log = open("fram_compilation.log","w+")
log.write("---------------------------------------------------\nCompilation of "+ output_name +" started."+now.strftime("%Y-%m-%d %H:%M")+"\n")
log.write("Parameters of cell:\nword size = "+ str(word_size) +"\nnumber of words = "+ str(num_words))
log.write("\n \n \n \n")
'''
#-----------------------Initialization--------------------


layout = pya.Layout()
layout.dbu = 1
bitline = layout.create_cell("bitline")
bitline_m = layout.create_cell("bitline_m")#mirror of top driver and sen amp
TOP = layout.create_cell("TOP")

# One cell for all multipart Pahts 
multipart_cell = layout.create_cell("multipart")
multipart_cell_index = multipart_cell.cell_index()








gdsFiles= [ "./gds_files/nch_25.gds","./gds_files/pch_25.gds" ]
vias = ["./gds_files/multipart_vdd1.gds","./gds_files/multipart_gnd1.gds"]
drivers = ["./gds_files/driver.gds","./gds_files/driver_vdd.gds","./gds_files/driver_gnd.gds","./gds_files/PL_driver.gds", "./gds_files/driver_3u.gds", "./gds_files/driver_3u_m.gds" ]
amps = ["./gds_files/sense_amp.gds","./gds_files/sense_amp_vdd.gds","./gds_files/sense_amp_gnd.gds",]
memory_cells_string = ["./gds_files/memory_cell.gds","./gds_files/memory_cell_600.gds"]

gdsFiles.extend(vias)
gdsFiles.extend(drivers)
gdsFiles.extend(amps)
gdsFiles.extend(memory_cells_string)
if (estimation == "Phox_picture_estimation"):
	est_string = ["./gds_files/nazca_export.gds"]
	gdsFiles.extend(est_string)



# Read all cells
for i in gdsFiles:
	layout.read(i)
	for j in layout.top_cells():
		if (j.name == "memory_cell"):
			memory_cell = j
			print(j.name+" found")
		if (j.name == "sense_amp"):
			amp_cell = j
			print(j.name+" found")
		if (j.name == "driver"):
			driver_cell = j
			print(j.name+" found")
		if (j.name == "nsvt25"):
			nmos_cell = j
			print(j.name+" found")
		if (j.name == "psvt25"):
			pmos_cell = j
			print(j.name+"found")
		if (j.name == "multipart_vdd1"):
			multipart_vdd1_cell = j
			print(j.name+" found")
		if (j.name == "multipart_gnd1"):
			multipart_gnd1_cell = j
			print(j.name+" found")
		if (j.name == "c_inv_3u"):
			pl_driver_cell = j 
			print(j.name + " found")
		if (j.name == "driver_gnd"):
			driver_gnd_cell = j
			print(j.name+" found")
		if (j.name == "driver_vdd"):
			driver_vdd_cell = j
			driver_vdd_1_cell = j
			print(j.name+" found")
		if (j.name == "driver_3u"):
			driver_3u_cell = j
			print(j.name+" found")
		if (j.name == "driver_3u_m"):
			driver_3u_m_cell = j
			driver_3u_m_top_cell = j
			print(j.name+" found")
		if (j.name == "sense_amp_vdd"):
			sense_amp_vdd_cell = j
			print(j.name+" found")
		if (j.name == "sense_amp_gnd"):
			sense_amp_gnd_cell = j
			print(j.name+" found")
		if (j.name == "memory_cell_600"):
			memory_cell_600 = j




		if (estimation == "Phox_picture_estimation"):
			if (j.name == "nazca"):
				nazca_cell = j
				print(j.name+" found")





# self, cell, drain, gate, source, cell_index, width, length
nmos = Mos( nmos_cell, pya.Point(450,200), pya.Point(150,200) , pya.Point(-170,200), nmos_cell.cell_index(), nmos_width, nmos_length)
pmos = Mos (pmos_cell,pya.Point(450,200), pya.Point(150,200) , pya.Point(-170,200),pmos_cell.cell_index() , pmos_width , pmos_length)

# def __init__ (self, cell, bl_pin, gnd_pin, wn_pin , cell_index):
array_cell = Memory_cell(memory_cell,pya.Point(650,1200),pya.Point(400,1350), pya.Point(1120,1200),1200 )
array_cell_600 = Memory_cell(memory_cell_600,pya.Point(650,1200),pya.Point(400,1350), pya.Point(1120,1200),600 )


if (cell_type == "600nm"):
	main_cell = array_cell_600
if (cell_type == "1200nm"):
	main_cell = array_cell

main_cell.p00 = p00


driver = Top_driver( driver_cell)

driver_vdd = Top_driver(driver_vdd_cell)
driver_gnd = Top_driver(driver_gnd_cell)
driver_vdd_1 = Top_driver(driver_vdd_1_cell)

driver_3u = PL_driver(driver_3u_cell)
driver_3u_m = PL_driver(driver_3u_m_cell)

sense_amp_vdd = Sense_amp(sense_amp_vdd_cell)
sense_amp_gnd = Sense_amp(sense_amp_gnd_cell)

multipart_vdd1 = My_Cell(multipart_vdd1_cell)
multipart_gnd1 = My_Cell(multipart_gnd1_cell)

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
#NW drawing 3 0

#==================Declare Multipart path===================


nod_straps = [(NP, 460 , 0),(M1,200 , 1),(OD,200, 1)] #[(layer,width,lenth {0 = long } {1 = short} {2 = inverted long} , ),()]
nod_straps_implant = [(NP, 460 , 0),(M1,200 , 1),(OD,200, 1),(PP, 460, 2 , 100)]# , True, (PP, 460 , 200)

nod_pin_size = 120
nod_pin_layer = OD
nod_tie = MultipartPath( "nod_tie" , nod_pin_layer, nod_pin_size,*nod_straps)
nod_tie_implant = MultipartPath( "nod_tie_implant" , nod_pin_layer, nod_pin_size,*nod_straps_implant) 


pod_pin_size = 120
pod_pin_layer = CO
pod_straps = [(PP, 460),(M1,200),(OD,200)]
pod_straps_implant = [(PP, 460 , 0),(M1,200 , 1),(OD,200, 1),(NP, 200, 2 , 100)]
pod_tie = MultipartPath( "pod_tie",pod_pin_layer, pod_pin_size ,*pod_straps)
pod_tie_implant = MultipartPath( "pod_tie_implant",pod_pin_layer, pod_pin_size ,*pod_straps_implant)

#nod = vdd

#pod = gnd

#nod_tie.place(multipart_cell,pya.Point(-1000,0),pya.Point(-1000,-10000))

#nod_tie.place(multipart_cell,pya.Point(-4000,-10000),pya.Point(-4000,0))

#nod_tie_implant.place(multipart_cell,pya.Point(-4000,-6000),pya.Point(-8000,-6000))

#=================================TEST=========================


'''
xpos = -10000
ypos = -10000

t = pya.Trans(   xpos    ,  ypos )
driver.place(TOP,t)

xpos = -10000 -5000
# this is how to make smth reversed
t = pya.Trans(-2 , True, pya.Vector(xpos, ypos))


driver.place(TOP,t)
'''
#Estimation
if (estimation == "Phox_picture_estimation"):
	nazca = My_Cell(nazca_cell)
	t = pya.Trans(Xcell_size * word_size*10 , Ycell_size * num_words * 10  )
	nazca.place(TOP,t)


#-------------------------------------FORM BITLINE--------------------------------

xpos = 0  - main_cell.bl_pin.x
ypos = 0 - main_cell.bl_pin.y

t = pya.Trans(   xpos    ,  ypos )




'''
for yIndex in range(0,num_words):
	cell_index=memory_cell.cell_index()
	array_cell_inst = pya.CellInstArray(cell_index,t)
	bitline.insert(array_cell_inst)
	ypos = ypos + 2*Ycell_size
	t = pya.Trans(   xpos,  ypos)
'''


n=0

for yIndex in range(0,num_words):
	main_cell.place(bitline,t)
	main_cell.place(bitline_m,t)
	ypos = ypos + 2*Ycell_size
	t = pya.Trans(xpos,ypos)



#------------------------------------Insert top driver and sense amp--------------------------------


start = pya.Point(-1690,12090)
end = pya.Point(-1690,14390)

driver_gnd.cell.shapes(M1).insert(simple_path( start, end , Ycell_size))

start = pya.Point(-1690,1090)
end = pya.Point(-1690,3390)

driver_vdd.cell.shapes(M1).insert(simple_path( start, end , Ycell_size))



t = pya.Trans(driver.out_pin.x+650, 2*num_words*Ycell_size+ driver.out_pin.y )
driver_gnd.place(bitline,t)


#t = pya.Trans(-2 , True, pya.Vector(-1700, 2*num_words*Ycell_size+ driver.out_pin.y) )
t = pya.Trans(driver.out_pin.x+650, 2*num_words*Ycell_size+ driver.out_pin.y )
driver_vdd.place(bitline_m,t)



#-----------Bitline power and gnd lines 






#bitline.insert(amp_cell)

#------------------ROUTING_BITLINE-------------------------
bl_start = pya.Point(0, - 3 * Ycell_size )
bl_end = pya.Point(0,2*num_words*Ycell_size+ driver.out_pin.y/2)

bl_pth = pya.Path([bl_start,bl_end] , bl_width)
bl_poly = bl_pth.simple_polygon()

bitline.shapes(M1).insert(bl_poly)
#bl_path = [(-4000,0.0),(-4000,Ycell_size*2.00*(num_words-1))]



bitline_m.shapes(M1).insert(simple_path(bl_start,bl_end,bl_width))
#decoder_cell.shapes(OD).insert(simple_path( start, end , 200))




#----------------------------Adding Sen_amp-------------



t = pya.Trans(-1000,-2800)
sense_amp_gnd.place(bitline,t)
sense_amp_vdd.place(bitline_m,t)



#----------------ADDING BITLINES---------------------------

xpos = 0
ypos = 0
t = pya.Trans(   xpos,  ypos)

n=0

for yIndex in range(0,word_size):
	if ( n % 2 == 0):
		cell_index = bitline.cell_index()
		bl_cell_inst = pya.CellInstArray(cell_index,t)
		TOP.insert(bl_cell_inst)
		xpos = xpos + 4*Xcell_size
		t = pya.Trans(   xpos,  ypos)
	if ( n % 2 != 0):
		cell_index = bitline_m.cell_index()
		bl_cell_inst = pya.CellInstArray(cell_index,t)
		TOP.insert(bl_cell_inst)
		xpos = xpos + 4*Xcell_size
		t = pya.Trans(   xpos,  ypos)
	n+=1







#-----------------------------DECODERS--------------------------

if (n_decoders and decoders25):
	decoder_cell = layout.create_cell("decoder_cell")
	xpos1 = pmos_placement_width*4
	ypos1 = 0
	xpos2 = -nmos_placement_width*4
	ypos2 = 0
	num_addr_bus = find_pwr2(num_words,0)

	for i in range (0, num_addr_bus):
		t1 = pya.Trans(1 , False, pya.Vector(xpos1, ypos1))
		t2 = pya.Trans(1 , False, pya.Vector(xpos2, ypos2))
		pmos.place(decoder_cell,t1)
		nmos.place(decoder_cell,t2)
		xpos1 = xpos1 + pmos_placement_width*4
		xpos2 = xpos2 - nmos_placement_width*4
	# GND Via

	# Vdd Via #MANUAL PLACEMENT!
	xpos1 = pmos_placement_width*4 + 250
	xpos2 = - nmos_placement_width*4 + 250
	ypos1 = -nmos_width*2-60
	ypos2 = -nmos_width*2-60

	for i in range (0, num_addr_bus):
		t1 = pya.Trans(1 , False, pya.Vector(xpos1, ypos1))
		multipart_vdd1.place(decoder_cell,t1)
		t2 =  pya.Trans(1 , False, pya.Vector(xpos2, ypos2))
		multipart_gnd1.place(decoder_cell,t2)
		xpos1 = xpos1 + pmos_placement_width*4
		xpos2 = xpos2 - nmos_placement_width*4

	#Decoder via extra routing ---VDD
	start = pya.Point(pmos_placement_width ,  -nmos_width*2+170)
	end = pya.Point(num_addr_bus*pmos_placement_width*4 , -nmos_width*2 +170)
	decoder_cell.shapes(M1).insert(simple_path( start, end , 200))
	decoder_cell.shapes(OD).insert(simple_path( start, end , 200))
	# ---GND
	start = pya.Point(- nmos_placement_width*4 ,  -nmos_width*2+170)
	end = pya.Point(-num_addr_bus*nmos_placement_width*4 , -nmos_width*2 +170)
	decoder_cell.shapes(M1).insert(simple_path( start, end , 200))
	decoder_cell.shapes(OD).insert(simple_path( start, end , 200))


	#Routing of decoder


	start = pya.Point( -pmos_placement_width*5 ,  pmos.source.x)
	end = pya.Point(num_addr_bus*pmos_placement_width*4 , pmos.source.x)
	decoder_cell.shapes(M1).insert(simple_path( start, end , bl_width))
	j=1
	xpos = -150 -nmos_placement_width*4 # IN FUTURE CHANGE 150 to proper value
	for i in range (0,num_addr_bus -1 ):
		if (j%2 == 1 ):
			start = pya.Point( xpos,  pmos.drain.x)
			xpos = xpos - nmos_placement_width*4
			end = pya.Point( xpos, pmos.drain.x)
			decoder_cell.shapes(M1).insert(simple_path( start, end , bl_width))
		else:
			start = pya.Point( xpos,  pmos.source.x)
			xpos = xpos - nmos_placement_width*4
			end = pya.Point( xpos, pmos.source.x)
			decoder_cell.shapes(M1).insert(simple_path( start, end , bl_width))
		j=j+1





if (n_decoders and decoders25):

	#Add decoders to TOP-cell
	xpos = - num_addr_bus*pmos_placement_width*6
	ypos = - pmos.source.x
	t = pya.Trans(   xpos,  ypos )

	for i in range(0,num_words):
		cell_index = decoder_cell.cell_index()
		decoder_cell_inst = pya.CellInstArray(cell_index,t)
		TOP.insert(decoder_cell_inst)
		ypos = ypos + 2*Ycell_size
		t = pya.Trans(   xpos,  ypos)


#=======================PL DRIVERS=========================




xpos_0 =  4*Xcell_size*word_size # Initial point
xpos =  xpos_0
ypos = - PL_driver.out_pin.x + 250


n = 0
t = pya.Trans(1 , True, pya.Vector(xpos, ypos))
start = pya.Point (0,450)
end =  pya.Point (0,3270)
driver_3u_m.cell.shapes(M1).insert(simple_path( start, end , Ycell_size))
start = pya.Point (1820,4270)
end =  pya.Point (1820,7090)
driver_3u_m.cell.shapes(M1).insert(simple_path( start, end , Ycell_size))

for i in range(0,num_words-1):
	if (n % 2 == 0):
		driver_3u.place(TOP,t)
		ypos = ypos + 2*Ycell_size
		t = pya.Trans(1 , True, pya.Vector(xpos, ypos))
	if (n % 2 != 0):
		driver_3u_m.place(TOP,t)
		ypos = ypos + 2*Ycell_size
		t = pya.Trans(1 , True, pya.Vector(xpos, ypos))

	n+=1
#extra driver with its own vdd (because of the "mirror" placement  system)
driver_3u_m_top = My_Cell(driver_3u_m_top_cell)
nod_tie.place(driver_3u_m_top_cell,pya.Point(1800, 4275),pya.Point( 1800 , 7080 ))
driver_3u_m.place(TOP,t)


#------------------Pl drivers metal intersections-----------------------------



#------------------Pl drivers large N-well-------------------------


#top.shapes(l1).insert(pya.Box(0, 0, 1000, 2000))

TOP.shapes(NW).insert(pya.Box(xpos_0  + 3720  , 0 ,xpos_0  + 3720+ 4850 , 2*Ycell_size*(num_words-1) ))

#( pya.Point(4*Xcell_size*word_size + 3700  , -1500 ),pya.Point( 4*Xcell_size*word_size + 3700 +4000, 2*Ycell_size*num_words )))



#--------------WORD line-------------------------------------

#wl_pth = pya.Path([bl_start,bl_end] , bl_width)
#wl_poly = bl_pth.simple_polygon()


#bitline.shapes(l1).insert(simple_path( wl_start, wl_end , wl_width))

xpos = 0
ypos = 500

for yIndex in range(0, num_words):
	start = pya.Point(-1000, ypos)
	end = pya.Point(4 * Xcell_size * word_size, ypos)
	TOP.shapes(M2).insert(simple_path( start, end , wl_width))
	ypos = ypos + 2*Ycell_size
#	print(start.y , end.y)



#---------------------------Plate line---------------------
xpos = 0
ypos = 0

for yIndex in range(0, num_words):
	start = pya.Point( - 1000 , ypos)
	end = pya.Point(4 * Xcell_size * word_size + 500 , ypos)
	TOP.shapes(M4).insert(simple_path( start, end , gnd_width))
	ypos = ypos + 2*Ycell_size






#--------------------------------GROUND HORIZONTAL----------------------
xpos = 0
ypos = -800

for yIndex in range( 0 , num_words ):
	start = pya.Point( 0 , ypos)
	end = pya.Point( Xcell_size * 4 * word_size , ypos )
	TOP.shapes(M2).insert( simple_path( start, end , gnd_width ))
	ypos = ypos + 2 * Ycell_size
#	print(start.y , end.y)



#--------------------- extra driver ground




#====================Add huge OD_25 polygon

xpos_0 =  2*Xcell_size*word_size # Initial point X
ypos_0 =  2*Ycell_size*num_words # Initial point Y


#TOP.shapes(OD_25).insert(pya.Box( 0 - xpos_0,0 , xpos_0*word_size , ypos_0 * num_words ,  ))






#======================Add multipart cell==========
t = pya.Trans(   0,  0)
mp_cell_array = pya.CellInstArray(multipart_cell.cell_index(),t)
TOP.insert(mp_cell_array)

#=======================FINAL GDS OUTPUT===========


layout.write("./gds_files/"+ output_name+".gds")
print("\n layout has been saved as ./gds_files/"+ output_name+".gds\n" )

#======================CREATE NETLIST (OBJECT WAY)=============

GND = "0"
VDD = "vdd"



cell_size_sim = cell_x_size * cell_y_size

#fram_netlist = Netlist(output_name , word_size , num_words,sense_amp,array_cell, driver,pmos,nmos,p00 ,cell_size_sim , args*)





#fram_netlist = Netlist(output_name , word_size , num_words,sense_amp,array_cell, driver,pmos,nmos,p00 ,cell_size_sim , args*)










'''
#------------------Create PDF file-------------------------
array_cell_layout.rename("arrayLayout")
visualizer = gdsMill.PdfLayout(array_cell_layout)


#Making all colors radnom and set them
if (color_set == "random" ):
	log.write("------------------Colors in use----------------- \n")
	for i in range(len(array_cell_layout.layerNumbersInUse)):
		color = ("#"+random.choice('0123456789ABCDEF')+random.choice('0123456789ABCDEF')+random.choice('0123456789ABCDEF')+random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF')+ random.choice('0123456789ABCDEF') )
		visualizer.layerColors[array_cell_layout.layerNumbersInUse[i]] = color
		log.write("Color for layer"+str(i)+" = "+color+"\n")
log.write("\n \n \n")



visualizer.setScale(500)
visualizer.drawLayout()



visualizer.writeToFile("./gdsFiles/array_gds/new_pdf.pdf")
print("STAT: Pdf file saved")


#layers = array_cell_layout.layerNumbersInUse()


log.write("--------------------Layers in use:-----------------\n")
log.write("\n Cell layers: \n ")
for i in range(len(array_cell_layout.layerNumbersInUse)):
	s = "Layer N "+str(i)+" = "+str(array_cell_layout.layerNumbersInUse[i])+"\n"
	log.write(s) 


log.write("\n \n \n ")
log.write("\n Sen_Amp layers: \n ")
log.write("--------------------Layers in use:-----------------\n")
for i in range(len(amp_layout.layerNumbersInUse)):
	s = "Layer N "+str(i)+" = "+str(amp_layout.layerNumbersInUse[i])+"\n"
	log.write(s) 


#-----------------------move log file to  folder and close----------

log.close()
os.rename("./fram_compilation.log", "./gds_files/fram_compilation.log")
'''


print ("In case of any confusion in files you are welcome to check README.txt ,\nor contact me via e-mail or phone.")