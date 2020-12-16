# Interface
> 2020.11.18 [🚀](../index/index.md) [despace](index.md) → [Doc](doc.md), [SC](sc.md)

[TOC]

---

> <small>**Interface** — EN term. **Интерфейс** — RU analogue.</small>

An **interface** is a shared boundary across which two or more separate components exchange information. The exchange can be between software, computer hardware, peripheral devices, humans, etc. Interfaces can provide both input and output, or just one of them.

Spacecraft interfaces are combining [external factors](ef.md), budgets, speeds, and include:

   1. **Overall description:**
      - Reliability,
      - [Standards](doc.md),
      - Timeline of tests & functioning.
   1. **Electrical & electromagnetic**
      - **Environment:**
         1. [Electromagnetic interference (EMI), & Radio frequency interference](eni.md),
         1. [Magnetic fields](mag_field.md),
         1. Magnetic materials,
         1. Radiated emissions,
         1. Radiated susceptibility.
      - **Interfaces:**
         1. Commands & Data budgets,
         1. [Communications](comms.md),
         1. Connectors,
         1. Exchange protocols,
         1. Fields & Points of view,
         1. Metallization,
         1. [Power](sps.md) & Consumption timeline,
         1. [Voltage](voltage.md).
   1. **Mechanical**
      - **Environment:**
         1. Acoustic,
         1. [Meteorites](aob.md), Dust, & Liquids,
         1. Quasi‑static loads,
         1. Random loads,
         1. Shock events,
         1. Sine vibration.
      - **Interfaces:** (incl. their evolutions)
         1. Accuracy,
         1. Connectors,
         1. Deployment & Moving parts,
         1. [Dimensions](draft_model.md),
         1. Fields & Points of view,
         1. Hydraulic characteristics: location, evolution, connectors,
         1. Mass allocation & Center on mass,
         1. [Materials](sgm.md) & their [emission](mat_sublime.md),
         1. Mounting points,
         1. Orientation,
         1. Oscillator circuit,
         1. Pressurization level.
   1. **[Radiation](ion_rad.md):** (incl. [cosmic rays](cr.md))
      - **Environment:**
         1. Non‑ionising displacement damage dose (DDD),
         1. Non‑ionising linear energy transfer (LET),
         1. Total ionising dose (TID).
      - **Interfaces:**
         1. Protection.
   1. **[Thermal](tcs.md):**
      - **Environment:**
         1. Atmosphere & its Temperature ranges & timeline,
         1. Solar & Surrounding bodies [thermal radiation, illumination](illum.md), & placement.
      - **Interfaces:**
         1. Heaters, covers & their mounting points, optical characteristics, radiators,
         1. Temperature ranges,
         1. Thermal emission,
         1. Thermal lines, Exchange spots, & Exchange protocols,
         1. Thermal resistance.

List of common documents:

   - **ICD** — interface control document
   - **IRD** — interface requirements document



## ICD
> <small>**Interface control document (ICD)** — EN term. **Документ контроля интерфейсов** — RU analogue.</small>

An **interface control document (ICD)** in systems engineering & software engineering, provides a record of all interface information (drawings, diagrams, tables, & text) generated for a project. The underlying interface documents provide the details & describe the interface(s) between subsystems or to a system or subsystem.

ICDs are a key element of systems engineering as they control the documented interface(s) of a system, as well as specify a set of interface versions that work together, & thereby bound the requirements. The purpose is to control & maintain a record of system interface information. This includes all possible inputs to & all potential outputs from a system for some potential or actual user of the system. The internal interfaces of a system or subsystem are documented in their respective interface requirements specifications, while human‑machine interfaces might be in a system design document (such as a software design document).

