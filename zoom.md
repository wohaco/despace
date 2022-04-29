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
|:-|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**【[Software](soft.md)】**<br> [ASP](asp.md)・ [Blender](blender.md)・ [C](plang.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [DWG](cad_f.md)・ [GIMP](gimp.md)・ [Git](git.md)・ [IGES](cad_f.md)・ [ISIS](isis.md)・ [JT](cad_f.md)・ [NGT](neogeography_toolkit.md)・ [NX](nx.md)・ [Octave](gnu_octave.md)・ [OS](os.md)・ [PDF](pdf.md)・ [Python](plang.md)・ [R](plang.md)・ [SPICE](spice.md)・ [STEP](cad_f.md)・ [STL](stk.md)・ [SVG](cad_f.md)・ [Syncthing](syncthing.md)・ [SysML](sysml.md)・ [Teamcenter](teamcenter.md)・ [Система управления версиями](vcs.md)・ [ХРИП](adra.md)|

   1. Docs: …
   1. <https://en.wikipedia.org/wiki/Zoom_Video_Communications>
