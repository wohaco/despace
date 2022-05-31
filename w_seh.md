# Wohaco Systems Engineering Handbook


## ➀ Core principles

| |*➀ Core principles*|
|:-|:-|
|TBD|  |
|TBD| Some links:<br> ・<https://en.wikibooks.org/wiki/Space_Transport_and_Engineering_Methods><br> ・<https://en.wikibooks.org/wiki/Astrodynamics> |
|TBD|  |
|TBD|  |
|TBD|  |



## ➁ Ground & Space

| |*➁ Ground & Space*|
|:-|:-|
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |



## ➂ Movement mechanics

| |*➂ Movement mechanics*|
|:-|:-|
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |
|TBD|  |



## TBD

**Основное:**

   1. БЕЗ ПАНИКИ!
   1. Спроектировать КА может любой.
   1. Должен соблюдаться баланс.
   1. Краткость — сестра таланта.
   1. Бюрократия тормозит всё, но записывать / обосновывать принятые решения и полученные результаты — необходимо, иначе всё будет забыто.
   1. Терминология должна быть единой для всех.
   1. Сомнения — ключ к успеху.

| | |
|:-|:-|
|TBD|Вноси везде мелкие детали.<br> Маленькие детали не испортят общего впечатления от творения, зато порадуют тех, кто сумеет их разглядеть:<br> ➀  Если делаешь большую красивую картинку с КА и космосом, не забывай добавить маленькое изображение НЛО, или планету с Маленьким Принцем, аль ещё чего‑нибудь.<br> ➁  В большом документе (100+ стр) старайтесь в текст добавь словосочетания в духе — гениальный сетевой график・ двигатели‑моховики・ демоническая модель・ комический аппарат・ комический комплекс・ ракетно‑комический комплекс・ неземной комплекс управления・ энергообречённость космического аппарата・ spacegraft・ и т.д.<br> ➂  А ещё у проектов могут быть маскоты. При подготовке презентации на первом слайде суньте в малозаметном месте маскота и лозунт *«Только вперёд»* или *«Keep moving forward»*.|
|TBD|Инженер многолик. Инженер всегда во всём уверен. Инженер никогда ни в чём не уверен. Инженер стремится создавать стандарты. Инженер стремится обходить стандарты. Инженер сохраняет статус‑кво. Инженер изменяет статус‑кво. Все утверждения верны.|
|TBD|Соблюдай алфавитный порядок; отходи от него только в крайних случаях. Нумеруй каждый раздел и, по‑возможности, каждый пункт документа — это позволит точно ссылаться и меньше ошибаться.|
|TBD|Если есть общепринятые стандарты оформления, старайся придерживаться их. Это позволит:<br> ➀  общаться с остальным сообществом на одном языке,<br> ➁  не тратить время на изобретение велосипедов,<br> ➂  избегать типовых ошибок,<br> ➃  концентрироваться на содержимом, а не на форме.|
|TBD|Содержимое превыше формы. Сперва изучают форму, потом — содержимое. Нельзя создавать, зная форму, но не зная содержимого. Нельзя создавать, зная содержимое, но не зная формы.|
|TBD|Не допускай вендок-лока. Вендор-лок удобен, красив, интегрирован, и там есть люди, которые готовы за твои деньги сделать хорошо. Но если что-то случится (банкротство, изменение настроения, пожар, ссора, и пр.), то твоё дело остановится.<br> Поэтому, твоя информация и минимальные средства для работы с ней должны быть у тебя, но улучшать и упрощать можно и у других.<br> Поэтому же, отдавай предпочтение простоте в реализации и поддержании, и только потом — простоте в использовании.|
|TBD|Technical part:<br> ・Bots — to perform robotic and routine duties, accept commands, remind, & track states<br> ・Chat (XMPP) or Mattermost or Rocket.chat — to communicate<br> ・Git (Gitea, GitLab) — to store them all with history & backups<br> ・Markdown — to collaboratively write, parse, & remember everything<br> ・Office apps (Word, Excel) — because they look nice, have an ability to create math models, & everyone have them|
|TBD|Простота — многогранное понятие. Кому‑то молоток — сложно, а кому‑то P vs NP problem — довольно просто.|
|TBD|Документы и процессы должны быть живыми и актуальными. Если что‑то требует периодической регулировки, значит, между регулировками оно находится в неотрегулированном состоянии. Сообщение об изменениях должны приходить по готовности, а не на очередном совещании. Изменения в документы должны вноситься по готовности, а не когда запланировано.|
|TBD|What may be automated should be automated.|
|TBD|Расчёт радиаторов (концептуальные шаги):<br> ➀  Определить объём тепла, которое нужно сбросить, состоящий из:<br> ・собственного тепловыделения БА (в первом приближении равно электропотреблению)<br> ・тепла, полученного от Солнца и переотражения от небесного тела (с учётом теплозащиты и покрытий)<br> ➁  Построить циклограмму работы с учётом участков, где радиаторы работают:<br> ・на свету и могут получать тепло извне (засветка, переотражение) и их мощности может быть недостаточно<br> ・в тени и их мощность может быть излишня<br> ➂  Выбрать материал, форму и толщину радиатора с учётом:<br> ・скоростей нагрева и охлаждения<br> ・суммарной теплоёмкости<br> ・возможности КА поддерживать тепловой баланс в тени|
|TBD|Almost everything can be broken down in 2 pieces — that is how it’s done in nature. In most cases everything else is just a combination of these 2 pieces.|
|TBD|Proper non-scientific books to read:<br> ・Antoine de Saint-Exupéry — Le Petit Prince<br> ・Clifford D. Simak — City<br> ・Isaac Asimov — anything (especially the Foundation series)<br> ・Stanisław Lem — Solaris<br> ・Strugatsky — anything<br> ・Sun Tzu — The Art of War<br> ・Arthur C. Clarke — Childhood's End<br> ・Lewis Carroll — Alice in Wonderland|
|TBD|When working with humans try to:<br> ・always reply them;<br> ・not make robots reply to humans in negative way — robots shall make human's life easier;<br> ・not make robots judge human effectivenes in performing robot's duties.|
|TBD|Pay attention to what they do, not what they say. Yet, a progress will be there, where you can make an agreement with those who have similar goals.|
|TBD|Everybody in a company are hired employees, even CEO. Apply equality. You're not better than they, and they're not worse than you. Despite anything.|
|TBD|Use different approaches and combinations of them. Be flexible, have plans and a vision of how to reach them.|
|TBD|Применяй инструменты, нужные для достижения цели, а не только те, к которым все привыкли. В IT используй универсальные стандарты, которые показываются пользователю в том виде, к которому он привык.|
|TBD|Принимая решения, необходимо, чтобы сейчас и потом было ясно:<br> ・как было принято решение,<br> ・как оно влияет на всё остальное,<br> ・какие варианты были рассмотрены и почему отклонены.|
|TBD|Терминология должна быть единой для всех. При этом цель должна превалировать над содержанием. Не стоит тратить много времени на придумывание/изменение терминов.|
|TBD|Хаос наиболее динамичен и способен приспосабливаться.|
|TBD||
|TBD||




