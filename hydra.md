# Hydra
> 2019.07.24 [🚀](../index/index.md) [despace](index.md) → **[ЗД](sensor.md)**

[TOC]

---

> <small>**Hydra** — англоязычный термин, не имеющий аналога в русском языке. **Гидра** — дословный перевод с английского на русский.</small>

**Hydra** — звёздный датчик для определения и выдачи в [GNC](gnc.md) информации о положении и угловых скоростях системы координат (СК) изделия относительно геоцентрической СК.  
Разработчик [Sodern](zz_sodern.md), EU. Разработано в 2012 году получен УГТ 9. Активное применение.

|*Characteristics*|*[Value](si.md)<br> (Hydra / Hydra-M)*|*[Value](si.md)<br> (Hydra-TC)*|
|:--|:--|:--|
|Composition|2 ОБ (до 3), 1 БЭ|2 ОБ (до 3), 1 БЭ|
|Consumption, W|8|8|
|Dimensions, ㎜|⌀147 × 283 ОБ, 170 × 146 × 103 БЭ|⌀147 × 283 ОБ, 194 × 166 × 159 БЭ|
|[Interfaces](interface.md)|[RS-422](rs_xxx.md), [MIL-STD-1553B](mil_std_1553.md)|[RS-422](rs_xxx.md), [MIL-STD-1553B](mil_std_1553.md)|
|[Lifetime](lifetime.md)/Resource, h(y)|НОО: 87 600 (10)<br> ГСО: 157 680 (18)|НОО: 87 600 (10)<br> ГСО: 157 680 (18)|
|Mass, ㎏|4.6 (2 ОБ по 1.4, 1 БЭ по 1.8)|6.7 (2 ОБ по 1.4, 1 БЭ по 3.9)|
|[Overload](vibration.md), Grms|28 случайные, 2 000 ударные|30 случайные, 2 350 ударные|
|[Rad.resist](ion_rad.md), ㏉ (㎭)| | |
|[Reliability](qm.md) per [lifetime](lifetime.md)|0.99968 (200 FIT)|0.99968 (200 FIT)|
|[Thermal range](tcs.md), ℃|−30 ‑ +60|−30 ‑ +60|
|[TRL](trl.md)| | |
|[Voltage](voltage.md), V|… (21 ‑ 52)|… (21 ‑ 52)|
|**【Specific】**|• • •|• • •|
|Accept. ang. speed, °/s|10|7|
|Accuracy|2.1″|3.1″|
|Back. brightn., ㏅/m²| | |
|Delay, s, ≤| | |
|[FOV](fov.md), °|18.5|18.5|
|Identification time, s|1.5|2.5|
|Lens| | |
|Output data| | |
|Ready mode| | |
|Refresh rate, ㎐|16 ‑ 30|10 ‑ 30|
| |[![](f/sensor/h/hydra_pic2_thumb.jpg)](f/sensor/h/hydra_pic2.jpg)| |

**Notes:**

   1. Hydra is available in four different versions:
      - **Hydra** baseline, suited to all missions, optimized for earth-observation and science missions.
      - **Hydra-TC**, designed for hardened radiation env. Fully redundant EU version for 2 OH, GEO shielding.
      - **Hydra-M**, cost-optimized. Light LEO version for 1 or 2 OH without Thermo-Electric Cooler.
      - **Hydra-CP** (centralized), optimized for easy S/C accommodation. Software hosted into On-Board Computer.
   1. **Applicability:**
      - …

| |
|:--|
|[![](f/sensor/h/hydra_pic1_thumb.jpg)](f/sensor/h/hydra_pic1.jpg) [![](f/sensor/a/auriga_hydra_pic1_thumb.jpg)](f/sensor/a/auriga_hydra_pic1.jpg) и **[Видео ❐](f/sensor/h/hydra_logo_sodern.mkv)**|



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Patent](патент.md)**·Пат., **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**`Звёздный датчик (ЗД):`**<br> [Видимая звёздная величина](app_mag.md)・ [ПЗр](fov.md)<br>• • •<br> **Европа:** [ASTRO 15](astro_15.md) (6.15)・ [Hydra](hydra.md) (4.6)・ [ASTRO 10](astro_10.md) (3.8)・ [A-STR](a_str.md) (3.55)・ [AA-STR](aa_str.md) (2.6)・ [HE-5AS](he_5as.md) (2.2)・ [ASTRO APS](astro_aps.md) (2)・ [Horus](horus.md) (1.6)・ [T2](t2.md) (0.8)・ [T1](t1.md) (0.6 ‑ 1)・ [Auriga](auriga.md) (0.21)  ▮  **РФ:** [348К](348k.md) (3.45)・ [360К](360k.md) ()・ [АД-1](ad_1.md) (3.8)・ [БОКЗ-МФ](bokz_mf.md) (2.8)・ [мБОКЗ-2](мбокз_2.md) (1.5)・ [SX-SR-MicroBOKZ](sx_sr_microbokz.md) (0.5)  ▮  **США:** [HAST](hast.md) (7.7)・ [CT-2020](ct_2020.md) (3)・ [µSTAR](mustar.md) (2.1)・ [MIST](mist.md) (0.55) |

   1. Docs:
      - [Hydra baseline datasheet ❐](f/sensor/h/hydra_baseline_datasheet.pdf)
      - [Hydra-M datasheet ❐](f/sensor/h/hydra_m_datasheet.pdf)
      - [Hydra-TC datasheet ❐](f/sensor/h/hydra_tc_datasheet.pdf)
      - [Sodern presentation 2017 ❐](f/sensor/sodern_presentation_2017.pdf)
   1. Notable interwikies — …
   1. <http://www.sodern.com/website/en/ref/Hydra_316.html>

