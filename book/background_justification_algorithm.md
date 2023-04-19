# Background and Justification of Selected Algorithm

% snow
Snow is a mixture of ice crystals, liquid water and air. Over time, the density of a snow pack increases due to compaction by wind and gravity, and due to thermal metamorphism {cite:p}`rees_2005`.
Its internal structure is characterised primarily by the grain or crystal size, and by the form and orientation of those crystals.
A further property is snow wetness which refers to the liquid water content.
For temperatures at or above the freezing point, a considerable amount of liquid water might be present within a 'wet' snowpack.
For temperatures below the freezing point, on the other hand, a snowpack is unlikely to contain any liquid water and is thus considered to be 'dry'.
Below we discuss PMW remote sensing of snow with a focus on dry snow detection and associated challenges.

## Passive Microwave Remote Sensing of Snow

% general
In contrast to visible and infrared bands, dry snow is comparatively transparent to microwave radiation.
The microwave energy that is emitted from a snowpack hence originates not only from its surface, but also from deeper snow layers and from the ground beneath.
For dry snow detection, the contribution in emission from the snow layer itself is most of the times negligible because of its low emissivity in comparison to the ground underneath {cite:p}`tedesco_2014`.
The emission of the ground is in turn attenuated by the snow cover, predominantly due to volume scattering.
Since the magnitude of this attenuation is dependent on the microwave wavelength amongst other factors, lower brightness temperatures are measured for higher frequencies in the presence of snow.
Dry snow is thus commonly detected by comparing the brightness temperatures of different frequency bands in order to identify such attenuation.

% volume scattering
Volume scattering, the dominating type of attenuation as observed for dry snow, is highly dependent on frequency.
Air acts as a surrounding medium for the ice particles with diameters on the order of millimetres.
For propagating waves with wavelengths noticeably larger than this, snow appears as a homogeneous medium with only absorptive effects.
For wavelengths of similar magnitude, the ice particles act as scatterers due to the inhomogeneous dielectric properties between the ice itself and the air background {cite:p}`ulaby_long_2014`.
This scattering mechanism is shown in {numref}`emission-scattering`.
The phenomenon that the emissivity of snow-covered ground decreases with increasing frequency, is unique among land cover types {cite:p}`matzler_1994`.


```{figure} ./figures/emission-scattering.png
--- 
name: emission-scattering
width: 350px
---
Schematic of the microwave emission from snow characterised by volume scattering.
```

% scattering aspects
The amount of volume scattering is directly influenced by the snow's properties.
The impact of wavelength on scattering behaviour can be applied to snow grain size: the higher the frequency and/or the larger the grains, the more scattering is observed as the particle size approaches the wavelength {cite:p}`foster_1997,tedesco_2014`.
Snow density has a similar effect to grain size and since both generally increase for aging snow, older snowpacks result in more attenuation.
A further aspect to consider is snow depth, given deeper snowpacks naturally allow for more scattering to take place.

% scattering signature
This attenuation as found for snow-covered surfaces is detected through the difference in brightness temperature between two (or more) PMW bands.
A channel of lower frequency provides a scatter-free reference brightness temperature, whereas higher frequency channels may show an attenuation in brighness temperatures due to their sensitivity to scattering.
For this, the Ku and Ka-band are common respective choices {cite:p}`chang_1987,foster_1997,hall_2002,grody_basist_1996`.
Such a spectral difference, often referred to as scattering signature, is obviously sensitive to snow presence in first place as well as to snow properties and even to subnivean soil conditions {cite:p}`matzler_1994`.

% snow depth
This sensitivity to snow properties can be exploited to derive snow depth estimates from the scattering signature.
However, snow depths of less than about 3 cm are seldomly detected because the scattering effect is only marginal {cite:p}`chang_1987,hall_2002`.
To improve the sensitivity to thin snowpacks, brightness temperatures from high frequencies of 85 GHz and above can be included as those are subject to increased volume scattering {cite:p}`rees_2005`.
In addition, the influence of the underlying ground on the observed emission is more apparent for shallow snowpacks; an increase in soil temperature and/or wetness may significantly increase the measured brightness temperature.
On the other hand, snow depths larger than about 1.25 m become problematic as the maximum observable scattering is reached.
This results in signal saturation i.e. snow depths cannot be reliably estimated anymore using the brightness temperature difference since no variations in scattering are present beyond this snow depth {cite:p}`foster_1997`.
Snow is now the primary emitter, and its emissivity starts to increase rather than decrease for increasing snow depth {cite:p}`foster_1997,matzler_1994`.

% limitations and polarisation
Limitations of dry snow detection based on the scattering signature also arise due to anomalous scattering signals, caused for instance by precipitation or cold deserts {cite:p}`rees_2005,grody_basist_1996`, or due to internal variations in snow properties {cite:p}`tedesco_2014`.
The latter includes variations in density and grain size resulting from the snowpack stratigraphy.
Those distinctive snow layers affect the horizontal more than the vertical polarisations of the Ku and Ka channels {cite:p}`kelly_2003`.
It could be derived that vertical polarisations are more appropriate for snow depth estimations given they are less responsive to internal characteristics, whilst horizontal polarisations are more sensitive to those same properties and therefore suitable for detecting dry snow in first place {cite:p}`kelly_2003`.
Nonetheless, either polarisation have been applied for dry snow detection.

