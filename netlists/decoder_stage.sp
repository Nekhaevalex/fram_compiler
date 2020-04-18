// Library name: fram_cells5
// Cell name: 2bit_decoder
// View name: schematic
subckt fram_cells5_2bit_decoder_schematic IN1 IN2 gnd out vdd
M2 (net20 IN2 gnd gnd) nsvt25 w=0.4 l=0.28 
M0 (out IN1 net20 gnd) nsvt25 w=0.4 l=0.28 
M3 (out IN1 vdd vdd) psvt25 w=0.4 l=0.28 
M1 (out IN2 vdd vdd) psvt25 w=0.4 l=0.28 
ends fram_cells5_2bit_decoder_schematic
// End of subcircuit definition.

// Library name: fram_cells5
// Cell name: 1u_invertor
// View name: schematic
subckt fram_cells5_1u_invertor_schematic gnd in out vdd
M0 (out in gnd gnd) nsvt25 w=1.0 l=0.28 
M1 (out in vdd vdd) psvt25 w=1.0 l=0.28 
ends fram_cells5_1u_invertor_schematic
// End of subcircuit definition.

// Library name: fram_cells5
// Cell name: decoder_stage
// View name: schematic
I1 (addr npre gnd net1 vdd) fram_cells5_2bit_decoder_schematic
I0 (addr pre gnd net2 vdd) fram_cells5_2bit_decoder_schematic
I3 (gnd net1 WL0 vdd) fram_cells5_1u_invertor_schematic
I2 (gnd net2 WL1 vdd) fram_cells5_1u_invertor_schematic
M2 (addr naddr gnd gnd) nsvt25 w=0.4 l=0.28 
M0 (npre pre gnd gnd) nsvt25 w=0.4 l=0.28 
M3 (addr naddr vdd vdd) psvt25 w=0.4 l=0.28 
M1 (npre pre vdd vdd) psvt25 w=0.4 l=0.28 