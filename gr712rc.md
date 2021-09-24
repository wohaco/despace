# GR712RC
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → **[ЦВМ](obc.md)**

[TOC]

---

**GR712RC** — процессор, предназначенный для использования в составе [КА](sc.md).  
Разработчик [Cobham](cobham.md). Разработано в 2019 году. активное использование <small>(на 2019 год)</small>

|*Characteristics*|*[Value](si.md)<br> (GR712RC)*|
|:--|:--|
|Composition| |
|Consumption, W| |
|Dimensions, ㎜|75 × 75 × 3.5|
|[Interfaces](interface.md)|• Four [SpaceWire](spacewire.md) ports, maximum 200 Mbps full-duplex data rate;<br> ・Redundant [MIL-STD-1553B](mil_std_1553.md) BRM (BC/RT/BM) interface;<br> ・Two CAN 2.0B bus controllers;<br> ・Six UART ports, with 8-byte FIFO;<br> ・Ethernet MAC with RMII 10/100 Mbps port;<br> ・SPI master serial port;<br> ・I2C master serial port;<br> ・ASCS16 (STR) serial port;<br> ・SLINK 6 ㎒ serial port;<br> ・CCSDS/ECSS 5‑channel Telecommand decoder, 10 Mbps input rate;<br> ・CCSDS/ECSS Telemetry encoder, 50 Mbps output rate;<br> ・26 input and 38 input/output general purpose ports|
|[Lifetime](lifetime.md)/Resource, h(y)|… / …|
|Mass, ㎏|0.017|
|[Overload](vibration.md), Grms| |
|[Rad.resist](ion_rad.md), ㏉ (㎭)|3 000 (300 000)|
|[Reliability](qm.md) per [lifetime](lifetime.md)| |
|[Thermal range](tcs.md), ℃|−55 ‑ +125|
|[TRL](trl.md)|9|
|[Voltage](voltage.md), V|1.8 или 3.3|
|**【Specific】**|• • •|
|Performance|100 ㎒ (200 MIPS, 200 MFLOPS)|
|Recovery time, s| |
|Исполнение|Single unit|
|Commands,<br> sensors,<br> inputs|… — команд управления;<br>… — релейных матричных команд управления;<br>… — ТМ‑датчиков;<br>… — входов прерываний от контактных датчиков;<br>… — входов прерываний от импульсных датчиков|
|Объём|16 KiB multi-way instruction cache and 16 KiB multi-way data cache, 192 kByte memory block with EDAC|
|Bit depth|32 бит|
|CPU type|dual-core LEON3FT SPARC V8, 180 nm standard CMOS, Tower Semiconductors Ltd|
| |[![](f/cpu/g/gr712rc_pic1_thumb.jpg)](f/cpu/g/gr712rc_pic1.jpg)|

**Notes:**

   1. …
   1. **Applicability:**
      - [Beresheet](beresheet.md)



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC](sc.md)**·КА, **[OE](oe.md)**·БА, **[SGM](sgm.md)**·КММ】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[Model](model.md)**·Модель, **[N&B](nnb.md)**·БНО, **[Patent](патент.md)**·Патент, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://www.gaisler.com/index.php/products/components/gr712rc>
