# SX-MAGWR
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → **[Магнитометр](sensor.md)**

[TOC]

---

**SX‑MAGWR** — [магнитометр](sensor.md) — прибор для определения ориентации КА путём измерения характеристик магнитного поля Земли.  
*Разработчик:* [Спутникс](zz_sputnix.md). Разработано в <mark>TBD</mark> году …

| |
|:--|
|![](f/sensor/s/sx_magwr_pic1.png)|

<small>


|*Характеристика*|*[Значение](si.md) <small>SX‑MAG‑03<br> (3‑осевой магнитометр)</small>*|*[Значение](si.md) <small>SX‑WR‑01<br> (1‑осевой ДУС)</small>*|*[Значение](si.md) <small>ДУС SX‑WR‑03<br> (3‑осевой)</small>*|*[Значение](si.md) <small>SX‑MAGWR‑01<br> (3‑осевой ДУС и<br> 3‑осевой магнитометр)</small>*|
|:--|:--|:--|:--|:--|
|Всего измерителей| |3‑x Магнитометр|1‑x ДУС|3‑x ДУС|3‑x ДУС<br> 3‑x Магнитометр|
|Исполнение| | | | | |
|Магнитное поле: диапазон измерений, нТл|± 200 000|—|—|± 200 000|
|Магнитное поле: дискретность измерений, нТл|6.67|—|—|6.67|
|Магнитное поле: случайное отклонение (шум), нТл|± 100|—|—|± 100|
|Передаваемая телеметрия|<small>Проекции вектора магнитного поля, проекции вектора угловой скорости, температура каждого измерителя.</small>|<small>Проекции вектора магнитного поля, проекции вектора угловой скорости, температура каждого измерителя.</small>|<small>Проекции вектора магнитного поля, проекции вектора угловой скорости, температура каждого измерителя.</small>|<small>Проекции вектора магнитного поля, проекции вектора угловой скорости, температура каждого измерителя.</small>|
|Угл. скорость: диапазон измерения, °/c|—|± 250|± 250|± 250|
|Угл. скорость: дискретность измерений, °/c|—|0.0005|0.0005|0.0005|
|Угл. скорость: кол‑во осей измерения|—|1|3|3|
|Угл. скорость: случайное отклонение (шум), °/c|—|± 0.005|± 0.005|± 0.005|
|**Etc:**|• • •| | | |
|[Reliability](qm.md)/[lifetime](lifetime.md)| | | | |
|Габариты, Д×Ш×В, мм|34 × 38 × 25|34 × 38 × 25|34 × 38 × 66|34 × 38 × 66|
|Interfaces|CAN2B или SpaceWire|CAN2B или SpaceWire|CAN2B или SpaceWire|CAN2B или SpaceWire|
|Масса, кг|0.06|0.06|0.09|0.1|
|[Напряжение](voltage.md), В|5 и 12|5 и 12|5 и 12|5 и 12|
|Overload, g| | | | |
|[Радстойкость](ion_rad.md), Гр (рад)| | | | |
|Ресурс, ч (лет)| | | | |
|[Lifetime](lifetime.md), h (y)| | | | |
|[Тепловой режим](tcs.md)|от –40 до +60 ℃|от –40 до +60 ℃|от –40 до +60 ℃|от –40 до +60 ℃|
|Эл. потребление, W|0.6|0.6|1.2|1.5|

</small>



<p style="page-break-after:always"> </p>

## Примечания
   1. …



## Применяемость
   1. …



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**`Магнитометр:`**<br> … <br>• • •<br> **РФ:** [SX-MAGWR](sx_magwr.md) (100)|

   1. Docs:
      - [Чертёж и основные характеристики ❐](f/sensor/s/sx_magwr_sputnix_ru.pdf)
   1. Notable interwikies — …
   1. <…>
