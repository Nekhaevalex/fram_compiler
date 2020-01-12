# FRAM gds and netlist compiler

## This is a README file for MIPT lab fram memory compiler.

## Author: Solovyanov Mikhail

### About:
Compiler is aimed to create gds and simulation representation of embedded FRAM memory array with given paramethers. You are free to change them in annotated array_config file.

Compiler includes pre-made views of all cells such as:

- memory_cell = One 1T-1C cell
- sense_amp = non destructive comparator for in and ref signals
- driver (aka bl_driver) - high off state  impedance  driver connected directly to BL
- pmos and nmos for decoder creation
- PL driver = driver for plate line



###List of all files:

fram_array.py - main python file creates GDS view and calles netlist class.
netlist_generator.py - contains Netlist class
array_config = config file you are free to specify some paramethers here.
layout_class - contains class dedicated to create multipart path (usefull in some situations)


---------output---------------
fram_sample.sp - OUTPUT netlist example
./gds_files/fram_sample.gds = GDS file
./netlists/fram_sample.gds = netlist output

any questions you can ask here:

e-mail: solovyanov.mm@phystech.edu
