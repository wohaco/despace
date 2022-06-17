# Despace Engineering Handbook
> 2019.05.05 [🚀](../../index/index.md) [despace](index.md) → [SCS](scs.md)  
> *Navigation:*  
> **[FAQ](faq.md)**【**[SCS](scs.md)**·КК, **[SC (OE+SGM)](sc.md)**·КА】**[CON](contact.md)·[Pers](person.md)**·Контакт, **[Ctrl](control.md)**·Упр., **[Doc](doc.md)**·Док., **[Drawing](drawing.md)**·Чертёж, **[EF](ef.md)**·ВВФ, **[Error](error.md)**·Ошибки, **[Event](event.md)**·Событ., **[FS](fs.md)**·ТЭО, **[HF&E](hfe.md)**·Эрго., **[KT](kt.md)**·КТ, **[N&B](nnb.md)**·БНО, **[Project](project.md)**·Проект, **[QM](qm.md)**·БКНР, **[R&D](rnd.md)**·НИОКР, **[SI](si.md)**·СИ, **[Test](test.md)**·ЭО, **[TRL](trl.md)**·УГТ

**Table of contents:**

[TOC]

---

<p style="page-break-after:always"> </p>

## 1. Basics

### 1.1. Basic principles

| |*1.1. Basic principles*|
|:-|:-|
|1| This Handbook is intended to help space engineers to create & operate a spacecraft. It consists of several facts, best practices, cases, & links for further readings. |
|2| Core principles:<br> ➊ **DO NOT PANIC!**<br> ➋ Do what you want.<br> ➌ There shall be a balance.<br> ➍ Brevity is the soul of wit.<br> ➎ Doubt is the key to success.<br> ➏ Everyone can create a spacecraft.<br> ➐ The best system is the one you can use to succeed.<br> ➑ Terminology & design shall be the same for everything. But remember that words don’t matter.<br> ➒ Nothing is strict. Nothing is a rule. Nothing is constant. Flexibility & curiosity win most of the time.<br> ➓ Bureaucracy is slow, but you shall write down / justify the decisions & results — because everything will be forgotten. |
|TBD| Everything is relative. Everything can be seen through comparison. Bad is called good when worse happens. There is no point to tell how much “something” you obtain / lost if you do not compare it to “anything” previous. |
|TBD| Chaos is mostly dynamic & able to adapt. Use different approaches & combinations of them. Be flexible, have plans & a vision of how to achieve them. |
|TBD| When we do space engineering the only proper answer for questions like “who has to be in charge of something” or “who has to handle the situation” is — “the one who need it”. If you build your habits around this approach you will succeed. |
|TBD| Almost everything can be broken down into 2 pieces (eventually 3) — that is how it’s done in nature. In most cases, everything else is just a combination of these 2 pieces. |
|TBD| For everything you plan & do there have to be:<br> ➊ A Reason (or need or target). Try not to use anything that has bad reasons. Change approaches you use because of bad reasons as soon as possible. Examples of the bad reasons:<br> ・“It’s modern.”<br> ・“I don’t know.”<br> ・“It’s free / paid.”<br> ・“Everyone uses it.”<br> ・“The time is short.”<br> ・“They told me to do that.”<br> ・“This is a common path here.”<br> ・“I didn’t look for good alternatives.”<br> ・“I’m sure my way is correct, but I can’t prove it.”<br> ➋ A Consumer. Try to avoid bad consumers — the ones, who:<br> ・do not honor agreements;<br> ・do not pay;<br> ・lies. |
|TBD| When working with humans pay attention to what they do, not what they say. Yet, progress will be there, where you can make an agreement with those who have similar goals.<br> Everybody in a company is hired employee, even the CEO. Apply equality. You're not better than them, & they're not worse than you. Despite anything.<br> And try to:<br> ・always reply to them;<br> ・not make robots negatively reply to humans — robots shall make human's life easier;<br> ・not make robots judge human effectiveness in performing robot's duties. |
|TBD| Keep alphabetical order; break it only in extreme cases. Number each section and, if possible, each paragraph of any document — that will lead to accurate reference & less error rate. |
|TBD| Use KISS (keep it simple, stupid) — it seems that perfection is attained not when there’s nothing more to add, but when there’s nothing more to remove.<br> Simplicity is a multifaceted concept. For some, a hammer is difficult, but for some, the P vs NP problem is quite simple. |
|TBD| Reduce your overhead while letting your people to rest & think. Shorten the distances between every step, reduce the number of steps, get rid of supporting structures that require time & people. Let authors defend their works. |
|TBD| Use the tools you need to achieve your goal, not just the ones everyone is used to. In IT, use universal standards that are shown to the user in the form to which he is accustomed.<br> Despace technical part:<br> ・Bots — to perform robotic & routine duties, accept commands, remind, & track states<br> ・Chat — *XMPP or Mattermost or Rocket.chat* — to communicate<br> ・Git — *Gitea, GitLab* — to store them all with history & backups<br> ・Knowledge database<br> ・Markdown — to collaboratively write, parse, & remember everything<br> ・Office apps — *Word, Excel* — because they look nice, can create math models, & everyone has them<br> ・What may be automated should be automated |
|TBD| No one should be punished for “not done”, one should be punished for "not being told what might not be done". |
|TBD| There are 2 entities — documents & words. Let the words complement the documents, but not vice versa. |
|TBD| 1 lb = 0.453.592 ㎏<br> 1 g = 9.81 ㎧² (sometimes 9.806.650), but never 10. |
|TBD| Terminology shall be the same for everyone. Note, the purpose shall prevail over the content. Don't spend a lot of time on:<br> ・invent / change terms<br> ・reonrganize the documents. |
|TBD| When making decisions, it’s necessary to be clear now & then:<br> ・how the decision was made,<br> ・how it affects everything else,<br> ・what options were considered & why they were rejected. |
|TBD| Documents & processes shall be alive & up to date. If something requires periodic adjustment, then between adjustments it’s in an unadjusted state. Changes shall be reported when ready, not at the next meeting. Changes to documents shall be made when ready, not when scheduled. |
|TBD| Content over form. First you study the form, then the content. It’s impossible to create, knowing the form, but not knowing the content. It’s impossible to create, knowing the content, but not knowing the form. |
|TBD| The engineer is multifaceted & brave. An engineer is always sure of everything. An engineer is never sure of anything. The engineer seeks to create standards. The engineer seeks to bypass the standards. The engineer maintains the status quo. The engineer changes the status quo. All statements are correct. |
|TBD| If there are common design standards, try to stick to them. This will allow you to:<br> ➊ communicate with the rest of the community in the same language,<br> ➋ not waste time inventing bicycles,<br> ➌ avoid common mistakes,<br> ➍ focus on content, not form. |
|TBD| Don't allow vendor lock.<br> ・Vendor lock is convenient, beautiful, integrated, & there are people who are willing to do good for your money. But if something happens (bankruptcy, mood change, fire, quarrel, etc.), then your business will stop.<br> ・Therefore, your information & the minimum tools to work with it shall be yours, but improvements & simplifications can be performed by others.<br> ・Therefore, prioritize ease of implementation & maintenance over ease of use.<br> ・The information you produce/use shall be as free as possible — that's how you can avoid being influenced by someone else. |
|TBD| Bring in small details everywhere. Small details will not spoil the overall impression of the creation, but will please those who can see them:<br> ➊  If you make a big beautiful picture with spacecraft & space, do not forget to add a small image of a UFO, or a planet with the Little Prince, or something else.<br> ➋  In a large document (100+ pages), try to add phrases in the text like:<br> ・spacegraft<br> ・гениальный сетевой график<br> ・двигатели‑моховики<br> ・демоническая модель<br> ・комический аппарат<br> ・комический комплекс<br> ・ракетно‑комический комплекс<br> ・неземной комплекс управления<br> ・энергообречённость космического аппарата<br> ・etc.<br> ➌  Also, projects can have mascots. When preparing a presentation, on the first slide, stick a mascot & a slogan “Keep moving forward” or something else in an inconspicuous place. |
|TBD| Challenges, problems, issues |
|TBD|  |



