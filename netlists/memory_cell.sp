* Memory cell subcuircuit
.SUBCKT memory_cell bl wl pl gnd
MM0 net6 wn bl gnd nsvt25 w=0.4 l=0.28
X0 pl net6 conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
.ENDS memory_cell

