# Ведомость СЧ ОКР
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [Doc](doc.md), [НД](doc.md)

[TOC]

---

> <small>**Ведомость СЧ ОКР (ВСЧОКР)** — русскоязычный термин, не имеющий аналога в английском языке. **List of R&D systems and components (LORDSAC)** — дословный перевод с русского на английский.</small>

**Ведомость** — документ, включающий в себя перечень разработанной в результате аванпроекта (эскизного проекта, технического проекта) [конструкторской документации](doc.md).



## Описание

Выпускается в конце аванпроекта (ЭП, ТП). В отличие от [Перечня документации](list_doc.md) является результирующим документом, в то время как Перечень документации является планирующим документом. <small>([почему?:](dont_panic.md))</small>



## Разработка и согласование
[ГОСТ 15.203](гост_15_203.md) т.А.2 п.5.

|*[Этап](rnd.md)*|*Наименование документа*|*Разрабатывает*|*Согласует*|*Утверждает*|*Основание*|
|:--|:--|:--|:--|:--|:--|
|[НИР](rnd_0.md)|—|—|—|—|—|
|[АП](rnd_ap.md)|Ведомость АП|Исполнитель.|ГИ, ПЗ при ГИ.|Исполнитель, ПЗ при нём.| |
|[ЭП](rnd_ep.md)|Ведомость ЭП|Исполнитель.|ГИ, ПЗ при ГИ.|Исполнитель, ПЗ при нём.| |
|[ТП](rnd_tp.md)|Ведомость ТП|Исполнитель.|ГИ, ПЗ при ГИ.|Исполнитель, ПЗ при нём.| |
|[РКД](ркд.md)|—|—|—|—|—|
|[Макеты, НЭО](rnd_neo.md)|—|—|—|—|—|
|[ЛИ](rnd_e.md)|—|—|—|—|—|

**Типичные [конструкторские документы](doc.md), входящие в Ведомость на указанных выше этапах:**

   1. [пояснительная записка](report.md);
   1. [расчёты](calc.md);
   1. [схема деления](draft_model.md);
   1. [схема электрическая](draft_model.md);
   1. [схема подключений](draft_model.md);
   1. [чертежи](draft_model.md);
   1. [электронные модели](draft_model.md).



## Документация
   - [ГОСТ 2.102](гост_2_102.md)
   - [ГОСТ 2.106](гост_2_106.md) ЕСКД. Текстовые документы.
   - [ГОСТ 2.119](гост_2_119.md)



## Длинное описание
Ведомость АП, ЭП и ТП составляют на формах, представленные ниже.   В АП, ЭП и ТП записывают все [конструкторские документы](doc.md), вновь разработанные для данного АП, ЭП и ТП и примененные из других проектов и рабочей документации на ранее разработанные изделия. При этом записывают только те документы, которые являются необходимыми и достаточными для рассмотрения и утверждения данного проекта.

Запись документов в АП, ЭП и ТП производят по разделам в следующей последовательности:

   - документация общая;
   - документация по сборочным единицам.

Каждый **раздел** должен состоять из **подразделов**:

   - вновь разработанная;
   - примененная.

Наименования разделов и подразделов записывают в графе «Наименование» в виде заголовков. Наименования разделов подчеркивают.
   - В раздел *«Документация общая»*записывают документы, относящиеся к основному комплекту документов изделия.
   - В раздел *«Документация по сборочным единицам»* записывают документы, относящиеся к составным частям проектируемого изделия. При наличии в техническом проекте деталей их записывают после сборочных единиц. Перед перечислением деталей помещают заголовок *«Документация по деталям»*.
   - В подраздел *«Вновь разработанная»* записывают документы, разработанные для проектируемого изделия.
   - В подраздел *«Примененные»* записывают документы, примененные из других проектов и из рабочей документации других изделий. Документы технического предложения, эскизного и технического проектов комплектуют в папки, книги или альбомы.

Графы АП, ЭП, ТП заполняют следующим образом:

   - в графе «№ строки» указывают порядковый номер документа, включенного в ведомость;
   - в графе «формат» указывают формат, на котором выполнен документ. Если документ выполнен на нескольких листах различных форматов, то в графе проставляют «звездочку со скобкой», а в графе «Примечание» перечисляют все форматы в порядке их увеличения;
   - в графе «Обозначение» указывают обозначение документа;
   - в графе «Наименование» указывают:
   - в разделе «Документация общая» наименование документов, например: «Чертеж общего вида», «Габаритный чертеж», «Пояснительная записка»;
   - в разделе «Документация по сборочным единицам» — наименование изделия и документа в соответствии с основной надписью, например «Гидроцилиндр. Чертеж общего вида», «Пульт управления. Габаритный чертеж», «Механизм подачи. Схема электрическая принципиальная»;
   - в графе «Кол. листов» указывают количество листов, на которых выполнен данный документ. Для документов в электронной форме указывают количество листов копии на бумажном носителе, если копия используется при рассмотрении и утверждении АП, ЭП и ТП;
   - в графе «№ экз.» указывают номер экземпляра копии данного документа. При отсутствии номеров экземпляров графу прочеркивают;
   - в графе «Примечание» указывают дополнительные сведения. Для документов в электронной форме указывают идентификатор файла (файлов).

![](f/doc/vedomost-1.png) 

![](f/doc/vedomost-2.png)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [](.md) •··**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. Notable interwikies — …
   1. <…>