### 1.2. Links & books

| |*1.3. Links & books*|
|:-|:-|
|1| Proper non-scientific books to read:<br> ・Antoine de Saint-Exupéry — Le Petit Prince<br> ・Clifford D. Simak — City<br> ・Isaac Asimov — anything (especially the Foundation series)<br> ・Stanisław Lem — Solaris<br> ・Strugatsky — anything<br> ・Sun Tzu — The Art of War<br> ・Arthur C. Clarke — Childhood's End<br> ・Lewis Carroll — Alice in Wonderland<br> ・Модель космоса, том 1 и 2<br> ・[NASA Spacecraft systems engineering](book_nasa_seh.md) |
|2| Some links:<br> ・<https://en.wikibooks.org/wiki/Space_Transport_and_Engineering_Methods><br> ・<https://en.wikibooks.org/wiki/Astrodynamics> |
|3|**Sources.** Pretty far from what they call the proper list of sources, but that’s all we have.<br>・<https://3dnews.ru/952315> <small>— [archive ❐](f/archive/20170524_1.pdf) of 2019.01.27</small><br>・<https://academia.edu><br>・<https://alemak.livejournal.com/1379.html> <small>— [archive ❐](f/archive/20140213_1.pdf) of 2019.01.27</small><br>・<http://astronautix.com/><br>・<http://braeunig.us/space/><br>・<https://britastro.org/><br>・<http://ecoruspace.me/><br>・<https://epizodyspace.ru/><br>・<https://factoriesinspace.com/> — In‑Space Manufacturing & Orbital Economy<br>・<https://incose.org/> — International Council on Systems Engineering<br>・<https://trade.glavkosmos.com/><br>・<https://globalspaceexploration.org/><br>・<https://kosmolenta.com/><br>・<https://multitran.com/><br>・<https://nanosats.eu/> — nanosats database<br>・<https://nasa.gov/offices/education/about/index.html><br>     ・<https://jpl.nasa.gov/missions/?type=current><br>     ・<https://nasa.gov/connect/ebooks/index.html> — NASA ebooks<br>     ・<https://forum.nasaspaceflight.com/index.php?topic=32901.0><br>     ・<https://ntrs.nasa.gov/><br>     ・<https://pds.nasa.gov/><br>     ・<https://spaceflight.nasa.gov/cgi-bin/acronyms.cgi?program=shuttle&searchall=true><br>・<https://newspace.im/> — NewSpace index<br>・<https://forum.novosti-kosmonavtiki.ru/><br>     ・<http://novosti-kosmonavtiki.ru/forum/forum14/topic8552/><br>     ・<http://novosti-kosmonavtiki.ru/forum/forum14/topic14003/><br>・<https://rocketengines.ru/><br>・<https://satsearch.co/><br>・<http://sewiki.ru/> — Systems engineering thinking wiki<br>・<https://space.skyrocket.de/doc/acronyms.htm><br>・<https://spaceflightinsider.com/><br>・<https://en.wikipedia.org/>・ <https://ru.wikipedia.org/>・ <https://ru.wiktionary.org/><br>・[ГОСТ 16504-81](гост_16504.md)<br>・<https://www.spacematdb.com/><br>・<https://spaceindustrydatabase.com/><br>・**Unicode** — <https://compart.com/en/unicode/category/So>・ <https://htmlsymbols.xyz/unit-symbols>|



