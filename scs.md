# Spacecraft system
> 2019.05.05 [🚀](../index/index.md) [despace](index.md) → [SCS](scs.md)

[TOC]

---

> <small>**・ Spacecraft system (SCS)** — EN term. **Космический комплекс (КК)** — RU analogue.<br> **・ Многоразовая космическая система (МКС)** — русскоязычный термин. **Reusable space system** — англоязычный эквивалент.</small>

**Spacecraft system (SCS)** — combination of space & ground segments.

**Космический комплекс (КК)** — совокупность функционально взаимосвязанных орбитальных и наземных технических средств, обеспечивающих как самостоятельное решение целевых задач на основе использования космического пространства, так и в состав космической системы.

   - **Космическая система (КС)** — по [ГОСТ 53802](гост_53802.md) п. 1‑7 — совокупность одного или нескольких КК и специальных комплексов, предназначенных для решения целевых задач.
   - **Космическая система (КС)** — по [Положению РК‑11‑КТ](const_rk.md) стр. 17 — совокупность согласованно действующих и взаимосвязанных [КА](sc.md) и других технических средств КК и наземного специального комплекса, предназначенных для решения целевых задач. В состав КС могут входить несколько КК.
   - **Многоразовая космическая система (МКС)** — КС с орбитальными средствами многократного использования.



<p style="page-break-after:always"> </p>

## Description
Common dividing SCS into parts:

**Spacecraft system** (SCS)  
░║  
░╟ **Ground segment** (GS)  
░║  ╟ Ground networks  
░║  ╟ [Ground (or Earth) stations](scs.md)  
░║  ╟ Integration & test facilities  
░║  ╟ Launch facilities  
░║  ║  ╟ [Launch vehicle](lv.md)  
░║  ║  ╟ [Spaceport](spaceport.md)  
░║  ║  ╙ Transport & supporting facilities  
░║  ╟ [Mission (or flight) control (or operations) centers](scs.md) (MCC)  
░║  ╟ Remote terminals  
░║  ╙ [Search & rescue complex](sarc.md) (SARC)  
░║  
░╟ **User segment** (US)  
░║ ╙ Customer terminals  
░║  
░╙ **Space segment** (SS)  
░░░╙ **[Spacecraft](sc.md)** (SC) or **[Manned spacecraft](sc.md)** (MSC, ПКА)  
░░░░░╟ [Attitude control system](acs.md)  
░░░░░╟ [Command & Data Handling](c_n_dh.md) *(C&DH)*  
░░░░░║  ╟ [Data storage system](ds.md)  
░░░░░║  ╟ [Flight Software](soft.md)  
░░░░░║  ╟ [On-board computer](obc.md) *(OBC)*  
░░░░░║  ╙ [Telemetry system](obc.md) *(OBC)*  
░░░░░╟ [Communication system](comms.md)  
░░░░░║  ╟ Amplifiers  
░░░░░║  ╟ Antennas  
░░░░░║  ╙ Transmitters, receivers  
░░░░░╟ [Guidance, navigation, & control](gnc.md) *(GNC)*  
░░░░░╟ [Life support](ls.md)  
░░░░░╟ [Payload](sc.md) *(OE)*  
░░░░░╟ [Power system](sps.md) *(SPS)*  
░░░░░║  ╟ Automation & stabilization unit  
░░░░░║  ╟ [Cables](cable.md), connectors  
░░░░░║  ╟ Electroautomatics  
░░░░░║  ╟ Generator/converter  
░░░░░║  ╙ Storage device  
░░░░░╟ [Propulsion system](ps.md) *(PS)*  
░░░░░╟ [Structures, gears, materials, robotics](sc.md) *(SGM)*  
░░░░░║  ╟ Mounting gears, robotics, structures  
░░░░░║  ╟ On-board gears  
░░░░░║  ╟ On-board robotics  
░░░░░║  ╙ On-board structures  
░░░░░╙ [Thermal system](tcs.md) *(TCS)*

【TBD】

░░░░░░░░░╟ Бортовой комплекс управления (БКУ)  
░░░░░░░░░║  ╟ Высотомер  
░░░░░░░░░║  ╟ Гироскоп  
░░░░░░░░░║  ╟ Датчик звёздный (ЗД)  
░░░░░░░░░║  ╟ Датчик контроля электризации  
░░░░░░░░░║  ╟ Датчик относительной ориентации (GPS, GLONASS)  
░░░░░░░░░║  ╟ Датчик солнечный (СД)  
░░░░░░░░░║  ╟ Двигатель‑маховик (ДМ)  
░░░░░░░░░║  ╟ Запоминающее устройство (ЗУ)  
░░░░░░░░░║  ╟ Привод антенны  
░░░░░░░░░║  ╟ Привод солнечных панелей (ПСП)  
░░░░░░░░░║  ╟ Программное обеспечение (ПО)  
░░░░░░░░░║  ╙ Цифровая вычислительная машина (ЦВМ)  
░░░░░░░░░╟ Двигательная установка (ДУ)  
░░░░░░░░░║  ╟ Агрегаты  
░░░░░░░░░║  ╟ Баки  
░░░░░░░░░║  ╟ Двигатели  
░░░░░░░░░║  ╟ Защита, дренаж  
░░░░░░░░░║  ╟ Конструкция  
░░░░░░░░░║  ╟ Нагреватели, тепловые датчики  
░░░░░░░░░║  ╙ Трубопроводы  
░░░░░░░░░╟ Радиокомплекс (РК)  
░░░░░░░░░║  ╟ Антенно‑фидерная система (АФС)  
░░░░░░░░░║  ╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░║  ╙ Приёмо‑передатчик  
░░░░░░░░░╟ Система электроавтоматики (СЭА)  
░░░░░░░░░╟ Система электроснабжения (СЭС)  
░░░░░░░░░║  ╟ Аккумуляторная батарея (АБ)  
░░░░░░░░░║  ╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░║  ╟ Комплекс автоматики и стабилизации  
░░░░░░░░░║  ╙ Солнечные панели  

