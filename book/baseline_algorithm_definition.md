# Baseline Algorithm Definition

The TSA algorithm is based on dry snow detection as described by {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`. It is an empirical algorithm, based on the underlying physical principle that microwave radiation of higher frequencies is attenuated by snow cover due to volume scattering, while lower frequencies remain mostly unaffected.

## Retrieval Method

N/a


## Forward Model

N/a


## CIMR Level-1B Re-sampling Approach

Resampling approach to be defined.
Subsequent reprojection to EASE-Grid 2.0 polar projections of the Northern Hemisphere (NH) or Southern Hemisphere (SH).


## Algorithm Assumptions and Simplifications

To be added.


## Level-2 End to End Algorithm Functional Flow Diagram

{numref}`flow-diagram` shows the functional structure for the computation of the TSA product.

```{figure} ./figures/L2-algorithm.png
--- 
name: flow-diagram
width: 450px
---
Functional flow diagram of the Level-2 end to end algorithm of the TSA product.
```

## Functional description of each Algorithm step

As outlined in the flow diagram in {numref}`flow-diagram`, the algorithm follows four major steps: 

* Step 1: Mapping of L1B brightness temperatures to gridded brightness temperatures in swath projection.
* Step 2: Application of dry snow detection algorithm to gridded brightness temperatures.
* Step 3: Output of L2 TSA maps.
* Step 4: Optional masking for improved TSA maps, e.g. land/water and latitude masking.

### Mathematical description

The dry snow detection algorithm of the TSA product (Step 2) is based on the approach of {cite:t}`hall_2002` but applies updated empirically derived thresholds as implemented for the EUMETSAT H SAF snow status product H11 {cite:p}`pulliainen_2010`. The brightness temperature difference between the Ku and Ka-band is used to estimate snow depth (SD) as

```{math}
:label: TB_diff
\text{SD} = R_c \cdot (T_B^{18H}-T_B^{37H}),
```

with regression coefficient $R_c$ of 1.59 cm/K and brightness temperatures $T_B$, where the superscripts indicate the frequency and polarisation.
For the algorithm in {eq}`TB_diff` to detect dry snow, the following thresholds must be met:

```{math}
\begin{aligned}
\text{SD} &≥ 3.0~\text{cm}\\
T_B^{37V} &< 255~\text{K}\\
T_B^{37H} &< 250~\text{K}.
\end{aligned}
```

The use of further CIMR channels for dry snow detection is under investigation.

### Input data

For the algorithm development phase, brightness temperatures from operational instruments will be used to provide adequate sample data for all CIMR channels: Ka, Ku, X, C and L-band of dual polarisation.

### Output data

L2 TSA maps are provided, with 0 for 'snow-free land', 1 for 'snow-covered land', and NaN otherwise. In addition, flags indicate the reason of NaN values, such as 'open-water' and 'no data'.

### Auxiliary data

Auxiliary data for Step 4 include information on open water in order to have a consistent definition of land and water grid cells. Besides, the TSA product is only concerned with snow cover in the Northern Hemisphere, where seasonal terrestrial snow predominantly occurs. Latitudes at and below 40° N are masked out, as those historically do not experience snow cover, in order to avoid false positive snow cells. Masking for the Southern Hemisphere is to be confirmed.

### Ancillary data

N/a

### Validation process

The Level-2 TSA product is validated using brightness temperatures from operational instruments, e.g. AMSR2, which are collocated and temporally matched to exhaustive in situ SD observations from weather stations across the Northern Hemisphere.
Main sources for SD measurements are the European Centre for Medium-Range Weather Forecasts (ECMWF) and the Global Historical Climatology Network {cite:p}`menne_2012`. Those are complemented by observations of the World Data Center of the All-Russia Research Institute of Hydrometeorological Information {cite:p}`bulygina_2011`, of the Meteorological Service of Canada, and from across the continental United States {cite:p}`dyer_2006`. The observations encompass both snow and snow-free conditions for thorough validation of both true positive and true negative classifications. The validation dataset follows closely the structure of the Round Robin Data Package (RRDP) {cite:p}`pedersen_2021`.

The main metric used for validation is classification accuracy, including daily as well as monthly and total mean accuracy values.
By binning observation classes according to in situ SD, the ability of the TSA product to map dry snow for varying snow depth can be evaluated.



