#!/bin/bash

# Parameters
# 1) Top cell in view

/home/toolkit/cadence/installs/PVS151/bin/pvs -ext -control pvslvsctl -top_cell $1 -spice ./fram_sample.sp /home/dk/Mikron/HCMOS10_LP/PDK_v1.0_oa/physical/calibre/calibre.lvs > lvs.log