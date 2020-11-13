# Not invented here
> 2020.03.18 [🚀](../index/index.md) [despace](index.md) → **[Research](project.md.md)**

[TOC]

---

> <small>*Terms:* **Not invented here (NIH)** — English term. **Синдром неприятия чужой разработки** — Russian equivalent.</small>

**Not invented here (NIH)** is a stance adopted by social, corporate, or institutional cultures that avoids using or buying already existing products, research, standards, or knowledge because of their external origins and costs, such as royalties. Research illustrates a strong bias against ideas from the outside.

**Синдром неприятия чужой разработки** (NIH‑синдром от англ. not invented here — изобретено не нами) — позиция в социальной, корпоративной или организационной культурах, при которой избегается использование или покупка уже существующих разработок, исследований, стандартов или знаний из‑за их внешнего происхождения и затрат.



<p style="page-break-after:always"> </p>

## Description
The reasons for not wanting to use the work of others are varied, but some can include a desire to support a local economy instead of paying royalties to a foreign license‑holder, fear of patent infringement, lack of understanding of the foreign work, an unwillingness to acknowledge or value the work of others, jealousy, belief perseverance, or forming part of a wider turf war. As a social phenomenon, this tendency can manifest itself as an unwillingness to adopt an idea or product because it originates from another culture, a form of tribalism.

The term is normally used in a pejorative sense. The opposite predisposition is sometimes called "proudly found elsewhere" (PFE) or "invented elsewhere".

**In computing**

In programming, it is also common to refer to the "NIH syndrome" as the tendency towards reinventing the wheel (reimplementing something that is already available) based on the belief that in‑house developments are inherently better suited, more secure, more controlled, quicker to develop, and incur lower overall cost (incl. maintenance cost) than using existing implementations.

In some cases, software with the same functionality as an existing one is re‑implemented just to allow the use of a different software license. One approach to doing so is clean room design.



<p style="page-break-after:always"> </p>

## Описание
Причины для нежелающих использовать труд других разнообразны, среди них — страх перед нарушением патентного права, непонимание чужой работы, нежелание признать или оценить труд других, ревность или как часть более широкой «войны за территорию». Как социальное явление, эта философия проявляется нежеланием принять идею или продукт, потому что тот происходит из другой культуры, форма трайбализма.

Термин обычно используется в уничижительном смысле. Противоположные крайности называют PFE‑синдромом (англ. proudly found elsewhere — «с гордостью найдено в другом месте») и позицию «изобретено здесь».

**В информатике**

В программировании также часто ссылаются на NIH‑синдром как на тенденцию «заново изобретать колесо» (повторно то, что уже имеется; «изобретать велосипед»), основываясь на убеждении, что домашняя разработка по своей природе более приспособленная, более безопасная, более контролируемая, быстрее разрабатывается и претерпевает меньше общих расходов (включая эксплуатационные расходы), чем использование существующих реализаций.

В некоторых случаях программное обеспечение, с той же функциональностью уже существующее, повторно реализуется, просто чтобы сделать возможным его использование под другой лицензией. Один из таких подходов — метод чистой комнаты.

Основные доводы в пользу подхода NIH:

   - сторонние компоненты или услуги иногда не оправдывают ожиданий, когда требуется высокое качество;
   - сущность, находящаяся вне собственного контроля, будет привязана к поставщику и несёт постоянную угрозу для бизнеса пропорционально последствиям её потери;
   - закрытые решения могут быть восприняты как недостаточно гибкие в будущем.

При этом недостатки использования сторонней разработки могут быть нивелированы за счёт принятия внешнего решения лишь в качестве базы с последующей собственной доработкой, нежели использование его как есть, а также при обеспечении контроля над внешней сущностью в случае потери канала его поставки, например, через получение её исходного кода.



### С lurkmore
**Фатальный недостаток** — локальный мем айтишной тусовки. Вкратце означает, что кто-то от нежелания платить за авторские права, ЧСВ, зависти, скуки (или просто выгнали) решает сделать что-то своё, только с блекджеком и шлюхами. Как правило, в результате очередное унылое творение тихо загибается в гордом одиночестве.

