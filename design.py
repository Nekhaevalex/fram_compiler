import pya #Klayout 
import os
import sys
import datetime
import random
import time
from utils import * # Тут хранятся полезные функции которые я иногда юзаю во всех функциях
from cells import * # 

from layout import My_Layout # Модуль наследованный от klayout.layout с некоторыми полезными плюшками.
from config import Config # Main Config are used by compiler through all of the functions.
from netlist import * # My Netlist class

#  For Debug
from inspect import currentframe, getframeinfo






class Design():
	"""docstring for Design"""
	def __init__(self, Config , *args):
		self.design_units = args
		self.Config = Config
		self.key_words = self.Config.design_units
		self.dict_units = {}
		self.array_lenth = len(self.key_words)
		self.update_dict()



	def update_design(self,*args):
		self.design_units = args
		self.update_dict()

	def update_dict(self):
		for i in range(self.array_lenth):
			self.dict_units[self.key_words[i]] = self.design_units[i]
			#Check if needed :: print(f"{self.design_units[i].type_name} is  {self.dict_units[self.key_words[i]]}")