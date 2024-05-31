# Roadmap for Future ATBD Development

% wet snow
Passive microwave snow detection algorithms are known to underestimate global snow cover area {cite:p}`hall_2002,zschenderlein_2023`.
They are sensitive to dry snowpacks with minimal water content, and hence struggle to capture wet snow areas due to fundamentally different radiometric properties {cite:p}`matzler_1994`.
To expand the capabilities of the Level-2 {term}`TSA` product to reliably map also wet snow, the operational implementation of a wet snow detection module should be investigated.
For this purpose, feasible approaches might incorporate diurnal amplitude variations (e.g. {cite:t}`semmens_2014`), L-band brightness temperatures of horizontal polarization {cite:p}`pellarin_2016,rautiainen_2012`, or numerical weather prediction ({term}`NWP`) temperature data {cite:p}`tuttle_2019`.

% quality flag
Besides, the concept of the status flag as an indicator of uncertainty may be expanded and refined in the future.
For binary classifications as implemented within the TSA product, we lack a comprehensive quantitative and/or qualitative uncertainty characterization.
Further traceable uncertainty sources have to be identified in addition to the current components derived from {term}`TB` data of different looking directions, including for instance the impact of brightness temperature measurement uncertainties on the snow detection results.
Moreover, land surface or air temperature data could enable same-day identification of meteorological conditions that make snow presence (un)likely, thereby supporting near real-time ({term}`NRT`) quality assurance.
Such temperature data would also allow for retrospective quality assessment of the TSA maps: Using temperature data of the whole snow season, an end-of-season quality flag could be generated which affirms or rules out snow cover based on the weather conditions across consecutive days.
Furthermore, the use of a snow climatology could be considered to restrict snow detection to geolocations that have historically experienced snow cover, e.g. {cite:t}`dewey_heim_1982` in {cite:t}`kelly_2009`.
This would not only improve the TSA algorithm accuracy but would also provide likelihoods for snow presence in the spatial and temporal domain, which could again feed into the NRT quality flag.

% other
As the performance assessment highlighted, brightness temperature correction for water contamination per footprint or per grid cell is desirable.
In the unfortunate case that such a correction is not provided for CIMR L1b/L1c data products, the TSA algorithm would benefit from open water filtering, masking or correction in order to improve snow mapping accuracy in proximity to coastlines and (unmasked) freshwater lakes.
Other product extensions could address the screening for precipitation and the detection of thin snow cover.
Both the additional scattering due to hydrometeors and the lesser scattering of thin snowpacks are known challenges to passive microwave dry snow detection {cite:p}`matzler_1994`;
They have been previously addressed by means of brightness temperatures at 22 GHz and 85 GHz, which are sensitive to the respective scattering behaviours {cite:p}`grody_1996, foster_2011`.
Since those channels are not available for CIMR, the TSA product could draw upon external satellite TBs although this would fall beyond the Level-2 status.

While the CIMR Level-2 TSA product is a stand-alone data product within the CIMR product suite, the development and implementation of the CIMR Level-2 Global Snow Water Equivalent ({term}`SWE`) product will be closely linked – directly incorporating the TSA output in its processing chain (compare e.g. {cite:p}`luojus_2021`).
Although the SWE retrieval itself will require noticeable development efforts, future improvement and development of the TSA algorithm and {term}`ATBD` remain of high interest.