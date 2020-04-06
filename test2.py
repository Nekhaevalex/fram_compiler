import subprocess
import os
pwd = os.getcwd()

from config import Config


#subprocess.run('echo "Hello world"',shell = True)

#subprocess.run(f'. ./lvs/.bashrc',shell = True)


Config = Config()

lvs_dir = (f"{pwd}/lvs")

pvslvsctl = (f"{pwd}/lvs/pvslvsctl")


print (f'''
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
lvs_report_file "{lvs_dir}/report.rep";
lvs_report_max 50 -mismatched_net_limit 100;
lvs_run_erc_checks yes;
lvs_report_opt -none;
report_summary -erc "{lvs_dir}/results/report.sum" -replace;
max_results -erc 1000;
results_db -erc "{lvs_dir}/results/.erc_errors.ascii" -ascii;
keep_layers -none;
abort_on_layout_error yes;
layout_format gdsii;
layout_path "./gds_files/{Config.output_name}.gds";
schematic_format spice;
schematic_path "./netlists/{Config.output_name}.sp";
''')





'''
class new_class():
	"""docstring for new_class"""
	def __init__(self, arg):
		self.arg = arg
		self.arg = "arg"+arg
		print(self.arg)

b = "12345"
a = new_class(b)
c = a.arg
print(b)
print(c)
'''

