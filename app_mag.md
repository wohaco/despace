# Видимая звёздная величина
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → **[ЗД](sensor.md)**, [Space](index.md)

[TOC]

---

> <small>**Видимая звёздная величина** — русскоязычный термин. **Apparent magnitude** — англоязычный эквивалент.</small>

**Видимая звёздная величина (m)** — мера яркости небесного тела (точнее, освещённости, создаваемой этим телом) с точки зрения земного наблюдателя. Обычно используют величину, скорректированную до значения, которое она имела бы при отсутствии атмосферы. Чем ярче объект, тем меньше его звёздная величина.

Уточнение «видимая» указывает только на то, что эта звёздная величина наблюдается с [Земли](earth.md); это уточнение нужно, чтобы отличить её от абсолютной. Оно не указывает на видимый диапазон: видимыми называют и величины, измеренные в инфракрасном или каком‑либо другом диапазоне. Величина, измеренная в видимом диапазоне, называется визуальной.

В [видимой части спектра](rf.md) самая яркая звезда на ночном небе — Сириус, а в инфракрасном J‑диапазоне — Бетельгейзе.



## История
|*<small>Видны<br> невооружённым<br> глазом</small>*|*<small>Видимая<br> величина</small>*|*<small>Яркость<br> относительно<br> Веги</small>*|*<small>Число звёзд<br> ярче этой<br> видимой величины</small>*|
|:--|:--|:--|:--|
|Да|−1,0|250 %|1|
|Да|0,0|100 %|4|
|Да|1,0|40 %|15|
|Да|2,0|16 %|48|
|Да|3,0|6,3 %|171|
|Да|4,0|2,5 %|513|
|Да|5,0|1,0 %|1 602|
|Да|6,0|0,40 %|4 800|
|Да|6,5|0,25 %|9 096|
|*Нет*|7,0|0,16 %|14 000|
|*Нет*|8,0|0,063 %|42 000|
|*Нет*|9,0|0,025 %|121 000|
|*Нет*|10,0|0,010 %|340 000|

Современная шкала звёздных величин берёт начало в Древней Греции. Её предложил во II веке до н.э. Гиппарх, разделив звезды, видимые невооруженным глазом, по шести величинам. Самые яркие из них он назвал звёздами первой величины (m = 1), а самые слабые — звёздами шестой величины (m = 6). Современная астрономия не ограничивается шестью величинами или только видимым светом. Очень яркие объекты имеют отрицательную величину.



## Вычисление
Видимая звёздная величина объектов 1 и 2 определяется как

`m₁ − m₂ = −2.5 · lg(L₁ / L₂)`  
где m — звёздные величины объектов, L — освещённости от этих объектов.

Таким образом, разница в 5 звёздных величин соответствует отношению освещённостей в 100 раз, а разница в одну звёздную величину — в 100<sup>1/5</sup> ≈ 2.512 раза.

**Примеры:**

Видимая звёздная величина полной Луны равна −12.7; яркость Солнца составляет −26.7.

Разница звёздных величин Луны (m₁) и Солнца (m₂):  
`m₁ − m₂ = (−12.7) − (−26.7) = 14.0`

Отношение освещённостей от Солнца и Луны:  
`L₁ / L₂ = 2.512^(m₁ − m₂) = 2.512^14.0 = 400000`

Таким образом, Солнце примерно в 400 000 раз ярче полной Луны.



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SRRQ](srrq.md)**·БКНР, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**`Звёздный датчик (ЗД):`**<br> [Видимая звёздная величина](app_mag.md)|
|**··• [Space](index.md) •··**<br> [Apparent magnitude](app_mag.md) ┊ [Astro.object](aob.md) ┊ [Blue Marble](earth.md) ┊ [Cosmic rays](cr.md) ┊ [Ecliptic](ecliptic.md) ┊ [Escape velocity](esc_vel.md) ┊ [Health](health.md) ┊ [Hill sphere](hill_sphere.md) ┊ [Information](info.md) ┊ [Lagrangian points](l_points.md) ┊ [Near space](near_space.md) ┊ [Pale Blue Dot](earth.md) ┊ [Parallax](parallax.md) ┊ [Point Nemo](earth.md) ┊ [Silver Snoopy award](silver_snoopy_award.md) ┊ [Solar constant](solar_const.md) ┊ [Terminator](terminator.md) ┊ [Time](time.md) ┊ [Wormhole](wormhole.md) ┊ ··•·· **Solar system:** [Ariel](ariel.md) ┊ [Callisto](callisto.md) ┊ [Ceres](ceres.md) ┊ [Deimos](deimos.md) ┊ [Earth](earth.md) ┊ [Enceladus](enceladus.md) ┊ [Eris](eris.md) ┊ [Europa](europa.md) ┊ [Ganymede](ganymede.md) ┊ [Haumea](haumea.md) ┊ [Iapetus](iapetus.md) ┊ [Io](io.md) ┊ [Jupiter](jupiter.md) ┊ [Makemake](makemake.md) ┊ [Mars](mars.md) ┊ [Mercury](mercury.md) ┊ [Moon](moon.md) ┊ [Neptune](neptune.md) ┊ [Nereid](nereid.md) ┊ [Nibiru](nibiru.md) ┊ [Oberon](oberon.md) ┊ [Phobos](phobos.md) ┊ [Pluto](pluto.md) ┊ [Proteus](proteus.md) ┊ [Rhea](rhea.md) ┊ [Saturn](saturn.md) ┊ [Sedna](sedna.md) ┊ [Solar day](solar_day.md) ┊ [Sun](sun.md) ┊ [Titan](titan.md) ┊ [Titania](titania.md) ┊ [Triton](triton.md) ┊ [Umbriel](umbriel.md) ┊ [Uranus](uranus.md) ┊ [Venus](venus.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Apparent_magnitude>
   1. <https://ru.wikipedia.org/wiki/Видимая_звёздная_величина>

