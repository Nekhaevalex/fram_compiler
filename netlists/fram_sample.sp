* Declare basic devices
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
X16 bl4 wl0 pl0 gnd memory_cell
X17 bl4 wl1 pl1 gnd memory_cell
X18 bl4 wl2 pl2 gnd memory_cell
X19 bl4 wl3 pl3 gnd memory_cell
X20 bl5 wl0 pl0 gnd memory_cell
X21 bl5 wl1 pl1 gnd memory_cell
X22 bl5 wl2 pl2 gnd memory_cell
X23 bl5 wl3 pl3 gnd memory_cell
X24 bl6 wl0 pl0 gnd memory_cell
X25 bl6 wl1 pl1 gnd memory_cell
X26 bl6 wl2 pl2 gnd memory_cell
X27 bl6 wl3 pl3 gnd memory_cell
X28 bl7 wl0 pl0 gnd memory_cell
X29 bl7 wl1 pl1 gnd memory_cell
X30 bl7 wl2 pl2 gnd memory_cell
X31 bl7 wl3 pl3 gnd memory_cell
X32 bl8 wl0 pl0 gnd memory_cell
X33 bl8 wl1 pl1 gnd memory_cell
X34 bl8 wl2 pl2 gnd memory_cell
X35 bl8 wl3 pl3 gnd memory_cell
X36 bl9 wl0 pl0 gnd memory_cell
X37 bl9 wl1 pl1 gnd memory_cell
X38 bl9 wl2 pl2 gnd memory_cell
X39 bl9 wl3 pl3 gnd memory_cell
X40 bl10 wl0 pl0 gnd memory_cell
X41 bl10 wl1 pl1 gnd memory_cell
X42 bl10 wl2 pl2 gnd memory_cell
X43 bl10 wl3 pl3 gnd memory_cell
X44 bl11 wl0 pl0 gnd memory_cell
X45 bl11 wl1 pl1 gnd memory_cell
X46 bl11 wl2 pl2 gnd memory_cell
X47 bl11 wl3 pl3 gnd memory_cell
X48 bl12 wl0 pl0 gnd memory_cell
X49 bl12 wl1 pl1 gnd memory_cell
X50 bl12 wl2 pl2 gnd memory_cell
X51 bl12 wl3 pl3 gnd memory_cell
X52 bl13 wl0 pl0 gnd memory_cell
X53 bl13 wl1 pl1 gnd memory_cell
X54 bl13 wl2 pl2 gnd memory_cell
X55 bl13 wl3 pl3 gnd memory_cell
X56 bl14 wl0 pl0 gnd memory_cell
X57 bl14 wl1 pl1 gnd memory_cell
X58 bl14 wl2 pl2 gnd memory_cell
X59 bl14 wl3 pl3 gnd memory_cell
X60 bl15 wl0 pl0 gnd memory_cell
X61 bl15 wl1 pl1 gnd memory_cell
X62 bl15 wl2 pl2 gnd memory_cell
X63 bl15 wl3 pl3 gnd memory_cell
X64 bl16 wl0 pl0 gnd memory_cell
X65 bl16 wl1 pl1 gnd memory_cell
X66 bl16 wl2 pl2 gnd memory_cell
X67 bl16 wl3 pl3 gnd memory_cell
X68 bl17 wl0 pl0 gnd memory_cell
X69 bl17 wl1 pl1 gnd memory_cell
X70 bl17 wl2 pl2 gnd memory_cell
X71 bl17 wl3 pl3 gnd memory_cell
X72 bl18 wl0 pl0 gnd memory_cell
X73 bl18 wl1 pl1 gnd memory_cell
X74 bl18 wl2 pl2 gnd memory_cell
X75 bl18 wl3 pl3 gnd memory_cell
X76 bl19 wl0 pl0 gnd memory_cell
X77 bl19 wl1 pl1 gnd memory_cell
X78 bl19 wl2 pl2 gnd memory_cell
X79 bl19 wl3 pl3 gnd memory_cell
X80 bl20 wl0 pl0 gnd memory_cell
X81 bl20 wl1 pl1 gnd memory_cell
X82 bl20 wl2 pl2 gnd memory_cell
X83 bl20 wl3 pl3 gnd memory_cell
X84 bl21 wl0 pl0 gnd memory_cell
X85 bl21 wl1 pl1 gnd memory_cell
X86 bl21 wl2 pl2 gnd memory_cell
X87 bl21 wl3 pl3 gnd memory_cell
X88 bl22 wl0 pl0 gnd memory_cell
X89 bl22 wl1 pl1 gnd memory_cell
X90 bl22 wl2 pl2 gnd memory_cell
X91 bl22 wl3 pl3 gnd memory_cell
X92 bl23 wl0 pl0 gnd memory_cell
X93 bl23 wl1 pl1 gnd memory_cell
X94 bl23 wl2 pl2 gnd memory_cell
X95 bl23 wl3 pl3 gnd memory_cell
X96 bl24 wl0 pl0 gnd memory_cell
X97 bl24 wl1 pl1 gnd memory_cell
X98 bl24 wl2 pl2 gnd memory_cell
X99 bl24 wl3 pl3 gnd memory_cell
X100 bl25 wl0 pl0 gnd memory_cell
X101 bl25 wl1 pl1 gnd memory_cell
X102 bl25 wl2 pl2 gnd memory_cell
X103 bl25 wl3 pl3 gnd memory_cell
X104 bl26 wl0 pl0 gnd memory_cell
X105 bl26 wl1 pl1 gnd memory_cell
X106 bl26 wl2 pl2 gnd memory_cell
X107 bl26 wl3 pl3 gnd memory_cell
X108 bl27 wl0 pl0 gnd memory_cell
X109 bl27 wl1 pl1 gnd memory_cell
X110 bl27 wl2 pl2 gnd memory_cell
X111 bl27 wl3 pl3 gnd memory_cell
X112 bl28 wl0 pl0 gnd memory_cell
X113 bl28 wl1 pl1 gnd memory_cell
X114 bl28 wl2 pl2 gnd memory_cell
X115 bl28 wl3 pl3 gnd memory_cell
X116 bl29 wl0 pl0 gnd memory_cell
X117 bl29 wl1 pl1 gnd memory_cell
X118 bl29 wl2 pl2 gnd memory_cell
X119 bl29 wl3 pl3 gnd memory_cell
X120 bl30 wl0 pl0 gnd memory_cell
X121 bl30 wl1 pl1 gnd memory_cell
X122 bl30 wl2 pl2 gnd memory_cell
X123 bl30 wl3 pl3 gnd memory_cell
X124 bl31 wl0 pl0 gnd memory_cell
X125 bl31 wl1 pl1 gnd memory_cell
X126 bl31 wl2 pl2 gnd memory_cell
X127 bl31 wl3 pl3 gnd memory_cell
X128 bl32 wl0 pl0 gnd memory_cell
X129 bl32 wl1 pl1 gnd memory_cell
X130 bl32 wl2 pl2 gnd memory_cell
X131 bl32 wl3 pl3 gnd memory_cell
X132 bl33 wl0 pl0 gnd memory_cell
X133 bl33 wl1 pl1 gnd memory_cell
X134 bl33 wl2 pl2 gnd memory_cell
X135 bl33 wl3 pl3 gnd memory_cell
X136 bl34 wl0 pl0 gnd memory_cell
X137 bl34 wl1 pl1 gnd memory_cell
X138 bl34 wl2 pl2 gnd memory_cell
X139 bl34 wl3 pl3 gnd memory_cell
X140 bl35 wl0 pl0 gnd memory_cell
X141 bl35 wl1 pl1 gnd memory_cell
X142 bl35 wl2 pl2 gnd memory_cell
X143 bl35 wl3 pl3 gnd memory_cell
X144 bl36 wl0 pl0 gnd memory_cell
X145 bl36 wl1 pl1 gnd memory_cell
X146 bl36 wl2 pl2 gnd memory_cell
X147 bl36 wl3 pl3 gnd memory_cell
X148 bl37 wl0 pl0 gnd memory_cell
X149 bl37 wl1 pl1 gnd memory_cell
X150 bl37 wl2 pl2 gnd memory_cell
X151 bl37 wl3 pl3 gnd memory_cell
X152 bl38 wl0 pl0 gnd memory_cell
X153 bl38 wl1 pl1 gnd memory_cell
X154 bl38 wl2 pl2 gnd memory_cell
X155 bl38 wl3 pl3 gnd memory_cell
X156 bl39 wl0 pl0 gnd memory_cell
X157 bl39 wl1 pl1 gnd memory_cell
X158 bl39 wl2 pl2 gnd memory_cell
X159 bl39 wl3 pl3 gnd memory_cell
X160 bl40 wl0 pl0 gnd memory_cell
X161 bl40 wl1 pl1 gnd memory_cell
X162 bl40 wl2 pl2 gnd memory_cell
X163 bl40 wl3 pl3 gnd memory_cell
X164 bl41 wl0 pl0 gnd memory_cell
X165 bl41 wl1 pl1 gnd memory_cell
X166 bl41 wl2 pl2 gnd memory_cell
X167 bl41 wl3 pl3 gnd memory_cell
X168 bl42 wl0 pl0 gnd memory_cell
X169 bl42 wl1 pl1 gnd memory_cell
X170 bl42 wl2 pl2 gnd memory_cell
X171 bl42 wl3 pl3 gnd memory_cell
X172 bl43 wl0 pl0 gnd memory_cell
X173 bl43 wl1 pl1 gnd memory_cell
X174 bl43 wl2 pl2 gnd memory_cell
X175 bl43 wl3 pl3 gnd memory_cell
X176 bl44 wl0 pl0 gnd memory_cell
X177 bl44 wl1 pl1 gnd memory_cell
X178 bl44 wl2 pl2 gnd memory_cell
X179 bl44 wl3 pl3 gnd memory_cell
X180 bl45 wl0 pl0 gnd memory_cell
X181 bl45 wl1 pl1 gnd memory_cell
X182 bl45 wl2 pl2 gnd memory_cell
X183 bl45 wl3 pl3 gnd memory_cell
X184 bl46 wl0 pl0 gnd memory_cell
X185 bl46 wl1 pl1 gnd memory_cell
X186 bl46 wl2 pl2 gnd memory_cell
X187 bl46 wl3 pl3 gnd memory_cell
X188 bl47 wl0 pl0 gnd memory_cell
X189 bl47 wl1 pl1 gnd memory_cell
X190 bl47 wl2 pl2 gnd memory_cell
X191 bl47 wl3 pl3 gnd memory_cell
X192 bl48 wl0 pl0 gnd memory_cell
X193 bl48 wl1 pl1 gnd memory_cell
X194 bl48 wl2 pl2 gnd memory_cell
X195 bl48 wl3 pl3 gnd memory_cell
X196 bl49 wl0 pl0 gnd memory_cell
X197 bl49 wl1 pl1 gnd memory_cell
X198 bl49 wl2 pl2 gnd memory_cell
X199 bl49 wl3 pl3 gnd memory_cell
X200 bl50 wl0 pl0 gnd memory_cell
X201 bl50 wl1 pl1 gnd memory_cell
X202 bl50 wl2 pl2 gnd memory_cell
X203 bl50 wl3 pl3 gnd memory_cell
X204 bl51 wl0 pl0 gnd memory_cell
X205 bl51 wl1 pl1 gnd memory_cell
X206 bl51 wl2 pl2 gnd memory_cell
X207 bl51 wl3 pl3 gnd memory_cell
X208 bl52 wl0 pl0 gnd memory_cell
X209 bl52 wl1 pl1 gnd memory_cell
X210 bl52 wl2 pl2 gnd memory_cell
X211 bl52 wl3 pl3 gnd memory_cell
X212 bl53 wl0 pl0 gnd memory_cell
X213 bl53 wl1 pl1 gnd memory_cell
X214 bl53 wl2 pl2 gnd memory_cell
X215 bl53 wl3 pl3 gnd memory_cell
X216 bl54 wl0 pl0 gnd memory_cell
X217 bl54 wl1 pl1 gnd memory_cell
X218 bl54 wl2 pl2 gnd memory_cell
X219 bl54 wl3 pl3 gnd memory_cell
X220 bl55 wl0 pl0 gnd memory_cell
X221 bl55 wl1 pl1 gnd memory_cell
X222 bl55 wl2 pl2 gnd memory_cell
X223 bl55 wl3 pl3 gnd memory_cell
X224 bl56 wl0 pl0 gnd memory_cell
X225 bl56 wl1 pl1 gnd memory_cell
X226 bl56 wl2 pl2 gnd memory_cell
X227 bl56 wl3 pl3 gnd memory_cell
X228 bl57 wl0 pl0 gnd memory_cell
X229 bl57 wl1 pl1 gnd memory_cell
X230 bl57 wl2 pl2 gnd memory_cell
X231 bl57 wl3 pl3 gnd memory_cell
X232 bl58 wl0 pl0 gnd memory_cell
X233 bl58 wl1 pl1 gnd memory_cell
X234 bl58 wl2 pl2 gnd memory_cell
X235 bl58 wl3 pl3 gnd memory_cell
X236 bl59 wl0 pl0 gnd memory_cell
X237 bl59 wl1 pl1 gnd memory_cell
X238 bl59 wl2 pl2 gnd memory_cell
X239 bl59 wl3 pl3 gnd memory_cell
X240 bl60 wl0 pl0 gnd memory_cell
X241 bl60 wl1 pl1 gnd memory_cell
X242 bl60 wl2 pl2 gnd memory_cell
X243 bl60 wl3 pl3 gnd memory_cell
X244 bl61 wl0 pl0 gnd memory_cell
X245 bl61 wl1 pl1 gnd memory_cell
X246 bl61 wl2 pl2 gnd memory_cell
X247 bl61 wl3 pl3 gnd memory_cell
X248 bl62 wl0 pl0 gnd memory_cell
X249 bl62 wl1 pl1 gnd memory_cell
X250 bl62 wl2 pl2 gnd memory_cell
X251 bl62 wl3 pl3 gnd memory_cell
X252 bl63 wl0 pl0 gnd memory_cell
X253 bl63 wl1 pl1 gnd memory_cell
X254 bl63 wl2 pl2 gnd memory_cell
X255 bl63 wl3 pl3 gnd memory_cell
X256 bl0 ref seb nb nt vdd gnd sense_amp
X257 bl1 ref seb nb nt vdd gnd sense_amp
X258 bl2 ref seb nb nt vdd gnd sense_amp
X259 bl3 ref seb nb nt vdd gnd sense_amp
X260 bl4 ref seb nb nt vdd gnd sense_amp
X261 bl5 ref seb nb nt vdd gnd sense_amp
X262 bl6 ref seb nb nt vdd gnd sense_amp
X263 bl7 ref seb nb nt vdd gnd sense_amp
X264 bl8 ref seb nb nt vdd gnd sense_amp
X265 bl9 ref seb nb nt vdd gnd sense_amp
X266 bl10 ref seb nb nt vdd gnd sense_amp
X267 bl11 ref seb nb nt vdd gnd sense_amp
X268 bl12 ref seb nb nt vdd gnd sense_amp
X269 bl13 ref seb nb nt vdd gnd sense_amp
X270 bl14 ref seb nb nt vdd gnd sense_amp
X271 bl15 ref seb nb nt vdd gnd sense_amp
X272 bl16 ref seb nb nt vdd gnd sense_amp
X273 bl17 ref seb nb nt vdd gnd sense_amp
X274 bl18 ref seb nb nt vdd gnd sense_amp
X275 bl19 ref seb nb nt vdd gnd sense_amp
X276 bl20 ref seb nb nt vdd gnd sense_amp
X277 bl21 ref seb nb nt vdd gnd sense_amp
X278 bl22 ref seb nb nt vdd gnd sense_amp
X279 bl23 ref seb nb nt vdd gnd sense_amp
X280 bl24 ref seb nb nt vdd gnd sense_amp
X281 bl25 ref seb nb nt vdd gnd sense_amp
X282 bl26 ref seb nb nt vdd gnd sense_amp
X283 bl27 ref seb nb nt vdd gnd sense_amp
X284 bl28 ref seb nb nt vdd gnd sense_amp
X285 bl29 ref seb nb nt vdd gnd sense_amp
X286 bl30 ref seb nb nt vdd gnd sense_amp
X287 bl31 ref seb nb nt vdd gnd sense_amp
X288 bl32 ref seb nb nt vdd gnd sense_amp
X289 bl33 ref seb nb nt vdd gnd sense_amp
X290 bl34 ref seb nb nt vdd gnd sense_amp
X291 bl35 ref seb nb nt vdd gnd sense_amp
X292 bl36 ref seb nb nt vdd gnd sense_amp
X293 bl37 ref seb nb nt vdd gnd sense_amp
X294 bl38 ref seb nb nt vdd gnd sense_amp
X295 bl39 ref seb nb nt vdd gnd sense_amp
X296 bl40 ref seb nb nt vdd gnd sense_amp
X297 bl41 ref seb nb nt vdd gnd sense_amp
X298 bl42 ref seb nb nt vdd gnd sense_amp
X299 bl43 ref seb nb nt vdd gnd sense_amp
X300 bl44 ref seb nb nt vdd gnd sense_amp
X301 bl45 ref seb nb nt vdd gnd sense_amp
X302 bl46 ref seb nb nt vdd gnd sense_amp
X303 bl47 ref seb nb nt vdd gnd sense_amp
X304 bl48 ref seb nb nt vdd gnd sense_amp
X305 bl49 ref seb nb nt vdd gnd sense_amp
X306 bl50 ref seb nb nt vdd gnd sense_amp
X307 bl51 ref seb nb nt vdd gnd sense_amp
X308 bl52 ref seb nb nt vdd gnd sense_amp
X309 bl53 ref seb nb nt vdd gnd sense_amp
X310 bl54 ref seb nb nt vdd gnd sense_amp
X311 bl55 ref seb nb nt vdd gnd sense_amp
X312 bl56 ref seb nb nt vdd gnd sense_amp
X313 bl57 ref seb nb nt vdd gnd sense_amp
X314 bl58 ref seb nb nt vdd gnd sense_amp
X315 bl59 ref seb nb nt vdd gnd sense_amp
X316 bl60 ref seb nb nt vdd gnd sense_amp
X317 bl61 ref seb nb nt vdd gnd sense_amp
X318 bl62 ref seb nb nt vdd gnd sense_amp
X319 bl63 ref seb nb nt vdd gnd sense_amp
X320 bl0 ref seb nb nt vdd gnd sense_amp
X321 bl1 ref seb nb nt vdd gnd sense_amp
X322 bl2 ref seb nb nt vdd gnd sense_amp
X323 bl3 ref seb nb nt vdd gnd sense_amp
X324 bl4 ref seb nb nt vdd gnd sense_amp
X325 bl5 ref seb nb nt vdd gnd sense_amp
X326 bl6 ref seb nb nt vdd gnd sense_amp
X327 bl7 ref seb nb nt vdd gnd sense_amp
X328 bl8 ref seb nb nt vdd gnd sense_amp
X329 bl9 ref seb nb nt vdd gnd sense_amp
X330 bl10 ref seb nb nt vdd gnd sense_amp
X331 bl11 ref seb nb nt vdd gnd sense_amp
X332 bl12 ref seb nb nt vdd gnd sense_amp
X333 bl13 ref seb nb nt vdd gnd sense_amp
X334 bl14 ref seb nb nt vdd gnd sense_amp
X335 bl15 ref seb nb nt vdd gnd sense_amp
X336 bl16 ref seb nb nt vdd gnd sense_amp
X337 bl17 ref seb nb nt vdd gnd sense_amp
X338 bl18 ref seb nb nt vdd gnd sense_amp
X339 bl19 ref seb nb nt vdd gnd sense_amp
X340 bl20 ref seb nb nt vdd gnd sense_amp
X341 bl21 ref seb nb nt vdd gnd sense_amp
X342 bl22 ref seb nb nt vdd gnd sense_amp
X343 bl23 ref seb nb nt vdd gnd sense_amp
X344 bl24 ref seb nb nt vdd gnd sense_amp
X345 bl25 ref seb nb nt vdd gnd sense_amp
X346 bl26 ref seb nb nt vdd gnd sense_amp
X347 bl27 ref seb nb nt vdd gnd sense_amp
X348 bl28 ref seb nb nt vdd gnd sense_amp
X349 bl29 ref seb nb nt vdd gnd sense_amp
X350 bl30 ref seb nb nt vdd gnd sense_amp
X351 bl31 ref seb nb nt vdd gnd sense_amp
X352 bl32 ref seb nb nt vdd gnd sense_amp
X353 bl33 ref seb nb nt vdd gnd sense_amp
X354 bl34 ref seb nb nt vdd gnd sense_amp
X355 bl35 ref seb nb nt vdd gnd sense_amp
X356 bl36 ref seb nb nt vdd gnd sense_amp
X357 bl37 ref seb nb nt vdd gnd sense_amp
X358 bl38 ref seb nb nt vdd gnd sense_amp
X359 bl39 ref seb nb nt vdd gnd sense_amp
X360 bl40 ref seb nb nt vdd gnd sense_amp
X361 bl41 ref seb nb nt vdd gnd sense_amp
X362 bl42 ref seb nb nt vdd gnd sense_amp
X363 bl43 ref seb nb nt vdd gnd sense_amp
X364 bl44 ref seb nb nt vdd gnd sense_amp
X365 bl45 ref seb nb nt vdd gnd sense_amp
X366 bl46 ref seb nb nt vdd gnd sense_amp
X367 bl47 ref seb nb nt vdd gnd sense_amp
X368 bl48 ref seb nb nt vdd gnd sense_amp
X369 bl49 ref seb nb nt vdd gnd sense_amp
X370 bl50 ref seb nb nt vdd gnd sense_amp
X371 bl51 ref seb nb nt vdd gnd sense_amp
X372 bl52 ref seb nb nt vdd gnd sense_amp
X373 bl53 ref seb nb nt vdd gnd sense_amp
X374 bl54 ref seb nb nt vdd gnd sense_amp
X375 bl55 ref seb nb nt vdd gnd sense_amp
X376 bl56 ref seb nb nt vdd gnd sense_amp
X377 bl57 ref seb nb nt vdd gnd sense_amp
X378 bl58 ref seb nb nt vdd gnd sense_amp
X379 bl59 ref seb nb nt vdd gnd sense_amp
X380 bl60 ref seb nb nt vdd gnd sense_amp
X381 bl61 ref seb nb nt vdd gnd sense_amp
X382 bl62 ref seb nb nt vdd gnd sense_amp
X383 bl63 ref seb nb nt vdd gnd sense_amp
