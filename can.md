# CAN
> 2021.01.21 [🚀](../index/index.md) [despace](index.md) → [Cable](cable.md), [Doc](doc.md), [GNC](gnc.md)

[TOC]

---

> <small>**Controller Area Network (CAN bus)** — EN term. **Сеть контроллеров (КАН)** — literal RU translation.</small>

A **Controller Area Network (CAN bus)** is a robust vehicle bus standard designed to allow microcontrollers & devices to communicate with each other's applications without a host computer. It is a message‑based protocol, designed originally for multiplex electrical wiring within automobiles to save on copper, but can also be used in many other contexts. For each device the data in a frame is transmitted sequentially but in such a way that if more than one device transmits at the same time the highest priority device is able to continue while the others back off. Frames are received by all devices, including by the transmitting device.

Bosch published several versions of the CAN specification & the latest is CAN 2.0 published in 1991. This specification has two parts; part A is for the standard format with an 11‑bit identifier, & part B is for the extended format with a 29‑bit identifier. A CAN device that uses 11‑bit identifiers is commonly called **CAN 2.0A** & a CAN device that uses 29‑bit identifiers is commonly called **CAN 2.0B**. These standards are freely available from Bosch along with other specifications & white papers.

|*Standard*|*ISO 11898*|
|:--|:--|
|Connector types|Not specified. DE‑9 is commonly used|
|Creation date|1986|
|Max. Binary Rate|10 kbit/s ‑ 1 Mbit/s, or 5 Mbit/s (incl. 3/11 of bitrate for service information)|
|Max. Devices|40|
|Max. Distance|40 ‑ 5 000 m|
|Network Topology|multi‑master serial|
|Physical Media|two wire|
|Voltage Levels|0 ‑ 5 V, both wires must be able to handle −27 ‑ +40 V without damage|

[![](f/cable/de_9_1_thumb.jpg)](f/cable/d3_9_1.jpg)  
*DE‑9 is commonly used*

**Physical organization.**  
CAN is a multi‑master serial bus standard for connecting Electronic Control Units (ECUs) also known as nodes. (Automotive electronics is a major application domain.) Two or more nodes are required on the CAN network to communicate. A node may interface to devices from simple digital logic e.g. PLD, via FPGA up to an embedded computer running extensive software. Such a computer may also be a gateway allowing a general purpose computer (like a laptop) to communicate over a USB or Ethernet port to the devices on a CAN network.  
All nodes are connected to each other through a physically conventional two wire bus. The wires are a twisted pair with a 120 Ω (nominal) characteristic impedance.  
This bus uses differential wired‑AND signals. Two signals, CAN high (CANH) & CAN low (CANL) are either driven to a “dominant” state with CANH > CANL, or not driven & pulled by passive resistors to a “recessive” state with CANH ≤ CANL. A 0 data bit encodes a dominant state, while a 1 data bit encodes a recessive state, supporting a wired‑AND convention, which gives nodes with lower ID numbers priority on the bus.  
ISO 11898‑2, also called high‑speed CAN (bit speeds up to 1 Mbit/s on CAN, 5 Mbit/s on CAN‑FD), uses a linear bus terminated at each end with 120 Ω resistors. High‑speed CAN signaling drives the CANH wire towards 3.5 V & the CANL wire towards 1.5 V when any device is transmitting a dominant (0), while if no device is transmitting a dominant, the terminating resistors passively return the two wires to the recessive (1) state with a nominal differential voltage of 0 V. (Receivers consider any differential voltage of less than 0.5 V to be recessive.) The dominant differential voltage is a nominal 2 V. The dominant common mode voltage (CANH+CANL)/2 must be within 1.5 to 3.5 V of common, while the recessive common mode voltage must be within ±12 of common.  
ISO 11898‑3, also called low‑speed or fault‑tolerant CAN (up to 125 kbit/s), uses a linear bus, star bus or multiple star buses connected by a linear bus & is terminated at each node by a fraction of the overall termination resistance. The overall termination resistance should be close to, but not less than, 100 Ω. Low‑speed fault‑tolerant CAN signaling operates similarly to high‑speed CAN, but with larger voltage swings. The dominant state is transmitted by driving CANH towards the device power supply voltage (5 V or 3.3 V), & CANL towards 0 V when transmitting a dominant (0), while the termination resistors pull the bus to a recessive state with CANH at 0 V & CANL at 5 V. This allows a simpler receiver which just considers the sign of CANH−CANL. Both wires must be able to handle −27 ‑ +40 V without damage.

