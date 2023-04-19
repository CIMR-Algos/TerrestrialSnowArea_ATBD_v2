# Introduction, Purpose and Scope

Snow cover, the second-largest component of the cryosphere, is a crucial factor in the Earth’s energy balance owing to its high albedo {cite:p}`tedesco_2014`. Even though the largest annual and interannual variations in surface albedo are due to seasonal changes in snow conditions, seasonal snow occurs predominantly in the Northern Hemisphere only. Here, the vast majority of seasonal snow is found above 40° N and the maximum extent reaches about 50% of the hemispheric land area, making snow the dominant land cover type during snow season {cite:p}`rees_2005`. Meltwater from seasonal snow thus has an essential impact on freshwater resources as well as soil moisture {cite:p}`pulliainen_2020`.

Snow monitoring on global scale is an important task considering the essential role of snow in global climate and hydrologic systems, and given the scarcity of ground-based snow observations. Snow has distinctive, frequency-dependent characteristics in terms of microwave emission. This enables the use of brightness temperatures, as measured by spaceborne passive microwave sensors, for the estimation of terrestrial snow area (TSA) through (dry) snow detection methods. Those dry snow detection methods form a typical preprocessing step for the global retrieval of snow water equivalent (SWE) in order to minimise uncertainties in the latter. Reliable dry snow detection is thus crucial not only for the estimation of TSA, but also for the quantification of snow mass as demonstrated by {cite:t}`pulliainen_2020`. The authors assess hemispheric snow distribution as shown in {numref}`SWE_nature`, amongst other, and their trend analysis provides critical information for the evaluation of the impacts and feedbacks due to changes in snow mass.

```{figure} ./figures/SWE_nature.png
--- 
name: SWE_nature
width: 400px
---
Average snow distribution of the Northern Hemisphere (non-alpine regions above 40° N) between 1980-2018 {cite:p}`pulliainen_2020`.
```

Dry snow is often detected by the use of multi-spectral and/or multi-polarization methods {cite:p}`tedesco_2014`. Such passive microwave dry snow detection algorithms are commonly based on the Ka and Ku-band {cite:p}`chang_1987,hall_2002`, though some also incorporate further channels provided by CIMR {cite:p}`kelly_2009`.

The purpose of this study as part of CIMR Devalgo is the development of a dry snow detection algorithm tailored to the specifications of CIMR. The scope is to establish a stable initial version using Ka and Ku as core frequency bands according to {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`, and to prepare a snow dataset for validation and verification purposes. Upon stable performance, the X and C-band will be investigated regarding their potential to improve the dry snow detection algorithm, with the aim to develop a decision tree following the example of {cite:t}`grody_basist_1996`. Ultimately, it is planned to evaluate L-band for the determination of subnivean soil properties.
