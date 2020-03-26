* Declare basic devices
* Memory cell subcuircuit
.SUBCKT memory_cell bl wl pl gnd
MM0 net6 wn bl gnd nsvt25 w=0.4 l=0.28
X0 pl net6 conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
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
* Declare subcurcuits
* Declare instances
I0 bl0 ref seb nb nt vdd gnd sense_amp
I1 bl1 ref seb nb nt vdd gnd sense_amp
I2 bl2 ref seb nb nt vdd gnd sense_amp
I3 bl3 ref seb nb nt vdd gnd sense_amp
I4 bl0 wl0 pl0 gnd memory_cell
I5 bl0 wl1 pl1 gnd memory_cell
I6 bl0 wl2 pl2 gnd memory_cell
I7 bl0 wl3 pl3 gnd memory_cell
I8 bl1 wl0 pl0 gnd memory_cell
I9 bl1 wl1 pl1 gnd memory_cell
I10 bl1 wl2 pl2 gnd memory_cell
I11 bl1 wl3 pl3 gnd memory_cell
I12 bl2 wl0 pl0 gnd memory_cell
I13 bl2 wl1 pl1 gnd memory_cell
I14 bl2 wl2 pl2 gnd memory_cell
I15 bl2 wl3 pl3 gnd memory_cell
I16 bl3 wl0 pl0 gnd memory_cell
I17 bl3 wl1 pl1 gnd memory_cell
I18 bl3 wl2 pl2 gnd memory_cell
I19 bl3 wl3 pl3 gnd memory_cell
