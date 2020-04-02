import pya
import os
import sys
import subprocess

from utils import *
from config import Config




class LVS:
	"""docstring for ClassName"""
	def __init__(self, Config):
		self.Config = Config
		self.pwd = os.getcwd()


		if Config.lvs == True :
			self.Config.debug_message(2,"Starting LVS:")
			self.start_lvs()
		else:
			self.Config.debug_message(2,"No LVS required")

	def start_lvs(self):
		p_init = subprocess.run('echo "Sucsessfully get bash in $(pwd).\nOS: $(uname -a)\n"', capture_output = True ,shell = True , text  = True)

		self.Config.debug_message(2,p_init.stdout)

		check_os_content(f"{self.pwd}/lvs")

		p_init = subprocess.run(f'. {self.pwd}/lvs/.bashrc', capture_output = True ,shell = True , text  = True)

		if (p_init.returncode != 0):
			self.Config.debug_message(2,f".bashrc returncode:{p_init.returncode} => {p_init.stdout}\n ")
			self.Config.debug_message(0,f"\t========== Error!! =========\n\nIn lvs bash command '. ./lvs/.bashrc'.\n {p_init.stderr}")
		else:
			self.Config.debug_message(2,f".bashrc returncode:{p_init.returncode} => {p_init.stdout}")
			