**And logics:**

   - [Communications](comms.md)
      1. Ground & onboard antennas
      1. [RF agreements](comms.md)
   - [Control](control.md)
      1. [Management](mgmt.md)
   - [Documents](doc.md), incl. major ones:
      1. [Drafts, models](drawing.md)
      1. [Report](report.md)
      1. [Terms of reference](tor.md) (TOR)
   - [Ecology](ecology.md)
   - [Electronic components](elc.md) (ElC)
   - [External factors](ef.md)
   - [Errors](error.md)
   - [Human factors & ergonomics](hfe.md) (HF&E)
   - [Interfaces](interface.md)
   - [International System of Units](si.md) (SI)
   - [Key technologies](kt.md) (KT)
   - [Model](drawing.md)
   - [Navigation & ballistics](nnb.md) (NB)
   - [Research & Development](rnd.md) (R&D)
   - [Safety, Reliability, Risk, Quality](qm.md) (SRRQ)
   - [Software](soft.md)
   - [Systems engineering](se.md)
   - [Tests](test.md)
   - [Timeline](timeline.md)
   - [TRL](trl.md) & [CML](cml.md)
   - **[Ecology](ecology.md)**·Экология
   - **[Ground station (GS)](scs.md)**·НС
   - **[Launch vehicle (LV)](lv.md)**·РН
   - **[Manned spacecraft (MSC)](sc.md)**·ПКА
   - **[Mission control center (MCC)](mcc.md)**·ЦУП
   - **[Search & rescue complex (SARC)](sarc.md)**·ПСК
   - **[Systems engineering (SE)](se.md)**·СЭ
   - **[Software](soft.md)**·ПО
   - **[Spaceport](spaceport.md)**·Космодром

   1. [Класс чистоты](clean_lvl.md);
   1. [Контейнеры для транспортировки](ship_contain.md);
   1. [О выводимых массах](throw_weight.md);



### Ground segment
A **ground segment (GS)** consists of all the ground‑based control elements of a spacecraft system, as opposed to the space segment & user segment. The GS serves to enable control of a spacecraft, & distribution of payload data & telemetry among interested parties on the ground.

The ground segment, though not technically part of the spacecraft, is vital to the operation of the spacecraft. Typical components of a GS in use during normal operations include a mission operations facility where the flight operations team conducts the operations of the spacecraft, a data processing & storage facility, ground stations to radiate signals to & receive signals from the spacecraft, & a voice & data communications network to connect all mission elements.

The **[launch vehicle](lv.md)** propels the spacecraft from Earth’s surface, through the atmosphere, & into an orbit, the exact orbit being dependent on the mission configuration. The launch vehicle may be expendable or reusable.

| | |
|:-|:-|
|**AE**|…|
|**AU**|…|
|**CA**|・[ADGA](contact/adga.md) — GS engineering (incl. software)<br> ・[BRASS](contact/brass.md) — satellite operations<br> ・[Calian AT](contact/calian_at.md) — Composite carbon fiber antenna, Comms systems, TT&C systems, Earth observation systems, Monitor & reconfiguration systems, Mission operations systems, Satellite gateway systems<br> ・[Honeywell Aerospace](contact/honeywell_as.md) — signal & data processing, flight & ground operations<br> ・[MDA](contact/mda.md)|
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





#### Mission control center (MCC)
> <small>**Mission control center (MCC), Launch control center (LCC)** — EN term. **Центр управления полётами (ЦУП)** — RU analogue.</small>

A **mission control center** (**MCC**, sometimes called a **flight control center** or **operations center**) — a part of a [SCS](scs.md) — is a facility that manages space flights, usually from the point of launch until landing or the end of the mission. It is part of the ground segment of spacecraft operations. A staff of flight controllers & other support personnel monitor all aspects of the mission using telemetry, & send commands to the vehicle using ground stations. Personnel supporting the mission from an MCC can include representatives of the attitude control system, power, propulsion, thermal, attitude dynamics, orbital operations & other subsystem disciplines. The training for these missions usually falls under the responsibility of the flight controllers, typically including extensive rehearsals in the MCC.

![](f/control/mcc_global.webp)

**(RU) ЦУП**

