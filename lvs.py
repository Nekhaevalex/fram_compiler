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
		self.lvs_dir = (f"{self.pwd}/lvs")

		self.pvslvsctl = (f"{self.pwd}/lvs/pvslvsctl")

		self.create_control(self.pvslvsctl)


		p_init = subprocess.run(f'. {self.pwd}/lvs/.bashrc', capture_output = True ,shell = True , text  = True)

		if (p_init.returncode != 0):
			self.Config.debug_message(2,f".bashrc returncode:{p_init.returncode} => {p_init.stdout}\n ")
			self.Config.debug_message(0,f"\t========== Error!! =========\n\nIn lvs bash command '. ./lvs/.bashrc'.\n {p_init.stderr}")
			self.Config.debug_message(1,f"\nMaybe cadence or Micron PDK not installed or installed inproperly!!!\n ")
		else:
			self.Config.debug_message(2,f".bashrc returncode:{p_init.returncode} => {p_init.stdout}")

			p_lvs = subprocess.run(f'/home/toolkit/cadence/installs/PVS151/bin/pvs -lvs -control {self.pvslvsctl} -top_cell core -spice {self.lvs_dir}/{self.Config.output_name}_ext.sp -source_top_cell core /home/dk/Mikron/HCMOS10_LP/PDK_v1.0_oa/physical/calibre/calibre.lvs > lvs.log')


	def create_control(self,file):
		with open(file,'w') as pvslvsctl:
			pvslvsctl.write(f''' 
			
			text_depth -primary;
			virtual_connect -colon no;
			virtual_connect -semicolon_as_colon yes;
			virtual_connect -noname;
			virtual_connect -report no;
			virtual_connect -depth -primary;
			lvs_ignore_ports no;
			lvs_compare_port_names no;
			lvs_recognize_gates -all;
			lvs_break_ambig_max 32;
			lvs_abort -softchk no;
			lvs_abort -supply_error no;
			lvs_find_shorts no;
			sconnect_upper_shape_count no;
			lvs_report_file "{self.lvs_dir}/report.rep";
			lvs_report_max 50 -mismatched_net_limit 100;
			lvs_run_erc_checks yes;
			lvs_report_opt -none;
			report_summary -erc "{self.lvs_dir}/results/report.sum" -replace;
			max_results -erc 1000;
			results_db -erc "{self.lvs_dir}/results/.erc_errors.ascii" -ascii;
			keep_layers -none;
			abort_on_layout_error yes;
			layout_format gdsii;
			layout_path "./gds_files/{self.Config.output_name}.gds";
			schematic_format spice;
			schematic_path "./netlists/{self.Config.output_name}.sp";
			''')

