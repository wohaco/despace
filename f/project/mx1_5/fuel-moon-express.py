# -*- coding: utf-8 -*-

import os
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')


# Исходные данные
Mstart = 250  # Масса КА
Mka = Mstart
Mfuel = 0
Msbb = 0  # Масса сбрасываемого блока баков, если таковой есть. Если нет, поставить 0
Madapter = 0  # Масса адаптера КА-РБ
Mlgm = 0  # Масса ПМ сухого, включая адаптер КА-РБ
Mvm = 0  # Масса ВМ, не включая СМ

# Коэффициенты запаса по топливу по этапам полёта
Kf1 = 1.2
Kf2 = 1.01

# Усреднённые импульсы по этапам полёта
Isp1 = 320
Isp2 = 220
Isp3 = 310

# Расчёт КА
try:
	print u'Аналог Moon Express MX-1. Стартовая масса:', Mstart, u' ( без адаптера:', Mstart - Madapter, u')\n'
	Mstart = Mstart - Madapter

	V = 5800
	Isp = Isp1
	Kf = Kf2
	Mt = Mstart * ( 1 - math.exp((-V) / (9.81 * Isp)) ) * Kf
	Mfuel = Mfuel + round(Mt)
	Mfuelsbb = Mfuel
	Mstart = Mstart - round(Mt)
	print u'1) Перелёт Земля-Луна, а также прилунение.\n   └ Скорость:', V, u'   уд. импульс:', Isp, u'  треб. топлива:', round(Mt), u'(резерв', (Kf - 1)*100, '%)'
except:
	print u'\nВозникла какая-то ошибка.'


Mfuel = round(Mfuel)
Mfuelbaki = Mfuel - Mfuelsbb
print u'\nИтого топлива, кг:', Mfuel

Mstart = Mka - Madapter - Msbb - Mfuel
print u'Масса КА на поверхности, кг:', Mstart

input()