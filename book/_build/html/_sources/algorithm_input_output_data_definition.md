# Algorithm Input and Output Data Definition (IODD)

The processing of the TSA product requires resampling of TB data from the instrument grid to EASE-Grid 2.0 of polar projection for the Northern or Southern Hemisphere. Even though the application of auxiliary data is not mandatory, it is highly recommended to mask out known water bodies and latitudes which historically do not experience snow cover. 

## Input data

Daily Level-2 brightness temperature data are the main input, requiring data of the Ku-band of horizontal polarisation and of the Ka-band of both polarisations.
Brightness temperature data of all other bands and polarisations may be necessary for future TSA product versions.

```{important}
If available, early morning satellite data is preferred as input over late afternoon data in order to minimise effects of liquid water within the snowpack.
```

| Field | Description | Shape/Amount |
| ---   | ----------- | ------------ |
| L1B TB Ku-band &nbsp; | L1B Brightness Temperatures at 18.7 GHZ <br> (H polarisation) | Full swath or swath section <br> (Nscans,Npos) |
| L1B TB Ka-band &nbsp; | L1B Brightness Temperatures at 36.5 GHZ <br> (H and V polarisation) | Full swath or swath section <br> (Nscans,Npos) |

## Output data

| Field | Description | Shape/Amount |
| ----- | -------- | ------------ |
| L2 TSA | Terrestrial Snow Area: <br> 0 for 'snow-free', 1 for 'snow-covered land'  | EASE-Grid 2.0 NH/SH <br> (nx,ny) |
| Status Flag &nbsp; | Pixel status: <br> 'no data', 'valid, 'open water', 'no snow possible' | EASE-Grid 2.0 NH/SH <br> (nx,ny) |

## Auxiliary data

* Land/water information (EASE-Grid 2.0)
* Latitude information (EASE-Grid 2.0)

## Ancillary data

N/a
