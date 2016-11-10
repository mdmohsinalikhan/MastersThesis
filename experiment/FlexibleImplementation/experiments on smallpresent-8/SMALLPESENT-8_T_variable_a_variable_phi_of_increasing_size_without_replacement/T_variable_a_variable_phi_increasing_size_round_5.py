import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(256.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(246.000000,2),math.log(212.000000,2),math.log(229.500000,2),math.log(258.500000,2),math.log(265.500000,2),math.log(267.312500,2),math.log(235.781250,2),math.log(262.265625,2),math.log(273.820312,2),math.log(298.027344,2),math.log(376.845703,2),math.log(415.932617,2),math.log(507.833984,2),math.log(673.030273,2),math.log(1168.191772,2),math.log(2016.567383,2),math.log(3754.753082,2)]
t_1 = [math.log(256.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(230.000000,2),math.log(229.000000,2),math.log(248.500000,2),math.log(263.000000,2),math.log(285.625000,2),math.log(262.437500,2),math.log(274.562500,2),math.log(253.656250,2),math.log(308.835938,2),math.log(327.363281,2),math.log(438.748047,2),math.log(695.445312,2),math.log(1045.264160,2),math.log(1795.996826,2),math.log(3089.056763,2),math.log(5796.698547,2),math.log(11552.837097,2)]
t_2 = [math.log(272.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(245.000000,2),math.log(232.500000,2),math.log(250.750000,2),math.log(240.750000,2),math.log(188.562500,2),math.log(212.343750,2),math.log(236.687500,2),math.log(285.265625,2),math.log(296.113281,2),math.log(395.054688,2),math.log(527.853516,2),math.log(749.939941,2),math.log(1150.551270,2),math.log(2114.520142,2),math.log(3995.658203,2),math.log(7595.628448,2)]
t_3 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(250.000000,2),math.log(233.500000,2),math.log(239.250000,2),math.log(239.875000,2),math.log(238.437500,2),math.log(257.187500,2),math.log(271.578125,2),math.log(327.953125,2),math.log(367.765625,2),math.log(491.666016,2),math.log(648.931641,2),math.log(1045.375488,2),math.log(1811.710938,2),math.log(3377.920776,2),math.log(6243.067627,2),math.log(12043.106964,2)]
t_4 = [math.log(224.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(324.000000,2),math.log(256.750000,2),math.log(276.500000,2),math.log(275.875000,2),math.log(282.250000,2),math.log(329.187500,2),math.log(344.656250,2),math.log(383.496094,2),math.log(430.119141,2),math.log(614.527344,2),math.log(995.669922,2),math.log(1683.591064,2),math.log(3185.806396,2),math.log(6280.292908,2),math.log(12204.896576,2)]
t_5 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(267.000000,2),math.log(248.500000,2),math.log(242.250000,2),math.log(269.125000,2),math.log(307.250000,2),math.log(274.968750,2),math.log(250.656250,2),math.log(318.703125,2),math.log(346.710938,2),math.log(413.121094,2),math.log(607.894531,2),math.log(981.288574,2),math.log(1856.631104,2),math.log(3441.623291,2),math.log(6453.827209,2),math.log(12635.737671,2)]
t_6 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(271.000000,2),math.log(248.750000,2),math.log(240.875000,2),math.log(223.500000,2),math.log(263.906250,2),math.log(324.359375,2),math.log(371.679688,2),math.log(446.183594,2),math.log(594.912109,2),math.log(907.648438,2),math.log(1511.709961,2),math.log(2921.402344,2),math.log(5441.468140,2),math.log(10957.912781,2),math.log(22059.686279,2)]
t_7 = [math.log(256.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(238.000000,2),math.log(238.500000,2),math.log(264.750000,2),math.log(242.625000,2),math.log(288.812500,2),math.log(284.343750,2),math.log(267.812500,2),math.log(292.023438,2),math.log(412.296875,2),math.log(519.347656,2),math.log(776.783203,2),math.log(1273.372070,2),math.log(2313.695068,2),math.log(4547.476196,2),math.log(8634.551514,2),math.log(16956.189850,2)]
t_8 = [math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(245.000000,2),math.log(261.500000,2),math.log(256.750000,2),math.log(272.375000,2),math.log(301.250000,2),math.log(291.625000,2),math.log(265.562500,2),math.log(292.507812,2),math.log(336.035156,2),math.log(458.380859,2),math.log(554.927734,2),math.log(985.484375,2),math.log(1731.732910,2),math.log(3166.640869,2),math.log(5917.095276,2),math.log(11532.311615,2)]
t_9 = [math.log(256.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(248.000000,2),math.log(231.000000,2),math.log(249.000000,2),math.log(292.250000,2),math.log(276.625000,2),math.log(260.062500,2),math.log(273.437500,2),math.log(315.750000,2),math.log(350.078125,2),math.log(459.617188,2),math.log(588.423828,2),math.log(925.739258,2),math.log(1649.306152,2),math.log(3051.593506,2),math.log(5942.249878,2),math.log(11293.649292,2),math.log(22404.000610,2)]
t_10 = [math.log(272.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(264.000000,2),math.log(282.000000,2),math.log(280.500000,2),math.log(268.750000,2),math.log(253.250000,2),math.log(301.125000,2),math.log(292.343750,2),math.log(363.171875,2),math.log(457.406250,2),math.log(724.722656,2),math.log(1093.841797,2),math.log(1830.129883,2),math.log(3383.388184,2),math.log(6590.380859,2),math.log(12733.460815,2),math.log(25554.314209,2),math.log(50949.509888,2)]
t_11 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(269.000000,2),math.log(245.500000,2),math.log(248.500000,2),math.log(296.000000,2),math.log(266.937500,2),math.log(245.562500,2),math.log(271.609375,2),math.log(305.898438,2),math.log(383.402344,2),math.log(481.511719,2),math.log(740.156250,2),math.log(1336.678711,2),math.log(2462.060791,2),math.log(4499.224487,2),math.log(9000.691833,2),math.log(17952.941345,2)]
t_12 = [math.log(240.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(312.000000,2),math.log(304.000000,2),math.log(288.500000,2),math.log(278.750000,2),math.log(277.500000,2),math.log(301.375000,2),math.log(286.968750,2),math.log(288.671875,2),math.log(285.867188,2),math.log(363.296875,2),math.log(453.757812,2),math.log(673.302734,2),math.log(1000.457031,2),math.log(1714.240234,2),math.log(3199.559448,2),math.log(6401.469910,2),math.log(12519.002289,2)]
t_13 = [math.log(256.000000,2),math.log(296.000000,2),math.log(296.000000,2),math.log(308.000000,2),math.log(263.000000,2),math.log(267.500000,2),math.log(282.250000,2),math.log(262.750000,2),math.log(260.687500,2),math.log(301.093750,2),math.log(329.734375,2),math.log(368.906250,2),math.log(453.773438,2),math.log(649.599609,2),math.log(1098.394531,2),math.log(1955.487305,2),math.log(3778.872314,2),math.log(7040.369873,2),math.log(13635.707703,2),math.log(27175.358490,2)]
t_14 = [math.log(256.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(299.500000,2),math.log(302.000000,2),math.log(282.625000,2),math.log(294.375000,2),math.log(302.843750,2),math.log(316.234375,2),math.log(346.296875,2),math.log(486.230469,2),math.log(667.359375,2),math.log(1093.341797,2),math.log(1957.925781,2),math.log(3696.227051,2),math.log(7407.119995,2),math.log(14614.597168,2),math.log(28751.165283,2)]
t_15 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(254.000000,2),math.log(275.000000,2),math.log(277.000000,2),math.log(281.750000,2),math.log(265.812500,2),math.log(258.625000,2),math.log(281.343750,2),math.log(339.992188,2),math.log(472.300781,2),math.log(656.871094,2),math.log(978.592773,2),math.log(1658.472168,2),math.log(3176.357422,2),math.log(5949.412354,2),math.log(12129.516846,2),math.log(24051.966492,2)]
t_16 = [math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(284.000000,2),math.log(292.000000,2),math.log(238.750000,2),math.log(285.250000,2),math.log(293.312500,2),math.log(292.562500,2),math.log(285.156250,2),math.log(297.445312,2),math.log(363.921875,2),math.log(447.376953,2),math.log(640.867188,2),math.log(1043.282715,2),math.log(1970.806152,2),math.log(3703.776978,2),math.log(7302.225281,2),math.log(14626.654144,2)]
t_17 = [math.log(256.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(280.000000,2),math.log(273.250000,2),math.log(265.375000,2),math.log(284.875000,2),math.log(278.187500,2),math.log(324.140625,2),math.log(396.414062,2),math.log(425.414062,2),math.log(592.976562,2),math.log(853.569336,2),math.log(1391.607910,2),math.log(2598.178467,2),math.log(5191.688843,2),math.log(10348.691895,2),math.log(20584.788971,2)]
t_18 = [math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(222.000000,2),math.log(253.000000,2),math.log(261.500000,2),math.log(280.750000,2),math.log(252.375000,2),math.log(266.625000,2),math.log(269.625000,2),math.log(286.156250,2),math.log(325.289062,2),math.log(339.968750,2),math.log(521.216797,2),math.log(794.267578,2),math.log(1318.197266,2),math.log(2415.534424,2),math.log(4562.895386,2),math.log(8879.750061,2),math.log(17533.960114,2)]
t_19 = [math.log(256.000000,2),math.log(240.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(247.000000,2),math.log(237.000000,2),math.log(252.250000,2),math.log(290.375000,2),math.log(261.562500,2),math.log(244.000000,2),math.log(251.218750,2),math.log(316.679688,2),math.log(370.910156,2),math.log(518.443359,2),math.log(746.163086,2),math.log(1265.860840,2),math.log(2086.258057,2),math.log(3908.539673,2),math.log(7751.370605,2),math.log(15312.808044,2)]
t_20 = [math.log(240.000000,2),math.log(208.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(278.000000,2),math.log(255.500000,2),math.log(256.250000,2),math.log(281.250000,2),math.log(300.187500,2),math.log(309.437500,2),math.log(320.343750,2),math.log(315.570312,2),math.log(360.304688,2),math.log(533.605469,2),math.log(784.943359,2),math.log(1304.818848,2),math.log(2463.519531,2),math.log(4666.234497,2),math.log(9076.508362,2),math.log(17636.510712,2)]
t_21 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(226.000000,2),math.log(228.000000,2),math.log(261.000000,2),math.log(281.000000,2),math.log(303.750000,2),math.log(245.687500,2),math.log(279.093750,2),math.log(274.265625,2),math.log(322.835938,2),math.log(379.457031,2),math.log(486.359375,2),math.log(714.941406,2),math.log(1281.164551,2),math.log(2372.305664,2),math.log(4374.420532,2),math.log(8368.467041,2),math.log(16632.574615,2)]
t_22 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(206.000000,2),math.log(203.500000,2),math.log(235.750000,2),math.log(255.500000,2),math.log(284.000000,2),math.log(306.156250,2),math.log(310.343750,2),math.log(301.085938,2),math.log(359.144531,2),math.log(458.955078,2),math.log(763.935547,2),math.log(1231.561523,2),math.log(2250.103271,2),math.log(4372.009644,2),math.log(8746.898865,2),math.log(17094.312622,2)]
t_23 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(247.000000,2),math.log(258.500000,2),math.log(267.750000,2),math.log(290.750000,2),math.log(276.687500,2),math.log(253.031250,2),math.log(256.140625,2),math.log(297.679688,2),math.log(367.121094,2),math.log(498.128906,2),math.log(772.972656,2),math.log(1358.623047,2),math.log(2374.484131,2),math.log(4472.464233,2),math.log(8685.574158,2),math.log(17377.577606,2)]
t_24 = [math.log(256.000000,2),math.log(296.000000,2),math.log(292.000000,2),math.log(262.000000,2),math.log(256.000000,2),math.log(249.000000,2),math.log(283.000000,2),math.log(266.125000,2),math.log(309.625000,2),math.log(290.625000,2),math.log(260.578125,2),math.log(304.382812,2),math.log(351.195312,2),math.log(474.193359,2),math.log(739.952148,2),math.log(1308.702637,2),math.log(2510.041748,2),math.log(4584.368652,2),math.log(8894.002563,2),math.log(17526.877960,2)]
t_25 = [math.log(320.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(246.000000,2),math.log(235.000000,2),math.log(234.500000,2),math.log(232.000000,2),math.log(203.500000,2),math.log(256.125000,2),math.log(292.531250,2),math.log(296.390625,2),math.log(354.703125,2),math.log(438.246094,2),math.log(541.751953,2),math.log(851.620117,2),math.log(1531.716309,2),math.log(2717.022949,2),math.log(5162.752319,2),math.log(10278.133362,2),math.log(19843.138977,2)]
t_26 = [math.log(272.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(316.000000,2),math.log(262.000000,2),math.log(284.500000,2),math.log(255.000000,2),math.log(271.750000,2),math.log(302.250000,2),math.log(321.375000,2),math.log(345.703125,2),math.log(378.507812,2),math.log(544.234375,2),math.log(938.642578,2),math.log(1622.112305,2),math.log(2852.827148,2),math.log(5225.658936,2),math.log(10470.245728,2),math.log(20253.422668,2),math.log(40308.090179,2)]
t_27 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(245.000000,2),math.log(236.500000,2),math.log(233.500000,2),math.log(244.625000,2),math.log(271.062500,2),math.log(276.406250,2),math.log(300.656250,2),math.log(327.523438,2),math.log(400.390625,2),math.log(675.152344,2),math.log(1194.956055,2),math.log(2111.003906,2),math.log(3905.158203,2),math.log(7768.056641,2),math.log(15379.052673,2),math.log(30922.977844,2)]
t_28 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(284.000000,2),math.log(263.500000,2),math.log(252.750000,2),math.log(248.625000,2),math.log(261.812500,2),math.log(261.312500,2),math.log(288.468750,2),math.log(355.757812,2),math.log(435.792969,2),math.log(585.320312,2),math.log(871.771484,2),math.log(1571.210449,2),math.log(2898.223633,2),math.log(5477.698364,2),math.log(10702.545044,2),math.log(21572.286072,2)]
t_29 = [math.log(240.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(242.000000,2),math.log(233.000000,2),math.log(251.000000,2),math.log(273.750000,2),math.log(258.875000,2),math.log(259.625000,2),math.log(255.968750,2),math.log(310.734375,2),math.log(411.828125,2),math.log(476.425781,2),math.log(710.693359,2),math.log(1146.646484,2),math.log(2224.460938,2),math.log(4065.681396,2),math.log(7999.608154,2),math.log(16010.975464,2),math.log(31669.125732,2)]
t_30 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(245.000000,2),math.log(247.000000,2),math.log(269.750000,2),math.log(270.250000,2),math.log(286.687500,2),math.log(296.843750,2),math.log(397.406250,2),math.log(483.031250,2),math.log(613.734375,2),math.log(894.267578,2),math.log(1522.636719,2),math.log(2814.846680,2),math.log(5228.429443,2),math.log(10264.125366,2),math.log(20404.749878,2),math.log(39781.493744,2)]
t_31 = [math.log(224.000000,2),math.log(208.000000,2),math.log(228.000000,2),math.log(234.000000,2),math.log(253.000000,2),math.log(268.500000,2),math.log(273.750000,2),math.log(249.000000,2),math.log(294.312500,2),math.log(299.937500,2),math.log(362.656250,2),math.log(408.835938,2),math.log(529.683594,2),math.log(712.425781,2),math.log(1147.681641,2),math.log(2082.720703,2),math.log(4234.886475,2),math.log(8419.815430,2),math.log(16334.724609,2),math.log(32716.003052,2)]
t_32 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(261.000000,2),math.log(257.500000,2),math.log(247.500000,2),math.log(263.000000,2),math.log(255.062500,2),math.log(245.593750,2),math.log(249.484375,2),math.log(259.281250,2),math.log(319.507812,2),math.log(355.281250,2),math.log(470.736328,2),math.log(640.532227,2),math.log(1121.765381,2),math.log(2049.152222,2),math.log(3765.179565,2),math.log(7421.043030,2)]
t_33 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(245.000000,2),math.log(253.500000,2),math.log(251.250000,2),math.log(276.875000,2),math.log(336.312500,2),math.log(304.750000,2),math.log(297.531250,2),math.log(288.867188,2),math.log(338.101562,2),math.log(411.562500,2),math.log(665.425781,2),math.log(1080.625488,2),math.log(2051.331787,2),math.log(3962.149780,2),math.log(7561.484192,2),math.log(14881.869812,2)]
t_34 = [math.log(256.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(258.000000,2),math.log(237.750000,2),math.log(235.375000,2),math.log(301.375000,2),math.log(314.500000,2),math.log(276.859375,2),math.log(286.062500,2),math.log(335.953125,2),math.log(444.542969,2),math.log(573.128906,2),math.log(843.385254,2),math.log(1543.495117,2),math.log(2904.177734,2),math.log(5646.189087,2),math.log(11427.709808,2)]
t_35 = [math.log(256.000000,2),math.log(304.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(256.000000,2),math.log(257.500000,2),math.log(246.125000,2),math.log(271.562500,2),math.log(260.468750,2),math.log(253.687500,2),math.log(295.734375,2),math.log(302.089844,2),math.log(356.494141,2),math.log(425.621094,2),math.log(567.372559,2),math.log(888.269287,2),math.log(1515.792969,2),math.log(2638.923035,2),math.log(5012.024292,2)]
t_36 = [math.log(304.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(255.000000,2),math.log(252.500000,2),math.log(262.750000,2),math.log(293.500000,2),math.log(314.812500,2),math.log(274.968750,2),math.log(279.843750,2),math.log(331.117188,2),math.log(368.437500,2),math.log(453.339844,2),math.log(701.660156,2),math.log(1090.454590,2),math.log(1851.436768,2),math.log(3512.569214,2),math.log(6932.348511,2),math.log(13510.038849,2)]
t_37 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(236.000000,2),math.log(259.000000,2),math.log(264.500000,2),math.log(255.125000,2),math.log(277.250000,2),math.log(289.531250,2),math.log(310.890625,2),math.log(300.101562,2),math.log(311.250000,2),math.log(359.230469,2),math.log(577.036133,2),math.log(892.593262,2),math.log(1505.195557,2),math.log(2577.461060,2),math.log(4853.093628,2),math.log(9523.095856,2)]
t_38 = [math.log(272.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(260.000000,2),math.log(277.000000,2),math.log(266.000000,2),math.log(276.125000,2),math.log(277.375000,2),math.log(246.593750,2),math.log(317.343750,2),math.log(381.265625,2),math.log(486.308594,2),math.log(637.792969,2),math.log(979.349609,2),math.log(1832.426270,2),math.log(3433.500732,2),math.log(6401.852539,2),math.log(12494.639465,2),math.log(24570.022949,2)]
t_39 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(238.000000,2),math.log(213.000000,2),math.log(234.000000,2),math.log(256.500000,2),math.log(224.000000,2),math.log(228.875000,2),math.log(247.500000,2),math.log(276.343750,2),math.log(311.343750,2),math.log(354.261719,2),math.log(438.976562,2),math.log(601.405273,2),math.log(964.436523,2),math.log(1750.974609,2),math.log(3062.181396,2),math.log(5943.967346,2),math.log(11727.593903,2)]
t_40 = [math.log(240.000000,2),math.log(216.000000,2),math.log(212.000000,2),math.log(222.000000,2),math.log(219.000000,2),math.log(253.500000,2),math.log(254.250000,2),math.log(267.125000,2),math.log(272.562500,2),math.log(280.406250,2),math.log(310.218750,2),math.log(306.726562,2),math.log(255.949219,2),math.log(333.859375,2),math.log(475.899414,2),math.log(649.641602,2),math.log(1097.270996,2),math.log(1868.697998,2),math.log(3385.248169,2),math.log(6558.137665,2)]
t_41 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(284.000000,2),math.log(278.000000,2),math.log(280.500000,2),math.log(261.500000,2),math.log(271.500000,2),math.log(255.187500,2),math.log(272.625000,2),math.log(262.750000,2),math.log(310.671875,2),math.log(395.324219,2),math.log(522.140625,2),math.log(805.441406,2),math.log(1313.181641,2),math.log(2377.347412,2),math.log(4534.638306,2),math.log(8819.275330,2),math.log(17575.396362,2)]
t_42 = [math.log(256.000000,2),math.log(312.000000,2),math.log(264.000000,2),math.log(258.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(261.250000,2),math.log(262.750000,2),math.log(250.375000,2),math.log(246.968750,2),math.log(269.656250,2),math.log(379.109375,2),math.log(543.507812,2),math.log(841.130859,2),math.log(1503.698242,2),math.log(2781.624023,2),math.log(5012.109375,2),math.log(9563.511230,2),math.log(18657.462463,2),math.log(37565.950897,2)]
t_43 = [math.log(224.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(232.000000,2),math.log(206.000000,2),math.log(213.000000,2),math.log(251.750000,2),math.log(269.125000,2),math.log(258.250000,2),math.log(254.781250,2),math.log(272.640625,2),math.log(275.007812,2),math.log(310.542969,2),math.log(387.072266,2),math.log(508.351562,2),math.log(701.754883,2),math.log(1243.151367,2),math.log(2451.407227,2),math.log(4582.782166,2),math.log(8713.878723,2)]
t_44 = [math.log(224.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(271.000000,2),math.log(267.500000,2),math.log(262.500000,2),math.log(258.000000,2),math.log(238.312500,2),math.log(259.843750,2),math.log(324.015625,2),math.log(299.625000,2),math.log(366.992188,2),math.log(461.398438,2),math.log(663.964844,2),math.log(1058.459473,2),math.log(1833.311279,2),math.log(3275.436523,2),math.log(6286.044373,2),math.log(12176.761963,2)]
t_45 = [math.log(224.000000,2),math.log(208.000000,2),math.log(228.000000,2),math.log(262.000000,2),math.log(242.000000,2),math.log(274.500000,2),math.log(279.750000,2),math.log(243.500000,2),math.log(267.750000,2),math.log(299.031250,2),math.log(300.109375,2),math.log(383.476562,2),math.log(421.968750,2),math.log(603.671875,2),math.log(969.238281,2),math.log(1718.827148,2),math.log(3276.617432,2),math.log(6443.120728,2),math.log(12576.037903,2),math.log(25568.706970,2)]
t_46 = [math.log(240.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(266.500000,2),math.log(291.125000,2),math.log(291.875000,2),math.log(300.406250,2),math.log(337.875000,2),math.log(378.601562,2),math.log(444.585938,2),math.log(669.550781,2),math.log(1063.595703,2),math.log(2028.273438,2),math.log(3900.908447,2),math.log(7209.668945,2),math.log(14159.729065,2),math.log(27967.975067,2)]
t_47 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(274.000000,2),math.log(266.500000,2),math.log(264.000000,2),math.log(258.000000,2),math.log(219.875000,2),math.log(273.593750,2),math.log(245.859375,2),math.log(289.312500,2),math.log(337.839844,2),math.log(466.722656,2),math.log(666.954102,2),math.log(1006.473633,2),math.log(1638.739990,2),math.log(3013.850342,2),math.log(5761.250000,2),math.log(11213.777283,2)]
t_48 = [math.log(240.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(242.250000,2),math.log(223.375000,2),math.log(215.937500,2),math.log(237.531250,2),math.log(258.625000,2),math.log(286.953125,2),math.log(338.691406,2),math.log(436.287109,2),math.log(560.973633,2),math.log(918.640137,2),math.log(1546.521484,2),math.log(2877.733643,2),math.log(5373.281982,2),math.log(10201.052704,2)]
t_49 = [math.log(240.000000,2),math.log(288.000000,2),math.log(300.000000,2),math.log(268.000000,2),math.log(259.000000,2),math.log(283.000000,2),math.log(246.500000,2),math.log(225.750000,2),math.log(236.375000,2),math.log(254.750000,2),math.log(263.250000,2),math.log(251.960938,2),math.log(298.269531,2),math.log(321.167969,2),math.log(394.192383,2),math.log(553.556641,2),math.log(901.195801,2),math.log(1525.745483,2),math.log(2759.151062,2),math.log(5183.278748,2)]
t_50 = [math.log(272.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(232.000000,2),math.log(231.000000,2),math.log(237.000000,2),math.log(251.750000,2),math.log(258.875000,2),math.log(259.250000,2),math.log(260.781250,2),math.log(252.875000,2),math.log(266.695312,2),math.log(293.890625,2),math.log(370.457031,2),math.log(485.920898,2),math.log(744.324707,2),math.log(1227.589844,2),math.log(2191.693970,2),math.log(4300.539978,2),math.log(8181.077332,2)]
t_51 = [math.log(240.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(230.000000,2),math.log(224.000000,2),math.log(270.500000,2),math.log(284.500000,2),math.log(268.125000,2),math.log(295.312500,2),math.log(278.781250,2),math.log(320.437500,2),math.log(373.046875,2),math.log(496.460938,2),math.log(830.726562,2),math.log(1479.011719,2),math.log(2545.922363,2),math.log(4893.988525,2),math.log(9290.174194,2),math.log(18433.469299,2),math.log(36961.221863,2)]
t_52 = [math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(274.000000,2),math.log(258.000000,2),math.log(253.000000,2),math.log(250.250000,2),math.log(234.625000,2),math.log(270.562500,2),math.log(243.593750,2),math.log(272.921875,2),math.log(297.414062,2),math.log(324.867188,2),math.log(353.644531,2),math.log(459.849609,2),math.log(656.652832,2),math.log(1115.937744,2),math.log(2011.052490,2),math.log(3826.619934,2),math.log(7219.510925,2)]
t_53 = [math.log(256.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(222.000000,2),math.log(242.000000,2),math.log(213.500000,2),math.log(229.250000,2),math.log(274.125000,2),math.log(279.562500,2),math.log(282.906250,2),math.log(275.359375,2),math.log(236.546875,2),math.log(316.800781,2),math.log(407.513672,2),math.log(568.565430,2),math.log(846.221680,2),math.log(1468.836426,2),math.log(2674.393677,2),math.log(5069.528687,2),math.log(9830.452545,2)]
t_54 = [math.log(256.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(262.000000,2),math.log(246.000000,2),math.log(236.000000,2),math.log(264.000000,2),math.log(232.875000,2),math.log(276.000000,2),math.log(315.781250,2),math.log(315.984375,2),math.log(323.960938,2),math.log(363.957031,2),math.log(473.066406,2),math.log(646.863281,2),math.log(1010.994141,2),math.log(1744.931885,2),math.log(3333.665894,2),math.log(6563.426331,2),math.log(13243.041748,2)]
t_55 = [math.log(224.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(214.000000,2),math.log(231.000000,2),math.log(219.000000,2),math.log(262.250000,2),math.log(268.500000,2),math.log(276.812500,2),math.log(283.406250,2),math.log(286.671875,2),math.log(370.890625,2),math.log(419.871094,2),math.log(731.177734,2),math.log(1170.492188,2),math.log(2201.752930,2),math.log(4240.327881,2),math.log(8381.089600,2),math.log(16834.840271,2),math.log(33606.177551,2)]
t_56 = [math.log(224.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(254.500000,2),math.log(283.750000,2),math.log(298.500000,2),math.log(295.375000,2),math.log(331.875000,2),math.log(317.078125,2),math.log(340.617188,2),math.log(418.578125,2),math.log(657.007812,2),math.log(967.704102,2),math.log(1598.393066,2),math.log(2838.410400,2),math.log(5293.032227,2),math.log(10156.362122,2),math.log(20269.739624,2)]
t_57 = [math.log(224.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(241.000000,2),math.log(268.000000,2),math.log(302.750000,2),math.log(266.125000,2),math.log(255.687500,2),math.log(275.781250,2),math.log(325.656250,2),math.log(356.914062,2),math.log(372.750000,2),math.log(519.773438,2),math.log(787.435547,2),math.log(1246.759277,2),math.log(2386.320068,2),math.log(4503.018799,2),math.log(8701.996643,2),math.log(17397.981659,2)]
t_58 = [math.log(272.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(281.000000,2),math.log(272.000000,2),math.log(265.125000,2),math.log(316.500000,2),math.log(335.375000,2),math.log(355.718750,2),math.log(519.273438,2),math.log(825.421875,2),math.log(1334.050781,2),math.log(2446.366211,2),math.log(4612.859375,2),math.log(8709.616455,2),math.log(17003.584839,2),math.log(33847.805908,2),math.log(68300.879608,2)]
t_59 = [math.log(224.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(272.000000,2),math.log(251.000000,2),math.log(271.000000,2),math.log(283.500000,2),math.log(289.875000,2),math.log(285.937500,2),math.log(274.250000,2),math.log(377.000000,2),math.log(469.992188,2),math.log(673.343750,2),math.log(1110.148438,2),math.log(1980.285156,2),math.log(3614.445312,2),math.log(7093.692139,2),math.log(13980.449219,2),math.log(27708.367004,2),math.log(55571.525024,2)]
t_60 = [math.log(256.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(286.000000,2),math.log(249.000000,2),math.log(279.000000,2),math.log(265.750000,2),math.log(254.750000,2),math.log(261.687500,2),math.log(267.000000,2),math.log(272.281250,2),math.log(346.046875,2),math.log(465.535156,2),math.log(677.226562,2),math.log(970.349609,2),math.log(1699.095703,2),math.log(3098.858643,2),math.log(5932.304443,2),math.log(11719.058960,2),math.log(22738.087799,2)]
t_61 = [math.log(224.000000,2),math.log(232.000000,2),math.log(304.000000,2),math.log(290.000000,2),math.log(289.000000,2),math.log(259.000000,2),math.log(272.250000,2),math.log(250.000000,2),math.log(256.250000,2),math.log(289.593750,2),math.log(322.593750,2),math.log(388.851562,2),math.log(482.488281,2),math.log(749.349609,2),math.log(1329.342773,2),math.log(2302.453613,2),math.log(4568.268066,2),math.log(8785.310181,2),math.log(17393.295593,2),math.log(34035.421631,2)]
t_62 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(234.000000,2),math.log(230.000000,2),math.log(219.500000,2),math.log(248.750000,2),math.log(280.000000,2),math.log(266.375000,2),math.log(286.718750,2),math.log(272.437500,2),math.log(349.921875,2),math.log(507.019531,2),math.log(756.982422,2),math.log(1310.634766,2),math.log(2547.558105,2),math.log(4853.463379,2),math.log(9696.594482,2),math.log(19030.919067,2),math.log(37190.061707,2)]
t_63 = [math.log(256.000000,2),math.log(264.000000,2),math.log(220.000000,2),math.log(258.000000,2),math.log(246.000000,2),math.log(256.000000,2),math.log(235.000000,2),math.log(240.375000,2),math.log(272.250000,2),math.log(341.000000,2),math.log(362.546875,2),math.log(440.296875,2),math.log(629.113281,2),math.log(1050.523438,2),math.log(1874.894531,2),math.log(3605.333496,2),math.log(7007.264893,2),math.log(13711.692749,2),math.log(27905.251221,2),math.log(55184.107910,2)]
t_64 = [math.log(256.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(274.000000,2),math.log(290.500000,2),math.log(283.000000,2),math.log(277.250000,2),math.log(260.500000,2),math.log(263.750000,2),math.log(260.046875,2),math.log(298.218750,2),math.log(350.707031,2),math.log(405.037109,2),math.log(553.854492,2),math.log(895.786133,2),math.log(1499.889893,2),math.log(2682.670288,2),math.log(4977.401733,2),math.log(9845.022827,2)]
t_65 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(227.000000,2),math.log(241.000000,2),math.log(243.750000,2),math.log(237.250000,2),math.log(257.562500,2),math.log(256.718750,2),math.log(278.265625,2),math.log(321.546875,2),math.log(414.699219,2),math.log(526.904297,2),math.log(798.791016,2),math.log(1437.237305,2),math.log(2543.657959,2),math.log(5029.822388,2),math.log(9613.275574,2),math.log(18824.005585,2)]
t_66 = [math.log(272.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(254.000000,2),math.log(280.500000,2),math.log(234.000000,2),math.log(221.750000,2),math.log(221.062500,2),math.log(261.437500,2),math.log(268.625000,2),math.log(310.953125,2),math.log(433.527344,2),math.log(601.353516,2),math.log(872.802734,2),math.log(1525.007812,2),math.log(2825.705322,2),math.log(5285.764038,2),math.log(10215.844788,2),math.log(20046.694031,2)]
t_67 = [math.log(240.000000,2),math.log(216.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(259.000000,2),math.log(288.000000,2),math.log(264.250000,2),math.log(279.625000,2),math.log(295.437500,2),math.log(279.718750,2),math.log(311.906250,2),math.log(331.171875,2),math.log(360.832031,2),math.log(507.306641,2),math.log(687.933594,2),math.log(1057.580566,2),math.log(1929.860352,2),math.log(3606.634399,2),math.log(6871.847778,2),math.log(13677.237701,2)]
t_68 = [math.log(256.000000,2),math.log(304.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(289.000000,2),math.log(272.000000,2),math.log(210.500000,2),math.log(270.875000,2),math.log(245.375000,2),math.log(285.000000,2),math.log(333.531250,2),math.log(344.437500,2),math.log(392.960938,2),math.log(518.675781,2),math.log(752.637695,2),math.log(1233.467773,2),math.log(2103.478271,2),math.log(3926.380615,2),math.log(7636.715942,2),math.log(15052.283020,2)]
t_69 = [math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(229.000000,2),math.log(217.500000,2),math.log(244.000000,2),math.log(270.375000,2),math.log(273.875000,2),math.log(295.125000,2),math.log(302.906250,2),math.log(341.484375,2),math.log(422.601562,2),math.log(656.882812,2),math.log(1034.010742,2),math.log(1706.501953,2),math.log(3414.011230,2),math.log(6695.201904,2),math.log(13435.955322,2),math.log(26594.831238,2)]
t_70 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(287.500000,2),math.log(310.000000,2),math.log(269.000000,2),math.log(260.437500,2),math.log(275.906250,2),math.log(299.687500,2),math.log(361.156250,2),math.log(503.835938,2),math.log(823.000000,2),math.log(1383.989258,2),math.log(2380.359863,2),math.log(4468.570312,2),math.log(8589.836914,2),math.log(16716.865051,2),math.log(33331.033600,2)]
t_71 = [math.log(256.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(278.500000,2),math.log(279.250000,2),math.log(279.250000,2),math.log(246.500000,2),math.log(309.656250,2),math.log(247.796875,2),math.log(294.898438,2),math.log(416.464844,2),math.log(490.298828,2),math.log(729.557617,2),math.log(1088.426270,2),math.log(1953.852295,2),math.log(3675.078735,2),math.log(7004.357788,2),math.log(13567.382782,2)]
t_72 = [math.log(256.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(250.000000,2),math.log(295.000000,2),math.log(293.000000,2),math.log(262.250000,2),math.log(254.875000,2),math.log(264.500000,2),math.log(266.343750,2),math.log(282.390625,2),math.log(330.750000,2),math.log(375.281250,2),math.log(497.529297,2),math.log(723.951172,2),math.log(1025.150879,2),math.log(1850.948242,2),math.log(3368.023926,2),math.log(6272.369202,2),math.log(12343.398560,2)]
t_73 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(304.000000,2),math.log(314.000000,2),math.log(281.000000,2),math.log(270.000000,2),math.log(258.125000,2),math.log(246.875000,2),math.log(261.656250,2),math.log(283.125000,2),math.log(320.703125,2),math.log(432.289062,2),math.log(623.875000,2),math.log(1056.615234,2),math.log(1805.776855,2),math.log(3335.806885,2),math.log(6592.199707,2),math.log(12851.728455,2),math.log(25412.010376,2)]
t_74 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(258.000000,2),math.log(248.000000,2),math.log(259.000000,2),math.log(300.750000,2),math.log(298.500000,2),math.log(320.062500,2),math.log(321.000000,2),math.log(372.281250,2),math.log(476.781250,2),math.log(654.980469,2),math.log(1055.123047,2),math.log(1914.958008,2),math.log(3471.442383,2),math.log(6604.447754,2),math.log(13104.768311,2),math.log(26223.609131,2),math.log(52711.565918,2)]
t_75 = [math.log(272.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(252.000000,2),math.log(262.000000,2),math.log(244.000000,2),math.log(273.000000,2),math.log(268.875000,2),math.log(301.750000,2),math.log(301.218750,2),math.log(336.500000,2),math.log(352.414062,2),math.log(424.203125,2),math.log(589.931641,2),math.log(917.088867,2),math.log(1593.430176,2),math.log(2762.041504,2),math.log(5422.291260,2),math.log(10515.816345,2),math.log(20177.944061,2)]
t_76 = [math.log(272.000000,2),math.log(232.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(232.000000,2),math.log(253.500000,2),math.log(238.250000,2),math.log(255.625000,2),math.log(268.500000,2),math.log(257.968750,2),math.log(295.859375,2),math.log(307.796875,2),math.log(384.757812,2),math.log(511.472656,2),math.log(681.085938,2),math.log(950.221680,2),math.log(1703.126465,2),math.log(3270.212891,2),math.log(6688.570312,2),math.log(12954.877686,2)]
t_77 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(232.000000,2),math.log(267.000000,2),math.log(247.000000,2),math.log(268.000000,2),math.log(295.875000,2),math.log(285.437500,2),math.log(277.718750,2),math.log(314.187500,2),math.log(346.359375,2),math.log(447.183594,2),math.log(673.867188,2),math.log(1143.670898,2),math.log(1977.020996,2),math.log(3747.366211,2),math.log(7142.618774,2),math.log(14179.563660,2),math.log(28256.589661,2)]
t_78 = [math.log(288.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(207.000000,2),math.log(206.750000,2),math.log(223.125000,2),math.log(249.625000,2),math.log(274.093750,2),math.log(278.375000,2),math.log(362.335938,2),math.log(536.644531,2),math.log(833.078125,2),math.log(1362.967773,2),math.log(2338.097168,2),math.log(4384.761719,2),math.log(8488.510498,2),math.log(16663.096741,2),math.log(33813.757935,2)]
t_79 = [math.log(304.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(282.000000,2),math.log(278.000000,2),math.log(251.750000,2),math.log(254.750000,2),math.log(234.687500,2),math.log(277.156250,2),math.log(337.312500,2),math.log(388.031250,2),math.log(537.792969,2),math.log(779.101562,2),math.log(1187.815430,2),math.log(2010.936523,2),math.log(3573.247070,2),math.log(6885.447266,2),math.log(13803.205811,2),math.log(27707.319122,2)]
t_80 = [math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(233.000000,2),math.log(252.500000,2),math.log(261.000000,2),math.log(266.000000,2),math.log(276.750000,2),math.log(279.656250,2),math.log(296.828125,2),math.log(357.914062,2),math.log(414.882812,2),math.log(556.687500,2),math.log(908.901367,2),math.log(1459.525879,2),math.log(2643.533447,2),math.log(5152.198486,2),math.log(10311.967163,2),math.log(20098.416901,2)]
t_81 = [math.log(240.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(277.000000,2),math.log(268.000000,2),math.log(262.000000,2),math.log(240.625000,2),math.log(242.625000,2),math.log(259.593750,2),math.log(266.437500,2),math.log(317.328125,2),math.log(391.515625,2),math.log(526.560547,2),math.log(851.389648,2),math.log(1401.511719,2),math.log(2698.267822,2),math.log(5156.713989,2),math.log(10291.781494,2),math.log(20149.056641,2)]
t_82 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(231.000000,2),math.log(228.000000,2),math.log(263.750000,2),math.log(241.125000,2),math.log(255.000000,2),math.log(240.000000,2),math.log(253.109375,2),math.log(364.757812,2),math.log(440.546875,2),math.log(553.205078,2),math.log(908.397461,2),math.log(1532.656738,2),math.log(2572.977051,2),math.log(5055.104248,2),math.log(9833.724060,2),math.log(19770.990356,2)]
t_83 = [math.log(256.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(276.000000,2),math.log(269.000000,2),math.log(241.000000,2),math.log(218.250000,2),math.log(236.375000,2),math.log(270.062500,2),math.log(314.562500,2),math.log(305.968750,2),math.log(347.179688,2),math.log(424.703125,2),math.log(639.177734,2),math.log(968.452148,2),math.log(1652.663574,2),math.log(2981.301025,2),math.log(5847.348999,2),math.log(11275.626465,2),math.log(22421.126068,2)]
t_84 = [math.log(240.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(258.000000,2),math.log(287.000000,2),math.log(245.500000,2),math.log(241.250000,2),math.log(255.375000,2),math.log(228.562500,2),math.log(258.375000,2),math.log(263.640625,2),math.log(292.515625,2),math.log(332.125000,2),math.log(448.214844,2),math.log(685.881836,2),math.log(1157.916504,2),math.log(2200.185059,2),math.log(4136.065674,2),math.log(7785.129395,2),math.log(15131.300781,2)]
t_85 = [math.log(272.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(245.000000,2),math.log(229.000000,2),math.log(273.500000,2),math.log(232.250000,2),math.log(246.687500,2),math.log(256.375000,2),math.log(280.656250,2),math.log(327.992188,2),math.log(406.722656,2),math.log(590.980469,2),math.log(966.714844,2),math.log(1689.663086,2),math.log(3182.255127,2),math.log(6148.111328,2),math.log(11997.333557,2),math.log(22825.179108,2)]
t_86 = [math.log(224.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(243.000000,2),math.log(300.000000,2),math.log(281.750000,2),math.log(256.750000,2),math.log(272.687500,2),math.log(265.843750,2),math.log(314.390625,2),math.log(374.460938,2),math.log(472.882812,2),math.log(692.500000,2),math.log(1081.790039,2),math.log(1882.241211,2),math.log(3480.418457,2),math.log(6713.386230,2),math.log(13077.110168,2),math.log(26017.626038,2)]
t_87 = [math.log(272.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(254.000000,2),math.log(212.000000,2),math.log(237.000000,2),math.log(243.000000,2),math.log(255.750000,2),math.log(253.750000,2),math.log(284.843750,2),math.log(314.968750,2),math.log(316.164062,2),math.log(436.820312,2),math.log(594.996094,2),math.log(909.728516,2),math.log(1596.722168,2),math.log(2871.263916,2),math.log(5394.161133,2),math.log(10749.751282,2),math.log(21058.930389,2)]
t_88 = [math.log(240.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(264.000000,2),math.log(269.500000,2),math.log(296.500000,2),math.log(262.250000,2),math.log(288.625000,2),math.log(288.000000,2),math.log(233.000000,2),math.log(317.671875,2),math.log(344.707031,2),math.log(430.699219,2),math.log(800.228516,2),math.log(1305.490723,2),math.log(2386.083008,2),math.log(4647.388306,2),math.log(9181.798767,2),math.log(17745.772797,2)]
t_89 = [math.log(288.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(294.000000,2),math.log(254.000000,2),math.log(244.000000,2),math.log(222.750000,2),math.log(238.500000,2),math.log(287.500000,2),math.log(318.843750,2),math.log(327.546875,2),math.log(366.976562,2),math.log(485.250000,2),math.log(648.847656,2),math.log(1046.611328,2),math.log(1781.872559,2),math.log(3409.886719,2),math.log(6425.800293,2),math.log(12804.658020,2),math.log(25725.418610,2)]
t_90 = [math.log(256.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(282.000000,2),math.log(237.000000,2),math.log(221.000000,2),math.log(255.250000,2),math.log(269.000000,2),math.log(286.437500,2),math.log(314.218750,2),math.log(384.671875,2),math.log(473.625000,2),math.log(607.570312,2),math.log(992.460938,2),math.log(1880.019531,2),math.log(3654.749512,2),math.log(7011.345215,2),math.log(13756.033081,2),math.log(27190.007202,2),math.log(54342.217377,2)]
t_91 = [math.log(272.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(235.000000,2),math.log(263.000000,2),math.log(244.250000,2),math.log(268.250000,2),math.log(283.562500,2),math.log(315.375000,2),math.log(315.578125,2),math.log(339.554688,2),math.log(453.875000,2),math.log(736.250000,2),math.log(1211.451172,2),math.log(2217.372559,2),math.log(4383.732910,2),math.log(8835.830200,2),math.log(17273.253296,2),math.log(33761.845520,2)]
t_92 = [math.log(288.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(234.000000,2),math.log(249.000000,2),math.log(247.000000,2),math.log(237.000000,2),math.log(253.875000,2),math.log(271.000000,2),math.log(267.968750,2),math.log(277.437500,2),math.log(318.742188,2),math.log(413.371094,2),math.log(549.193359,2),math.log(836.076172,2),math.log(1499.703125,2),math.log(2742.230469,2),math.log(5138.190063,2),math.log(10472.459106,2),math.log(20555.727051,2)]
t_93 = [math.log(272.000000,2),math.log(320.000000,2),math.log(308.000000,2),math.log(236.000000,2),math.log(273.000000,2),math.log(284.500000,2),math.log(251.500000,2),math.log(245.375000,2),math.log(264.625000,2),math.log(282.937500,2),math.log(342.656250,2),math.log(393.343750,2),math.log(537.078125,2),math.log(723.035156,2),math.log(1312.993164,2),math.log(2398.814453,2),math.log(4488.035400,2),math.log(8625.827393,2),math.log(17408.281982,2),math.log(34346.445679,2)]
t_94 = [math.log(256.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(242.000000,2),math.log(258.000000,2),math.log(267.000000,2),math.log(267.000000,2),math.log(251.750000,2),math.log(280.000000,2),math.log(318.343750,2),math.log(337.328125,2),math.log(399.546875,2),math.log(567.902344,2),math.log(868.212891,2),math.log(1513.598633,2),math.log(2687.043945,2),math.log(5211.522705,2),math.log(10529.857422,2),math.log(20865.046448,2),math.log(41276.580597,2)]
t_95 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(276.000000,2),math.log(268.500000,2),math.log(254.750000,2),math.log(253.125000,2),math.log(259.250000,2),math.log(276.656250,2),math.log(318.859375,2),math.log(406.140625,2),math.log(515.417969,2),math.log(694.921875,2),math.log(1251.738281,2),math.log(2241.497559,2),math.log(4174.601807,2),math.log(8213.748047,2),math.log(16237.468628,2),math.log(32069.275330,2)]
t_96 = [math.log(224.000000,2),math.log(264.000000,2),math.log(296.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(244.500000,2),math.log(225.500000,2),math.log(278.875000,2),math.log(268.062500,2),math.log(251.906250,2),math.log(277.406250,2),math.log(308.320312,2),math.log(409.621094,2),math.log(549.267578,2),math.log(792.910156,2),math.log(1347.689941,2),math.log(2524.967285,2),math.log(4819.154663,2),math.log(9444.470947,2),math.log(18774.774689,2)]
t_97 = [math.log(272.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(269.000000,2),math.log(272.000000,2),math.log(245.250000,2),math.log(272.625000,2),math.log(249.125000,2),math.log(259.531250,2),math.log(306.578125,2),math.log(341.726562,2),math.log(482.671875,2),math.log(689.380859,2),math.log(1127.211914,2),math.log(1755.886719,2),math.log(3173.611572,2),math.log(6288.393555,2),math.log(12100.638306,2),math.log(23180.593842,2)]
t_98 = [math.log(256.000000,2),math.log(296.000000,2),math.log(268.000000,2),math.log(230.000000,2),math.log(229.000000,2),math.log(227.500000,2),math.log(204.750000,2),math.log(241.000000,2),math.log(226.187500,2),math.log(245.000000,2),math.log(302.281250,2),math.log(346.890625,2),math.log(479.355469,2),math.log(661.500000,2),math.log(1115.080078,2),math.log(1918.017578,2),math.log(3509.334229,2),math.log(6463.085083,2),math.log(12589.647095,2),math.log(25522.664703,2)]
t_99 = [math.log(224.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(268.000000,2),math.log(258.000000,2),math.log(259.500000,2),math.log(249.500000,2),math.log(246.125000,2),math.log(278.562500,2),math.log(273.937500,2),math.log(231.078125,2),math.log(266.242188,2),math.log(352.382812,2),math.log(465.021484,2),math.log(715.805664,2),math.log(1225.616699,2),math.log(2183.540283,2),math.log(4013.215820,2),math.log(7568.743225,2),math.log(14814.828125,2)]
t_100 = [math.log(288.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(267.000000,2),math.log(261.500000,2),math.log(246.750000,2),math.log(225.750000,2),math.log(281.125000,2),math.log(321.125000,2),math.log(332.484375,2),math.log(323.429688,2),math.log(402.605469,2),math.log(519.513672,2),math.log(737.378906,2),math.log(1288.486816,2),math.log(2344.840576,2),math.log(4319.678467,2),math.log(8371.558289,2),math.log(16430.754822,2)]
t_101 = [math.log(224.000000,2),math.log(208.000000,2),math.log(224.000000,2),math.log(246.000000,2),math.log(250.000000,2),math.log(262.000000,2),math.log(236.750000,2),math.log(273.625000,2),math.log(265.812500,2),math.log(258.375000,2),math.log(281.906250,2),math.log(352.039062,2),math.log(413.636719,2),math.log(548.835938,2),math.log(897.521484,2),math.log(1437.584473,2),math.log(2722.380371,2),math.log(5431.409058,2),math.log(10652.374390,2),math.log(21085.416748,2)]
t_102 = [math.log(272.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(230.000000,2),math.log(244.000000,2),math.log(262.500000,2),math.log(240.000000,2),math.log(245.750000,2),math.log(268.062500,2),math.log(295.468750,2),math.log(347.843750,2),math.log(430.179688,2),math.log(480.550781,2),math.log(714.542969,2),math.log(1151.663086,2),math.log(2010.152832,2),math.log(3622.834961,2),math.log(6991.532593,2),math.log(13798.596741,2),math.log(27191.850159,2)]
t_103 = [math.log(240.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(272.500000,2),math.log(283.000000,2),math.log(280.750000,2),math.log(270.187500,2),math.log(284.343750,2),math.log(330.781250,2),math.log(362.742188,2),math.log(434.789062,2),math.log(603.367188,2),math.log(896.285156,2),math.log(1336.045410,2),math.log(2478.326416,2),math.log(4566.300903,2),math.log(8828.767029,2),math.log(17562.858276,2)]
t_104 = [math.log(240.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(223.000000,2),math.log(249.500000,2),math.log(230.500000,2),math.log(246.000000,2),math.log(258.625000,2),math.log(260.875000,2),math.log(305.140625,2),math.log(332.921875,2),math.log(398.777344,2),math.log(483.054688,2),math.log(713.041992,2),math.log(1206.189453,2),math.log(2149.697998,2),math.log(3852.170532,2),math.log(7355.759827,2),math.log(14484.438843,2)]
t_105 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(249.000000,2),math.log(276.500000,2),math.log(306.500000,2),math.log(262.250000,2),math.log(264.625000,2),math.log(263.062500,2),math.log(287.718750,2),math.log(347.507812,2),math.log(452.976562,2),math.log(533.689453,2),math.log(893.798828,2),math.log(1474.138672,2),math.log(2741.257080,2),math.log(5295.675049,2),math.log(10365.195129,2),math.log(20551.341553,2)]
t_106 = [math.log(240.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(230.000000,2),math.log(253.000000,2),math.log(259.500000,2),math.log(257.500000,2),math.log(280.375000,2),math.log(292.437500,2),math.log(292.187500,2),math.log(347.546875,2),math.log(466.070312,2),math.log(587.386719,2),math.log(964.578125,2),math.log(1726.612305,2),math.log(3228.772949,2),math.log(6323.656006,2),math.log(12334.771973,2),math.log(24464.805481,2),math.log(48282.780792,2)]
t_107 = [math.log(256.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(274.000000,2),math.log(279.000000,2),math.log(261.500000,2),math.log(257.250000,2),math.log(229.000000,2),math.log(236.562500,2),math.log(233.125000,2),math.log(272.859375,2),math.log(342.390625,2),math.log(439.429688,2),math.log(583.822266,2),math.log(892.232422,2),math.log(1553.059570,2),math.log(2719.339111,2),math.log(5356.512573,2),math.log(10684.149597,2),math.log(20834.774536,2)]
t_108 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(214.000000,2),math.log(198.000000,2),math.log(212.000000,2),math.log(243.500000,2),math.log(250.375000,2),math.log(237.875000,2),math.log(237.906250,2),math.log(281.796875,2),math.log(326.960938,2),math.log(410.917969,2),math.log(586.537109,2),math.log(972.313477,2),math.log(1579.604980,2),math.log(2921.960693,2),math.log(5732.742676,2),math.log(11168.544189,2),math.log(22299.132935,2)]
t_109 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(228.000000,2),math.log(258.500000,2),math.log(235.750000,2),math.log(274.875000,2),math.log(309.000000,2),math.log(317.687500,2),math.log(350.343750,2),math.log(388.687500,2),math.log(521.070312,2),math.log(877.794922,2),math.log(1569.586914,2),math.log(3017.994629,2),math.log(5530.201172,2),math.log(10790.729980,2),math.log(21087.651062,2),math.log(42103.317505,2)]
t_110 = [math.log(240.000000,2),math.log(232.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(294.000000,2),math.log(264.000000,2),math.log(284.250000,2),math.log(252.125000,2),math.log(241.937500,2),math.log(263.593750,2),math.log(317.421875,2),math.log(364.625000,2),math.log(541.464844,2),math.log(864.132812,2),math.log(1671.478516,2),math.log(3094.711426,2),math.log(6067.541748,2),math.log(12048.140259,2),math.log(23699.306580,2),math.log(48026.726288,2)]
t_111 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(271.000000,2),math.log(276.500000,2),math.log(269.000000,2),math.log(230.000000,2),math.log(281.750000,2),math.log(255.312500,2),math.log(302.375000,2),math.log(336.593750,2),math.log(455.539062,2),math.log(651.687500,2),math.log(1091.305664,2),math.log(1812.483398,2),math.log(3273.345703,2),math.log(6236.387329,2),math.log(12193.513489,2),math.log(24858.811890,2)]
t_112 = [math.log(224.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(245.000000,2),math.log(262.500000,2),math.log(274.500000,2),math.log(274.625000,2),math.log(256.375000,2),math.log(288.187500,2),math.log(263.140625,2),math.log(289.390625,2),math.log(415.566406,2),math.log(559.443359,2),math.log(759.334961,2),math.log(1336.134277,2),math.log(2324.083740,2),math.log(4405.295532,2),math.log(8714.633911,2),math.log(17070.220673,2)]
t_113 = [math.log(240.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(246.500000,2),math.log(273.250000,2),math.log(272.250000,2),math.log(295.687500,2),math.log(266.125000,2),math.log(270.640625,2),math.log(292.062500,2),math.log(306.363281,2),math.log(361.294922,2),math.log(546.946289,2),math.log(772.145020,2),math.log(1279.448242,2),math.log(2422.319702,2),math.log(4571.870300,2),math.log(9071.039246,2)]
t_114 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(238.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(223.500000,2),math.log(241.250000,2),math.log(248.562500,2),math.log(238.656250,2),math.log(252.625000,2),math.log(293.281250,2),math.log(327.921875,2),math.log(374.923828,2),math.log(567.103516,2),math.log(947.402344,2),math.log(1564.256836,2),math.log(2877.390869,2),math.log(5569.412109,2),math.log(11122.074188,2)]
t_115 = [math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(241.000000,2),math.log(301.500000,2),math.log(298.000000,2),math.log(284.875000,2),math.log(316.312500,2),math.log(347.593750,2),math.log(392.500000,2),math.log(475.312500,2),math.log(626.855469,2),math.log(859.351562,2),math.log(1471.275391,2),math.log(2853.536133,2),math.log(5775.412598,2),math.log(11054.228027,2),math.log(21887.887207,2),math.log(43285.485840,2)]
t_116 = [math.log(224.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(258.000000,2),math.log(255.500000,2),math.log(213.000000,2),math.log(231.125000,2),math.log(244.062500,2),math.log(255.156250,2),math.log(282.703125,2),math.log(297.031250,2),math.log(347.988281,2),math.log(443.908203,2),math.log(604.187500,2),math.log(948.569824,2),math.log(1686.860840,2),math.log(3112.640747,2),math.log(5765.861633,2),math.log(11588.301788,2)]
t_117 = [math.log(256.000000,2),math.log(280.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(269.000000,2),math.log(264.000000,2),math.log(259.000000,2),math.log(232.000000,2),math.log(248.812500,2),math.log(290.156250,2),math.log(266.765625,2),math.log(314.617188,2),math.log(372.625000,2),math.log(499.519531,2),math.log(758.208984,2),math.log(1214.125977,2),math.log(2199.831055,2),math.log(4235.476440,2),math.log(8046.340332,2),math.log(15673.483124,2)]
t_118 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(270.000000,2),math.log(256.000000,2),math.log(254.500000,2),math.log(250.500000,2),math.log(262.500000,2),math.log(263.187500,2),math.log(300.406250,2),math.log(316.687500,2),math.log(375.085938,2),math.log(469.343750,2),math.log(579.871094,2),math.log(871.935547,2),math.log(1397.125977,2),math.log(2458.786133,2),math.log(4764.534058,2),math.log(9415.809387,2),math.log(18414.102325,2)]
t_119 = [math.log(224.000000,2),math.log(200.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(249.000000,2),math.log(246.500000,2),math.log(273.750000,2),math.log(277.875000,2),math.log(276.500000,2),math.log(327.625000,2),math.log(315.484375,2),math.log(375.390625,2),math.log(543.179688,2),math.log(848.238281,2),math.log(1510.637695,2),math.log(2837.148926,2),math.log(5221.162598,2),math.log(10535.666504,2),math.log(20875.946228,2),math.log(41139.449951,2)]
t_120 = [math.log(272.000000,2),math.log(256.000000,2),math.log(224.000000,2),math.log(208.000000,2),math.log(268.000000,2),math.log(263.500000,2),math.log(237.000000,2),math.log(263.125000,2),math.log(300.312500,2),math.log(315.531250,2),math.log(330.609375,2),math.log(369.757812,2),math.log(400.625000,2),math.log(515.435547,2),math.log(806.432617,2),math.log(1357.938965,2),math.log(2449.436523,2),math.log(4655.614258,2),math.log(9320.504395,2),math.log(18329.656738,2)]
t_121 = [math.log(288.000000,2),math.log(320.000000,2),math.log(260.000000,2),math.log(288.000000,2),math.log(251.000000,2),math.log(244.000000,2),math.log(204.250000,2),math.log(231.375000,2),math.log(240.000000,2),math.log(251.250000,2),math.log(253.375000,2),math.log(296.453125,2),math.log(398.906250,2),math.log(554.630859,2),math.log(772.551758,2),math.log(1315.505859,2),math.log(2374.279053,2),math.log(4368.947754,2),math.log(8367.654297,2),math.log(16893.620239,2)]
t_122 = [math.log(288.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(298.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(290.500000,2),math.log(294.500000,2),math.log(324.875000,2),math.log(344.062500,2),math.log(420.000000,2),math.log(549.460938,2),math.log(780.253906,2),math.log(1232.648438,2),math.log(2253.450195,2),math.log(4195.003418,2),math.log(8114.259033,2),math.log(15936.080811,2),math.log(31829.491211,2),math.log(62768.021362,2)]
t_123 = [math.log(272.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(278.000000,2),math.log(288.000000,2),math.log(290.500000,2),math.log(283.750000,2),math.log(274.875000,2),math.log(271.437500,2),math.log(333.531250,2),math.log(424.640625,2),math.log(543.585938,2),math.log(803.820312,2),math.log(1287.130859,2),math.log(2296.462891,2),math.log(4199.748047,2),math.log(8113.079102,2),math.log(16052.366455,2),math.log(31448.552307,2),math.log(63457.174347,2)]
t_124 = [math.log(256.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(278.000000,2),math.log(263.000000,2),math.log(236.000000,2),math.log(245.750000,2),math.log(267.250000,2),math.log(269.250000,2),math.log(266.281250,2),math.log(331.328125,2),math.log(439.734375,2),math.log(573.421875,2),math.log(832.445312,2),math.log(1416.433594,2),math.log(2548.365723,2),math.log(4796.946289,2),math.log(9480.496826,2),math.log(18749.942261,2),math.log(37622.101440,2)]
t_125 = [math.log(256.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(238.000000,2),math.log(250.000000,2),math.log(295.000000,2),math.log(246.250000,2),math.log(253.125000,2),math.log(264.937500,2),math.log(299.656250,2),math.log(331.437500,2),math.log(428.179688,2),math.log(647.476562,2),math.log(1037.132812,2),math.log(1704.230469,2),math.log(3120.576660,2),math.log(6156.941406,2),math.log(11894.711182,2),math.log(23863.454041,2),math.log(46900.608276,2)]
t_126 = [math.log(288.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(238.000000,2),math.log(270.000000,2),math.log(267.500000,2),math.log(305.250000,2),math.log(291.125000,2),math.log(300.000000,2),math.log(315.593750,2),math.log(416.359375,2),math.log(508.773438,2),math.log(716.003906,2),math.log(1099.720703,2),math.log(1811.602539,2),math.log(3271.944824,2),math.log(6419.768799,2),math.log(12626.789185,2),math.log(25111.446655,2),math.log(50618.530457,2)]
t_127 = [math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(206.000000,2),math.log(226.000000,2),math.log(228.000000,2),math.log(219.500000,2),math.log(260.500000,2),math.log(316.062500,2),math.log(319.625000,2),math.log(323.328125,2),math.log(498.671875,2),math.log(743.332031,2),math.log(1190.720703,2),math.log(2000.384766,2),math.log(3730.541992,2),math.log(7206.886963,2),math.log(14149.762939,2),math.log(27792.311218,2),math.log(54995.915009,2)]
t_128 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(233.500000,2),math.log(221.500000,2),math.log(293.625000,2),math.log(270.625000,2),math.log(291.437500,2),math.log(268.546875,2),math.log(337.250000,2),math.log(309.824219,2),math.log(355.011719,2),math.log(440.052734,2),math.log(600.714355,2),math.log(861.718506,2),math.log(1488.414673,2),math.log(2565.842407,2),math.log(4817.083588,2)]
t_129 = [math.log(272.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(285.000000,2),math.log(283.000000,2),math.log(254.500000,2),math.log(282.875000,2),math.log(318.000000,2),math.log(293.531250,2),math.log(269.265625,2),math.log(300.507812,2),math.log(298.441406,2),math.log(389.556641,2),math.log(632.929688,2),math.log(992.541016,2),math.log(1765.231201,2),math.log(3380.511353,2),math.log(6187.998962,2),math.log(11995.052277,2)]
t_130 = [math.log(240.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(234.000000,2),math.log(289.000000,2),math.log(256.500000,2),math.log(283.500000,2),math.log(278.750000,2),math.log(283.187500,2),math.log(287.843750,2),math.log(251.734375,2),math.log(288.265625,2),math.log(346.035156,2),math.log(409.845703,2),math.log(566.486328,2),math.log(904.197266,2),math.log(1525.637451,2),math.log(2703.189331,2),math.log(5122.974365,2),math.log(9944.886383,2)]
t_131 = [math.log(224.000000,2),math.log(224.000000,2),math.log(212.000000,2),math.log(242.000000,2),math.log(285.000000,2),math.log(291.500000,2),math.log(306.750000,2),math.log(287.125000,2),math.log(259.562500,2),math.log(265.687500,2),math.log(308.078125,2),math.log(318.726562,2),math.log(337.816406,2),math.log(489.414062,2),math.log(668.572266,2),math.log(1137.803711,2),math.log(1929.203857,2),math.log(3467.230469,2),math.log(6593.801270,2),math.log(12826.144226,2)]
t_132 = [math.log(224.000000,2),math.log(248.000000,2),math.log(292.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(210.000000,2),math.log(229.500000,2),math.log(250.875000,2),math.log(256.500000,2),math.log(285.000000,2),math.log(277.390625,2),math.log(296.812500,2),math.log(313.160156,2),math.log(385.810547,2),math.log(577.531250,2),math.log(765.963867,2),math.log(1226.219971,2),math.log(2249.336670,2),math.log(4339.850098,2),math.log(8505.172272,2)]
t_133 = [math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(242.000000,2),math.log(244.000000,2),math.log(227.000000,2),math.log(252.500000,2),math.log(241.250000,2),math.log(252.312500,2),math.log(259.375000,2),math.log(269.718750,2),math.log(296.828125,2),math.log(388.160156,2),math.log(511.109375,2),math.log(728.209961,2),math.log(1145.871094,2),math.log(1962.003906,2),math.log(3712.846436,2),math.log(7182.867676,2),math.log(14078.545319,2)]
t_134 = [math.log(288.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(294.000000,2),math.log(275.000000,2),math.log(250.000000,2),math.log(261.250000,2),math.log(257.875000,2),math.log(311.250000,2),math.log(314.250000,2),math.log(319.921875,2),math.log(344.421875,2),math.log(437.765625,2),math.log(664.023438,2),math.log(1188.885742,2),math.log(2039.085938,2),math.log(3704.269287,2),math.log(7394.670288,2),math.log(14665.106018,2),math.log(28930.970215,2)]
t_135 = [math.log(256.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(274.000000,2),math.log(327.000000,2),math.log(287.000000,2),math.log(276.750000,2),math.log(252.750000,2),math.log(260.750000,2),math.log(262.281250,2),math.log(256.500000,2),math.log(275.054688,2),math.log(336.566406,2),math.log(398.689453,2),math.log(484.080078,2),math.log(705.796387,2),math.log(1054.667725,2),math.log(1909.566284,2),math.log(3701.295044,2),math.log(7262.710785,2)]
t_136 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(263.500000,2),math.log(251.750000,2),math.log(271.875000,2),math.log(257.750000,2),math.log(245.093750,2),math.log(292.265625,2),math.log(323.820312,2),math.log(384.070312,2),math.log(499.169922,2),math.log(759.513672,2),math.log(1176.880859,2),math.log(2021.921875,2),math.log(3758.576172,2),math.log(7298.601318,2),math.log(14177.532074,2)]
t_137 = [math.log(272.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(241.000000,2),math.log(254.500000,2),math.log(233.000000,2),math.log(236.375000,2),math.log(253.437500,2),math.log(312.031250,2),math.log(316.281250,2),math.log(359.335938,2),math.log(495.105469,2),math.log(754.996094,2),math.log(1218.177734,2),math.log(2123.759766,2),math.log(3950.006104,2),math.log(7735.306641,2),math.log(15628.124146,2),math.log(30784.156372,2)]
t_138 = [math.log(288.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(325.000000,2),math.log(277.500000,2),math.log(283.750000,2),math.log(294.000000,2),math.log(298.062500,2),math.log(322.812500,2),math.log(380.562500,2),math.log(514.335938,2),math.log(778.347656,2),math.log(1265.134766,2),math.log(2356.021484,2),math.log(4429.991699,2),math.log(8618.283936,2),math.log(16887.234985,2),math.log(33351.911255,2),math.log(65681.636200,2)]
t_139 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(277.000000,2),math.log(265.000000,2),math.log(282.500000,2),math.log(265.750000,2),math.log(296.187500,2),math.log(349.093750,2),math.log(337.890625,2),math.log(355.648438,2),math.log(493.605469,2),math.log(697.509766,2),math.log(1009.697266,2),math.log(1703.197754,2),math.log(3060.520264,2),math.log(6084.582275,2),math.log(11605.233337,2),math.log(22102.148621,2)]
t_140 = [math.log(288.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(255.000000,2),math.log(291.500000,2),math.log(259.250000,2),math.log(276.125000,2),math.log(259.312500,2),math.log(270.781250,2),math.log(272.625000,2),math.log(283.492188,2),math.log(376.355469,2),math.log(386.986328,2),math.log(493.382812,2),math.log(786.565430,2),math.log(1245.013428,2),math.log(2218.501831,2),math.log(4320.943359,2),math.log(8633.446930,2)]
t_141 = [math.log(224.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(318.000000,2),math.log(313.000000,2),math.log(291.500000,2),math.log(320.000000,2),math.log(299.375000,2),math.log(304.000000,2),math.log(291.562500,2),math.log(302.750000,2),math.log(328.992188,2),math.log(440.367188,2),math.log(534.181641,2),math.log(755.127930,2),math.log(1308.945801,2),math.log(2346.823730,2),math.log(4255.145020,2),math.log(8430.615112,2),math.log(16649.236389,2)]
t_142 = [math.log(256.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(278.000000,2),math.log(238.000000,2),math.log(267.500000,2),math.log(262.500000,2),math.log(267.125000,2),math.log(248.250000,2),math.log(274.781250,2),math.log(312.625000,2),math.log(335.343750,2),math.log(419.722656,2),math.log(596.566406,2),math.log(950.681641,2),math.log(1555.991699,2),math.log(3054.798828,2),math.log(5805.361938,2),math.log(11048.280823,2),math.log(21833.565186,2)]
t_143 = [math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(266.000000,2),math.log(268.000000,2),math.log(253.500000,2),math.log(246.750000,2),math.log(246.250000,2),math.log(276.500000,2),math.log(301.750000,2),math.log(361.421875,2),math.log(398.507812,2),math.log(478.246094,2),math.log(673.599609,2),math.log(1172.500000,2),math.log(2058.674316,2),math.log(3727.263184,2),math.log(7314.412720,2),math.log(14409.608154,2),math.log(28721.845734,2)]
t_144 = [math.log(256.000000,2),math.log(264.000000,2),math.log(308.000000,2),math.log(330.000000,2),math.log(303.000000,2),math.log(277.500000,2),math.log(286.000000,2),math.log(274.250000,2),math.log(278.000000,2),math.log(300.375000,2),math.log(345.359375,2),math.log(404.070312,2),math.log(476.660156,2),math.log(603.689453,2),math.log(976.038086,2),math.log(1738.488770,2),math.log(3138.209473,2),math.log(6263.662964,2),math.log(12126.592041,2),math.log(23317.966095,2)]
t_145 = [math.log(240.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(256.000000,2),math.log(242.500000,2),math.log(267.250000,2),math.log(256.000000,2),math.log(237.312500,2),math.log(273.687500,2),math.log(294.140625,2),math.log(351.867188,2),math.log(425.656250,2),math.log(613.224609,2),math.log(918.871094,2),math.log(1526.306152,2),math.log(2901.169434,2),math.log(5776.059570,2),math.log(11312.662720,2),math.log(22549.527069,2)]
t_146 = [math.log(272.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(221.000000,2),math.log(277.500000,2),math.log(265.500000,2),math.log(252.750000,2),math.log(240.250000,2),math.log(268.156250,2),math.log(264.187500,2),math.log(287.765625,2),math.log(346.347656,2),math.log(493.636719,2),math.log(818.139648,2),math.log(1452.730957,2),math.log(2641.889648,2),math.log(5118.990234,2),math.log(10024.601807,2),math.log(19914.918243,2)]
t_147 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(238.000000,2),math.log(287.000000,2),math.log(224.000000,2),math.log(208.250000,2),math.log(262.125000,2),math.log(270.062500,2),math.log(288.625000,2),math.log(327.250000,2),math.log(386.171875,2),math.log(527.664062,2),math.log(762.658203,2),math.log(1243.524414,2),math.log(2193.650391,2),math.log(3913.839844,2),math.log(7497.471069,2),math.log(14877.487244,2),math.log(29594.807922,2)]
t_148 = [math.log(240.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(250.000000,2),math.log(266.000000,2),math.log(268.500000,2),math.log(249.250000,2),math.log(245.625000,2),math.log(271.375000,2),math.log(267.125000,2),math.log(293.187500,2),math.log(356.257812,2),math.log(372.613281,2),math.log(451.339844,2),math.log(671.843750,2),math.log(1182.668457,2),math.log(1965.023438,2),math.log(3455.349854,2),math.log(6714.619812,2),math.log(12986.068634,2)]
t_149 = [math.log(240.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(242.000000,2),math.log(306.000000,2),math.log(256.500000,2),math.log(285.000000,2),math.log(278.500000,2),math.log(280.812500,2),math.log(305.406250,2),math.log(289.828125,2),math.log(284.734375,2),math.log(351.949219,2),math.log(451.199219,2),math.log(810.308594,2),math.log(1395.611816,2),math.log(2558.368164,2),math.log(4769.214355,2),math.log(9360.322327,2),math.log(18362.176575,2)]
t_150 = [math.log(256.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(246.000000,2),math.log(251.000000,2),math.log(249.000000,2),math.log(252.500000,2),math.log(244.750000,2),math.log(251.437500,2),math.log(271.875000,2),math.log(279.375000,2),math.log(330.718750,2),math.log(399.105469,2),math.log(484.822266,2),math.log(775.282227,2),math.log(1248.765137,2),math.log(2274.737305,2),math.log(4225.986328,2),math.log(8436.176636,2),math.log(16616.588318,2)]
t_151 = [math.log(288.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(282.000000,2),math.log(251.500000,2),math.log(243.250000,2),math.log(276.125000,2),math.log(289.500000,2),math.log(280.968750,2),math.log(322.406250,2),math.log(339.742188,2),math.log(438.550781,2),math.log(627.277344,2),math.log(969.617188,2),math.log(1809.377930,2),math.log(3260.562256,2),math.log(6622.340210,2),math.log(12921.106201,2),math.log(25139.894318,2)]
t_152 = [math.log(256.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(262.000000,2),math.log(264.000000,2),math.log(227.500000,2),math.log(235.000000,2),math.log(257.875000,2),math.log(282.812500,2),math.log(288.437500,2),math.log(345.234375,2),math.log(416.335938,2),math.log(549.863281,2),math.log(810.574219,2),math.log(1258.956055,2),math.log(2047.188477,2),math.log(3845.929932,2),math.log(8007.405151,2),math.log(16103.860657,2),math.log(32095.255829,2)]
t_153 = [math.log(256.000000,2),math.log(248.000000,2),math.log(308.000000,2),math.log(288.000000,2),math.log(314.000000,2),math.log(289.000000,2),math.log(273.500000,2),math.log(251.750000,2),math.log(239.750000,2),math.log(260.312500,2),math.log(283.281250,2),math.log(376.734375,2),math.log(530.523438,2),math.log(760.558594,2),math.log(1217.016602,2),math.log(2336.925781,2),math.log(4528.091309,2),math.log(8946.402710,2),math.log(17610.450073,2),math.log(34527.650146,2)]
t_154 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(228.000000,2),math.log(208.000000,2),math.log(230.000000,2),math.log(242.500000,2),math.log(225.250000,2),math.log(269.562500,2),math.log(293.468750,2),math.log(309.968750,2),math.log(495.039062,2),math.log(754.710938,2),math.log(1190.070312,2),math.log(2108.328125,2),math.log(4049.269043,2),math.log(7611.801758,2),math.log(14863.467773,2),math.log(29886.510437,2),math.log(59919.217102,2)]
t_155 = [math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(275.000000,2),math.log(261.000000,2),math.log(239.500000,2),math.log(256.125000,2),math.log(240.062500,2),math.log(252.468750,2),math.log(361.578125,2),math.log(462.460938,2),math.log(661.019531,2),math.log(1097.398438,2),math.log(1960.044922,2),math.log(3658.318848,2),math.log(7164.498047,2),math.log(14123.697876,2),math.log(27988.732300,2),math.log(55915.398529,2)]
t_156 = [math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(262.000000,2),math.log(265.000000,2),math.log(272.500000,2),math.log(295.500000,2),math.log(302.500000,2),math.log(278.375000,2),math.log(263.593750,2),math.log(305.468750,2),math.log(350.273438,2),math.log(459.429688,2),math.log(738.886719,2),math.log(1198.287109,2),math.log(2012.250977,2),math.log(3793.812500,2),math.log(7276.952881,2),math.log(14126.520630,2),math.log(28268.331421,2)]
t_157 = [math.log(240.000000,2),math.log(288.000000,2),math.log(240.000000,2),math.log(292.000000,2),math.log(275.000000,2),math.log(226.500000,2),math.log(219.000000,2),math.log(275.750000,2),math.log(313.500000,2),math.log(332.437500,2),math.log(374.250000,2),math.log(420.257812,2),math.log(519.562500,2),math.log(803.193359,2),math.log(1272.278320,2),math.log(2200.896973,2),math.log(4074.071777,2),math.log(7816.262939,2),math.log(15650.280334,2),math.log(31250.888000,2)]
t_158 = [math.log(256.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(210.000000,2),math.log(207.000000,2),math.log(253.500000,2),math.log(232.750000,2),math.log(211.250000,2),math.log(229.500000,2),math.log(234.875000,2),math.log(307.734375,2),math.log(404.109375,2),math.log(632.894531,2),math.log(897.939453,2),math.log(1509.095703,2),math.log(2810.023926,2),math.log(5654.950684,2),math.log(11318.757935,2),math.log(22246.212158,2),math.log(44587.690918,2)]
t_159 = [math.log(256.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(251.500000,2),math.log(244.000000,2),math.log(257.000000,2),math.log(236.562500,2),math.log(271.468750,2),math.log(352.156250,2),math.log(412.539062,2),math.log(608.582031,2),math.log(1019.111328,2),math.log(1706.234375,2),math.log(2987.662109,2),math.log(5638.715088,2),math.log(11251.532837,2),math.log(21940.650757,2),math.log(43211.049805,2)]
t_160 = [math.log(288.000000,2),math.log(272.000000,2),math.log(224.000000,2),math.log(238.000000,2),math.log(259.000000,2),math.log(305.000000,2),math.log(291.000000,2),math.log(265.125000,2),math.log(282.750000,2),math.log(269.156250,2),math.log(264.203125,2),math.log(303.687500,2),math.log(414.703125,2),math.log(561.234375,2),math.log(837.378906,2),math.log(1468.420410,2),math.log(2588.895020,2),math.log(5128.719971,2),math.log(10286.290466,2),math.log(20832.704071,2)]
t_161 = [math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(268.000000,2),math.log(272.500000,2),math.log(293.000000,2),math.log(281.375000,2),math.log(258.687500,2),math.log(264.062500,2),math.log(312.500000,2),math.log(341.015625,2),math.log(389.367188,2),math.log(588.261719,2),math.log(912.092773,2),math.log(1443.615234,2),math.log(2774.104736,2),math.log(5445.462158,2),math.log(11144.602173,2),math.log(21952.852173,2)]
t_162 = [math.log(256.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(228.000000,2),math.log(226.000000,2),math.log(229.500000,2),math.log(255.000000,2),math.log(290.750000,2),math.log(272.000000,2),math.log(271.000000,2),math.log(280.062500,2),math.log(298.968750,2),math.log(341.894531,2),math.log(498.021484,2),math.log(777.330078,2),math.log(1360.584473,2),math.log(2381.921631,2),math.log(4543.238770,2),math.log(8651.118408,2),math.log(16934.833405,2)]
t_163 = [math.log(240.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(266.000000,2),math.log(224.000000,2),math.log(229.000000,2),math.log(210.750000,2),math.log(262.875000,2),math.log(280.000000,2),math.log(285.812500,2),math.log(275.000000,2),math.log(343.890625,2),math.log(413.300781,2),math.log(544.449219,2),math.log(831.506836,2),math.log(1535.322754,2),math.log(2666.390381,2),math.log(4819.662354,2),math.log(9138.867126,2),math.log(17996.544891,2)]
t_164 = [math.log(256.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(257.500000,2),math.log(289.750000,2),math.log(227.250000,2),math.log(275.437500,2),math.log(308.687500,2),math.log(319.687500,2),math.log(337.203125,2),math.log(381.777344,2),math.log(472.152344,2),math.log(731.801758,2),math.log(1275.407227,2),math.log(2292.105957,2),math.log(4547.105469,2),math.log(8771.365234,2),math.log(17182.807861,2)]
t_165 = [math.log(288.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(250.000000,2),math.log(238.500000,2),math.log(207.000000,2),math.log(202.000000,2),math.log(231.875000,2),math.log(279.656250,2),math.log(296.515625,2),math.log(336.328125,2),math.log(373.492188,2),math.log(542.208984,2),math.log(768.540039,2),math.log(1211.765625,2),math.log(2093.642090,2),math.log(3990.574585,2),math.log(7795.617004,2),math.log(15425.421112,2)]
t_166 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(242.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(250.750000,2),math.log(265.000000,2),math.log(263.312500,2),math.log(309.406250,2),math.log(347.812500,2),math.log(438.851562,2),math.log(511.511719,2),math.log(818.826172,2),math.log(1381.519531,2),math.log(2501.540039,2),math.log(4995.606201,2),math.log(9611.450317,2),math.log(19141.017517,2),math.log(38311.534790,2)]
t_167 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(227.000000,2),math.log(244.000000,2),math.log(290.250000,2),math.log(269.250000,2),math.log(278.312500,2),math.log(246.937500,2),math.log(277.015625,2),math.log(375.289062,2),math.log(540.484375,2),math.log(892.720703,2),math.log(1453.722656,2),math.log(2580.162598,2),math.log(4916.073486,2),math.log(9134.165283,2),math.log(18050.555908,2),math.log(35716.019989,2)]
t_168 = [math.log(272.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(262.000000,2),math.log(292.500000,2),math.log(250.750000,2),math.log(243.250000,2),math.log(274.375000,2),math.log(293.500000,2),math.log(291.359375,2),math.log(326.976562,2),math.log(417.625000,2),math.log(528.216797,2),math.log(811.673828,2),math.log(1212.164062,2),math.log(2162.377441,2),math.log(4000.842163,2),math.log(7741.203674,2),math.log(15391.238037,2)]
t_169 = [math.log(224.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(228.500000,2),math.log(246.000000,2),math.log(264.625000,2),math.log(263.875000,2),math.log(266.625000,2),math.log(317.031250,2),math.log(385.585938,2),math.log(507.105469,2),math.log(789.160156,2),math.log(1420.422852,2),math.log(2522.590820,2),math.log(4756.735352,2),math.log(9154.322266,2),math.log(17632.707336,2),math.log(35731.599609,2)]
t_170 = [math.log(224.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(269.000000,2),math.log(245.000000,2),math.log(258.500000,2),math.log(232.250000,2),math.log(232.937500,2),math.log(284.468750,2),math.log(357.171875,2),math.log(488.203125,2),math.log(690.144531,2),math.log(1083.589844,2),math.log(1758.289062,2),math.log(3192.440918,2),math.log(6307.724365,2),math.log(12334.868774,2),math.log(24571.871033,2),math.log(48772.782959,2)]
t_171 = [math.log(288.000000,2),math.log(248.000000,2),math.log(212.000000,2),math.log(250.000000,2),math.log(230.000000,2),math.log(258.000000,2),math.log(222.500000,2),math.log(219.000000,2),math.log(247.187500,2),math.log(268.687500,2),math.log(344.250000,2),math.log(385.093750,2),math.log(498.488281,2),math.log(800.650391,2),math.log(1443.059570,2),math.log(2588.187012,2),math.log(4911.167969,2),math.log(9475.790161,2),math.log(18743.236511,2),math.log(37828.958099,2)]
t_172 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(231.000000,2),math.log(220.000000,2),math.log(222.750000,2),math.log(218.875000,2),math.log(233.750000,2),math.log(292.656250,2),math.log(290.515625,2),math.log(333.734375,2),math.log(391.898438,2),math.log(624.636719,2),math.log(1027.553711,2),math.log(1845.077637,2),math.log(3362.894531,2),math.log(6402.115723,2),math.log(12385.302307,2),math.log(24784.059448,2)]
t_173 = [math.log(224.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(246.000000,2),math.log(238.000000,2),math.log(223.000000,2),math.log(229.500000,2),math.log(245.250000,2),math.log(266.375000,2),math.log(337.312500,2),math.log(353.125000,2),math.log(411.234375,2),math.log(602.984375,2),math.log(864.398438,2),math.log(1459.624023,2),math.log(2704.830566,2),math.log(5043.216797,2),math.log(9617.887329,2),math.log(19219.926941,2),math.log(38585.097595,2)]
t_174 = [math.log(304.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(254.000000,2),math.log(270.000000,2),math.log(238.000000,2),math.log(233.250000,2),math.log(241.500000,2),math.log(309.500000,2),math.log(295.875000,2),math.log(325.625000,2),math.log(378.500000,2),math.log(600.582031,2),math.log(1006.277344,2),math.log(1708.112305,2),math.log(3084.245605,2),math.log(6106.407959,2),math.log(11743.290039,2),math.log(22835.910645,2),math.log(45422.884003,2)]
t_175 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(286.000000,2),math.log(274.000000,2),math.log(272.500000,2),math.log(273.000000,2),math.log(295.250000,2),math.log(255.000000,2),math.log(305.687500,2),math.log(316.750000,2),math.log(345.609375,2),math.log(452.363281,2),math.log(730.878906,2),math.log(1232.095703,2),math.log(2121.885742,2),math.log(4010.661133,2),math.log(7641.371826,2),math.log(14648.934937,2),math.log(28631.873871,2)]
t_176 = [math.log(288.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(234.000000,2),math.log(249.000000,2),math.log(260.000000,2),math.log(217.250000,2),math.log(265.750000,2),math.log(283.062500,2),math.log(271.187500,2),math.log(270.515625,2),math.log(338.117188,2),math.log(422.093750,2),math.log(614.779297,2),math.log(1002.521484,2),math.log(1879.551758,2),math.log(3382.325439,2),math.log(6281.450073,2),math.log(12545.247742,2),math.log(25219.912811,2)]
t_177 = [math.log(256.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(227.000000,2),math.log(246.500000,2),math.log(261.750000,2),math.log(238.750000,2),math.log(230.937500,2),math.log(249.312500,2),math.log(272.609375,2),math.log(283.429688,2),math.log(314.316406,2),math.log(342.835938,2),math.log(425.570312,2),math.log(664.052246,2),math.log(1044.207520,2),math.log(1971.070068,2),math.log(3807.150696,2),math.log(7588.916687,2)]
t_178 = [math.log(224.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(262.000000,2),math.log(299.000000,2),math.log(307.500000,2),math.log(277.750000,2),math.log(266.500000,2),math.log(253.187500,2),math.log(248.531250,2),math.log(293.250000,2),math.log(306.140625,2),math.log(339.265625,2),math.log(469.775391,2),math.log(639.879883,2),math.log(951.355957,2),math.log(1720.530029,2),math.log(3265.928955,2),math.log(6207.095398,2),math.log(12502.697235,2)]
t_179 = [math.log(224.000000,2),math.log(232.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(250.000000,2),math.log(233.000000,2),math.log(246.500000,2),math.log(278.250000,2),math.log(338.312500,2),math.log(333.218750,2),math.log(396.156250,2),math.log(493.585938,2),math.log(685.453125,2),math.log(1105.328125,2),math.log(2013.974609,2),math.log(3838.527344,2),math.log(7367.406982,2),math.log(14439.266602,2),math.log(28878.372742,2),math.log(58060.788635,2)]
t_180 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(222.000000,2),math.log(246.000000,2),math.log(230.500000,2),math.log(259.500000,2),math.log(283.625000,2),math.log(250.562500,2),math.log(227.906250,2),math.log(293.984375,2),math.log(267.859375,2),math.log(340.699219,2),math.log(425.234375,2),math.log(570.786133,2),math.log(847.200684,2),math.log(1586.609131,2),math.log(2869.529053,2),math.log(5426.197083,2),math.log(10327.700500,2)]
t_181 = [math.log(224.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(238.000000,2),math.log(265.000000,2),math.log(219.500000,2),math.log(256.250000,2),math.log(249.250000,2),math.log(260.187500,2),math.log(266.218750,2),math.log(266.843750,2),math.log(269.804688,2),math.log(372.464844,2),math.log(444.148438,2),math.log(577.479492,2),math.log(902.645020,2),math.log(1527.405762,2),math.log(2760.200928,2),math.log(5444.002441,2),math.log(10615.810089,2)]
t_182 = [math.log(224.000000,2),math.log(208.000000,2),math.log(212.000000,2),math.log(236.000000,2),math.log(241.000000,2),math.log(230.500000,2),math.log(253.250000,2),math.log(267.750000,2),math.log(268.187500,2),math.log(288.906250,2),math.log(289.078125,2),math.log(305.296875,2),math.log(408.902344,2),math.log(556.857422,2),math.log(835.185547,2),math.log(1405.442871,2),math.log(2403.337158,2),math.log(4616.796875,2),math.log(9166.768066,2),math.log(18010.046478,2)]
t_183 = [math.log(256.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(308.000000,2),math.log(251.000000,2),math.log(274.500000,2),math.log(282.250000,2),math.log(253.125000,2),math.log(277.750000,2),math.log(291.718750,2),math.log(341.500000,2),math.log(503.164062,2),math.log(752.351562,2),math.log(1110.500000,2),math.log(1860.324219,2),math.log(3427.333008,2),math.log(6839.319336,2),math.log(13567.014038,2),math.log(26561.484070,2),math.log(53238.286316,2)]
t_184 = [math.log(240.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(243.000000,2),math.log(258.250000,2),math.log(237.125000,2),math.log(247.437500,2),math.log(275.843750,2),math.log(324.703125,2),math.log(406.343750,2),math.log(501.960938,2),math.log(776.125000,2),math.log(1353.083008,2),math.log(2448.311035,2),math.log(4262.567383,2),math.log(8380.961182,2),math.log(16136.341248,2),math.log(32462.000183,2)]
t_185 = [math.log(288.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(238.000000,2),math.log(236.000000,2),math.log(251.000000,2),math.log(284.000000,2),math.log(261.250000,2),math.log(267.250000,2),math.log(284.437500,2),math.log(327.343750,2),math.log(349.257812,2),math.log(431.597656,2),math.log(685.585938,2),math.log(1128.810547,2),math.log(1918.288574,2),math.log(3568.848389,2),math.log(7080.339844,2),math.log(13350.057556,2),math.log(26484.613007,2)]
t_186 = [math.log(272.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(277.000000,2),math.log(258.750000,2),math.log(283.375000,2),math.log(320.750000,2),math.log(393.843750,2),math.log(421.000000,2),math.log(560.156250,2),math.log(864.476562,2),math.log(1456.292969,2),math.log(2491.764648,2),math.log(4941.965332,2),math.log(9541.454102,2),math.log(19243.676514,2),math.log(37933.666199,2),math.log(76169.394287,2)]
t_187 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(260.000000,2),math.log(248.500000,2),math.log(247.750000,2),math.log(272.500000,2),math.log(328.500000,2),math.log(367.687500,2),math.log(455.328125,2),math.log(703.273438,2),math.log(1098.707031,2),math.log(1888.699219,2),math.log(3340.000977,2),math.log(6138.909180,2),math.log(11883.854248,2),math.log(23397.886230,2),math.log(46285.435181,2),math.log(92015.591583,2)]
t_188 = [math.log(240.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(280.000000,2),math.log(300.000000,2),math.log(272.000000,2),math.log(240.500000,2),math.log(262.250000,2),math.log(246.406250,2),math.log(287.968750,2),math.log(358.750000,2),math.log(479.984375,2),math.log(750.978516,2),math.log(1283.690430,2),math.log(2597.977051,2),math.log(5046.200195,2),math.log(9927.726929,2),math.log(19045.854004,2),math.log(37678.779938,2)]
t_189 = [math.log(272.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(268.000000,2),math.log(265.000000,2),math.log(254.500000,2),math.log(269.500000,2),math.log(288.500000,2),math.log(301.062500,2),math.log(301.781250,2),math.log(363.171875,2),math.log(467.273438,2),math.log(659.011719,2),math.log(966.574219,2),math.log(1640.192383,2),math.log(2987.008789,2),math.log(5666.451904,2),math.log(11106.080566,2),math.log(21620.627747,2),math.log(43083.691101,2)]
t_190 = [math.log(240.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(206.000000,2),math.log(274.000000,2),math.log(275.500000,2),math.log(274.500000,2),math.log(300.875000,2),math.log(308.875000,2),math.log(295.937500,2),math.log(318.875000,2),math.log(386.750000,2),math.log(603.781250,2),math.log(1013.496094,2),math.log(1840.753906,2),math.log(3264.514160,2),math.log(6508.065430,2),math.log(12936.382080,2),math.log(25299.447449,2),math.log(50121.640472,2)]
t_191 = [math.log(272.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(214.000000,2),math.log(267.000000,2),math.log(235.500000,2),math.log(252.250000,2),math.log(276.000000,2),math.log(285.875000,2),math.log(330.843750,2),math.log(384.687500,2),math.log(561.218750,2),math.log(767.441406,2),math.log(1177.615234,2),math.log(2138.287109,2),math.log(3983.349121,2),math.log(7568.559814,2),math.log(14591.165283,2),math.log(29153.867920,2),math.log(58380.314911,2)]
t_192 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(246.000000,2),math.log(259.000000,2),math.log(273.250000,2),math.log(242.750000,2),math.log(240.062500,2),math.log(207.093750,2),math.log(255.625000,2),math.log(256.835938,2),math.log(275.441406,2),math.log(318.775391,2),math.log(408.934570,2),math.log(572.494141,2),math.log(972.994141,2),math.log(1692.531006,2),math.log(3128.751282,2),math.log(6302.049286,2)]
t_193 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(267.000000,2),math.log(242.500000,2),math.log(287.000000,2),math.log(284.500000,2),math.log(307.062500,2),math.log(307.375000,2),math.log(272.734375,2),math.log(296.656250,2),math.log(312.246094,2),math.log(438.271484,2),math.log(633.940430,2),math.log(1074.186523,2),math.log(1841.505615,2),math.log(3366.407593,2),math.log(6385.874146,2),math.log(11975.242218,2)]
t_194 = [math.log(304.000000,2),math.log(248.000000,2),math.log(300.000000,2),math.log(302.000000,2),math.log(287.000000,2),math.log(276.500000,2),math.log(253.500000,2),math.log(234.500000,2),math.log(235.250000,2),math.log(275.562500,2),math.log(265.640625,2),math.log(274.945312,2),math.log(283.925781,2),math.log(375.904297,2),math.log(544.024414,2),math.log(869.918945,2),math.log(1511.372070,2),math.log(2619.275635,2),math.log(4877.987122,2),math.log(9332.310181,2)]
t_195 = [math.log(272.000000,2),math.log(280.000000,2),math.log(232.000000,2),math.log(278.000000,2),math.log(285.000000,2),math.log(296.500000,2),math.log(281.500000,2),math.log(276.375000,2),math.log(257.250000,2),math.log(301.625000,2),math.log(313.359375,2),math.log(327.054688,2),math.log(389.226562,2),math.log(564.888672,2),math.log(855.420898,2),math.log(1449.286621,2),math.log(2631.270752,2),math.log(4956.643677,2),math.log(9683.239197,2),math.log(18755.862946,2)]
t_196 = [math.log(288.000000,2),math.log(272.000000,2),math.log(228.000000,2),math.log(258.000000,2),math.log(211.000000,2),math.log(238.000000,2),math.log(288.750000,2),math.log(276.000000,2),math.log(255.125000,2),math.log(278.062500,2),math.log(245.406250,2),math.log(295.875000,2),math.log(352.332031,2),math.log(499.662109,2),math.log(741.826172,2),math.log(1261.663574,2),math.log(2353.565430,2),math.log(4624.347290,2),math.log(8978.637573,2),math.log(17522.508728,2)]
t_197 = [math.log(256.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(257.000000,2),math.log(262.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(279.000000,2),math.log(270.156250,2),math.log(233.562500,2),math.log(277.562500,2),math.log(347.074219,2),math.log(435.253906,2),math.log(623.898438,2),math.log(984.604492,2),math.log(1592.798584,2),math.log(2953.760864,2),math.log(5664.268494,2),math.log(11321.358307,2)]
t_198 = [math.log(272.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(249.500000,2),math.log(241.250000,2),math.log(229.312500,2),math.log(311.125000,2),math.log(301.625000,2),math.log(354.421875,2),math.log(454.941406,2),math.log(563.423828,2),math.log(970.271484,2),math.log(1541.897949,2),math.log(2902.177490,2),math.log(5570.475464,2),math.log(10618.733948,2),math.log(20908.288635,2)]
t_199 = [math.log(256.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(234.000000,2),math.log(249.000000,2),math.log(273.000000,2),math.log(300.250000,2),math.log(295.375000,2),math.log(298.375000,2),math.log(309.875000,2),math.log(346.156250,2),math.log(438.445312,2),math.log(595.371094,2),math.log(924.451172,2),math.log(1611.127930,2),math.log(2788.924316,2),math.log(5504.677002,2),math.log(10379.589844,2),math.log(20242.346741,2),math.log(40506.592865,2)]
t_200 = [math.log(224.000000,2),math.log(240.000000,2),math.log(212.000000,2),math.log(228.000000,2),math.log(234.000000,2),math.log(211.500000,2),math.log(225.750000,2),math.log(241.750000,2),math.log(247.562500,2),math.log(246.718750,2),math.log(260.218750,2),math.log(277.125000,2),math.log(339.929688,2),math.log(404.482422,2),math.log(539.554688,2),math.log(729.685059,2),math.log(1191.458984,2),math.log(2153.007202,2),math.log(4081.177429,2),math.log(8040.805145,2)]
t_201 = [math.log(304.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(281.000000,2),math.log(288.500000,2),math.log(283.500000,2),math.log(272.375000,2),math.log(265.312500,2),math.log(270.437500,2),math.log(290.890625,2),math.log(348.937500,2),math.log(414.398438,2),math.log(538.699219,2),math.log(822.820312,2),math.log(1216.245605,2),math.log(2083.652588,2),math.log(4021.197998,2),math.log(7965.013489,2),math.log(15569.606873,2)]
t_202 = [math.log(256.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(262.000000,2),math.log(254.000000,2),math.log(262.500000,2),math.log(266.750000,2),math.log(278.000000,2),math.log(252.750000,2),math.log(291.437500,2),math.log(341.546875,2),math.log(406.539062,2),math.log(529.343750,2),math.log(833.609375,2),math.log(1552.341797,2),math.log(2894.531250,2),math.log(5413.929443,2),math.log(10586.107178,2),math.log(21030.816589,2),math.log(41844.393097,2)]
t_203 = [math.log(272.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(253.000000,2),math.log(257.500000,2),math.log(253.500000,2),math.log(251.250000,2),math.log(250.562500,2),math.log(294.906250,2),math.log(340.546875,2),math.log(394.546875,2),math.log(471.312500,2),math.log(677.423828,2),math.log(1088.875977,2),math.log(2022.133789,2),math.log(3740.999023,2),math.log(7518.839966,2),math.log(14710.104614,2),math.log(28726.373322,2)]
t_204 = [math.log(240.000000,2),math.log(240.000000,2),math.log(204.000000,2),math.log(236.000000,2),math.log(220.000000,2),math.log(215.000000,2),math.log(223.000000,2),math.log(263.125000,2),math.log(264.500000,2),math.log(280.468750,2),math.log(266.421875,2),math.log(280.781250,2),math.log(394.703125,2),math.log(538.599609,2),math.log(811.731445,2),math.log(1344.231445,2),math.log(2391.454102,2),math.log(4413.021729,2),math.log(8286.779907,2),math.log(16308.363159,2)]
t_205 = [math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(226.000000,2),math.log(223.000000,2),math.log(267.500000,2),math.log(253.500000,2),math.log(254.750000,2),math.log(246.937500,2),math.log(310.843750,2),math.log(316.640625,2),math.log(412.554688,2),math.log(558.457031,2),math.log(663.539062,2),math.log(1139.613281,2),math.log(1852.616211,2),math.log(3501.571533,2),math.log(6581.424927,2),math.log(13548.271362,2),math.log(27009.566406,2)]
t_206 = [math.log(240.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(242.000000,2),math.log(266.000000,2),math.log(243.500000,2),math.log(265.500000,2),math.log(239.375000,2),math.log(271.250000,2),math.log(261.562500,2),math.log(320.343750,2),math.log(387.109375,2),math.log(493.937500,2),math.log(810.466797,2),math.log(1146.445312,2),math.log(2006.354980,2),math.log(3818.993652,2),math.log(7544.210205,2),math.log(15009.123657,2),math.log(30042.753632,2)]
t_207 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(243.000000,2),math.log(258.000000,2),math.log(272.000000,2),math.log(229.000000,2),math.log(281.312500,2),math.log(280.000000,2),math.log(306.453125,2),math.log(366.078125,2),math.log(437.121094,2),math.log(576.580078,2),math.log(797.131836,2),math.log(1320.785645,2),math.log(2361.873047,2),math.log(4513.368164,2),math.log(8778.075745,2),math.log(17434.989563,2)]
t_208 = [math.log(240.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(268.000000,2),math.log(247.000000,2),math.log(254.500000,2),math.log(260.000000,2),math.log(276.625000,2),math.log(244.312500,2),math.log(320.062500,2),math.log(328.562500,2),math.log(375.625000,2),math.log(415.597656,2),math.log(568.949219,2),math.log(864.222656,2),math.log(1515.351074,2),math.log(2708.231689,2),math.log(5139.138306,2),math.log(10102.752319,2),math.log(19842.103149,2)]
t_209 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(249.000000,2),math.log(264.500000,2),math.log(264.000000,2),math.log(271.375000,2),math.log(270.437500,2),math.log(244.312500,2),math.log(272.609375,2),math.log(319.625000,2),math.log(405.125000,2),math.log(638.501953,2),math.log(925.981445,2),math.log(1678.346191,2),math.log(3319.600830,2),math.log(6286.487915,2),math.log(12357.336731,2),math.log(24328.382202,2)]
t_210 = [math.log(256.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(292.000000,2),math.log(274.000000,2),math.log(299.250000,2),math.log(261.375000,2),math.log(269.875000,2),math.log(271.156250,2),math.log(291.953125,2),math.log(334.414062,2),math.log(395.273438,2),math.log(526.796875,2),math.log(759.398438,2),math.log(1258.547852,2),math.log(2401.429443,2),math.log(4508.953979,2),math.log(9197.986206,2),math.log(18628.180908,2)]
t_211 = [math.log(224.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(274.000000,2),math.log(266.000000,2),math.log(267.500000,2),math.log(246.500000,2),math.log(277.375000,2),math.log(250.625000,2),math.log(228.656250,2),math.log(291.562500,2),math.log(373.304688,2),math.log(439.781250,2),math.log(650.978516,2),math.log(1081.171875,2),math.log(1895.452148,2),math.log(3563.037354,2),math.log(6606.743286,2),math.log(13095.808716,2),math.log(25925.505005,2)]
t_212 = [math.log(240.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(214.000000,2),math.log(231.000000,2),math.log(222.000000,2),math.log(224.250000,2),math.log(234.000000,2),math.log(262.062500,2),math.log(272.281250,2),math.log(320.687500,2),math.log(369.882812,2),math.log(458.203125,2),math.log(636.175781,2),math.log(997.903320,2),math.log(1820.174316,2),math.log(3372.601074,2),math.log(6388.185791,2),math.log(12589.267273,2),math.log(24683.753082,2)]
t_213 = [math.log(224.000000,2),math.log(216.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(246.000000,2),math.log(239.500000,2),math.log(270.750000,2),math.log(261.875000,2),math.log(256.562500,2),math.log(297.093750,2),math.log(284.625000,2),math.log(327.296875,2),math.log(399.269531,2),math.log(536.316406,2),math.log(857.157227,2),math.log(1412.100098,2),math.log(2717.832520,2),math.log(5211.035522,2),math.log(10537.621338,2),math.log(21055.571655,2)]
t_214 = [math.log(224.000000,2),math.log(232.000000,2),math.log(284.000000,2),math.log(236.000000,2),math.log(260.000000,2),math.log(238.000000,2),math.log(237.750000,2),math.log(242.250000,2),math.log(260.437500,2),math.log(235.812500,2),math.log(251.921875,2),math.log(294.234375,2),math.log(400.750000,2),math.log(518.492188,2),math.log(855.061523,2),math.log(1539.069824,2),math.log(2984.615479,2),math.log(5764.371216,2),math.log(11168.035767,2),math.log(21996.493225,2)]
t_215 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(242.000000,2),math.log(269.000000,2),math.log(266.000000,2),math.log(282.500000,2),math.log(263.000000,2),math.log(252.687500,2),math.log(274.437500,2),math.log(287.031250,2),math.log(347.210938,2),math.log(469.628906,2),math.log(792.039062,2),math.log(1416.587891,2),math.log(2517.895508,2),math.log(4653.491943,2),math.log(8975.975464,2),math.log(17818.242126,2),math.log(35678.800781,2)]
t_216 = [math.log(240.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(240.000000,2),math.log(261.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(278.875000,2),math.log(292.125000,2),math.log(272.718750,2),math.log(275.031250,2),math.log(289.140625,2),math.log(362.882812,2),math.log(475.875000,2),math.log(711.801758,2),math.log(1248.338867,2),math.log(2135.447021,2),math.log(4265.794678,2),math.log(8618.772217,2),math.log(17108.381714,2)]
t_217 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(246.000000,2),math.log(227.000000,2),math.log(224.500000,2),math.log(216.250000,2),math.log(237.000000,2),math.log(221.812500,2),math.log(237.375000,2),math.log(264.625000,2),math.log(350.054688,2),math.log(465.417969,2),math.log(632.404297,2),math.log(957.882812,2),math.log(1676.476562,2),math.log(3137.456055,2),math.log(5969.430176,2),math.log(11982.407471,2),math.log(24061.177765,2)]
t_218 = [math.log(240.000000,2),math.log(312.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(279.000000,2),math.log(250.000000,2),math.log(261.500000,2),math.log(255.375000,2),math.log(283.250000,2),math.log(328.875000,2),math.log(403.515625,2),math.log(489.476562,2),math.log(684.167969,2),math.log(1013.177734,2),math.log(1615.686523,2),math.log(3029.546387,2),math.log(5932.224121,2),math.log(11197.732544,2),math.log(21858.652710,2),math.log(43596.187866,2)]
t_219 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(247.000000,2),math.log(267.000000,2),math.log(283.750000,2),math.log(275.125000,2),math.log(274.937500,2),math.log(279.281250,2),math.log(299.906250,2),math.log(362.460938,2),math.log(512.570312,2),math.log(777.531250,2),math.log(1228.394531,2),math.log(2256.786133,2),math.log(4334.933838,2),math.log(8573.403076,2),math.log(16902.324036,2),math.log(33602.610657,2)]
t_220 = [math.log(224.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(248.000000,2),math.log(276.750000,2),math.log(283.375000,2),math.log(320.812500,2),math.log(319.562500,2),math.log(384.328125,2),math.log(433.421875,2),math.log(575.382812,2),math.log(925.859375,2),math.log(1565.387695,2),math.log(2965.101074,2),math.log(5691.388428,2),math.log(11002.567505,2),math.log(21471.265930,2),math.log(43222.665710,2)]
t_221 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(243.000000,2),math.log(238.000000,2),math.log(231.000000,2),math.log(272.250000,2),math.log(293.000000,2),math.log(327.812500,2),math.log(352.718750,2),math.log(467.757812,2),math.log(598.281250,2),math.log(954.666016,2),math.log(1736.401367,2),math.log(3175.304199,2),math.log(6129.725830,2),math.log(12099.409424,2),math.log(23840.282471,2),math.log(47345.907745,2)]
t_222 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(244.000000,2),math.log(237.000000,2),math.log(214.000000,2),math.log(254.250000,2),math.log(264.125000,2),math.log(270.375000,2),math.log(277.000000,2),math.log(331.187500,2),math.log(401.515625,2),math.log(667.050781,2),math.log(1031.412109,2),math.log(1861.021484,2),math.log(3585.910645,2),math.log(7022.588867,2),math.log(13830.152588,2),math.log(26539.782166,2),math.log(52657.585175,2)]
t_223 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(236.000000,2),math.log(235.000000,2),math.log(231.000000,2),math.log(245.125000,2),math.log(292.187500,2),math.log(267.531250,2),math.log(335.484375,2),math.log(484.968750,2),math.log(619.500000,2),math.log(966.888672,2),math.log(1656.546875,2),math.log(2947.247070,2),math.log(5758.857910,2),math.log(11456.567017,2),math.log(22784.168396,2),math.log(45415.055695,2)]
t_224 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(289.000000,2),math.log(255.500000,2),math.log(264.750000,2),math.log(250.875000,2),math.log(273.625000,2),math.log(262.312500,2),math.log(288.968750,2),math.log(294.304688,2),math.log(391.390625,2),math.log(517.603516,2),math.log(738.201172,2),math.log(1134.537109,2),math.log(2295.265625,2),math.log(4323.219727,2),math.log(8150.567139,2),math.log(15850.947815,2)]
t_225 = [math.log(288.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(258.000000,2),math.log(263.000000,2),math.log(260.000000,2),math.log(273.500000,2),math.log(256.125000,2),math.log(260.062500,2),math.log(274.625000,2),math.log(299.437500,2),math.log(356.476562,2),math.log(466.707031,2),math.log(571.960938,2),math.log(877.749023,2),math.log(1496.631348,2),math.log(2673.237061,2),math.log(4916.019653,2),math.log(9708.438660,2),math.log(19737.928650,2)]
t_226 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(269.000000,2),math.log(251.500000,2),math.log(254.750000,2),math.log(233.375000,2),math.log(247.375000,2),math.log(270.125000,2),math.log(277.265625,2),math.log(286.093750,2),math.log(361.480469,2),math.log(485.880859,2),math.log(718.661133,2),math.log(1133.428711,2),math.log(2091.400635,2),math.log(3670.537109,2),math.log(6711.957886,2),math.log(12672.175385,2)]
t_227 = [math.log(240.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(218.500000,2),math.log(214.250000,2),math.log(210.750000,2),math.log(258.250000,2),math.log(270.843750,2),math.log(271.484375,2),math.log(320.843750,2),math.log(489.308594,2),math.log(663.539062,2),math.log(1084.010742,2),math.log(2012.299316,2),math.log(3704.110352,2),math.log(7201.449829,2),math.log(13654.834778,2),math.log(26991.912506,2)]
t_228 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(276.000000,2),math.log(263.000000,2),math.log(252.500000,2),math.log(206.750000,2),math.log(227.875000,2),math.log(245.062500,2),math.log(270.125000,2),math.log(291.609375,2),math.log(337.617188,2),math.log(440.515625,2),math.log(648.433594,2),math.log(1111.314453,2),math.log(2001.157715,2),math.log(3565.232910,2),math.log(6825.522339,2),math.log(13452.955750,2),math.log(26509.751709,2)]
t_229 = [math.log(240.000000,2),math.log(240.000000,2),math.log(204.000000,2),math.log(210.000000,2),math.log(225.000000,2),math.log(241.000000,2),math.log(248.750000,2),math.log(271.250000,2),math.log(210.562500,2),math.log(219.031250,2),math.log(260.156250,2),math.log(300.414062,2),math.log(387.742188,2),math.log(440.443359,2),math.log(695.540039,2),math.log(1115.981445,2),math.log(1997.053711,2),math.log(3732.418457,2),math.log(7181.561462,2),math.log(14327.248169,2)]
t_230 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(248.000000,2),math.log(250.500000,2),math.log(259.250000,2),math.log(284.375000,2),math.log(267.187500,2),math.log(300.687500,2),math.log(368.796875,2),math.log(417.460938,2),math.log(514.148438,2),math.log(728.193359,2),math.log(1156.505859,2),math.log(2043.235352,2),math.log(3814.027832,2),math.log(7269.838257,2),math.log(14047.564758,2),math.log(27735.878998,2)]
t_231 = [math.log(256.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(262.000000,2),math.log(243.000000,2),math.log(237.000000,2),math.log(251.000000,2),math.log(260.500000,2),math.log(258.125000,2),math.log(286.281250,2),math.log(284.984375,2),math.log(395.687500,2),math.log(637.812500,2),math.log(970.773438,2),math.log(1771.798828,2),math.log(3142.145508,2),math.log(6363.307617,2),math.log(12215.323975,2),math.log(24679.492432,2),math.log(48204.291168,2)]
t_232 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(288.000000,2),math.log(274.000000,2),math.log(274.000000,2),math.log(261.750000,2),math.log(243.375000,2),math.log(248.375000,2),math.log(214.937500,2),math.log(234.031250,2),math.log(289.453125,2),math.log(369.750000,2),math.log(401.470703,2),math.log(523.335938,2),math.log(856.556152,2),math.log(1391.093994,2),math.log(2507.172974,2),math.log(4808.882751,2),math.log(9460.669312,2)]
t_233 = [math.log(240.000000,2),math.log(216.000000,2),math.log(216.000000,2),math.log(242.000000,2),math.log(247.000000,2),math.log(215.500000,2),math.log(229.250000,2),math.log(253.375000,2),math.log(259.000000,2),math.log(251.312500,2),math.log(265.531250,2),math.log(290.976562,2),math.log(355.062500,2),math.log(459.988281,2),math.log(811.750977,2),math.log(1446.647949,2),math.log(2540.370850,2),math.log(4655.591675,2),math.log(9223.645569,2),math.log(17980.082703,2)]
t_234 = [math.log(304.000000,2),math.log(280.000000,2),math.log(304.000000,2),math.log(282.000000,2),math.log(268.000000,2),math.log(303.000000,2),math.log(253.750000,2),math.log(279.000000,2),math.log(316.562500,2),math.log(307.625000,2),math.log(315.093750,2),math.log(350.078125,2),math.log(438.890625,2),math.log(680.160156,2),math.log(1138.727539,2),math.log(2046.724609,2),math.log(3852.326660,2),math.log(7571.403076,2),math.log(15010.789307,2),math.log(30177.819397,2)]
t_235 = [math.log(336.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(270.000000,2),math.log(281.000000,2),math.log(303.000000,2),math.log(267.750000,2),math.log(267.000000,2),math.log(270.500000,2),math.log(332.968750,2),math.log(348.500000,2),math.log(442.164062,2),math.log(595.542969,2),math.log(808.796875,2),math.log(1410.396484,2),math.log(2605.900879,2),math.log(5050.532227,2),math.log(9637.920166,2),math.log(18725.721558,2),math.log(36952.244415,2)]
t_236 = [math.log(224.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(222.500000,2),math.log(232.750000,2),math.log(281.500000,2),math.log(300.625000,2),math.log(289.000000,2),math.log(299.015625,2),math.log(376.296875,2),math.log(520.781250,2),math.log(778.119141,2),math.log(1281.391602,2),math.log(2360.856934,2),math.log(4448.492432,2),math.log(8683.728882,2),math.log(16902.845825,2),math.log(33657.088776,2)]
t_237 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(222.000000,2),math.log(244.000000,2),math.log(276.000000,2),math.log(249.500000,2),math.log(233.000000,2),math.log(295.875000,2),math.log(296.843750,2),math.log(367.578125,2),math.log(410.281250,2),math.log(601.375000,2),math.log(876.943359,2),math.log(1618.330078,2),math.log(2875.461426,2),math.log(5606.714111,2),math.log(11021.168579,2),math.log(21998.590088,2),math.log(44027.139069,2)]
t_238 = [math.log(256.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(258.000000,2),math.log(296.000000,2),math.log(282.500000,2),math.log(261.250000,2),math.log(265.500000,2),math.log(255.125000,2),math.log(262.531250,2),math.log(287.625000,2),math.log(402.140625,2),math.log(554.363281,2),math.log(917.000000,2),math.log(1586.561523,2),math.log(2809.238770,2),math.log(5378.218750,2),math.log(10790.975830,2),math.log(21763.391785,2),math.log(43729.924103,2)]
t_239 = [math.log(256.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(262.000000,2),math.log(254.000000,2),math.log(265.250000,2),math.log(247.375000,2),math.log(266.500000,2),math.log(252.562500,2),math.log(332.156250,2),math.log(369.148438,2),math.log(500.292969,2),math.log(691.402344,2),math.log(1067.872070,2),math.log(1774.733887,2),math.log(3415.139893,2),math.log(6604.287476,2),math.log(12851.099243,2),math.log(25457.665680,2)]
t_240 = [math.log(272.000000,2),math.log(304.000000,2),math.log(272.000000,2),math.log(286.000000,2),math.log(281.000000,2),math.log(264.000000,2),math.log(279.250000,2),math.log(261.250000,2),math.log(234.625000,2),math.log(231.468750,2),math.log(300.750000,2),math.log(314.906250,2),math.log(356.203125,2),math.log(468.115234,2),math.log(641.849609,2),math.log(1075.684570,2),math.log(1987.524414,2),math.log(3745.002319,2),math.log(7152.509033,2),math.log(14290.193695,2)]
t_241 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(274.000000,2),math.log(272.500000,2),math.log(246.250000,2),math.log(274.500000,2),math.log(287.000000,2),math.log(299.812500,2),math.log(279.531250,2),math.log(305.437500,2),math.log(371.617188,2),math.log(466.957031,2),math.log(672.810547,2),math.log(1074.035645,2),math.log(1985.296631,2),math.log(3758.715698,2),math.log(7243.778687,2),math.log(14165.155151,2)]
t_242 = [math.log(256.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(264.000000,2),math.log(249.000000,2),math.log(258.000000,2),math.log(261.750000,2),math.log(244.250000,2),math.log(231.875000,2),math.log(219.593750,2),math.log(251.750000,2),math.log(295.757812,2),math.log(357.996094,2),math.log(518.726562,2),math.log(713.381836,2),math.log(1223.008301,2),math.log(2192.066650,2),math.log(3966.330566,2),math.log(7311.523071,2),math.log(14077.712219,2)]
t_243 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(216.000000,2),math.log(208.000000,2),math.log(231.000000,2),math.log(221.250000,2),math.log(217.125000,2),math.log(268.312500,2),math.log(298.625000,2),math.log(334.921875,2),math.log(426.484375,2),math.log(567.542969,2),math.log(908.404297,2),math.log(1526.676758,2),math.log(2740.348145,2),math.log(5255.061523,2),math.log(10018.928467,2),math.log(19742.826538,2),math.log(38737.911377,2)]
t_244 = [math.log(272.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(230.000000,2),math.log(231.000000,2),math.log(204.500000,2),math.log(203.500000,2),math.log(203.375000,2),math.log(243.000000,2),math.log(252.312500,2),math.log(289.312500,2),math.log(343.132812,2),math.log(425.218750,2),math.log(619.570312,2),math.log(968.240234,2),math.log(1736.966797,2),math.log(3299.508057,2),math.log(6341.777954,2),math.log(12258.975586,2),math.log(23975.791809,2)]
t_245 = [math.log(272.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(253.000000,2),math.log(240.500000,2),math.log(241.250000,2),math.log(263.375000,2),math.log(257.937500,2),math.log(250.687500,2),math.log(253.750000,2),math.log(321.414062,2),math.log(349.164062,2),math.log(463.802734,2),math.log(680.911133,2),math.log(1180.206543,2),math.log(2080.460205,2),math.log(3922.930176,2),math.log(7457.933472,2),math.log(14665.284088,2)]
t_246 = [math.log(240.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(229.000000,2),math.log(227.500000,2),math.log(267.000000,2),math.log(250.250000,2),math.log(229.000000,2),math.log(247.562500,2),math.log(306.515625,2),math.log(306.437500,2),math.log(401.113281,2),math.log(611.892578,2),math.log(1087.980469,2),math.log(1843.877930,2),math.log(3529.619873,2),math.log(6859.925049,2),math.log(13619.132812,2),math.log(26765.816010,2)]
t_247 = [math.log(240.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(238.000000,2),math.log(266.000000,2),math.log(302.500000,2),math.log(326.750000,2),math.log(295.250000,2),math.log(223.062500,2),math.log(244.968750,2),math.log(278.687500,2),math.log(388.601562,2),math.log(571.402344,2),math.log(809.451172,2),math.log(1347.196289,2),math.log(2374.364258,2),math.log(4542.187256,2),math.log(8716.071655,2),math.log(17350.363831,2),math.log(34817.793915,2)]
t_248 = [math.log(256.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(198.000000,2),math.log(209.000000,2),math.log(213.000000,2),math.log(215.250000,2),math.log(212.125000,2),math.log(227.125000,2),math.log(251.562500,2),math.log(314.984375,2),math.log(359.609375,2),math.log(508.054688,2),math.log(663.726562,2),math.log(996.347656,2),math.log(1601.106445,2),math.log(2920.181641,2),math.log(5666.899902,2),math.log(10993.285400,2),math.log(21962.764832,2)]
t_249 = [math.log(256.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(226.000000,2),math.log(240.000000,2),math.log(250.500000,2),math.log(282.000000,2),math.log(286.875000,2),math.log(275.750000,2),math.log(263.437500,2),math.log(307.531250,2),math.log(395.695312,2),math.log(493.574219,2),math.log(613.191406,2),math.log(870.895508,2),math.log(1472.533203,2),math.log(2740.571777,2),math.log(5426.554565,2),math.log(10576.072449,2),math.log(20744.712616,2)]
t_250 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(224.000000,2),math.log(210.000000,2),math.log(218.500000,2),math.log(251.750000,2),math.log(276.750000,2),math.log(288.562500,2),math.log(327.250000,2),math.log(397.656250,2),math.log(488.937500,2),math.log(764.359375,2),math.log(1274.287109,2),math.log(2298.635742,2),math.log(4445.463379,2),math.log(8435.913818,2),math.log(16460.903809,2),math.log(32279.675964,2),math.log(64898.536346,2)]
t_251 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(286.000000,2),math.log(277.000000,2),math.log(259.500000,2),math.log(264.750000,2),math.log(263.375000,2),math.log(292.875000,2),math.log(322.937500,2),math.log(330.953125,2),math.log(391.437500,2),math.log(508.621094,2),math.log(814.876953,2),math.log(1361.300781,2),math.log(2536.599121,2),math.log(4588.623779,2),math.log(8717.245728,2),math.log(17583.980103,2),math.log(35202.753082,2)]
t_252 = [math.log(224.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(246.000000,2),math.log(251.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(250.750000,2),math.log(246.437500,2),math.log(260.656250,2),math.log(285.703125,2),math.log(317.390625,2),math.log(404.296875,2),math.log(495.609375,2),math.log(723.634766,2),math.log(1209.408203,2),math.log(2067.810059,2),math.log(3883.448364,2),math.log(7792.127563,2),math.log(15028.691498,2)]
t_253 = [math.log(272.000000,2),math.log(264.000000,2),math.log(224.000000,2),math.log(242.000000,2),math.log(305.000000,2),math.log(304.500000,2),math.log(295.500000,2),math.log(257.500000,2),math.log(283.312500,2),math.log(270.187500,2),math.log(287.984375,2),math.log(315.539062,2),math.log(377.226562,2),math.log(501.343750,2),math.log(822.851562,2),math.log(1355.000977,2),math.log(2373.140381,2),math.log(4813.702759,2),math.log(9388.235474,2),math.log(18124.190979,2)]
t_254 = [math.log(272.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(277.000000,2),math.log(255.500000,2),math.log(258.000000,2),math.log(256.375000,2),math.log(275.250000,2),math.log(306.125000,2),math.log(358.421875,2),math.log(360.062500,2),math.log(459.871094,2),math.log(684.542969,2),math.log(1058.487305,2),math.log(1908.517090,2),math.log(3432.773193,2),math.log(6457.605957,2),math.log(12773.157471,2),math.log(25196.307434,2)]
t_255 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(250.000000,2),math.log(243.500000,2),math.log(248.750000,2),math.log(282.500000,2),math.log(304.250000,2),math.log(307.062500,2),math.log(346.796875,2),math.log(521.867188,2),math.log(880.761719,2),math.log(1518.562500,2),math.log(2759.405273,2),math.log(5388.258301,2),math.log(10679.653320,2),math.log(20852.594604,2),math.log(41044.150146,2),math.log(81474.317322,2)]


#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00155004
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00155004)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00155004
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00155004)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00155004
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00155004)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00155004
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00155004)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00155004
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00155004)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00155004
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00155004)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00155004
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00155004)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00155004
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00155004)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00155004
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00155004)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00155004
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00155004)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00155004
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00155004)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00155004
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00155004)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00155004
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00155004)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00155004
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00155004)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00155004
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00155004)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00155004
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00155004)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00155004
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00155004)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00155004
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00155004)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00155004
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00155004)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00155004
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00155004)**2)


#Plotting 5 different lines to present the theoretical distirbution of T

expected_T_a_0 = []
expected_T_a_0.append(math.log(mu_32,2))
expected_T_a_0.append(math.log(mu_64,2))
expected_T_a_0.append(math.log(mu_128,2))
expected_T_a_0.append(math.log(mu_256,2))
expected_T_a_0.append(math.log(mu_512,2))
expected_T_a_0.append(math.log(mu_1024,2))
expected_T_a_0.append(math.log(mu_2048,2))
expected_T_a_0.append(math.log(mu_4096,2))
expected_T_a_0.append(math.log(mu_8192,2))
expected_T_a_0.append(math.log(mu_16384,2))
expected_T_a_0.append(math.log(mu_32768,2))
expected_T_a_0.append(math.log(mu_65536,2))
expected_T_a_0.append(math.log(mu_131072,2))
expected_T_a_0.append(math.log(mu_262144,2))
expected_T_a_0.append(math.log(mu_524288,2))
expected_T_a_0.append(math.log(mu_1048576,2))
expected_T_a_0.append(math.log(mu_2097152,2))
expected_T_a_0.append(math.log(mu_4194304,2))
expected_T_a_0.append(math.log(mu_8388608,2))
expected_T_a_0.append(math.log(mu_16777216,2))
plt.plot(t,expected_T_a_0,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_1 = []
expected_T_a_1.append(math.log(mu_32+sigma_32,2))
expected_T_a_1.append(math.log(mu_64+sigma_64,2))
expected_T_a_1.append(math.log(mu_128+sigma_128,2))
expected_T_a_1.append(math.log(mu_256+sigma_256,2))
expected_T_a_1.append(math.log(mu_512+sigma_512,2))
expected_T_a_1.append(math.log(mu_1024+sigma_1024,2))
expected_T_a_1.append(math.log(mu_2048+sigma_2048,2))
expected_T_a_1.append(math.log(mu_4096+sigma_4096,2))
expected_T_a_1.append(math.log(mu_8192+sigma_8192,2))
expected_T_a_1.append(math.log(mu_16384+sigma_16384,2))
expected_T_a_1.append(math.log(mu_32768+sigma_32768,2))
expected_T_a_1.append(math.log(mu_65536+sigma_65536,2))
expected_T_a_1.append(math.log(mu_131072+sigma_131072,2))
expected_T_a_1.append(math.log(mu_262144+sigma_262144,2))
expected_T_a_1.append(math.log(mu_524288+sigma_524288,2))
expected_T_a_1.append(math.log(mu_1048576+sigma_1048576,2))
expected_T_a_1.append(math.log(mu_2097152+sigma_2097152,2))
expected_T_a_1.append(math.log(mu_4194304+sigma_4194304,2))
expected_T_a_1.append(math.log(mu_8388608+sigma_8388608,2))
expected_T_a_1.append(math.log(mu_16777216+sigma_16777216,2))
plt.plot(t,expected_T_a_1,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_2 = []
expected_T_a_2.append(math.log(mu_32-sigma_32,2))
expected_T_a_2.append(math.log(mu_64-sigma_64,2))
expected_T_a_2.append(math.log(mu_128-sigma_128,2))
expected_T_a_2.append(math.log(mu_256-sigma_256,2))
expected_T_a_2.append(math.log(mu_512-sigma_512,2))
expected_T_a_2.append(math.log(mu_1024-sigma_1024,2))
expected_T_a_2.append(math.log(mu_2048-sigma_2048,2))
expected_T_a_2.append(math.log(mu_4096-sigma_4096,2))
expected_T_a_2.append(math.log(mu_8192-sigma_8192,2))
expected_T_a_2.append(math.log(mu_16384-sigma_16384,2))
expected_T_a_2.append(math.log(mu_32768-sigma_32768,2))
expected_T_a_2.append(math.log(mu_65536-sigma_65536,2))
expected_T_a_2.append(math.log(mu_131072-sigma_131072,2))
expected_T_a_2.append(math.log(mu_262144-sigma_262144,2))
expected_T_a_2.append(math.log(mu_524288-sigma_524288,2))
expected_T_a_2.append(math.log(mu_1048576-sigma_1048576,2))
expected_T_a_2.append(math.log(mu_2097152-sigma_2097152,2))
expected_T_a_2.append(math.log(mu_4194304-sigma_4194304,2))
expected_T_a_2.append(math.log(mu_8388608-sigma_8388608,2))
expected_T_a_2.append(math.log(mu_16777216-sigma_16777216,2))
plt.plot(t,expected_T_a_2,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_3 = []
expected_T_a_3.append(math.log(mu_32+2*sigma_32,2))
expected_T_a_3.append(math.log(mu_64+2*sigma_64,2))
expected_T_a_3.append(math.log(mu_128+2*sigma_128,2))
expected_T_a_3.append(math.log(mu_256+2*sigma_256,2))
expected_T_a_3.append(math.log(mu_512+2*sigma_512,2))
expected_T_a_3.append(math.log(mu_1024+2*sigma_1024,2))
expected_T_a_3.append(math.log(mu_2048+2*sigma_2048,2))
expected_T_a_3.append(math.log(mu_4096+2*sigma_4096,2))
expected_T_a_3.append(math.log(mu_8192+2*sigma_8192,2))
expected_T_a_3.append(math.log(mu_16384+2*sigma_16384,2))
expected_T_a_3.append(math.log(mu_32768+2*sigma_32768,2))
expected_T_a_3.append(math.log(mu_65536+2*sigma_65536,2))
expected_T_a_3.append(math.log(mu_131072+2*sigma_131072,2))
expected_T_a_3.append(math.log(mu_262144+2*sigma_262144,2))
expected_T_a_3.append(math.log(mu_524288+2*sigma_524288,2))
expected_T_a_3.append(math.log(mu_1048576+2*sigma_1048576,2))
expected_T_a_3.append(math.log(mu_2097152+2*sigma_2097152,2))
expected_T_a_3.append(math.log(mu_4194304+2*sigma_4194304,2))
expected_T_a_3.append(math.log(mu_8388608+2*sigma_8388608,2))
expected_T_a_3.append(math.log(mu_16777216+2*sigma_16777216,2))
plt.plot(t,expected_T_a_3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_4 = []
expected_T_a_4.append(math.log(mu_32-2*sigma_32,2))
expected_T_a_4.append(math.log(mu_64-2*sigma_64,2))
expected_T_a_4.append(math.log(mu_128-2*sigma_128,2))
expected_T_a_4.append(math.log(mu_256-2*sigma_256,2))
expected_T_a_4.append(math.log(mu_512-2*sigma_512,2))
expected_T_a_4.append(math.log(mu_1024-2*sigma_1024,2))
expected_T_a_4.append(math.log(mu_2048-2*sigma_2048,2))
expected_T_a_4.append(math.log(mu_4096-2*sigma_4096,2))
expected_T_a_4.append(math.log(mu_8192-2*sigma_8192,2))
expected_T_a_4.append(math.log(mu_16384-2*sigma_16384,2))
expected_T_a_4.append(math.log(mu_32768-2*sigma_32768,2))
expected_T_a_4.append(math.log(mu_65536-2*sigma_65536,2))
expected_T_a_4.append(math.log(mu_131072-2*sigma_131072,2))
expected_T_a_4.append(math.log(mu_262144-2*sigma_262144,2))
expected_T_a_4.append(math.log(mu_524288-2*sigma_524288,2))
expected_T_a_4.append(math.log(mu_1048576-2*sigma_1048576,2))
expected_T_a_4.append(math.log(mu_2097152-2*sigma_2097152,2))
expected_T_a_4.append(math.log(mu_4194304-2*sigma_4194304,2))
expected_T_a_4.append(math.log(mu_8388608-2*sigma_8388608,2))
expected_T_a_4.append(math.log(mu_16777216-2*sigma_16777216,2))
plt.plot(t,expected_T_a_4,linewidth=.1, linestyle="-", c="DimGray")

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_1, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_2, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_3, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_4, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_5, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_6, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_7, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_8, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_9, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_10, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_11, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_12, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_13, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_14, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_15, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_16, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_17, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_18, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_19, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_20, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_21, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_22, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_23, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_24, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_25, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_26, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_27, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_28, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_29, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_30, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_31, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_32, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_33, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_34, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_35, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_36, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_37, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_38, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_39, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_40, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_41, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_42, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_43, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_44, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_45, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_46, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_47, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_48, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_49, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_50, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_51, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_52, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_53, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_54, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_55, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_56, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_57, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_58, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_59, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_60, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_61, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_62, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_63, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_64, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_65, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_66, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_67, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_68, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_69, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_70, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_71, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_72, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_73, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_74, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_75, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_76, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_77, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_78, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_79, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_80, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_81, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_82, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_83, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_84, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_85, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_86, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_87, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_88, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_89, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_90, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_91, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_92, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_93, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_94, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_95, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_96, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_97, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_98, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_99, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_100, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_101, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_102, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_103, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_104, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_105, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_106, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_107, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_108, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_109, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_110, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_111, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_112, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_113, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_114, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_115, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_116, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_117, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_118, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_119, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_120, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_121, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_122, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_123, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_124, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_125, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_126, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_127, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_128, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_129, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_130, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_131, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_132, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_133, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_134, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_135, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_136, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_137, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_138, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_139, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_140, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_141, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_142, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_143, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_144, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_145, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_146, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_147, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_148, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_149, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_150, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_151, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_152, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_153, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_154, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_155, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_156, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_157, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_158, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_159, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_160, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_161, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_162, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_163, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_164, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_165, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_166, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_167, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_168, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_169, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_170, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_171, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_172, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_173, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_174, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_175, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_176, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_177, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_178, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_179, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_180, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_181, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_182, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_183, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_184, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_185, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_186, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_187, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_188, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_189, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_190, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_191, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_192, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_193, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_194, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_195, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_196, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_197, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_198, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_199, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_200, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_201, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_202, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_203, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_204, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_205, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_206, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_207, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_208, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_209, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_210, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_211, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_212, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_213, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_214, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_215, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_216, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_217, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_218, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_219, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_220, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_221, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_222, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_223, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_224, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_225, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_226, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_227, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_228, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_229, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_230, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_231, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_232, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_233, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_234, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_235, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_236, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_237, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_238, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_239, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_240, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_241, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_242, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_243, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_244, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_245, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_246, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_247, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_248, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_249, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_250, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_251, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_252, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_253, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_254, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_255, linewidth=.001, linestyle="-", c="red",alpha = .15)



#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=1)
plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=1)
plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=1)


#Formatting the plot
plt.xlabel('$log_2(|\phi|)$')
plt.ylabel('$log_2(T(\phi,a))$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 5 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(8.5,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