**Центр управле́ния полётами (ЦУП)** — сооружения с техническими системами и технологическими средствами командно‑программного, телеметрического и [баллистико‑навигационного обеспечения](nnb.md), вешних информационных обменов, магистральных и специальных связей, отображения, предназначенными для обеспечения деятельности обслуживающего персонала по формированию, передаче, приёму, обработке, хранению, документированию информации при непрерывном процессе управления полётами [космических аппаратов](sc.md) в период проведения [лётных испытаний](rnd_e.md) и эксплуатации [космических систем](scs.md). Согласно типовой [схеме деления](drawing.md) ЦУП входит в состав [НКУ](scs.md). Часто в состав ЦУП входят также [баллистические центры](scs.md).

【**Таблица.** Крупнейшие ЦУП】

|*#*|*List*|
|:-|:-|
|**[CN](contact/cnsa.md)**|➀ Пекинский центр управления космическими полётами|
|**[EU](contact/esa.md)**|➀ Европейский центр управления космическими объектами — Дармштадт, Германия<br> ➁ ATV Control Centre — Тулуза, Франция<br> ➂ Columbus Control Center — Оберпфаффенхофен, Германия|
|**[JP](contact/jaxa.md)**|➀ NEC Satellite Operation Center ([NEC](contact/nec.md))|
|**[RU](contact/roskosmos.md)**|➀ Центр управления полётами [ЦНИИмаш](contact/tsniimash.md) — Королёв, Московская область<br> ➁ Главный испытательный центр испытаний и управления космическими средствами имени Г.С. Титова — Краснознаменск, Московская область<br> ➂ Центр управления спутниками народно‑хозяйственного назначения (ЦУП-НХ) — [ОАО ИСС](contact/iss_r.md), Железногорск<br> ➃ ЦУП‑Л — [LAV](contact/lav.md), Химки, Московская область<br> ➄ ЦУП Бонум (ЦКС Сколково) — ФГУП «Космическая связь», Сколково, Московская область|
|**[US](contact/nasa.md)**|➀ Центр управления полётами (НАСА) — Хьюстон, Техас<br> ➁ [JPL](contact/jpl.md) — Пасадина, Калифорния|



### Space segment
   - **Attitude control.** A Spacecraft needs an attitude control subsystem to be correctly oriented in space & respond to external torques & forces properly. The attitude control subsystem consists of sensors & actuators, together with controlling algorithms. The attitude‑control subsystem permits proper pointing for the science objective, sun pointing for power to the solar arrays & earth pointing for communications.
   - **Command & data handling.** The CDH subsystem receives commands from the communications subsystem, performs validation & decoding of the commands, & distributes the commands to the appropriate spacecraft subsystems & components. The CDH also receives housekeeping data & science data from the other spacecraft subsystems & components, & packages the data for storage on a data recorder or transmission to the ground via the communications subsystem. Other functions of the CDH include maintaining the spacecraft clock & state‑of‑health monitoring.
   - **Communications.** SC, both robotic & crewed, utilize various communications systems for communication with terrestrial stations as well as for communication between spacecraft in space. Technologies utilized include RF & optical communication. In addition, some spacecraft payloads are explicitly for the purpose of ground‑ground communication using receiver/retransmitter electronic technologies.
   - **GNC.** Guidance refers to the calculation of the commands (usually done by the CDH subsystem) needed to steer the spacecraft where it is desired to be. Navigation means determining a spacecraft’s orbital elements or position. Control means adjusting the path of the spacecraft to meet mission requirements.
   - **Life support.** SC intended for human spaceflight must also include a life support system for the crew.
   - **Payload.** The payload depends on the mission of the SC, & is typically regarded as the part of the SC “that pays the bills”. Typical payloads could include scientific instruments (cameras, telescopes, or particle detectors, for example), cargo, or a human crew.
   - **Power.** SC need an electrical power generation & distribution subsystem for powering the various SC subsystems. For spacecraft near the Sun, solar panels are frequently used to generate electrical power. SC designed to operate in more distant locations, for example Jupiter, might employ a radioisotope thermoelectric generator (RTG) to generate electrical power. Electrical power is sent through power conditioning equipment before it passes through a power distribution unit over an electrical bus to other spacecraft components. Batteries are typically connected to the bus via a battery charge regulator, & the batteries are used to provide electrical power during periods when primary power is not available, for example when a low Earth orbit spacecraft is eclipsed by Earth.
   - **Thermal control.** SC must be engineered to withstand transit through Earth’s atmosphere & the space environment. They must operate in a vacuum with temperatures potentially ranging across hundreds of ℃ as well as (if subject to reentry) in the presence of plasmas. Material requirements are such that either high melting temperature, low density materials such as beryllium & reinforced carbon‑carbon or (possibly due to the lower thickness requirements despite its high density) tungsten or ablative carbon‑carbon composites are used. Depending on mission profile, spacecraft may also need to operate on the surface of another planetary body. The thermal control subsystem (TCS) can be passive, dependent on the selection of materials with specific radiative properties. Active TCS makes use of electrical heaters & certain actuators such as louvers to control temperature of equipments within specific ranges.
   - **Spacecraft propulsion.** SC may or may not have a propulsion subsystem, depending on whether or not the mission profile calls for propulsion. The Swift spacecraft is an example of a spacecraft that does not have a propulsion subsystem. Typically though, LEO spacecraft include a propulsion subsystem for altitude adjustments (drag make‑up maneuvers) & inclination adjustment maneuvers. A propulsion system is also needed for spacecraft that perform momentum management maneuvers. Components of a conventional propulsion subsystem include fuel, tankage, valves, pipes, & thrusters. The thermal control system interfaces with the propulsion subsystem by monitoring the temperature of those components, & by preheating tanks & thrusters in preparation for a spacecraft maneuver.
   - **Structures.** SC must be engineered to withstand launch loads imparted by a [LV](lv.md), & must have a point of attachment for all the other subsystems. Depending on mission profile, the structural subsystem might need to withstand loads imparted by entry into the atmosphere of another planetary body, & landing on the surface of another planetary body.



