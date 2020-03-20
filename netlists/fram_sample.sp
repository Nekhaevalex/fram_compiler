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
I0 in ref seb nb nt vdd gnd sense_amp
I1 in ref seb nb nt vdd gnd sense_amp
I2 in ref seb nb nt vdd gnd sense_amp
I3 in ref seb nb nt vdd gnd sense_amp
I4 in ref seb nb nt vdd gnd sense_amp
I5 in ref seb nb nt vdd gnd sense_amp
I6 in ref seb nb nt vdd gnd sense_amp
I7 in ref seb nb nt vdd gnd sense_amp
I8 bl0 wl0 pl0 gnd memory_cell
I9 bl0 wl1 pl1 gnd memory_cell
I10 bl0 wl2 pl2 gnd memory_cell
I11 bl0 wl3 pl3 gnd memory_cell
I12 bl0 wl4 pl4 gnd memory_cell
I13 bl0 wl5 pl5 gnd memory_cell
I14 bl0 wl6 pl6 gnd memory_cell
I15 bl0 wl7 pl7 gnd memory_cell
I16 bl1 wl0 pl0 gnd memory_cell
I17 bl1 wl1 pl1 gnd memory_cell
I18 bl1 wl2 pl2 gnd memory_cell
I19 bl1 wl3 pl3 gnd memory_cell
I20 bl1 wl4 pl4 gnd memory_cell
I21 bl1 wl5 pl5 gnd memory_cell
I22 bl1 wl6 pl6 gnd memory_cell
I23 bl1 wl7 pl7 gnd memory_cell
I24 bl2 wl0 pl0 gnd memory_cell
I25 bl2 wl1 pl1 gnd memory_cell
I26 bl2 wl2 pl2 gnd memory_cell
I27 bl2 wl3 pl3 gnd memory_cell
I28 bl2 wl4 pl4 gnd memory_cell
I29 bl2 wl5 pl5 gnd memory_cell
I30 bl2 wl6 pl6 gnd memory_cell
I31 bl2 wl7 pl7 gnd memory_cell
I32 bl3 wl0 pl0 gnd memory_cell
I33 bl3 wl1 pl1 gnd memory_cell
I34 bl3 wl2 pl2 gnd memory_cell
I35 bl3 wl3 pl3 gnd memory_cell
I36 bl3 wl4 pl4 gnd memory_cell
I37 bl3 wl5 pl5 gnd memory_cell
I38 bl3 wl6 pl6 gnd memory_cell
I39 bl3 wl7 pl7 gnd memory_cell
I40 bl4 wl0 pl0 gnd memory_cell
I41 bl4 wl1 pl1 gnd memory_cell
I42 bl4 wl2 pl2 gnd memory_cell
I43 bl4 wl3 pl3 gnd memory_cell
I44 bl4 wl4 pl4 gnd memory_cell
I45 bl4 wl5 pl5 gnd memory_cell
I46 bl4 wl6 pl6 gnd memory_cell
I47 bl4 wl7 pl7 gnd memory_cell
I48 bl5 wl0 pl0 gnd memory_cell
I49 bl5 wl1 pl1 gnd memory_cell
I50 bl5 wl2 pl2 gnd memory_cell
I51 bl5 wl3 pl3 gnd memory_cell
I52 bl5 wl4 pl4 gnd memory_cell
I53 bl5 wl5 pl5 gnd memory_cell
I54 bl5 wl6 pl6 gnd memory_cell
I55 bl5 wl7 pl7 gnd memory_cell
I56 bl6 wl0 pl0 gnd memory_cell
I57 bl6 wl1 pl1 gnd memory_cell
I58 bl6 wl2 pl2 gnd memory_cell
I59 bl6 wl3 pl3 gnd memory_cell
I60 bl6 wl4 pl4 gnd memory_cell
I61 bl6 wl5 pl5 gnd memory_cell
I62 bl6 wl6 pl6 gnd memory_cell
I63 bl6 wl7 pl7 gnd memory_cell
I64 bl7 wl0 pl0 gnd memory_cell
I65 bl7 wl1 pl1 gnd memory_cell
I66 bl7 wl2 pl2 gnd memory_cell
I67 bl7 wl3 pl3 gnd memory_cell
I68 bl7 wl4 pl4 gnd memory_cell
I69 bl7 wl5 pl5 gnd memory_cell
I70 bl7 wl6 pl6 gnd memory_cell
I71 bl7 wl7 pl7 gnd memory_cell
