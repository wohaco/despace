# SysML
> 2021.02.04 [🚀](../index/index.md) [despace](index.md) → [SE](se.md), [Soft](soft.md)

[TOC]

---

> <small>**The Systems Modeling Language (SysML)** — EN term. **Язык моделирования систем** — RU analogue.</small>

The **Systems Modeling Language (SysML)** is a general‑purpose modeling language for systems engineering applications. It supports the specification, analysis, design, verification & validation of a broad range of systems & systems‑of‑systems.

SysML was originally developed by an open source specification project, & includes an open source license for distribution & use. SysML is defined as an extension of a subset of the Unified Modeling Language (UML) using UML’s profile mechanism. The language's extensions were designed to support systems engineering activities.


## Description

**Contrast with UML.**  
SysML offers systems engineers several noteworthy improvements over UML, which tends to be software‑centric. These improvements include the following:

   - SysML’s semantics are more flexible & expressive. SysML reduces UML’s software‑centric restrictions & adds two new diagram types, requirement & parametric diagrams. The former can be used for requirements engineering; the latter can be used for performance analysis & quantitative analysis. Consequent to these enhancements, SysML is able to model a wide range of systems, which may include hardware, software, information, processes, personnel, & facilities.
   - SysML is a comparatively small language that is easier to learn & apply. Since SysML removes many of UML’s software‑centric constructs, the overall language is smaller both in diagram types & total constructs.
   - SysML allocation tables support common kinds of allocations. Whereas UML provides only limited support for tabular notations, SysML furnishes flexible allocation tables that support requirements allocation, functional allocation, & structural allocation. This capability facilitates automated verification & validation (V&V) & gap analysis.
   - SysML model management constructs support models, views, & viewpoints. These constructs extend UML’s capabilities & are architecturally aligned with IEEE‑Std‑1471‑2000 (IEEE Recommended Practice for Architectural Description of Software Intensive Systems).

SysML reuses seven of UML 2’s fourteen diagrams, & adds two diagrams (requirement & parametric diagrams) for a total of nine diagram types. SysML also supports allocation tables, a tabular format that can be dynamically derived from SysML allocation relationships. A table which compares SysML & UML 2 diagrams is available in the SysML FAQ.  
Consider modeling an automotive system: with SysML one can use Requirement diagrams to efficiently capture functional, performance, & interface requirements, whereas with UML one is subject to the limitations of use case diagrams to define high‑level functional requirements. Likewise, with SysML one can use Parametric diagrams to precisely define performance & quantitative constraints like maximum acceleration, minimum curb weight, & total air conditioning capacity. UML provides no straightforward mechanism to capture this sort of essential performance & quantitative information.  
Concerning the rest of the automotive system, enhanced activity diagrams & state machine diagrams can be used to specify the embedded software control logic & information flows for the on‑board automotive computers. Other SysML structural & behavioral diagrams can be used to model factories that build the automobiles, as well as the interfaces between the organizations that work in the factories.

