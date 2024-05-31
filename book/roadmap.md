# Roadmap for Future ATBD Development

Future improvements of the TSA algorithm may incorporate the CIMR Level-2 Global Land Surface Temperature data product or other air temperature data.
Such temperature data would enable same-day identification of meteorological conditions that make snow presence (un)likely, thereby supporting NRT quality assurance.
In addition to NRT information, land surface and/or air temperatures would allow for retrospective quality assessment of the TSA maps: Using temperature data of the whole snow season, an end-of-season quality flag could be generated which affirms or rules out snow cover based on the weather conditions across consecutive days.

Moreover, the use of a snow climatology could be considered to restrict snow detection to geolocations that have historically experienced snow cover, e.g. {cite:t}`dewey_heim_1982` in {cite:t}`kelly_2009`.
This would not only improve the TSA algorithm accuracy but also provide likelihoods for snow presence in the spatial and temporal domain, which could feed into the NRT quality flag.
Besides, brightness temperature correction for water contamination per footprint or per grid cell is desirable.
In case such a correction is not provided for CIMR L1b/L1c data products, the TSA algorithm would benefit from open water detection and filtering or correction in order to improve snow mapping accuracy especially in proximity to coastlines and (unmasked) freshwater lakes.
Further algorithm extensions should address the screening for precipitation and the detection of thin snow cover. The additional scattering due to hydrometeors and the lesser scattering of thin snowpacks are both known challenges to passive microwave dry snow detection {cite:p}`matzler_1994`;
They have been previously addressed by means of 22-GHz and 85-GHz brightness temperatures, which are sensitive to the respective scattering behaviours {cite:p}`grody_1996, foster_2011`.
As those channels are not available for CIMR, alternative approaches have to be investigated.

Although the TSA product is a stand-alone product, the development and implementation of the CIMR Level-2 Global Snow Water Equivalent (SWE) data product will be closely linked – possibly directly incorporating the TSA data in its processing chain (compare e.g. {cite:p}`luojus_2021`).
Although the SWE retrieval itself also presents other noticeable challenges, including but not limited to the handling of auxiliary data like ground-based synoptic snow observations, future improvements of the TSA algorithm remain of high interest.
