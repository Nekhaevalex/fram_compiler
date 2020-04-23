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
		self.design_views = args
		self.Config = Config
		self.key_words = self.Config.design_views
		self.dict_views = {}
		self.array_lenth = len(self.key_words)
		self.update_dict()



	def update_design(self,*args, **kwargs):
		""" Запихнуть измененные вьюшки обратно в дизайн. Порядок важен! """
		if (args):
			self.design_views = args
			self.update_dict()
		if (kwargs):
			for word in kwargs :
				self.dict_views[word] = kwargs[word]


	def update_dict(self):
		for i in range(self.array_lenth):
			self.dict_views[self.key_words[i]] = self.design_views[i]
			#Check if needed :: print(f"{self.design_views[i].type_name} is  {self.dict_views[self.key_words[i]]}")

	def return_layout(self):
		return self.dict_views["layout"]

	def return_netlist(self):
		return self.dict_views["netlist"]	