# Background and Justification of Selected Algorithm

Dry snow is often detected by the use of multi-spectral and/or multi-polarization methods.
Such passive microwave dry snow detection algorithms are commonly based on the Ka and Ku-band {cite:p}`chang_1987,hall_2002`.
For the {term}`TSA` product, the dry snow detection algorithm by {cite:t}`pulliainen_2010` is selected, which implements the approach by {cite:t}`hall_2002` with updated empirical thresholds.
The origins of the algorithm reach back to a physical model inversion by {cite:t}`chang_1987`.

The algorithm in this form is found to perform best for the channels available from {term}`CIMR`, according to {cite:t}`zschenderlein_2023`.
This study includes an extensive long-term comparison of {term}`PMW` dry snow detection approaches centering on the Ka and Ku-bands, namely {cite:t}`chang_1987,grody_1996,foster_1997,armstrong_2001`, {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`.
The latter two algorithms are implemented in the GlobSnow v3.0 {term}`SWE` product of the Global Snow Monitoring for Climate Research initiative of the European Space Agency ({term}`ESA`) {cite:p}`luojus_2021`, and in the snow status (dry/wet) H11 product by the Support to Operational Hydrology and Water Management ({term}`H SAF`) of the European Organization for the Exploitation of Meteorological Satellites ({term}`EUMETSAT`).
The approaches by {cite:t}`hall_2002` and {cite:t}`pulliainen_2010` are thus referred to as *GlobSnow* and *H SAF*, respectively.

```{note}
Due to significant differences in microwave emission between wet and dry snow {cite:p}`matzler_1994`, the PMW methods mentioned here apply only to dry snow conditions with minimal liquid water content, and are furthermore static i.e. disregarding temporal variations for instance in snow grain size or snow density.
```

PMW dry snow detection algorithms are known to generally underestimate the presence of snow due to their sensitivity to vegetation and liquid water content of the snowpack, among other reasons.
This can be seen in {numref}`difference` which illustrates the difference between snow extent as estimated by GlobSnow and H SAF for brightness temperatures of SSM/I and SSMIS, with respect to snow maps of the Interactive Multisensor Snow and Ice Mapping System ({term}`IMS`).
Daily {term}`IMS` maps are based on multiple input sources and human analysis, and serve therefore as spatially complete reference for global snow extent complementing pointwise weather station measurements.
A negative number indicates the days per pixel for which the PMW algorithm flags 'snow-free' and IMS data flags 'snow', and vice versa for a positive number.
The difference shown in {numref}`difference` then gives the final sum of both cases for every day of the investigated time period, and thus shows the tendency of an algorithm to under- or overestimate.
The better performance of H SAF over GlobSnow is apparent, and the dry snow detection part of the ESA Snow Climate Change Initiative (CCI) project has been updated accordingly to the approach by {cite:t}`pulliainen_2010`.
This approach is the most accurate to-date on a global scale for the channels available on CIMR, and is therefore chosen for the Level-2 TSA product.

```{figure} ./figures/difference.png
--- 
name: difference
width: 600px
---
Difference maps of PMW algorithms with respect to IMS data over all snow seasons (September-February) from 2007/2008 until 2016/2017 above 40° N, based on {cite:t}`zschenderlein_2023`.
```