## ➃ Addons

### Microblog entries

Below is a list of microblog (less than 500 chars) entries that are (have been) posted every Wednesday & Saturday at 11:11 GMT *(14:11 MSK)*. The aim is to promote space sciences, engineering approaches, obtain reviews & opinions, which can be included into this WSEH.

<small>

   1. 2022.05.21 — The #space nowadays is not a #rocket #science anymore. Some believe it’s because there are a lot of affordable technologies for low orbits (which I don’t classify as “space”). Probably it never was a rocket science, — it was a hidden science. Or maybe a science that doesn’t worth spending time because there are more interesting things on Earth, or you cannot gain money out of fundamental space #explorations. Anyway, the space was & is simple. As any engineering matter.
   1. 2022.05.25 — There’s no big difference between the #space engineering & Earth one. Just some additions & complications for requirements & environment. Some notable points: fast evaporation & degradation of materials (metals, plastics, lubricants), lack of possibility of being maintained by a human, large temperature ranges, lesser gravity, own atmosphere, particles, radiation, vacuum. Basically, if a device can survive these conditions for a needed period then it can be used in space.
   1. 2022.05.28 — ... где начинается космос
   1. 2022.06.01 — ... problems
   1. 2022.06.04 — ... почему земное неприменимо-1
   1. 2022.06.08 — ... почему земное неприменимо-2
   1. 2022.06.11 — ... почему земное применимо
   1. 2022.06.15 — ... почему космос важен
   1. 2022.06.18 — ... инженерный подход, причины и следствия
   1. 2022.06.22 — ... инженерный подход, определение необходимости
   1. 2022.06.25 — ... инженерный подход, дуализм
   1. 2022.06.29 — 
   1. 2022.07.02 — 
   1. 2022.07.06 — 
   1. 2022.07.09 — 
   1. 2022.07.13 — 
   1. 2022.07.16 — 
   1. 2022.07.20 — 
   1. 2022.07.23 — 
   1. 2022.07.27 — 
   1. 2022.07.30 — 
   1. 2022.08.03 — 
   1. 2022.08.06 — 
   1. 2022.08.10 — 
   1. 2022.08.13 — 
   1. 2022.08.17 — 
   1. 2022.08.20 — 
   1. 2022.08.24 — 
   1. 2022.08.27 — 
   1. 2022.08.31 — 
   1. 2022.09.03 — 
   1. 2022.09.07 — 
   1. 2022.09.10 — 
   1. 2022.09.14 — 
   1. 2022.09.17 — 
   1. 2022.09.21 — 
   1. 2022.09.24 — 
   1. 2022.09.28 — 
   1. 2022.10.01 — 
   1. 2022.10.05 — 
   1. 2022.10.08 — 
   1. 2022.10.12 — 
   1. 2022.10.15 — 
   1. 2022.10.19 — 
   1. 2022.10.22 — 
   1. 2022.10.26 — 
   1. 2022.10.29 — 
   1. 2022.11.03 — 
   1. 2022.11.05 — 
   1. 2022.11.09 — 
   1. 2022.11.12 — 
   1. 2022.11.16 — 
   1. 2022.11.19 — 
   1. 2022.11.23 — 
   1. 2022.11.26 — 
   1. 2022.11.30 — 
   1. 2022.12.03 — 
   1. 2022.12.07 — 
   1. 2022.12.10 — 
   1. 2022.12.14 — 
   1. 2022.12.17 — 
   1. 2022.12.21 — 
   1. 2022.12.24 — 
   1. 2022.12.28 — 
   1. 2022.12.31 — 

</small>
