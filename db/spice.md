# SPICE
> 2019.08.05 [🚀](../../index/index.md) [despace](index.md) → [Soft](soft.md)
> *Navigation:*
> **[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·Событ., **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ

**Table of contents:**

[TOC]

---

> <small>**Spacecraft planet instrument C‑matrix events (SPICE)** — англоязычный термин, не имеющий аналога в русском языке. **Космический аппарат, планета, прибор, ориентация, события** — дословный перевод с английского на русский.</small>

**Spacecraft planet instrument C‑matrix events (SPICE)** — программное обеспечение и база данных для моделирования и анализа траекторий, орбит, ориентации, полей зрения, доступности радиосвязи и Солнца и пр.

[Open‑source](soft.md). [ITAR](itar.md)‑free.

The SPICE system’s logical components & the actual data files — the kernels — used to realize those components are summarized below.

|*#*|*Description*|
|:-|:-|
|**S**|Spacecraft ephemeris, given as a function of time. (SPK)|
|**P**|Planet, satellite, comet, or asteroid ephemerides, or more generally, location of any target body, given as a function of time. (also SPK). The **P** component also logically includes certain physical, dynamical & cartographic constants for target bodies, such as size & shape specifications, & orientation of the spin axis & prime meridian. (PCK)|
|**I**|Instrument information containing descriptive data peculiar to the geometric aspects of a particular scientific instrument, such as field‑of‑view size, shape & orientation parameters. (IK)|
|**C**|Orientation information, containing a transformation, traditionally called the «C‑matrix», which provides time‑tagged pointing (orientation) angles for a spacecraft bus or a spacecraft structure upon which science instruments are mounted. The **C** component may also include angular rate data for that structure. (CK)|
|**E**|Events information, summarizing mission activities — both planned & unanticipated. Events data are contained in the SPICE E‑kernel file set, which consists of three components: Science Plans, Sequences, & Notes. (EK)|



## Docs & links (TRANSLATEME ALREADY)
|*Sections & pages*|
|:-|
|**`Баллистико‑навигационное обеспечение (БНО):`**<br> [SPICE](spice.md)・ [Апоцентр и перицентр](apopericentre.md)・ [Гравманёвр](gravass.md)・ [Кеплеровы элементы](keplerian.md)・ [Космическая скорость](esc_vel.md)・ [Сфера Хилла](hill_sphere.md)・ [Терминатор](terminator.md)・ [Точки Лагранжа](l_points.md)・ [Эффект Оберта](oberth_eff.md)|
|**【[Software](soft.md)】**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](plang.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [OS](os.md)・ [PDF](pdf.md)・ [Python](plang.md)・ [R](plang.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](stk.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs: [Презентация, ИКИ РАН, Ледков, 2015 ❐](f/soft/spice_20150101_1.pdf)
   1. <https://naif.jpl.nasa.gov/naif/toolkit.html>