An ICD is the umbrella document over the system interfaces; examples of what these interface specifications should describe include:

   - The inputs & outputs of a single system, documented in individual SIRS & HIRS documents, would fall under “The Wikipedia Interface Control Document”.
   - The interface between two systems or subsystems, e.g. “The Doghouse to Outhouse Interface” would also have a parent ICD.
   - The complete interface protocol from the lowest physical elements (e.g., the mating plugs, the electrical signal voltage levels) to the highest logical levels (e.g., the level 7 application layer of the OSI model) would each be documented in the appropriate interface requirements spec & fall under a single ICD for the “system”.

An application programming interface is a form of interface for a software system, in that it describes how to access the functions & services provided by a system via an interface. If a system producer wants others to be able to use the system, an ICD & interface specs (or their equivalent) is a worthwhile investment.

An ICD should only describe the detailed interface documentation itself, & not the characteristics of the systems which use it to connect. The function & logic of those systems should be described in their own requirements & design documents as needed (there are DIDs for all of these). In this way, independent teams can develop the connecting systems which use the interface specified, without regard to how other systems will react to data & signals which are sent over the interface. For example, the ICD & associated interface documentation must include information about the size, format, & what is measured by the data, but not any ultimate meaning of the data in its intended use by any user.

An adequately defined interface will allow one team to test its implementation of the interface by simulating the opposing side with a simple communications simulator. Not knowing the business logic of the system on the far side of an interface makes it more likely that one will develop a system that does not break when the other system changes its business rules & logic. (Provision for limits or sanity checking should be pointedly avoided in an interface requirements specification.) Thus, good modularity & abstraction leading to easy maintenance & extensibility are achieved.

**Criticism:**

   - Critics of requirements documentation & systems engineering in general often complain of the over‑emphasis on documentation. ICDs are often present on document‑driven projects, but may be useful on agile projects as well (although not explicitly named as such). An ICD need not be a textual document. It may be an (evolving) table of goes‑intos & comes‑out‑ofs, a dynamic database representing each subsystem as a DB view, a set of interaction diagrams, etc.
   - ICDs are often used where subsystems are developed asynchronously in time, since they provide a structured way to communicate information about subsystems interfaces between different subsystem design teams.



## IRD
> <small>**Interface requirements document (IRD)** — EN term. **Документ требований к интерфейсам** — RU analogue.</small>

<mark>TBD</mark>

