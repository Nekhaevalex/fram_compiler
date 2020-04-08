* Library name: fram_cells3
* Cell name: top_driver
* View name: schematic
.SUBCKT top_driver out in bl_gnd vdd gnd
M0 out in vdd vdd psvt25 w=2.0 l=0.28
M3 out in net19 gnd nsvt25 w=2.0 l=0.28
M1 net19 bl_gnd gnd gnd nsvt25 w=2.0 l=0.28
.ENDS top_driver