% snow wetness
In contrast to dry snow and regardless of polarisation, consistently wet or melting snow can be hardly discriminated from bare wet or frozen soil.
The liquid water content significantly reduces, if not eliminates, the snowpack's transparency to microwave radiation as shown in {numref}`emission-ambient`.
The scattering signature as such is thus not present, and the emissivity spectrum of wet snow is hence drastically different to the one of dry snow {cite:p}`matzler_1994`.
The internal wetness of snow also affects the capability of scattering signatures for snow accumulation monitoring.
Even though PMW remote sensing can be used to retrieve accumulation rates in the dry-snow zone of ice sheets, it is greatly limited by spatial and temporal variability in liquid water and refrozen subsurface ice structures {cite:p}`tedesco_2014`, and relies highly on in situ measurements {cite:p}`rees_2005`.
An additional classification for glacial ice might need to be introduced since common scattering signatures for snow detection can result in a lack of scattering for large regions of Greenland and Antarctica {cite:p}`grody_basist_1996`.

```{figure} ./figures/emission-ambient.png
--- 
name: emission-ambient
width: 350px
---
Schematic of the effect of ambient conditions (vegetation and liquid water content) on the microwave emission from snow.
```

% challenges: water, mountains, vegetation
Liquid water similarly poses a key challenge in form of water bodies.
For that reason, large waters such as oceans and large lakes are commonly masked out, as are pixels that cover large percentages of water e.g. in coastal areas or lakeland.
Another problem is that most of the Earth’s seasonal snow cover occurs in complex landscapes {cite:p}`rees_2005`.
Firstly, mountainous terrain hinders dry snow detection since large spatial differences in snow depth are to be expected: whilst deep snow eventually reaches saturation depth, the signal of areas with shallow snow prevails which may be mistaken for bare ground.
And secondly, the changes in slope gradient within the sensor footprint cause variations in (local) observation angle and thus in view-dependent emissivity which again may be falsely identified as snow-free conditions {cite:p}`tedesco_2014`.
Besides, overlying vegetation reflects upwelling microwave radiation and emits some on its own {cite:p}`grody_basist_1996`, as illustrated in {numref}`emission-ambient`.
Snow cover in forested areas consequently presents higher emissivities and brightness temperatures than in unforested regions.

## Algorithm Selection 

The selection of algorithms mainly addresses dry snow detection. Later development stages may focus on the determination of subnivean soil properties.

### Dry Snow Detection

For the TSA product, the algorithm by {cite:t}`hall_2002` is selected with updated thresholds as proposed by {cite:t}`pulliainen_2010`.
The algorithm in this form is found to perform best for the channels available from CIMR, according to a recent study by {cite:t}`zschenderlein_2023`.
This study includes an extensive long-term comparison of PMW dry snow detection approaches focusing on the Ka and Ku-bands, namely {cite:t}`chang_1987,grody_basist_1996,foster_1997,armstrong_brodzik_2001`, {cite:t}`hall_2002` and {cite:t}`pulliainen_2010`.
The latter two algorithms are implemented in the GlobSnow v3.0 SWE product and in the EUMETSAT H SAF snow status (dry/wet) H11 product and are thus referred to as *GlobSnow* and *H SAF*, respectively.

```{note}
Due to significant differences in microwave emission between wet and dry snow {cite:p}`matzler_1994,rees_2005`, the PMW methods mentioned here apply only to dry snow conditions with liquid water content equal to zero, and are furthermore static i.e. disregarding temporal variations for instance in snow grain size or snow density.
```

PMW dry snow detection algorithms are known to generally underestimate the presence of snow due to their sensitivity to vegetation and liquid water content of the snowpack, among other reasons.
This can be seen in {numref}`difference` which illustrates the difference between snow extent as estimated by GlobSnow and H SAF for brightness temperatures of SSM/I and SSMIS, with respect to snow maps of the Interactive Multisensor Snow and Ice Mapping System (IMS).
Daily IMS maps are based on multiple input sources and human analysis, and serve therefore as reliable reference for global snow extent instead of ground-truth though only pointwise weather station measurements.
A negative number indicates the days per pixel for which the PMW algorithm flags 'snow-free' and IMS data flags 'snow', and vice versa for a positive number.
The difference shown in {numref}`difference` then gives the final sum of both cases for every day of the investigated time period, and thus shows the tendency of an algorithm to under- or overestimate (and not necessarily the actual number of days that it deviates from IMS data).
The better performance of H SAF over GlobSnow is apparent.

```{figure} ./figures/difference.png
--- 
name: difference
width: 600px
---
Difference maps of PMW algorithms with respect to IMS data over all snow seasons (September-February) from 2007/2008 until 2016/2017 above 40° N, based on {cite:t}`zschenderlein_2023`.
```

The daily mean TSA of the same time period for both algorithms and IMS maps as shown in {numref}`area` again highlights the impact of the updated thresholds of {cite:t}`pulliainen_2010`: the underestimation in TSA by GlobSnow is significantly larger than by H SAF.
Even though the spatial correctness of the TSA as estimated by the PMW approaches is not validated against in-situ measurements or IMS data, the evaluation by {cite:t}`zschenderlein_2023` indicates that the computed snow extents are representative.

```{figure} ./figures/area.png
--- 
name: area
width: 500px
---
Daily mean terrestrial snow area for snow seasons from 2007/2008 until 2016/2017 as estimated by PMW algorithms (solid lines) with respect to IMS data (dashed line) above 40° N, adapted from {cite:t}`zschenderlein_2023`.
```

Investigations on the implementation of the X and C-band will be based for instance on the work of {cite:t}`kelly_2009`.

### Subnivean Soil Status

A possible future implementation of L-band brightness temperatures in order to specify the soil status underneath the snowpack may be based on {cite:t}`rautiainen_2014`.