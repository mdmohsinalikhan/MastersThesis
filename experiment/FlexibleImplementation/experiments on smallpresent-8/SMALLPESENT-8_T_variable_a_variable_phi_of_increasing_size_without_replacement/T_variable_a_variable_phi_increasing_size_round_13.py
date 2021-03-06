import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(240.000000,2),math.log(208.000000,2),math.log(208.000000,2),math.log(240.000000,2),math.log(293.000000,2),math.log(282.000000,2),math.log(268.500000,2),math.log(234.250000,2),math.log(240.562500,2),math.log(236.906250,2),math.log(264.812500,2),math.log(257.976562,2),math.log(249.328125,2),math.log(257.103516,2),math.log(256.785156,2),math.log(254.485352,2),math.log(230.057129,2),math.log(236.713379,2),math.log(266.871948,2),math.log(262.700165,2)]
t_1 = [math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(258.000000,2),math.log(255.000000,2),math.log(229.000000,2),math.log(227.750000,2),math.log(267.875000,2),math.log(268.875000,2),math.log(258.000000,2),math.log(279.671875,2),math.log(286.703125,2),math.log(270.390625,2),math.log(288.412109,2),math.log(263.970703,2),math.log(278.191406,2),math.log(230.798340,2),math.log(275.521118,2),math.log(267.545776,2),math.log(259.409821,2)]
t_2 = [math.log(240.000000,2),math.log(248.000000,2),math.log(296.000000,2),math.log(302.000000,2),math.log(266.000000,2),math.log(284.000000,2),math.log(265.500000,2),math.log(261.375000,2),math.log(249.000000,2),math.log(255.062500,2),math.log(267.265625,2),math.log(248.476562,2),math.log(258.554688,2),math.log(251.464844,2),math.log(259.954102,2),math.log(254.936035,2),math.log(247.894775,2),math.log(247.703247,2),math.log(267.088867,2),math.log(210.217590,2)]
t_3 = [math.log(240.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(222.000000,2),math.log(219.500000,2),math.log(232.250000,2),math.log(209.500000,2),math.log(234.312500,2),math.log(226.593750,2),math.log(247.562500,2),math.log(243.835938,2),math.log(256.109375,2),math.log(259.097656,2),math.log(278.988281,2),math.log(217.162109,2),math.log(239.316895,2),math.log(194.549927,2),math.log(218.150269,2),math.log(253.020691,2)]
t_4 = [math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(247.500000,2),math.log(242.250000,2),math.log(227.250000,2),math.log(224.625000,2),math.log(230.843750,2),math.log(241.187500,2),math.log(225.140625,2),math.log(223.718750,2),math.log(221.794922,2),math.log(231.386719,2),math.log(224.566406,2),math.log(224.264893,2),math.log(231.054443,2),math.log(214.973267,2),math.log(247.318176,2)]
t_5 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(252.000000,2),math.log(279.500000,2),math.log(312.000000,2),math.log(281.625000,2),math.log(277.250000,2),math.log(235.656250,2),math.log(235.609375,2),math.log(226.312500,2),math.log(250.964844,2),math.log(293.130859,2),math.log(262.964844,2),math.log(245.500000,2),math.log(269.168945,2),math.log(254.886108,2),math.log(241.943481,2),math.log(282.561340,2)]
t_6 = [math.log(240.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(262.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(250.250000,2),math.log(265.625000,2),math.log(260.625000,2),math.log(274.437500,2),math.log(289.781250,2),math.log(263.687500,2),math.log(268.136719,2),math.log(269.996094,2),math.log(282.426758,2),math.log(269.918457,2),math.log(246.792969,2),math.log(272.070435,2),math.log(279.922119,2),math.log(320.382538,2)]
t_7 = [math.log(272.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(212.000000,2),math.log(227.500000,2),math.log(220.000000,2),math.log(280.625000,2),math.log(262.812500,2),math.log(283.343750,2),math.log(264.187500,2),math.log(289.312500,2),math.log(267.324219,2),math.log(281.207031,2),math.log(276.595703,2),math.log(283.865723,2),math.log(261.243652,2),math.log(244.103882,2),math.log(222.436279,2),math.log(213.185944,2)]
t_8 = [math.log(288.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(242.000000,2),math.log(251.000000,2),math.log(242.250000,2),math.log(249.375000,2),math.log(212.750000,2),math.log(267.093750,2),math.log(262.367188,2),math.log(293.261719,2),math.log(301.904297,2),math.log(276.051758,2),math.log(250.571289,2),math.log(292.299072,2),math.log(256.184082,2),math.log(275.199646,2),math.log(266.655731,2)]
t_9 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(212.000000,2),math.log(257.000000,2),math.log(228.500000,2),math.log(274.000000,2),math.log(250.500000,2),math.log(216.062500,2),math.log(207.750000,2),math.log(248.890625,2),math.log(220.820312,2),math.log(273.667969,2),math.log(237.783203,2),math.log(221.552734,2),math.log(264.836914,2),math.log(249.175537,2),math.log(244.761841,2),math.log(239.522400,2),math.log(257.527649,2)]
t_10 = [math.log(256.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(282.000000,2),math.log(247.000000,2),math.log(286.500000,2),math.log(271.750000,2),math.log(249.250000,2),math.log(248.750000,2),math.log(264.781250,2),math.log(289.218750,2),math.log(288.554688,2),math.log(265.828125,2),math.log(248.992188,2),math.log(287.559570,2),math.log(285.750000,2),math.log(281.515137,2),math.log(252.513184,2),math.log(254.380127,2),math.log(256.861145,2)]
t_11 = [math.log(256.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(234.000000,2),math.log(260.500000,2),math.log(225.250000,2),math.log(234.375000,2),math.log(231.937500,2),math.log(276.875000,2),math.log(269.187500,2),math.log(311.789062,2),math.log(284.714844,2),math.log(290.599609,2),math.log(257.699219,2),math.log(247.437988,2),math.log(243.101562,2),math.log(236.396606,2),math.log(246.465515,2),math.log(246.307190,2)]
t_12 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(271.000000,2),math.log(275.125000,2),math.log(239.062500,2),math.log(235.718750,2),math.log(246.453125,2),math.log(238.843750,2),math.log(271.585938,2),math.log(242.107422,2),math.log(265.220703,2),math.log(251.222168,2),math.log(233.399902,2),math.log(225.748901,2),math.log(226.107605,2),math.log(263.838074,2)]
t_13 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(272.000000,2),math.log(243.500000,2),math.log(259.000000,2),math.log(276.750000,2),math.log(249.812500,2),math.log(270.375000,2),math.log(256.781250,2),math.log(300.492188,2),math.log(268.886719,2),math.log(271.283203,2),math.log(226.449219,2),math.log(273.251465,2),math.log(278.576660,2),math.log(287.344360,2),math.log(254.006104,2),math.log(242.832764,2)]
t_14 = [math.log(272.000000,2),math.log(264.000000,2),math.log(296.000000,2),math.log(274.000000,2),math.log(287.000000,2),math.log(310.500000,2),math.log(295.500000,2),math.log(335.125000,2),math.log(296.125000,2),math.log(269.062500,2),math.log(271.328125,2),math.log(267.679688,2),math.log(254.769531,2),math.log(260.300781,2),math.log(245.167969,2),math.log(221.187500,2),math.log(221.794678,2),math.log(250.427246,2),math.log(228.254639,2),math.log(234.180267,2)]
t_15 = [math.log(240.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(272.500000,2),math.log(291.000000,2),math.log(235.375000,2),math.log(247.562500,2),math.log(252.250000,2),math.log(267.281250,2),math.log(296.390625,2),math.log(295.761719,2),math.log(231.125000,2),math.log(243.887695,2),math.log(242.100586,2),math.log(232.650879,2),math.log(214.417236,2),math.log(213.363586,2),math.log(254.062225,2)]
t_16 = [math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(230.000000,2),math.log(244.000000,2),math.log(269.000000,2),math.log(278.000000,2),math.log(263.750000,2),math.log(286.375000,2),math.log(270.375000,2),math.log(252.281250,2),math.log(244.484375,2),math.log(224.746094,2),math.log(267.173828,2),math.log(249.518555,2),math.log(267.311035,2),math.log(253.883545,2),math.log(243.962891,2),math.log(249.164612,2),math.log(230.183990,2)]
t_17 = [math.log(240.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(240.000000,2),math.log(226.500000,2),math.log(279.500000,2),math.log(280.875000,2),math.log(303.062500,2),math.log(276.156250,2),math.log(275.000000,2),math.log(250.085938,2),math.log(237.113281,2),math.log(244.050781,2),math.log(240.835938,2),math.log(220.808594,2),math.log(282.061523,2),math.log(241.012085,2),math.log(276.450195,2),math.log(272.932831,2)]
t_18 = [math.log(256.000000,2),math.log(312.000000,2),math.log(320.000000,2),math.log(294.000000,2),math.log(282.000000,2),math.log(300.500000,2),math.log(292.250000,2),math.log(274.875000,2),math.log(256.875000,2),math.log(245.250000,2),math.log(247.000000,2),math.log(249.398438,2),math.log(290.945312,2),math.log(249.654297,2),math.log(255.012695,2),math.log(276.777344,2),math.log(287.625732,2),math.log(255.660645,2),math.log(261.043640,2),math.log(235.547058,2)]
t_19 = [math.log(272.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(234.250000,2),math.log(229.500000,2),math.log(259.562500,2),math.log(253.281250,2),math.log(260.796875,2),math.log(239.679688,2),math.log(247.921875,2),math.log(244.355469,2),math.log(266.294922,2),math.log(258.739746,2),math.log(274.293945,2),math.log(256.910645,2),math.log(262.145874,2),math.log(254.520782,2)]
t_20 = [math.log(224.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(214.000000,2),math.log(226.000000,2),math.log(260.500000,2),math.log(233.250000,2),math.log(253.750000,2),math.log(272.000000,2),math.log(224.125000,2),math.log(226.953125,2),math.log(230.546875,2),math.log(241.765625,2),math.log(242.791016,2),math.log(248.382812,2),math.log(219.208984,2),math.log(194.620850,2),math.log(233.673828,2),math.log(232.262695,2),math.log(218.220764,2)]
t_21 = [math.log(224.000000,2),math.log(240.000000,2),math.log(280.000000,2),math.log(292.000000,2),math.log(281.000000,2),math.log(249.000000,2),math.log(276.500000,2),math.log(282.625000,2),math.log(246.000000,2),math.log(254.531250,2),math.log(257.984375,2),math.log(258.210938,2),math.log(233.222656,2),math.log(220.689453,2),math.log(247.751953,2),math.log(256.084961,2),math.log(266.631592,2),math.log(252.208130,2),math.log(259.395569,2),math.log(251.265778,2)]
t_22 = [math.log(272.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(257.500000,2),math.log(253.500000,2),math.log(245.812500,2),math.log(210.406250,2),math.log(235.843750,2),math.log(268.601562,2),math.log(238.738281,2),math.log(224.529297,2),math.log(229.693359,2),math.log(273.580078,2),math.log(243.977539,2),math.log(249.796387,2),math.log(256.673401,2),math.log(261.790009,2)]
t_23 = [math.log(240.000000,2),math.log(216.000000,2),math.log(268.000000,2),math.log(280.000000,2),math.log(273.000000,2),math.log(276.500000,2),math.log(252.000000,2),math.log(257.000000,2),math.log(239.000000,2),math.log(231.781250,2),math.log(245.000000,2),math.log(274.070312,2),math.log(280.355469,2),math.log(277.957031,2),math.log(298.422852,2),math.log(271.323242,2),math.log(266.087646,2),math.log(227.619385,2),math.log(216.884644,2),math.log(252.156952,2)]
t_24 = [math.log(240.000000,2),math.log(272.000000,2),math.log(284.000000,2),math.log(270.000000,2),math.log(228.000000,2),math.log(243.500000,2),math.log(263.750000,2),math.log(261.125000,2),math.log(227.125000,2),math.log(213.843750,2),math.log(237.171875,2),math.log(235.734375,2),math.log(228.488281,2),math.log(243.732422,2),math.log(254.105469,2),math.log(223.180176,2),math.log(238.899414,2),math.log(231.483276,2),math.log(250.148804,2),math.log(267.024963,2)]
t_25 = [math.log(288.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(231.500000,2),math.log(222.000000,2),math.log(231.500000,2),math.log(255.250000,2),math.log(244.187500,2),math.log(264.875000,2),math.log(271.539062,2),math.log(271.250000,2),math.log(275.296875,2),math.log(258.172852,2),math.log(235.732422,2),math.log(264.169189,2),math.log(241.651245,2),math.log(222.232239,2),math.log(252.493164,2)]
t_26 = [math.log(272.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(245.500000,2),math.log(265.750000,2),math.log(276.375000,2),math.log(260.562500,2),math.log(244.187500,2),math.log(241.312500,2),math.log(247.937500,2),math.log(227.097656,2),math.log(209.173828,2),math.log(222.538086,2),math.log(242.932129,2),math.log(227.603760,2),math.log(258.020874,2),math.log(236.727661,2),math.log(243.539001,2)]
t_27 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(250.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(258.500000,2),math.log(258.750000,2),math.log(240.812500,2),math.log(241.437500,2),math.log(239.046875,2),math.log(249.609375,2),math.log(267.714844,2),math.log(278.523438,2),math.log(267.438477,2),math.log(244.766113,2),math.log(241.533936,2),math.log(223.398926,2),math.log(228.108398,2),math.log(229.680054,2)]
t_28 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(219.000000,2),math.log(233.500000,2),math.log(288.500000,2),math.log(268.250000,2),math.log(261.750000,2),math.log(275.343750,2),math.log(248.718750,2),math.log(241.390625,2),math.log(259.214844,2),math.log(267.931641,2),math.log(246.191406,2),math.log(263.405762,2),math.log(257.645020,2),math.log(265.767578,2),math.log(240.238953,2),math.log(270.601929,2)]
t_29 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(232.000000,2),math.log(263.000000,2),math.log(275.500000,2),math.log(277.500000,2),math.log(284.375000,2),math.log(264.062500,2),math.log(254.250000,2),math.log(270.593750,2),math.log(225.609375,2),math.log(214.527344,2),math.log(246.130859,2),math.log(231.996094,2),math.log(251.758789,2),math.log(257.026367,2),math.log(251.296875,2),math.log(272.559937,2),math.log(268.692047,2)]
t_30 = [math.log(336.000000,2),math.log(288.000000,2),math.log(304.000000,2),math.log(322.000000,2),math.log(308.000000,2),math.log(294.000000,2),math.log(280.000000,2),math.log(293.375000,2),math.log(313.000000,2),math.log(309.468750,2),math.log(263.250000,2),math.log(267.578125,2),math.log(252.187500,2),math.log(234.570312,2),math.log(262.166016,2),math.log(224.055176,2),math.log(245.381104,2),math.log(246.844727,2),math.log(245.087585,2),math.log(287.457581,2)]
t_31 = [math.log(272.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(242.000000,2),math.log(231.000000,2),math.log(210.000000,2),math.log(222.250000,2),math.log(254.000000,2),math.log(240.000000,2),math.log(275.000000,2),math.log(272.453125,2),math.log(257.281250,2),math.log(271.988281,2),math.log(268.425781,2),math.log(276.172852,2),math.log(291.054688,2),math.log(311.870117,2),math.log(264.697754,2),math.log(248.707642,2),math.log(241.951050,2)]
t_32 = [math.log(272.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(227.500000,2),math.log(205.750000,2),math.log(214.125000,2),math.log(216.187500,2),math.log(240.531250,2),math.log(271.843750,2),math.log(293.812500,2),math.log(269.503906,2),math.log(275.169922,2),math.log(261.304688,2),math.log(226.423828,2),math.log(218.731934,2),math.log(245.868896,2),math.log(274.390564,2),math.log(261.400208,2)]
t_33 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(278.000000,2),math.log(247.000000,2),math.log(262.500000,2),math.log(241.000000,2),math.log(252.750000,2),math.log(265.625000,2),math.log(259.250000,2),math.log(273.453125,2),math.log(236.531250,2),math.log(231.621094,2),math.log(253.816406,2),math.log(292.608398,2),math.log(291.811523,2),math.log(289.214355,2),math.log(288.213257,2),math.log(251.969849,2),math.log(265.832489,2)]
t_34 = [math.log(240.000000,2),math.log(248.000000,2),math.log(296.000000,2),math.log(278.000000,2),math.log(288.000000,2),math.log(273.000000,2),math.log(246.750000,2),math.log(235.125000,2),math.log(231.437500,2),math.log(278.843750,2),math.log(256.140625,2),math.log(244.531250,2),math.log(234.890625,2),math.log(239.222656,2),math.log(217.195312,2),math.log(218.327148,2),math.log(232.981445,2),math.log(226.021729,2),math.log(233.812561,2),math.log(240.433075,2)]
t_35 = [math.log(272.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(228.000000,2),math.log(213.000000,2),math.log(235.000000,2),math.log(267.250000,2),math.log(250.375000,2),math.log(283.937500,2),math.log(267.312500,2),math.log(270.843750,2),math.log(244.820312,2),math.log(214.664062,2),math.log(240.669922,2),math.log(260.215820,2),math.log(272.447754,2),math.log(272.424072,2),math.log(281.075806,2),math.log(242.106018,2),math.log(217.564209,2)]
t_36 = [math.log(256.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(223.000000,2),math.log(229.500000,2),math.log(229.000000,2),math.log(285.000000,2),math.log(304.375000,2),math.log(288.531250,2),math.log(295.593750,2),math.log(286.781250,2),math.log(242.406250,2),math.log(260.873047,2),math.log(264.246094,2),math.log(248.143555,2),math.log(208.934814,2),math.log(215.396240,2),math.log(258.242676,2),math.log(225.780914,2)]
t_37 = [math.log(256.000000,2),math.log(232.000000,2),math.log(276.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(208.000000,2),math.log(223.000000,2),math.log(274.125000,2),math.log(286.500000,2),math.log(310.156250,2),math.log(295.078125,2),math.log(262.898438,2),math.log(317.835938,2),math.log(289.251953,2),math.log(277.577148,2),math.log(241.833496,2),math.log(258.106201,2),math.log(240.315430,2),math.log(260.381104,2),math.log(286.760223,2)]
t_38 = [math.log(256.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(242.000000,2),math.log(219.500000,2),math.log(193.000000,2),math.log(213.500000,2),math.log(240.000000,2),math.log(225.000000,2),math.log(249.765625,2),math.log(262.375000,2),math.log(281.523438,2),math.log(256.410156,2),math.log(251.443359,2),math.log(260.294434,2),math.log(242.416504,2),math.log(284.094727,2),math.log(235.154907,2),math.log(240.459686,2)]
t_39 = [math.log(240.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(242.000000,2),math.log(275.000000,2),math.log(292.500000,2),math.log(290.250000,2),math.log(279.250000,2),math.log(262.312500,2),math.log(265.406250,2),math.log(259.671875,2),math.log(246.093750,2),math.log(248.566406,2),math.log(217.333984,2),math.log(230.176758,2),math.log(224.140137,2),math.log(208.912354,2),math.log(208.797363,2),math.log(219.265320,2),math.log(238.572601,2)]
t_40 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(286.000000,2),math.log(226.000000,2),math.log(237.000000,2),math.log(253.750000,2),math.log(241.625000,2),math.log(305.687500,2),math.log(315.687500,2),math.log(266.093750,2),math.log(274.203125,2),math.log(260.019531,2),math.log(248.449219,2),math.log(259.931641,2),math.log(271.870117,2),math.log(242.321289,2),math.log(259.129150,2),math.log(229.519836,2),math.log(260.251740,2)]
t_41 = [math.log(288.000000,2),math.log(336.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(237.000000,2),math.log(243.500000,2),math.log(266.000000,2),math.log(256.375000,2),math.log(246.125000,2),math.log(259.375000,2),math.log(233.109375,2),math.log(257.210938,2),math.log(277.167969,2),math.log(271.566406,2),math.log(254.655273,2),math.log(274.859863,2),math.log(243.313477,2),math.log(299.363770,2),math.log(292.693237,2),math.log(249.350891,2)]
t_42 = [math.log(256.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(204.500000,2),math.log(197.750000,2),math.log(218.125000,2),math.log(262.000000,2),math.log(243.000000,2),math.log(219.031250,2),math.log(257.820312,2),math.log(271.761719,2),math.log(236.990234,2),math.log(263.176758,2),math.log(251.536621,2),math.log(266.046387,2),math.log(269.796265,2),math.log(255.174377,2),math.log(298.243805,2)]
t_43 = [math.log(256.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(233.500000,2),math.log(256.750000,2),math.log(257.500000,2),math.log(266.312500,2),math.log(254.312500,2),math.log(246.593750,2),math.log(241.148438,2),math.log(267.328125,2),math.log(279.486328,2),math.log(233.498047,2),math.log(248.562988,2),math.log(236.826904,2),math.log(268.893555,2),math.log(247.336975,2),math.log(261.246918,2)]
t_44 = [math.log(256.000000,2),math.log(280.000000,2),math.log(324.000000,2),math.log(298.000000,2),math.log(284.000000,2),math.log(281.000000,2),math.log(254.250000,2),math.log(224.875000,2),math.log(234.062500,2),math.log(226.718750,2),math.log(240.859375,2),math.log(231.601562,2),math.log(244.945312,2),math.log(244.931641,2),math.log(232.344727,2),math.log(247.758301,2),math.log(237.431641,2),math.log(243.476685,2),math.log(255.502991,2),math.log(254.735352,2)]
t_45 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(222.000000,2),math.log(256.000000,2),math.log(257.250000,2),math.log(246.625000,2),math.log(267.625000,2),math.log(290.125000,2),math.log(293.828125,2),math.log(281.554688,2),math.log(274.066406,2),math.log(222.250000,2),math.log(264.986328,2),math.log(252.302734,2),math.log(259.871826,2),math.log(259.083740,2),math.log(274.482788,2),math.log(268.143860,2)]
t_46 = [math.log(256.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(240.000000,2),math.log(238.000000,2),math.log(228.000000,2),math.log(271.250000,2),math.log(241.875000,2),math.log(215.812500,2),math.log(207.500000,2),math.log(198.296875,2),math.log(195.367188,2),math.log(225.222656,2),math.log(251.220703,2),math.log(243.361328,2),math.log(247.174316,2),math.log(284.189453,2),math.log(253.305420,2),math.log(260.156982,2),math.log(271.582733,2)]
t_47 = [math.log(256.000000,2),math.log(248.000000,2),math.log(204.000000,2),math.log(198.000000,2),math.log(232.000000,2),math.log(237.000000,2),math.log(260.750000,2),math.log(234.250000,2),math.log(266.750000,2),math.log(241.906250,2),math.log(232.843750,2),math.log(217.320312,2),math.log(231.253906,2),math.log(219.609375,2),math.log(235.767578,2),math.log(241.813477,2),math.log(224.993652,2),math.log(243.321289,2),math.log(264.215698,2),math.log(263.691071,2)]
t_48 = [math.log(240.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(283.000000,2),math.log(269.000000,2),math.log(248.250000,2),math.log(253.625000,2),math.log(251.312500,2),math.log(257.343750,2),math.log(235.859375,2),math.log(251.164062,2),math.log(237.132812,2),math.log(227.125000,2),math.log(241.033203,2),math.log(253.495117,2),math.log(271.580322,2),math.log(268.179321,2),math.log(286.570251,2),math.log(251.964752,2)]
t_49 = [math.log(272.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(245.000000,2),math.log(250.000000,2),math.log(253.000000,2),math.log(213.625000,2),math.log(205.812500,2),math.log(238.156250,2),math.log(243.781250,2),math.log(270.476562,2),math.log(279.949219,2),math.log(246.833984,2),math.log(237.915039,2),math.log(288.044434,2),math.log(265.944824,2),math.log(255.236450,2),math.log(219.070862,2),math.log(222.109344,2)]
t_50 = [math.log(288.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(249.000000,2),math.log(239.000000,2),math.log(271.000000,2),math.log(241.000000,2),math.log(270.312500,2),math.log(260.562500,2),math.log(263.265625,2),math.log(240.921875,2),math.log(248.515625,2),math.log(265.246094,2),math.log(248.413086,2),math.log(233.134277,2),math.log(242.975098,2),math.log(244.727661,2),math.log(227.062439,2),math.log(226.066711,2)]
t_51 = [math.log(256.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(252.000000,2),math.log(257.500000,2),math.log(258.250000,2),math.log(271.375000,2),math.log(271.312500,2),math.log(294.687500,2),math.log(276.453125,2),math.log(272.453125,2),math.log(262.175781,2),math.log(268.599609,2),math.log(277.101562,2),math.log(274.637207,2),math.log(273.232910,2),math.log(272.357788,2),math.log(228.261169,2),math.log(226.305847,2)]
t_52 = [math.log(256.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(271.000000,2),math.log(245.500000,2),math.log(253.125000,2),math.log(286.187500,2),math.log(252.406250,2),math.log(257.312500,2),math.log(267.312500,2),math.log(251.460938,2),math.log(250.400391,2),math.log(255.356445,2),math.log(244.821289,2),math.log(250.148193,2),math.log(277.805298,2),math.log(238.555542,2),math.log(238.224884,2)]
t_53 = [math.log(256.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(222.000000,2),math.log(252.000000,2),math.log(251.000000,2),math.log(225.750000,2),math.log(224.125000,2),math.log(272.000000,2),math.log(241.593750,2),math.log(215.015625,2),math.log(208.226562,2),math.log(222.128906,2),math.log(251.179688,2),math.log(266.165039,2),math.log(251.577148,2),math.log(261.656006,2),math.log(261.370239,2),math.log(268.033691,2),math.log(280.675537,2)]
t_54 = [math.log(224.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(339.000000,2),math.log(316.000000,2),math.log(286.500000,2),math.log(277.000000,2),math.log(250.312500,2),math.log(251.093750,2),math.log(256.500000,2),math.log(227.523438,2),math.log(254.007812,2),math.log(202.664062,2),math.log(212.712891,2),math.log(224.104004,2),math.log(250.808594,2),math.log(261.283203,2),math.log(236.151855,2),math.log(238.208069,2)]
t_55 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(240.000000,2),math.log(266.000000,2),math.log(236.500000,2),math.log(251.125000,2),math.log(276.187500,2),math.log(238.625000,2),math.log(226.437500,2),math.log(252.640625,2),math.log(229.097656,2),math.log(254.283203,2),math.log(250.232422,2),math.log(227.365234,2),math.log(236.271973,2),math.log(239.874878,2),math.log(230.427002,2),math.log(249.690796,2)]
t_56 = [math.log(256.000000,2),math.log(280.000000,2),math.log(240.000000,2),math.log(258.000000,2),math.log(283.000000,2),math.log(262.000000,2),math.log(263.000000,2),math.log(303.375000,2),math.log(257.312500,2),math.log(236.031250,2),math.log(278.000000,2),math.log(278.492188,2),math.log(242.488281,2),math.log(244.513672,2),math.log(236.191406,2),math.log(222.346680,2),math.log(241.358887,2),math.log(261.455322,2),math.log(284.896240,2),math.log(240.637115,2)]
t_57 = [math.log(256.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(300.000000,2),math.log(221.000000,2),math.log(244.500000,2),math.log(258.500000,2),math.log(252.125000,2),math.log(234.062500,2),math.log(233.437500,2),math.log(242.687500,2),math.log(241.257812,2),math.log(255.773438,2),math.log(252.119141,2),math.log(261.147461,2),math.log(261.336426,2),math.log(240.116455,2),math.log(238.102905,2),math.log(219.696777,2),math.log(208.027191,2)]
t_58 = [math.log(256.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(221.000000,2),math.log(245.500000,2),math.log(236.000000,2),math.log(215.625000,2),math.log(237.062500,2),math.log(237.343750,2),math.log(262.937500,2),math.log(296.765625,2),math.log(254.953125,2),math.log(236.544922,2),math.log(229.724609,2),math.log(243.725586,2),math.log(240.745850,2),math.log(243.828491,2),math.log(235.663330,2),math.log(264.753479,2)]
t_59 = [math.log(256.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(230.000000,2),math.log(209.000000,2),math.log(223.000000,2),math.log(232.000000,2),math.log(247.000000,2),math.log(241.250000,2),math.log(242.843750,2),math.log(228.453125,2),math.log(279.296875,2),math.log(298.355469,2),math.log(271.357422,2),math.log(289.948242,2),math.log(280.915527,2),math.log(245.915771,2),math.log(272.131470,2),math.log(211.312927,2),math.log(218.413818,2)]
t_60 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(274.000000,2),math.log(257.000000,2),math.log(270.000000,2),math.log(264.750000,2),math.log(240.875000,2),math.log(247.750000,2),math.log(270.437500,2),math.log(273.781250,2),math.log(250.617188,2),math.log(276.183594,2),math.log(245.320312,2),math.log(246.366211,2),math.log(313.857422,2),math.log(304.702148,2),math.log(258.597656,2),math.log(285.662598,2),math.log(306.934906,2)]
t_61 = [math.log(288.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(238.000000,2),math.log(273.000000,2),math.log(261.500000,2),math.log(275.250000,2),math.log(273.000000,2),math.log(205.250000,2),math.log(204.156250,2),math.log(245.921875,2),math.log(277.570312,2),math.log(270.570312,2),math.log(234.134766,2),math.log(214.559570,2),math.log(210.864746,2),math.log(221.001465,2),math.log(228.085815,2),math.log(247.669861,2),math.log(236.454681,2)]
t_62 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(255.000000,2),math.log(268.500000,2),math.log(262.250000,2),math.log(256.750000,2),math.log(251.375000,2),math.log(257.406250,2),math.log(300.078125,2),math.log(274.351562,2),math.log(275.628906,2),math.log(269.638672,2),math.log(249.858398,2),math.log(287.485840,2),math.log(282.473877,2),math.log(275.165283,2),math.log(278.366455,2),math.log(285.906738,2)]
t_63 = [math.log(240.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(224.000000,2),math.log(234.000000,2),math.log(238.000000,2),math.log(262.250000,2),math.log(240.000000,2),math.log(237.437500,2),math.log(262.312500,2),math.log(226.484375,2),math.log(243.843750,2),math.log(238.039062,2),math.log(252.880859,2),math.log(217.848633,2),math.log(273.285156,2),math.log(253.110107,2),math.log(249.677856,2),math.log(220.747986,2),math.log(199.646515,2)]
t_64 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(256.000000,2),math.log(274.500000,2),math.log(292.250000,2),math.log(297.750000,2),math.log(283.875000,2),math.log(267.187500,2),math.log(228.015625,2),math.log(248.609375,2),math.log(252.957031,2),math.log(261.501953,2),math.log(258.971680,2),math.log(257.833008,2),math.log(243.930420,2),math.log(254.071167,2),math.log(253.762085,2),math.log(225.101654,2)]
t_65 = [math.log(256.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(234.000000,2),math.log(250.000000,2),math.log(251.500000,2),math.log(280.000000,2),math.log(271.625000,2),math.log(271.937500,2),math.log(262.437500,2),math.log(245.406250,2),math.log(265.804688,2),math.log(280.597656,2),math.log(273.035156,2),math.log(272.841797,2),math.log(261.492676,2),math.log(293.640137,2),math.log(260.694336,2),math.log(264.072144,2),math.log(248.423920,2)]
t_66 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(249.000000,2),math.log(234.500000,2),math.log(212.250000,2),math.log(227.250000,2),math.log(269.687500,2),math.log(276.187500,2),math.log(260.156250,2),math.log(277.140625,2),math.log(304.847656,2),math.log(268.074219,2),math.log(292.601562,2),math.log(309.463867,2),math.log(271.398682,2),math.log(254.257690,2),math.log(222.946350,2),math.log(238.356232,2)]
t_67 = [math.log(288.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(253.000000,2),math.log(238.500000,2),math.log(231.000000,2),math.log(233.375000,2),math.log(211.937500,2),math.log(220.656250,2),math.log(246.765625,2),math.log(222.023438,2),math.log(215.949219,2),math.log(231.623047,2),math.log(233.643555,2),math.log(212.465820,2),math.log(223.597656,2),math.log(232.480103,2),math.log(255.951111,2),math.log(259.923309,2)]
t_68 = [math.log(240.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(246.500000,2),math.log(257.750000,2),math.log(283.125000,2),math.log(258.250000,2),math.log(268.187500,2),math.log(260.796875,2),math.log(228.414062,2),math.log(216.578125,2),math.log(212.132812,2),math.log(222.316406,2),math.log(238.981934,2),math.log(237.660400,2),math.log(260.524170,2),math.log(253.093872,2),math.log(251.903259,2)]
t_69 = [math.log(256.000000,2),math.log(248.000000,2),math.log(296.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(237.500000,2),math.log(274.250000,2),math.log(270.500000,2),math.log(302.875000,2),math.log(309.875000,2),math.log(302.828125,2),math.log(279.242188,2),math.log(245.578125,2),math.log(236.341797,2),math.log(248.253906,2),math.log(289.839844,2),math.log(247.517334,2),math.log(245.918213,2),math.log(276.003845,2),math.log(270.649933,2)]
t_70 = [math.log(288.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(213.000000,2),math.log(228.000000,2),math.log(265.000000,2),math.log(268.750000,2),math.log(248.000000,2),math.log(243.593750,2),math.log(287.875000,2),math.log(298.078125,2),math.log(285.179688,2),math.log(236.455078,2),math.log(292.671875,2),math.log(252.241211,2),math.log(232.296143,2),math.log(226.621216,2),math.log(267.524658,2),math.log(277.978149,2)]
t_71 = [math.log(272.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(243.000000,2),math.log(288.000000,2),math.log(265.000000,2),math.log(291.500000,2),math.log(320.875000,2),math.log(289.125000,2),math.log(294.875000,2),math.log(275.359375,2),math.log(260.796875,2),math.log(233.421875,2),math.log(241.603516,2),math.log(206.235840,2),math.log(226.054199,2),math.log(233.246094,2),math.log(235.805786,2),math.log(254.288605,2)]
t_72 = [math.log(224.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(234.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(254.750000,2),math.log(238.375000,2),math.log(245.937500,2),math.log(252.156250,2),math.log(240.890625,2),math.log(274.914062,2),math.log(286.039062,2),math.log(243.105469,2),math.log(242.793945,2),math.log(261.627441,2),math.log(246.531982,2),math.log(256.202881,2),math.log(287.878235,2),math.log(267.953369,2)]
t_73 = [math.log(288.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(266.000000,2),math.log(260.000000,2),math.log(280.500000,2),math.log(265.500000,2),math.log(253.875000,2),math.log(259.875000,2),math.log(249.937500,2),math.log(246.234375,2),math.log(236.625000,2),math.log(256.230469,2),math.log(236.021484,2),math.log(251.516602,2),math.log(255.147949,2),math.log(277.478516,2),math.log(281.195312,2),math.log(269.684082,2),math.log(321.522766,2)]
t_74 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(235.000000,2),math.log(251.000000,2),math.log(209.500000,2),math.log(240.250000,2),math.log(268.875000,2),math.log(259.750000,2),math.log(250.562500,2),math.log(212.195312,2),math.log(246.195312,2),math.log(284.705078,2),math.log(271.529297,2),math.log(300.531738,2),math.log(284.523682,2),math.log(264.256836,2),math.log(250.950745,2),math.log(230.021423,2)]
t_75 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(292.000000,2),math.log(266.000000,2),math.log(273.500000,2),math.log(285.250000,2),math.log(254.375000,2),math.log(278.937500,2),math.log(255.125000,2),math.log(243.843750,2),math.log(240.882812,2),math.log(252.816406,2),math.log(247.496094,2),math.log(252.107422,2),math.log(288.189453,2),math.log(232.173828,2),math.log(245.273071,2),math.log(228.841980,2),math.log(282.047150,2)]
t_76 = [math.log(240.000000,2),math.log(304.000000,2),math.log(304.000000,2),math.log(250.000000,2),math.log(274.000000,2),math.log(274.000000,2),math.log(219.000000,2),math.log(203.750000,2),math.log(227.937500,2),math.log(233.937500,2),math.log(225.843750,2),math.log(242.281250,2),math.log(253.375000,2),math.log(235.244141,2),math.log(252.817383,2),math.log(226.371094,2),math.log(247.282227,2),math.log(217.505249,2),math.log(259.844299,2),math.log(242.586426,2)]
t_77 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(230.000000,2),math.log(247.000000,2),math.log(261.500000,2),math.log(243.500000,2),math.log(295.375000,2),math.log(255.250000,2),math.log(267.093750,2),math.log(269.453125,2),math.log(263.445312,2),math.log(270.714844,2),math.log(271.015625,2),math.log(220.852539,2),math.log(261.380371,2),math.log(262.420166,2),math.log(279.348633,2),math.log(251.924988,2),math.log(279.976807,2)]
t_78 = [math.log(240.000000,2),math.log(240.000000,2),math.log(212.000000,2),math.log(232.000000,2),math.log(250.000000,2),math.log(233.500000,2),math.log(228.750000,2),math.log(265.875000,2),math.log(247.000000,2),math.log(224.750000,2),math.log(232.015625,2),math.log(240.773438,2),math.log(226.738281,2),math.log(206.800781,2),math.log(226.426758,2),math.log(236.895508,2),math.log(247.510498,2),math.log(272.043213,2),math.log(224.948608,2),math.log(247.569550,2)]
t_79 = [math.log(240.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(274.000000,2),math.log(269.000000,2),math.log(233.000000,2),math.log(265.000000,2),math.log(284.500000,2),math.log(264.250000,2),math.log(270.250000,2),math.log(262.031250,2),math.log(266.710938,2),math.log(232.968750,2),math.log(200.750000,2),math.log(200.593750,2),math.log(197.165039,2),math.log(192.300049,2),math.log(201.431641,2),math.log(256.243225,2),math.log(267.038361,2)]
t_80 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(247.000000,2),math.log(267.250000,2),math.log(229.875000,2),math.log(247.687500,2),math.log(249.218750,2),math.log(232.250000,2),math.log(241.257812,2),math.log(243.460938,2),math.log(219.294922,2),math.log(249.591797,2),math.log(220.629883,2),math.log(233.486328,2),math.log(267.349243,2),math.log(268.280029,2),math.log(259.948181,2)]
t_81 = [math.log(224.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(266.000000,2),math.log(243.000000,2),math.log(254.500000,2),math.log(229.250000,2),math.log(227.625000,2),math.log(225.125000,2),math.log(220.343750,2),math.log(221.578125,2),math.log(248.960938,2),math.log(244.562500,2),math.log(229.054688,2),math.log(243.250000,2),math.log(262.359375,2),math.log(223.546631,2),math.log(249.937866,2),math.log(214.005798,2),math.log(218.206879,2)]
t_82 = [math.log(256.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(235.000000,2),math.log(239.500000,2),math.log(266.500000,2),math.log(242.500000,2),math.log(257.625000,2),math.log(257.187500,2),math.log(264.140625,2),math.log(280.585938,2),math.log(262.531250,2),math.log(297.154297,2),math.log(280.857422,2),math.log(285.821289,2),math.log(292.009766,2),math.log(274.104492,2),math.log(257.629089,2),math.log(246.665039,2)]
t_83 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(283.000000,2),math.log(239.500000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(219.187500,2),math.log(257.656250,2),math.log(244.937500,2),math.log(234.820312,2),math.log(251.304688,2),math.log(211.574219,2),math.log(231.333008,2),math.log(276.556641,2),math.log(247.173828,2),math.log(265.465332,2),math.log(246.859985,2),math.log(222.057617,2)]
t_84 = [math.log(240.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(242.000000,2),math.log(234.000000,2),math.log(241.500000,2),math.log(278.000000,2),math.log(234.875000,2),math.log(235.187500,2),math.log(239.531250,2),math.log(221.890625,2),math.log(246.906250,2),math.log(255.492188,2),math.log(254.412109,2),math.log(257.328125,2),math.log(219.317871,2),math.log(238.306396,2),math.log(281.107422,2),math.log(252.343628,2),math.log(227.717957,2)]
t_85 = [math.log(288.000000,2),math.log(288.000000,2),math.log(308.000000,2),math.log(266.000000,2),math.log(232.000000,2),math.log(246.500000,2),math.log(272.000000,2),math.log(240.625000,2),math.log(233.312500,2),math.log(224.968750,2),math.log(263.812500,2),math.log(254.726562,2),math.log(245.128906,2),math.log(252.611328,2),math.log(249.719727,2),math.log(261.290039,2),math.log(230.876953,2),math.log(253.199341,2),math.log(296.124146,2),math.log(282.723633,2)]
t_86 = [math.log(224.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(266.000000,2),math.log(247.000000,2),math.log(255.000000,2),math.log(281.500000,2),math.log(271.000000,2),math.log(264.250000,2),math.log(265.343750,2),math.log(264.828125,2),math.log(259.593750,2),math.log(256.445312,2),math.log(238.646484,2),math.log(207.366211,2),math.log(225.719238,2),math.log(225.115723,2),math.log(256.370483,2),math.log(240.790955,2),math.log(279.271057,2)]
t_87 = [math.log(288.000000,2),math.log(296.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(285.000000,2),math.log(255.000000,2),math.log(236.000000,2),math.log(226.375000,2),math.log(242.750000,2),math.log(211.093750,2),math.log(227.125000,2),math.log(198.984375,2),math.log(204.878906,2),math.log(233.574219,2),math.log(202.588867,2),math.log(251.067871,2),math.log(218.588867,2),math.log(235.695923,2),math.log(232.580994,2),math.log(232.760803,2)]
t_88 = [math.log(304.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(229.000000,2),math.log(216.500000,2),math.log(233.250000,2),math.log(210.000000,2),math.log(264.375000,2),math.log(237.312500,2),math.log(286.218750,2),math.log(254.429688,2),math.log(240.050781,2),math.log(223.962891,2),math.log(236.789062,2),math.log(230.865723,2),math.log(265.854736,2),math.log(250.229370,2),math.log(256.830566,2),math.log(289.070435,2)]
t_89 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(254.000000,2),math.log(262.500000,2),math.log(275.750000,2),math.log(237.375000,2),math.log(227.187500,2),math.log(220.406250,2),math.log(245.703125,2),math.log(240.062500,2),math.log(260.859375,2),math.log(266.140625,2),math.log(252.439453,2),math.log(284.020508,2),math.log(281.120605,2),math.log(241.470093,2),math.log(235.337158,2),math.log(239.361053,2)]
t_90 = [math.log(288.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(220.000000,2),math.log(249.000000,2),math.log(259.000000,2),math.log(264.500000,2),math.log(237.875000,2),math.log(232.187500,2),math.log(246.093750,2),math.log(247.484375,2),math.log(256.070312,2),math.log(252.980469,2),math.log(245.996094,2),math.log(260.003906,2),math.log(239.992188,2),math.log(215.601807,2),math.log(211.786621,2),math.log(258.920715,2),math.log(263.759552,2)]
t_91 = [math.log(256.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(302.000000,2),math.log(309.500000,2),math.log(265.250000,2),math.log(221.875000,2),math.log(226.000000,2),math.log(249.906250,2),math.log(236.390625,2),math.log(220.789062,2),math.log(259.207031,2),math.log(219.843750,2),math.log(216.039062,2),math.log(240.514648,2),math.log(216.946289,2),math.log(239.178833,2),math.log(258.610962,2),math.log(282.283813,2)]
t_92 = [math.log(256.000000,2),math.log(256.000000,2),math.log(212.000000,2),math.log(226.000000,2),math.log(242.000000,2),math.log(265.000000,2),math.log(248.000000,2),math.log(253.125000,2),math.log(260.625000,2),math.log(262.156250,2),math.log(235.078125,2),math.log(246.242188,2),math.log(252.546875,2),math.log(251.119141,2),math.log(241.172852,2),math.log(273.628418,2),math.log(241.691650,2),math.log(258.386108,2),math.log(239.073181,2),math.log(229.335419,2)]
t_93 = [math.log(320.000000,2),math.log(368.000000,2),math.log(328.000000,2),math.log(312.000000,2),math.log(303.000000,2),math.log(274.000000,2),math.log(254.250000,2),math.log(253.250000,2),math.log(281.937500,2),math.log(246.312500,2),math.log(219.609375,2),math.log(253.164062,2),math.log(249.765625,2),math.log(257.441406,2),math.log(244.266602,2),math.log(291.869141,2),math.log(244.859619,2),math.log(204.867188,2),math.log(222.091003,2),math.log(250.646698,2)]
t_94 = [math.log(240.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(276.000000,2),math.log(271.000000,2),math.log(256.500000,2),math.log(232.500000,2),math.log(227.125000,2),math.log(222.687500,2),math.log(224.875000,2),math.log(257.625000,2),math.log(230.835938,2),math.log(236.250000,2),math.log(226.460938,2),math.log(247.299805,2),math.log(243.324219,2),math.log(273.835938,2),math.log(276.449219,2),math.log(250.010803,2),math.log(242.066772,2)]
t_95 = [math.log(288.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(258.000000,2),math.log(262.000000,2),math.log(226.000000,2),math.log(229.750000,2),math.log(264.000000,2),math.log(252.500000,2),math.log(248.531250,2),math.log(235.734375,2),math.log(255.593750,2),math.log(229.523438,2),math.log(240.017578,2),math.log(263.584961,2),math.log(277.123047,2),math.log(239.061279,2),math.log(246.245605,2),math.log(255.797729,2),math.log(246.216980,2)]
t_96 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(302.000000,2),math.log(252.000000,2),math.log(216.500000,2),math.log(228.000000,2),math.log(241.875000,2),math.log(241.875000,2),math.log(254.312500,2),math.log(241.578125,2),math.log(258.773438,2),math.log(230.949219,2),math.log(232.542969,2),math.log(238.672852,2),math.log(279.886230,2),math.log(267.520508,2),math.log(275.007202,2),math.log(257.414124,2),math.log(251.133270,2)]
t_97 = [math.log(240.000000,2),math.log(256.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(242.000000,2),math.log(235.500000,2),math.log(264.000000,2),math.log(259.500000,2),math.log(248.875000,2),math.log(269.812500,2),math.log(260.281250,2),math.log(274.468750,2),math.log(277.621094,2),math.log(269.363281,2),math.log(254.256836,2),math.log(281.872559,2),math.log(250.828369,2),math.log(264.144897,2),math.log(254.998779,2),math.log(240.310516,2)]
t_98 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(282.000000,2),math.log(264.000000,2),math.log(254.500000,2),math.log(288.000000,2),math.log(251.750000,2),math.log(271.375000,2),math.log(247.906250,2),math.log(243.906250,2),math.log(284.140625,2),math.log(259.609375,2),math.log(244.144531,2),math.log(230.862305,2),math.log(219.086426,2),math.log(248.927734,2),math.log(259.626709,2),math.log(222.403992,2),math.log(224.017548,2)]
t_99 = [math.log(288.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(290.000000,2),math.log(280.000000,2),math.log(258.500000,2),math.log(243.750000,2),math.log(223.500000,2),math.log(268.250000,2),math.log(258.281250,2),math.log(260.671875,2),math.log(301.703125,2),math.log(271.316406,2),math.log(278.427734,2),math.log(239.722656,2),math.log(235.695312,2),math.log(271.819580,2),math.log(270.346069,2),math.log(234.967163,2),math.log(236.074524,2)]
t_100 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(267.000000,2),math.log(224.500000,2),math.log(247.625000,2),math.log(253.875000,2),math.log(245.781250,2),math.log(258.046875,2),math.log(274.562500,2),math.log(272.886719,2),math.log(307.583984,2),math.log(266.791992,2),math.log(239.947266,2),math.log(271.094238,2),math.log(237.676514,2),math.log(250.725220,2),math.log(233.354889,2)]
t_101 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(242.000000,2),math.log(242.000000,2),math.log(231.500000,2),math.log(222.250000,2),math.log(283.875000,2),math.log(280.312500,2),math.log(272.156250,2),math.log(284.687500,2),math.log(261.078125,2),math.log(250.722656,2),math.log(274.550781,2),math.log(258.757812,2),math.log(235.855957,2),math.log(205.705566,2),math.log(216.604736,2),math.log(234.638062,2),math.log(262.498322,2)]
t_102 = [math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(265.000000,2),math.log(275.000000,2),math.log(259.750000,2),math.log(249.125000,2),math.log(271.625000,2),math.log(242.000000,2),math.log(236.640625,2),math.log(240.171875,2),math.log(259.390625,2),math.log(266.289062,2),math.log(261.864258,2),math.log(241.512695,2),math.log(269.222412,2),math.log(257.716187,2),math.log(247.275146,2),math.log(240.357910,2)]
t_103 = [math.log(240.000000,2),math.log(224.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(253.000000,2),math.log(252.500000,2),math.log(291.500000,2),math.log(291.250000,2),math.log(293.937500,2),math.log(236.875000,2),math.log(235.859375,2),math.log(231.000000,2),math.log(246.093750,2),math.log(258.833984,2),math.log(255.607422,2),math.log(269.474121,2),math.log(237.883057,2),math.log(224.897461,2),math.log(216.318359,2),math.log(231.303436,2)]
t_104 = [math.log(224.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(294.250000,2),math.log(257.187500,2),math.log(257.625000,2),math.log(297.171875,2),math.log(285.789062,2),math.log(260.210938,2),math.log(277.939453,2),math.log(313.814453,2),math.log(318.272949,2),math.log(260.025146,2),math.log(289.999756,2),math.log(264.053223,2),math.log(238.766632,2)]
t_105 = [math.log(224.000000,2),math.log(224.000000,2),math.log(212.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(240.500000,2),math.log(258.500000,2),math.log(272.875000,2),math.log(275.187500,2),math.log(272.500000,2),math.log(275.687500,2),math.log(255.742188,2),math.log(238.546875,2),math.log(229.548828,2),math.log(237.776367,2),math.log(251.793457,2),math.log(284.498291,2),math.log(275.275269,2),math.log(280.853149,2),math.log(270.893982,2)]
t_106 = [math.log(256.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(250.000000,2),math.log(245.000000,2),math.log(268.000000,2),math.log(227.000000,2),math.log(233.875000,2),math.log(229.062500,2),math.log(301.187500,2),math.log(331.843750,2),math.log(297.437500,2),math.log(254.656250,2),math.log(254.128906,2),math.log(254.898438,2),math.log(241.347656,2),math.log(220.013184,2),math.log(249.453369,2),math.log(288.732239,2),math.log(258.414459,2)]
t_107 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(281.000000,2),math.log(307.500000,2),math.log(253.500000,2),math.log(246.375000,2),math.log(290.562500,2),math.log(312.718750,2),math.log(273.968750,2),math.log(287.609375,2),math.log(279.062500,2),math.log(272.753906,2),math.log(247.296875,2),math.log(246.211426,2),math.log(222.998291,2),math.log(255.578491,2),math.log(222.215515,2),math.log(210.651794,2)]
t_108 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(237.000000,2),math.log(241.500000,2),math.log(225.750000,2),math.log(266.875000,2),math.log(281.687500,2),math.log(294.906250,2),math.log(316.156250,2),math.log(287.679688,2),math.log(279.156250,2),math.log(289.664062,2),math.log(244.502930,2),math.log(236.232422,2),math.log(248.057129,2),math.log(284.318848,2),math.log(287.116882,2),math.log(243.546387,2)]
t_109 = [math.log(272.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(266.000000,2),math.log(217.500000,2),math.log(239.250000,2),math.log(220.375000,2),math.log(291.062500,2),math.log(266.593750,2),math.log(253.906250,2),math.log(286.492188,2),math.log(248.347656,2),math.log(260.800781,2),math.log(261.841797,2),math.log(271.484863,2),math.log(274.198486,2),math.log(292.338257,2),math.log(274.677124,2),math.log(221.263397,2)]
t_110 = [math.log(224.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(274.000000,2),math.log(237.000000,2),math.log(231.000000,2),math.log(239.000000,2),math.log(247.750000,2),math.log(269.187500,2),math.log(296.093750,2),math.log(283.406250,2),math.log(259.179688,2),math.log(254.093750,2),math.log(235.988281,2),math.log(265.388672,2),math.log(249.816406,2),math.log(209.471924,2),math.log(205.321289,2),math.log(245.050476,2),math.log(239.164307,2)]
t_111 = [math.log(272.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(214.000000,2),math.log(275.000000,2),math.log(230.000000,2),math.log(206.500000,2),math.log(230.625000,2),math.log(267.625000,2),math.log(291.000000,2),math.log(251.578125,2),math.log(218.062500,2),math.log(216.335938,2),math.log(255.699219,2),math.log(258.548828,2),math.log(229.288574,2),math.log(252.428467,2),math.log(233.131226,2),math.log(234.085449,2),math.log(242.518677,2)]
t_112 = [math.log(256.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(278.000000,2),math.log(287.000000,2),math.log(309.000000,2),math.log(277.000000,2),math.log(235.750000,2),math.log(219.625000,2),math.log(225.406250,2),math.log(231.687500,2),math.log(244.000000,2),math.log(293.492188,2),math.log(271.730469,2),math.log(235.650391,2),math.log(276.337891,2),math.log(269.850342,2),math.log(266.110107,2),math.log(271.678589,2),math.log(250.841675,2)]
t_113 = [math.log(304.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(238.000000,2),math.log(233.000000,2),math.log(241.500000,2),math.log(267.500000,2),math.log(240.375000,2),math.log(265.937500,2),math.log(268.531250,2),math.log(232.734375,2),math.log(258.609375,2),math.log(215.175781,2),math.log(228.025391,2),math.log(244.148438,2),math.log(272.044434,2),math.log(260.563232,2),math.log(288.961182,2),math.log(243.613647,2),math.log(203.430756,2)]
t_114 = [math.log(240.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(224.000000,2),math.log(244.500000,2),math.log(250.750000,2),math.log(251.875000,2),math.log(231.875000,2),math.log(252.375000,2),math.log(268.890625,2),math.log(267.390625,2),math.log(270.097656,2),math.log(288.044922,2),math.log(275.252930,2),math.log(233.833496,2),math.log(235.075195,2),math.log(275.758301,2),math.log(280.865356,2),math.log(249.728760,2)]
t_115 = [math.log(240.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(276.000000,2),math.log(285.000000,2),math.log(294.500000,2),math.log(257.250000,2),math.log(255.500000,2),math.log(257.312500,2),math.log(263.687500,2),math.log(240.421875,2),math.log(243.968750,2),math.log(276.812500,2),math.log(267.998047,2),math.log(284.291992,2),math.log(275.520996,2),math.log(263.857422,2),math.log(264.241333,2),math.log(246.791931,2),math.log(242.151672,2)]
t_116 = [math.log(288.000000,2),math.log(280.000000,2),math.log(296.000000,2),math.log(254.000000,2),math.log(253.000000,2),math.log(260.000000,2),math.log(259.750000,2),math.log(251.500000,2),math.log(269.125000,2),math.log(290.343750,2),math.log(271.515625,2),math.log(237.234375,2),math.log(256.566406,2),math.log(269.398438,2),math.log(251.818359,2),math.log(247.269043,2),math.log(255.187744,2),math.log(275.909546,2),math.log(249.894043,2),math.log(249.761963,2)]
t_117 = [math.log(272.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(258.000000,2),math.log(267.000000,2),math.log(270.750000,2),math.log(270.375000,2),math.log(290.187500,2),math.log(293.843750,2),math.log(264.015625,2),math.log(269.367188,2),math.log(266.113281,2),math.log(254.708984,2),math.log(256.545898,2),math.log(251.812500,2),math.log(225.743652,2),math.log(238.801880,2),math.log(262.459656,2),math.log(292.756989,2)]
t_118 = [math.log(256.000000,2),math.log(256.000000,2),math.log(320.000000,2),math.log(312.000000,2),math.log(303.000000,2),math.log(316.000000,2),math.log(293.000000,2),math.log(268.250000,2),math.log(250.625000,2),math.log(255.125000,2),math.log(263.328125,2),math.log(244.789062,2),math.log(244.683594,2),math.log(280.882812,2),math.log(275.396484,2),math.log(264.367676,2),math.log(225.520020,2),math.log(240.127563,2),math.log(232.591736,2),math.log(218.968445,2)]
t_119 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(328.750000,2),math.log(302.375000,2),math.log(257.000000,2),math.log(259.937500,2),math.log(250.625000,2),math.log(244.632812,2),math.log(215.867188,2),math.log(248.515625,2),math.log(239.215820,2),math.log(205.759277,2),math.log(240.219482,2),math.log(253.542969,2),math.log(258.825378,2),math.log(247.788422,2)]
t_120 = [math.log(288.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(234.000000,2),math.log(274.000000,2),math.log(254.000000,2),math.log(227.000000,2),math.log(236.375000,2),math.log(239.062500,2),math.log(245.093750,2),math.log(255.828125,2),math.log(238.898438,2),math.log(224.476562,2),math.log(240.246094,2),math.log(253.095703,2),math.log(249.619629,2),math.log(238.934570,2),math.log(246.518677,2),math.log(284.256653,2),math.log(264.600098,2)]
t_121 = [math.log(224.000000,2),math.log(208.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(250.000000,2),math.log(215.500000,2),math.log(264.500000,2),math.log(250.875000,2),math.log(251.125000,2),math.log(241.875000,2),math.log(241.343750,2),math.log(269.398438,2),math.log(269.402344,2),math.log(278.845703,2),math.log(270.887695,2),math.log(268.291016,2),math.log(236.113281,2),math.log(230.322266,2),math.log(263.352905,2),math.log(245.045105,2)]
t_122 = [math.log(272.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(234.000000,2),math.log(257.000000,2),math.log(288.500000,2),math.log(251.500000,2),math.log(264.750000,2),math.log(258.312500,2),math.log(265.031250,2),math.log(241.140625,2),math.log(250.359375,2),math.log(241.347656,2),math.log(259.480469,2),math.log(237.871094,2),math.log(221.065918,2),math.log(227.078613,2),math.log(251.402344,2),math.log(295.246399,2),math.log(324.988892,2)]
t_123 = [math.log(240.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(218.000000,2),math.log(276.000000,2),math.log(257.500000,2),math.log(239.500000,2),math.log(236.125000,2),math.log(244.125000,2),math.log(227.343750,2),math.log(220.031250,2),math.log(214.265625,2),math.log(220.925781,2),math.log(253.626953,2),math.log(242.359375,2),math.log(264.492676,2),math.log(246.483887,2),math.log(252.696533,2),math.log(280.026367,2),math.log(276.162811,2)]
t_124 = [math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(249.000000,2),math.log(237.000000,2),math.log(257.500000,2),math.log(269.500000,2),math.log(252.312500,2),math.log(241.000000,2),math.log(224.203125,2),math.log(256.359375,2),math.log(258.480469,2),math.log(281.681641,2),math.log(257.852539,2),math.log(259.252930,2),math.log(272.744873,2),math.log(245.470947,2),math.log(254.895081,2),math.log(255.375977,2)]
t_125 = [math.log(256.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(296.000000,2),math.log(260.000000,2),math.log(288.250000,2),math.log(280.625000,2),math.log(264.375000,2),math.log(245.750000,2),math.log(239.093750,2),math.log(267.062500,2),math.log(248.511719,2),math.log(201.957031,2),math.log(225.936523,2),math.log(236.173340,2),math.log(235.027100,2),math.log(258.452026,2),math.log(258.979248,2),math.log(224.418457,2)]
t_126 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(262.000000,2),math.log(276.000000,2),math.log(272.250000,2),math.log(279.000000,2),math.log(273.312500,2),math.log(271.562500,2),math.log(244.093750,2),math.log(246.710938,2),math.log(267.804688,2),math.log(236.738281,2),math.log(269.119141,2),math.log(271.524902,2),math.log(252.046143,2),math.log(274.963623,2),math.log(304.477112,2),math.log(310.632050,2)]
t_127 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(290.000000,2),math.log(261.000000,2),math.log(284.000000,2),math.log(277.750000,2),math.log(246.875000,2),math.log(238.250000,2),math.log(241.656250,2),math.log(267.734375,2),math.log(259.468750,2),math.log(254.617188,2),math.log(225.033203,2),math.log(224.809570,2),math.log(215.816406,2),math.log(229.699219,2),math.log(213.147827,2),math.log(236.818909,2),math.log(254.504059,2)]
t_128 = [math.log(256.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(231.000000,2),math.log(257.500000,2),math.log(252.000000,2),math.log(268.500000,2),math.log(282.250000,2),math.log(280.125000,2),math.log(290.265625,2),math.log(303.046875,2),math.log(290.058594,2),math.log(265.539062,2),math.log(246.659180,2),math.log(227.753906,2),math.log(255.771729,2),math.log(245.601318,2),math.log(245.512024,2),math.log(202.810486,2)]
t_129 = [math.log(224.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(232.000000,2),math.log(257.000000,2),math.log(311.000000,2),math.log(225.000000,2),math.log(201.875000,2),math.log(208.312500,2),math.log(227.156250,2),math.log(235.796875,2),math.log(266.320312,2),math.log(269.855469,2),math.log(251.804688,2),math.log(279.937500,2),math.log(289.683594,2),math.log(247.930420,2),math.log(277.080811,2),math.log(272.941528,2),math.log(274.387238,2)]
t_130 = [math.log(272.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(218.000000,2),math.log(255.000000,2),math.log(246.000000,2),math.log(249.750000,2),math.log(275.125000,2),math.log(300.062500,2),math.log(257.843750,2),math.log(275.984375,2),math.log(248.273438,2),math.log(251.851562,2),math.log(279.634766,2),math.log(249.728516,2),math.log(260.669434,2),math.log(246.420654,2),math.log(246.902344,2),math.log(225.136292,2),math.log(236.225281,2)]
t_131 = [math.log(256.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(255.500000,2),math.log(231.000000,2),math.log(270.125000,2),math.log(229.562500,2),math.log(261.218750,2),math.log(260.718750,2),math.log(306.226562,2),math.log(294.605469,2),math.log(267.521484,2),math.log(292.516602,2),math.log(292.213379,2),math.log(300.027344,2),math.log(276.764282,2),math.log(253.661743,2),math.log(253.005920,2)]
t_132 = [math.log(240.000000,2),math.log(224.000000,2),math.log(240.000000,2),math.log(282.000000,2),math.log(255.000000,2),math.log(311.000000,2),math.log(274.000000,2),math.log(266.750000,2),math.log(278.250000,2),math.log(271.625000,2),math.log(261.046875,2),math.log(254.132812,2),math.log(279.535156,2),math.log(282.544922,2),math.log(253.260742,2),math.log(268.635742,2),math.log(256.052979,2),math.log(265.306885,2),math.log(270.429199,2),math.log(289.249084,2)]
t_133 = [math.log(272.000000,2),math.log(256.000000,2),math.log(216.000000,2),math.log(264.000000,2),math.log(269.000000,2),math.log(271.500000,2),math.log(235.500000,2),math.log(268.875000,2),math.log(255.312500,2),math.log(268.250000,2),math.log(257.453125,2),math.log(233.562500,2),math.log(233.476562,2),math.log(266.691406,2),math.log(245.606445,2),math.log(233.732910,2),math.log(246.478760,2),math.log(239.109863,2),math.log(226.868103,2),math.log(207.975830,2)]
t_134 = [math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(275.000000,2),math.log(261.000000,2),math.log(233.250000,2),math.log(215.750000,2),math.log(290.687500,2),math.log(233.906250,2),math.log(241.656250,2),math.log(219.148438,2),math.log(229.246094,2),math.log(202.074219,2),math.log(229.023438,2),math.log(275.940430,2),math.log(255.617676,2),math.log(276.400146,2),math.log(269.612488,2),math.log(251.833405,2)]
t_135 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(273.000000,2),math.log(259.000000,2),math.log(263.500000,2),math.log(238.750000,2),math.log(253.000000,2),math.log(266.687500,2),math.log(272.468750,2),math.log(276.085938,2),math.log(271.257812,2),math.log(237.332031,2),math.log(259.562500,2),math.log(241.667480,2),math.log(292.072754,2),math.log(296.586060,2),math.log(297.489014,2),math.log(282.139313,2)]
t_136 = [math.log(224.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(234.000000,2),math.log(229.000000,2),math.log(253.000000,2),math.log(234.500000,2),math.log(223.500000,2),math.log(252.187500,2),math.log(256.250000,2),math.log(240.062500,2),math.log(249.835938,2),math.log(283.679688,2),math.log(254.044922,2),math.log(242.489258,2),math.log(248.613281,2),math.log(237.134033,2),math.log(243.656860,2),math.log(230.191284,2),math.log(244.363678,2)]
t_137 = [math.log(240.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(240.000000,2),math.log(236.500000,2),math.log(248.750000,2),math.log(249.250000,2),math.log(281.062500,2),math.log(278.562500,2),math.log(272.906250,2),math.log(250.617188,2),math.log(276.164062,2),math.log(312.462891,2),math.log(277.334961,2),math.log(263.652832,2),math.log(270.200195,2),math.log(266.287109,2),math.log(249.803589,2),math.log(226.196259,2)]
t_138 = [math.log(304.000000,2),math.log(312.000000,2),math.log(292.000000,2),math.log(238.000000,2),math.log(222.000000,2),math.log(251.500000,2),math.log(244.500000,2),math.log(249.250000,2),math.log(268.250000,2),math.log(284.031250,2),math.log(288.593750,2),math.log(292.601562,2),math.log(266.410156,2),math.log(261.378906,2),math.log(254.827148,2),math.log(298.318359,2),math.log(311.534424,2),math.log(277.937744,2),math.log(264.477112,2),math.log(257.416565,2)]
t_139 = [math.log(288.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(218.000000,2),math.log(242.000000,2),math.log(230.000000,2),math.log(220.250000,2),math.log(238.375000,2),math.log(235.250000,2),math.log(247.656250,2),math.log(247.937500,2),math.log(268.296875,2),math.log(269.804688,2),math.log(257.353516,2),math.log(257.984375,2),math.log(254.717773,2),math.log(276.795654,2),math.log(259.527710,2),math.log(255.121033,2),math.log(260.972107,2)]
t_140 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(280.000000,2),math.log(269.000000,2),math.log(267.750000,2),math.log(253.875000,2),math.log(241.875000,2),math.log(253.968750,2),math.log(248.687500,2),math.log(235.281250,2),math.log(240.726562,2),math.log(252.474609,2),math.log(244.065430,2),math.log(245.489746,2),math.log(228.378662,2),math.log(265.966919,2),math.log(259.693298,2),math.log(275.936920,2)]
t_141 = [math.log(288.000000,2),math.log(272.000000,2),math.log(284.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(257.250000,2),math.log(262.625000,2),math.log(259.000000,2),math.log(277.218750,2),math.log(275.859375,2),math.log(258.117188,2),math.log(256.050781,2),math.log(269.019531,2),math.log(303.819336,2),math.log(288.717773,2),math.log(255.346924,2),math.log(247.243896,2),math.log(263.488098,2),math.log(257.715027,2)]
t_142 = [math.log(256.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(290.000000,2),math.log(275.000000,2),math.log(276.500000,2),math.log(259.000000,2),math.log(269.875000,2),math.log(256.937500,2),math.log(259.875000,2),math.log(231.250000,2),math.log(218.781250,2),math.log(224.910156,2),math.log(246.111328,2),math.log(253.038086,2),math.log(248.171875,2),math.log(246.346924,2),math.log(267.413330,2),math.log(283.913696,2),math.log(274.174286,2)]
t_143 = [math.log(288.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(283.000000,2),math.log(249.000000,2),math.log(237.250000,2),math.log(262.250000,2),math.log(260.187500,2),math.log(267.343750,2),math.log(244.046875,2),math.log(232.414062,2),math.log(249.156250,2),math.log(276.238281,2),math.log(226.374023,2),math.log(195.875488,2),math.log(233.234619,2),math.log(240.881226,2),math.log(257.275024,2),math.log(253.051270,2)]
t_144 = [math.log(240.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(290.000000,2),math.log(284.000000,2),math.log(274.500000,2),math.log(307.000000,2),math.log(316.750000,2),math.log(290.375000,2),math.log(283.031250,2),math.log(296.328125,2),math.log(276.015625,2),math.log(266.113281,2),math.log(254.015625,2),math.log(264.156250,2),math.log(260.661621,2),math.log(278.324463,2),math.log(280.465332,2),math.log(231.440918,2),math.log(221.675873,2)]
t_145 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(220.000000,2),math.log(280.000000,2),math.log(279.000000,2),math.log(301.250000,2),math.log(312.500000,2),math.log(288.687500,2),math.log(271.000000,2),math.log(262.187500,2),math.log(277.796875,2),math.log(265.609375,2),math.log(298.361328,2),math.log(253.880859,2),math.log(244.394531,2),math.log(254.685547,2),math.log(245.858521,2),math.log(245.449768,2),math.log(246.298340,2)]
t_146 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(238.000000,2),math.log(269.000000,2),math.log(249.000000,2),math.log(279.375000,2),math.log(265.937500,2),math.log(274.750000,2),math.log(250.671875,2),math.log(249.539062,2),math.log(247.832031,2),math.log(298.667969,2),math.log(299.270508,2),math.log(248.851562,2),math.log(258.011719,2),math.log(229.974121,2),math.log(215.948730,2),math.log(249.417419,2)]
t_147 = [math.log(240.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(262.000000,2),math.log(252.000000,2),math.log(290.000000,2),math.log(273.250000,2),math.log(280.500000,2),math.log(255.500000,2),math.log(258.875000,2),math.log(235.750000,2),math.log(237.617188,2),math.log(241.652344,2),math.log(237.505859,2),math.log(231.926758,2),math.log(261.063965,2),math.log(236.065918,2),math.log(256.109009,2),math.log(239.824280,2),math.log(245.624115,2)]
t_148 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(249.000000,2),math.log(238.500000,2),math.log(251.750000,2),math.log(224.375000,2),math.log(230.187500,2),math.log(259.781250,2),math.log(254.921875,2),math.log(211.109375,2),math.log(198.261719,2),math.log(202.609375,2),math.log(223.572266,2),math.log(216.929199,2),math.log(259.872314,2),math.log(280.980713,2),math.log(236.240173,2),math.log(247.616974,2)]
t_149 = [math.log(256.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(210.000000,2),math.log(235.000000,2),math.log(269.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(234.562500,2),math.log(276.718750,2),math.log(278.093750,2),math.log(241.781250,2),math.log(251.429688,2),math.log(294.396484,2),math.log(268.162109,2),math.log(256.901367,2),math.log(270.855225,2),math.log(306.108521,2),math.log(270.452881,2),math.log(260.702362,2)]
t_150 = [math.log(272.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(274.000000,2),math.log(293.000000,2),math.log(232.000000,2),math.log(251.500000,2),math.log(267.750000,2),math.log(246.875000,2),math.log(238.656250,2),math.log(248.031250,2),math.log(255.289062,2),math.log(269.605469,2),math.log(308.212891,2),math.log(257.949219,2),math.log(264.471680,2),math.log(248.442627,2),math.log(251.501953,2),math.log(244.044189,2),math.log(262.778015,2)]
t_151 = [math.log(240.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(262.000000,2),math.log(238.000000,2),math.log(246.500000,2),math.log(205.250000,2),math.log(252.250000,2),math.log(255.812500,2),math.log(313.437500,2),math.log(274.640625,2),math.log(288.359375,2),math.log(293.726562,2),math.log(261.183594,2),math.log(234.629883,2),math.log(244.350098,2),math.log(286.679932,2),math.log(280.179810,2),math.log(290.898987,2),math.log(285.748535,2)]
t_152 = [math.log(224.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(268.000000,2),math.log(233.000000,2),math.log(234.500000,2),math.log(266.000000,2),math.log(257.875000,2),math.log(290.187500,2),math.log(270.125000,2),math.log(278.000000,2),math.log(252.898438,2),math.log(221.695312,2),math.log(263.361328,2),math.log(267.821289,2),math.log(281.188965,2),math.log(252.021240,2),math.log(238.725098,2),math.log(269.190063,2),math.log(240.693573,2)]
t_153 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(257.000000,2),math.log(258.000000,2),math.log(237.250000,2),math.log(240.000000,2),math.log(239.187500,2),math.log(228.187500,2),math.log(242.765625,2),math.log(266.867188,2),math.log(239.824219,2),math.log(242.779297,2),math.log(260.296875,2),math.log(247.411621,2),math.log(252.250732,2),math.log(254.289551,2),math.log(295.927368,2),math.log(280.297211,2)]
t_154 = [math.log(240.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(260.000000,2),math.log(287.500000,2),math.log(261.000000,2),math.log(247.250000,2),math.log(227.437500,2),math.log(210.812500,2),math.log(190.375000,2),math.log(214.984375,2),math.log(211.500000,2),math.log(215.833984,2),math.log(247.853516,2),math.log(259.062988,2),math.log(277.132324,2),math.log(286.769043,2),math.log(284.751343,2),math.log(263.749176,2)]
t_155 = [math.log(256.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(282.000000,2),math.log(289.000000,2),math.log(297.000000,2),math.log(275.500000,2),math.log(268.500000,2),math.log(251.937500,2),math.log(232.593750,2),math.log(251.156250,2),math.log(213.828125,2),math.log(270.707031,2),math.log(288.144531,2),math.log(254.103516,2),math.log(261.469238,2),math.log(240.224121,2),math.log(294.430176,2),math.log(247.050354,2),math.log(241.757843,2)]
t_156 = [math.log(224.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(257.000000,2),math.log(237.500000,2),math.log(247.500000,2),math.log(244.000000,2),math.log(255.062500,2),math.log(243.687500,2),math.log(225.500000,2),math.log(226.039062,2),math.log(245.328125,2),math.log(244.375000,2),math.log(248.200195,2),math.log(209.378418,2),math.log(263.618652,2),math.log(286.062012,2),math.log(282.175842,2),math.log(280.458252,2)]
t_157 = [math.log(240.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(269.000000,2),math.log(297.000000,2),math.log(255.250000,2),math.log(237.875000,2),math.log(260.250000,2),math.log(275.406250,2),math.log(252.187500,2),math.log(247.007812,2),math.log(263.789062,2),math.log(224.406250,2),math.log(224.216797,2),math.log(245.575684,2),math.log(261.741211,2),math.log(253.702393,2),math.log(301.989319,2),math.log(229.433746,2)]
t_158 = [math.log(304.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(274.000000,2),math.log(263.000000,2),math.log(254.000000,2),math.log(252.250000,2),math.log(269.937500,2),math.log(262.468750,2),math.log(227.390625,2),math.log(270.906250,2),math.log(230.777344,2),math.log(219.087891,2),math.log(274.020508,2),math.log(298.744629,2),math.log(263.613525,2),math.log(223.474365,2),math.log(219.131226,2),math.log(222.693665,2)]
t_159 = [math.log(256.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(260.000000,2),math.log(235.500000,2),math.log(239.000000,2),math.log(230.625000,2),math.log(253.062500,2),math.log(248.812500,2),math.log(233.250000,2),math.log(265.851562,2),math.log(275.937500,2),math.log(275.740234,2),math.log(290.132812,2),math.log(284.962891,2),math.log(297.778809,2),math.log(289.887451,2),math.log(274.236206,2),math.log(286.563354,2)]
t_160 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(224.000000,2),math.log(200.000000,2),math.log(259.000000,2),math.log(284.500000,2),math.log(271.125000,2),math.log(238.187500,2),math.log(232.093750,2),math.log(247.156250,2),math.log(269.312500,2),math.log(271.957031,2),math.log(257.935547,2),math.log(259.750977,2),math.log(250.359375,2),math.log(260.339355,2),math.log(257.193115,2),math.log(259.616333,2),math.log(244.448547,2)]
t_161 = [math.log(256.000000,2),math.log(224.000000,2),math.log(204.000000,2),math.log(236.000000,2),math.log(278.000000,2),math.log(284.000000,2),math.log(280.500000,2),math.log(263.000000,2),math.log(257.312500,2),math.log(247.406250,2),math.log(242.187500,2),math.log(258.445312,2),math.log(278.343750,2),math.log(259.468750,2),math.log(274.759766,2),math.log(301.955566,2),math.log(244.079590,2),math.log(238.624878,2),math.log(286.487244,2),math.log(281.273834,2)]
t_162 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(245.000000,2),math.log(239.000000,2),math.log(275.000000,2),math.log(265.000000,2),math.log(251.812500,2),math.log(249.687500,2),math.log(264.437500,2),math.log(322.023438,2),math.log(310.109375,2),math.log(290.441406,2),math.log(282.662109,2),math.log(282.819336,2),math.log(259.301270,2),math.log(273.941040,2),math.log(252.836060,2),math.log(264.516541,2)]
t_163 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(272.000000,2),math.log(253.500000,2),math.log(250.000000,2),math.log(233.125000,2),math.log(234.187500,2),math.log(228.062500,2),math.log(252.437500,2),math.log(243.656250,2),math.log(273.050781,2),math.log(267.632812,2),math.log(252.504883,2),math.log(277.765625,2),math.log(242.492676,2),math.log(233.644043,2),math.log(240.742493,2),math.log(261.601593,2)]
t_164 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(290.000000,2),math.log(260.000000,2),math.log(224.500000,2),math.log(229.500000,2),math.log(246.500000,2),math.log(239.750000,2),math.log(251.062500,2),math.log(255.718750,2),math.log(258.359375,2),math.log(272.375000,2),math.log(298.312500,2),math.log(292.859375,2),math.log(290.938965,2),math.log(282.215576,2),math.log(281.535278,2),math.log(281.997131,2),math.log(257.347137,2)]
t_165 = [math.log(224.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(235.000000,2),math.log(249.500000,2),math.log(253.250000,2),math.log(254.000000,2),math.log(239.312500,2),math.log(215.593750,2),math.log(268.796875,2),math.log(265.250000,2),math.log(270.527344,2),math.log(276.794922,2),math.log(260.651367,2),math.log(275.012207,2),math.log(231.071533,2),math.log(263.552246,2),math.log(253.959106,2),math.log(257.862640,2)]
t_166 = [math.log(224.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(286.000000,2),math.log(304.750000,2),math.log(256.125000,2),math.log(267.437500,2),math.log(239.125000,2),math.log(248.531250,2),math.log(232.164062,2),math.log(234.019531,2),math.log(222.542969,2),math.log(218.390625,2),math.log(224.061523,2),math.log(232.553467,2),math.log(217.165405,2),math.log(263.698547,2),math.log(252.853363,2)]
t_167 = [math.log(272.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(230.000000,2),math.log(213.000000,2),math.log(255.000000,2),math.log(250.500000,2),math.log(266.500000,2),math.log(253.000000,2),math.log(236.406250,2),math.log(265.296875,2),math.log(282.445312,2),math.log(262.589844,2),math.log(274.083984,2),math.log(242.768555,2),math.log(247.709473,2),math.log(275.593262,2),math.log(261.071777,2),math.log(284.739502,2),math.log(268.248810,2)]
t_168 = [math.log(272.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(266.000000,2),math.log(247.000000,2),math.log(264.500000,2),math.log(292.250000,2),math.log(266.125000,2),math.log(237.500000,2),math.log(305.375000,2),math.log(291.703125,2),math.log(245.468750,2),math.log(252.093750,2),math.log(259.085938,2),math.log(280.902344,2),math.log(267.863770,2),math.log(253.297852,2),math.log(259.282715,2),math.log(244.879883,2),math.log(277.920013,2)]
t_169 = [math.log(256.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(251.000000,2),math.log(251.000000,2),math.log(240.000000,2),math.log(259.125000,2),math.log(271.062500,2),math.log(225.500000,2),math.log(229.531250,2),math.log(256.875000,2),math.log(235.414062,2),math.log(220.685547,2),math.log(260.654297,2),math.log(317.009766,2),math.log(303.527588,2),math.log(278.295044,2),math.log(241.017883,2),math.log(211.650574,2)]
t_170 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(284.000000,2),math.log(270.000000,2),math.log(234.500000,2),math.log(258.000000,2),math.log(267.375000,2),math.log(236.125000,2),math.log(237.000000,2),math.log(248.937500,2),math.log(243.007812,2),math.log(246.570312,2),math.log(255.119141,2),math.log(245.671875,2),math.log(207.923828,2),math.log(229.129883,2),math.log(233.833862,2),math.log(235.950378,2),math.log(262.235504,2)]
t_171 = [math.log(224.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(230.000000,2),math.log(262.000000,2),math.log(274.500000,2),math.log(269.000000,2),math.log(275.000000,2),math.log(265.687500,2),math.log(213.093750,2),math.log(233.640625,2),math.log(219.179688,2),math.log(238.375000,2),math.log(275.937500,2),math.log(265.440430,2),math.log(244.191895,2),math.log(232.087158,2),math.log(235.191162,2),math.log(259.858459,2),math.log(243.704895,2)]
t_172 = [math.log(224.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(268.000000,2),math.log(266.000000,2),math.log(246.500000,2),math.log(231.250000,2),math.log(294.250000,2),math.log(267.656250,2),math.log(278.375000,2),math.log(247.710938,2),math.log(251.355469,2),math.log(257.177734,2),math.log(248.873047,2),math.log(271.270020,2),math.log(253.110596,2),math.log(250.106079,2),math.log(261.705383,2),math.log(248.559479,2)]
t_173 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(224.000000,2),math.log(246.500000,2),math.log(262.500000,2),math.log(271.000000,2),math.log(266.312500,2),math.log(254.218750,2),math.log(283.343750,2),math.log(257.132812,2),math.log(235.628906,2),math.log(249.388672,2),math.log(244.474609,2),math.log(258.146484,2),math.log(264.658203,2),math.log(262.014282,2),math.log(277.725647,2),math.log(240.782532,2)]
t_174 = [math.log(272.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(234.000000,2),math.log(251.000000,2),math.log(242.500000,2),math.log(230.000000,2),math.log(238.750000,2),math.log(246.812500,2),math.log(264.625000,2),math.log(260.000000,2),math.log(282.203125,2),math.log(292.671875,2),math.log(282.873047,2),math.log(230.389648,2),math.log(217.659668,2),math.log(257.173584,2),math.log(260.662720,2),math.log(270.433594,2),math.log(260.957916,2)]
t_175 = [math.log(272.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(218.000000,2),math.log(261.000000,2),math.log(241.000000,2),math.log(238.500000,2),math.log(269.500000,2),math.log(263.312500,2),math.log(248.031250,2),math.log(230.875000,2),math.log(244.195312,2),math.log(248.289062,2),math.log(237.154297,2),math.log(272.885742,2),math.log(275.204102,2),math.log(278.578369,2),math.log(275.591431,2),math.log(262.446228,2),math.log(256.785583,2)]
t_176 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(299.000000,2),math.log(285.500000,2),math.log(252.500000,2),math.log(223.875000,2),math.log(259.187500,2),math.log(237.875000,2),math.log(252.984375,2),math.log(211.406250,2),math.log(249.222656,2),math.log(237.839844,2),math.log(251.402344,2),math.log(250.380859,2),math.log(238.995117,2),math.log(220.894531,2),math.log(242.383667,2),math.log(278.834869,2)]
t_177 = [math.log(256.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(282.000000,2),math.log(266.000000,2),math.log(273.000000,2),math.log(285.250000,2),math.log(268.875000,2),math.log(269.437500,2),math.log(239.906250,2),math.log(241.656250,2),math.log(234.257812,2),math.log(221.617188,2),math.log(212.351562,2),math.log(238.648438,2),math.log(268.811035,2),math.log(256.473145,2),math.log(274.207764,2),math.log(229.819946,2),math.log(240.301575,2)]
t_178 = [math.log(288.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(244.500000,2),math.log(281.750000,2),math.log(232.000000,2),math.log(258.687500,2),math.log(247.468750,2),math.log(260.031250,2),math.log(285.257812,2),math.log(279.777344,2),math.log(237.359375,2),math.log(201.318359,2),math.log(241.135254,2),math.log(250.760498,2),math.log(273.225952,2),math.log(264.209595,2),math.log(276.180817,2)]
t_179 = [math.log(256.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(260.000000,2),math.log(279.125000,2),math.log(310.625000,2),math.log(222.875000,2),math.log(268.953125,2),math.log(233.835938,2),math.log(227.054688,2),math.log(222.132812,2),math.log(239.912109,2),math.log(230.552246,2),math.log(273.302246,2),math.log(271.948730,2),math.log(216.093872,2),math.log(238.165100,2)]
t_180 = [math.log(256.000000,2),math.log(208.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(245.000000,2),math.log(237.000000,2),math.log(237.500000,2),math.log(267.500000,2),math.log(247.250000,2),math.log(254.875000,2),math.log(277.609375,2),math.log(267.367188,2),math.log(263.312500,2),math.log(276.576172,2),math.log(231.971680,2),math.log(242.605469,2),math.log(263.215332,2),math.log(263.978027,2),math.log(255.390503,2),math.log(236.045013,2)]
t_181 = [math.log(224.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(295.500000,2),math.log(268.125000,2),math.log(249.812500,2),math.log(250.406250,2),math.log(234.765625,2),math.log(268.546875,2),math.log(251.390625,2),math.log(256.953125,2),math.log(256.501953,2),math.log(272.475586,2),math.log(244.570068,2),math.log(266.502808,2),math.log(260.575012,2),math.log(275.707550,2)]
t_182 = [math.log(272.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(259.500000,2),math.log(231.750000,2),math.log(247.375000,2),math.log(277.000000,2),math.log(245.375000,2),math.log(259.281250,2),math.log(282.796875,2),math.log(244.800781,2),math.log(257.376953,2),math.log(277.612305,2),math.log(247.040039,2),math.log(235.554443,2),math.log(238.483643,2),math.log(224.314636,2),math.log(213.086823,2)]
t_183 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(290.000000,2),math.log(302.000000,2),math.log(299.000000,2),math.log(278.000000,2),math.log(271.500000,2),math.log(248.125000,2),math.log(291.125000,2),math.log(290.875000,2),math.log(279.640625,2),math.log(262.902344,2),math.log(265.242188,2),math.log(288.705078,2),math.log(245.641113,2),math.log(266.594482,2),math.log(253.272827,2),math.log(237.190796,2),math.log(308.836853,2)]
t_184 = [math.log(240.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(286.000000,2),math.log(280.000000,2),math.log(258.000000,2),math.log(248.000000,2),math.log(228.125000,2),math.log(249.000000,2),math.log(237.937500,2),math.log(254.500000,2),math.log(259.343750,2),math.log(258.160156,2),math.log(245.802734,2),math.log(284.362305,2),math.log(254.345215,2),math.log(251.996094,2),math.log(258.656128,2),math.log(268.392700,2),math.log(259.703156,2)]
t_185 = [math.log(256.000000,2),math.log(232.000000,2),math.log(200.000000,2),math.log(234.000000,2),math.log(228.000000,2),math.log(236.000000,2),math.log(246.500000,2),math.log(259.125000,2),math.log(290.937500,2),math.log(266.312500,2),math.log(306.265625,2),math.log(291.406250,2),math.log(263.582031,2),math.log(244.986328,2),math.log(228.962891,2),math.log(266.741699,2),math.log(245.220215,2),math.log(228.009766,2),math.log(268.602478,2),math.log(258.032898,2)]
t_186 = [math.log(288.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(298.000000,2),math.log(281.000000,2),math.log(293.500000,2),math.log(256.250000,2),math.log(240.375000,2),math.log(240.312500,2),math.log(239.968750,2),math.log(219.171875,2),math.log(245.195312,2),math.log(250.476562,2),math.log(246.082031,2),math.log(277.841797,2),math.log(255.665527,2),math.log(251.252441,2),math.log(250.876953,2),math.log(267.995972,2),math.log(276.802673,2)]
t_187 = [math.log(272.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(226.000000,2),math.log(271.000000,2),math.log(254.500000,2),math.log(207.000000,2),math.log(214.625000,2),math.log(239.125000,2),math.log(267.062500,2),math.log(257.156250,2),math.log(272.148438,2),math.log(289.167969,2),math.log(237.968750,2),math.log(241.241211,2),math.log(249.119629,2),math.log(222.280518,2),math.log(217.441772,2),math.log(233.030945,2),math.log(236.217590,2)]
t_188 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(268.000000,2),math.log(245.875000,2),math.log(239.750000,2),math.log(232.406250,2),math.log(258.375000,2),math.log(256.210938,2),math.log(245.023438,2),math.log(250.412109,2),math.log(257.789062,2),math.log(252.408203,2),math.log(286.263916,2),math.log(267.619751,2),math.log(251.260559,2),math.log(266.858582,2)]
t_189 = [math.log(224.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(270.000000,2),math.log(249.000000,2),math.log(250.000000,2),math.log(239.000000,2),math.log(236.750000,2),math.log(227.687500,2),math.log(237.593750,2),math.log(233.562500,2),math.log(253.187500,2),math.log(241.488281,2),math.log(252.302734,2),math.log(237.125000,2),math.log(271.100586,2),math.log(280.487305,2),math.log(279.103394,2),math.log(260.538940,2),math.log(262.222656,2)]
t_190 = [math.log(304.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(221.000000,2),math.log(241.000000,2),math.log(213.750000,2),math.log(237.375000,2),math.log(234.250000,2),math.log(254.875000,2),math.log(226.390625,2),math.log(198.117188,2),math.log(224.378906,2),math.log(240.427734,2),math.log(226.541016,2),math.log(229.381348,2),math.log(223.182617,2),math.log(236.016602,2),math.log(254.385010,2),math.log(229.918793,2)]
t_191 = [math.log(224.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(257.000000,2),math.log(242.000000,2),math.log(277.500000,2),math.log(282.875000,2),math.log(262.750000,2),math.log(311.531250,2),math.log(282.546875,2),math.log(286.921875,2),math.log(292.695312,2),math.log(324.695312,2),math.log(248.820312,2),math.log(296.606445,2),math.log(273.800537,2),math.log(266.161621,2),math.log(251.225586,2),math.log(252.153534,2)]
t_192 = [math.log(240.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(228.000000,2),math.log(225.000000,2),math.log(211.500000,2),math.log(244.250000,2),math.log(260.250000,2),math.log(262.062500,2),math.log(244.062500,2),math.log(256.531250,2),math.log(260.750000,2),math.log(259.503906,2),math.log(250.955078,2),math.log(262.395508,2),math.log(279.201172,2),math.log(278.675781,2),math.log(271.221924,2),math.log(257.929260,2),math.log(237.938568,2)]
t_193 = [math.log(224.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(246.000000,2),math.log(257.000000,2),math.log(271.000000,2),math.log(230.000000,2),math.log(266.250000,2),math.log(236.750000,2),math.log(290.000000,2),math.log(259.390625,2),math.log(260.882812,2),math.log(261.519531,2),math.log(296.769531,2),math.log(252.634766,2),math.log(303.505371,2),math.log(312.030762,2),math.log(289.644287,2),math.log(256.149353,2),math.log(264.294189,2)]
t_194 = [math.log(240.000000,2),math.log(232.000000,2),math.log(200.000000,2),math.log(214.000000,2),math.log(255.000000,2),math.log(294.000000,2),math.log(284.500000,2),math.log(235.625000,2),math.log(271.437500,2),math.log(228.625000,2),math.log(218.531250,2),math.log(249.515625,2),math.log(256.085938,2),math.log(270.537109,2),math.log(285.580078,2),math.log(264.208008,2),math.log(273.029785,2),math.log(269.526611,2),math.log(220.482849,2),math.log(248.096161,2)]
t_195 = [math.log(224.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(271.000000,2),math.log(252.500000,2),math.log(260.000000,2),math.log(218.250000,2),math.log(256.000000,2),math.log(273.468750,2),math.log(272.656250,2),math.log(278.351562,2),math.log(282.183594,2),math.log(280.179688,2),math.log(246.378906,2),math.log(227.440918,2),math.log(228.386230,2),math.log(254.561646,2),math.log(251.227722,2),math.log(239.933563,2)]
t_196 = [math.log(272.000000,2),math.log(248.000000,2),math.log(292.000000,2),math.log(254.000000,2),math.log(248.000000,2),math.log(270.500000,2),math.log(248.250000,2),math.log(285.500000,2),math.log(271.437500,2),math.log(258.375000,2),math.log(283.640625,2),math.log(284.343750,2),math.log(279.621094,2),math.log(271.716797,2),math.log(263.724609,2),math.log(287.947754,2),math.log(254.853760,2),math.log(253.668945,2),math.log(235.000244,2),math.log(225.149139,2)]
t_197 = [math.log(256.000000,2),math.log(312.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(255.000000,2),math.log(270.500000,2),math.log(262.500000,2),math.log(271.250000,2),math.log(293.562500,2),math.log(279.718750,2),math.log(247.218750,2),math.log(254.398438,2),math.log(283.851562,2),math.log(263.177734,2),math.log(292.675781,2),math.log(287.950684,2),math.log(255.521729,2),math.log(291.967529,2),math.log(297.329712,2),math.log(297.970551,2)]
t_198 = [math.log(288.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(283.000000,2),math.log(309.000000,2),math.log(265.500000,2),math.log(241.000000,2),math.log(244.750000,2),math.log(230.437500,2),math.log(262.671875,2),math.log(220.718750,2),math.log(235.843750,2),math.log(247.025391,2),math.log(243.109375,2),math.log(226.768066,2),math.log(221.037842,2),math.log(243.060303,2),math.log(239.548523,2),math.log(240.747589,2)]
t_199 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(270.500000,2),math.log(241.500000,2),math.log(223.625000,2),math.log(265.437500,2),math.log(250.562500,2),math.log(242.421875,2),math.log(238.664062,2),math.log(225.285156,2),math.log(230.093750,2),math.log(261.304688,2),math.log(249.823730,2),math.log(251.825439,2),math.log(252.378662,2),math.log(237.204468,2),math.log(216.039673,2)]
t_200 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(256.000000,2),math.log(243.500000,2),math.log(237.250000,2),math.log(260.000000,2),math.log(267.437500,2),math.log(250.718750,2),math.log(258.390625,2),math.log(248.851562,2),math.log(259.644531,2),math.log(237.992188,2),math.log(246.536133,2),math.log(207.364746,2),math.log(241.855225,2),math.log(250.851440,2),math.log(247.391785,2),math.log(270.050995,2)]
t_201 = [math.log(240.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(286.000000,2),math.log(248.000000,2),math.log(230.000000,2),math.log(250.250000,2),math.log(236.250000,2),math.log(215.312500,2),math.log(246.750000,2),math.log(214.906250,2),math.log(244.437500,2),math.log(223.000000,2),math.log(218.189453,2),math.log(224.218750,2),math.log(245.486328,2),math.log(275.918213,2),math.log(231.933228,2),math.log(262.641907,2),math.log(298.464417,2)]
t_202 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(252.000000,2),math.log(280.000000,2),math.log(241.625000,2),math.log(222.250000,2),math.log(262.218750,2),math.log(270.500000,2),math.log(259.914062,2),math.log(263.250000,2),math.log(246.503906,2),math.log(240.259766,2),math.log(252.793945,2),math.log(252.114990,2),math.log(275.693115,2),math.log(302.188599,2),math.log(284.990936,2)]
t_203 = [math.log(224.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(294.000000,2),math.log(259.000000,2),math.log(285.500000,2),math.log(267.750000,2),math.log(258.750000,2),math.log(234.375000,2),math.log(250.218750,2),math.log(232.453125,2),math.log(211.539062,2),math.log(242.027344,2),math.log(232.732422,2),math.log(266.058594,2),math.log(272.229004,2),math.log(268.946777,2),math.log(233.364746,2),math.log(271.093933,2),math.log(263.501678,2)]
t_204 = [math.log(256.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(204.000000,2),math.log(223.000000,2),math.log(215.000000,2),math.log(218.750000,2),math.log(221.000000,2),math.log(225.250000,2),math.log(227.000000,2),math.log(223.984375,2),math.log(274.718750,2),math.log(282.546875,2),math.log(265.148438,2),math.log(257.708008,2),math.log(287.112793,2),math.log(279.714111,2),math.log(250.704956,2),math.log(250.289062,2),math.log(251.079193,2)]
t_205 = [math.log(224.000000,2),math.log(208.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(258.000000,2),math.log(219.500000,2),math.log(224.250000,2),math.log(229.375000,2),math.log(253.500000,2),math.log(245.281250,2),math.log(282.968750,2),math.log(279.039062,2),math.log(285.703125,2),math.log(280.900391,2),math.log(260.566406,2),math.log(270.863770,2),math.log(245.547607,2),math.log(228.764160,2),math.log(229.200256,2),math.log(241.127167,2)]
t_206 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(229.000000,2),math.log(235.000000,2),math.log(239.500000,2),math.log(240.875000,2),math.log(242.250000,2),math.log(257.531250,2),math.log(236.250000,2),math.log(239.195312,2),math.log(250.761719,2),math.log(257.382812,2),math.log(254.748047,2),math.log(242.740723,2),math.log(232.127197,2),math.log(223.043945,2),math.log(210.596130,2),math.log(253.514343,2)]
t_207 = [math.log(272.000000,2),math.log(248.000000,2),math.log(316.000000,2),math.log(314.000000,2),math.log(268.000000,2),math.log(252.500000,2),math.log(255.750000,2),math.log(271.375000,2),math.log(304.812500,2),math.log(300.781250,2),math.log(297.921875,2),math.log(271.367188,2),math.log(242.750000,2),math.log(285.025391,2),math.log(260.529297,2),math.log(239.005859,2),math.log(234.571289,2),math.log(255.947266,2),math.log(257.849304,2),math.log(233.569855,2)]
t_208 = [math.log(224.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(277.000000,2),math.log(261.500000,2),math.log(237.250000,2),math.log(210.125000,2),math.log(255.625000,2),math.log(289.343750,2),math.log(278.437500,2),math.log(286.296875,2),math.log(258.277344,2),math.log(276.550781,2),math.log(246.696289,2),math.log(234.841797,2),math.log(280.635498,2),math.log(283.010254,2),math.log(249.918518,2),math.log(269.404327,2)]
t_209 = [math.log(272.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(222.000000,2),math.log(185.000000,2),math.log(196.000000,2),math.log(232.500000,2),math.log(248.875000,2),math.log(240.250000,2),math.log(251.875000,2),math.log(244.093750,2),math.log(249.796875,2),math.log(243.015625,2),math.log(248.574219,2),math.log(256.323242,2),math.log(276.702148,2),math.log(255.463379,2),math.log(267.486572,2),math.log(287.034790,2),math.log(286.950439,2)]
t_210 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(236.000000,2),math.log(215.000000,2),math.log(241.250000,2),math.log(218.875000,2),math.log(232.687500,2),math.log(232.500000,2),math.log(258.859375,2),math.log(292.078125,2),math.log(249.019531,2),math.log(256.843750,2),math.log(250.948242,2),math.log(280.831055,2),math.log(286.481689,2),math.log(297.821167,2),math.log(256.562927,2),math.log(226.373779,2)]
t_211 = [math.log(272.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(251.000000,2),math.log(280.250000,2),math.log(286.625000,2),math.log(266.187500,2),math.log(250.750000,2),math.log(245.343750,2),math.log(236.765625,2),math.log(241.421875,2),math.log(256.177734,2),math.log(238.107422,2),math.log(237.304688,2),math.log(245.026123,2),math.log(259.973022,2),math.log(286.918884,2),math.log(296.664185,2)]
t_212 = [math.log(240.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(221.000000,2),math.log(235.000000,2),math.log(242.750000,2),math.log(235.375000,2),math.log(254.062500,2),math.log(243.218750,2),math.log(251.281250,2),math.log(268.593750,2),math.log(259.406250,2),math.log(288.593750,2),math.log(309.725586,2),math.log(276.767090,2),math.log(258.538086,2),math.log(277.602417,2),math.log(241.209229,2),math.log(261.969666,2)]
t_213 = [math.log(304.000000,2),math.log(296.000000,2),math.log(288.000000,2),math.log(278.000000,2),math.log(245.000000,2),math.log(266.500000,2),math.log(250.000000,2),math.log(240.875000,2),math.log(247.625000,2),math.log(232.250000,2),math.log(223.609375,2),math.log(229.609375,2),math.log(218.914062,2),math.log(250.777344,2),math.log(227.991211,2),math.log(256.334473,2),math.log(244.853516,2),math.log(238.836304,2),math.log(258.524414,2),math.log(251.205536,2)]
t_214 = [math.log(272.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(258.000000,2),math.log(265.500000,2),math.log(262.250000,2),math.log(273.500000,2),math.log(275.562500,2),math.log(236.906250,2),math.log(208.031250,2),math.log(232.070312,2),math.log(225.496094,2),math.log(267.501953,2),math.log(298.444336,2),math.log(273.587402,2),math.log(268.405029,2),math.log(268.127319,2),math.log(249.340332,2),math.log(250.960632,2)]
t_215 = [math.log(240.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(239.000000,2),math.log(265.500000,2),math.log(222.750000,2),math.log(245.500000,2),math.log(234.500000,2),math.log(226.781250,2),math.log(217.625000,2),math.log(230.703125,2),math.log(239.324219,2),math.log(242.761719,2),math.log(232.740234,2),math.log(276.731445,2),math.log(271.315186,2),math.log(287.101318,2),math.log(230.005615,2),math.log(213.777802,2)]
t_216 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(258.000000,2),math.log(305.750000,2),math.log(265.500000,2),math.log(243.000000,2),math.log(226.968750,2),math.log(250.296875,2),math.log(235.734375,2),math.log(245.265625,2),math.log(251.363281,2),math.log(265.747070,2),math.log(252.125488,2),math.log(234.344727,2),math.log(253.296753,2),math.log(231.862915,2),math.log(205.162445,2)]
t_217 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(240.000000,2),math.log(227.000000,2),math.log(222.000000,2),math.log(224.000000,2),math.log(231.375000,2),math.log(240.125000,2),math.log(285.437500,2),math.log(281.062500,2),math.log(243.351562,2),math.log(266.054688,2),math.log(280.312500,2),math.log(271.475586,2),math.log(269.773926,2),math.log(231.671631,2),math.log(229.181641,2),math.log(262.759521,2),math.log(245.285095,2)]
t_218 = [math.log(240.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(284.000000,2),math.log(233.000000,2),math.log(242.000000,2),math.log(247.000000,2),math.log(247.125000,2),math.log(303.062500,2),math.log(301.968750,2),math.log(301.765625,2),math.log(274.726562,2),math.log(300.125000,2),math.log(286.876953,2),math.log(255.254883,2),math.log(259.861328,2),math.log(267.821533,2),math.log(241.510010,2),math.log(278.416809,2),math.log(243.990112,2)]
t_219 = [math.log(240.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(261.500000,2),math.log(237.250000,2),math.log(221.500000,2),math.log(226.125000,2),math.log(255.593750,2),math.log(282.843750,2),math.log(296.875000,2),math.log(259.703125,2),math.log(255.814453,2),math.log(290.139648,2),math.log(267.273926,2),math.log(244.348145,2),math.log(228.022583,2),math.log(249.824280,2),math.log(244.689850,2)]
t_220 = [math.log(288.000000,2),math.log(312.000000,2),math.log(312.000000,2),math.log(266.000000,2),math.log(245.000000,2),math.log(214.500000,2),math.log(228.250000,2),math.log(232.625000,2),math.log(279.812500,2),math.log(295.156250,2),math.log(270.718750,2),math.log(303.890625,2),math.log(320.023438,2),math.log(294.509766,2),math.log(276.896484,2),math.log(238.684082,2),math.log(279.066650,2),math.log(301.663086,2),math.log(311.487183,2),math.log(265.983368,2)]
t_221 = [math.log(272.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(242.000000,2),math.log(281.000000,2),math.log(250.000000,2),math.log(237.500000,2),math.log(256.125000,2),math.log(285.625000,2),math.log(274.843750,2),math.log(261.875000,2),math.log(265.187500,2),math.log(274.535156,2),math.log(265.474609,2),math.log(255.332031,2),math.log(263.629395,2),math.log(251.342041,2),math.log(252.140869,2),math.log(282.844849,2),math.log(271.033600,2)]
t_222 = [math.log(224.000000,2),math.log(200.000000,2),math.log(228.000000,2),math.log(276.000000,2),math.log(265.000000,2),math.log(238.500000,2),math.log(212.750000,2),math.log(219.000000,2),math.log(225.062500,2),math.log(258.093750,2),math.log(284.046875,2),math.log(255.351562,2),math.log(226.832031,2),math.log(248.675781,2),math.log(265.540039,2),math.log(230.727539,2),math.log(222.751465,2),math.log(228.639771,2),math.log(257.684509,2),math.log(276.624939,2)]
t_223 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(258.000000,2),math.log(259.000000,2),math.log(253.000000,2),math.log(243.000000,2),math.log(240.500000,2),math.log(244.750000,2),math.log(237.062500,2),math.log(266.000000,2),math.log(274.578125,2),math.log(239.738281,2),math.log(223.419922,2),math.log(305.601562,2),math.log(276.354980,2),math.log(276.798828,2),math.log(287.276123,2),math.log(255.215576,2),math.log(250.267609,2)]
t_224 = [math.log(304.000000,2),math.log(296.000000,2),math.log(252.000000,2),math.log(220.000000,2),math.log(243.000000,2),math.log(244.000000,2),math.log(249.000000,2),math.log(213.000000,2),math.log(249.312500,2),math.log(239.593750,2),math.log(243.328125,2),math.log(247.250000,2),math.log(250.210938,2),math.log(215.648438,2),math.log(220.409180,2),math.log(254.907715,2),math.log(233.577881,2),math.log(217.477051,2),math.log(218.145447,2),math.log(285.400116,2)]
t_225 = [math.log(224.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(256.000000,2),math.log(285.500000,2),math.log(295.000000,2),math.log(275.625000,2),math.log(269.062500,2),math.log(288.781250,2),math.log(244.250000,2),math.log(243.960938,2),math.log(246.507812,2),math.log(231.931641,2),math.log(242.354492,2),math.log(235.833984,2),math.log(246.505859,2),math.log(230.248657,2),math.log(250.631714,2),math.log(240.883392,2)]
t_226 = [math.log(240.000000,2),math.log(296.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(303.000000,2),math.log(270.750000,2),math.log(236.750000,2),math.log(212.812500,2),math.log(245.875000,2),math.log(254.765625,2),math.log(252.507812,2),math.log(267.070312,2),math.log(216.380859,2),math.log(240.689453,2),math.log(244.071289,2),math.log(233.715332,2),math.log(222.905396,2),math.log(251.926208,2),math.log(252.439362,2)]
t_227 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(234.000000,2),math.log(226.000000,2),math.log(231.750000,2),math.log(274.750000,2),math.log(266.375000,2),math.log(274.812500,2),math.log(251.000000,2),math.log(201.296875,2),math.log(215.617188,2),math.log(232.783203,2),math.log(249.417969,2),math.log(276.590820,2),math.log(288.854004,2),math.log(285.172852,2),math.log(276.197998,2),math.log(323.559631,2)]
t_228 = [math.log(272.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(270.000000,2),math.log(262.500000,2),math.log(282.000000,2),math.log(268.750000,2),math.log(240.562500,2),math.log(238.812500,2),math.log(244.890625,2),math.log(267.320312,2),math.log(274.925781,2),math.log(247.996094,2),math.log(213.495117,2),math.log(259.507812,2),math.log(249.270752,2),math.log(255.008301,2),math.log(230.286072,2),math.log(267.665771,2)]
t_229 = [math.log(272.000000,2),math.log(296.000000,2),math.log(304.000000,2),math.log(262.000000,2),math.log(278.000000,2),math.log(267.500000,2),math.log(275.250000,2),math.log(302.375000,2),math.log(281.625000,2),math.log(273.562500,2),math.log(258.390625,2),math.log(267.351562,2),math.log(291.972656,2),math.log(272.566406,2),math.log(242.125977,2),math.log(220.034668,2),math.log(223.673828,2),math.log(249.201660,2),math.log(257.092346,2),math.log(275.740143,2)]
t_230 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(210.000000,2),math.log(235.000000,2),math.log(232.000000,2),math.log(236.750000,2),math.log(239.375000,2),math.log(247.250000,2),math.log(248.031250,2),math.log(209.484375,2),math.log(274.390625,2),math.log(258.574219,2),math.log(239.042969,2),math.log(261.482422,2),math.log(280.157715,2),math.log(233.876465,2),math.log(236.668457,2),math.log(223.931335,2),math.log(209.905701,2)]
t_231 = [math.log(256.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(265.000000,2),math.log(227.500000,2),math.log(251.500000,2),math.log(253.500000,2),math.log(262.000000,2),math.log(275.968750,2),math.log(285.281250,2),math.log(291.398438,2),math.log(283.437500,2),math.log(254.314453,2),math.log(234.646484,2),math.log(252.360840,2),math.log(267.315674,2),math.log(280.506836,2),math.log(278.695312,2),math.log(297.123077,2)]
t_232 = [math.log(272.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(238.000000,2),math.log(256.500000,2),math.log(274.750000,2),math.log(225.250000,2),math.log(226.937500,2),math.log(208.156250,2),math.log(281.281250,2),math.log(242.351562,2),math.log(283.207031,2),math.log(279.900391,2),math.log(254.446289,2),math.log(244.999023,2),math.log(223.756348,2),math.log(222.896484,2),math.log(215.814148,2),math.log(220.188202,2)]
t_233 = [math.log(272.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(274.000000,2),math.log(299.000000,2),math.log(272.000000,2),math.log(275.250000,2),math.log(234.250000,2),math.log(234.125000,2),math.log(245.375000,2),math.log(221.359375,2),math.log(206.859375,2),math.log(232.886719,2),math.log(267.970703,2),math.log(267.316406,2),math.log(236.658691,2),math.log(222.627930,2),math.log(241.361816,2),math.log(267.513916,2),math.log(274.028625,2)]
t_234 = [math.log(272.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(236.000000,2),math.log(261.500000,2),math.log(229.750000,2),math.log(270.125000,2),math.log(250.625000,2),math.log(265.406250,2),math.log(277.234375,2),math.log(260.890625,2),math.log(254.281250,2),math.log(247.195312,2),math.log(250.468750,2),math.log(237.333496,2),math.log(248.742920,2),math.log(249.717163,2),math.log(252.388489,2),math.log(222.319092,2)]
t_235 = [math.log(288.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(269.500000,2),math.log(280.250000,2),math.log(242.500000,2),math.log(248.937500,2),math.log(274.218750,2),math.log(264.609375,2),math.log(300.476562,2),math.log(269.281250,2),math.log(257.968750,2),math.log(268.958008,2),math.log(246.382812,2),math.log(261.233643,2),math.log(219.833374,2),math.log(201.072632,2),math.log(214.255920,2)]
t_236 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(261.000000,2),math.log(281.000000,2),math.log(252.500000,2),math.log(236.000000,2),math.log(249.250000,2),math.log(264.062500,2),math.log(262.000000,2),math.log(264.281250,2),math.log(311.609375,2),math.log(327.357422,2),math.log(258.391602,2),math.log(261.951660,2),math.log(223.997559,2),math.log(223.739258,2),math.log(245.093872,2),math.log(240.881378,2)]
t_237 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(265.500000,2),math.log(254.500000,2),math.log(244.125000,2),math.log(233.562500,2),math.log(242.281250,2),math.log(236.515625,2),math.log(225.226562,2),math.log(223.078125,2),math.log(216.306641,2),math.log(249.208984,2),math.log(275.436035,2),math.log(243.545410,2),math.log(273.455322,2),math.log(246.844666,2),math.log(248.543060,2)]
t_238 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(254.000000,2),math.log(251.500000,2),math.log(263.750000,2),math.log(295.375000,2),math.log(287.125000,2),math.log(297.375000,2),math.log(281.343750,2),math.log(289.468750,2),math.log(250.769531,2),math.log(240.125000,2),math.log(249.575195,2),math.log(254.572754,2),math.log(279.098389,2),math.log(280.794922,2),math.log(273.757874,2),math.log(239.038300,2)]
t_239 = [math.log(224.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(253.000000,2),math.log(214.500000,2),math.log(192.500000,2),math.log(226.250000,2),math.log(273.250000,2),math.log(266.250000,2),math.log(282.921875,2),math.log(242.890625,2),math.log(223.500000,2),math.log(217.958984,2),math.log(212.798828,2),math.log(253.500488,2),math.log(258.276855,2),math.log(270.908447,2),math.log(279.635071,2),math.log(260.669067,2)]
t_240 = [math.log(256.000000,2),math.log(248.000000,2),math.log(324.000000,2),math.log(300.000000,2),math.log(289.000000,2),math.log(249.000000,2),math.log(252.750000,2),math.log(259.000000,2),math.log(283.000000,2),math.log(278.687500,2),math.log(289.078125,2),math.log(263.882812,2),math.log(287.722656,2),math.log(264.515625,2),math.log(246.909180,2),math.log(242.554199,2),math.log(281.074951,2),math.log(276.298828,2),math.log(257.601379,2),math.log(232.610413,2)]
t_241 = [math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(266.000000,2),math.log(267.000000,2),math.log(265.000000,2),math.log(264.500000,2),math.log(270.875000,2),math.log(262.687500,2),math.log(263.750000,2),math.log(278.921875,2),math.log(250.281250,2),math.log(277.410156,2),math.log(277.318359,2),math.log(245.234375,2),math.log(237.653809,2),math.log(219.798340,2),math.log(238.389038,2),math.log(235.736694,2),math.log(247.853821,2)]
t_242 = [math.log(240.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(247.000000,2),math.log(231.500000,2),math.log(235.250000,2),math.log(259.750000,2),math.log(263.187500,2),math.log(273.281250,2),math.log(258.031250,2),math.log(284.695312,2),math.log(231.027344,2),math.log(206.117188,2),math.log(228.047852,2),math.log(220.986816,2),math.log(231.606934,2),math.log(249.664429,2),math.log(261.648376,2),math.log(302.304535,2)]
t_243 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(296.000000,2),math.log(310.500000,2),math.log(279.250000,2),math.log(257.875000,2),math.log(252.312500,2),math.log(280.218750,2),math.log(273.062500,2),math.log(272.484375,2),math.log(219.347656,2),math.log(247.703125,2),math.log(262.980469,2),math.log(262.968262,2),math.log(280.570801,2),math.log(241.179199,2),math.log(272.754028,2),math.log(266.427185,2)]
t_244 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(231.000000,2),math.log(246.000000,2),math.log(280.500000,2),math.log(278.750000,2),math.log(243.750000,2),math.log(258.812500,2),math.log(248.546875,2),math.log(252.390625,2),math.log(267.703125,2),math.log(263.638672,2),math.log(261.155273,2),math.log(236.921387,2),math.log(236.369141,2),math.log(254.250977,2),math.log(280.516724,2),math.log(283.934418,2)]
t_245 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(213.000000,2),math.log(231.500000,2),math.log(224.500000,2),math.log(266.687500,2),math.log(276.031250,2),math.log(238.093750,2),math.log(236.695312,2),math.log(246.894531,2),math.log(271.419922,2),math.log(277.372070,2),math.log(267.569336,2),math.log(261.571533,2),math.log(268.361694,2),math.log(261.913391,2),math.log(250.349060,2)]
t_246 = [math.log(224.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(230.000000,2),math.log(239.000000,2),math.log(224.000000,2),math.log(242.500000,2),math.log(248.500000,2),math.log(267.125000,2),math.log(279.531250,2),math.log(254.593750,2),math.log(282.039062,2),math.log(282.835938,2),math.log(261.826172,2),math.log(229.657227,2),math.log(255.628418,2),math.log(259.677002,2),math.log(242.882568,2),math.log(239.186401,2),math.log(245.487518,2)]
t_247 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(242.500000,2),math.log(237.375000,2),math.log(233.687500,2),math.log(265.500000,2),math.log(268.078125,2),math.log(216.953125,2),math.log(228.328125,2),math.log(274.496094,2),math.log(253.548828,2),math.log(257.384766,2),math.log(264.180664,2),math.log(256.143433,2),math.log(252.875977,2),math.log(266.785919,2)]
t_248 = [math.log(320.000000,2),math.log(296.000000,2),math.log(244.000000,2),math.log(268.000000,2),math.log(256.000000,2),math.log(268.500000,2),math.log(257.250000,2),math.log(270.500000,2),math.log(261.000000,2),math.log(248.687500,2),math.log(238.125000,2),math.log(225.390625,2),math.log(217.199219,2),math.log(227.833984,2),math.log(223.500000,2),math.log(241.675293,2),math.log(244.649170,2),math.log(242.329834,2),math.log(265.426086,2),math.log(273.885345,2)]
t_249 = [math.log(288.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(276.000000,2),math.log(249.000000,2),math.log(285.000000,2),math.log(277.500000,2),math.log(252.500000,2),math.log(259.812500,2),math.log(253.062500,2),math.log(263.250000,2),math.log(241.171875,2),math.log(233.066406,2),math.log(244.998047,2),math.log(228.451172,2),math.log(240.218750,2),math.log(255.837402,2),math.log(213.298828,2),math.log(247.872986,2),math.log(273.894592,2)]
t_250 = [math.log(224.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(241.000000,2),math.log(256.500000,2),math.log(226.750000,2),math.log(227.500000,2),math.log(198.000000,2),math.log(257.046875,2),math.log(271.851562,2),math.log(276.617188,2),math.log(280.804688,2),math.log(284.875000,2),math.log(268.571777,2),math.log(269.966309,2),math.log(254.695190,2),math.log(249.085754,2),math.log(232.589478,2)]
t_251 = [math.log(320.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(249.000000,2),math.log(287.500000,2),math.log(272.750000,2),math.log(246.750000,2),math.log(234.875000,2),math.log(228.593750,2),math.log(223.062500,2),math.log(240.882812,2),math.log(273.558594,2),math.log(255.339844,2),math.log(269.816406,2),math.log(233.810059,2),math.log(228.962891,2),math.log(238.538208,2),math.log(244.993835,2),math.log(231.226898,2)]
t_252 = [math.log(288.000000,2),math.log(280.000000,2),math.log(228.000000,2),math.log(248.000000,2),math.log(203.000000,2),math.log(237.500000,2),math.log(248.500000,2),math.log(266.375000,2),math.log(296.125000,2),math.log(236.062500,2),math.log(228.171875,2),math.log(251.507812,2),math.log(268.304688,2),math.log(214.761719,2),math.log(239.222656,2),math.log(223.195312,2),math.log(253.684326,2),math.log(264.626831,2),math.log(320.219421,2),math.log(258.586060,2)]
t_253 = [math.log(240.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(238.000000,2),math.log(229.500000,2),math.log(256.750000,2),math.log(270.625000,2),math.log(259.187500,2),math.log(272.250000,2),math.log(247.953125,2),math.log(309.007812,2),math.log(268.519531,2),math.log(239.150391,2),math.log(251.855469,2),math.log(239.326660,2),math.log(221.795898,2),math.log(241.885254,2),math.log(228.936218,2),math.log(240.440918,2)]
t_254 = [math.log(240.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(241.000000,2),math.log(248.500000,2),math.log(250.000000,2),math.log(230.875000,2),math.log(232.750000,2),math.log(238.906250,2),math.log(218.953125,2),math.log(210.476562,2),math.log(232.761719,2),math.log(237.025391,2),math.log(279.514648,2),math.log(284.958496,2),math.log(287.931396,2),math.log(261.060669,2),math.log(240.988586,2),math.log(240.581757,2)]
t_255 = [math.log(240.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(240.000000,2),math.log(247.000000,2),math.log(277.000000,2),math.log(252.250000,2),math.log(291.375000,2),math.log(246.375000,2),math.log(271.062500,2),math.log(267.125000,2),math.log(294.835938,2),math.log(258.855469,2),math.log(213.958984,2),math.log(200.118164,2),math.log(231.999023,2),math.log(248.198242,2),math.log(253.187866,2),math.log(257.992615,2),math.log(264.329041)]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00001510
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00001510)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00001510
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00001510)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00001510
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00001510)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00001510
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00001510)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00001510
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00001510)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00001510
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00001510)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00001510
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00001510)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00001510
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00001510)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00001510
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00001510)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00001510
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00001510)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00001510
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00001510)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00001510
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00001510)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00001510
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00001510)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00001510
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00001510)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00001510
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00001510)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00001510
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00001510)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00001510
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00001510)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00001510
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00001510)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00001510
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00001510)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00001510
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00001510)**2)


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
plt.plot(t,expected_T_a_0,linewidth=1, linestyle="-", c="DimGray")

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
plt.plot(t,expected_T_a_1,linewidth=1, linestyle="-", c="DimGray")

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
plt.plot(t,expected_T_a_2,linewidth=1, linestyle="-", c="DimGray")

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
plt.plot(t,expected_T_a_3,linewidth=1, linestyle="-", c="DimGray")

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
plt.plot(t,expected_T_a_4,linewidth=1, linestyle="-", c="DimGray")

#Plotting the experimental lines
plt.plot(t, t_0, linewidth=.001, linestyle="-", c="red",alpha = .15)
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
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 13 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(8.5,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
