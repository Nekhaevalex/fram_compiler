* Declare basic devices
* Memory cell subcuircuit
.SUBCKT memory_cell bl wl pl gnd
MM0 net6 wn bl gnd nsvt25 w=0.4 l=0.28
*X0 pl net6 conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
.ENDS memory_cell

* sense_amp subcuircuit
.SUBCKT sense_amp in ref seb nb nt vdd gnd
M3 nb seb gnd gnd nsvt25 w=0.4 l=0.28
M2 gnd seb nt gnd nsvt25 w=0.4 l=0.28
M1 nt nb gnd gnd nsvt25 w=0.4 l=0.28
M0 gnd nt nb gnd nsvt25 w=0.4 l=0.28
M8 net25 seb vdd vdd psvt25 w=0.4 l=0.28
M7 net25 ref net33 vdd psvt25 w=0.4 l=0.28
M6 net29 in net25 vdd psvt25 w=0.4 l=0.28
M5 nt nb net33 vdd psvt25 w=0.4 l=0.28
M4 net29 nt nb vdd psvt25 w=0.4 l=0.28
* SA
.ENDS
* Library name: fram_cells3
* Cell name: top_driver
* View name: schematic
.SUBCKT top_driver out in bl_gnd vdd gnd
M0 out in vdd vdd psvt25 w=2.0 l=0.28
M3 out in net19 gnd nsvt25 w=2.0 l=0.28
M1 net19 bl_gnd gnd gnd nsvt25 w=2.0 l=0.28
.ENDS top_driver* Declare subcurcuits
* Declare instances
X0 bl0 wl0 pl0 gnd memory_cell
X1 bl0 wl1 pl1 gnd memory_cell
X2 bl0 wl2 pl2 gnd memory_cell
X3 bl0 wl3 pl3 gnd memory_cell
X4 bl1 wl0 pl0 gnd memory_cell
X5 bl1 wl1 pl1 gnd memory_cell
X6 bl1 wl2 pl2 gnd memory_cell
X7 bl1 wl3 pl3 gnd memory_cell
X8 bl2 wl0 pl0 gnd memory_cell
X9 bl2 wl1 pl1 gnd memory_cell
X10 bl2 wl2 pl2 gnd memory_cell
X11 bl2 wl3 pl3 gnd memory_cell
X12 bl3 wl0 pl0 gnd memory_cell
X13 bl3 wl1 pl1 gnd memory_cell
X14 bl3 wl2 pl2 gnd memory_cell
X15 bl3 wl3 pl3 gnd memory_cell
X16 bl0 ref seb nb nt vdd gnd sense_amp
X17 bl1 ref seb nb nt vdd gnd sense_amp
X18 bl2 ref seb nb nt vdd gnd sense_amp
X19 bl3 ref seb nb nt vdd gnd sense_amp
X20 bl0 in bl_gnd vdd gnd top_driver
X21 bl1 in bl_gnd vdd gnd top_driver
X22 bl2 in bl_gnd vdd gnd top_driver
X23 bl3 in bl_gnd vdd gnd top_driver
* End of netlist. Compiled by NCS Memory compiler.