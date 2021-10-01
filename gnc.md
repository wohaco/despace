# Бортовой комплекс управления
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [GNC](gnc.md), [Control](control.md)

[TOC]

---

> <small>**Бортовой комплекс управления (БКУ)** — русскоязычный термин. **Guidance, navigation, control (GNC)** — примерный англоязычный эквивалент.</small>

**Бортовой комплекс управления (БКУ)** — это совокупность систем КА, обеспечивающих управление функционированием КА. БКУ предназначен для:

   1. управления движением [центра масс](mic.md) КА и движением вокруг центра масс;
   1. наведения [АФС](comms.md) на [НС](scs.md);
   1. управления [бортовой аппаратурой](sc.md);
   1. контроля работоспособности БА, переключения резервной аппаратуры в программируемых случаях;
   1. сверки и коррекции [БШВ](time.md).

**Составные части:**

   1. [Автономная система навигации](ans.md) (АСН, САН);
   1. [Блоки автоматики и подрыва пиротехники](eas.md) (БАППТ);
   1. [Бортовая кабельная сеть БКУ](cable.md) (БКС);
   1. [Блок управления](sp.md) (БУ);
   1. [Гироскоп](iu.md);
   1. [Дальномер](doppler.md) (ИСР, измеритель скорости и расстояния);
   1. [Двигатель‑маховик](iu.md) (ДМ);
   1. [Звёздный датчик](sensor.md) (ЗД);
   1. [Компьютер](obc.md) (ЦВМ, БЦВМ);
   1. [Магнитометр](sensor.md);
   1. [Программное обеспечение](soft.md);
   1. [Привод направленной антенны](devd.md) (ПНА, ПОНА, ПСНА);
   1. [Солнечный датчик](sensor.md) (СД);
   1. [Система ориентации солнечных батарей](devd.md) (СОСБ);
   1. [Система электроавтоматики](eas.md) (СЭА);

**Стандарты и [интерфейсы](interface.md):**

|*Name*|*Purpose*|*Bitrate*|
|:--|:--|:--|
|[CAN](can.md)|data exchange, only data‑link layer|1 Mbit/s|
|[JTAG](jtag.md)|testing|—|
|[LVDS](lvds.md)|data exchange, physical layer only|655 Mbit/s|
|[MIL-STD-1553](mil_std_1553.md)|data exchange|1 Mbit/s|
|[RS-232](rs_xxx.md)|data exchange|0.1 Mbit/s|
|[RS-422](rs_xxx.md)|data exchange|10 Mbit/s|
|[RS-485](rs_xxx.md)|data exchange|10 Mbit/s |
|[SpaceWire](spacewire.md)|data exchange, currently most perspective|400 Mbit/s|



## Designers, manufacturers
   - **РФ:**
      1. БКУ КА производят все, кто производит КА ([ВНИИЭМ](zz_vniiem.md), [ИСС](zz_iss_r.md), [LAV](zz_lav.md) и т.д.)
      1. СЧ БКУ — см. соответствующую СЧ из списка выше

**Manufacturers**

| | |
|:--|:--|
|**AE**|…|
|**AU**|…|
|**CA**|…|
|**CN**|…|
|**EU**|…|
|**IL**|…|
|**IN**|…|
|**JP**|…|
|**KR**|…|
|**RU**|…|
|**SA**|…|
|**SG**|…|
|**US**|…|
|**VN**|…|



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Patent](патент.md)**·Пат., **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**【[Guidance, Navigation & Control (GNC)](gnc.md)】**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md) (МКО)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [АСН, САН](ans.md)・ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](eas.md)・ [БКС](cable.md)・ [БУ](eas.md)・ [БШВ](time.md)・ [Гироскоп](iu.md)・ [Дальномер](doppler.md) (ИСР)・ [ДМ](iu.md)・ [ЗД](sensor.md)・ [Компьютер](obc.md) (ЦВМ, БЦВМ)・ [Магнитометр](sensor.md)・ [МИХ](mic.md)・ [МКО](mil_std_1553.md)・ [ПО](soft.md)・ [ПНА, ПОНА, ПСНА](devd.md)・ [СД](sensor.md)・ [Система координат](coord_sys.md)・ [СОСБ](devd.md)|
|**【[Control](Control.md)】**<br> [Ad hoc](ad_hoc.md)・ [Business travel](business_travel.md)・ [Chief designers council](cocd.md)・ [CML](cml.md)・ [Competence](competence.md)・ [Confident](confident.md)・ [Consp.theory](consp_theory.md)・ [Control sys. (CS)](cs.md)・ [Coordinate system](coord_sys.md)・ [Curator](curator.md)・ [Designer’s supervision](des_spv.md)・ [E‑sig](esig.md)・ [Engineer](se.md)・ [Errand](errand.md)・ [Federal law](fed_law.md)・ [Federal TP](fed_tp.md)・ [Federal SP](fed_sp.md)・ [GNC](gnc.md)・ [Gravity assist](gravass.md)・ [Industrial archaeology](ind_arch.md)・ [Instruction](instruction.md)・ [Lean manuf.](lean_man.md)・ [Lifetime](lifetime.md)・ [Manager](manager.md)・ [MBSE](mbse.md)・ [Meeting](meeting.md)・ [MCC](scs.md)・ [MIC](mic.md)・ [MML](mml.md)・ [MoU](mou.md)・ [Nav. & ballistics (NB)](nnb.md)・ [Nonprofit org.](nonprof_org.md)・ [NX](nx.md)・ [Oberth effect](oberth_eff.md)・ [Org.structure](orgstruct.md)・ [Outcomes commission](outccom.md)・ [Patent](patent_res.md)・ [Peter prin.](peter_principle.md)・ [Plan](plan.md)・ [PMBok](pmbok.md)・ [Quorum](quorum.md)・ [R&D management](mgmt.md)・ [R&D support](rnd_support.md)・ [Recursion](recurs.md)・ [Schulze_method](schulze_method.md)・ [Sci'N'Tech activities](st_act.md)・ [Sci'N'Tech council](satc.md)・ [Single-window system](sw_sys.md)・ [Situ.leadership](situ_leadership.md)・ [Skunk works](skunk_works.md)・ [State arm. plan](plan_sa.md)・ [Swamp](swamp.md)・ [Teamcenter](teamcenter.md)・ [Tennis racket theorem](tr_theorem.md)・ [TRIZ](triz.md)・ [TRL](trl.md)・ [V‑model](v_model.md)・ [Veto](veto.md)・ [Workflow](workflow.md)・ [Workgroup](wg.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://ru.wikipedia.org/wiki/Система_ориентации_космического_аппарата>
   1. <https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control>