### User segment
…



<p style="page-break-after:always"> </p>

## (RU) КК и СЧ КК
Стандартная схема деления КК:

**Космический комплекс** (КК)  
░║  
░╟ **Наземный комплекс управления** (НКУ)  
░║  ╟ Баллистический центр (БЦ)  
░║  ╟ Наземные станции слежения (НСС)  
░║  ╟ Наземные станции управления (НСУ)  
░║  ╟ Сектор главного конструктора (СГК)  
░║  ╟ Средства связи и передачи данных (ССПД)  
░║  ╙ Центр управления полётом (ЦУП)  
░║  
░╟ **Наземный научный комплекс** (ННК)  
░║  ╟ Лаборатория  
░║  ╟ Комплекс долговременного хранения и обработки научных данных (КДХ)  
░║  ╟ Комплекс планирования работы научной аппаратуры (КПР)  
░║  ╟ Комплекс приёма и анализа научных и телеметрических данных (КПНД)  
░║  ╙ Комплекс связи и коммуникации (КСК)  
░║  
░╙ **Ракетно‑космический комплекс** (РКК)  
░░░╟ Комплекс разгонного блока (КРБ)  
░░░╟ Комплекс ракеты‑носителя (ТК РН)  
░░░╟ Комплес средств измерений, сбора и обработки (КСИСО)  
░░░╟ Технический комплекс космического аппарата (ТК КА)  
░░░╟ Технический комплекс космической головной части (ТК КГЧ)  
░░░╟ Технический комплекс ракеты космического назначения (ТК РКН)  
░░░╙ Ракета космического назначения (РКН)  
░░░░░╟ [Ракета‑носитель](lv.md) (РН)  
░░░░░╙ Космическая головная часть (КГЧ)  
░░░░░░░╟ [Головной обтекатель](lv.md) (ГО)  
░░░░░░░╟ Разгонный блок (РБ)  
░░░░░░░╟ [Переходной отсек](lv.md) (ПхО)  
░░░░░░░╙ **[Космический аппарат](sc.md)** (КА)  
░░░░░░░░░╟ Адаптер с устройством отделения  
░░░░░░░░░╟ Бортовой комплекс управления (БКУ)  
░░░░░░░░░║  ╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░║  ╟ Высотомер  
░░░░░░░░░║  ╟ Гироскоп  
░░░░░░░░░║  ╟ Датчик звёздный (ЗД)  
░░░░░░░░░║  ╟ Датчик контроля электризации  
░░░░░░░░░║  ╟ Датчик относительной ориентации (GPS, GLONASS)  
░░░░░░░░░║  ╟ Датчик солнечный (СД)  
░░░░░░░░░║  ╟ Двигатель‑маховик (ДМ)  
░░░░░░░░░║  ╟ Запоминающее устройство (ЗУ)  
░░░░░░░░░║  ╟ Привод антенны  
░░░░░░░░░║  ╟ Привод солнечных панелей (ПСП)  
░░░░░░░░░║  ╟ Программное обеспечение (ПО)  
░░░░░░░░░║  ╙ Цифровая вычислительная машина (ЦВМ)  
░░░░░░░░░╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░╟ Двигательная установка (ДУ)  
░░░░░░░░░║  ╟ Агрегаты  
░░░░░░░░░║  ╟ Баки  
░░░░░░░░░║  ╟ Двигатели  
░░░░░░░░░║  ╟ Защита, дренаж  
░░░░░░░░░║  ╟ Конструкция  
░░░░░░░░░║  ╟ Нагреватели, тепловые датчики  
░░░░░░░░░║  ╙ Трубопроводы  
░░░░░░░░░╟ Комплекс научной аппаратуры (КНА)  
░░░░░░░░░╟ Конструкция и механизмы (КММ)  
░░░░░░░░░╟ Радиокомплекс (РК)  
░░░░░░░░░║  ╟ Антенно‑фидерная система (АФС)  
░░░░░░░░░║  ╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░║  ╙ Приёмо‑передатчик  
░░░░░░░░░╟ Система электроавтоматики (СЭА)  
░░░░░░░░░╟ Система электроснабжения (СЭС)  
░░░░░░░░░║  ╟ Аккумуляторная батарея (АБ)  
░░░░░░░░░║  ╟ Бортовая кабельная сеть (БКС)  
░░░░░░░░░║  ╟ Комплекс автоматики и стабилизации  
░░░░░░░░░║  ╙ Солнечные панели  
░░░░░░░░░╟ Средства обеспечения теплового режима (СОТР)  
░░░░░░░░░║  ╟ Нагреватели, тепловые датчики  
░░░░░░░░░║  ╟ Покрытия  
░░░░░░░░░║  ╟ Радиаторы, коллекторы, тепловые трубы  
░░░░░░░░░║  ╙ Экранно‑вакуумная теплоизоляция (ЭВТИ)  
░░░░░░░░░╙ Телеметрическая система (ТМС)



