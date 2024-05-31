# Abstract

% snow importance
Snow cover is a central component of the Earth’s cryosphere, encountered at mid to high latitudes.
It plays an important role in climate and hydrologic systems, directly influencing the global surface energy budget and regional freshwater resources particularly in the Northern Hemisphere.
Rising temperatures have resulted in a profound global reduction of snow cover area and seasonal duration, which drastically affect the global climate and restrict communities in accessing subsistence and freshwater resources.
Understanding those climate impacts and risks to water supply is paramount for successful climate mitigation and adaptation, as well as informed water resource management.
This requires global monitoring tools, including spaceborne snow mapping using passive microwave data.

% algorithm
Snow mapping by means of spaceborne passive microwave dry snow detection is commonly based on the spectral difference between 18 GHz (Ku-band) and 36 GHz (Ka-band) brightness temperatures of horizontal polarisation.
This principle is also fundamental for the dry snow detection algorithm of the {term}`Terrestrial Snow Area` ({term}`TSA`) Level-2 product for the {term}`Copernicus Imaging Microwave Radiometer` ({term}`CIMR`) mission.
The TSA algorithm implements the approaches of {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`, as described in this Algorithm Theoretical Basis Document ({term}`ATBD`).