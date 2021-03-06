# Бортовой комплекс управления
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [GNC](gnc.md), [Control](control.md)

[TOC]

---

> <small>**Бортовой комплекс управления (БКУ)** — русскоязычный термин. **Guidance, navigation, control (GNC)** — примерный англоязычный эквивалент.</small>

**Бортовой комплекс управления (БКУ)** — это совокупность систем КА, обеспечивающих управление функционированием КА. БКУ предназначен для:

   1. управления движением [центра масс](mic.md) КА и движением вокруг центра масс;
   1. наведения [АФС](comms.md) на [НС](scs.md);
   1. управления [бортовой аппаратурой](oe.md);
   1. контроля работоспособности БА, переключения резервной аппаратуры в программируемых случаях;
   1. сверки и коррекции [БШВ](time.md).

**Составные части:**

   1. [Автономная система навигации](ans.md) (АСН, САН);
   1. [Блоки автоматики и подрыва пиротехники](acup.md) (БАППТ);
   1. [Бортовая кабельная сеть БКУ](cable.md) (БКС);
   1. [Блок управления](sp.md) (БУ);
   1. [Гироскоп](iu.md);
   1. [Дальномер](doppler.md) (ИСР, измеритель скорости и расстояния);
   1. [Двигатель‑маховик](iu.md) (ДМ);
   1. [Звёздный датчик](sensor.md) (ЗД);
   1. [Компьютер](obc.md) (ЦВМ, БЦВМ);
   1. [Магнитометр](sensor.md);
   1. [Программное обеспечение](soft.md);
   1. [Привод направленной антенны](aiad.md) (ПНА, ПОНА, ПСНА);
   1. [Солнечный датчик](sensor.md) (СД);
   1. [Система ориентации солнечных батарей](spos.md) (СОСБ);
   1. [Система электроавтоматики](ea_sys.md) (СЭА);

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



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Guidance, Navigation & Control (GNC)](gnc.md) •··**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md) (МКО)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [АСН, САН](ans.md)・ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](acup.md)・ [БКС](cable.md)・ [БУ](sp.md)・ [БШВ](time.md)・ [Гироскоп](iu.md)・ [Дальномер](doppler.md) (ИСР)・ [ДМ](iu.md)・ [ЗД](sensor.md)・ [Компьютер](obc.md) (ЦВМ, БЦВМ)・ [Магнитометр](sensor.md)・ [МИХ](mic.md)・ [МКО](mil_std_1553.md)・ [ПО](soft.md)・ [ПНА, ПОНА, ПСНА](aiad.md)・ [СД](sensor.md)・ [Система координат](coord_sys.md)・ [СОСБ](spos.md)|
|**`Управление:`**<br> [Ad hoc](ad_hoc.md)・ [MoU](mou.md)・ [NX](nx.md)・ [Teamcenter](teamcenter.md)・ [Авторский надзор](des_spv.md)・ [Балансовая комиссия](outccom.md)・ [Бережливое производство](lean_man.md)・ [БУ](sp.md)・ [БНО](nnb.md)・ [Болото](swamp.md)・ [GNC](gnc.md)・ [Вето](veto.md)・ [ГОСТ 15.208](гост_15_208.md)・ [Гос. программа вооружения](plan_sa.md)・ [Грав.манёвр](gravass.md)・ [Документ планирования](plan.md)・ [Индустриальная археология](ind_arch.md)・ [Инженер (Engineer)](se.md)・ [Кворум](quorum.md)・ [Командировка](business_travel.md)・ [Компетенция](competence.md)・ [Куратор](curator.md)・ [Метод Шульце](schulze_method.md)・ [МИХ](mic.md)・ [НКО](nonprof_org.md)・ [НТД](st_act.md)・ [Научно‑технический совет](satc.md)・ [Научно‑техническое сопровождение](rnd_support.md)・ [Одно окно](sw_sys.md)・ [Оргструктура](orgstruct.md)・ [Патенты](patent_res.md)・ [Поручение](errand.md)・ [Принцип Питера](peter_principle.md)・ [Раб.процесс](workflow.md)・ [Рабочая группа](wg.md)・ [Рекурсия](recurs.md)・ [Руководитель](manager.md)・ [Руководство ОКР](mgmt.md)・ [САС](lifetime.md)・ [Свод знаний по управлению проектами](pmbok.md)・ [Секретность](confident.md)・ [Ситуационное лидерство](situ_leadership.md)・ [Система координат](coord_sys.md)・ [Скунсовая фабрика](skunk_works.md)・ [Совет главных конструкторов](cocd.md)・ [Совещание](meeting.md)・ [СУ](cs.md)・ [Теория заговора](consp_theory.md)・ [ТРИЗ](triz.md)・ [Указание](instruction.md)・ [Уровни готовности технологии](trl.md)・ [Уровни зрелости концепта](cml.md)・ [Уровни зрелости управления](mml.md)・ [ФКП](fed_sp.md)・ [ФЦП](fed_tp.md)・ [ФЗ](fed_law.md)・ [ЦУП](цуп.md)・ [ЭЦП](esig.md)・ [Эффект Оберта](oberth_eff.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://ru.wikipedia.org/wiki/Система_ориентации_космического_аппарата>

