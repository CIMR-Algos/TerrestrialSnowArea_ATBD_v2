# Level-2 Product Definition

The content of the Level-2 TSA product files is defined in Tables {numref}`%s <product_netcdf>`, {numref}`%s <variable_attributes>`, {numref}`%s <status_flag>` and {numref}`%s <global_attributes>`.
The product is provided in netCDF format and contains the variables given in {numref}`product_netcdf`.

```{table} NetCDF Group: Processed Data (tbc).
:name: product_netcdf

| Variable name | Description | Units | Dimension |
| ---           | ----        | ----  | ----      |
| `crs`         | Definition of the product grid (EASE-Grid 2.0) | n/a | n/a |
| `tsa`         | Terrestrial snow area | 1 | (nx,ny) |
| `c`           | Confidence of detected terrestrial snow area | 1 | (nx,ny) |
| `status_flag` | Flag indicating status of pixels | n/a | (nx,ny) |
```

```{note}
The CIMR Level-2 TSA product is a gridded product. The dimensions of each variable in the Level-2 file refer to the (nx,ny) dimensions of the product grid i.e. EASE-Grid 2.0 polar projection.
```

Each data variable of the processed data in {numref}`product_netcdf` holds conventional attributes following NetCDF Climate and Forecast (CF) Metadata Conventions Version 1.7 (CF-1.7) or above as given in {numref}`variable_attributes`.

```{table} Standard variable attributes (tbc).
:name: variable_attributes
|  Name                  | Description |
|  --------------------- | ----- | 
| `standard_name` | A standard name that references a description of a variable's content                 |
| `long_name`     | A descriptive name that indicates a variable's content                                |
| `fill_value`    | Value that will appear in the dataset when the data is either missing or undefined     |
| `units`         | Unit of measure                                     |
```

The `status_flag` is an 8-bit mask whose structure is given in {numref}`status_flag`.

```{table} Status flag (tbc).
:name: status_flag

| Bit | Description |
| --- | ----        |
| 0   | No data |
| 1   | Validity of snow detection (set to valid)  |
| 2   | Water mask (open water) |
| 3   | Latitude mask (snow occurrence not possible) |
| 4-8 | Reserved |
```

Some global attributes of the Level-2 product files are given in {numref}`global_attributes`.

```{table} Global attributes (tbc).
:name: global_attributes

|  Name                  | Description |
|  --------------------- | ----- | 
|  `title`                 | CIMR L2 Sea Ice Drift product |
|  `processing_level`      | Level-2 |
|  `time_coverage_start`   | Valid start time of the product |
|  `time_coverage_end`     | Valid end time of the product |
|  `area`                  | (Northern or Southern) Hemisphere |
```