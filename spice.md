# SPICE
> 2019.08.05 [🚀](../index/index.md) [despace](index.md) → [БНО](nnb.md), **[Модель](model.md)**

[TOC]

---

> <small>**Spacecraft planet instrument C‑matrix events (SPICE)** — англоязычный термин, не имеющий аналога в русском языке. **Космический аппарат, планета, прибор, ориентация, события** — дословный перевод с английского на русский.</small>

**Spacecraft planet instrument C‑matrix events (SPICE)** — программное обеспечение и база данных для моделирования и анализа траекторий, орбит, ориентации, полей зрения, доступности радиосвязи и Солнца и пр.

[Open‑source](soft.md). [ITAR](itar.md)‑free.



## Описание
The SPICE system’s logical components and the actual data files — the kernels — used to realize those components are summarized below.

   - **S —** Spacecraft ephemeris, given as a function of time. (SPK)
   - **P —** Planet, satellite, comet, or asteroid ephemerides, or more generally, location of any target body, given as a function of time. (also SPK). The **P** component also logically includes certain physical, dynamical and cartographic constants for target bodies, such as size and shape specifications, and orientation of the spin axis and prime meridian. (PCK)
   - **I —** Instrument information containing descriptive data peculiar to the geometric aspects of a particular scientific instrument, such as field‑of‑view size, shape and orientation parameters. (IK)
   - **C —** Orientation information, containing a transformation, traditionally called the «C‑matrix», which provides time‑tagged pointing (orientation) angles for a spacecraft bus or a spacecraft structure upon which science instruments are mounted. The **C** component may also include angular rate data for that structure. (CK)
   - **E —** Events information, summarizing mission activities — both planned and unanticipated. Events data are contained in the SPICE E‑kernel file set, which consists of three components: Science Plans, Sequences, and Notes. (EK)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Patent](патент.md)**·Пат., **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**`Баллистико‑навигационное обеспечение (БНО):`**<br> [SPICE](spice.md)・ [Апоцентр и перицентр](apopericentre.md)・ [Гравманёвр](gravass.md)・ [Кеплеровы элементы](keplerian.md)・ [Космическая скорость](esc_vel.md)・ [Сфера Хилла](hill_sphere.md)・ [Терминатор](terminator.md)・ [Точки Лагранжа](l_points.md)・ [Эффект Оберта](oberth_eff.md)|
|**`Модель:`**<br> [DEM](digital_elev_model.md)・ [SPICE](spice.md)・ [ВДМ](vd_model.md)・ [Лимит](limit.md)・ [МИХ](mic.md)・ [Осциллятор](oscillator.md)|
|**【[Software](soft.md)】**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](c.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [PDF](pdf.md)・ [Python](python.md)・ [R](r.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](systems_tool_kit.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs:
      - [Презентация, ИКИ РАН, Ледков, 2015 ❐](f/soft/spice_20150101_1.pdf)
   1. Notable interwikies — …
   1. <https://naif.jpl.nasa.gov/naif/toolkit.html>