**Происхождение мема**

> История программных революций от Microsoft, вкратце: Сначала были Windows API и DLL Hell. Революцией №1 было DDE — помните, как ссылки позволили нам создавать статусные строки, отражающие текущую цену акций Microsoft?: Примерно тогда же Microsoft создала ресурс VERSION INFO, исключающий DLL Hell. Но другая группа в Microsoft нашла в DDE **фатальный недостаток** — его писали не они! Для решения этой проблемы они создали OLE (похожее на DDE, но другое), и я наивно вспоминаю докладчика на Microsoft‑овской конференции, говорящего, что скоро Windows API перепишут как OLE API, и каждый элемент на экране будет ОСХ‑ом. В OLE появились интерфейсы, исключающие DLL Hell. Помните болезнь с названием «по месту», при которой мы мечтали встроить все свои приложения в один (возможно, очень большой) документ Word?: Где‑то в то же время Microsoft уверовала в религию С++, возникла MFC решившая все наши проблемы еще раз. Но OLE не собиралась сложа руки смотреть на это, поэтому оно заново родилось под именем COM, и мы внезапно поняли, что OLE (или это было DDE?:) будет всегда — и даже включает тщательно разработанную систему версий компонентов, исключающую DLL Hell. В это время группа отступников внутри Microsoft обнаружила в MFC **фатальный недостаток** — его писали не они! Они немедленно исправили этот недочет, создав ATL, который как MFC, но другой, и попытались спрятать все замечательные вещи, которым так упорно старалась обучить нас группа COM. Это заставило группу COM (или это было OLE?:) переименоваться в ActiveX и выпустить около тонны новых интерфейсов (включая интерфейсы контроля версий, исключающие DLL Hell), а заодно возможность сделать весь код загружаемым через броузеры, прямо вместе с определяемыми пользователем вирусами (назло этим гадам из ATL!). Группа операционных систем громким криком, как забытый средний ребенок, потребовала внимания, сказав, что нам следует готовиться к Cairo, некой таинственной хреновине, которую никогда не могли даже толком описать, не то, что выпустить. К их чести, следует сказать, что они таки представили концепцию «System File Protection», исключающую DLL Hell. Но тут некая группа в Microsoft нашла **фатальный недостаток** в Java — её писали не они! Это было исправлено созданием то ли J, то ли Jole, а может, и ActiveJ (если честно, я просто не помню), точно такого же как Java, но другого. Это было круто, но Sun засудило Microsoft по какому‑то дряхлому закону. Это была явная попытка задушить право Microsoft выпускать такие же продукты, как у других, но другие. Помните менеджера по J/Jole/ActiveJ, стучащего по столу туфлей и говорящего, что Microsoft никогда не бросит этот продукт?: Глупец! Все это означало только одно — недостаток внимания к группе ActiveX (или это был COM?:). Эта невероятно жизнерадостная толпа вернулась с COM+ и MTS наперевес (может, это стоило назвать ActiveX+?:). Непонятно почему к MTS не приставили «COM» или «Active» или «X» или «+» — они меня просто потрясли этим! Они также грозились добавить + ко всем модным тогда выражениям. Примерно тогда же кое‑кто начал вопить про «Windows DNA» (почему не DINA) и «Windows Washboard», и вопил некоторое время, но все это почило раньше, чем все поняли, что это было. К этому моменту Microsoft уже несколько лет с нарастающей тревогой наблюдала за интернет. Недавно они пришли к пониманию, что у Интернет есть **фатальный недостаток**: ну, вы поняли. И это приводит нас к текущему моменту и технологии .NET (произносится как «doughnut (пончик по‑нашему)», но по‑другому), похожей на Интернет, но с большим количеством пресс‑релизов. Главное, что нужно очень четко понимать — .NET исключает DLL Hell. В .NET входит новый язык, C#, (выясняется, что в Active++ Jspresso был **фатальный недостаток**, от которого он и помер). .NET включает виртуальную машину, которую будут использовать все языки (видимо, из‑за фатальных недостатков в процессорах Интел). .NET включает единую систему защиты (есть всё‑таки **фатальный недостаток** в хранении паролей не на серверах Microsoft). Реально проще перечислить вещи, которых .NET не включает. .NET наверняка революционно изменит Windows‑программирование… примерно на год.



