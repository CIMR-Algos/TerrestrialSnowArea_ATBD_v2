# Level-2 Product Definition

The Level-2 {term}`TSA` product files are provided in netCDF format, with contents as defined in Tables {numref}`%s <product_netcdf>`, {numref}`%s <variable_attributes>`, and {numref}`%s <global_attributes>`.
Each data variable of the processed data in {numref}`product_netcdf` holds conventional attributes following NetCDF Climate and Forecast Metadata Conventions Version 1.7 (CF-1.7) or above as given in {numref}`variable_attributes`.
Some global attributes of the Level-2 product files are given in {numref}`global_attributes`.

```{seealso}
Refer to the {ref}`content:annex` for a sample run demonstrating the processing sequence to create the L2 TSA product files (see [Jupyter Notebook](../algorithm/CIMR_L2_TSA_PICASSO.ipynb)).
```

```{table} NetCDF Group: Processed Data.
:name: product_netcdf

| Variable name | Description | Units | Dimension |
| ------------- | ----------- | ----- | --------- |
| `tsa`         | Terrestrial snow area ({term}`TSA`) | 1 | (nx,ny) |
| `tsa_uncertainty` | Confidence of detected  TSA | 1 | (nx,ny) |
| `status_flag`     | Flag indicating pixel status | n/a | (nx,ny) |
| `crs` |  Coordinate reference system ({term}`CRS`) of the TSA product | n/a | n/a |
| `lat` |  Latitudes of pixel centres according to CRS | degrees North | (nx,ny) |
| `lon` |  Longitudes of pixel centres according to CRS | degrees East | (nx,ny) |
| `x` |  x-Coordinate of the CRS | m | (nx) |
| `y` |  y-Coordinate of the CRS | m | (ny) |
```

```{note}
The CIMR Level-2 TSA product are gridded files. The dimensions of each variable in the Level-2 file refer to the (nx,ny) dimensions of the product grid, i.e. EASE-Grid 2.0 NH polar projection.
```

```{table} Standard variable attributes.
:name: variable_attributes
| Name            | Description                                                      |
| ----            | -----------                                                      | 
| `standard_name` | Sandard name referencing the description of a variable's content |
| `long_name`     | Descriptive name indicating a variable's content                 |
| `fill_value`    | Value indicating missing or undefined data                       |
| `units`         | Unit of measure                                                  |
```

```{table} Global attributes.
:name: global_attributes

| Name                  | Description                     |
| ----                  | -----------                     | 
| `title`               | CIMR L2 Terrestrial Snow Area   |
| `processing_level`    | Level-2                         |
| `time_coverage_start` | Valid start time of the product |
| `time_coverage_end`   | Valid end time of the product   |
| `area`                | Northern Hemisphere             |
```