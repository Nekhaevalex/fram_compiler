* Declare basic devices
* Memory cell subcuircuit
.SUBCKT memory_cell bl wl pl gnd
MM0 net6 wn bl gnd nsvt25 w=0.4 l=0.28
X0 pl net6 conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
.ENDS memory_cell

* Declare subcurcuits
* Declare instances
I0 bl0 wl0 pl0 gnd memory_cell
I1 bl0 wl1 pl1 gnd memory_cell
I2 bl0 wl2 pl2 gnd memory_cell
I3 bl0 wl3 pl3 gnd memory_cell
I4 bl0 wl4 pl4 gnd memory_cell
I5 bl0 wl5 pl5 gnd memory_cell
I6 bl0 wl6 pl6 gnd memory_cell
I7 bl0 wl7 pl7 gnd memory_cell
I8 bl1 wl0 pl0 gnd memory_cell
I9 bl1 wl1 pl1 gnd memory_cell
I10 bl1 wl2 pl2 gnd memory_cell
I11 bl1 wl3 pl3 gnd memory_cell
I12 bl1 wl4 pl4 gnd memory_cell
I13 bl1 wl5 pl5 gnd memory_cell
I14 bl1 wl6 pl6 gnd memory_cell
I15 bl1 wl7 pl7 gnd memory_cell
I16 bl2 wl0 pl0 gnd memory_cell
I17 bl2 wl1 pl1 gnd memory_cell
I18 bl2 wl2 pl2 gnd memory_cell
I19 bl2 wl3 pl3 gnd memory_cell
I20 bl2 wl4 pl4 gnd memory_cell
I21 bl2 wl5 pl5 gnd memory_cell
I22 bl2 wl6 pl6 gnd memory_cell
I23 bl2 wl7 pl7 gnd memory_cell
I24 bl3 wl0 pl0 gnd memory_cell
I25 bl3 wl1 pl1 gnd memory_cell
I26 bl3 wl2 pl2 gnd memory_cell
I27 bl3 wl3 pl3 gnd memory_cell
I28 bl3 wl4 pl4 gnd memory_cell
I29 bl3 wl5 pl5 gnd memory_cell
I30 bl3 wl6 pl6 gnd memory_cell
I31 bl3 wl7 pl7 gnd memory_cell
I32 bl4 wl0 pl0 gnd memory_cell
I33 bl4 wl1 pl1 gnd memory_cell
I34 bl4 wl2 pl2 gnd memory_cell
I35 bl4 wl3 pl3 gnd memory_cell
I36 bl4 wl4 pl4 gnd memory_cell
I37 bl4 wl5 pl5 gnd memory_cell
I38 bl4 wl6 pl6 gnd memory_cell
I39 bl4 wl7 pl7 gnd memory_cell
I40 bl5 wl0 pl0 gnd memory_cell
I41 bl5 wl1 pl1 gnd memory_cell
I42 bl5 wl2 pl2 gnd memory_cell
I43 bl5 wl3 pl3 gnd memory_cell
I44 bl5 wl4 pl4 gnd memory_cell
I45 bl5 wl5 pl5 gnd memory_cell
I46 bl5 wl6 pl6 gnd memory_cell
I47 bl5 wl7 pl7 gnd memory_cell
I48 bl6 wl0 pl0 gnd memory_cell
I49 bl6 wl1 pl1 gnd memory_cell
I50 bl6 wl2 pl2 gnd memory_cell
I51 bl6 wl3 pl3 gnd memory_cell
I52 bl6 wl4 pl4 gnd memory_cell
I53 bl6 wl5 pl5 gnd memory_cell
I54 bl6 wl6 pl6 gnd memory_cell
I55 bl6 wl7 pl7 gnd memory_cell
I56 bl7 wl0 pl0 gnd memory_cell
I57 bl7 wl1 pl1 gnd memory_cell
I58 bl7 wl2 pl2 gnd memory_cell
I59 bl7 wl3 pl3 gnd memory_cell
I60 bl7 wl4 pl4 gnd memory_cell
I61 bl7 wl5 pl5 gnd memory_cell
I62 bl7 wl6 pl6 gnd memory_cell
I63 bl7 wl7 pl7 gnd memory_cell
