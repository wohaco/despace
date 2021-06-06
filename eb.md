# Electric battery
> 2019.05.12 [🚀](../index/index.md) [despace](index.md) → [EB](eb.md), [SPS](sps.md)

[TOC]

---

> <small>**Chemical source of electricity (CSE), Electric battery (EB), Primary cell (PC)** — EN term. **Химический источник тока (ХИТ)** — RU analogue.</small>

**Chemical source of electricity (CSE), Electric battery (EB)** — a source of electromotive force (EMF), in which the energy of chemical reactions taking place in it is directly converted into electrical energy.

Subdivided into:

   - **galvanic cells** (primary EB), which, due to the irreversibility of the reactions occurring in them, cannot be recharged.
   - **electric batteries** (secondary EB), they are **rechargeable batteries (RB)** — rechargeable galvanic cells that can be recharged using an external current source (charger);
   - **fuel cells** (electrochemical generators) — devices similar to a galvanic cell, but differing from it in that substances for an electrochemical reaction are supplied to it from the outside, and reaction products are removed from it, which allows it to function continuously:
      - direct methanol fuel cell;
      - solid oxide fuel cell;
      - alkaline fuel cell.

The division of cells into galvanic and accumulators is somewhat arbitrary, since some galvanic cells, for example alkaline batteries, can be recharged, but the efficiency of this process is extremely low.



## Varieties

|*°*|*[Company](contact.md)*|*Actual (capacity, Ah)*|
|:--|:--|:--|
|**EU**|[Saft](zz_saft.md)|[8S8P](8s8p.md) (30)|
|•|• • • • • • • • •|• • •|
|**JP**|[GS Yuasa](zz_gs_yuasa.md)|EB cells|
| |[Mitsubishi Electric](zz_mitsubishi.md)|Assembly|
|•|• • • • • • • • •|• • •|
|**RU**| [VNIIEM](zz_vniiem.md) | |
| | [Orion‑Hit](zz_orion_hit.md) | |
| | [PAO Saturn](pao_saturn.md) | [8LI‑70](8li_70.md) (70) ┊ [12LI‑120](12li_120.md) (120) |

**Comparison.**

|*Type of sealed battery*|*Vol&shy;tage,<br> V*|*Spec. <br> energy <br> (mass), <br> Wh / ㎏*|*Specific<br> energy <br> (volume), <br> Wh / dm³*|*Self-<br> discharge <br> per day, <br>%*|*[Output]( charge_eff.md), <br>%*|*Service<br> life,<br> years / <br> cycles*|*Temp., <br> ℃*|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
|**Lithium-Iron-Phosphate** <br> (LiFePO₄, or LFP) | 3.3 | 90‑130 | 320‑400 | 0.16 | 90 | 15 / 2 000 <br> 15 / 7 000 | −30 ‑ +55 |
|**Lithium-Ion**| 3.6 | 130 | 260 | 15 (28) | 98 | 5 / 500 |−… ‑ +… |
|**Lithium-Ion** <br> (SIS, silicon) | | | | | |… / … | −… ‑ +300 |
|**Lithium-Cobalt** <br> (LiCoO₂, or LCO) | 3.6 | 200 | 560 | | |… / 1 000 | −… ‑ +… |
|**Lithium-Manganese** <br> (LiMn₂O₄, or LMO) | 3.7 | 150 | 420 | | 90 |… / 700 | −… ‑ +… |
|**Lithium-Metallic**| | | | | |… / ┊ | −… ‑ +… |
|**Lithium-Nickel-Cobalt-Aluminum-Oxide** <br> (LiNiCoAlO₂, or NCA) | 3.6 | 260 | 600 | | |… / 500 | −… ‑ +… |
|**Lithium-Nickel-Manganese-Cobalt** <br> (LiNiMnCoO₂, or NMC) | 3.7 | 220 | | | |… / 2 000 | −… ‑ +… |
|**Lithium-Sulfur** <br> (LiS) | 2.1 | 500 | 350 | | |… / 1400 | −… ‑ +… |
|**Lithium-Thionyl-Chloride** <br> (Li ‑ SOCl₂) | 3.6 | 37 | | 0.002 7 | |… /… <br>… / ┊ | −40 ‑ +145 |
|**Lithium-Titanate** <br> (Li₄Ti₅O₁₂, or SCiB / LTO) | 2.4 | 60‑110 | 177 | | 85‑90 | 10 / 6 000 <br> 20 / 20 000 | −… ‑ +… |
|•••|•••|•••|•••|•••|•••|•••|•••|
|**Nickel-Hydrogen** <br> (NiH₂) | 1.25 | 50‑55 | 100‑120 | 40 (3) | 90‑92 | 7 / 1 000 | −… ‑ +… |
|**Nickel-Cadmium** <br> (NiCd) | 1.2 | 40‑45 | 80‑100 | 20 (28) | 72 | 5 / 500 | −… ‑ +… |
|**Nickel-Metal Hydride** <br> (NiMH) | 1.25 | 60‑75 | 180‑200 | 20 (28) | 96‑98 | 5 / 500 | −… ‑ +… |
|•••|•••|•••|•••|•••|•••|•••|•••|
|**Sulfur-Magnesium**| | 1 720 | | | |… / 110 | −… ‑ +… |

