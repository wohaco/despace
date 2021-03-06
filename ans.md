# Система автономной навигации
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [GNC](gnc.md)

[TOC]

---

> <small>**Система автономной навигации (САН) / Автономная система навигации (АСН)** — русскоязычный термин. **Autonomous navigation system (ANS)** — англоязычный эквивалент.</small>

**Система автономной навигации (САН)** — бортовая система [КА](sc.md), предназначенная для координатно‑временного и навигационно‑баллистического обеспечения функционирования КА в части определения координат и вектора скорости КА, формирования сигналов [шкалы времени](time.md) и выдачи этой [целевой информации](info.md) в [GNC](gnc.md).

**Автономная система навигации (АСН)** — синоним.



## Описание САН
САН относится к **астроинерциальной системе навигации**, основанной на комплексировании астрономической и инерциальной навигации.

**Состав САН:**  
░╟ аппаратура радионавигации (АРН);  
░╟ [антенно‑фидерное устройство (АФУ)](afdev.md) САН с МШУ;  
░╙ программное обеспечение (ПО) САН.

САН предназначена для:

   - определения и выдачи в БКУ вектора состояния (координат и вектора скорости) КА в гринвичской системе координат ПЗ‑90.02 по измерениям навигационных параметров по НКА ГЛОНАСС и GPS на заданный момент времени;
   - формирования и выдачи по [МКО](mil_std_1553.md) в БКУ текущих значений времени по шкале времени (ШВ) САН, поправок к ШВ ГЛОНАСС и UTC;
   - измерений навигационных параметров (псевдодальности и псевдоскорости), их привязке к шкале времени САН;
   - приёма от навигационных КА (НКА) цифровой информации.

САН взаимодействует в составе КА с [GNC](gnc.md), [СЭС](sps.md) и [ТМС](tms.md) КА. САН в части взаимодействия с другими системами КА функционирует под управлением БКУ.



## Designers, manufacturers
   - **РФ:**
      1. [ИРЗ](zz_irz.md)
      1. [ИСС](zz_iss_r.md)
      1. [НПЦАП](zz_npcap.md)
      1. [РИРВ](рирв.md)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Guidance, Navigation & Control (GNC)](gnc.md) •··**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md) (МКО)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [АСН, САН](ans.md)・ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](acup.md)・ [БКС](cable.md)・ [БУ](sp.md)・ [БШВ](time.md)・ [Гироскоп](iu.md)・ [Дальномер](doppler.md) (ИСР)・ [ДМ](iu.md)・ [ЗД](sensor.md)・ [Компьютер](obc.md) (ЦВМ, БЦВМ)・ [Магнитометр](sensor.md)・ [МИХ](mic.md)・ [МКО](mil_std_1553.md)・ [ПО](soft.md)・ [ПНА, ПОНА, ПСНА](aiad.md)・ [СД](sensor.md)・ [Система координат](coord_sys.md)・ [СОСБ](spos.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://ru.wikipedia.org/wiki/Астроинерциальная_навигация>