<p style="page-break-after:always"> </p>

## Docs & links (TRANSLATEME ALREADY)
|Navigation|
|:--|
|<small>**[FAQ](faq.md)**, **[Cable](cable.md)**·БКС, **[Camera](cam.md)**·Камера, **[Comms](comms.md)**·Радио, **[Contact](contact.md)**·Контакт, **[Control](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Doppler](doppler.md)**·ИСР, **[DS](ds.md)**·ЗУ, **[EB](eb.md)**·ХИТ, **[ECO](ecology.md)**·Экол., **[EF](ef.md)**·ВВФ, **[ElC](elc.md)**·ЭКБ, **[EMC](emc.md)**·ЭМС, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[Fuel](fuel.md)**·Топливо, **[GNC](gnc.md)**·БКУ, **[GS](scs.md)**·НС, **[HF&E](hfe.md)**·Эрго., **[IU](iu.md)**·Гиро., **[KT](kt.md)**·КТЕХ, **[LAG](lag.md)**·ПУC, **[LES](les.md)**·САСП, **[LS](ls.md)**·СЖО, **[LV](lv.md)**·РН, **[MCC](mcc.md)**·ЦУП, **[Model](model.md)**·Модель, **[MSC](sc.md)**·ПКА, **[N&B](nnb.md)**·БНО, **[NR](nr.md)**·ЯР, **[OBC](obc.md)**·ЦВМ, **[OE](oe.md)**·БА, **[Pat.](патент.md)**·Патент, **[Project](project.md)**·Проект, **[PS](ps.md)**·ДУ, **[R&D](rnd.md)**·НИОКР, **[SRRQ](srrq.md)**·БКНР, **[Robot](robotics.md)**·Робот, **[Rover](rover.md)**·Планетоход, **[RTG](rtg.md)**·РИТЭГ, **[SARC](sarc.md)**·ПСК, **[Sensor](sensor.md)**·Датчик, **[SC](sc.md)**·КА, **[SCS](scs.md)**·КК, **[SGM](sgm.md)**·КММ, **[SI](si.md)**·СИ, **[Soft](soft.md)**·ПО, **[SP](sp.md)**·БС, **[Spaceport](spaceport.md)**·Космодром, **[SPS](sps.md)**·СЭС, **[SSS](sss.md)**·ГЗУ, **[TCS](tcs.md)**·СОТР, **[Test](test.md)**·ЭО, **[Timeline](timeline.md)**·ЦГМ, **[TMS](tms.md)**·ТМС, **[TOR](tor.md)**·ТЗ, **[TRL](trl.md)**·УГТ</small>|
|*Sections & pages*|
|**··• [Project](project.md) •··**<br> [Interferometer](interferometer.md) ┊ [NASA open](nasa_open.md) ┊ [NASA STI](nasa_sti.md) ┊ [NIH](nih.md) ┊ [Past, future and everything](pfaeverything.md) ┊ [PSDS](us_psds.md) [MGSC](mgsc.md) ┊ [Raman spectroscopy](raman_spsc.md) ┊ [SC price](sc_price.md) ┊ [SC typical forms](sc_ts.md) ┊ [Tech derivative laws](td_laws.md) ┊ [View](view.md) ┊ [XRF](xrf.md)|

   1. Docs: …
   1. Notable interwikies — …
   1. <https://en.wikipedia.org/wiki/Not_invented_here>
   1. <https://ru.wikipedia.org/wiki/Синдром_неприятия_чужой_разработки>