**Electrical properties.**  
With both high‑speed & low‑speed CAN, the speed of the transition is faster when a recessive to dominant transition occurs since the CAN wires are being actively driven. The speed of the dominant to recessive transition depends primarily on the length of the CAN network & the capacitance of the wire used.  
High‑speed CAN is usually used in automotive & industrial applications where the bus runs from one end of the environment to the other. Fault‑tolerant CAN is often used where groups of nodes need to be connected together.  
The specifications require the bus be kept within a minimum & maximum common mode bus voltage, but do not define how to keep the bus within this range.  
The CAN bus must be terminated. The termination resistors are needed to suppress reflections as well as return the bus to its recessive or idle state.  
High‑speed CAN uses a 120 Ω resistor at each end of a linear bus. Low‑speed CAN uses resistors at each node. Other types of terminations may be used such as the Terminating Bias Circuit defined in ISO 11783.  
A terminating bias circuit provides power & ground in addition to the CAN signaling on a four‑wire cable. This provides automatic electrical bias & termination at each end of each bus segment. An ISO 11783 network is designed for hot plug‑in & removal of bus segments & ECUs.



## (RU) CAN
**CAN** (англ. Controller Area Network — сеть контроллеров) — стандарт промышленной сети для объединения в единую сеть различных исполнительных устройств и датчиков. Режим передачи — последовательный, широковещательный, пакетный. CAN разработан компанией Robert Bosch GmbH в середине 1980‑х, широко распространён в промышленной и домашней автоматизации, автомобильной промышленности и пр. Непосредственно стандарт CAN компании Bosch определяет передачу в отрыве от физического уровня — он может быть каким угодно, например, радиоканалом или оптоволокном. Но на практике под CAN‑сетью обычно подразумевается сеть топологии «шина» с физическим уровнем в виде дифференциальной пары, определённым в стандарте ISO 11898. Передача ведётся кадрами, которые принимаются всеми узлами сети. Для доступа к шине выпускаются специализированные микросхемы — драйверы CAN‑шины.

   - **Преимущества:**
      - Возможность работы в режиме жёсткого реального времени.
      - Простота реализации и минимальные затраты на использование.
      - Высокая устойчивость к помехам.
      - Арбитраж доступа к сети без потерь пропускной способности.
      - Надёжный контроль ошибок передачи и приёма.
      - Широкий диапазон скоростей работы.
      - Большое распространение технологии, широкий ассортимент продуктов от различных поставщиков.
   - **Недостатки:**
      - Небольшое количество данных, которое можно передать в одном пакете (до 8 байт).
      - Большой размер служебных данных в пакете (по отношению к полезным данным).
      - Отсутствие единого общепринятого стандарта на протокол высокого уровня, однако это и достоинство. Стандарт сети предоставляет широкие возможности для практически безошибочной передачи данных между узлами, оставляя разработчику возможность вложить в этот стандарт всё, что туда сможет поместиться. В этом отношении CAN подобен простому электрическому проводу. Туда можно «затолкать» любой поток информации, который сможет выдержать пропускная способность шины. Известны примеры передачи звука и изображения по шине CAN (Россия). Известен случай создания системы аварийной связи вдоль автодороги длиной несколько десятков километров (Германия) (в первом случае нужна была большая скорость передачи и небольшая длина линии, во втором случае — наоборот). Изготовители, как правило, не афишируют, как именно они используют полезные байты в пакете.

