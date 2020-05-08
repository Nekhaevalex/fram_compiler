import pya

class MultipartPath():
	"""Класс для генерации процедурных стрэпов питания. Условно работает. Пока не используется"""
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
			orrint = 1 #vertical
			if (end.y   > begin.y):
				direct = "UP"
			if (end.y <=  begin.y ):
				direct = "DOWN"
		else :
			orrint = 2 #horisontal
			if (end.x > begin.x ):
				direct = "RIGHT"
			if (end.x  < begin.x):
				direct = "LEFT"
		print("ORRIIIINT:")
		print(orrint)
		print("DIRECT:")
		print(direct)
		straps = self.straps
		self.num=self.num + 1
		begin_short = pya.Point(begin.x , begin.y)
		end_short = pya.Point(end.x , end.y)
		if (orrint == 1):
			if (direct == "UP"):
				begin_short.y = begin.y + 130
				end_short.y = end.y -130
			if (direct == "DOWN"):
				begin_short.y = begin.y - 130
				end_short.y = end.y + 130
		elif (orrint == 2):
			if (direct == "RIGHT"):
				begin_short.x = begin.x +130
				end_short.x = end.x -130
			if (direct == "LEFT"):
				begin_short.x = begin.x - 130
				end_short.x = end.x + 130


		#--------Adding lines-------
		for i in range(0,len(straps)):
			if (straps[i][2] == 0): #long line
				pth = pya.Path([begin,end] , straps[i][1])
				#print("added stap in layer"+str(straps[i][0]))
				poly = pth.simple_polygon()
				multipart_cell.shapes(straps[i][0]).insert(poly)
			if (straps[i][2] == 1): #short line
				pth = pya.Path([begin_short,end_short] , straps[i][1])
				#print("added stap in layer"+str(straps[i][0]))
				poly = pth.simple_polygon()
				multipart_cell.shapes(straps[i][0]).insert(poly)
			if (straps[i][2] == 2):
				begin_inv1 = pya.Point(begin.x,begin.y)
				begin_inv2 = pya.Point(begin.x,begin.y)
				end_inv1 = pya.Point(end.x,end.y)
				end_inv2 = pya.Point(end.x,end.y)
				straif = straps[i][1]/2 + (straps[i][3])
				if (orrint == 1):
					begin_inv1.x  += straif
					end_inv1.x += straif
					begin_inv2.x -= straif
					end_inv2.x -= straif
					pth1 = pya.Path([begin_inv1 , end_inv1] , straps[i][3]*2)
					pth2 = pya.Path([begin_inv2 , end_inv2] , straps[i][3]*2)
					poly1 = pth1.simple_polygon()
					poly2 = pth2.simple_polygon()
					multipart_cell.shapes(straps[i][0]).insert(poly1)
					multipart_cell.shapes(straps[i][0]).insert(poly2)
				elif (orrint == 2):
					begin_inv1.y  += straif
					end_inv1.y += straif
					begin_inv2.y -= straif
					end_inv2.y -= straif
					pth1 = pya.Path([begin_inv1 , end_inv1] , straps[i][3]*2)
					pth2 = pya.Path([begin_inv2 , end_inv2] , straps[i][3]*2)
					poly1 = pth1.simple_polygon()
					poly2 = pth2.simple_polygon()
					multipart_cell.shapes(straps[i][0]).insert(poly1)
					multipart_cell.shapes(straps[i][0]).insert(poly2)


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

		coord = pya.Point(begin.x,begin.y)
		poly = []
		if ((orrint == 1) & (direct == "UP") ):
			coord.y = coord.y + 70
			coord_end = pya.Point(coord.x , coord.y)
			poly = []
			while (coord.y <= end.y - (100 + pins[1])) :
				coord_end = pya.Point(coord.x , coord.y)
				coord_end.y = coord_end.y + pins[1]
				pth = pya.Path([coord, coord_end] , pins[1])
				poly.append(pth.simple_polygon())
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
		if ((orrint == 2) & (direct == "RIGHT")):
			coord.x = coord.x + 70
			coord_end = pya.Point(coord.x , coord.y)
			while (coord.x <= end.x - (100 + pins[1])) :
				coord_end = pya.Point(coord.x , coord.y)
				coord_end.x = coord_end.x+ pins[1]
				pth = pya.Path([coord, coord_end] , pins[1])
				poly.append(pth.simple_polygon())
				a = pth.simple_polygon()
				multipart_cell.shapes(pins[0]).insert(a)
				coord.x=coord.x+140*2
		if ((orrint == 2) & (direct == "LEFT")):
			coord.x = coord.x - 70
			while (coord.x >= end.x + ( 100 + pins[1])):
				coord_end = pya.Point(coord.x , coord.y)
				coord_end.x = coord_end.x - pins[1]
				pth = pya.Path([coord, coord_end] , pins[1])
				poly.append(pth.simple_polygon())
				a = pth.simple_polygon()
				multipart_cell.shapes(pins[0]).insert(a)
				coord.x=coord.x - 140 * 2

		for i in range(len(poly)):
			multipart_cell.shapes(pins[0]).insert(poly[i])