### БЦ (Баллистический центр)
> <small>**Баллистический центр (БЦ)** — русскоязычный термин. **Ballistic analysis center (BAC)** — англоязычный эквивалент.</small>

**Баллистический центр (БЦ)** — комплекс программно‑аппаратных средств для определения орбит КА и расчётов траектории его движения, необходимых манёвров и для прочего баллистико‑навигационного обеспечения. Часто входит в состав [ЦУП](scs.md).

Известные БЦ РФ:

   1. БЦ [ИПМ Келдыша](contact/keldysh_ipm.md);
   1. БЦ [ЦНИИмаш](contact/tsniimash.md).



### КИК (Командно‑измерительный комплекс)
> <small>**Командно‑измерительный комплекс** — русскоязычный термин, не имеющий аналога в английском языке. **Сommand & measurement complex (CAMC)** — дословный перевод с русского на английский.</small>

**Командно‑измерительный комплекс (КИК)** — совокупность Земных средств и служб, с помощью которых осуществляется управление полётом [космических аппаратов](sc.md), [ракет‑носителей](lv.md) и космических объектов.

В состав КИК входят командно‑измерительные пункты, расположенные на суше, плавучие (корабельные) и самолётные измерительные пункты. Количество и местоположение стационарных командно‑измерительных пунктов определяются задачами обеспечения непрерывности управления различными КА и требованиями дублирования и резервирования. Состав и размещение стационарных и подвижных средств КИК, используемых для управления конкретными типами КА, определяются их орбитой, типом установленной на борту аппаратуры и программой полёта.

Основными средствами управления в КИК являются: аппаратура траекторных измерений (для определения параметров орбиты); телеметрическая аппаратура (для контроля и диагностики состояния КА); командно‑программная аппаратура (для выдачи на борт управляющих команд, программ и контроля их исполнения). В состав КИК входят также: вычислительные комплексы (ЭВМ), аппаратура автоматического ввода данных траекторных измерений в ЭВМ, системы автоматической обработки результатов телеизмерений, аппаратура приёма и передачи телевизионной информации, телефонной, телеграфной связи с космонавтами, служба единого точного времени, каналы и средства космической и наземной связи, средства контроля и отображения хода полёта, системы моделирования процессов управления и др.

Информация, поступающая с КА, обрабатывается координационно‑вычислительными центрами, которые выдают необходимые данные в Центр управления полётом).



### КИС (Командно‑измерительная система)
> <small>**Командно‑измерительная система (КИС)** — русскоязычный термин, не имеющий аналога в английском языке. **Command measurement system (COMES)** — дословный перевод с русского на английский.</small>

**Командно‑измерительная система (КИС)** — радиотехническое средство [НКУ](scs.md) и [НАКУ](scs.md) в совокупности с бортовой аппаратурой [КА](sc.md) или [РБ](lv.md), предназначенное для измерения параметров движения КА и РБ, приёма и передачи различных видов информации, формирования и передачи на КА и РБ команд и программ управления, стандартных частот и сигналов [времени](time.md) для синхронизации работы [GNC](gnc.md).

Известные КИС:

   1. <mark>TBD</mark>

Согласно типовой [схеме деления](drawing.md) КИС не входит в состав КК (КС), однако функционально входит в состав [НКУ](scs.md).



### КСИСО (Комплекс средств измерения, сбора и обработки информации)
> <small>**Комплекс средств измерения, сбора и обработки информации (КСИСО)** — русскоязычный термин, не имеющий аналога в английском языке. **System of measuring instruments, data acquisition & processing (SMIDAP)** — дословный перевод с русского на английский.</small>

**Комплекс средств измерения, сбора и обработки информации (КСИСО)** — совокупность сооружений, взаимосвязанных между собой технических средств и программного обеспечения [НКУ](scs.md) и [НАКУ](scs.md) [космическими аппаратами](sc.md) и измерений, предназначенных для автоматизированного контроля за функционированием [РКН](lv.md) в процессе предстартовой подготовки и на участке выведения, обеспечивающих обработку, документирование и распределение результатов измерений между потребителями.

Привлекается на этапе выведения [КА](sc.md) на орбиту перелёта и осуществляет контроль за выполнением [полётных заданий](fp.md) [LV](lv.md) и [РБ](lv.md) совместно с [НИК РБ](lm_sys.md). После выведения КА на орбиту перелёта функции контроля передаются в [НКУ](scs.md).



