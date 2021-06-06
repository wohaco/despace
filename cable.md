# Cables
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [Cable](cable.md), [GNC](gnc.md)

[TOC]

---

> <small>**Cables, Onboard cables (OBC)** — EN term. **Бортовая кабельная сеть (БКС)** — RU analogue.</small>

**Бортовая кабельная сеть (БКС)** предназначена для электрического объединения отдельных приборов в системы и для электрического соединения систем между собой. Includes in common:

   1. Connectors
   1. Mounting elements
   1. Wires

По опыту [резервируются](reserve.md) следующие массы БКС КА от сухой массы КА: на этапе [АП](rnd_ap.md) — 12 ‑ 20 %, на этапе [ЭП](rnd_ep.md) — 7 ‑ 12 %. Среднестатистические массы:

   1. 1 погонного метра силового кабеля: 0.0133 ㎏;
   1. 1 разъёма: 0.015 ㎏.

**Connectors**

|*Picture*|*Description*|
|:--|:--|
|![](f/cable/de_9_1_thumb.jpg)|[CAN](can.md)<br> (data exchange, only data‑link layer)|
|*No spec.*|[JTAG](jtag.md)<br> (testing)|
|*No spec.*|[LVDS](lvds.md)<br> (data exchange, physical layer only)|
|![](f/cable/mil_std_1553_1_thumb2.jpg)|[MIL-STD-1553](mil_std_1553.md) (МКО)<br> (data exchange)|
|![](f/cable/db_25_1_thumb.jpg)|[RS-232](rs_xxx.md) (DB-25)<br> (data exchange)|
|![](f/cable/de_9_1_thumb.jpg)|[RS-422](rs_xxx.md) (DE-9)<br> (data exchange)|
|![](f/cable/de_9_1_thumb.jpg)|[RS-485](rs_xxx.md) (DE-9)<br> (data exchange)|
|![](f/cable/micro_d_1_thumb.jpg)|[SpaceWire](spacewire.md)<br> (data exchange, currently **most perspective**)|


## Designers, manufacturers
   - **РФ:**
     1. БКС КА производят все, кто производит КА ([ВНИИЭМ](zz_vniiem.md), [ИСС](zz_iss_r.md), [LAV](zz_lav.md) и т.д.)
     1. межблочную БКС производят все, кто производит бортовую аппаратуру



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](qa.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Cable](cable.md) •··**<br> [CAN](can.md)┊ [LVDS](lvds.md)┊ [MIL‑STD‑1553](mil_std_1553.md)┊ [RS‑232, 422, 485](rs_xxx.md)┊ [SpaceWire](spacewire.md)┊ [ОТБКС](cable_ct.md)|
|**··• [Guidance, Navigation & Control (GNC)](gnc.md) •··**<br> [CAN](can.md)┊ [LVDS](lvds.md)┊ [MIL‑STD‑1553](mil_std_1553.md) (МКО)┊ [RS‑232, 422, 485](rs_xxx.md)┊ [SpaceWire](spacewire.md)┊ [АСН, САН](ans.md)┊ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](acup.md)┊ [БКС](cable.md)┊ [БУ](sp.md)┊ [БШВ](time.md)┊ [Гироскоп](iu.md)┊ [Дальномер](doppler.md) (ИСР)┊ [ДМ](iu.md)┊ [ЗД](sensor.md)┊ [Компьютер](obc.md) (ЦВМ, БЦВМ)┊ [Магнитометр](sensor.md)┊ [МИХ](mic.md)┊ [МКО](mil_std_1553.md)┊ [ПО](soft.md)┊ [ПНА, ПОНА, ПСНА](aiad.md)┊ [СД](sensor.md)┊ [Система координат](coord_sys.md)┊ [СОСБ](spos.md)|

   1. Docs: …
   1. Notable interwikies — …
