// Generated on: Apr 27 18:41:09 2020 (NCS design MIPT)
// Design library name: fram_cells5
// Design cell name: mos_pair_t
// Design view name: schematic
// Library name: fram_cells5
// Cell name: mos_pair
// View name: schematic
subckt mos_pair_vdd gnd in in_p out_n out_p vdd
M0 (out_n in in_p gnd) nsvt25 w=0.4 l=0.28
M1 (out_p in vdd vdd) psvt25 w=0.4 l=0.28
ends mos_pair
// End of subcircuit definition.
