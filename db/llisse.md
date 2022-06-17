# LLISSE
> .. [🚀](../../index/index.md) [despace](index.md) → **[](.md)** <mark>NOCAT</mark>  
> *Navigation:*  
> **[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·Событ., **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ

**Table of contents:**

[TOC]

---

> <small>**Long-Lived In-situ Solar System Explorer (LLISSE)** — EN term. **Местный Долгоживущий Исследователь Солнечной Системы (МДИСС)** — literal RU translation.</small>

<p style="page-break-after:always"> </p>

|*Parameter*|*[Value](si.md)*|
|:-|:-|
|Duration|≥ 90 days (~117 days in the best case)|
|Program|[Venera-D](venera_d_open_ru.md)|
|Goal|Returning compositional and physical information about near‑surface winds|
|Developer|NASA|
|Mass|10 ㎏|
|Orbit / Place|Surface|
|Payload|METEO, MEMS chemical sensor|

***Targets and investigations:***

   - **T** — technical; **C** — contact research; **D** — distant research; **F** — fly‑by; **H** — manned; **S** — soil sample return; **X** — technology demonstration
   - **Sections of measurement and observation:**
      - Atmospheric/climate — **Ac** composition, **Ai** imaging, **Am** mapping, **Ap** pressure, **As** samples, **At** temperature, **Aw** wind speed/direction.
      - General — **Gi** planet’s interactions with outer space.
      - Soil/surface — **Sc** composition, **Si** imaging, **Sm** mapping, **Ss** samples.

<small>

|*EVN‑XXX*|*T*|*EN*|*Section of m&o*|*D*|*C*|*F*|*H*|*S*|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|EVN‑006|T|Exploration: from surface.| | |C| | | |
|EVN‑007| |Atmosphere: connection between the topography & the atmo circulation.| |D| | | | |
|EVN‑010| |Atmosphere: vertical model.| |D| | | | |
|EVN‑013| |Atmosphere: illumination of the surface & the atmo layers.| |D| | | | |
|EVN‑014| |Atmosphere: composition.| |D| | |F| |
|EVN‑019| |Atmosphere: energetic balance.| |D| | | | |
|EVN‑025| |Surface: structure.| | |C| | | |
|EVN‑026| |Surface: elemental composition.| | |C| | | |
|EVN‑031| |Atmosphere: long‑term variations of the surface meteo characteristics.| |D| | | | |
|EVN‑034| |Atmosphere: nature of the superrotation.| |D| | | | |
|EVN‑041| |Common connection between the atmosphere & the surface.| |D| | | | |
|EVN‑044| |Surface: nature & causes of forming of the current rocks & soils.| | |C| | | |
|EVN‑058|T|Exploration: directed seismoexperiment.| |D| |F| | |
|EVN‑069|T|Prolonged surface‑spacecraft functioning.| | |C| | | |
|EVN‑089| |Measuring the planetary gravitational field.| |D| |F| | |
|EVN‑094|T|High temperature electronics.| |D|C|F| | |
|EVN‑095| |Climate: history & causes of changes.| |D| | | | |

</small>



<p style="page-break-after:always"> </p>


## Technology Readiness Level

As of December 2018, the LLISSE project has made notable progress toward its objectives. The capability of the core electronics has been increased by over an order of magnitude since the start of the project less than 2 year ago. Components of some of the important subsystems, like communications, have been developed and proof-of-concepts have been demonstrated. A recent test verified successful integrated operations between driving electronics and the supported sensor. If the project continues on its successful path, it will demonstrate a battery-powered version of a breadboard fidelity probe in late 2019 to early 2020. The system-level demonstration test will be conducted in the NASA Glenn Extreme Environments Rig (GEER), which will replicate Venus surface temperature, pressure, and chemistry. The system is planned to have full functional capability (although not with a flight‑like structure and not at the final communication frequency it will have in flight). This demonstration will provide a high degree of confidence that the probe will work on Venus. Final demonstration of full communication capability (operations between 50 and 150 ㎒) is planned in the project schedule in 2021. A lower fidelity wind-powered version of LLISSE is also being developed in the same timeframe. 

Demonstration full performance for the desired life is expected to occur in the 2019 to 2021 timeframe. Until that happens, LLISSE as a system will be in the TRL 3 to 4 range and relatively high technology risk. 

Current LLISSE development scope does not include vibration or shock testing; however, LLISSE is being designed to successfully pass those and other relevant tests once the launch and other environments are known.

In the recommended baseline mission, LLISSE serves as a companion to Venera-D in that ➀ Venera-D will include a long-duration orbiter, which will perform the necessary data relay functionality, and ➁ Venera-D will include a main lander, which will serve as host to help deliver the small LLISSE probes to the Venus surface. The main Venera-D lander will have sophisticated instruments and sensors that can complete their mission in ~2 hr. Inclusion of a contributed LLISSE probe will allow for continued weather and chemical species variability data to be collected at that site for three months, and thus enhancing the science in a unique way.

The remarkable operating life of LLISSE is enabled by three key elements, namely:

   - high‑temperature electronics and systems that operate without cooling at Venus surface conditions ([EVN‑094](venus.md));
   - use of simple instrumentation and supporting avionics with emphasis on low data volume instruments and sensors;
   - minimizing energy utilization through a novel operations approach.



<p style="page-break-after:always"> </p>

## Description

A baseline Venera-D mission would consist of an orbiter and a VEGA-type lander with an attached Long-Lived, In-Situ Solar System Explorer (LLISSE). This station will provide sporadic monitoring of meteorological parameters at the surface over three months ([EVN‑006](venus.md), [EVN‑031](venus.md), [EVN‑069](venus.md)), possibly identifying the origin of gravity waves ([EVN‑089](venus.md)), which have been evident in the atmosphere over a broad altitude range extending up to at least 90 km. 

As with [SAEVe](saeve.md), there are no power, data, or thermal controls required for LLISSE during cruise. The LLISSE battery, and therefore, probe would stay dormant during cruise and launch.  To provide comparative measurements, the chemical and atmospheric sensor suite on the LLISSE will commence taking measurements when it reaches a specific internal temperature (details will be worked out for Phase Ⅲ) and communications to the main orbiter are established.

LLISSE probes are small and lightweight (~200 ㎜ and 10 ㎏) but will function on the surface of Venus for 90 days or longer ([EVN‑069](venus.md)). The LLISSE project includes the design and development of two probes (battery and wind powered) and demonstration tests to confirm functionality over the desired life at Venus surface conditions.

As a power supply, 2 options are offered: a primary battery designed for a working time of about 3000 hours and a wind battery with a small wind turbine. The wind-powered version could theoretically have indefinite life.

<small>

|*Battery Version*|*Wind Powered Version*|
|:-|:-|
|![battery_version](f/project/l/llisse/llisse1.webp)|![wind_powered_version](f/project/l/llisse/llisse.webp)|
|Resource 3 000 hours|Resource is not defined|

</small>

The long-lived stations are not expected to have any memory for storing data and measurements are immediately sent to the transmitter for reception by any available communications receiver on the main orbiter or other relay assets such as the small satellites around L1 and/or L2 points (which will likely provide longer communication windows as the planet slowly rotates).

Low-power, high‑temperature sensors are being employed ([EVN‑094](venus.md)) to take the periodic meteorology measurements listed above and chemical composition ([EVN‑077](venus.md)). These periodic measurements (assumed to be every 8 hr) would occur over 60 days, covering at least one terminator.



<p style="page-break-after:always"> </p>

## Objectives and Payload

The key goals of LLISSE and its long-duration measurements are to increase our knowledge of superrotation of the atmosphere ([EVN‑034](venus.md)), the climate and its evolution ([EVN‑095](venus.md)), and surface-atmosphere interaction ([EVN‑041](venus.md)). These goals are achieved by taking measurements of wind speed and direction, temperature, pressure, incident and reflected solar radiance, and abundance of local selected atmospheric chemical species.

***Prioritized LLISSE Goals and Measurements:***

<small>

|*Objective Title*|*Science Objectives*|*Measurements*|*Priority*|
|:-|:-|:-|:-|
|L2b. Near-surface atmospheric composition ([EVN‑014](venus.md), [EVN‑077](venus.md))|Long-term study of possible variation of near‑surface atmospheric composition|Measure abundances of predefined components|High|
|L3b. Near-surface meteorological (METEO) parameters (pressure, temperature, wind speed, and direction) ([EVN‑031](venus.md))|Study of long-term characteristics of near‑surface dynamics, waves, thermal tides, and atmosphere-surface interaction|Long-term measurements of near‑surface temperature, pressure, wind speed, and direction; incident and reflected radiation|High|
|L4b. Solar fluxes on the surface ([EVN‑013](venus.md), [EVN‑019](venus.md), [EVN‑080](venus.md))|Surface albedo. Study of factors that influence solar illumination (cloud opacity, local time, local relief, etc.)|Measurements of incident and reflected solar radiation over 60 days|Medium|

</small>

One station LLISSE at the moment is part of the base of the mission Venera-D. Multiple stations could provide enhanced surface coverage by extending the capability of the Venera-D mission to several points (observing possibly two LSTs and/or latitudes simultaneously). This would improve our understanding of the impact of local topography, solar time, and meridional transport processes on the superrotation mechanism ([EVN‑007](venus.md)). The level of technological risk is high. The priority for the second LLISSE is 6 (the lowest). Potential contribution of the second LLISSE station − will allow a more complete study of goals:

   - L1. Atmosphere composition during descent ([EVN‑014](venus.md), [EVN‑077](venus.md));
   - L2. Atmosphere composition at the surface and near‑surface atmospheric composition ([EVN‑014](venus.md), [EVN‑077](venus.md));
   - L5. Surface structure and morphology ([EVN‑025](venus.md), [EVN‑044](venus.md));
   - L6. Surface elemental composition ([EVN‑026](venus.md));
   - L9. Electromagnetic fields;
   - O1: Vertical structure of mesosphere, temperature, clouds, and dynamics of cloud-born gases and vertical structure of troposphere, temperature, clouds, composition, and dynamics ([EVN‑010](venus.md), [EVN‑017](venus.md), [EVN‑074](venus.md)).

***Composition of LLISSE scientific instruments:***

<small>

|*Data Sheet(s) Completed*|*Instrument or Specific Subsystem*|*Description*|*Size*|*Mass, ㎏*|*Power, W*|*Data, ㎆/h*|*Science Priority*|*TRL*|*Time Required to be Ready for Mission, Years*|*Rationale / Other Comments*|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|☑|METEO|Temperature, pressures, radiance, and wind speed and direction sensors|Fits on 20 ㎜ station|<0.2|—|—|High|4 to 5|5|TRL driven by radiance sensing|
|☑|Microelectromechanical systems chemical sensor|Detect and measure concentration of preselected element set|Fits on 20 ㎜ station|<0.2|—|—|High|5|3| |

</small>

> Notes:
> 
   - ☑ — This mark signifies that a datasheet is complete and available.
   - instrument characteristics (physical properties) are shown for the worst expected case.



<p style="page-break-after:always"> </p>

## Docs & links
|*Sections & pages*|
|:-|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs:
      - [Venera-D Phase II Final Report](Venera-DPhaseIIFinalReport.pdf)
   1. <https://www.lpi.usra.edu/vexag/meetings/archive/vexag_14/presentations/27-Kremic-Long-Lived%20Venus%20Station.pdf>
   1. <…>