### НАКУ (Наземный автоматизированный комплекс управления)
> <small>**Наземный автоматизированный комплекс управления (НАКУ)** — русскоязычный термин. **Ground automated control complex** — англоязычный эквивалент.</small>

**Наземный автоматизированный комплекс управления (НАКУ)** — по [ГОСТ 53802](гост_53802.md), п. 30‑32 — совокупность необходимой инфраструктуры, технических систем, средств из состава командно‑измерительных и измерительных пунктов, центров и пунктов управления орбитальными средствами, центров обработки измерительной информации, предназначенных для формирования наземных комплексов, обеспечивающих реализацию автоматизированных процессов контроля параметров полёта [изделий](unit.md) ракетно‑космической техники, состояния бортовой аппаратуры и управления их функционированием.

Согласно типовой [схеме деления](drawing.md) НАКУ является самостоятельной структурой и не входит в состав [КК (КС)](scs.md).



### НИП (Наземный измерительный пункт)
> <small>**Наземный измерительный пункт (НИП)** — русскоязычный термин. **Ground telemetry station** — англоязычный эквивалент.</small>

**Наземный измерительный пункт (НИП)**, также **Научно‑измерительный пункт** (Отдельный командно‑измерительный комплекс) — пункт контроля и управления [космическими аппаратами](sc.md).

Разделяют на:

   - наземные измерительные пункты (НИП);
   - плавучие измерительные пункты;
   - самолётные измерительные пункты (СИП);
   - отдельные измерительные пункты (ОИП).

Обычно функционально входит в состав [НКУ](scs.md).



### НК (Наземный комплекс)
> <small>**Наземный комплекс (НК)** — русскоязычный термин, не имеющий аналога в английском языке. **Ground‑based complex** — дословный перевод с русского на английский.</small>

**Наземный комплекс** ─ общее негостированное название всех наземных элементов, предназначенных для управления и обмена информацией с космическим аппаратом.

Может включать в свой состав:

   1. **Наземный комплекс управления (НКУ)**:
      - баллистические центры;
      - наземные станции слежения;
      - наземные станции управления
      - телекоммуникации и средства связи;
      - сектор главного конструктора;
      - средства обработки и хранения информации;
      - прочие средства управления и обеспечения управления.
   2. **Наземный научный комплекс (ННК)**:
      - аппаратно‑программные средства приёма, передачи, обработки и хранения информации.



### НКПОР (Наземный комплекс приёма, обработки и распределения информации)
> <small>**Наземный комплекс приёма, обработки и распределения информации (НКПОР)** — русскоязычный термин, не имеющий аналога в английском языке. **Ground-based complex for data receiving, processing & distribution (GCDRPD)** — дословный перевод с русского на английский.</small>

**Наземный комплекс приёма, обработки и распределения информации (НКПОР)** — совокупность взаимосвязанных технических средств с программным обеспечением, расположенных на [Земле](earth.md) и предназначенных для обеспечения заказчика и его потребителей целевой информацией, полученной на основе космических данных.

Согласно типовой [схеме деления](drawing.md) НКПОР не входит никуда.



### НКУ (Наземный комплекс управления)
> <small>**Наземный комплекс управления (НКУ)** — русскоязычный термин. **Ground segment (GS)** — примерный англоязычный эквивалент.</small>

**Наземный комплекс управления (НКУ)** — совокупность взаимосвязанных технических средств с информационным и математическим обеспечением, сооружений, [центра управления полётом](scs.md) и отдельных командно‑измерительных комплексов, предназначенных для автоматизированного управления КА на всех этапах полёта КА после его отделения от [разгонного блока](lv.md).

**НКУ** обычно включает в свой [состав](drawing.md):

   - [Баллистический центр](scs.md) (БЦ)
   - Наземная станция (НС)
   - [Сектор главного конструктора](cd_segm.md) (СГК)
   - [Средства связи и передачи данных](mcntd.md) (ССПД)
   - [Центр управления полётом](scs.md) (ЦУП)

На этапе выведения на орбиту перелёта НКУ не привлекается. На этом этапе полёта контроль за выполнением [полётных заданий](fp.md) [LV](lv.md) и [РБ](lv.md) осуществляется наземными средствами [КСИСО](scs.md) и [НИК](lm_sys.md) РБ. Также может включать в свой состав [КИС](scs.md) и [НИП](scs.md).



### ННК (Наземный научный комплекс)
> <small>**Наземный научный комплекс (ННК)** — русскоязычный термин. **[User segment (US)](us.md)** или **[Payload data ground segment (PDGS)](pdgs.md)** — примерный англоязычный эквивалент.</small>

**Наземный научный комплекс (ННК)** — совокупность [аппаратно‑программных средства (АПС)](hns.md) предназначенных для осуществления полного цикла сбора, обработки, анализа и долговременного хранения всех типов данных (калибровочной, научной, вспомогательной и служебной информации), принимаемых с борта [КА](sc.md), подготовки программ проведения наблюдений, а также распространения научной информации среди участников проекта.

По факту ННК представляет собой группу серверов со специализированным ПО и каналы связи.