Comparison of rechargeable and disposable batteries

| |*disposable (70Ah)*|*rechargeable 8LI‑70 (70Ah)*|
|:--|:--|:--|
|**Weight, ㎏**| 15.5 | 18.8 |
|**Dimensions, ㎜**| 328 × 342 × 150 | 268 × 232 × 270 |



## Notes

### Converting Ah to Wh
Often battery manufacturers indicate in the technical specifications only the stored charge in mAh (mAh), others — only the stored energy in Wh (Wh). Both characteristics can be called “capacity” (not to be confused with electrical capacity as a measure of a conductor's ability to store a charge, measured in farads). In general, it is not easy to calculate the stored energy from the stored charge: it is required to integrate the instantaneous power delivered by the battery during the entire discharge time. If greater accuracy is not needed, instead of integration, you can use the average values ​​of voltage and current consumption and use the formula following from the fact that  
`1W = 1V × 1A` and `1Wh = 1V × 1Ah`

That is, the stored energy (Wh) is approximately equal to the product of the stored charge (VAh) by the average voltage (in Volts):  
`E = q × U`

**Example**  
The technical specification of the device indicates that the “capacity” (stored charge) of the battery is 56 Ah, the operating voltage is 15 V. Then the “capacity” (stored energy) is: 56 × 15 = 840 Wh (≈3 MJ)  
When the batteries are connected in series, the “capacity” remains the same, when connected in parallel, it is added.  
3.3v 1 000 mAh + 3.3v 1 000 mAh = 6.6v 1 000 mAh — serial connection.  
3.3v 1 000 mAh + 3.3v 1 000 mAh = 3.3v 2 000 mAh — parallel connection.



### Calculating battery capacity
Produced according to the formula:  
**Battery capacity (Ah) = load power (kW) × time (h) × 100**



### Some types of EB

**Galvanic cell** — a chemical source of electrical current named after Luigi Galvani. The principle of operation of a galvanic cell is based on the interaction of two metals through an electrolyte, leading to the emergence of an electric current in a closed circuit.

|*Type*|*Cathode*|*Electrolyte*|*Anode*|*Voltage, V*|
|:--|:--|:--|:--|:--|
| Manganese-Magnesium element | MnO₂ | MgBr₂ | Mg | 2.00 |
| Manganese-Tin element | MnO₂ | KOH | Sn | 1.65 |
| Manganese-Zinc element | MnO₂ | KOH | Zn | 1.56 |
| Oxide-Mercury-Tin element | HgO₂ | KOH | Sn | 1.30 |
| Mercury-Cadmium element | HgO₂ | KOH | Cd | 1.92 |
| Mercury-Zinc element | HgO | KOH | Zn | 1.36 |
| Lead-Cadmium cell | PbO₂ | H₂SO₄ | Cd | 2.42 |
| Lead-Chlorine element | PbO₂ | HClO₄ | Pb | 1.92 |
| Lead-Cinc cell | PbO₂ | H₂SO₄ | Zn | 2.55 |
| Chromium-Zinc element | K₂Cr₂O₇ | H₂SO₄ | Zn | 1.8 ‑ 1.9 |

   - Bromine-Silver element
   - Bismuth-Magnesium element
   - Dioxysulfate-Mercury element
   - Zinc Iodate element
   - Iodine-Silver element
   - Calcium chromate element
   - Lithium bismuth cell
   - Lithium-dioxide-Sulfur cell
   - Lithium Iodine Cell
   - Lithium-Iodine-lead cell
   - Lithium-Copper oxide cell
   - Lithium Vanadium Oxide Cell
   - Lithium-Thionyl chloride cell
   - Lithium-Fluoride cell
   - Lithium-Chrome silver cell
   - Magnesium vanadium element
   - Magnesium-M‑DNB element
   - Magnesium perchlorate element
   - Copper oxide galvanic cell
   - Mercury-Bismuth-Indium element
   - Lead-Fluoric element
   - Sulfur-Magnesium element
   - Chlorine-Silver element
   - Chloride-Copper-Magnesium element
   - Lead chloride-Magnesium element
   - Silver chloride-Magnesium element
   - Zinc-Silver chloride element

**Electric accumulator**, also **accumulator battery (AB)** is a reusable chemical current source (that is, unlike a galvanic cell, chemical reactions directly converted into electrical energy are reversible many times). Electric accumulators are used for energy storage and autonomous power supply of various devices.

   - Iron-Air battery
   - Iron-Nickel battery
   - Lanthanum-Fluoride battery
   - Lithium-Iron-Sulfide battery
   - Li-Ion battery
   - Lithium-polymer battery
   - Lithium-Sulfur battery
   - Lithium-fluorine battery
   - Lithium-chlorine battery
   - Manganese-Tin element
   - Nickel-Cadmium battery
   - Nickel-Metal-hydride battery
   - Sodium-Nickel-chloride battery
   - Sodium Sulfur battery
   - Nickel-Zinc battery
   - Lead-Hydrogen battery
   - Lead-Acid battery
   - Lead-Tin battery
   - Silver-Cadmium battery
   - Silver-Zinc battery
   - Zinc-Bromine battery
   - Zinc-Air accumulator
   - Zinc-Chlorine accumulator



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:--|
|**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[CON](contact.md)·[Pers](person.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Proj.](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[QA](qa.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Ровер, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[SE](se.md)**·СЭ, **[Sens.](sensor.md)**·Датч., **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодр., **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ|
|*Sections & pages*|
|**··• [Spacecraft power system (SPS)](sps.md) •··**<br> [ACUER](acuer.md)┊ [Charge eff.](charge_eff.md)┊ [EB](eb.md)┊ [EMI, RFI](emi.md)┊ [NR](nr.md)┊ [Rotor](rotor.md)┊ [RTG](rtg.md)┊ [Solar cell](sp.md)┊ [SP](sp.md)┊ [SPB/USPB](suspb.md)┊ [Voltage](voltage.md)┊ [WT](wt.md)<br>• • •<br> **RF/CIF:** [BAK-01](bak_01.md)┊ [KAS‑LOA](kas_loa.md)|
|**··• [Chemical source of electricity (CSE), Electric battery (EB)](eb.md) •··**<br> [Charge efficiency](charge_eff.md) <br>• • •<br> **EU:** [8S8P](8s8p.md) (30)  ▮  **RU:** [8LI-70](8li_70.md) (70)┊ [12LI-120](12li_120.md) (120)|

   1. Docs: …
   1. Notable interwikies — …
   1. 2019.08.02 [Есть ли альтернатива литий‑ионному аккумулятору? ⎆](https://habr.com/ru/company/toshibarus/blog/462185/) — [archive ❐](f/sps/20190802_1_01.pdf) of 2019.08.04)
   1. <https://ru.wikipedia.org/wiki/Химический_источник_тока>
   1. <https://en.wikipedia.org/wiki/Rechargeable_battery>
   1. <http://niai.ru/catalog.php?:id=6>
   1. <http://at-systems.ru/quest/new-quest/capacity-count-easy-y.shtml>
   1. <https://en.wikipedia.org/wiki/Peukert’s_law>