Interface Requirements Document Outline (according to [NASA Systems Engineering Handbook, App. L](https://www.nasa.gov/seh/appendix-l-interface-requirements-document-outline))

   1. Introduction
      - 1.1 Purpose and Scope. State the purpose of this document and briefly identify the interface to be defined. (For example, “This IRD defines and controls the interface(s) requirements between ______ and ______.”)
      - 1.2 Precedence. Define the relationship of this document to other program documents and specify which is controlling in the event of a conflict.
      - 1.3 Responsibility and Change Authority. State the responsibilities of the interfacing organizations for development of this document and its contents. Define document approval authority (including change approval authority).
   2. Documents
      - 2.1 Applicable Documents. List binding documents that are invoked to the extent specified in this IRD. The latest revision or most recent version should be listed. Documents and requirements imposed by higher-level documents (higher order of precedence) should not be repeated.
      - 2.2 Reference Documents. List any document that is referenced in the text in this subsection.
   3. Interfaces
      - 3.1 General. In the subsections that follow, provide the detailed description, responsibilities, coordinate systems, and numerical requirements as they relate to the interface plane.
         - 3.1.1 Interface Description. Describe the interface as defined in the system specification. Use tables, figures, or drawings as appropriate.
         - 3.1.2 Interface Responsibilities. Define interface hardware and interface boundary responsibilities to depict the interface plane. Use tables, figures, or drawings as appropriate.
         - 3.1.3 Coordinate Systems. Define the coordinate system used for interface requirements on each side of the interface. Use tables, figures, or drawings as appropriate.
         - 3.1.4 Engineering Units, Tolerances, and Conversion. Define the measurement units along with tolerances. If required, define the conversion between measurement systems.
      - 3.2 Interface Requirements. In the subsections that follow, define structural limiting values at the interface, such as interface loads, forcing functions, and dynamic conditions. Define the interface requirements on each side of the interface plane.
         - 3.2.1 Mass Properties. Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover the mass of the element.
         - 3.2.2 Structural/Mechanical. Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover attachment, stiffness, latching, and mechanisms.
         - 3.2.3 Fluid. Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover fluid areas such as thermal control, O2 and N2, potable and waste water, fuel cell water, and atmospheric sampling.
         - 3.2.4 Electrical (Power). Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover various electric current, voltage, wattage, and resistance levels.
         - 3.2.5 Electronic (Signal). Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover various signal types such as audio, video, command data handling, and navigation.
         - 3.2.6 Software and Data. Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, this subsection should cover various data standards, message timing, protocols, error detection/correction, functions, initialization, and status.
         - 3.2.7 Environments. Define the derived interface requirements based on the allocated requirements contained in the applicable specification pertaining to that side of the interface. For example, cover the dynamic envelope measures of the element in English units or the metric equivalent on this side of the interface.
            - 3.2.7.1 Electromagnetic Effects
               - 3.2.7.1.a Electromagnetic Compatibility. Define the appropriate electromagnetic compatibility requirements. For example, the end-item-1-to-end-item-2 interface shall meet the requirements [to be determined] of systems requirements for electromagnetic compatibility.
               - 3.2.7.1.b Electromagnetic Interference. Define the appropriate electromagnetic interference requirements. For example, the end-item-1-to-end-item-2 interface shall meet the requirements [to be determined] of electromagnetic emission and susceptibility requirements for electromagnetic compatibility.
               - 3.2.7.1.c Grounding. Define the appropriate grounding requirements. For example, the end-item-1-to-end-item-2 interface shall meet the requirements [to be determined] of grounding requirements.
               - 3.2.7.1.d Bonding. Define the appropriate bonding requirements. For example, the end-item-1-to-end-item-2 structural/mechanical interface shall meet the requirements [to be determined] of electrical bonding requirements.
               - 3.2.7.1.e Cable and Wire Design. Define the appropriate cable and wire design requirements. For example, the end-item-1-to-end-item-2 cable and wire interface shall meet the requirements [to be determined] of cable/wire design and control requirements for electromagnetic compatibility.
            - 3.2.7.2 Acoustic. Define the appropriate acoustics requirements. Define the acoustic noise levels on each side of the interface in accordance with program or project requirements.
            - 3.2.7.3 Structural Loads. Define the appropriate structural loads requirements. Define the mated loads that each end item should accommodate.
            - 3.2.7.4 Vibroacoustics. Define the appropriate vibroacoustics requirements. Define the vibroacoustic loads that each end item should accommodate.
            - 3.2.7.5 Human Operability. Define the appropriate human interface requirements. Define the human-centered design considerations, constraints, and capabilities that each end item should accommodate.
         - 3.2.8 Other Types of Interface Requirements. Define other types of unique interface requirements that may be applicable.




## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SRRQ](srrq.md)**·БКНР, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Documents](doc.md) •··**<br> **Схема:** [КСС](ксс.md) ┊ [ПГС](пгс.md) ┊ [ПЛИС](плис.md) ┊ [СхД](wbs.md) ┊ [СхО](draft_model.md) ┊ [СхПЗ](draft_model.md) ┊ [СхЧ](unit_decd.md) ┊ [СхЭ](ei_diagram.md)<br> [Interface](interface.md) ┊ [Mission proposal](proposal.md)|
|**··• [Spacecraft (SC)](sc.md) •··**<br> [Cleanliness level](clean_lvl.md) ┊ [Cubesat](sc.md) ┊ [Interface](interface.md) ┊ [Manned SC](sc.md) ┊ [Satellite](sc.md) ┊ [Sub-item](sui.md) ┊ [Typical forms](sc_ts.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Interface_(computing)>
   1. <https://en.wikipedia.org/wiki/Interface_control_document>
   1. <https://www.nasa.gov/seh/appendix-l-interface-requirements-document-outline>
