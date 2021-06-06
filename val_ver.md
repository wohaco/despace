# Валидация и верификация
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [Test](test.md), [Качество](qa.md)

[TOC]

---

## Валидация

> <small>**Валидация** — русскоязычный термин. **Validation** — англоязычный эквивалент.</small>

**Валида́ция** *(от лат. validus «здоровый, крепкий; сильный»)* в технике или в системе менеджмента качества — доказательство того, что требования конкретного пользователя, продукта, услуги или системы удовлетворены.

Отличия от верификации:

   - верификация — проводится практически всегда, выполняется методом проверки (сличения) характеристик продукции с заданными требованиями, результатом является вывод о соответствии (или несоответствии) продукции,
   - валидация — проводится при необходимости, выполняется методом анализа заданных условий применения и оценки соответствия характеристик продукции этим требованиям, результатом является вывод о возможности применения продукции для конкретных условий.

Исходя из вышеописанного, валидация должна быть определена как подтверждение на основе объективных свидетельств того, что требования предопределены, а цель достигнута.

A simplified validation asks the questions: Does the system work as expected? How does the system respond to failures, faults, & anomalies? Is the system affordable? If the answer to any of these questions is no, then changes to the design or stakeholder expectations will be required, & the process is started over again.



## Верификация
> <small>**Верификация** — русскоязычный термин. **Verification** — англоязычный эквивалент.</small>

**Верификация** — *по [ГОСТ 56469](гост_56469.md)* — подтверждение с помощью объективных данных того факта, что заданные требования выполнены.

At least one method of verification have to be used. Verification methods:

   - **Testing.** Testing is a verification method using technical aids, such as special equipment, instruments, simulation methods & application of common principles & methonds to assess components, subsystems & systems for cimpliance to the requirements. Testing is a primary method of verification & is applied when analytical methods do not produce necessary results, when there are failures which may endanger the safety of personnel, have negative effect on in‑flight systems or payload functioning, or may endanger mission objectives.
   - **Analysis.** Verification by analysis applied together with or instead of other verification methods to confirm compliance to the specification requirements. The methods selected may include without limitation technical analysis, statistical & qualitative analysis, software & hardware simulation & analogue modeling. Analysis may be used when ➀ thorough & precise analys is possible, ➁ testing is unpractical due to costs, ➂ verification by inspection is insufficient.
   - **Design Review.** Design Review is a verification method where the verification is carried out by means of checking documented data or by demonstration of approved Basic Design documents or approved design reports, technical descriptions or drawings definitely supporting compliance to a requirement.
   - **Inspection.** During the Inspection principal attention is paid to examination of physical characteristics of the product to support compliance to the requirements to design elements, compliance to documentation & drawings, quality standards & physical conditions without application of special laboratory equipment, methods, testing instrumentation or services.



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](qa.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Test](test.md) •··**<br> [JTAG](jtag.md)┊ [Proto fligt model](pfm.md)┊ [Безэховая камера](ach.md)┊ [Валидация](val_ver.md)┊ [Класс чистоты](clean_lvl.md)┊ [КПЭО](ctpr.md)┊ [Перечень методик испытаний](list_tp.md)┊ [Программа и методика испытаний](pmot.md)┊ [Опытный образец](pilot_sample.md)┊ [Циклограмма](obc.md)┊ [Штатный образец](flight_unit.md)┊ [ЭО](test.md)┊ [Экспериментально‑теоретический метод](etetm.md)|
|**`Качество:`**<br> [Bus factor](bus_factor.md)┊ [АВПКО](fmeca.md)┊ [Авторский надзор](des_spv.md)┊ [Бережливое производство](lean_man.md)┊ [Валидация, верификация](val_ver.md)┊ [Класс чистоты](clean_lvl.md)┊ [Конструктивное совершенство](con_vel.md)┊ [Крит. технологии](kt.md)┊ [Крит. элементы](sens_elem.md)┊ [Метрология](metrology.md)┊ [Надёжность](qa.md)┊ [Нештатная ситуация](emergency.md)┊ [Ошибки](error.md)┊ [Система менеджмента качества](qms.md)┊ [УГТ](trl.md)/[TRL](trl.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Validation>
   1. <https://ru.wikipedia.org/wiki/Валидация>
