# Algorithm Performance Assessment

Self standing Python code and results within Jupyter Book

## L1 E2ES Demonstration Reference Scenario (Picasso) scene definition

```{figure} ./figures/picasso-scene.png
--- 
name: picasso-scene
width: 500px
---
Demonstration Reference Scenario (Picasso) including a radiometric scene (left) representing 8 different surface types (2x sea ice, 2x land, 4x ocean) adjacent to each other and sea ice concentration sub-resolution gradients, and a geometric scene (right) with a high-contrast brightness temperature pattern.
```

## Algorithm Performance Metrics (MPEF)

The performance of the TSA algorithm is evaluated by means of classification accuracy.
For this, TSA estimates are divided into true positive (TP), false positive (FP), true negative (TN) and false negative (FN) observations.
Those observation classes for a single day are used to calculate the daily classification accuracy:

```{math}
:label: accuracy
\text{accuracy} = \frac{\text{TP}+\text{TN}}{\text{TP}+\text{FP}+\text{TN}+\text{FN}},
```

which is obtained for all days and subsequently used to derive monthly and total mean accuracy values.
In addition, observation classes are binned with respect to corresponding in situ SD which clarifies the ability of the TSA algorithm to detect dry snow for varying snow depth.

## Algorithm Calibration Data Set (ACDAT)

N/a

## Algorithm Validation Data Set (AVDAT)

The reference dataset spans the years 2017 and 2018, thus covering a whole snow season in the Northern Hemisphere.
It follows closely the structure of existing ESA CCI reference datasets for other climate variables, commonly in the form of a Multisensor Matchup Dataset (MMD).
Brightness temperatures for all CIMR equivalent channels are obtained from AMSR2 and SMAP data products, such as the AMSR2 level 1R (L1R) swath data product.
The inclusion of all channels, in addition to Ka and Ku as main bands for TSA retrieval, aims to facilitate further research on the development and tuning of the TSA algorithm.
Main sources for in situ snow depth measurements are the European Centre for Medium-Range Weather Forecasts (ECMWF) and the Global Historical Climatology Network {cite:p}`menne_2012`.
Those are complemented by observations of the World Data Center of the All-Russia Research Institute of Hydrometeorological Information {cite:p}`bulygina_2012`, of the Meteorological Service of Canada, and from across the continental United States {cite:p}`dyer_mote_2006`.
The observations encompass both snow and snow-free conditions.
Quality control of the weather station data includes, but is not limited to, filtering for duplicates, as well as for negative and extremely high SD values.
In situ data from the same sources though with different filtering applied, were used e.g. by {cite:t}`luojus_2021`.


## Test Results using Demonstration Reference Scenario

## Algorithm Performance Assessment using Demonstration Reference Scenario