| | |
|:-|:-|
|**AE**|…|
|**AU**|…|
|**CA**|…|
|**CN**|…|
|**EU**|…|
|**IL**|…|
|**IN**|…|
|**JP**|・[NEC](contact/nec.md)|
|**Korea South**|…|
|**RU**|…|
|**Saudi Arabia**|…|
|**SG**|…|
|**US**|…|
|**VN**|…|



### НС (Наземная станция)
> <small>**Наземная станция (НС)** — русскоязычный термин. **Ground station (GS) / Earth station (ES) / Earth terminal (ET)** — англоязычные эквиваленты.</small>

**Наземная станция (НС)** — земная [радиостанция](comms.md), предназначенная для связи с [космическим аппаратом](sc.md), находящимся вне Земли, или для приёма‑передачи радиоволн от (к) астрономическим источникам радиоизлучения. НС входит в состав НКУ.

**Разновидности:**

   - **Наземная станция приёма информации (НСПИ)** — наземная станция, предназначенная для приёма информации от космического аппарата.  **Ground station for information reception** — дословный перевод с русского на английский.
   - **Наземная станция приёма научной информации (НСПНИ)** — наземная станция, предназначенная для приёма научной информации от космического аппарата. **Ground station for scientific information reception** — дословный перевод с русского на английский.
   - **Наземная станция управления (НСУ)** — наземная станция, предназначенная для управления КА. **Ground control station** — англоязычный эквивалент.

**Производители, операторы:**

| | |
|:-|:-|
|**AU**|…|
|**CA**|・[MDA](contact/mda.md)|
|**CN**|…|
|**EU**|…|
|**IL**|…|
|**IN**|…|
|**JP**|・[Infostellar](contact/infostellar.md) — space communication infrastructure, 10+ UHF/S/X antennas<br> ・[Kratos IS](contact/kratos.md) — R&D ground antennas, optimizing/managing satelllites, signals<br> ・[Mitsubishi Elecric](contact/mitsubishi.md) — ground control stations for satellite tracking, & optical/radio telescopes for astronomical observation, antennas, transmitters & receivers<br> ・[RESTEC](contact/restec.md)|
|**KR**|…|
|**RU**|・[ОКБ МЭИ](contact/okbmei.md)|
|**SA**|…|
|**SG**|…|
|**US**|…|
|**AE**|…|
|**VN**|…|

|*Изображение*|*Описание*|
|:-|:-|
|[![](f/gs/cdsn_pic1_thumb.webp)](f/gs/cdsn_pic1.webp)|**[Chinese Deep Space Network](cdsn.md)**<br> (Китай)|
|[![](f/gs/estrack_pic1_thumb.webp)](f/gs/estrack_pic1.webp)|**[ESTRACK](estrack.md)**<br> (Европа)|
|[![](f/gs/idsn_pic1_thumb.webp)](f/gs/idsn_pic1.webp)|**[Indian Deep Space Network](idsn.md)**<br> (Индия)|
|[![](f/gs/dsn_antenna_thumb2.webp)](f/gs/dsn_antenna.webp)|**[NASA Deep Space Network](dsn.md)**<br> (США)|
|[![](f/gs/ssc_ggsn_thumb2.webp)](f/gs/ssc_ggsn.webp)|**[SSC’s Global Ground Station Network](ssc_ggsn.md)**<br> (Европа, Швеция)|
|[![](f/gs/udsc_pic1_thumb.webp)](f/gs/udsc_pic1.webp)|**[Usuda Deep Space Center](udsc.md)**<br> (Япония)|
|[![](f/gs/map_world_ground_stations_thumb2.webp)](f/gs/map_world_ground_stations.webp)|**Мировые НС**|
|[![](f/gs/map_world_ground_stations_nkudka_thumb2.webp)](f/gs/map_world_ground_stations_nkudka.webp)|**НС в рамках НКУ‑ДКА**<br> (примерное расположение)|

【**Таблица.** Известные НС】