### 1.3. Common paths

| |*1.3. Common paths*|
|:-|:-|
|1|【**Anything failed**】<br><br> **Situation** — anything happened or can happen in the future. (a common way to mitigate / avoid anything)<br><br> **Solution**:<br> ➊ Define the threat level.<br> ➋ Define possible risks, environment, requirements & available / possible resources.<br> ➌ Make a decision & implement it.<br> ➍ Make a solution to avoid this issue in the future.|
|2|【**A device broke down before the launch**】<br><br> **Situation** — a device can no longer be used, but you have time before the launch (e.g. broke, didn’t pass the tests, is no longer produced, etc.).<br><br> **Solution** — as usual, you need to balance resources (equipment, money, people, time, etc.). Typical solutions look like this (to choose any or a combination of them):<br> ➊ Repair the device.<br> ➋ Buy a new one, the same (but working) device.<br> ➌ Buy a device with similar characteristics, modify the SC & the mission in minor terms.<br> ➍ Adapt the device, SC & mission, albeit with some deterioration.<br> ➎ Buy a device that is not very close in characteristics, modify the SC & the mission.<br> ➏ Create a device or order it on the side, taking additional risks & quickly going through the stages of R&D.|
|3|【**Requirements have not been verified**】<br><br> **Situation** — some requirements cannot be [verified](vnv.md) (digits are worse than expected).<br><br> **Solution** — a group that is in charge (e.g. for an SUI, ground equipment, etc.) shall describe the following issues to understand what mistake had been done, how to fix it & how to avoid it in the future. In case of failure that shall be done by that group with the help of the upper-level designers.<br> ➊ What is the problem we try to solve.<br> ➋ How we got to this point & what will be done to prevent this from happening in the future.<br> ➌ Why what was described in the previous documents (approved by a customer) doesn’t work now.<br> ➍ What can be done so that what has already been approved will work.<br> ➎ A description of the pros & cons of the proposed options.<br> ➏ If it’s still impossible to satisfy the requirements, then what are the options for how the updated SUI will look like.<br> ➐ A description of the pros & cons of the proposed options.<br> ➑ What the developer ultimately proposes as the main option(s).|



<p style="page-break-after:always"> </p>

## 2. Ground & Space

### 2.1. General requirements

