# Payload Definition Document
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [Doc](doc.md), [OE](oe.md)

[TOC]

---

> <small>**Payload Definition Document (PDD)** — англоязычный термин, не имеющий аналога в русском языке. **_** — дословный перевод с английского на русский.</small>

**Payload Definition Document (PDD)** — документ, используемый [ESA](zz_esa.md) в рамках разработки [R&D](rnd.md) — содержит в себе описание, требования и характеристики научных задач миссии и научной аппаратуры, а также анализ возможности реализации миссии данной научной аппаратурой.

**Typical table of contents:**

   - 1 INTRODUCTION
      - 1.1 Scope
      - 1.2 Reference documentation
         - 1.2.1 Applicable documents
         - 1.2.2 Reference documents
      - 1.3 Acronyms
      - 1.4 Definitions
   - 2 SYSTEM ARCHITECTURE OVERVIEW
      - 2.1 Spacecraft Architecture
      - 2.2 Reference Payload complement
   - 3 INSTRUMENT PERFORMANCE REQUIREMENTS
   - 4 PAYLOAD INTERFACE REQUIREMENTS
   - 5 REFERENCE PAYLOAD COMPLEMENT
      - 5.1 Payload unit #1
         - 5.1.1 Payload Overview and Design Justification
         - 5.1.2 Instrument electronics/Data handling
         - 5.1.3 Budgets/ Interfaces
            - 5.1.3.1 Mass budget
            - 5.1.3.2 Thermal/Cryogenic Budget
            - 5.1.3.3 Power Budget
            - 5.1.3.4 Data Rate Budget
         - 5.1.4 Volume
            - 5.1.4.1 Configuration
            - 5.1.4.2 Mass
         - 5.1.5 Data
         - 5.1.6 Power



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](qa.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**`Documents:`**<br> …|
|**`Бортовая аппаратура (БА):`**<br> [PDD](pdd.md)┊ [Антенна](antenna.md)┊ [АПС](hns.md)┊ [БУ](sp.md)┊ [ЗУ](ds.md)┊ [Изделие](unit.md)┊ [КЛЧ](clean_lvl.md)┊ [ПЗР](fov.md)┊ [ПО](soft.md)┊ [Прототип](prototype.md)┊ [Радиосвязь](comms.md)┊ [СКЭ](elmsys.md)┊ [ССИТД](tsdcs.md)┊ [СИТ](etedp.md)┊ [УГТ](trl.md)┊ [ЭКБ](elc.md)┊ [EMC](emc.md)|

   1. Docs:
      - [Solar Orbiter PDD ❐](f/doc/pdd_solar_orbiter_esa_2004.pdf) (2004 г)
      - [EChO PDD ❐](f/doc/pdd_echo_esa_2013.pdf) (2013 г)
   1. Notable interwikies — …
   1. <…>
