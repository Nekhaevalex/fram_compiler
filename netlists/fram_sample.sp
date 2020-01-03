---------------------------------------------------
//Compilation of fram_sample netlist started.2020-01-03 17:53
//Parameters of cell:
//word size = 16
//number of words = 16
 
 
 
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

I10 ( bl0 wl8 pl8 0) memory_cell

I11 ( bl0 wl9 pl9 0) memory_cell

I12 ( bl0 wl10 pl10 0) memory_cell

I13 ( bl0 wl11 pl11 0) memory_cell

I14 ( bl0 wl12 pl12 0) memory_cell

I15 ( bl0 wl13 pl13 0) memory_cell

I16 ( bl0 wl14 pl14 0) memory_cell

I17 ( bl0 wl15 pl15 0) memory_cell

I18 ( bl1 nb nt ref seb vdd 0) sense_amp

I19 ( bl_control1 bl1 vdd 0) driver

I20 ( bl1 wl0 pl0 0) memory_cell

I21 ( bl1 wl1 pl1 0) memory_cell

I22 ( bl1 wl2 pl2 0) memory_cell

I23 ( bl1 wl3 pl3 0) memory_cell

I24 ( bl1 wl4 pl4 0) memory_cell

I25 ( bl1 wl5 pl5 0) memory_cell

I26 ( bl1 wl6 pl6 0) memory_cell

I27 ( bl1 wl7 pl7 0) memory_cell

I28 ( bl1 wl8 pl8 0) memory_cell

I29 ( bl1 wl9 pl9 0) memory_cell

I30 ( bl1 wl10 pl10 0) memory_cell

I31 ( bl1 wl11 pl11 0) memory_cell

I32 ( bl1 wl12 pl12 0) memory_cell

I33 ( bl1 wl13 pl13 0) memory_cell

I34 ( bl1 wl14 pl14 0) memory_cell

I35 ( bl1 wl15 pl15 0) memory_cell

I36 ( bl2 nb nt ref seb vdd 0) sense_amp

I37 ( bl_control2 bl2 vdd 0) driver

I38 ( bl2 wl0 pl0 0) memory_cell

I39 ( bl2 wl1 pl1 0) memory_cell

I40 ( bl2 wl2 pl2 0) memory_cell

I41 ( bl2 wl3 pl3 0) memory_cell

I42 ( bl2 wl4 pl4 0) memory_cell

I43 ( bl2 wl5 pl5 0) memory_cell

I44 ( bl2 wl6 pl6 0) memory_cell

I45 ( bl2 wl7 pl7 0) memory_cell

I46 ( bl2 wl8 pl8 0) memory_cell

I47 ( bl2 wl9 pl9 0) memory_cell

I48 ( bl2 wl10 pl10 0) memory_cell

I49 ( bl2 wl11 pl11 0) memory_cell

I50 ( bl2 wl12 pl12 0) memory_cell

I51 ( bl2 wl13 pl13 0) memory_cell

I52 ( bl2 wl14 pl14 0) memory_cell

I53 ( bl2 wl15 pl15 0) memory_cell

I54 ( bl3 nb nt ref seb vdd 0) sense_amp

I55 ( bl_control3 bl3 vdd 0) driver

I56 ( bl3 wl0 pl0 0) memory_cell

I57 ( bl3 wl1 pl1 0) memory_cell

I58 ( bl3 wl2 pl2 0) memory_cell

I59 ( bl3 wl3 pl3 0) memory_cell

I60 ( bl3 wl4 pl4 0) memory_cell

I61 ( bl3 wl5 pl5 0) memory_cell

I62 ( bl3 wl6 pl6 0) memory_cell

I63 ( bl3 wl7 pl7 0) memory_cell

I64 ( bl3 wl8 pl8 0) memory_cell

I65 ( bl3 wl9 pl9 0) memory_cell

I66 ( bl3 wl10 pl10 0) memory_cell

I67 ( bl3 wl11 pl11 0) memory_cell

I68 ( bl3 wl12 pl12 0) memory_cell

I69 ( bl3 wl13 pl13 0) memory_cell

I70 ( bl3 wl14 pl14 0) memory_cell

I71 ( bl3 wl15 pl15 0) memory_cell

I72 ( bl4 nb nt ref seb vdd 0) sense_amp

I73 ( bl_control4 bl4 vdd 0) driver

I74 ( bl4 wl0 pl0 0) memory_cell

I75 ( bl4 wl1 pl1 0) memory_cell

