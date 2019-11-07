// Generated for: spectre
// Generated on: Nov  7 03:44:44 2019
// Design library name: fram_cells
// Design cell name: small_netlist
// Design view name: schematic
simulator lang=spectre
global 0
include "models.scs"
parameters Vdd=2

// Library name: fram_cells
// Cell name: memory_cell
// View name: schematic
subckt memory_cell bl gnd pl wn
M0 (net6 wn bl gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
    I0 (pl net6) conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
ends memory_cell
// End of subcircuit definition.

// Library name: test1
// Cell name: sense_amp
// View name: schematic
subckt sense_amp gnd in nb nt ref seb vdd
M3 (nb seb gnd gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M2 (gnd seb nt gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M1 (nt nb gnd gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M0 (gnd nt nb gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M8 (net25 seb vdd vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M7 (net25 ref net33 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M6 (net29 in net25 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M5 (nt nb net33 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M4 (net29 nt nb vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
ends sense_amp
// End of subcircuit definition.

// Library name: fram_cells
// Cell name: driver
// View name: schematic
subckt driver gnd in out vdd
M0 (out in net12 gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M3 (gnd in net12 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M2 (net11 in vdd vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M1 (out in net11 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
ends driver
// End of subcircuit definition.

// Library name: fram_cells
// Cell name: small_netlist
// View name: schematic
I1 (bl 0 pl w2) memory_cell
I0 (bl 0 pl w1) memory_cell
I4 (0 bl net010 net09 net011 net012 net08) sense_amp
V1 (vdd 0) vsource dc=Vdd type=dc
V0 (net08 0) vsource dc=Vdd type=dc
I7 (0 net017 bl vdd) driver
simulatorOptions options reltol=1e-3 vabstol=1e-6 iabstol=1e-12 temp=27 \
    tnom=27 scalem=1.0 scale=1.0 gmin=1e-12 rforce=1 maxnotes=5 maxwarns=5 \
    digits=5 cols=80 pivrel=1e-3 sensfile="../psf/sens.output" \
    checklimitdest=psf 
tran tran stop=1000n write="spectre.ic" writefinal="spectre.fc" \
    method=gear2 annotate=status maxiters=5 
finalTimeOP info what=oppoint where=rawfile
modelParameter info what=models where=rawfile
element info what=inst where=rawfile
outputParameter info what=output where=rawfile
designParamVals info what=parameters where=rawfile
primitives info what=primitives where=rawfile
subckts info what=subckts where=rawfile
saveOptions options save=allpub subcktprobelvl=2
ahdl_include "/home/solovyanov_m/work_shell/fram_cells/conder/veriloga/veriloga.va"
