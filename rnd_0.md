# Научно‑исследовательская работа
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [R&D](rnd.md)

**Table of contents:**

[TOC]

---

|*Phase*| | |*Design*| | | | |*Mass prod.:*| |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|**[R&D phases](rnd.md)**|0 (pre‑A)|A|≈ B|≈ B|≈ C|≈ C/D|≈ E|…|F|
|**[НИОКР](rnd.md)**|[НИР](rnd_0.md)|[АП](rnd_ap.md)|[ЭП](rnd_ep.md)|[ТП](rnd_tp.md)|[РКД (РРД)](rnd_rkd.md)|[Макеты, НЭО](test.md)|[ЛИ](rnd_e.md)|ПСП → СП → ПЭ|Вывод|
| |*[NIR](rnd_0.md)*|*[AP](rnd_ap.md)*|*[EP](rnd_ep.md)*|*[TP](rnd_tp.md)*|*[RKD (RRD)](rnd_rkd.md)*|*[Models, Tests](test.md)*|*[LI](rnd_e.md)*|*PSP → SP → PE*|*Closeout*|

> <small>**Научно‑исследовательская работа (НИР)** — русскоязычный термин. **pre‑Phase A** — англоязычный эквивалент.</small>

**Научно‑исследовательская работа (НИР)** — комплекс теоретических и (или) экспериментальных исследований, проводимых с целью получения обоснованных исходных данных, изыскания принципов и путей создания (модернизации) продукции.

**Phase 0 (pre‑Phase A).** Concept studies.

| | |
|:-|:-|
|**Вх. данные**|・[ТЗ](tor.md)<br> ・[контракт](contract.md)<br> ・целевая программа с обоснованием состава НА и экспериментов<br> ・прочие [ИД](init_data.md) от Заказчика|
|**Вых. данные**|[НТО](report.md)|
|**Итог**|документы без присвоения литеры|
|**[НД](doc.md)**|・[РК‑11](const_rk.md), п.2.1<br> ・[ГОСТ 2.102](гост_2_102.md) «ЕСКД. Виды и комплектность КД»<br> ・[ГОСТ 2.103](гост_2_103.md) «ЕСКД. Стадии разработки»<br> ・[ГОСТ 2.105](гост_2_105.md) «ЕСКД. Общие требования к текстовым документам»<br> ・[ГОСТ 2.106](гост_2_106.md) «ЕСКД. Текстовые документы»<br> ・[ГОСТ 7.32](гост_7_32.md) «Отчёт о НИР. Структура и правила оформления»<br> ・[ГОСТ 15.203](гост_15_203.md) «Порядок выполнения ОКР»<br> ・[ГОСТ 15.208](гост_15_208.md) «Единый сквозной план»<br> ・[ГОСТ 51540](гост_51540.md) «Военная техника. Термины и определения»<br>Порядок выполнения, на выбор:<br> ・[ГОСТ 15.101](гост_15_101.md) «Порядок выполнения НИР и их СЧ»<br> ・[ГОСТ 15.105](гост_15_105.md) «СРПП ВТ. Порядок выполнения НИР и их СЧ»|
|**Процесс**|[формирование](dont_panic.md#Словоблудие) материалов в НТО на НИР|
|**[УЗК](cml.md)**|0 ‑ 4|



<p style="page-break-after:always"> </p>

## Phase 0, Pre-Phase A
During the Phase 0 the following logical components have to handled. The goal is to show for stakeholders that the proposed matter is worth doing.

Components have to be provided both with a short & simple description (for decision makers who may not be a specialist in the proposed area) and a long description that includes models, calculations, references (for specialists in this area in order to prove your ideas are viable).

   1. A description of why an exact matter (experiment, method, mission, spacecraft, unit, etc.) is important in terms of scientific, technical, etc. aspects, and what benefits it can provide.
   1. A description of the exact matter you would like to perform, including proof that it can be performed in the supposed conditions.
   1. A description of the exact matter you would like to install on a mother unit, including characteristics (see the table in a [unit description](unit.md); try to fill as much as possible) and proof that it can(’t) survive the supposed conditions.
   1. Any additional information you may find useful, e.g., but not limited to:
      - a roadmap, including supposed dates for key points, reviews and finish
      - cost estimation
      - cooperation, including proof of their readiness to work
      - key technologies
      - supposed [TRLs](trl.md)
      - your team



<p style="page-break-after:always"> </p>

## (RU) НИР

### Документация НИР
**Таблица.** Типовая комплектность документации

<small>

|*№*|*Наименование документа НИР на КК*|*Соглас.*|*Утвержд.*|*Примечание*|*Основание*|
|:-|:-|:-|:-|:-|:-|
|1|**[Заключение НТС Исполнителя](report.md)**|Исполнитель|Исполнитель| | |
|2|**[ИД](init_data.md) для разработки НИР**|По усмотрению Заказчика|Заказчик| | |
|3|**[Матрица соответствия](matrix_compl.md)**|Исполнитель|Исполнитель| | |
|4|**[НТО](report.md)**|Исполнитель|Исполнитель| | |
|5|**[План‑проспект выпуска НИР](plan.md)**|Исполнитель|Исполнитель|Он же «[План совместных работ](plan.md)». Объединён с графиком разработки.| |

</small>



<p style="page-break-after:always"> </p>

### Рабочий процесс
В начале [каждого этапа ОКР](rnd.md) должно быть:

   1. сформирована [рабочая группа](wg.md), из расчёта 2 сотрудника (1 исполнитель, 1 заместитель) от каждого участвующего в разработке этапа отдела (дирекции, комплекса);
   1. назначены [главный конструктор](mgmt.md), [главный технолог](mgmt.md), [менеджер по качеству](mgmt.md), [руководитель проекта](mgmt.md) (входят в рабочую группу); обычно на этапе НИР не назначаются.

</small>

До этапа «[Аванпроект (Техническое предложение)](rnd_ap.md)» должны быть проведены, как правило, научно‑исследовательские (в т.ч. системные, проектно‑поисковые) работы по:

   1. обоснованию целесообразности создания РК и КК (изделий комплексов);
   1. формированию технического облика (ТТТ) и правовой охраны создаваемых [РИД](intel_deliv.md);
   1. определению путей внедрения в конструкцию и схем КК (ПКК) новейших достижений науки и техники, новых технических решений;
   1. разработке:
      - новых материалов,
      - компонентов топлив,
      - прогрессивных технологий;
   1. созданию научно‑технического (технологического) задела;
   1. разработке и проверке:
      - типовых конструкторско‑технологических решений,
      - новых принципов и режимов функционирования изделий комплексов, включая научную аппаратуру и другие целевые системы и приборы;
   1. разработке и внедрению передовых технологий автоматизации проектирования и изготовления изделий комплекса, в т.ч. ИПИ‑технологий, охватывающих все этапы жизненного цикла изделия.

<mark>TBD</mark>



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:-|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·Событ., **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. <https://ru.wikipedia.org/wiki/Научно-исследовательская_работа>
