# GR712RC
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → **[ЦВМ](obc.md)**

[TOC]

---

**GR712RC** — процессор, предназначенный для использования в составе [КА](sc.md).  
*Разработчик:* [Cobham](cobham.md). Разработано в 2019 году. активное использование <small>(на 2019 год)</small>
   - **Предшественник:** 
   - **Преемник:** 

| |
|:--|
|[![](f/cpu/g/gr712rc_pic1_thumb.jpg)](f/cpu/g/gr712rc_pic1.jpg)|

<small>

|*Характеристика*|*[Значение](si.md) <small>()</small>*|
|:--|:--|
|[TRL](trl.md)|9|
|Быстродействие|100 ㎒ (200 MIPS, 200 MFLOPS)|
|Время восстановления<br> работоспособности, с| |
|Исполнение|Моноблок|
|Команды, датчики, входы|… — команд управления;<br>… — релейных матричных команд управления;<br>… — ТМ‑датчиков;<br>… — входов прерываний от контактных датчиков;<br>… — входов прерываний от импульсных датчиков|
|Объём|16 KiB multi-way instruction cache and 16 KiB multi-way data cache, 192 kByte memory block with EDAC|
|Разрядность данных|32 бит|
|Тип процессора|dual-core LEON3FT SPARC V8, 180 nm standard CMOS, Tower Semiconductors Ltd|
|**Etc:**|• • •|
|[Reliability](qm.md)/[lifetime](lifetime.md)| |
|Dimensions, L×W×H, mm|75 × 75 × 3.5|
|Interfaces|• Four SpaceWire ports, maximum 200 Mbps full-duplex data rate;<br> ・Redundant [MIL-STD-1553B](mil_std_1553.md) BRM (BC/RT/BM) interface;<br> ・Two CAN 2.0B bus controllers;<br> ・Six UART ports, with 8-byte FIFO;<br> ・Ethernet MAC with RMII 10/100 Mbps port;<br> ・SPI master serial port;<br> ・I2C master serial port;<br> ・ASCS16 (STR) serial port;<br> ・SLINK 6 ㎒ serial port;<br> ・CCSDS/ECSS 5‑channel Telecommand decoder, 10 Mbps input rate;<br> ・CCSDS/ECSS Telemetry encoder, 50 Mbps output rate;<br> ・26 input and 38 input/output general purpose ports|
|Mass, ㎏|0.017|
|[Voltage](voltage.md), V|1.8 или 3.3|
|Overload, g| |
|[Rad.resist](ion_rad.md), ㏉ (㎭)|3 000 (300 000)|
|Resource, h (y)| |
|[Lifetime](lifetime.md), h (y)| |
|[Thermal range](tcs.md), ℃|от −55 до +125 ℃|
|Consumption, W| |

</small>



<p style="page-break-after:always"> </p>

## Примечания
   1. …



## Применяемость
По состоянию на 2019.03.11 прибор GR712RC применяется в составе:

   1. [Beresheet](beresheet.md)



## Опыт использования
…



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [](.md) •··**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://www.gaisler.com/index.php/products/components/gr712rc>
