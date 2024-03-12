import xarray as xr
import numpy as np
import pyresample as pr

def read_l1x(l1x_file):
    '''
    Read test card

    Parameters
    ----------
    l1x_file: str
        File location of test card file.

    Returns
    -------
    data_fwd: dict
        Test card brightness temperatures (forward scan).
    data_bck: dict
        Test card brightness temperatures (backward scan).
    '''

    geolocation_fwd = xr.open_dataset(l1x_file, group='FWD_geolocation')
    geolocation_bck = xr.open_dataset(l1x_file, group='BCK_geolocation')
    
    data_fwd = dict()
    data_bck = dict()
    bands = ('KU', 'KA')
    for gr in bands:
        data_fwd[gr] = xr.open_dataset(l1x_file, group='FWD_' + gr + '_BAND')
        data_bck[gr] = xr.open_dataset(l1x_file, group='BCK_' + gr + '_BAND')

    return data_fwd, geolocation_fwd, data_bck, geolocation_bck

def reproject_to_grid(TSA_swath,geo_swath,area_def,radius_of_influence=5000):
    '''
    ADD DESCRIPTION
    '''

    radius_of_influence = radius_of_influence       # 20000/4 for 3.125, 2 for 6.25, 1 for 12.5

    swath_def = pr.geometry.SwathDefinition(lons=geo_swath['lon'].values, lats=geo_swath['lat'].values)
    TSA_proj = pr.kd_tree.resample_nearest(swath_def, TSA_swath, area_def,
                            radius_of_influence=radius_of_influence, fill_value=np.nan)
    # TSA_proj = pr.kd_tree.resample_gauss(swath_def, TSA_swath, area_def,
    #                         radius_of_influence=radius_of_influence, sigmas=1000, fill_value=np.nan)

    del swath_def

    return TSA_proj


def combine_proj(TSA_fwd_proj,TSA_bck_proj):
    '''
    Combine projected/gridded forward and backward TSA

    Parameters
    ----------
    TSA_fwd_proj: array
        Projected forward TSA.
    TSA_bck_proj: array
        Projected backward TSA.

    Returns
    -------
    TSA_comb: array
        Combined TSA with snow-free fwd&bck (0), snow-covered fwd|bck (0.5) and snow-covered fwd&bck (1).
    TSA_comb_uncert: array
        Combined TSA with snow-free fwd (0)
    (TSA_comb_val): array
        Flag for combined data, indicating swath data validity.
        
    '''

    _fwd_invalid = np.isnan(TSA_fwd_proj)
    _bck_invalid = np.isnan(TSA_bck_proj)
    keep_fwd = ~_fwd_invalid & _bck_invalid
    keep_bck = _fwd_invalid & ~_bck_invalid

    TSA_comb_uncert = 0.5 * (TSA_fwd_proj + TSA_bck_proj)

    TSA_comb_uncert[keep_fwd] = 0.5 * TSA_fwd_proj[keep_fwd]
    TSA_comb_uncert[keep_bck] = 0.5 * TSA_bck_proj[keep_bck]

    TSA_comb = np.ceil(TSA_comb_uncert)

    # swath data flag
    # TSA_comb_val = np.zeros(TSA_comb_uncert.shape, dtype='i8')
    # _fwd_valid = ~_fwd_invalid
    # _bck_valid = ~_bck_invalid
    # TSA_comb_val[_fwd_invalid*_bck_invalid] = 0      # 0: Invalid, N/A
    # TSA_comb_val[_fwd_valid] = 1                     # 1: FWD valid
    # TSA_comb_val[_bck_valid] = 2                     # 2: BCK valid
    # TSA_comb_val[_fwd_valid*_bck_valid] = 3          # 3: FWD&BCK valid

    return TSA_comb, TSA_comb_uncert

# (Read SCEPS??)


# Write NetCDF file

# def write_l2nc():
#     return x

