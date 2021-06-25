# Communications
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [Comms](comms.md), [OE](oe.md)

[TOC]

---

> <small>**Communications, Radiolink** — EN term. **Радиосвязь** — RU analogue.</small>

**Radio communication** — a type of telecommunication, wireless communication, in which the carrier of the signal is radio waves, i.e. electromagnetic waves freely propagating in space:

   - **Antenna-feeder system (AFS)** — see AFS.
   - **Antenna-feeder device (AFD)** — a set of technical means designed to receive & emit radio waves in a given direction.
   - **Onboard radio complex (ORC)** — a set of technical means intended for the implementation of radio communications. Includes receiving & transmitting equipment and AFD.



## Receiver noise temperature

| |*Temp.*|*Station*|
|:--|:--|:--|
|**On Earth**|50|Green Bank Telescope (GBT), Latitude: 38.433°N, Longitude: 79.84°W, ESA|
| |60|Sardinia Radio Telescope (SRT), Latitude: 39.493°N, Longitude: 9.245°E, ESA|
|**In space**|200|Space, Venus and Mars (average)|
| |300|Near the Earth (average)|
| |400|Surface of Venus (average)|
| |450|Space, min.|
| |500|Space, max.|



## Varieties
*Radio communication (DBK and AFS).* Included in the [spacecraft](sc.md).

| |*Company*|*Transmitters/receivers (mass, ㎏)*|
|:--|:--|:--|
|**RU**|[MOKB Mars](zz_mars_mokb.md)| |
| |[NPO IT](zz_npoit.md)|[PRIZYV-3](prizyv_3.md) (0.17)・ [PRIZYV-1](prizyv_1.md) (0.075)|
| |[LAV](zz_lav.md)|[BRK](brk_lav.md) (12)|
| |[NPP Sait](zz_sait_ltd.md)|[RU PNI](ру_пни.md) ()・ [HSXBDT](hsxbdt.md) (1.8)・ [CSXBT](csxbt.md) (0.38)|
| |[RKS](zz_rss.md)|[BA KIS](ба_кис.md) (21)|
|•|• • • • • • • • •|• • •|
|**US**|[Space Micro](space_micro.md)| |

**Manufacturers**

| | |
|:--|:--|
|**Australia**|…|
|**Canada**|[C-CORE](zz_c_core.md) — from radio beacons & ice measurement radars to satellite transponders & space‑qualified hardware.|
|**China**|…|
|**Europe**|…|
|**India**|…|
|**Israel**|…|
|**Japan**|・[Meisei](zz_meisei.md) — transmitters<br> ・[Mitsubishi](zz_mitsubishi.md) — telemetry & beacon transmitters, power amplifier, low noise amplifiers, receiver & up/down converters.<br> ・[NEC](zz_nec.md) — low noise amplifiers (LNA), converters (CONV), receivers (RCVR), solid state power amplifiers (SSPA), & modulators (MOD), command receivers (CMDRX), telemetry transmitters (TLMTX), beacon transmitters (BCNTX), GPS receivers (GPSR), & multiuse interface modules (MIM), antennas/spaceborne radars, transponders.|
|**Korea South**|・[Satrec Initiative](zz_satreci.md)|
|**Russia**|・[AvantSpace](zz_avantspace.md)<br> ・[IRZ](zz_irz.md), [NII Guskova](нии_гуськова.md) — LNA, PE<br> ・[RADIS](zz_radis.md)|
|**Saudi Arabia**|…|
|**Singapore**|…|
|**USA**|…|
|**UAE**|…|
|**Vietnam**|…|

TMP:

   1. <http://www.spacemicro.com/products/rf-and-microwave.html>
   1. Микроволновые системы <http://Mwsystems.ru>
   1. Глобальные системы <http://global-s.world/>



## Radiolink

[General radiolink calculation ❐](f/comms/radiolink_calc_full.zip)


### Frequency Reuse

**Frequency reuse (FR)** — technique for using a specified range of frequencies more than once in the same radio system so that the total capacity of the system is increased without increasing its allocated bandwidth. Frequency reuse schemes require sufficient isolation among the signals that use the same frequencies so that mutual interference among them is controlled at an acceptable level. For satellites, frequency reuse can be achieved by using **orthogonal polarization** states for transmission and/or by using satellite antenna **(spot) beams** that serve separate, non-overlapping geographic regions.

![](f/comms/frequency_reuse.png)  
*This image shows an example of frequency reuse in cellular networks (in this case 4 frequencies are used). The image is an idealised representation with perfectly hexagonal cells. Eight separate cells are shown packed one next to the other. The first cell on the top left uses frequency 1. The cells which are next to it then use frequency 2 and 3. Beyond those cells, another cell again uses frequency 1. This pattern with the same frequency never being reused by direct neighbours repeats across the diagram. The frequency reuse pattern shown is typical example for a digital cellular system (i.e. GSM). For earlier analog systems a higher reuse pattern (7 or greater) is more usual.*



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**`Бортовая аппаратура (БА):`**<br> [PDD](pdd.md)・ [Антенна](antenna.md)・ [АПС](hns.md)・ [БУ](sp.md)・ [ЗУ](ds.md)・ [Изделие](unit.md)・ [КЛЧ](clean_lvl.md)・ [ПЗР](fov.md)・ [ПО](soft.md)・ [Прототип](prototype.md)・ [Радиосвязь](comms.md)・ [СКЭ](elmsys.md)・ [ССИТД](tsdcs.md)・ [СИТ](etedp.md)・ [УГТ](trl.md)・ [ЭКБ](elc.md)・ [EMC](emc.md)|
|**`Радиосвязь:`**<br> [CCSDS](ccsds.md)・ [Антенна](antenna.md)・ [АФУ](afdev.md)・ [Битрейт](bitrate.md)・ [ВОЛП](ofts.md)・ [ДНА](дна.md)・ [Диапазоны частот](rf.md)・ [Зрение](view.md)・ [Интерферометр](interferometer.md)・ [Информация](info.md)・ [КНД](directivity.md)・ [Код Рида‑Соломона](rsco.md)・ [КПДА](antenna_ap.md)・ [КСВ](swr.md)・ [КУ](ку.md)・ [ЛКС, АОЛС, FSO](fso.md)・ [Несущий сигнал](carrwave.md)・ [ПНА, ПОНА, ПСНА](aiad.md)・ [Помехи](emi.md) (EMI, RFI)・ [Последняя миля](last_mile.md)・ [Регламент радиосвязи](rf.md)・ [СИТ](etedp.md)・ [Фидер](feeder.md) <br>• • •<br> **РФ:** [БА КИС](ба_кис.md) (21)・ [БРК](brk_lav.md) (12)・ [РУ ПНИ](ру_пни.md) ()・ [HSXBDT](hsxbdt.md) (1.8)・ [CSXBT](csxbt.md) (0.38)・ [ПРИЗЫВ-3](prizyv_3.md) (0.17) *([ПРИЗЫВ-1](prizyv_1.md) (0.075))*|

   1. Docs:
      - [General radiolink calculation ❐](f/comms/radiolink_calc_full.zip)
   1. Notable interwikies — …
   1. <https://ru.wikipedia.org/wiki/Система_передачи_информации_космического_аппарата>
   1. <https://ru.wikipedia.org/wiki/Радиосвязь>
   1. <http://www.radioscanner.ru/>
   1. <https://www.gartner.com/en/information-technology/glossary/frequency-reuse>
   1. <https://en.wikipedia.org/wiki/Cellular_network>
