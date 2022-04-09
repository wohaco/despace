# Common mistakes and lessons learned
> 2019.12.19 [🚀](../index/index.md) [despace](index.md) → [Качество](qm.md), **[НД](doc.md)**

[TOC]

---

> <small>**Typical mistakes** — EN term. **Типичные ошибки** — RU analogue.</small>  
>> <small>*There is never time to do it right, but there is always time to fix it.・ Errare humanum est.*</small>

An **error** (from the Latin error, meaning “wandering”) is an action which is inaccurate or incorrect. In some usages, an error is synonymous with a mistake. In statistics, “error” refers to the difference between the value which has been computed & the correct value. An error could result in failure or in a deviation from the intended performance or behavior.

Differences between an error & a mistake: an “**error**” — is a deviation from accuracy or correctness, A “**mistake**” — is an error caused by a fault: the fault being misjudgment, carelessness, or forgetfulness.

This manual contains a list of common errors in operation & [documentation](doc.md). The list is compiled based on the experience of working on various R&D projects, is almost universal & is not tied to any particular organization. Created for:

   1. reduce the cost of subsequent fixes
   1. improving the quality of work
   1. focusing on the main, not the secondary

【**Table.** Error Types by [xkcd ⎆](https://xkcd.com/2303/)】

|*#*|*Description*|
|:-|:-|
|**1**|False positive|
|**2**|False negative|
|**3**|True positive for incorrect reasons|
|**4**|True negative for incorrect reasons|
|**5**|Incorrect result which leads you to a correct conclusion due to unrelated errors|
|**6**|Correct result which you interpret wrong|
|**7**|Incorrect result which produces a cool graph|
|**8**|Incorrect result which sparks further research & the development of new tools which reveal the flaw in the original result while producing novel correct results|
|**9**|The rise of Skywalker|

【**Table.** Common mistakes, their causes & consequences】

|*#*|*Name*|*Description*|
|:-|:-|:-|
|1|**Implement an additional system for the same task**|Leads to overhead & errors when rewriting from one to another.|
|2|**Stupidity**|“There are 2 infinities — the Universe & human stupidity. I’m not sure about the universe.”|
|3|**Game “to get in the ass & get out of it heroically”**|Classic. Make the wrong decision, & then clean up the consequences with sweat & blood.|
|4|**Change what works without learning why it was done this way**|Leads to breakdowns / complications — often what looks awkward, but was done by smart people, was done that way with a reason. The Chernobyl nuclear power plant burned down precisely because of this.|
|5|**Small amount of time**|“Fast, high quality, cheap — choose any 2”. They often choose “fast, cheap”.|
|6|**Non‑working atmosphere**|Nerves, pressure, noise, calls, etc. distract, confuse thoughts, reduce concentration.|
|7|**Transfer of information by words. [Agreement](contract.md) in words**|When a person speaks, & doesn’t write on paper & doesn’t sign, then the [end‑to‑end information path](etedp.md) looks something like this: 【What I thought → What I felt → What I said → What I decided about what I said → What my opponent heard → What he/she understood → What he/she remembered】; distortion of information is possible in each transition. In the human brain there is a “center of criticism” through which incoming information passes, but not outgoing information. Thus, a person can say not what he wants, & the opponent can perceive not what he hears. Write protocols & sign them on the spot.|
|8|**Disconnection from the process, frequent switching**|…|
|9|**Make sequential processes parallel**|In common leads to a lot of risks & overhead. The whole system can fail at once because of one small piece.|
|10|**Survivor Bias**|*(ru. Систематическая ошибка выжившего)* is a type of selection bias, when there is a lot of data on one group (“survivors”), & practically none on the other (“dead”). So researchers try to look for similarities among the “survivors” & lose sight of the fact that equally important information is hidden among the “dead”. **Examples:**<br> ➀ In WW2, mathematician A. Wald from the New York SRG laboratory was instructed to find a solution to the problem: not all US bombers returned, & there were many holes on the returning ones, but they were unevenly distributed: many on the fuselage, fewer in the fuel system, & few — in the engine. So, more armor is needed in the holes? Wald replied: no, this shows that an aircraft with holes in these places can return. An aircraft that has been hit with an engine or gas tank will not be returned. Because hits in the 1st approximation are evenly distributed, it’s necessary to strengthen the places that the returnees have the most “clean”.<br> ➁ There is also an opinion about the kindness of dolphins, based on the stories of swimmers who were pushed by animals to the shore, but there is no data from those who were pushed in the opposite direction.<br> ➂ Labor safety research is complicated by the fact that workers who are not adapted to harmful conditions quickly leave (the so‑called healthy worker effect).|
|11|**[Meetings](meeting.md) with a quick decision**|Often, in meetings, decisions are made quickly without a detailed immersion in the issue. Subsequently, you have to spend resources on correcting the consequences of these decisions.|
|12|**Single‑handed decision making**|There are always those who (not)deliberately distort the facts in their personal interests. Therefore there is a scientific approach & peer review, & therefore consensus is important.|
|13|**(Not)consider everyone around as idiots**|…|
|14|**Arphagraphy, gramar**|Well, where can we go without them. MS Word can, of course, check something, but still check the document yourself. Also read fiction, improve your own literacy. |
|15|**A cursory reading of the documents**|The devil is in the details, & in a hurry you can’t see the details. And sometimes it happens that there is almost no water in the document, which can be skipped, & the written words are written for a reason.|
|16|**Duplication of information**|If some information (composition, dimensions, mass, etc.) is indicated in more than one place, then during corrections it’s often corrected in one place, & in others it’s forgotten.|
|17|**Do not do your job**|[Do not do their work for others❐](f/doc/20191106_1.pdf).|
|18|**Superfluous information**|We write technical documentation, which, firstly, is read by managers & generals who do not understand technology, & secondly, by technical specialists, who then use it to sharpen glands & carry out assembly. Therefore, there’s no need to spread thoughts along the tree — write briefly, clearly & to the point, follow the principle of [Oссams razor](dont_panic.md).|
|19|**Using both [SI](si.md) & non‑SI units**|Often, when converting one dimension to another, a size error will be made.|
|20|**Mythical “generally known information”**|What is known to everyone today may lose its relevance tomorrow. Therefore, try to refer (and it’s better to cite in the text) to generally accepted systems, constants, calculations, so that in 2, 10, 30 years you can understand how it all works & why. Some also think g = 10.|
|21|**Violation of alphabetical order**|When compiling lists of jobs, documents, employees, etc., there is a desire to sort them in non‑alphabetical order (by importance, significance, stages, etc.). This leads to the fact that, after agreeing on the document with the author of such a procedure, it’s required to explain this procedure to everyone who agrees later. And then everyone forgets the meaning of this logic & spends time looking for the right item. Alphabetical order is good for its speed & impartiality.|
|22|**Lack of numbers for documents**|“Mustache, paws & tail” of any document is the name, number & signatures. There can be many documents with this name, documents with the same name, number & number — only one.|
|23|**Absence of an explicit choice**|The choice should be spelled out clearly: “based on the results of the given study, named matters were chosen”. No conventions, proposals, references like “well, we wrote one thing in the conclusions, but in the footnotes on the hundredth page it’s written in small print that the conclusions should not be trusted.”|
|24|**Different names of the same matter**|Often, within the framework of one document/project, devices are called either by name, then by name with a prefix, then by index, then by everyday name, then somehow else. This raises questions — is it really the same device? Sometimes this is not the case & we are talking about different ones. The same applies to the names of documents, organizations, places, stages, etc.|
|25|**Links to non‑public documentation**|If there is a link to non‑public documentation (internal orders, letters, materials of other R&D, etc.), then they should be attached. There is no guarantee that they will be available to the Customer, & even more so when checked by the prosecutor in a couple of years.|
|26|**History does not tolerate the subjunctive mood**|When evaluating history, it’s wrong to say something like: “If Macedonian did not reach India, then…” history went the way it went, & the rest is unfounded speculation.|
|27|**One fool can confuse a thousand wise people**|The owner “doesn’t have to know all the technical details” & for him it’s necessary to explain that such an employee generates nonsense, for this it’s necessary to spend a lot of expensive time chewing on where these ideas are untenable. The owner sees “an employee who is actively trying to solve problems”. It ends with the fact that everyone gets tired & starts to implement this nonsense, in parallel, employees often appear at interviews with other employers. After a generation of employees has changed, the business of such an enterprise resembles a bicycle bed, which “the grave will fix” or a very robust investment in putting things in order, & then the grave.|
|28|**The judge & the prosecutor rolled into one**|Equals should discuss/decide, a third party should judge, unless the equals agree.|
|29|**Implicit/unclear expressions & judgments**|A person should not be attached to the document. Everything should be: written clearly, all numbers are available, links on the spot, etc.|
|30|**Figures without scatter**|It’s usually considered that a number (dimensions, electricity, mass, etc.) is the worst boundary, i.e. there will be no worse value. But sometimes, in case of unscrupulous/negligent work, the performers consider the indicated figure to be the face value & subsequently give tolerances for it. Demand immediately either to write tolerances, or to indicate in words that the number is the limit.|
|31|**Pointing that something can be specified later**|R&D process means that any document or unit at any stage can be specified. Actually, this is the principle of R&D — clarification through iterations, & then coordination of clarifications with stakeholders. However, in case of unfair work, such phrases in the documents lead to the fact that unreliable performers begin to demand the adoption of changes in fact. Therefore, such phrases shall be excluded from documents.|
|32|**Murphy’s Law & its variations**|If something can go wrong, it will definitely go wrong. If something can be misunderstood, then they will definitely misunderstand. If 4 variants of malfunctions were envisaged & they were eliminated, then the 5th option will certainly appear.|
|33|**(Not‑to)doubt anything**|…|
|34|**Not to use upper/lower UTF characters**|Often, when copying from document to document, superscripts & subscripts (which were obtained by lifting numbers/letters using tags) are lost, and, say, 10⁴ ㎩ turn into 104 ㎩. And it happens the other way around, when 104 ㎩ is mistaken for a mistake & is regarded as 10 ㎪.|
|35|**Not knowing or understanding the contractor**|Know the organizational structure, capabilities, goals, responsibilities, functions of the contractor, otherwise you will not be able to interact with him.|
|36|**Ignore deviation if you see it**|Even if it is not in your competence or responsibility, not informing means dooming the whole company to inefficiency or marriage. If you see a deviation — tell about it, you know how to do it or fix it — teach them how.|



<p style="page-break-after:always"> </p>

## Metrology

   - **Allowed:**
      - use only SI units; non‑SI may be indicated in brackets;
      - use international or national designations, but not simultaneously;
      - apply decreasing indices up to 10⁻³ inclusive (㎝, ㎜, ㎳, ㎃, etc.), then — only numbers;
      - apply from 10⁻¹ from 10⁻⁶ inclusive zeros after the decimal point, then — only powers of 10;
      - apply increasing indices up to 10⁹ (㎞, ㎆, ㎬), then — only the power of 10;
   - **Forbidden:**
      - abbreviate the designations of quantities, if they are used without numbers, except for quantities in the heads and sides of tables and in the decoding of letter designations included in formulas and figures. (**ignored in this DB**)
      - separate the name from the number (or transfer them to different lines/pages).
      - apply turns of colloquial speech, technicalism, professionalism; (**ignored in this DB**)
      - apply for the same concept various terms close to the meaning, foreign terms in the presence of equivalent terms in the national language;
      - apply arbitrary word formations;
      - apply abbreviations of words, except for those established by the spelling rules, the corresponding state standards;
      - In the text of the document, with the exception of formulas, tables, figures:
         - use the “−” sign (should be written with the word minus); (**ignored in this DB**)
         - use the “⌀” sign (should be written with the word diameter); (**ignored in this DB**)
         - apply without numerical values ​​mat. signs, for example, \>, \<, =, ≤, ≥, ≠, №, %. (**ignored in this DB**)


<u><big>**RU**</big></u>

【**Table.** Размерности】

|*Правильно* |*Неправильно* |*Комментарии*|
|:-|:-|:-|
|г|гр| |
|кг|Кг| |
|мин|м| |
|ч|час| |
|с|сек| |
|рад|град| |
|5 градусов или 5°|5 град| |
|10 угловых минут или 10´|10 угл. мин| |
|40 угловых секунд или 40´´|40 угл. с| |
|10 угловых градусов или 10°|10 угл. град.| |
|окт/мин|октава/мин| |
|К|°К| |
|°/s или угловой градус в секунду|град/с| |
|°/ч|град/час| |
|Па (㎏f/㎝²)|㎏f/㎝²; кГс/㎝²; ㎏/㎝²| |
|Ом|Ом∙м| |
|Гр или Гр (рад)|рад| |
|Дж|дж| |
|В|в| |
|Гц|гц| |
|км/ч|км/час| |
|m/s² (g)|g, (ед)|<small>g не является единицей величины ускорения, а лишь символьное обозначение ускорения.</small>|
|Па∙с/м|Пас/м| |
|Па∙с/m³|Пас/m³| |
|(7 ± 2) Н·м [(70 ± 20) ㎏f·см]|7 Н·м| |
|70 ± 20 кгс·см| |
|бит<br> Б, байт<br> кбит<br> Кбайт|б<br> бт<br> Кбит<br> кбайт| |
|При нормальных условиях  m³|нm³| |
|Lр (исх. 20 м㎪) = 20 дБ или<br> 20 дБ (исх. 20 м㎪)<br> Не более 80 дБ (исх. 1 мкА)<br> Не менее 120 дБ (исх. 1 мкВ/м)|Не более 80 дБ мкА<br> Не менее 120 дБ мкВ/м|<small>Пример обозначения уровня звукового давления. Необходимо указывать исходную величину, её значение помещают в скобках  за обозначением<br> логарифмической величины. При краткой форме записи значение исходной величины указывают в скобках за значением уровня.</small>|
|100 ㎸т<br> 80 %<br> 20 ℃<br> 10 Ом<br> 20°<br> 1220×740 ㎜<br> 5,758°|100кВт<br> 80 %<br> 20℃<br> 10Ом<br> 20 °<br> 1220×740мм<br> 5°758| |
|㎪∙с/м|Па∙кс/м| |
|v = 3,6 s/t,<br> где v — скорость,км/ч;<br> s — путь, м;<br> t — время, с|v = 3,6 s/t км/ч,<br> где  s — путь, м;<br> t — время, с| |
|Вт/(м∙К)|Вт/м∙К| |
|Н∙м<br> А∙m²<br> Па∙с|НмНхм<br> Аm² Ахm²<br> Пас| |
|Вт∙м⁻²∙К⁻¹<br> Вт/(m²·K)|W/m²/К| |
|80 км/ч<br> 80 километров в час|80 км/час<br> 80 км в час| |
|Провести испытания пяти труб, каждая длиной 5 м.<br> Отобрать 15 труб для испытания на давление.|Провести испытания 5‑ти труб, каждая длиной 5 м.|<small>Числовые значения величин с обозначением единиц величин и единиц счёта следует писать цифрами, а числа без обозначения единиц величин и единиц счёта от единицы до девяти — словами.</small>|
|1,50; 1,75; 2,00 м|1,50 м; 1,75 м; 2,00 м| |
|Диаметр крепёжных отверстий прибора должен соответствовать М 4 (4,5 ㎜)|Диаметр крепёжных отверстий прибора должен соответствовать М 4 (⌀ 4,5)| |
|От 1 до 5 ㎜<br> От 10 до 100 кг<br> От плюс 10 до минус 40 ℃<br> От 8454,3 до 8464,3 ㎒|От 1 ㎜ до 5 ㎜<br> 10 … 100 ㎏<br> +10 ‑ −40 ℃<br> (8459,3 ± 5,0) ㎒| |
|Не более (если допустимы все значения меньше указанного значения).<br> Не менее (если допустимы все значения больше указанного значения).<br> Знак «±» не ставят перед не более, ≥|Больше, ниже, выше, меньше, хуже.<br> Не более ± 5 ℃.<br> Не менее ± 5 ℃| |
|Шероховатость поверхности.<br> Rₐ = 0,63 мкм<br> R<sub>z</sub>= 0,63 мкм|Чистота поверхности не хуже √ 0,63| |
|1,22∙10⁴|1,22Е+04| |
|Lo ≥ 15 МэВ/(мг∙см⁻²)<br> σо ≤ 10⁻² ㎝²|Lo ≥ 15 МэВ/(мг∙см⁻²)<br> σо ≤ 10⁻² ㎝²| |

【**Table.** Термины】

|*Правильно*|*Неправильно*|
|:-|:-|
|Температура точки росы ℃|Точка росы|
|Измерение|Замер, обмер|
|Точность, прецизионность|Верность измерений|
|Произвести измерение|Замерить, мерить, обмерить|
|Измерить давление|Померить давление|
|Измерить значение  напряжения или определить значение напряжения|Измерить  напряжение или<br> измерить величину напряжения|
|Результат измерений|Измеренные значения|
|Температура выражается в кельвинах|Температура измеряется в кельвинах|
|Единица скорости|Размерность скорости|
|Погрешность средств измерений|Погрешность показания прибора|
|Класс точности прибора указывается — 0,1; 0,2; 1, 2, 3.|Класс точности прибора ± 1,5 %|
|Погрешность измерения не должна быть  более 0,01 г<br> Погрешность измерения ±0,01 г|Ошибка измерения 0,01 г|
|Температура минус (60 ± 5) ℃|Температура — 60 ℃|
|Диапазон измерений от минус 50 до плюс 200 ℃|Предел измерений (−50 ‑ 200) ℃|
|Оси находились на одной высоте с допускаемыми отклонениями ± 1 ㎜|Оси находились на одной высоте с погрешностью ± 1 ㎜|
|Погрешность измерений не должна быть более (не менее) 1 %;<br> Погрешность измерения ± 1 %|Точность измерений 1 %|
|Погрешность измерений равна ± 5 %|Погрешность 3σ равна  ± 5 %|
|Единицы  величин|Единиц физических величин|
|Средство измерений или измерительный прибор|Мерительное средство|
|Средство измерений или измерительный прибор|Измерительная аппаратура|
|Средство измерений или измерительный прибор|Для измерения применялось средство контроля|
|Стандартный образец или измерительный прибор|Эталонная деталь|
|Нормальные климатические условия с указанием конкретных значений величин|Комнатная температура|
|Значение пусковой силы тока бортовой аппаратуры должна не превышать полуторократного номинального значения силы тока (указать значение или заменить термин номинального тока на потребляемый ток) электропотребления на время до 50 ㎳.|Величина пускового тока бортовой аппаратуры не должна превышать полуторократного значения номинального тока электро&shy;потребления на время до 50 ㎳.|
|Увеличение силы электрического тока до 23,5 А|Увеличение тока до 23,5 А|
|Значение силы электрического тока|Величина тока|
|Значение атмосферного давления 8,6∙10⁴ ㎩ (645 ㎜ рт. ст.)|Величина атмосферного давления 645 ㎜ рт. ст.|
|Ускорение|Перегрузка|
|Масса 3 ㎏|Груз 3 ㎏|
|Изделие массой 1 500 т|Изделие весом 1 500 т|
|Среднее квадратическое отклонение (стандартное отклонение) — параметр функции распределения измеренных значений или показаний, характеризующий их рассеивание и равный положительному корню квадратному из дисперсии этого распределения.|Не корректное употребление термина среднее квадратическое отклонение| |



<p style="page-break-after:always"> </p>

## Docs & links
|Navigation|
|:-|
|**[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·События, **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ, **[Way](way.md)**·Пути|
|*Sections & pages*|
|**`Качество:`**<br> [Bus factor](bus_factor.md)・ [Way](way.md)・ [АВПКО](fmeca.md)・ [Авторский надзор](des_spv.md)・ [Бережливое производство](lean_man.md)・ [Валидация, верификация](vnv.md)・ [Класс чистоты](clean_lvl.md)・ [Конструктивное совершенство](con_vel.md)・ [Крит. технологии](kt.md)・ [Крит. элементы](sens_elem.md)・ [Метрология](metrology.md)・ [Надёжность](qm.md)・ [Нештатная ситуация](emergency.md)・ [Номинал](nominal.md)・ [Ошибки](error.md)・ [Система менеджмента качества](qms.md)・ [УГТ](trl.md)/[TRL](trl.md)|

   1. Docs: [Do not do their work for others ❐](f/doc/20191106_1.pdf)
   1. <https://en.wikipedia.org/wiki/List_of_common_misconceptions>
   1. <https://en.wikipedia.org/wiki/Survivorship_bias>
   1. <https://ru.wikipedia.org/wiki/Систематическая_ошибка_выжившего>
