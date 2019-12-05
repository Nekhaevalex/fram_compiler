import pya


class MultipartPath():
	"""docstring for ClassName"""
	num = 0
	#straps = (layer, w)
	def __init__(self, name,pin_layer,pin_size, *straps):
		self.straps = straps
		self.name = name
		self.pins = [pin_layer,pin_size]

	def place(self,multipart_cell,begin,end): # TOP TO BOTTOM RIGHT TO LEFT!!
		#Need to understand orientation of 
		orrint = 0 # 0 = null ; 1 = vertical; 2 = horisontal ; 3 = error
		direct = "NULL"
		pins = self.pins
		print("pin lenth:")
		print(pins[1])
		vertcal_lenth = abs(end.y - begin.y)
		horisontal_lenth = abs(end.x - begin.x)
		print("Vertical:" +str(vertcal_lenth)+" Horisontal: "+str(horisontal_lenth))
		if (vertcal_lenth > horisontal_lenth):
			print("vertcal_lenth > horisontal_lenth")
			orrint = 1 #vertical
			if (end.y   > begin.y):
				direct = "UP"
			if (end.y <=  begin.y ):
				direct = "DOWN"
		else :
			orrint = 2 #horisontal
			if (end.x - begin.x > 0):
				direct = "RIGHT"
			if (end.x - begin.x > 0):
				direct = "LEFT"
		print("ORRIIIINT:")
		print(orrint)
		print("DIRECT:")
		print(direct)
		straps = self.straps
		self.num=self.num + 1
		pth = pya.Path([begin,end] , straps[0][1])
		poly = pth.simple_polygon()
		multipart_cell.shapes(straps[0][0]).insert(poly)
		if (orrint == 1):
			if (direct == "UP"):
				begin.y = begin.y + 130
				end.y = end.y -130
			if (direct == "DOWN"):
				begin.y = begin.y - 130
				end.y = end.y + 130
		elif (orrint == 2):
			if (direct == "RIGHT"):
				begin.x = begin.x +130
				end.x = end.x -130
			if (direct == "LEFT"):
				begin.x = begin.x - 130
				end.x = end.x + 130
		else:
			print("Wrong!!")  
		for i in range(1,len(straps)):
			pth = pya.Path([begin,end] , straps[i][1])
			#print("added stap in layer"+str(straps[i][0]))
			poly = pth.simple_polygon()
			multipart_cell.shapes(straps[i][0]).insert(poly)
		'''
		n = 0
		if (orrint == 1 ):
			n = vertcal_lenth/260
		if (orrint == 2)
			n = horisontal_lenth/260
		if (n == 0)
			print("ERROR DEFINING orientation in"+self.name+str(self.num))
		else:
			if((orrint == 1) && (direct == "TOP") ):
				coord = begin
				coord.x = coord.x + 70
				for i in range(n): #top.shapes(l1).insert(pya.Box(0, 0, 1000, 2000))
		'''
		coord = pya.Point(begin.x,begin.y)
		if ((orrint == 1) & (direct == "UP") ):
			coord.y = coord.y + 70
			coord_end = pya.Point(coord.x , coord.y)
			poly = []
			while (coord.y <= end.y - (100 + pins[1])) :
				coord_end = pya.Point(coord.x , coord.y)
				coord_end.y = coord_end.y + pins[1]
				pth = pya.Path([coord, coord_end] , pins[1])
				poly.append(pth.simple_polygon())
				print("after")
				print(coord_end.y)
				print(coord.y)
				coord.y=coord.y+140*2
		if ((orrint == 1) & (direct == "DOWN")):
			poly = []
			coord.y = coord.y - 70
			while (coord.y >= end.y + ( 100 + pins[1])):
				coord_end = pya.Point(coord.x , coord.y)
				coord_end.y=coord_end.y - pins[1]
				pth = pya.Path([coord, coord_end] , pins[1])
				poly.append(pth.simple_polygon())
				a = pth.simple_polygon()
				multipart_cell.shapes(pins[0]).insert(a)
				coord.y=coord.y - 140 * 2
		for i in range(len(poly)):
			multipart_cell.shapes(pins[0]).insert(poly[i])



