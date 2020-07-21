# Failures in time
> 2019.07.25 **[🚀](../index/index.md) [despace](index.md)** → **[](.md)** <mark>NOCAT</mark>

[TOC]

---

> <small>*Terms:* **Failures in time** — English term. **Вероятность безотказной работы / Отказов в единицу времени (ВБР)** — equivalent in Russian.</small>

**Failure rate** is the frequency with which an engineered system or component fails, expressed in failures per unit of time. It is usually denoted by the Greek letter λ (lambda) and is often used in reliability engineering.



## Description

The failure rate of a system usually depends on time, with the rate varying over the life cycle of the system. For example, an automobile’s failure rate in its fifth year of service may be many times greater than its failure rate during its first year of service. One does not expect to replace an exhaust pipe, overhaul the brakes, or have major transmission problems in a new vehicle.

In practice, the mean time between failures (MTBF, 1/λ) is often reported instead of the failure rate. This is valid and useful if the failure rate may be assumed constant — often used for complex units / systems, electronics — and is a general agreement in some reliability standards (Military and Aerospace). It does in this case only relate to the flat region of the bathtub curve, which is also called the “useful life period”. Because of this, it is incorrect to extrapolate MTBF to give an estimate of the service lifetime of a component, which will typically be much less than suggested by the MTBF due to the much higher failure rates in the “end-of-life wearout” part of the “bathtub curve”.

The **Failures In Time (FIT)** rate of a device is the number of failures that can be expected in one billion (10⁹) device‑hours of operation. (E.g. 1 000 devices for 1 million hours, or 1 million devices for 1 000 hours each, or some other combination.) This term is used particularly by the semiconductor industry.

The relationship of FIT to MTBF may be expressed as: `MTBF = 1 000 000 000 x 1 / FIT`.

The relationship of FIT to [ВБР](rams.md): `P(t) = 100 − (t • FIT / 1000 000 000)`, where  
t — Lifetime (h)


<br><br><br> <p style="page-break-after:always"> </p>

---

# Docs & links
|…°·•¹²³±×÷≤≥≈≠ ‑ −— ⎆✉ ❐“”’«»✔→✘☐☑├┕┆ 1 lb = 0.453592 kg; 1 g = 9.80665 m/s²|
|:--|
|<small>**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](camera.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Управ., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Errors](error.md)**·Ошибки, **[Events](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Project](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](quality.md)**·QA, **[R&D](rnd.md)**·НИОКР, **[RAMS](rams.md)**·НиБ, **[Risk](risk.md)**·Риск, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Планетоход, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодром, **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·Циклограмма, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ</small>|
|*Sections & pages*|
|**··• [](.md) •··**<br> <mark>NOCAT</mark> |

**Documents:**

   1. …

**Links:**

   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Failure_rate>
   1. <https://electronics.stackexchange.com/questions/59774/what-are-fits-and-how-they-used-in-reliability-calculations>
