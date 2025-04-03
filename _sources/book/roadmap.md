# Roadmap for Future ATBD Development

% forward and backward
Passive microwave snow detection algorithms are known to underestimate global snow cover area {cite:p}`hall_2002,zschenderlein_2023`.
However, the presented performance assessment for synthetic scenes demonstrates the potential of exploiting CIMR's scanning geometry in this regard; A separate ingestion of forward and backward-looking brightness temperatures into the TSA algorithm, followed by their combined regridding, increases the detected snow cover area.
Although promising, this concept requires verification by means of real scenes, for instance from fore and aft WindSat L1c brightness temperatures in swath geometry {cite:p}`meissner_2022`.
WindSat data could be used as input for the TSA algorithm to not only obtain a proof of concept, but to also gain a deeper understanding of the underestimation problem in the first place.

% wet snow
Among others, the underestimating behaviour stems from the sensitivity of passive microwave snow retrievals to dry snowpacks with minimal liquid water content.
Hence, they struggle to capture wet snow areas which have fundamentally different radiometric properties {cite:p}`matzler_1994`.
To expand the capabilities of the Level-2 {term}`TSA` product to reliably map also wet snow, the operational implementation of a wet snow detection module should be investigated.
For this purpose, feasible approaches might incorporate diurnal amplitude variations (e.g. {cite:t}`semmens_2014`), L-band brightness temperatures of horizontal polarization {cite:p}`pellarin_2016,rautiainen_2012`, or numerical weather prediction ({term}`NWP`) temperature data {cite:p}`tuttle_2019`.

% quality flag
Besides, the concept of the status flag as an indicator of uncertainty may be expanded and refined in the future.
For binary classifications as implemented within the TSA product, we lack a comprehensive quantitative and/or qualitative uncertainty characterization.
Further traceable uncertainty sources have to be identified in addition to the current components derived from {term}`TB` data of different look directions, including for instance the impact of brightness temperature measurement uncertainties on the snow detection results.
Moreover, land surface or air temperature data could enable same-day identification of meteorological conditions that make snow presence (un)likely, thereby supporting near real-time ({term}`NRT`) quality assurance.
Such temperature data would also allow for retrospective quality assessment of the TSA maps: Using temperature data of the whole snow season, an end-of-season quality flag could be generated which affirms or rules out snow cover based on the weather conditions across consecutive days.
Furthermore, the use of a snow climatology could be considered to restrict snow detection to geolocations that have historically experienced snow cover, e.g. {cite:t}`dewey_heim_1982` in {cite:t}`kelly_2009`.
This would not only improve the TSA algorithm accuracy but would also provide likelihoods for snow presence in the spatial and temporal domain, which could again feed into the NRT quality flag.

% other
As the performance assessment highlighted, brightness temperature correction for water contamination per footprint or per grid cell is desirable.
In the case that such a correction is not provided for CIMR L1b/L1c data products, the TSA algorithm would benefit from open water filtering, masking or correction in order to improve snow mapping accuracy in proximity to coastlines and (unmasked) freshwater lakes.
Other product extensions could address the screening for precipitation and the detection of thin snow cover.
Both the additional scattering due to hydrometeors and the lesser scattering of thin snowpacks are known challenges to passive microwave dry snow detection {cite:p}`matzler_1994`;
They have been previously addressed by means of brightness temperatures at 22 GHz and 85 GHz, which are sensitive to the respective scattering behaviours {cite:p}`grody_1996, foster_2011`.
Since those channels are not available for CIMR, the TSA product could draw upon external satellite TBs although this would fall beyond the scope of a Level-2 product status.

% L2PAD
The CIMR Level-2 TSA product is a stand-alone data product within the CIMR product suite, yet its development and implementation will be closely linked to the CIMR Level-2 Snow Water Equivalent ({term}`SWE`) product, which will directly incorporate the TSA output in its processing chain (compare e.g. {cite:p}`luojus_2021`).
While the SWE retrieval itself will require noticeable development efforts, future improvements of the TSA algorithm remain of high interest.