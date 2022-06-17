# Command & Data-handling
> 2020.11.07 [🚀](../../index/index.md) [despace](index.md) → **[](.md)** <mark>NOCAT</mark>  
> *Navigation:*  
> **[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·Событ., **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ

**Table of contents:**

[TOC]

---

> <small>**RU** — RU term w/o analogues in English. **EN** — literal EN translation.</small>

The **Command and Data Handling (C&DH)** subsystem is essentially the “brains” of the spacecraft and controls all spacecraft functions. The C&DH system handles all data sent and received by the spacecraft, including science data and spacecraft or payload operations. The system is connected to the RF transmitter and receiver units provide a communication channel between the spacecraft and the ground operators. The basic data flow over a space link is made of Telemetry (TM) and Telecommand (TC) data.

Command & Data-handling Systems system:

   - manages all forms of data on the spacecraft;
   - carries out commands sent from Earth;
   - prepares data for transmission to Earth;
   - manages collection of solar power and charging of the batteries;
   - collects and processes information about all subsystems and payloads;
   - keeps and distributes the spacecraft time;
   - calculates the spacecraft's position in orbit around the planet;
   - carries out commanded maneuvers;
   - autonomously monitors and responds to a wide range of onboard problems that might occur.

The key parts of this system are:

   - **[Data storage system](ds.md).** The science data is stored on this recorder until it is ready for transmission to Earth, and then is overwritten with new science data.
   - **[Flight Software](soft.md).** The Flight Software is an integral part of the Space Flight Computer, and includes many applications running on top of an operating system. Common operating system is VxWorks.
   - **[Space Flight Computer](obc.md) (On-board computer, OBC)**

【**Table.** Manufacturers】

| | |
|:-|:-|
|**AE**|…|
|**AU**|…|
|**CA**|・[Xiphos](contact/xiphos.md) — CPUs (OBCs), Firmware & Software|
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



<p style="page-break-after:always"> </p>

## Docs & links
|*Sections & pages*|
|:-|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. <https://mars.nasa.gov/mro/mission/spacecraft/parts/command/>
   1. <https://www.ruag.com/en/products-services/space/electronics/satellite-and-launcher-computers/command-and-data-handling-systems>
