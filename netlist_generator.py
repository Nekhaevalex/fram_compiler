import time
import datetime
import os

class Subsercuit():
	
	def __init__(self, name, *pins ):
		#netlist.nlst.write(str(list(pins)))
		self.name = name
		self.nlst = open(name+".sp","w+")
		self.nlst.write("//Subsercuit "+ name)
		self.nlst.write("\nsubckt "+name)
		
		#self.nlst.close()

	def add_to_netlist(self,n,*pins):
		s = "\nI"+str(n)+" ("
		for i in range(len(pins)):
			s = s+" "+pins[i]
		s = s+") "+self.name+'\n'
		return s


class Element():# NOT USED ANY MORE
	def __init__(self, letter, param, other , *pins):
		self.letter = letter
		self.param = param

	#def add_to_netlist()
	#	s = 
	#	return s 

		



class SenAmpSubsct(Subsercuit):
	GND = "gnd"
	IN = "in"
	REF = "ref"
	NB = "nb"
	NT = "nt"
	SEB = "seb"
	VDD = "vdd"
	net25 = "net25"
	net33 = "net33"
	net29 = "net29"
	mos_skip = 10


	def __init__(self,name, nmos, pmos, *pins): # PINS order: gnd in nb nt ref seb vdd
		self.name = name
		self.nmos = nmos
		self.pmos = pmos
		self.pins = pins
		#self.nlst = open(name+".sp","w+")
		#self.nlst.write("#Subsercuit "+ name)
		#self.nlst.write("\nsubckt "+name+"\n")
		#self.


	def add_definition(self,n_sbskt_mos):
		
		GND = self.GND
		IN = self.IN
		REF = self.REF
		NB = self.NB
		NT = self.NT
		SEB = self.SEB
		VDD = self.VDD
		net25 = self.net25
		net33 = self.net33
		net29 = self.net29
		s = "#Subsercuit "+ self.name+" definition."
		s = s+"\nsubckt "+self.name+' '+IN+' '+NB+' '+NT+' '+REF+' '+SEB+' '+VDD+' '+GND+"\n"
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,NB,SEB,GND,GND)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,GND,SEB,NT,GND)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,NT,NB,GND,GND)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,GND,NT,NB,GND)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,GND,NT,NB,GND)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.pmos.add_to_netlist(n_sbskt_mos,net25 ,SEB, VDD, VDD)+"\n"
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.pmos.add_to_netlist(n_sbskt_mos,net25 , REF , net33 , VDD )
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.pmos.add_to_netlist(n_sbskt_mos,net29 , IN , net25 , VDD )
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.pmos.add_to_netlist(n_sbskt_mos,NT , NB , net33 , VDD )
		n_sbskt_mos = n_sbskt_mos+1
		s = s+self.pmos.add_to_netlist(n_sbskt_mos,net29, NT, NB, VDD )
		n_sbskt_mos = n_sbskt_mos+1
		s = s+ "\nends "+self.name
		s+ "\n//End of subcircuit definition."
		return s


class MemoryCellSub(Subsercuit):
	mos_skip = 1
	GND = "gnd"
	VDD = "vdd"
	bl = "bl"
	pl = "pl"
	wl = "wl"
	def __init__ (self,name, p00, cell_size_sim ,nmos):
		self.name = name
		self.nmos = nmos
		self.p00 = p00
		self.cell_size_sim = cell_size_sim


	def add_definition(self,n_sbskt_mos):
		bl = "bl"
		pl = "pl"
		wl = "wl"
		net1 = "net1"
		s = "//Subsercuit \n //Cell name:  "+ self.name
		s = s + "// \n"
		s = s + "\nsubckt "+self.name+' '+bl+' '+wl+' '+pl+' '+self.GND+"\n"
		s = s+self.nmos.add_to_netlist(n_sbskt_mos,bl,wl, net1 ,self.GND)+"\n"
		s = s + "I0 conder "+net1+' '+pl+"  Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 "+str(self.p00) #Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
		s += "\nends "+self.name
		s += "\n// End of subcircuit definition.\n"
		return s