| |*2.1. General requirements*|
|:-|:-|
|TBD| Расчёт радиаторов (концептуальные шаги):<br> ➊  Определить объём тепла, которое нужно сбросить, состоящий из:<br> ・собственного тепловыделения БА (в первом приближении равно электропотреблению)<br> ・тепла, полученного от Солнца и переотражения от небесного тела (с учётом теплозащиты и покрытий)<br> ➋  Построить циклограмму работы с учётом участков, где радиаторы работают:<br> ・на свету и могут получать тепло извне (засветка, переотражение) и их мощности может быть недостаточно<br> ・в тени и их мощность может быть излишня<br> ➌  Выбрать материал, форму и толщину радиатора с учётом:<br> ・скоростей нагрева и охлаждения<br> ・суммарной теплоёмкости<br> ・возможности КА поддерживать тепловой баланс в тени |
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |


### 2.2. Electrical & electro­magnetic requirements

| |*2.2. Electrical & electro­magnetic requirements*|
|:-|:-|
|TBD|  |



### 2.3. Mechanical & atmospheric requirements

| |*2.3. Mechanical & atmospheric requirements*|
|:-|:-|
|TBD|  |



### 2.4. Radiation & cosmic rays requirements

| |*2.4. Radiation & cosmic rays requirements*|
|:-|:-|
|TBD|  |



### 2.5. Thermal requirements

| |*2.5. Thermal requirements*|
|:-|:-|
|TBD|  |



<p style="page-break-after:always"> </p>

## 3. Movement mechanics

| |*3. Movement mechanics*|
|:-|:-|
|TBD|  |



<p style="page-break-after:always"> </p>

## 4. Addons