**History.**  
The SysML initiative originated in a January 2001 decision by the [International Council on Systems Engineering (INCOSE) ⎆](https://www.incose.org/) Model Driven Systems Design workgroup to customize the UML for systems engineering applications. Following this decision, INCOSE & the Object Management Group (OMG), which maintains the UML specification, jointly chartered the OMG Systems Engineering Domain Special Interest Group (SE DSIG) in July 2001. The SE DSIG, with support from INCOSE & the ISO AP 233 workgroup, developed the requirements for the modeling language, which were subsequently issued by the OMG parting in the UML for Systems Engineering Request for Proposal (UML for SE RFP; OMG document ad/03‑03‑41) in March 2003.  
In 2003 Cris Kobryn & Sanford Friedenthal organized & co‑chaired the SysML Partners, an informal association of industry leaders & tool vendors, which initiated an open source specification project to develop the SysML in response to the UML for Systems Engineering RFP. The original technical contributors & co‑authors of the SysML 1.0a specification were Laurent Balmelli, Conrad Bock, Rick Steiner, Alan Moore & Roger Burkhart. The SysML Partners distributed their first open source SysML specification drafts in 2004, & submitted SysML 1.0a to the OMG for technology adoption in November 2005.

**OMG SysML.**  
After a series of competing SysML specification proposals, a SysML Merge Team was proposed to the OMG in April 2006. This proposal was voted upon & adopted by the OMG in July 2006 as OMG SysML, to differentiate it from the original open source specification from which it was derived. Because OMG SysML is derived from open source SysML, it also includes an open source license for distribution & use.  
The OMG SysML v. 1.0 specification was issued by the OMG as an Available Specification in September 2007. The current version of OMG SysML is v1.6, which was issued by the OMG in December 2019. In addition, SysML was published by the International Organization for Standardization (ISO) in 2017 as a full International Standard (IS), ISO/IEC 19514:2017 (Information technology — Object management group systems modeling language).  
The OMG has been working on the next generation of SysML & issued a Request for Proposals (RFP) for version 2 on December 8, 2017, following its open standardization process. The resulting specification, which will incorporate language enhancements from experience applying the language, will include a UML profile, a metamodel, & a mapping between the profile & metamodel. A second RFP for a SysML v2 Application Programming Interface (API) & Services RFP was issued in June 2018. Its aim is to enhance the interoperability of model‑based systems engineering tools.


## Diagrams

SysML includes 9 types of diagram, some of which are taken from UML.

   1. Activity diagram
   1. Block definition diagram
   1. Internal block diagram
   1. Package diagram
   1. Parametric diagram
   1. Requirement Diagram
   1. State machine diagram
   1. Sequence diagram
   1. Use case diagram


### Activity diagram
**Activity diagrams** are graphical representations of workflows of stepwise activities & actions with support for choice, iteration & concurrency. In the Unified Modeling Language, activity diagrams are intended to model both computational & organizational processes (i.e., workflows), as well as the data flows intersecting with the related activities. Although activity diagrams primarily show the overall flow of control, they can also include elements showing the flow of data between activities through one or more data stores.

**Construction.**  
Activity diagrams are constructed from a limited number of shapes, connected with arrows. The most important shape types:

   - ellipses represent actions;
   - diamonds represent decisions;
   - bars represent the start (split) or end (join) of concurrent activities;
   - a black circle represents the start (initial node) of the workflow;
   - an encircled black circle represents the end (final node).

Arrows run from the start towards the end & represent the order in which activities happen.  
Activity diagrams can be regarded as a form of a structured flowchart combined with a traditional data flow diagram. Typical flowchart techniques lack constructs for expressing concurrency. However, the join & split symbols in activity diagrams only resolve this for simple cases; the meaning of the model is not clear when they are arbitrarily combined with decisions or loops.  
While in UML 1.x, activity diagrams were a specialized form of state diagrams, in UML 2.x, the activity diagrams were reformalized to be based on Petri net‑like semantics, increasing the scope of situations that can be modeled using activity diagrams. These changes cause many UML 1.x activity diagrams to be interpreted differently in UML 2.x.  
UML activity diagrams in version 2.x can be used in various domains, e.g. in design of embedded systems. It is possible to verify such a specification using model checking technique.

![](f/se/sysml_act_dia.png)


### Package diagram
A **package diagram** in the Unified Modeling Language depicts the dependencies between the packages that make up a model.

**Overview.**  
In addition to the standard UML Dependency relationship, there are two special types of dependencies defined between packages:

   - package import
   - package merge

A package import is “a relationship between an importing namespace & a package, indicating that the importing namespace adds the names of the members of the package to its own namespace”. By default, an unlabeled dependency between two packages is interpreted as a package import relationship. In this relationship, elements within the target package will be imported into the source package.  
A package merge is “a directed relationship between two packages, that indicates that the contents of the two packages are to be combined. It is very similar to Generalisation in the sense that the source element conceptually adds the characteristics of the target element to its own characteristics resulting in an element that combines the characteristics of both” In this relationship, if an element exists within both the source package & the target package, then the source element’s definition will be expanded to include the target element’s definition.

**Elements**

   1. Package: a general purpose mechanism for organising model elements & diagrams into groups. It provides an encapsulated namespace within which all the names must be unique. It is used to group semantically related elements. It is a namespace as well as an element that can be contained in other packages’ namespaces.
   1. Class: a representation of an object that reflects its structure & behavior within the system. It is a template from which running instances are created. Classes usually describe the logical structure of the system.
   1. Interface: a specification of behavior. An implementation class must be written to support the behavior of an interface class.
   1. Object: an instance of a class. It is often used in analysis to represent an artifact or other item.
   1. Table: a stereotyped class.

**Usage.**  
Package diagrams can use packages containing use cases to illustrate the functionality of a software system.  
Package diagrams can use packages that represent the different layers of a software system to illustrate the layered architecture of a software system. The dependencies between these packages can be adorned with labels / stereotypes to indicate the communication mechanism between the layers.

**When To Use**

   1. It is used in large scale systems to picture dependencies between major elements in the system
   1. Package diagrams represent a compile time grouping mechanism.

![](f/se/sysml_pac_dia.png)


### Requirement diagram
A **requirement diagram** is a diagram specially used in SysML in which requirements & the relations between them & their relationship to other model elements are shown as discussed in the following paragraphs.

   - **Derive requirement relationship.** If a requirement is derived from another requirement, their relation is named “derive requirement relationship”.
   - **Namespace containment.** If a requirement is contained in another requirement, their relation is named “namespace containment”.
   - **Satisfy relationship.** If a requirement is satisfied by a design element, their relation is named “satisfy relationship”.
   - **Copy relationship.** If a requirement is a copy of another requirement, their relation is named “copy relationship”.
   - **Verify relationship.** If there exists a relation between a requirement & a test case verifying this requirement, their relation is named “verify relationship”.
   - **Test case.** A test case is defined by a flow checking whether the system under consideration satisfies a requirement.
   - **Refine relationship.** If a requirement is refined by other requirements / model elements, the relation is named “refine relationship”.
   - **Trace relationship.** If there exists a relation between a requirement & an arbitrary model element traced by this requirement, their relation is named “trace relationship”.


### Sequence diagram
A **sequence diagram** shows object interactions arranged in time sequence. It depicts the objects involved in the scenario & the sequence of messages exchanged between the objects needed to carry out the functionality of the scenario. Sequence diagrams are typically associated with use case realizations in the Logical View of the system under development. Sequence diagrams are sometimes called event diagrams or event scenarios.  
A sequence diagram shows, as parallel vertical lines (lifelines), different processes or objects that live simultaneously, and, as horizontal arrows, the messages exchanged between them, in the order in which they occur. This allows the specification of simple runtime scenarios in a graphical manner.

**Diagram building blocks.**  
If the lifeline is that of an object, it demonstrates a role. Leaving the instance name blank can represent anonymous & unnamed instances.  
Messages, written with horizontal arrows with the message name written above them, display interaction. Solid arrow heads represent synchronous calls, open arrow heads represent asynchronous messages, & dashed lines represent reply messages. If a caller sends a synchronous message, it must wait until the message is done, such as invoking a subroutine. If a caller sends an asynchronous message, it can continue processing & doesn’t have to wait for a response. Asynchronous calls are present in multithreaded applications, event‑driven applications & in message‑oriented middleware. Activation boxes, or method‑call boxes, are opaque rectangles drawn on top of lifelines to represent that processes are being performed in response to the message (ExecutionSpecifications in UML).  
Objects calling methods on themselves use messages & add new activation boxes on top of any others to indicate a further level of processing. If an object is destroyed (removed from memory), an X is drawn on bottom of the lifeline, & the dashed line ceases to be drawn below it. It should be the result of a message, either from the object itself, or another.  
A message sent from outside the diagram can be represented by a message originating from a filled‑in circle (found message in UML) or from a border of the sequence diagram (gate in UML).  
UML has introduced significant improvements to the capabilities of sequence diagrams. Most of these improvements are based on the idea of interaction fragments which represent smaller pieces of an enclosing interaction. Multiple interaction fragments are combined to create a variety of combined fragments, which are then used to model interactions that include parallelism, conditional branches, optional interactions.

![](f/se/sysml_seq_dia.png)


### State diagram

A **state diagram** is a type of diagram used in computer science & related fields to describe the behavior of systems. State diagrams require that the system described is composed of a finite number of states; sometimes, this is indeed the case, while at other times this is a reasonable abstraction. Many forms of state diagrams exist, which differ slightly & have different semantics.

State diagrams are used to give an abstract description of the behavior of a system. This behavior is analyzed & represented by a series of events that can occur in one or more possible states. Hereby “each diagram usually represents objects of a single class & track the different states of its objects through the system”.

State diagrams can be used to graphically represent finite‑state machines (also called finite automata). This was introduced by Claude Shannon & Warren Weaver in their 1949 book The Mathematical Theory of Communication. Another source is Taylor Booth in his 1967 book Sequential Machines & Automata Theory. Another possible representation is the state‑transition table.

![](f/se/sysml_sta_dia.png)


### Use case diagram
A **use case diagram** at its simplest is a representation of a user’s interaction with the system that shows the relationship between the user & the different use cases in which the user is involved. A use case diagram can identify the different types of users of a system & the different use cases & will often be accompanied by other types of diagrams as well. The use cases are represented by either circles or ellipses.

**Application.**  
While a use case itself might drill into a lot of detail about every possibility, a use‑case diagram can help provide a higher‑level view of the system. It has been said before that “Use case diagrams are the blueprints for your system”.  
Due to their simplistic nature, use case diagrams can be a good communication tool for stakeholders. The drawings attempt to mimic the real world & provide a view for the stakeholder to understand how the system is going to be designed. Siau & Lee conducted research to determine if there was a valid situation for use case diagrams at all or if they were unnecessary. What was found was that the use case diagrams conveyed the intent of the system in a more simplified manner to stakeholders & that they were “interpreted more completely than class diagrams”.  
The purpose of use case diagram is to capture the dynamic aspect of a system. Additional diagrams & documentation can be used to provide a complete functional & technical view of the system.They provide the simplified & graphical representation of what the system must actually do.

![](f/se/sysml_uca_dia.png)



## (RU) SysML
**SysML** (англ. The Systems Modeling Language, язык моделирования систем) — предметно‑ориентированный язык моделирования систем. Поддерживает определение, анализ, проектирование, проверку и подтверждение соответствия широкого спектра систем. SysML изначально разрабатывался в рамках проекта спецификации с открытым исходным кодом, и имеет открытую лицензию для распространения и использования. Как язык, SysML является расширением части языка UML. По сравнению с UML, ориентированным на моделирование программных продуктов, SysML предоставляет системному инженеру дополнительные возможности:

   - Большая гибкость и выразительность. SysML убирает программно‑ориентированные ограничения UML за счёт введения двух дополнительных типов диаграмм: диаграммы требований и параметрической диаграммы. Первая, очевидно, служит для сбора требований, а вторая для количественного анализа и анализа производительности. В результате становится возможным моделирование широкого спектра систем, которые могут включать оборудование, ПО, информацию, процессы, персонал и площади.
   - SysML более компактный язык, его легче изучать и применять, так как он избавлен от многих программно‑ориентированных особенностей UML.
   - Конструкции языка для управления моделью поддерживают модели, представления (англ. views), и точки зрения (англ. viewpoints) (используются для создания представлений). Эти конструкции расширяют возможности UML и архитектурно стоят в одном ряду с IEEE‑Std‑1471‑2000 (Рекомендованная IEEE практика для архитектурного описания программно‑нагруженных систем) англ. (IEEE Recommended Practice for Architectural Description of Software Intensive Systems).

**UML** (англ. Unified Modeling Language — унифицированный язык моделирования) — язык графического описания для объектного моделирования в области разработки программного обеспечения, для моделирования бизнес‑процессов, системного проектирования и отображения организационных структур. UML является языком широкого профиля, это — открытый стандарт, использующий графические обозначения для создания абстрактной модели системы, называемой UML‑моделью. UML был создан для определения, визуализации, проектирования и документирования, в основном, программных систем. UML не является языком программирования, но на основании UML‑моделей возможна генерация кода.



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**【[Systems engineering](se.md)】**<br> [Competence](competence.md)・ [Coordinate system](coord_sys.md)・ [Designer’s supervision](des_spv.md)・ [Industrial archaeology](ind_arch.md)・ [Instruction](instruction.md)・ [Lean manuf.](lean_man.md)・ [Lifetime](lifetime.md)・ [MBSE](mbse.md)・ [MML](mml.md)・ [Nav. & ballistics (NB)](nnb.md)・ [NASA SEH](nasa_seh.md)・ [Oberth effect](oberth_eff.md)・ [PMBok](pmbok.md)・ [Quorum](quorum.md)・ [R&D management](mgmt.md)・ [R&D support](rnd_support.md)・ [Recursion](recurs.md)・ [Schulze_method](schulze_method.md)・ [Sci'N'Tech activities](st_act.md)・ [Sci'N'Tech council](satc.md)・ [Skunk works](skunk_works.md)・ [SysML](sysml.md)・ [Tennis racket theorem](tr_theorem.md)・ [TRIZ](triz.md)・ [TRL](trl.md)・ [V‑model](v_model.md)・ [Workflow](workflow.md)・ [Workgroup](wg.md)|
|**【[Software](soft.md)】**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](c.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [PDF](pdf.md)・ [Python](python.md)・ [R](r.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](systems_tool_kit.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs: [System Modelling Language explained ❐](f/se/sysml_explained_finance.pdf)
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Systems_Modeling_Language>
   1. <http://www.sysml.org/> — Открытые спецификации SysML, ЧаВО, списки рассылки, и открытые лицензии
   1. <http://www.omgsysml.org/> — Спецификации OMG SysML, учебные пособия по SysML, статьи, и информацию о поставщиках инструментария
   1. <http://www.softwarestencils.com/sysml/index.html> — SysML 1.0 образцы и шаблоны для MS Visio
