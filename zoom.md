# Zoom
> 2020.04.16 [🚀](../index/index.md) [despace](index.md) → **[Soft](soft.md)**

[TOC]

---

> <small>**Zoom** — EN term. **Zoom** — RU analogue.</small>

**Zoom Video Communications, Inc.**, otherwise known as **Zoom**, is an American communications technology company headquartered in San Jose, California, founded in 2011. It provides videotelephony and online chat services through a cloud‑based and peer‑to‑peer software platform and is used for teleconferencing, telecommuting, distance education, and social relations. It has been noted to be more reliable and easier to use than competing software.



## Description
Use of the platform is free for video conferences of up to 100 participants, with a 40‑minute time limit. For longer or larger conferences with more features, paid subscriptions are available, costing $ 15 ‑ 20 per month.

Its software products have faced public and media scrutiny related to poor information privacy practices and computer security vulnerabilities.

### Сквозное шифрование в системе видеоконференции Zoom оказалось фикцией
01.04.2020 13:50 <https://www.opennet.ru/opennews/art.shtml?:num=52652>

Заявленная сервисом видеоконференций Zoom поддержка сквозного (end‑to‑end) шифрования оказалась маркетинговой уловкой. На деле управляющая информация передавалась с использованием обычного TLS‑шифрования между клиентом и сервером (как при использовании HTTPS), а транслируемый по UDP поток с видео и звуком шифровался при помощи симметричного шифра AES 256, ключ для которого передавался в рамках сеанса TLS.

Оконечное шифрование подразумевает шифрование и расшифровку на стороне клиента, так что на сервер поступают уже зашифрованные данные, которые может расшифровать только клиент. В случае Zoom шифрование применялось для канала связи, а на сервере данные обрабатывались в открытом виде и сотрудники Zoom могли получить доступ к передаваемым данным. Представители Zoom пояснили, что под end‑to‑end шифрованием подразумевали шифрование трафика, передаваемого между своими серверами.

Кроме того, Zoom уличили в нарушении законодательства Калифорнии в отношении обработки конфиденциальных данных — приложение Zoom для iOS передавало данные аналитики в Facebook, даже если пользователь не использовал учётную запись в Facebook для подключения к Zoom. Сквозное шифрование преподносилось как одна из ключевых возможностей Zoom, что способствовало росту популярности сервиса.



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Software](soft.md) •··**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](c.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [PDF](pdf.md)・ [Python](python.md)・ [R](r.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](systems_tool_kit.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Zoom_Video_Communications>
