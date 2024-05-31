# Algorithm Input and Output Data Definition (IODD)

Except for the input L1b {term}`TB` data, all auxiliary and output data follow the {term}`EASE-Grid` 2.0 polar projection of the Northern Hemisphere.
The current target spatial resolution for regridding is 3.125km.

## Input data

Daily Level-2 brightness temperature data are the main input, namely Ku-band data of horizontal polarisation and Ka-band data of both polarisations.

```{important}
If available, night or morning acquisition times are preferred over afternoon or evening brightness temperature data, in order to minimise effects of liquid water within the snowpack due to melt.
```

| Field | Description | Shape/Amount |
| ----- | ----------- | ------------ |
| L1b TB Ku-band &nbsp; | L1B Brightness Temperatures at 18.7 GHZ <br> (H polarisation) | Full swath or swath section <br> (Nscans,Npos) |
| L1b TB Ka-band &nbsp; | L1B Brightness Temperatures at 36.5 GHZ <br> (H and V polarisation) | Full swath or swath section <br> (Nscans,Npos) |

## Output data

| Field | Description | Shape/Amount |
| ----- | ----------- | ------------ |
| TSA | Terrestrial Snow Area (TSA) | EASE-Grid 2.0 NH <br> (nx,ny) |
| TSA Uncertainty | Qualitative uncertainty of TSA variable: <br> '0: very likely snow-free (FWD & BCK); 1: likely snow (FWD | BCK); 2: very likely snow (FWD & BCK)' | EASE-Grid 2.0 NH <br> (nx,ny) |
| Status Flag &nbsp; | Status flag for TSA | EASE-Grid 2.0 NH <br> (nx,ny) |

The main TSA variable (`tsa`) is a binary mask indicating snow-free pixels as `0`, and snow-covered pixels as `1`.
The TSA uncertainty (`tsa_uncertainty`) in turn is described through an 8-bit mask with the following allocated values:

```{table}
| Bit | Description              |
| --- | -----------              |
| 0   | Very likely snow free    |
| 1   | Likely snow covered      |
| 2   | Very likely snow covered |
```

The status flag (`status_flag`) similarly is an 8-bit mask with the following allocated values:

```{table}
| Bit | Description          |
| --- | -----------          |
| 0   | Water                |
| 1   | Land                 |
| 2   | Dry snow (valid)     |
| 3-7 | Placeholders         |
| 8   | No data, out of grid |
```

```{note}
Empty placeholders within the status flag may be used for future R&D activities, such as the development of a wet snow flag.
```

## Auxiliary data

* Land and water mask
Although the application of auxiliary data is not required to run the TSA algorithm per se, it is highly recommended to mask out known large water bodies thereby ensuring satisfactory product quality.

## Ancillary data

N/a
