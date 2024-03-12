# import os
# import sys
import numpy as np
# import xarray as xr
# import datetime as dt

def dry_snow_detection(data, tsa_algorithm):
    """
    Perform dry snow detection

    Parameters
    ----------
    data: DataSet
        xarray DataSet containing data with `float`type.
    tsa_algorithm: str
        Choice of dry snow detection algorithm.

    Returns
    -------
    bin_map: ndarray
        Binary 2D array indicating snow-free (0) and snow-covered (1)  with `float` type.
    """

    if tsa_algorithm == 'Pulliainen2010':
        # Dry snow detection by Pulliainen et al. (2010), H SAF H11 Snow Status
        
        shp = tuple(data['KA'].dims[d] for d in ['n_scans_interleave_feed','n_samples_earth'])
        # TSA = np.zeros(shp)
        TSA = np.full(shp,fill_value=0.)
        
        sd = 15.9 * (data['KU'].brightness_temperature_h - data['KA'].brightness_temperature_h) # (mm)
        TSA[(sd > 30) & (data['KA'].brightness_temperature_v < 255) & (data['KA'].brightness_temperature_h < 250)] = 1

    # Clean-up
    del sd, shp
    
    return TSA
