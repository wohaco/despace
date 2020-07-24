# SpaceID
> 2019.10.23 **[🚀](../index/index.md) [despace](index.md)** → **[Project](project.md)**

[TOC]

---
> <small>*Термины:* **Идентификатор космического объекта** — русскоязычный термин. **Space ID** — англоязычный эквивалент.</small>

**Идентификатор космического объекта** — общий термин для существующих каталожных номеров космических объектов (космических аппаратов, планет, метеоритов и пр.).



<p style="page-break-after:always"> </p>

## COSPAR ID, NSSDC ID, Номер полёта
> <small>*Термины:* **Номер полёта** — русскоязычный термин. **International designator / COSPAR ID / NSSDC ID** — англоязычный эквивалент.</small>

**Номер полёта** (англ. *International designator* — международный идентификатор, сокращённо **NSSDC ID** — номер по каталогу Национального центра анализа данных космических исследований США (англ. National Space Science Data Center, сокр. NSSDC) представляет собой каталожный номер каждого летающего космического объекта, находящегося на орбите и зарегистрированного в [COSPAR](cospar.md).

Понятие «летающего объекта» трактуется довольно свободно и включает также все объекты, появившиеся в результате старта какой‑либо ракеты и самостоятельно находящиеся на орбите. Всякие летающие объекты могут служить источником помех при астрономических наблюдениях. Чтобы исключить подобные помехи, параметры орбит таких объектов должны быть известны в гражданской астрономии. Подобная информация не могла быть почерпнута из национальных каталогов стран во время холодной войны. По этой же причине суборбитальные старты не получали номера полёта.

The **International Designator**, also known as COSPAR ID, and NSSDC ID, is an international identifier assigned to man‑made objects in space. It consists of the launch year, a three‑digit incrementing launch number of that year and up to a three‑letter code representing the sequential identifier of a piece in a launch. In TLE format the first two digits of the year and the dash are dropped.

For example, **1990-037A** is the Space Shuttle Discovery on mission STS-31, which carried the Hubble Space Telescope (**1990-037B**) into space. This launch was the 37th known successful launch worldwide in 1990.



### Описание
Согласно астрономической научной традиции любое новое небесное тело после 1957 года получало имя, состоящее из номера года и одной буквы греческого алфавита. С целью отождествления множественных объектов после буквы добавлялась одна цифра. Например, первый искусственный спутник Земли имеет обозначение 1957 α 2 (номер 1 получила вторая ступень ракеты‑носителя, также вышедшая на орбиту и имеющая гораздо большие размеры, чем спутник). Начиная с 1961 года, двадцати четырёх букв греческого алфавита стало не хватать, и для обозначения стали использовать две буквы.

В 1963 году перешли к обозначению, использующемуся и сегодня — год‑порядковый номер (двух‑ или трехзначный) и буквенный индекс — так называемый NSSDC ID. Буквенный индекс присваивается согласно кажущейся значимости объекта. Поскольку в настоящее время известна практически вся информация о полезной нагрузке ракет, то индексами A и далее обозначаются спутники, и лишь затем ступени ракет и прочие части. По состоянию на 2008 год в каталоге находилась информация о почти 6 500 объектах.

Альтернативной системой обозначения искусственных спутников является **номер по спутниковому каталогу (SCN)**.

The designation system has been generally known as the COSPAR system, named for the [Committee on Space Research (COSPAR)](cospar.md) of the International Council for Science. COSPAR subsumed the first designation system, devised at Harvard University in 1958. That system used letters of the Greek alphabet to designate artificial satellites. For example, Sputnik 1 was designated 1957 Alpha 2. The Harvard designation system continued to be used for satellites launched up to the end of 1962, when it was replaced with the modern system. The first satellite to receive a new‑format designator was Luna E-6 No.2, 1963-001B, although some sources, including the NSSDC website, anachronistically apply the new‑format designators to older satellites, even those no longer in orbit at the time of its introduction.

Designators are assigned to objects by USSTRATCOM along with satellite catalog numbers as they are discovered in space. The United Nations Office for Outer Space Affairs (UNOOSA) and the National Space Science Data Center (NSSDC), part of NASA, maintain two catalogs that provide additional information on the launchers and payloads associated with the designators. Spacecraft which do not complete an orbit of the Earth, for example launches which fail to achieve orbit, are not assigned IDs.



### Краткий список

   - 2010-020D — [Akatsuki](akatsuki.md) (2010)
   - 2005-045A — [Venus Express](venus_express.md) (2005)



<p style="page-break-after:always"> </p>

## SCN, Номер по спутниковому каталогу
> <small>*Термины:* **Номер по спутниковому каталогу** — русскоязычный термин. **Satellite Catalog Number (SCN)** — англоязычный эквивалент.</small>

**Номер по спутниковому каталогу** *(англ. Satellite Catalog Number, SCN, ранее также номер НОРАД или номер объекта USSPACECOM)* представляет собой уникальный пятизначный идентификационный номер искусственных спутников Земли.

The **Satellite Catalog Number** (also known as **NORAD Catalog Number, NORAD ID, NASA catalog number, USSPACECOM object number** or simply **catalog number** and similar variants) is a sequential five‑digit number assigned by USSTRATCOM (United States Strategic Command) in order of discovery to all man‑made objects in Earth orbit (including rocket bodies and debris) and space probes launched from Earth. The first catalogued object, catalog number 00001, is the Sputnik 1 launch vehicle, with the Sputnik 1 satellite assigned catalog number 00002.



### Описание
Первоначально каталог составлялся командованием воздушно‑космической обороны Северной Америки (NORAD). Затем пополнялся стратегическим командованием США (USSPACECOM).

В каталог заносятся параметры орбит объектов в виде двустрочных элементов (TLE). В каталоге отсутствуют данные о секретных военных спутниках США. По состоянию на 2008 год в каталоге насчитывалось до 900 активных спутников, около 400 из которых находились на [ГСО](nnb.md).

Открытая часть каталога содержит данные о почти 12 800 объектах на земной орбите, размеры которых превышают 10 см. Среди них около 8 130 частей разрушенных спутников, отработанных ступеней ракет и предметов, потерянных во время работ в открытом космосе (по состоянию на март 2009). Количество объектов размером более 1 см оценивается в 600 000.

Альтернативной системой нумерации спутников является **номер полёта (NSSDC ID)**.

Objects that fail to orbit or orbit for a short time are not catalogued. The minimum object size in the catalog is 10 centimeters in diameter. As of June 23, 2019, the catalog listed 44 336 objects including 8 558 satellites launched into orbit since 1957. 17 480 of them were actively tracked while 1 335 were lost. [ESA](zz_esa.md) estimates there are about 34 000 orbiting debris of the size USSTRATCOM is capable to track as of January 2019.

USSTRATCOM shares the catalog via <http://space-track.org> website. 18th Space Control Squadron (18 SPCS) is the unit that maintains the catalog.

**History**  
Initially the catalog was maintained by NORAD but starting from 1985 USSPACECOM (United States Space Command) was tasked to detect, track, identify, and maintain a catalog of all man‑made objects in Earth orbit. In 2002 USSPACECOM was merged with USSTRATCOM.



### Краткий список

   - 36576 — [Akatsuki](akatsuki.md) (2010)
   - 28901 — [Venus Express](venus_express.md) (2005)



<p style="page-break-after:always"> </p>

## TLE
**TLE** (аббр. от англ. **t**wo-**l**ine **e**lement set, двухстрочный набор элементов) — двухстрочный формат данных, представляющий собой набор элементов орбиты для спутника Земли.

Формат TLE был определен группировкой NORAD и, соответственно, используется в NORAD, NASA и других системах, которые используют данные группировки NORAD для определения положения интересующих космических объектов.

Модель SGP4/SDP4/SDP8 может использовать формат TLE для вычисления точного положения спутника в определенное время.

Орбитальные элементы определяются для многих тысяч космических объектов из базы данных NORAD и свободно распространяются для дальнейшего использования в Интернете. TLE всегда состоит из двух строк форматированного текста. Кроме того, им может предшествовать строка с названием объекта.

**Формат данных**

Ниже приведен пример TLE для одного из модулей Международной космической станции, обычно считающихся элементами станции.

ISS (ZARYA)  
1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927  
2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|…°·•¹²³±×÷≤≥≈≠ ‑ −— ⎆✉ ❐“”’«»✔→✘☐☑├┕┆ 1 lb = 0.453592 kg; 1 g = 9.80665 m/s²|
|:--|
|<small>**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Project](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[R&D](rnd.md)**·НИОКР, **[SRRQ](srrq.md)**·БКНР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Планетоход, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодром, **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ</small>|
|*Sections & pages*|
|**··• [](.md) •··**<br> <mark>NOCAT</mark> |

   1. Docs: …
   - Номер полёта:
      1. <https://ru.wikipedia.org/wiki/NSSDC_ID>
      1. <https://en.wikipedia.org/wiki/International_Designator>
      1. <http://www.unoosa.org/oosa/en/SORegister/regist.html> — UNOOSA: Регистр ООН
      1. <http://www.planet4589.org/space/un/un.html> — Зеркало регистра ООН с комментариями Джонатана Макдауелла (Jonathan’s Space Report)
      1. <http://nssdc.gsfc.nasa.gov/nmc/> — NSSDC Master Catalog
      1. <http://www.space-track.org/> — USSTRATCOM Space-Track
      1. <http://celestrak.com/> — CelesTrak (a partial copy of Space-Track.org catalog)
   - Номер по спутниковому каталогу:
      1. <https://ru.wikipedia.org/wiki/Номер_по_спутниковому_каталогу>
      1. <http://celestrak.com/NORAD/elements/>
      1. <http://space-track.org>
   - TLE:
      1. <https://ru.wikipedia.org/wiki/TLE>