I76 ( bl4 wl2 pl2 0) memory_cell

I77 ( bl4 wl3 pl3 0) memory_cell

I78 ( bl4 wl4 pl4 0) memory_cell

I79 ( bl4 wl5 pl5 0) memory_cell

I80 ( bl4 wl6 pl6 0) memory_cell

I81 ( bl4 wl7 pl7 0) memory_cell

I82 ( bl4 wl8 pl8 0) memory_cell

I83 ( bl4 wl9 pl9 0) memory_cell

I84 ( bl4 wl10 pl10 0) memory_cell

I85 ( bl4 wl11 pl11 0) memory_cell

I86 ( bl4 wl12 pl12 0) memory_cell

I87 ( bl4 wl13 pl13 0) memory_cell

I88 ( bl4 wl14 pl14 0) memory_cell

I89 ( bl4 wl15 pl15 0) memory_cell

I90 ( bl5 nb nt ref seb vdd 0) sense_amp

I91 ( bl_control5 bl5 vdd 0) driver

I92 ( bl5 wl0 pl0 0) memory_cell

I93 ( bl5 wl1 pl1 0) memory_cell

I94 ( bl5 wl2 pl2 0) memory_cell

I95 ( bl5 wl3 pl3 0) memory_cell

I96 ( bl5 wl4 pl4 0) memory_cell

I97 ( bl5 wl5 pl5 0) memory_cell

I98 ( bl5 wl6 pl6 0) memory_cell

I99 ( bl5 wl7 pl7 0) memory_cell

I100 ( bl5 wl8 pl8 0) memory_cell

I101 ( bl5 wl9 pl9 0) memory_cell

I102 ( bl5 wl10 pl10 0) memory_cell

I103 ( bl5 wl11 pl11 0) memory_cell

I104 ( bl5 wl12 pl12 0) memory_cell

I105 ( bl5 wl13 pl13 0) memory_cell

I106 ( bl5 wl14 pl14 0) memory_cell

I107 ( bl5 wl15 pl15 0) memory_cell

I108 ( bl6 nb nt ref seb vdd 0) sense_amp

I109 ( bl_control6 bl6 vdd 0) driver

I110 ( bl6 wl0 pl0 0) memory_cell

I111 ( bl6 wl1 pl1 0) memory_cell

I112 ( bl6 wl2 pl2 0) memory_cell

I113 ( bl6 wl3 pl3 0) memory_cell

I114 ( bl6 wl4 pl4 0) memory_cell

I115 ( bl6 wl5 pl5 0) memory_cell

I116 ( bl6 wl6 pl6 0) memory_cell

I117 ( bl6 wl7 pl7 0) memory_cell

I118 ( bl6 wl8 pl8 0) memory_cell

I119 ( bl6 wl9 pl9 0) memory_cell

I120 ( bl6 wl10 pl10 0) memory_cell

I121 ( bl6 wl11 pl11 0) memory_cell

I122 ( bl6 wl12 pl12 0) memory_cell

I123 ( bl6 wl13 pl13 0) memory_cell

I124 ( bl6 wl14 pl14 0) memory_cell

I125 ( bl6 wl15 pl15 0) memory_cell

I126 ( bl7 nb nt ref seb vdd 0) sense_amp

I127 ( bl_control7 bl7 vdd 0) driver

I128 ( bl7 wl0 pl0 0) memory_cell

I129 ( bl7 wl1 pl1 0) memory_cell

I130 ( bl7 wl2 pl2 0) memory_cell

I131 ( bl7 wl3 pl3 0) memory_cell

I132 ( bl7 wl4 pl4 0) memory_cell

I133 ( bl7 wl5 pl5 0) memory_cell

I134 ( bl7 wl6 pl6 0) memory_cell

I135 ( bl7 wl7 pl7 0) memory_cell

I136 ( bl7 wl8 pl8 0) memory_cell

I137 ( bl7 wl9 pl9 0) memory_cell

I138 ( bl7 wl10 pl10 0) memory_cell

I139 ( bl7 wl11 pl11 0) memory_cell

I140 ( bl7 wl12 pl12 0) memory_cell

I141 ( bl7 wl13 pl13 0) memory_cell

I142 ( bl7 wl14 pl14 0) memory_cell

I143 ( bl7 wl15 pl15 0) memory_cell

I144 ( bl8 nb nt ref seb vdd 0) sense_amp

I145 ( bl_control8 bl8 vdd 0) driver

I146 ( bl8 wl0 pl0 0) memory_cell

