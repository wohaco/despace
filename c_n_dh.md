# Command & Data-handling
> 2020.11.07 [🚀](../index/index.md) [despace](index.md) → **[](.md)** <mark>NOCAT</mark>

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

**Manufacturers**

| | |
|:--|:--|
|**Australia**|…|
|**Canada**|・[Xiphos](zz_xiphos.md) — CPUs (OBCs), Firmware & Software|
|**China**|…|
|**Europe**|…|
|**India**|…|
|**Israel**|…|
|**Japan**|…|
|**Korea S.**|…|
|**Russia**|…|
|**Saudi Ar.**|…|
|**Singapore**|…|
|**USA**|…|
|**UAE**|…|
|**Vietnam**|…|



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://mars.nasa.gov/mro/mission/spacecraft/parts/command/>
   1. <https://www.ruag.com/en/products-services/space/electronics/satellite-and-launcher-computers/command-and-data-handling-systems>