CAN является синхронной шиной с типом доступа Collision Resolving (CR, разрешение коллизии), который, в отличие от Collision Detect (CD, обнаружение коллизии) сетей (Ethernet), детерминировано (приоритетно) обеспечивает доступ на передачу сообщения, что особо ценно для промышленных сетей управления (fieldbus). Передача ведётся кадрами. Полезная информация в кадре состоит из идентификатора длиной 11 бит (стандартный формат) или 29 бит (расширенный формат, надмножество предыдущего) и поля данных длиной от 0 до 8 байт (0 ‑ 72 %). Идентификатор говорит о содержимом пакета и служит для определения приоритета при попытке одновременной передачи несколькими сетевыми узлами.

**Протоколы верхнего уровня.**  
Базовой спецификации CAN недостаёт многих возможностей, требуемых в реальных системах: передачи данных длиннее 8 байт, автоматического распределения идентификаторов между узлами, единообразного управления устройствами различных типов и производителей. Поэтому вскоре после появления CAN на рынке начали разрабатываться протоколы высокого уровня для него. В число распространённых на данный момент протоколов входят: CANopen, DeviceNet, CAN Kingdom, J1939, SDS, NMEA‑2000 (морской транспорт), ARINC‑825 (авиация)  (нем.), UAVCAN (робототехника и летательные аппараты).

**Скорость передачи и длина сети.**  
Все узлы в сети должны работать с одной скоростью. Стандарт CAN не определяет скоростей работы, но большинство как отдельных, так и встроенных в микроконтроллеры адаптеров позволяет плавно менять скорость в диапазоне, по крайней мере, от 20 кбит/с до 1 Мбит/с. Существуют решения, выходящие за рамки данного диапазона.  
Методы контроля ошибок требуют, чтобы изменение бита при передаче успело распространиться по всей сети к моменту замера значения. Это ставит максимальную длину сети в обратную зависимость от скорости передачи: чем больше скорость, тем меньше длина. Использование оптопар для защиты устройств от высоковольтных помех в сети ещё больше сокращает предельную длину, тем больше, чем больше задержка сигнала в оптопаре. Сильно разветвлённые сети (паутина) также снижают скорость из‑за множества отражений сигнала и большей электрической ёмкости шины. Например, для сети ISO 11898 предельные длины составляют приблизительно:

|*1 Мбит/с*|*500 кбит/с*|*125 кбит/с*|*10 кбит/с*|
|:--|:--|:--|:--|
|40 м|100 м|500 м|5 000 м|



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**【[Cable](cable.md)】**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [ОТБКС](cable.md)|
|**【[Guidance, Navigation & Control (GNC)](gnc.md)】**<br> [CAN](can.md)・ [LVDS](lvds.md)・ [MIL‑STD‑1553](mil_std_1553.md) (МКО)・ [RS‑232, 422, 485](rs_xxx.md)・ [SpaceWire](spacewire.md)・ [АСН, САН](ans.md)・ [БНО](nnb.md)[MIL‑STD‑1553](mil_std_1553.md) (МКО)[БАППТ](eas.md)・ [БКС](cable.md)・ [БУ](eas.md)・ [БШВ](time.md)・ [Гироскоп](iu.md)・ [Дальномер](doppler.md) (ИСР)・ [ДМ](iu.md)・ [ЗД](sensor.md)・ [Компьютер](obc.md) (ЦВМ, БЦВМ)・ [Магнитометр](sensor.md)・ [МИХ](mic.md)・ [МКО](mil_std_1553.md)・ [ПО](soft.md)・ [ПНА, ПОНА, ПСНА](devd.md)・ [СД](sensor.md)・ [Система координат](coord_sys.md)・ [СОСБ](devd.md)|

   1. Docs: …
   1. <https://en.wikipedia.org/wiki/CAN_bus>
   1. <https://www.micromax.ru/solution/theory-practice/articles/2160/>
