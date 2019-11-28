---------------------------------------------------
//Compilation of fram_sample netlist started.2019-11-27 01:58
//Parameters of cell:
//word size = 8
//number of words = 8
 
 
 
simulator lang=spectre
global 0
include models.scs
include conder.va
//-========Subsercuits========-
#Subsercuit sense_amp definition.
subckt sense_amp in nb nt ref seb vdd gnd
M0 (nb seb gnd gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M1 (gnd seb nt gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M2 (nt nb gnd gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M3 (gnd nt nb gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M4 (gnd nt nb gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M5 (net25 seb vdd vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

M6 (net25 ref net33 vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M7 (net29 in net25 vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M8 (nt nb net33 vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M9 (net29 nt nb vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

ends sense_amp
 //REMAINING 10 
//Subsercuit 
 //Cell name:  driver// 

subckt driver not_bl_drive_input bl_out vdd gnd
M10 (vdd not_bl_drive_input net_d0 vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M11 (net_d0 not_bl_drive_input net_d1 vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M12 (net_d1 not_bl_drive_input net_d2 gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1
M13 (net_d2 not_bl_drive_input gnd vdd ) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

ends driver// End of subcircuit definition.

//Subsercuit 
 //Cell name:  memory_cell// 

subckt memory_cell bl wl pl gnd
M10 (bl wl net1 gnd ) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 mismatch=1

I0 conder net1 pl  Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 1e-14
ends memory_cell
// End of subcircuit definition.

I0 ( bl0 nb nt ref seb vdd 0) sense_amp

I1 ( bl_control0 bl0 vdd 0) driver

I2 ( bl0 wl0 pl0 0) memory_cell

I3 ( bl0 wl1 pl1 0) memory_cell

I4 ( bl0 wl2 pl2 0) memory_cell

I5 ( bl0 wl3 pl3 0) memory_cell

I6 ( bl0 wl4 pl4 0) memory_cell

I7 ( bl0 wl5 pl5 0) memory_cell

I8 ( bl0 wl6 pl6 0) memory_cell

I9 ( bl0 wl7 pl7 0) memory_cell

I10 ( bl1 nb nt ref seb vdd 0) sense_amp

I11 ( bl_control1 bl1 vdd 0) driver

I12 ( bl1 wl0 pl0 0) memory_cell

I13 ( bl1 wl1 pl1 0) memory_cell

I14 ( bl1 wl2 pl2 0) memory_cell

I15 ( bl1 wl3 pl3 0) memory_cell

I16 ( bl1 wl4 pl4 0) memory_cell

I17 ( bl1 wl5 pl5 0) memory_cell

I18 ( bl1 wl6 pl6 0) memory_cell

I19 ( bl1 wl7 pl7 0) memory_cell

I20 ( bl2 nb nt ref seb vdd 0) sense_amp

I21 ( bl_control2 bl2 vdd 0) driver

I22 ( bl2 wl0 pl0 0) memory_cell

I23 ( bl2 wl1 pl1 0) memory_cell

I24 ( bl2 wl2 pl2 0) memory_cell

I25 ( bl2 wl3 pl3 0) memory_cell

I26 ( bl2 wl4 pl4 0) memory_cell

I27 ( bl2 wl5 pl5 0) memory_cell

I28 ( bl2 wl6 pl6 0) memory_cell

I29 ( bl2 wl7 pl7 0) memory_cell

I30 ( bl3 nb nt ref seb vdd 0) sense_amp

I31 ( bl_control3 bl3 vdd 0) driver

I32 ( bl3 wl0 pl0 0) memory_cell

I33 ( bl3 wl1 pl1 0) memory_cell

I34 ( bl3 wl2 pl2 0) memory_cell

I35 ( bl3 wl3 pl3 0) memory_cell

I36 ( bl3 wl4 pl4 0) memory_cell

I37 ( bl3 wl5 pl5 0) memory_cell

I38 ( bl3 wl6 pl6 0) memory_cell

I39 ( bl3 wl7 pl7 0) memory_cell

I40 ( bl4 nb nt ref seb vdd 0) sense_amp

I41 ( bl_control4 bl4 vdd 0) driver

I42 ( bl4 wl0 pl0 0) memory_cell

I43 ( bl4 wl1 pl1 0) memory_cell

I44 ( bl4 wl2 pl2 0) memory_cell

I45 ( bl4 wl3 pl3 0) memory_cell

I46 ( bl4 wl4 pl4 0) memory_cell

I47 ( bl4 wl5 pl5 0) memory_cell

I48 ( bl4 wl6 pl6 0) memory_cell

I49 ( bl4 wl7 pl7 0) memory_cell

I50 ( bl5 nb nt ref seb vdd 0) sense_amp

I51 ( bl_control5 bl5 vdd 0) driver

I52 ( bl5 wl0 pl0 0) memory_cell

I53 ( bl5 wl1 pl1 0) memory_cell

I54 ( bl5 wl2 pl2 0) memory_cell

I55 ( bl5 wl3 pl3 0) memory_cell

I56 ( bl5 wl4 pl4 0) memory_cell

I57 ( bl5 wl5 pl5 0) memory_cell

I58 ( bl5 wl6 pl6 0) memory_cell

I59 ( bl5 wl7 pl7 0) memory_cell

I60 ( bl6 nb nt ref seb vdd 0) sense_amp

I61 ( bl_control6 bl6 vdd 0) driver

I62 ( bl6 wl0 pl0 0) memory_cell

I63 ( bl6 wl1 pl1 0) memory_cell

I64 ( bl6 wl2 pl2 0) memory_cell

I65 ( bl6 wl3 pl3 0) memory_cell

I66 ( bl6 wl4 pl4 0) memory_cell

I67 ( bl6 wl5 pl5 0) memory_cell

I68 ( bl6 wl6 pl6 0) memory_cell

I69 ( bl6 wl7 pl7 0) memory_cell

I70 ( bl7 nb nt ref seb vdd 0) sense_amp

I71 ( bl_control7 bl7 vdd 0) driver

I72 ( bl7 wl0 pl0 0) memory_cell

I73 ( bl7 wl1 pl1 0) memory_cell

I74 ( bl7 wl2 pl2 0) memory_cell

I75 ( bl7 wl3 pl3 0) memory_cell

I76 ( bl7 wl4 pl4 0) memory_cell

I77 ( bl7 wl5 pl5 0) memory_cell

I78 ( bl7 wl6 pl6 0) memory_cell

I79 ( bl7 wl7 pl7 0) memory_cell