I147 ( bl8 wl1 pl1 0) memory_cell

I148 ( bl8 wl2 pl2 0) memory_cell

I149 ( bl8 wl3 pl3 0) memory_cell

I150 ( bl8 wl4 pl4 0) memory_cell

I151 ( bl8 wl5 pl5 0) memory_cell

I152 ( bl8 wl6 pl6 0) memory_cell

I153 ( bl8 wl7 pl7 0) memory_cell

I154 ( bl8 wl8 pl8 0) memory_cell

I155 ( bl8 wl9 pl9 0) memory_cell

I156 ( bl8 wl10 pl10 0) memory_cell

I157 ( bl8 wl11 pl11 0) memory_cell

I158 ( bl8 wl12 pl12 0) memory_cell

I159 ( bl8 wl13 pl13 0) memory_cell

I160 ( bl8 wl14 pl14 0) memory_cell

I161 ( bl8 wl15 pl15 0) memory_cell

I162 ( bl9 nb nt ref seb vdd 0) sense_amp

I163 ( bl_control9 bl9 vdd 0) driver

I164 ( bl9 wl0 pl0 0) memory_cell

I165 ( bl9 wl1 pl1 0) memory_cell

I166 ( bl9 wl2 pl2 0) memory_cell

I167 ( bl9 wl3 pl3 0) memory_cell

I168 ( bl9 wl4 pl4 0) memory_cell

I169 ( bl9 wl5 pl5 0) memory_cell

I170 ( bl9 wl6 pl6 0) memory_cell

I171 ( bl9 wl7 pl7 0) memory_cell

I172 ( bl9 wl8 pl8 0) memory_cell

I173 ( bl9 wl9 pl9 0) memory_cell

I174 ( bl9 wl10 pl10 0) memory_cell

I175 ( bl9 wl11 pl11 0) memory_cell

I176 ( bl9 wl12 pl12 0) memory_cell

I177 ( bl9 wl13 pl13 0) memory_cell

I178 ( bl9 wl14 pl14 0) memory_cell

I179 ( bl9 wl15 pl15 0) memory_cell

I180 ( bl10 nb nt ref seb vdd 0) sense_amp

I181 ( bl_control10 bl10 vdd 0) driver

I182 ( bl10 wl0 pl0 0) memory_cell

I183 ( bl10 wl1 pl1 0) memory_cell

I184 ( bl10 wl2 pl2 0) memory_cell

I185 ( bl10 wl3 pl3 0) memory_cell

I186 ( bl10 wl4 pl4 0) memory_cell

I187 ( bl10 wl5 pl5 0) memory_cell

I188 ( bl10 wl6 pl6 0) memory_cell

I189 ( bl10 wl7 pl7 0) memory_cell

I190 ( bl10 wl8 pl8 0) memory_cell

I191 ( bl10 wl9 pl9 0) memory_cell

I192 ( bl10 wl10 pl10 0) memory_cell

I193 ( bl10 wl11 pl11 0) memory_cell

I194 ( bl10 wl12 pl12 0) memory_cell

I195 ( bl10 wl13 pl13 0) memory_cell

I196 ( bl10 wl14 pl14 0) memory_cell

I197 ( bl10 wl15 pl15 0) memory_cell

I198 ( bl11 nb nt ref seb vdd 0) sense_amp

I199 ( bl_control11 bl11 vdd 0) driver

I200 ( bl11 wl0 pl0 0) memory_cell

I201 ( bl11 wl1 pl1 0) memory_cell

I202 ( bl11 wl2 pl2 0) memory_cell

I203 ( bl11 wl3 pl3 0) memory_cell

I204 ( bl11 wl4 pl4 0) memory_cell

I205 ( bl11 wl5 pl5 0) memory_cell

I206 ( bl11 wl6 pl6 0) memory_cell

I207 ( bl11 wl7 pl7 0) memory_cell

I208 ( bl11 wl8 pl8 0) memory_cell

I209 ( bl11 wl9 pl9 0) memory_cell

I210 ( bl11 wl10 pl10 0) memory_cell

I211 ( bl11 wl11 pl11 0) memory_cell

I212 ( bl11 wl12 pl12 0) memory_cell

I213 ( bl11 wl13 pl13 0) memory_cell

I214 ( bl11 wl14 pl14 0) memory_cell

I215 ( bl11 wl15 pl15 0) memory_cell

I216 ( bl12 nb nt ref seb vdd 0) sense_amp

