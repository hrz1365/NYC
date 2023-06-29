""" This scripy calls dasymetry.py. User can modify or call only the
    methods they want to use. Please see the namelist file for info
    on the parameters.
"""

import sys
from pathlib import Path

# enter your dasymetry path
dasypath    = './scripts/python/'
output_path = Path('./outputs/parcel_downscaling/')
workdir     = Path(dasypath)

sys.path.append(dasypath)

import dasymetry as dasy
import matplotlib.pyplot as plt


dasy = dasy.Dasymetry(workdir)
dasy.load_namelist(dasy.rundir)
dasy.load_source_files(dasy.configdict)


# Pre-process blocks and lots for disaggregation
dasy.getOverpopParcels(dasy.parcel_df, dasy.block_df)
dasy.assignParcels(dasy.parcel_df, dasy.block_df)



# disaggregate
dasy.blocksToOverpop(dasy.parcel_df, dasy.block_df)    # Determines parcels intersecting more than 1 block 
dasy.disaggregate(dasy.parcel_df, dasy.block_df)


# Write output
output_name = 'parcels_pop_2020.shp'
dasy.writeOutput(output_name, dasy.parcel_df)