class DriverSub(Subsercuit):
	mos_skip = 4
	GND = "gnd"
	VDD = "vdd"

	def __init__(self, name, nmos,pmos , *pins):
		self.nmos = nmos
		self.pmos = pmos
		self.pins = pins
		self.name = name
	

	def add_definition(self,n_sbskt_mos):
		IN = "not_bl_drive_input"
		OUT = "bl_out"
		VDD = self.VDD
		GND = self.GND
		net_d = []
		for i in range(0,3):
			net_d.append( "net_d"+str(i))
		s ="//Subsercuit \n //Cell name:  "+ self.name
		s += "// \n"
		s += "\nsubckt "+self.name+' '+IN+' '+OUT+' '+VDD+' '+GND+"\n"
		s += self.pmos.add_to_netlist(n_sbskt_mos, VDD , IN , net_d[0] , VDD )
		n_sbskt_mos += 1
		s += self.pmos.add_to_netlist(n_sbskt_mos, net_d[0]  , IN , net_d[1] , VDD )
		n_sbskt_mos += 1
		s += self.nmos.add_to_netlist(n_sbskt_mos, net_d[1] ,IN , net_d[2] , GND)
		n_sbskt_mos += 1
		s += self.pmos.add_to_netlist(n_sbskt_mos, net_d[2] ,IN , GND , VDD )
		s += "\nends "+self.name
		s += "// End of subcircuit definition.\n\n"
		return s 













class Netlist():
	path = os.getcwd()
	n_sbskt_mos = 0 
	GND = "0"
	VDD = "vdd"
	bl=[]
	wl=[]
	pl=[]

	def __init__ (self, output_name , word_size , num_words , sen_amp,array_cell,driver ,pmos,nmos , p00, cell_size_sim , *options):
		print("\n Netlist: Creating netlist \n")
		self.name = output_name
		self.pmos = pmos
		self.nmos = nmos
		self.memory_cell = array_cell
		now = datetime.datetime.now()
		self.nlst = open(output_name+".sp","w+")
		self.nlst.write("---------------------------------------------------\n//Compilation of "+ output_name +" netlist started."+now.strftime("%Y-%m-%d %H:%M")+"\n")
		self.nlst.write("//Parameters of cell:\n//word size = "+ str(word_size) +"\n//number of words = "+ str(num_words))
		self.nlst.write("\n \n \n \n")
		self.nlst.write("simulator lang=spectre\nglobal 0\ninclude ""models.scs""\ninclude ""conder.va""\n")
		self.nlst.write("//-========Subsercuits========-\n")
		sen_amp_sub = SenAmpSubsct(sen_amp.cell.name, nmos, pmos, "GND", "vdd")
		self.nlst.write(sen_amp_sub.add_definition(self.n_sbskt_mos))
		self.n_sbskt_mos= self.n_sbskt_mos + sen_amp_sub.mos_skip
		self.nlst.write("\n //REMAINING "+str(self.n_sbskt_mos)+" \n")
		#Driver IN+' '+OUT+' '+VDD+' '+GND

		driver_sub = DriverSub(driver.cell.name,nmos,pmos )
		self.nlst.write(driver_sub.add_definition(self.n_sbskt_mos))

		#Memory_cell
		memory_cell_sub = MemoryCellSub(array_cell.cell.name, p00, cell_size_sim, nmos)  #p00, cell_size_sim ,nmos
		self.nlst.write(memory_cell_sub.add_definition(self.n_sbskt_mos))
		self.n_sbskt_mos += memory_cell_sub.mos_skip
		bl=[]
		wl=[]
		pl=[]
		bl_control = []

		#--------------------GENERATION OF ARRAY---------------
		# bl_control controller control billine!

		for i in range(0,word_size):
			bl.append("bl"+str(i))
			bl_control.append("bl_control"+str(i))

		for i in range(0,num_words):
			wl.append("wl"+str(i))
			pl.append("pl"+str(i))
		self.bl=bl
		self.pl=pl
		self.wl=wl
		self.bl_control = bl_control
		n_inst=0
		for i in range(0,word_size):
			self.nlst.write(sen_amp_sub.add_to_netlist(n_inst,bl[i],"nb","nt","ref","seb",self.VDD, self.GND))
			n_inst += 1 
			self.nlst.write(driver_sub.add_to_netlist(n_inst, bl_control[i] ,bl[i], self.VDD,self.GND))
			n_inst += 1
			#IN+' '+NB+' '+NT+' '+REF+' '+SEB+' '+VDD+' '+GND
			for j in range(0,num_words):
				self.nlst.write(memory_cell_sub.add_to_netlist(n_inst, bl[i],wl[j],pl[j],self.GND))
				n_inst = n_inst + 1

		


		print("\nNetlist has been generated as ./"+output_name+".sp .\n To view it type: ""cat "+output_name+".sp" "")

		self.nlst.close()

	#def end_netlist():
	def simulation_options():
		s = "simulatorOptions options"
		return s

#	def add ()