### 4.1. Despace specific notes
**All content in this DB is under the [CC0 ⎆](https://creativecommons.org/choose/zero/) license, except for data obtained from the numberless sources that have been licensed under different licenses.** There’s no classified info. That means you can use it for your deeds without asking anyone, but if you’re about to distribute it, sell it, or whatever then you better check if it’s legal. We try to follow the rules of fair use & to keep the information true, but sadly we’re only human, we were born to die. Occasionally you may see Russian words due to it was the 1st lang of this DB. The source is here: <https://github.com/wohaco/despace>

   1. **For what?** Started as just another pocket notebook from tiny spacecraft engineering group of some space & SC brief facts which have to always be with you. Now it’s for science, for future planning & SC creating.
   1. **For who?** For scientists, engineers & sympathetic essences. For those who want to create / plan / be in a stream.
   1. **Who is now?** Almost as from the start but a bit wider — a group of spacecraft engineers & scientists.
   1. **Who is able?** In terms of git & CC0 — everybody can clone. In terms of this very DB — at least a bachelor in a near spacecraft area (engineering or science) shall take such a great responsibility.
   1. **Why not just Wikipedia?** Because of the nuances in [SC](sc.md) design, & the ability to take this DB with you.

**Some technical issues.** The database consists of text files with markdown. For not to be vendor‑locked. And to be able to use it anywhere in case you have a markdown editor / viewer. Notes & Requirements: (in historical order)

   1. Pages’re fitted for A4 pages or on a 6" device screen. The proposed themes for proposed editors (VNote, ghostwriter) renders pages in the width of A4. Liberation (Arial) Narrow; sometimes Tahoma. There’s a A5 (5 ㎜ margins) theme also.
   1. Each database page has to be as self‑sufficient as possible.
   1. Files / pages names only with lower case Latin letters, digits, underlines.
   1. Images ≤ 670 px wide. Photo ≤ 160×175 px (160×160 px body + 15 px year). [LV](lv.md) / [OE](sc.md) ≤ 120×120 px. Border 1px #ccc.
   1. Fit [contact / company page](contact.md) into 1 ‑ 2 A4. Webp 75. Mini — ≤ 100×90 & 60×50 px (60×50 for companies), webp 69.
   1. Dates are used in YYYY.MM.DD format, e.g. — 1947.02.20. Time — in 24h format, e.g. — 17:06.
   1. Digits on the left are divided w/ the unbreakable space “ ”, on the right — w/ dots, e.g.: 1 234 567.89 & 0.000.001.928.
   1. Tables. Use the left align. Try to fit list points into a single line.
   1. Prefer:
      - a text over images — it’s searchable, editable, scalable, consumes less bytes;
      - large pages full of topics & structured text over several tiny pages — it’s easier to see the full picture at once;
      - short lists — less than 10 points (for ordered ones) & less than 2 sub‑levels — it’s easier to remember.
   1. Assume there is only 3 levels of headings:<br> ░╙ Title of a page<br> ░░╙ Sections<br> ░░░╙ Subsections
   1. A spacecraft (SC) is a major matter of a Space Segment, it divides to the matters below, while these matters can be combined into systems & subsystems:<br>░╙ modules (can function separately)<br> ░░╙ units (cannot function separately)<br> ░░░╙ parts
   1. Special symbols have to be used: …°·•±×÷≤≥≈≠ ‑ − — ⎆ ↷✉ ❐“”’«»✔✘☐◪☑←↑→↓↔↕↖↗↘↙♁↗ 🚀↘ ªⁱⁿº⁺⁻⁼⁽⁾ ⁰¹²³⁴⁵⁶⁷⁸⁹₊₋₌₍₎ ₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₔₕₖₗₘₙₚₛₜ ░▒▓█┆╟║╙╓╱╲╳№©®™ ¼¾½⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞ π⌀∑∞√∛∜‰ ◯○⊙☀☁☂☃☄★☆$¢£¥€₽✓✕✖✗✉⌦ ｛｝（）［］【】・，、。「」『』 ➊➋➌➍➎➏➐➑➒➓ ➀➁➂➃➄➅➆➇➈➉ ⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ αβγδεζηθικλμνξο03C0πρςστυφχψω ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟ03A0ΠΡΣΤΥΦΧΨΩ ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ ♳♴♵♶♷♸♹ etc. ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ 👌👍👎👏✋✌ ⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇    ⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛  <br> №℡㏑㏒ K℃℉ ㎐㎑㎒㎓㎔ ㏈ ㎚㎜㎝㎞㎧㎳ ㍴ ㎅㎆㎇ ㎩㎪㎫㎬ ㏅㏐㏓ ㏙ ㎾㎿㎸㎹㎶㏁ ㎎㎏ ㎂㎃㎄ ㏉㏜㏂㏘ 😷😵😳😲😱😰😭😫😪😩😨😥😤😣😢😡😠😞😝😜😚😘😖😔😓😒😏😍😌😋😊😉😆😅😄😃😂😁

~~~
<p style="page-break-after:always"> </p>
<ruby>A<rt>BCD</rt></ruby>
【**Table.** …】
【**Picture.** …】
<!--…-->
~~~

**Типографика** *(от греч. τύπος — отпечаток + γράφω — пишу, en. Typography)* — искусство оформления при помощи наборного (не рисованного) текста, базирующееся на определённых, присущих конкретному языку правилах, посредством набора и вёрстки. Типографика, с одной стороны, представляет собой одну из отраслей графического дизайна, с другой — свод строгих правил, определяющих использование шрифтов в целях создания наиболее понятного для восприятия читателя текста.

   1. <https://en.wikipedia.org/wiki/Typography>
   1. <https://ru.wikipedia.org/wiki/Википедия:Отбивка_знака_процента_от_предшествующей_цифры>
   1. 2001.01.01 [Особенности набора ❐](http://web.archive.org/web/20080313061322/mamble.nm.ru/nabor.htm) — [archived ❐](f/archive/20010101_1.djvu) 2017.10.13
   1. **Некоторые факты**
      - По ГОСТ 8.417‑2002 знак процента (%) отбивается от цифры, то есть, неправильно: 5%, правильно: 5 %.
      - При отделении десятичных долей от целых чисел лучше ставить запятую (0,158), а не точку (0.158), как принято на Западе и в языках программирования.
      - Тире между цифрами в значении «от‑до» тире от цифр не отбивают (125‑199). На despace это игнорируется.
      - И, кстати, на ЖЖ просто надо добавить ?format=light

**Примеры**

| | |
|:-|:-|
|« »|короткий неразрывный пробел|
|« »|длинный неразрывный пробел|
|«‑»|неразрывный дефис|
|Верхний индекс|⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ ⁱ|
|Нижний индекс|₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₊ ₋ ₌ ₍ ₎ .|
|Деньги|₽ — рупь;<br> $ — доллар США;<br> € — евро;<br> ¥ — японская иена.|
|Псевдографика|░║╟ ╙<br> ┆ ┇ ┊ ┋ ╎ ╏|

<br>

<big><big>**Archive**</big></big>

Just some ~~hysterical~~ historical pages:

[Astrium](contact/astrium.md)・ [Canadian Space Commerce Association](contact/csca.md)・ [Venus (2020.06.18)](faq_venus_20200618.md)

<br>

<big><big>**TBD (roadmap)**</big></big>

   - **MBSE**
      1. PP&C Project planning & control
   - **[Vibrations & shocks](vibration.md):**
      1. <https://www.google.com/search?q=grms+random+vibration>
      1. <https://www.google.com/search?q=SINE+structural>
      1. <https://en.wikipedia.org/wiki/Random_vibration>
      1. <https://femci.gsfc.nasa.gov/random/randomgrms.html>
      1. <https://vibrationresearch.com/blog/sine-on-random-application-testing/>
      1. <https://sines.eimb.ru/Help.html>
      1. <https://en.wikipedia.org/wiki/Short_interspersed_nuclear_element>
   - **Companies & links:**
      1. <https://www.meicompany.com/>
      1. <https://www.linkedin.com/company/enpulsion/>
      1. <https://www.nasa.gov/directorates/spacetech/NASA_Technology_Enables_Precision_Landing_Without_a_Pilot/>
      1. <https://www.inovor.com.au/>
   - **Оформить и добавить методики расчёта, желательно в виде программ с комментариями:**
      1. баллистики:
         - видимость наземных станций
         - видимость Солнца
         - коррекции траекторий в зависимости от космодрома
         - окна старта
         - перелёт на ЖРДУ
         - перелёт на ЭРДУ
         - перелёт с гравманёвром
         - перелёт с повышением / понижением орбиты
         - спуск в атмосфере
         - цена изменения параметров орбиты
      1. мощности СЭС;
      1. надёжности;
      1. ПГС;
      1. прочности;
      1. радиации, РПЗ;
      1. радиолинии, в т.ч. связь с Землёй, диаграммы направленности: — <mark>Писаренко (перевод в Excel)</mark>
         - Orbiter ↔ Earth
         - Orbiter ↔ Lander
         - Lander ↔ Rover (payload on rover)
      1. СОТР;
         - размер радиаторов
         - эффективность радиаторов
      1. топлива;
      1. технического совершенства:
         - антенн
         - батарей аккумуляторных
         - батарей солнечных, включая ФЭП
         - двигателей
         - двигателей-маховиков и гироскопов
         - звёздных и солнечных датчиков
         - КА
         - кабельной сети
         - конструкции
         - РН
         - <mark>TBD</mark>
   - **Научиться внятно работать и применять данные с:**<br> [ASP](ames_stereo_pipeline.md)・ [Blender](blender.md)・ [Cosmographia](cosmographia.md)・ [DOORS](doors.md)・ [NASA open](nasa_open.md)・ [NASA STI program](nasa_sti.md)・ [Octave](gnu_octave.md)・ [SPICE](spice.md)・ [STK](stk.md)
   - **Научиться визуализировать информацию.**
   - **В части накопления информации:**
      1. Аналитика по Луне
         - Artemis
      1. Шары и конусы посадочных аппаратов Венер и Марсов
      1. Космические агентства — структура, подразделения, институты, их функции: [CNSA](03_cnsa.md)・ [CSA](03_csa.md)・ ± [ESA](03_esa.md)・ [ISRO](03_isro.md)・ [KARI](03_kari.md)・ [NASA](03_nasa.md)
      1. Тенденции по развитию космической отрасли.
      1. РН.
      1. Интеграция материалов <https://www.nasa.gov/offices/education/about/index.html>
      1. События.
      1. Добавить книги к описанию планет и прочих небесных объектов.
      1. Качество.
      1. Кооперация.
      1. БА отечественная / иностранная.
      1. НС.
      1. Схемы перелёта.
      1. Риск.
      1. Документы иностранные.
      1. Космические программы.
      1. Принципы разработки R&D (НИОКР): CH・ EU・ IN・ JP・ RU・ US
      1. Различные подходы к созданию СЧ КА.
      1. Инкубатор.
      1. Испытания.
      1. Качество.
      1. Научные исследования.
      1. Радиосвязь.
      1. Матрицы соответствия.
      1. Пилотируемый полёт.
      1. Планеты.
      1. Проекты.
      1. Экология.
      1. Эргономика.
      1. Удельный импульс топлива.
      1. Периодически патрулировать на предмет следующих пометок, добавлять / исправлять:<br> <mark>NOCAT</mark>・ <mark>TBD</mark>・ <mark>нетдаты</mark>・ <mark>нетин</mark>・ <mark>нетинсты</mark>・ <mark>нетмобильного</mark>・ <mark>нетподписи</mark>・ <mark>нетпочты</mark>・ <mark>нетрабочего</mark>・ <mark>неттви</mark>・ <mark>нетфб</mark>・ <mark>нетфото</mark>

<br>

<big><big>**Метафоры и мемы**</big></big>

**Мета́фора** *(от др.‑греч. μεταφορά — «перенос», «переносное значение»)* — слово или выражение, употребляемое в переносном значении, в основе которого лежит сравнение неназванного предмета с каким‑либо другим на основании их общего признака.

|*Метафора*|*Описание*|
|:-|:-|
|**Бритва Оккама**| **Бритва О́ккама** (иногда **лезвие Оккама**) — методологический принцип, получивший название от имени английского монаха‑францисканца, философа‑номиналиста Уильяма Оккама (ок. 1285‑1349). В кратком виде он гласит: *«Не следует множить сущее без необходимости»* (либо *«Не следует привлекать новые сущности без крайней на то необходимости»*). Сам Оккам писал: «Что может быть сделано на основе меньшего числа [предположений], не следует делать, исходя из большего» и «Многообразие не следует предполагать без необходимости». Этот принцип формирует базис методологического редукционизма, также называемый *принципом бережливости*, или *законом экономии* (лат. *lex parsimoniae*).<br> Принцип «бритвы Оккама» состоит в следующем: если некое явление может быть объяснено двумя способами: например, первым — через привлечение сущностей (терминов, факторов, фактов и проч.) А, В и С, либо вторым — через сущности А, В, С и D, — и при этом оба способа дают идентичный результат, то считать верным следует первое объяснение. Сущность D в этом примере — лишняя: и её привлечение избыточно.<br> Важно помнить, что бритва Оккама не аксиома, а презумпция, то есть она не запрещает более сложные объяснения в принципе, а лишь рекомендует *порядок рассмотрения* гипотез, который в большинстве случаев является оптимальным. |
|**Goose**| **Goose** is the only bird that can walk, swim, dive & fly, but does it all equally bad. |
| |**Гусь** — это единственная птица, которая умеет ходить, плавать, нырять и летать, но делает всё это одинаково плохо. |
|**Соотношение карты и территории**| **Соотношение карты и территории** — вопрос о соотношении между символом и объектом. Известное выражение Альфреда Коржибски — «Карта не есть территория» — означает, что абстракция, выведенная из чего‑нибудь, или реакция на неё не является самой вещью; иными словами, перст, указующий на предмет, не есть сам предмет; метафорическая репрезентация какого‑то концепта не является самим концептом; научная теория, описывающая «объективную реальность», не является самой «объективной реальностью» и т.д. То, что карта не территория, значит, что описание реальности не является самой реальностью. |
|**Шарики**| «Представьте себе, что жизнь — это игра, построенная на жонглировании пятью шариками. Эти шарики — Работа, Семья, Здоровье, Друзья и Душа, и вам необходимо, чтобы все они постоянно находились в воздухе. Вскоре вы поймёте, что шарик Работа сделан из резины — если вы его невзначай уроните, он подпрыгнет и вернётся обратно. Но остальные четыре шарика — Семья, Здоровье, Друзья и Душа — стеклянные. И, если вы уроните один из них, он будет непоправимо испорчен, надколот, поцарапан, серьёзно повреждён или даже полностью разбит. Он никогда не будет таким, как раньше. Вы должны осознавать это и стараться, чтобы этого не случилось. Работайте максимально эффективно в рабочее время и уходите домой вовремя. Посвящайте необходимое время своей семье, друзьям и полноценному отдыху. Ценность ценна только если её ценят».<br> *Брайан Дайсон, бывший СЕО Coca‑Cola* |
|**Словоблудие**| Да тут аж [целая отдельная статья](словоблудие.md). |
|**Если можете не писать — тогда не пишите**| Говорят, что однажды к Льву Толстому пришёл молодой писатель и попросил прочесть его рукопись.<br> — Зачем? — спросил его Толстой.<br> — Мне важно узнать Ваше мнение, — ответил молодой литератор.<br> — Зачем Вам, милейший, знать моё мнение? А если, допустим, я прочту и скажу Вам: не пишите. Что будете делать? — насупил брови Лев Николаевич.<br> — Ну, как… Если Вы скажете не писать, то я не буду… — промямлило молодое дарование.<br> — Если можете не писать — тогда не пишите. — сказал граф и удалился. |
|**Тут так заведено**| Анекдот.<br> Клетка. В ней 5 обезьян. К потолку подвязаны бананы. Под ними лестница. Проголодавшись, одна из обезьян подошла к лестнице с намерением достать банан. Как только она дотронулась до лестницы, вы открываете кран и поливаете ВСЕХ обезьян очень холодной водой. Проходит немного времени, и другая обезьяна пытается полакомиться бананом. Те же действия с вашей стороны. Третья обезьяна, одурев от голода, пытается достать банан, но остальные хватают её, не желая холодного душа.<br> А теперь уберите одну обезьяну из клетки и замените ее новой обезьяной. Она сразу же, заметив бананы, пытается их достать. К своему ужасу, она увидела злые морды остальных обезьян, атакующих её. После третьей попытки она поняла, что достать банан ей не удастся. Теперь уберите из клетки ещё одну из первоначальных пяти обезьян и запустите туда новенькую. Как только она попыталась достать банан, все обезьяны дружно атаковали её, причем та, которую заменили первой, ещё и с энтузиазмом.<br> И так, постепенно заменяя всех обезьян, вы придёте к ситуации, когда в клетке окажутся 5 обезьян, которых водой вообще не поливали, но которые не позволят никому достать банан. Почему? Потому что тут так принято.|
|**Ищите во всём позитив**|Никогда не упускайте возможность сделать наш скучный мир хоть чуточку интереснее. Например, если Вас собьёт машина или ударит по башке сосулька, прежде чем потерять сознание / впасть в кому / умереть, успейте прошептать склонившемуся к Вам прохожему: «Передайте членам Сопротивления, что Кальциноиды уже прибыли на Землю. Парапульсатор спрятан в сторожке у лесника. Пароль: “В лесу, говорят, снова появились хромые лисицы”… При этом, конечно, ещё хорошо бы сунуть прохожему в ладонь заранее подготовленную флэшку со списком фамилий (желательно латышских) и кусочком видеозаписи, на которой какой‑то человек жадно ест корейскую морковь.|



### 4.2. Microblog entries

Below is a list of microblog (~1 000 chars) entries that are (have been) posted om different platforms. The aim is to promote space sciences, engineering approaches, obtain reviews & opinions, which can be included into this handbook.

<small>

   1. 2022.06.06 — When we do #space #engineering the only proper answer for questions like “who has to be in charge of something” or “who has to handle the situation” is — “the one who need it”.
   1. 2022.06.07 — For the past 12 years, I was able to find & hire 11 engineers for my department (almost ¼ of the total headcount) & participated in #hiring ~25 people for other departments. So, 36 in total or 3 per year.<br> Not a big number, possibly, for an #HR but probably enough for an engineer during the first several years & the department's deputy head during the last several years. There was only 1 candidate who had participated in an #interview & didn't pass it. The HRs were involved only during the last stages — to prepare the needed documents.<br> Looking backward, I assume no one of those 11 could pass the first screening if we were using common advices “How to look cool on an interview” or “How to stand out during your job-seeking” because:<br>・some weren’t able to have an eye contact;<br>・some weren’t able to smile properly;<br>・most of them weren’t able to answer simple questions & build strong logical sentences;<br>・all of them, except for a single one, weren’t able to discuss their passion for #space freely, except for short responses;<br>・they all were nervous;<br>・etc.<br>Yet, now these are good & brave employees that can handle complex issues.<br>Probably, that is because the focus was on are they able to perform the job they are hiring for & is there a mutual interest, but not about are they able to smile properly or not.
   1. … — When you heading to your dreams no one can put strings on you, except yourself.<br> Because no one knows how to hurt you & what are your weak points. All they know is that they can try to push on random places waiting for your response. But why should you response then?<br> On the other hand, if that involves other people, then they still cannot put strings on you (until you let them) but they can block you if you'll get close to them.
   1. … — The #space nowadays is not a #rocket #science anymore. Some believe it’s because there are a lot of affordable technologies for low orbits (which I don’t classify as “space”). Probably it never was a rocket science, — it was a hidden science. Or maybe a science that doesn’t worth spending time because there are more interesting things on Earth, or you cannot gain money out of fundamental space #explorations. Anyway, the space was & is simple. As any engineering matter.
   1. … — There’s no big difference between the #space engineering & Earth one. Just some additions & complications for requirements & environment. Some notable points: fast evaporation & degradation of materials (metals, plastics, lubricants), lack of possibility of being maintained by a human, large temperature ranges, lesser gravity, own atmosphere, particles, radiation, vacuum. Basically, if a device can survive these conditions for a needed period then it can be used in space.
   1. … — … где начинается космос
   1. … — … problems
   1. … — … почему земное неприменимо
   1. … — … почему земное применимо
   1. … — … почему космос важен
   1. … — … инженерный подход, причины и следствия
   1. … — … инженерный подход, определение необходимости
   1. … — … инженерный подход, дуализм
   1. … — … почему плохи MBSE, Agile, Scrum и иже с ними
   1. … — … 
   1. … — … 
   1. … — … 
   1. … — … 
   1. … — … 

</small>



<p style="page-break-after:always"> </p>

## Docs & links
|*Sections & pages*|
|:-|
|**【[](.md)】**<br> <mark>NOCAT</mark>|

   1. Docs: …
   1. <…>
