# SPICE
> 2019.08.05 ┊ **🚀 [despace](index.md)** → [БНО](nnb.md), **[Модель](model.md)**

[TOC]

---

> <small>*Термины:* **Spacecraft planet instrument C‑matrix events (SPICE)** — англоязычный термин, не имеющий аналога в русском языке. **Космический аппарат, планета, прибор, ориентация, события** — дословный перевод с английского на русский.</small>

**Spacecraft planet instrument C‑matrix events (SPICE)** — программное обеспечение и база данных для моделирования и анализа траекторий, орбит, ориентации, полей зрения, доступности радиосвязи и Солнца и пр.

[Open‑source](soft.md). [ITAR](itar.md)‑free.



## Описание
The SPICE system's logical components and the actual data files — the kernels — used to realize those components are summarized below.

   - **S —** Spacecraft ephemeris, given as a function of time. (SPK)
   - **P —** Planet, satellite, comet, or asteroid ephemerides, or more generally, location of any target body, given as a function of time. (also SPK). The **P** component also logically includes certain physical, dynamical and cartographic constants for target bodies, such as size and shape specifications, and orientation of the spin axis and prime meridian. (PCK)
   - **I —** Instrument information containing descriptive data peculiar to the geometric aspects of a particular scientific instrument, such as field‑of‑view size, shape and orientation parameters. (IK)
   - **C —** Orientation information, containing a transformation, traditionally called the «C‑matrix», which provides time‑tagged pointing (orientation) angles for a spacecraft bus or a spacecraft structure upon which science instruments are mounted. The **C** component may also include angular rate data for that structure. (CK)
   - **E —** Events information, summarizing mission activities — both planned and unanticipated. Events data are contained in the SPICE E‑kernel file set, which consists of three components: Science Plans, Sequences, and Notes. (EK)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|…°·•¹²³±×÷≤≥≈≠ ‑ −— ⎆✉ ❐“”’«»✔→✘☐☑├┕┆ 1 lb = 0.453592 kg; 1 g = 9.80665 m/s²|
|:--|
|<small>**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](camera.md)**·Камера, **[Comms](comms.md)**·Радиосв., **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Управ., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Errors](error.md)**·Ошибки, **[Events](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эргоном., **[IMU](imu.md)**·Гироскоп, **[Incubator](incubator.md)**·Инкуб., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MAG](mag.md)**·Магнитом., **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Patent](патент.md)**·Патент, **[Project](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](quality.md)**·QA, **[R&D](rnd.md)**·НИОКР, **[RAMS](rams.md)**·НиБ, **[Risk](risk.md)**·Риск, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Планетоход, **[RTG](rtg.md)**·РИТЭГ, **[RW](rw.md)**·ДМ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодром, **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·Циклограмма, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ</small>|
|*Sections & pages*|
|**`Баллистико‑навигационное обеспечение (БНО):`**<br> [SPICE](spice.md) ┊ [Апоцентр и перицентр](apopericentre.md) ┊ [Гравманёвр](gravass.md) ┊ [Кеплеровы элементы](keplerian.md) ┊ [Космическая скорость](esc_vel.md) ┊ [Сфера Хилла](hill_sphere.md) ┊ [Терминатор](terminator.md) ┊ [Точки Лагранжа](l_points.md) ┊ [Эффект Оберта](oberth_eff.md) |
|**`Модель:`**<br> [DEM](digital_elev_model.md) ┊ [SPICE](spice.md) ┊ [ВДМ](vd_model.md) ┊ [Лимит](limit.md) ┊ [МИХ](mic.md) ┊ [Осциллятор](oscillator.md) |
|**··• [Software](soft.md) •··**<br> [ASP](asp.md) ┊ [Blender](blender.md) ┊ [C](c.md) ┊ [Cosmographia](cosmographia.md) ┊ [DOORS](doors.md) ┊ [DWG](cad_f.md) ┊ [GIMP](gimp.md) ┊ [Git](git.md) ┊ [IGES](cad_f.md) ┊ [ISIS](isis.md) ┊ [JT](cad_f.md) ┊ [NGT](neogeography_toolkit.md) ┊ [NX](nx.md) ┊ [Octave](gnu_octave.md) ┊ [PDF](pdf.md) ┊ [Python](python.md) ┊ [R](r.md) ┊ [SPICE](spice.md) ┊ [STEP](cad_f.md) ┊ [STL](systems_tool_kit.md) ┊ [SVG](cad_f.md) ┊ [Syncthing](syncthing.md) ┊ [Teamcenter](teamcenter.md) ┊ [Система управления версиями](vcs.md) ┊ [ХРИП](adra.md) |

**Docs:**

   1. [Презентация, ИКИ РАН, Ледков, 2015 ❐](f/soft/spice_20150101_1.pdf)

**Links:**

   1. Notable interwikies — …
   1. <https://naif.jpl.nasa.gov/naif/toolkit.html>
