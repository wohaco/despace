# MBSE
> 2021.02.04 [🚀](../index/index.md) [despace](index.md) → [Control](control.md), [SE](se.md)

[TOC]

---

> <small>**Model‑based systems engineering (MBSE)** — EN term. **Системное Проектирование На Основе Моделей (МБСЕ)** — RU analogue.</small>

**Model‑based systems engineering (MBSE)** is a systems engineering methodology that focuses on creating and exploiting domain models as the primary means of information exchange between engineers, rather than on document‑based information exchange.

**History.**  
In January 2007, the MBSE approach began to be popularized when the [INCOSE ⎆](https://www.incose.org/) introduced its [MBSE Initiative ⎆](http://www.omgwiki.org/MBSE/). Goals included increased productivity, by minimizing unnecessary manual transcription of concepts when coordinating the work of large teams. The MBSE approach is outlined in INCOSE’s “MBSE 2020 Vision”, with a methodology focusing on distributed but integrated model management.  
As of 2014, the focus has also started to cover aspects related to the model execution in computer simulation experiment, to further overcome the gap between the system model specification and the respective simulation software. As a consequence, the term **modeling and simulation‑based systems engineering (M&SBSE)** has also been used along with MBSE.


## NASA MBSE

INCOSE defines MBSE as “Model‑based systems engineering (MBSE) is the formalized application of modeling to support system requirements, design, analysis, verification and validation activities beginning in the conceptual design phase and continuing throughout development and later life cycle phases.” In practice, System Markup Language (SysML) based models have gained the most prevelance in MBSE application. These models are system relationship models and are useful for showing relationships among system functions, requirements, developers, and users. These models support 3 aspects of systems engineering:

   - System Functional Flows (i.e., System Architecture)
   - System Requirements Traceability
   - System and Organizational Process Flows

There are several organizations that have been working to advance the SysML modeling capabilities and applications. These include the INCOSE MBSE Initiative and the NASA MBSE Pathfinder.  The INCOSE MBSE Initiative is looking at a broad list of topics in the application of MBSE.  The application of Hamilton’s Principle to the definition of patterns by the Pattern Based Working Group is of particular interest to the development of system models.  The NASA MBSE Pathfinder is demonstrating application of MBSE in space related systems. Links to the INCOSE MBSE Initiative and the NASA MBSE Community of Practice, which also hosts the MBSE Pathfinder page, are included below.



## (RU) MBSE
**Системная инженерия (проектирование) на основе моделей** (**MBSE, model based systems engineering**) — является формализованным применением моделирования для обеспечения действий по удовлетворению требований, проектированию, анализу, верификации и валидации в течении всех фаз жизненного цикла проектируемой системы.

**MBSE** — методология, рассматривающая развитие различных взаимосвязанных моделей, которые используются для определения и разработки конечной системы. Модели предлагают эффективный способ изучения, обновления аспектов системы и предоставления информации о них заинтересованным сторонам, при этом значительно сокращая или устраняя зависимость от необходимости использования традиционной документации.

Ключевая характеристика MBSE — это поддержка одновременного использования множества методов описания (viewpoints), т.е. одновременного применения множества методов моделирования для получения множества групп описаний (views), которые адресуют различные интересы соответствующих заинтересованных лиц. MBSE заканчивается в тот момент, когда вам удалось объединить все имеющиеся модели и софт солверов: вы можете определить вашу систему и по результатам моделирования понять, как она себя поведёт в тех или иных условиях.

**Цели MBSE:**

   1. улучшить коммуникацию стейкхолдеров
   1. улучшить точность спецификации требований и дизайна
   1. обеспечить интеграцию компонентов системы
   1. предоставить возможность повторного использования артефактов дизайна системы
   1. результатом MBSE является модель системы

**Процесс MBSE:**

   - Выявление и анализ интересов стейкхолдеров для формулировки проблем и целей системы, а также критериев (метрики) оценки эффективности и качества;
   - Определение границ системы (system boundary), разграничение внутренних и внешних связей системы;
   - Спецификация функциональности системы. Определение интерфейсов, физических и качественных характеристик, обеспечивающих достижение целей;
   - Синтез альтернативных решений путем деления системы на компоненты, соответствующие требованиям к системе (декомпозиция);
   - Анализ трудоемкости для оценки и выбора предпочтительных решений, удовлетворяющих требованиям и обеспечивающих оптимальный баланс для значений метрик эффективности и качества;
   - Обеспечение контроля за выполнением требований к компонентам и достижением целей системы для удовлетворения всех стейкхолдеров.

**Стандарты MBSE**

|*Раздел*|*Стандарт*|
|:--|:--|
|Процессные стандарты|• EIA 632: Processes for Engineering a System;<br> • ISO 15288: Systems and software engineering — System life cycle processes;<br> • IEEE 1220: Standard for Application and Management of the Systems Engineering Process;<br> • CMMI (Capability Maturity Model Integration)|
|Архитектурные методологии<br> (frameworks)|• FEAF (Federal Enterprise Architecture Framework);<br> • DoDAF (The Department of Defense Architecture Framework );<br> • MODAF (The British Ministry of Defence Architecture Framework);<br> • PPOA (Fernandez Process Pipelines in Object oriented Architectures);<br> • ZF (Zachman Framework)|
|Методы моделирования|• HP;<br> • OOSE (Object‑oriented software engineering) — прародитель UML;<br> • OOSEM (Object‑Oriented Systems Engineering Method);<br> • SADT;<br> • прочие|
|Стандарты моделирования<br> и симуляции|*Системное моделирование:*<br> • IDEF0;<br> • [SysML](sysml.md);<br> • UPDM;<br> *Симуляция и анализ:*;<br> • Modelica;<br> • HLA;<br> • MathML|
|Стандарты обмена<br> и метамоделирования|• MOF;<br> • QVT;<br> • XMI;<br> • [STEP/AP 233](cad_f.md)|

**Методологии MBSE**

   - IBM Telelogic Harmony‑SE
   - IBM Rational Unified Process‑Systems Engineering (RUP‑SE) for Model‑Driven System Design (MDSD)
   - Vitech MBSE (STRATA)
   - Jet Propulsion Laboratory's State Analysis (JPL SA)
   - Object Process Methodology (OPM)
   - Weiliens Systems Modeling Process (SYSMOD)
   - An Ontology for State Analysis Formalizing the Mapping to SysML
   - SysML JumpStart Training with Enterprise Architect
   - MBSE Framework for Concept Development
   - и многие другие



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SRRQ](srrq.md)**·БКНР, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Control](Control.md) •··**<br> [Ad hoc](ad_hoc.md) ┊ [Business travel](business_travel.md) ┊ [Chief designers council](cocd.md) ┊ [CML](cml.md) ┊ [Competence](competence.md) ┊ [Confident](confident.md) ┊ [Consp.theory](consp_theory.md) ┊ [Control sys. (CS)](cs.md) ┊ [Coordinate system](coord_sys.md) ┊ [Curator](curator.md) ┊ [Designer’s supervision](des_spv.md) ┊ [E‑sig](esig.md) ┊ [Engineer](se.md) ┊ [Errand](errand.md) ┊ [Federal law](fed_law.md) ┊ [Federal TP](fed_tp.md) ┊ [Federal SP](fed_sp.md) ┊ [GNC](gnc.md) ┊ [Gravity assist](gravass.md) ┊ [Industrial archaeology](ind_arch.md) ┊ [Instruction](instruction.md) ┊ [Lean manuf.](lean_man.md) ┊ [Lifetime](lifetime.md) ┊ [Manager](manager.md) ┊ [MBSE](mbse.md) ┊ [Meeting](meeting.md) ┊ [MCC](mcc.md) ┊ [MIC](mic.md) ┊ [MML](mml.md) ┊ [MoU](mou.md) ┊ [Nav. & ballistics (NB)](nnb.md) ┊ [Nonprofit org.](nonprof_org.md) ┊ [NX](nx.md) ┊ [Oberth effect](oberth_eff.md) ┊ [Org.structure](orgstruct.md) ┊ [Outcomes commission](outccom.md) ┊ [Patent](patent_res.md) ┊ [Peter prin.](peter_principle.md) ┊ [Plan](plan.md) ┊ [PMBok](pmbok.md) ┊ [Quorum](quorum.md) ┊ [R&D management](mgmt.md) ┊ [R&D support](rnd_support.md) ┊ [Recursion](recurs.md) ┊ [Schulze_method](schulze_method.md) ┊ [Sci'N'Tech activities](st_act.md) ┊ [Sci'N'Tech council](satc.md) ┊ [Single-window system](sw_sys.md) ┊ [Situ.leadership](situ_leadership.md) ┊ [Skunk works](skunk_works.md) ┊ [State arm. plan](plan_sa.md) ┊ [Swamp](swamp.md) ┊ [Teamcenter](teamcenter.md) ┊ [Tennis racket theorem](tr_theorem.md) ┊ [TRIZ](triz.md) ┊ [TRL](trl.md) ┊ [V‑model](v_model.md) ┊ [Veto](veto.md) ┊ [Workflow](workflow.md) ┊ [Workgroup](wg.md)|
|**··• [Systems engineering](se.md) •··**<br> [Competence](competence.md) ┊ [Coordinate system](coord_sys.md) ┊ [Designer’s supervision](des_spv.md) ┊ [Industrial archaeology](ind_arch.md) ┊ [Instruction](instruction.md) ┊ [Lean manuf.](lean_man.md) ┊ [Lifetime](lifetime.md) ┊ [MBSE](mbse.md) ┊ [MML](mml.md) ┊ [Nav. & ballistics (NB)](nnb.md) ┊ [NASA SEH](nasa_seh.md) ┊ [Oberth effect](oberth_eff.md) ┊ [PMBok](pmbok.md) ┊ [Quorum](quorum.md) ┊ [R&D management](mgmt.md) ┊ [R&D support](rnd_support.md) ┊ [Recursion](recurs.md) ┊ [Schulze_method](schulze_method.md) ┊ [Sci'N'Tech activities](st_act.md) ┊ [Sci'N'Tech council](satc.md) ┊ [Skunk works](skunk_works.md) ┊ [SysML](sysml.md) ┊ [Tennis racket theorem](tr_theorem.md) ┊ [TRIZ](triz.md) ┊ [TRL](trl.md) ┊ [V‑model](v_model.md) ┊ [Workflow](workflow.md) ┊ [Workgroup](wg.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Model-based_systems_engineering>
   1. <http://sewiki.ru/MBSE>
   1. <http://www.omgwiki.org/MBSE/>
   1. <https://www.incose.org/incose-member-resources/working-groups/transformational/mbse-initiative>
   1. <https://www.nasa.gov/consortium/ModelBasedSystems>
