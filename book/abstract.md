# Abstract

Snow mapping by means of passive microwave dry snow detection is commonly based on the difference of spaceborne Ku and Ka brightness temperatures of horizontal polarisation.
This forms also the foundation of the dry snow detection algorithm for the Terrestrial Snow Area (TSA) Level-2 product which is based on the approaches of {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`, as described in this Algorithm Theoretical Basis Document (ATBD).
In order to benefit from the specifications of the Copernicus Imaging Microwave Radiometer (CIMR), an expansion of the TSA algorithm is investigated to include additional CIMR frequency bands.
Especially the implementation of X-band brightness temperatures is expected to further improve the algorithm performance. 
The TSA product is evaluated using a custom validation dataset, which is similar to the Round Robin Data Package (RRDP) by the ESA Climate Change Initiative {cite:p}`pedersen_2021`.