I217 ( bl_control12 bl12 vdd 0) driver

I218 ( bl12 wl0 pl0 0) memory_cell

I219 ( bl12 wl1 pl1 0) memory_cell

I220 ( bl12 wl2 pl2 0) memory_cell

I221 ( bl12 wl3 pl3 0) memory_cell

I222 ( bl12 wl4 pl4 0) memory_cell

I223 ( bl12 wl5 pl5 0) memory_cell

I224 ( bl12 wl6 pl6 0) memory_cell

I225 ( bl12 wl7 pl7 0) memory_cell

I226 ( bl12 wl8 pl8 0) memory_cell

I227 ( bl12 wl9 pl9 0) memory_cell

I228 ( bl12 wl10 pl10 0) memory_cell

I229 ( bl12 wl11 pl11 0) memory_cell

I230 ( bl12 wl12 pl12 0) memory_cell

I231 ( bl12 wl13 pl13 0) memory_cell

I232 ( bl12 wl14 pl14 0) memory_cell

I233 ( bl12 wl15 pl15 0) memory_cell

I234 ( bl13 nb nt ref seb vdd 0) sense_amp

I235 ( bl_control13 bl13 vdd 0) driver

I236 ( bl13 wl0 pl0 0) memory_cell

I237 ( bl13 wl1 pl1 0) memory_cell

I238 ( bl13 wl2 pl2 0) memory_cell

I239 ( bl13 wl3 pl3 0) memory_cell

I240 ( bl13 wl4 pl4 0) memory_cell

I241 ( bl13 wl5 pl5 0) memory_cell

I242 ( bl13 wl6 pl6 0) memory_cell

I243 ( bl13 wl7 pl7 0) memory_cell

I244 ( bl13 wl8 pl8 0) memory_cell

I245 ( bl13 wl9 pl9 0) memory_cell

I246 ( bl13 wl10 pl10 0) memory_cell

I247 ( bl13 wl11 pl11 0) memory_cell

I248 ( bl13 wl12 pl12 0) memory_cell

I249 ( bl13 wl13 pl13 0) memory_cell

I250 ( bl13 wl14 pl14 0) memory_cell

I251 ( bl13 wl15 pl15 0) memory_cell

I252 ( bl14 nb nt ref seb vdd 0) sense_amp

I253 ( bl_control14 bl14 vdd 0) driver

I254 ( bl14 wl0 pl0 0) memory_cell

I255 ( bl14 wl1 pl1 0) memory_cell

I256 ( bl14 wl2 pl2 0) memory_cell

I257 ( bl14 wl3 pl3 0) memory_cell

I258 ( bl14 wl4 pl4 0) memory_cell

I259 ( bl14 wl5 pl5 0) memory_cell

I260 ( bl14 wl6 pl6 0) memory_cell

I261 ( bl14 wl7 pl7 0) memory_cell

I262 ( bl14 wl8 pl8 0) memory_cell

I263 ( bl14 wl9 pl9 0) memory_cell

I264 ( bl14 wl10 pl10 0) memory_cell

I265 ( bl14 wl11 pl11 0) memory_cell

I266 ( bl14 wl12 pl12 0) memory_cell

I267 ( bl14 wl13 pl13 0) memory_cell

I268 ( bl14 wl14 pl14 0) memory_cell

I269 ( bl14 wl15 pl15 0) memory_cell

I270 ( bl15 nb nt ref seb vdd 0) sense_amp

I271 ( bl_control15 bl15 vdd 0) driver

I272 ( bl15 wl0 pl0 0) memory_cell

I273 ( bl15 wl1 pl1 0) memory_cell

I274 ( bl15 wl2 pl2 0) memory_cell

I275 ( bl15 wl3 pl3 0) memory_cell

I276 ( bl15 wl4 pl4 0) memory_cell

I277 ( bl15 wl5 pl5 0) memory_cell

I278 ( bl15 wl6 pl6 0) memory_cell

I279 ( bl15 wl7 pl7 0) memory_cell

I280 ( bl15 wl8 pl8 0) memory_cell

I281 ( bl15 wl9 pl9 0) memory_cell

I282 ( bl15 wl10 pl10 0) memory_cell

I283 ( bl15 wl11 pl11 0) memory_cell

I284 ( bl15 wl12 pl12 0) memory_cell

I285 ( bl15 wl13 pl13 0) memory_cell

I286 ( bl15 wl14 pl14 0) memory_cell

I287 ( bl15 wl15 pl15 0) memory_cell