| |*Описание*|*Изобр.*|
|:-|:-|:-|
|**EU**|**Raisting Satellite Earth Station (Германия)**, [Maspalomas Station](maspalomas_station.md)|
|**RU**|**Калязинская радиоастрономическая обсерватория**<br> Владелец — [ОКБ МЭИ](contact/okbmei.md).<br> ・Радиотелескоп ТНА‑1500 или РТ‑64: D = 64 м, F/0.37, полноповоротный параболический рефлектор, мин. раб. длина волны = 1 ㎝, M общая = 3 800 т, M зеркала = 800 т, вторичное зеркало D = 6 м.<br> ・Наблюдаемая часть небесной сферы: A = ± 300° H = 0 ‑ 90°. Класс наблюдений: B; Выделенные [полосы частот](comms.md) для наблюдений, ㎓.: 0.608 ‑ 0.614, 1.66 ‑ 1.67, 4.8 ‑ 4.99, 4.99 ‑ 5.0, 22.21 ‑ 22.50. Шумовая температура радиотелескопа, К: 80, 22, 22, 22, 65.|[![](f/gs/20081011_tna-1500_radio_telescope_in_kalyazin_wikipedia_ru_thumb.webp)](f/gs/20081011_tna-1500_radio_telescope_in_kalyazin_wikipedia_ru.webp)|
| |**Центр космической связи «Медвежьи озёра»**<br> Владелец — [ОКБ МЭИ](contact/okbmei.md).<br> ・Радиотелескоп ТНА‑1500 или РТ‑64: D = 64 м, F/0.37, полноповоротный параболический рефлектор, мин. раб. длина волны = 1 ㎝, M общая = 3 800 т, M зеркала = 800 т, вторичное зеркало D = 6 м. Собирающая площадь 1 500 m².<br> ・Работает с 1979 г. До 2010 г была только принимающей антенной, теперь она и передающая. Система облучения Грегори.|[![](f/gs/20160819_mosoblast_schyolkovo_district_radio_telescope_wikipedia_ru_thumb.webp)](f/gs/20160819_mosoblast_schyolkovo_district_radio_telescope_wikipedia_ru.webp)|
| |**Восточный центр дальней космической связи (Уссурийск)**<br> 44°00′57″ с.ш. 131°45′25″ в.д. <sup>[H](https://tools.wmflabs.org/geohack/geohack.php?:language=ru&pagename=%D0 %A0 %D0 %A2-70&params=44_0_57.90_N_131_45_25.13_E) [G](https://maps.google.com/maps?:ll=44.0160833,131.7569806&q=44.0160833,131.7569806&spn=0.03,0.03&t=h&hl=ru) [Я](https://yandex.ru/maps/?:ll=131.7569806,44.0160833&pt=131.7569806,44.0160833&spn=0.03,0.03&l=sat,skl) [O](https://www.openstreetmap.org/?:mlat=44.0160833&mlon=131.7569806&zoom=14)</sup><br> ・Радиотелескоп П‑2500 или РТ‑70.|[![](f/gs/20150412_ussuriisk_c538a_9da9691a_orig_livejournal_ru_thumb.webp)](f/gs/20150412_ussuriisk_c538a_9da9691a_orig_livejournal_ru.webp)|



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:-|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**`Космический комплекс (КК):`**<br> [Выводимая масса](throw_weight.md)・ [ГО и ПхО](lv.md)・ [Класс чистоты](clean_lvl.md)・ [Контейнеры для транспортировки](ship_contain.md)・ [СЧ](sui.md)|
|**`Наземный комплекс управления (НКУ):`**<br> [БЦ](scs.md)・ [КИС](scs.md)・ [КСИСО](scs.md)・ [НИК](lm_sys.md)・ [НИП](scs.md)・ [НС](scs.md)・ [ПОЗ](fp.md)・ [СГК](cd_segm.md)・ [ССПД](mcntd.md)・ [ЦУП](scs.md)|
|**`Наземная станция (НС):`**<br> … <br><br> [CDSN](cdsn.md)・ [DSN](dsn.md)・ [ESTRACK](estrack.md)・ [IDSN](idsn.md)・ [SSC_GGSN](ssc_ggsn.md)・ [UDSC](udsc.md)|
|**`Наземный научный комплекс (ННК):`**<br> [АПС](hns.md)|

   1. Docs:
      - SCS:
         1. [ГОСТ 53802](гост_53802.md), п. 1‑7
         1. [РК‑11](const_rk.md), стр. 17
      - НКУ: [ГОСТ 53802](гост_53802.md), п.30‑32
      - БЦ: [ГОСТ 53802](гост_53802.md), п.43
      - НКПОР: [ГОСТ 53802](гост_53802.md), п.50
      - НАКУ: [ГОСТ 53802](гост_53802.md), п. 30‑32
      - КСИСО: [ГОСТ 53802](гост_53802.md), п. 51
      - КИК: <https://ru.wikipedia.org/wiki/Категория:Командно‑измерительный_комплекс>
      - ЦУП: [ГОСТ 53802](гост_53802.md), п. 41‑42
   1. SCS:
      1. <https://en.wikipedia.org/wiki/Attitude_control>
      1. <https://en.wikipedia.org/wiki/Ground_segment>
      1. <https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control>
      1. <https://en.wikipedia.org/wiki/Space_segment>
      1. <https://en.wikipedia.org/wiki/Fixed-satellite_service>
      1. <https://ru.wikipedia.org/wiki/Научно‑измерительный_пункт>
   1. НС:
      1. <https://en.wikipedia.org/wiki/Ground_station>
      1. <https://ru.wikipedia.org/wiki/Восточный_центр_дальней_космической_связи>
      1. <https://ru.wikipedia.org/wiki/Калязинская_радиоастрономическая_обсерватория>
      1. <https://ru.wikipedia.org/wiki/РТ-70>
      1. <https://ru.wikipedia.org/wiki/Центр_космической_связи_«Медвежьи_озёра»>
   1. БЦ:
      1. <http://www.ngpedia.ru/id584007p1.html>
      1. <http://www.keldysh.ru/httpd/kiam-info_fr.html>
      1. <http://www.kiam1.rssi.ru/>
   1. ЦУП:
      1. <https://en.wikipedia.org/wiki/Mission_control_center>
      1. <https://ru.wikipedia.org/wiki/Центр_управления_полётами_(организация)>
