# Ames Stereo Pipeline
> 2019.09.13 **[🚀](../index/index.md) [despace](index.md)** → **[Soft](soft.md)**

[TOC]

---

> <small>*Термины:* **Ames Stereo Pipeline (ASP)** — англоязычный термин, не имеющий аналога в русском языке. **Стереотруба центра Эймса** — дословный перевод с английского на русский.</small>

The **NASA Ames Stereo Pipeline (ASP)** is a suite of free & open source automated geodesy & stereogrammetry tools designed for processing stereo imagery captured from satellites (around Earth & other planets), robotic rovers, aerial cameras, & historical imagery, with & without accurate camera pose information. It produces cartographic products, including [digital elevation models (DEMs)](digital_elev_model.md), ortho‑projected imagery, 3D models, & bundle‑adjusted networks of cameras. ASP’s data products are suitable for science analysis, mission planning, & public outreach.

The Stereo Pipeline is part of the NASA [NeoGeography Toolkit](neogeography_toolkit.md).



## Описание
The Ames Stereo Pipeline (ASP) was developed by the Intelligent Robotics Group (IRG), in the Intelligent Systems Division at the National Aeronautics and Space Administration (NASA) Ames Research Center in Moffett Field, CA. It builds on over ten years of IRG experience developing surface reconstruction tools for terrestrial robotic field tests and planetary exploration.

Project Lead

   - Dr. Ross Beyer (NASA/SETI Institute)

Development Team

   - Oleg Alexandrov (NASA/Stinger-Ghaffarian Technologies)
   - Scott McMichael (NASA/Stinger-Ghaffarian Technologies)

Former Developers

   - Zachary Moratto (NASA/Stinger-Ghaffarian Technologies)
   - Michael J. Broxton (NASA/Carnegie Mellon University)
   - Dr. Ara Nefian (NASA/Carnegie Mellon University)
   - Matthew Hancher (NASA)
   - Mike Lundy (NASA/Stinger-Ghaffarian Technologies)
   - Vinh To (NASA/Stinger-Ghaffarian Technologies)

Contributing Developer & Former IRG Terrain Reconstruction Lead

   - Dr. Laurence Edwards (NASA)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|…°·•¹²³±×÷≤≥≈≠ ‑ −— ⎆✉ ❐“”’«»✔→✘☐☑├┕┆ 1 lb = 0.453592 kg; 1 g = 9.80665 m/s²|
|:--|
|<small>**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](camera.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Управ., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Errors](error.md)**·Ошибки, **[Events](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Project](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](quality.md)**·QA, **[R&D](rnd.md)**·НИОКР, **[RAMS](rams.md)**·НиБ, **[Risk](risk.md)**·Риск, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Планетоход, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодром, **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·Циклограмма, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ</small>|
|*Sections & pages*|
|**··• [Software](soft.md) •··**<br> [ASP](asp.md) ┊ [Blender](blender.md) ┊ [C](c.md) ┊ [Cosmographia](cosmographia.md) ┊ [DOORS](doors.md) ┊ [DWG](cad_f.md) ┊ [GIMP](gimp.md) ┊ [Git](git.md) ┊ [IGES](cad_f.md) ┊ [ISIS](isis.md) ┊ [JT](cad_f.md) ┊ [NGT](neogeography_toolkit.md) ┊ [NX](nx.md) ┊ [Octave](gnu_octave.md) ┊ [PDF](pdf.md) ┊ [Python](python.md) ┊ [R](r.md) ┊ [SPICE](spice.md) ┊ [STEP](cad_f.md) ┊ [STL](systems_tool_kit.md) ┊ [SVG](cad_f.md) ┊ [Syncthing](syncthing.md) ┊ [Teamcenter](teamcenter.md) ┊ [Система управления версиями](vcs.md) ┊ [ХРИП](adra.md) |

   1. Docs: …
   1. Notable interwikies — …
   1. <https://ti.arc.nasa.gov/tech/asr/groups/intelligent-robotics/ngt/stereo/>

