import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(224.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(267.000000,2),math.log(271.000000,2),math.log(273.000000,2),math.log(282.500000,2),math.log(307.375000,2),math.log(284.468750,2),math.log(264.421875,2),math.log(264.945312,2),math.log(218.421875,2),math.log(226.324219,2),math.log(235.518555,2),math.log(225.928711,2),math.log(237.283691,2),math.log(253.341553,2),math.log(290.316345,2),math.log(302.522919,2)]
t_1 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(270.000000,2),math.log(256.000000,2),math.log(273.000000,2),math.log(238.250000,2),math.log(216.187500,2),math.log(250.312500,2),math.log(224.515625,2),math.log(229.101562,2),math.log(210.695312,2),math.log(227.214844,2),math.log(187.340820,2),math.log(230.020020,2),math.log(231.315674,2),math.log(233.544312,2),math.log(240.780640,2),math.log(254.588348,2)]
t_2 = [math.log(224.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(247.000000,2),math.log(281.000000,2),math.log(298.750000,2),math.log(246.375000,2),math.log(260.000000,2),math.log(232.125000,2),math.log(222.312500,2),math.log(246.312500,2),math.log(250.933594,2),math.log(263.492188,2),math.log(252.469727,2),math.log(268.306641,2),math.log(269.213623,2),math.log(260.990479,2),math.log(266.289307,2),math.log(259.337646,2)]
t_3 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(232.000000,2),math.log(270.500000,2),math.log(260.000000,2),math.log(238.125000,2),math.log(214.312500,2),math.log(217.000000,2),math.log(276.109375,2),math.log(247.140625,2),math.log(242.390625,2),math.log(247.279297,2),math.log(236.947266,2),math.log(292.757324,2),math.log(301.821045,2),math.log(318.176880,2),math.log(340.183899,2),math.log(293.361572,2)]
t_4 = [math.log(256.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(247.500000,2),math.log(277.750000,2),math.log(251.625000,2),math.log(268.750000,2),math.log(238.687500,2),math.log(237.500000,2),math.log(229.328125,2),math.log(242.937500,2),math.log(245.875000,2),math.log(223.001953,2),math.log(223.989746,2),math.log(206.251465,2),math.log(262.915649,2),math.log(224.410950,2),math.log(286.926422,2)]
t_5 = [math.log(272.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(290.000000,2),math.log(273.000000,2),math.log(269.500000,2),math.log(241.000000,2),math.log(290.000000,2),math.log(267.375000,2),math.log(285.031250,2),math.log(271.734375,2),math.log(252.742188,2),math.log(219.191406,2),math.log(208.980469,2),math.log(203.959961,2),math.log(229.757812,2),math.log(253.259277,2),math.log(280.103394,2),math.log(280.026855,2),math.log(298.090729,2)]
t_6 = [math.log(240.000000,2),math.log(224.000000,2),math.log(268.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(281.500000,2),math.log(232.250000,2),math.log(274.125000,2),math.log(229.312500,2),math.log(232.125000,2),math.log(255.781250,2),math.log(242.179688,2),math.log(265.398438,2),math.log(245.701172,2),math.log(242.633789,2),math.log(230.784668,2),math.log(234.222656,2),math.log(248.688721,2),math.log(284.305542,2),math.log(250.868439,2)]
t_7 = [math.log(272.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(196.000000,2),math.log(250.000000,2),math.log(242.000000,2),math.log(286.000000,2),math.log(249.375000,2),math.log(239.625000,2),math.log(273.312500,2),math.log(264.609375,2),math.log(272.492188,2),math.log(262.878906,2),math.log(282.533203,2),math.log(287.505859,2),math.log(275.877441,2),math.log(232.986084,2),math.log(251.537964,2),math.log(254.494385,2),math.log(256.759125,2)]
t_8 = [math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(217.000000,2),math.log(230.500000,2),math.log(213.750000,2),math.log(227.625000,2),math.log(264.812500,2),math.log(264.000000,2),math.log(233.859375,2),math.log(264.429688,2),math.log(242.265625,2),math.log(249.541016,2),math.log(249.155273,2),math.log(224.188477,2),math.log(230.756592,2),math.log(217.515991,2),math.log(229.675842,2),math.log(220.931641,2)]
t_9 = [math.log(288.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(255.000000,2),math.log(237.000000,2),math.log(235.000000,2),math.log(220.250000,2),math.log(257.875000,2),math.log(264.156250,2),math.log(232.781250,2),math.log(249.453125,2),math.log(235.070312,2),math.log(246.986328,2),math.log(273.821289,2),math.log(285.833496,2),math.log(260.157227,2),math.log(275.940186,2),math.log(271.776611,2),math.log(244.295746,2)]
t_10 = [math.log(240.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(239.000000,2),math.log(270.750000,2),math.log(249.250000,2),math.log(233.062500,2),math.log(254.875000,2),math.log(237.968750,2),math.log(210.265625,2),math.log(200.667969,2),math.log(225.595703,2),math.log(226.145508,2),math.log(236.903320,2),math.log(217.484131,2),math.log(235.161987,2),math.log(255.216919,2),math.log(266.954224,2)]
t_11 = [math.log(272.000000,2),math.log(288.000000,2),math.log(292.000000,2),math.log(240.000000,2),math.log(243.000000,2),math.log(229.500000,2),math.log(233.750000,2),math.log(225.750000,2),math.log(237.687500,2),math.log(262.437500,2),math.log(268.203125,2),math.log(274.250000,2),math.log(301.253906,2),math.log(290.265625,2),math.log(284.077148,2),math.log(301.741211,2),math.log(267.596191,2),math.log(290.677246,2),math.log(278.796692,2),math.log(315.733307,2)]
t_12 = [math.log(288.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(254.000000,2),math.log(276.000000,2),math.log(293.500000,2),math.log(245.500000,2),math.log(223.500000,2),math.log(232.687500,2),math.log(257.500000,2),math.log(243.703125,2),math.log(235.718750,2),math.log(225.773438,2),math.log(251.980469,2),math.log(240.603516,2),math.log(279.748535,2),math.log(247.529541,2),math.log(284.111938,2),math.log(284.211304,2),math.log(310.995026,2)]
t_13 = [math.log(256.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(280.000000,2),math.log(251.000000,2),math.log(266.000000,2),math.log(237.250000,2),math.log(253.375000,2),math.log(240.062500,2),math.log(254.062500,2),math.log(287.640625,2),math.log(259.343750,2),math.log(244.441406,2),math.log(256.554688,2),math.log(245.756836,2),math.log(233.268066,2),math.log(236.879639,2),math.log(252.051514,2),math.log(283.410339,2),math.log(264.881378,2)]
t_14 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(262.000000,2),math.log(280.000000,2),math.log(281.500000,2),math.log(278.000000,2),math.log(258.750000,2),math.log(278.250000,2),math.log(251.500000,2),math.log(257.625000,2),math.log(258.796875,2),math.log(265.046875,2),math.log(263.560547,2),math.log(260.664062,2),math.log(267.410645,2),math.log(293.526123,2),math.log(324.110596,2),math.log(293.873535,2),math.log(265.449921,2)]
t_15 = [math.log(224.000000,2),math.log(216.000000,2),math.log(236.000000,2),math.log(262.000000,2),math.log(264.000000,2),math.log(222.000000,2),math.log(258.750000,2),math.log(251.750000,2),math.log(240.750000,2),math.log(256.093750,2),math.log(275.765625,2),math.log(260.156250,2),math.log(261.234375,2),math.log(258.406250,2),math.log(268.383789,2),math.log(315.492188,2),math.log(306.665771,2),math.log(300.627075,2),math.log(306.202087,2),math.log(279.999390,2)]
t_16 = [math.log(288.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(247.000000,2),math.log(248.500000,2),math.log(242.250000,2),math.log(244.875000,2),math.log(252.750000,2),math.log(242.343750,2),math.log(266.750000,2),math.log(280.539062,2),math.log(249.199219,2),math.log(268.179688,2),math.log(243.467773,2),math.log(238.197266,2),math.log(249.634766,2),math.log(241.302246,2),math.log(258.654480,2),math.log(211.641113,2)]
t_17 = [math.log(256.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(242.000000,2),math.log(275.500000,2),math.log(275.250000,2),math.log(283.500000,2),math.log(280.500000,2),math.log(297.781250,2),math.log(262.062500,2),math.log(256.468750,2),math.log(261.421875,2),math.log(253.673828,2),math.log(289.798828,2),math.log(283.322266,2),math.log(226.755859,2),math.log(255.689819,2),math.log(257.261169,2),math.log(265.957855,2)]
t_18 = [math.log(240.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(210.000000,2),math.log(259.750000,2),math.log(263.625000,2),math.log(255.937500,2),math.log(237.718750,2),math.log(244.765625,2),math.log(222.421875,2),math.log(206.910156,2),math.log(221.994141,2),math.log(228.525391,2),math.log(237.445312,2),math.log(235.425293,2),math.log(215.754395,2),math.log(195.596741,2),math.log(202.830353,2)]
t_19 = [math.log(224.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(259.000000,2),math.log(230.500000,2),math.log(215.750000,2),math.log(215.750000,2),math.log(221.125000,2),math.log(265.437500,2),math.log(239.593750,2),math.log(272.406250,2),math.log(288.738281,2),math.log(303.353516,2),math.log(279.319336,2),math.log(239.827637,2),math.log(242.604980,2),math.log(230.211060,2),math.log(243.727234,2),math.log(278.786957,2)]
t_20 = [math.log(240.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(250.000000,2),math.log(230.000000,2),math.log(251.500000,2),math.log(246.000000,2),math.log(255.250000,2),math.log(262.000000,2),math.log(240.625000,2),math.log(216.140625,2),math.log(244.617188,2),math.log(246.078125,2),math.log(269.982422,2),math.log(264.085938,2),math.log(226.379395,2),math.log(210.142822,2),math.log(245.493164,2),math.log(283.765808,2),math.log(263.686615,2)]
t_21 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(280.000000,2),math.log(266.000000,2),math.log(220.875000,2),math.log(240.000000,2),math.log(243.437500,2),math.log(228.031250,2),math.log(238.125000,2),math.log(258.125000,2),math.log(245.867188,2),math.log(259.219727,2),math.log(237.030762,2),math.log(262.059570,2),math.log(260.586914,2),math.log(213.686523,2),math.log(232.456146,2)]
t_22 = [math.log(240.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(293.000000,2),math.log(281.000000,2),math.log(256.250000,2),math.log(265.000000,2),math.log(229.437500,2),math.log(221.718750,2),math.log(265.578125,2),math.log(258.906250,2),math.log(251.972656,2),math.log(243.175781,2),math.log(245.838867,2),math.log(248.661133,2),math.log(243.425781,2),math.log(244.744873,2),math.log(268.829590,2),math.log(264.352539,2)]
t_23 = [math.log(288.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(304.000000,2),math.log(314.000000,2),math.log(292.000000,2),math.log(287.750000,2),math.log(267.375000,2),math.log(238.062500,2),math.log(241.718750,2),math.log(260.953125,2),math.log(260.734375,2),math.log(296.265625,2),math.log(274.619141,2),math.log(254.894531,2),math.log(261.882324,2),math.log(238.239746,2),math.log(232.988037,2),math.log(247.682800,2),math.log(260.464935,2)]
t_24 = [math.log(272.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(270.000000,2),math.log(250.500000,2),math.log(313.000000,2),math.log(290.750000,2),math.log(264.687500,2),math.log(251.062500,2),math.log(260.171875,2),math.log(260.148438,2),math.log(235.433594,2),math.log(252.212891,2),math.log(250.140625,2),math.log(250.547852,2),math.log(275.484863,2),math.log(280.650635,2),math.log(274.603394,2),math.log(227.241913,2)]
t_25 = [math.log(272.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(274.000000,2),math.log(285.000000,2),math.log(275.000000,2),math.log(312.250000,2),math.log(291.625000,2),math.log(266.125000,2),math.log(248.750000,2),math.log(260.789062,2),math.log(258.703125,2),math.log(226.199219,2),math.log(264.215820,2),math.log(253.396484,2),math.log(266.343262,2),math.log(250.147217,2),math.log(259.047241,2),math.log(279.829590,2)]
t_26 = [math.log(320.000000,2),math.log(296.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(270.000000,2),math.log(250.875000,2),math.log(267.562500,2),math.log(242.062500,2),math.log(274.437500,2),math.log(259.093750,2),math.log(238.011719,2),math.log(252.582031,2),math.log(259.593750,2),math.log(230.929688,2),math.log(229.976562,2),math.log(224.543701,2),math.log(240.652466,2),math.log(216.631378,2)]
t_27 = [math.log(256.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(249.000000,2),math.log(244.000000,2),math.log(253.750000,2),math.log(276.875000,2),math.log(253.187500,2),math.log(229.781250,2),math.log(245.171875,2),math.log(294.484375,2),math.log(284.144531,2),math.log(259.304688,2),math.log(270.886719,2),math.log(251.800293,2),math.log(249.293701,2),math.log(230.726807,2),math.log(257.796753,2),math.log(266.341644,2)]
t_28 = [math.log(240.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(287.000000,2),math.log(255.000000,2),math.log(270.500000,2),math.log(248.125000,2),math.log(250.937500,2),math.log(243.656250,2),math.log(253.421875,2),math.log(254.703125,2),math.log(249.480469,2),math.log(283.152344,2),math.log(261.212891,2),math.log(279.925781,2),math.log(282.984131,2),math.log(257.799316,2),math.log(260.482910,2),math.log(239.278595,2)]
t_29 = [math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(250.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(275.500000,2),math.log(265.625000,2),math.log(287.187500,2),math.log(285.062500,2),math.log(250.953125,2),math.log(278.593750,2),math.log(300.636719,2),math.log(281.548828,2),math.log(262.827148,2),math.log(275.437988,2),math.log(275.510742,2),math.log(230.642334,2),math.log(252.589355,2),math.log(260.328094,2)]
t_30 = [math.log(224.000000,2),math.log(216.000000,2),math.log(216.000000,2),math.log(228.000000,2),math.log(222.000000,2),math.log(246.500000,2),math.log(204.250000,2),math.log(187.875000,2),math.log(221.375000,2),math.log(239.500000,2),math.log(260.890625,2),math.log(282.656250,2),math.log(289.550781,2),math.log(260.576172,2),math.log(262.565430,2),math.log(253.281738,2),math.log(261.873047,2),math.log(264.349731,2),math.log(298.112732,2),math.log(289.230438,2)]
t_31 = [math.log(240.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(246.000000,2),math.log(254.000000,2),math.log(242.500000,2),math.log(243.750000,2),math.log(264.875000,2),math.log(300.062500,2),math.log(273.343750,2),math.log(295.171875,2),math.log(284.304688,2),math.log(312.015625,2),math.log(257.011719,2),math.log(234.447266,2),math.log(229.779785,2),math.log(215.715332,2),math.log(202.641724,2),math.log(223.947327,2),math.log(250.009674,2)]
t_32 = [math.log(288.000000,2),math.log(304.000000,2),math.log(292.000000,2),math.log(272.000000,2),math.log(229.000000,2),math.log(238.000000,2),math.log(245.750000,2),math.log(231.750000,2),math.log(242.875000,2),math.log(238.562500,2),math.log(238.843750,2),math.log(227.484375,2),math.log(218.542969,2),math.log(227.177734,2),math.log(218.912109,2),math.log(252.424316,2),math.log(250.553467,2),math.log(239.525024,2),math.log(235.015015,2),math.log(230.376556,2)]
t_33 = [math.log(224.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(286.000000,2),math.log(288.000000,2),math.log(298.500000,2),math.log(282.500000,2),math.log(253.875000,2),math.log(273.312500,2),math.log(270.843750,2),math.log(262.718750,2),math.log(267.304688,2),math.log(260.023438,2),math.log(283.382812,2),math.log(276.696289,2),math.log(228.419922,2),math.log(243.909668,2),math.log(288.080322,2),math.log(244.096191,2),math.log(277.801910,2)]
t_34 = [math.log(224.000000,2),math.log(232.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(271.000000,2),math.log(282.000000,2),math.log(255.750000,2),math.log(275.250000,2),math.log(245.281250,2),math.log(273.375000,2),math.log(272.148438,2),math.log(272.691406,2),math.log(256.914062,2),math.log(245.947266,2),math.log(248.921875,2),math.log(269.544678,2),math.log(244.152222,2),math.log(272.856567,2),math.log(285.912140,2)]
t_35 = [math.log(288.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(302.000000,2),math.log(253.000000,2),math.log(254.000000,2),math.log(254.250000,2),math.log(258.500000,2),math.log(220.437500,2),math.log(233.875000,2),math.log(278.687500,2),math.log(299.437500,2),math.log(291.710938,2),math.log(260.107422,2),math.log(289.591797,2),math.log(264.428711,2),math.log(266.863037,2),math.log(287.649292,2),math.log(269.898743,2),math.log(267.110138,2)]
t_36 = [math.log(272.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(247.000000,2),math.log(238.250000,2),math.log(225.875000,2),math.log(235.687500,2),math.log(216.062500,2),math.log(233.984375,2),math.log(246.617188,2),math.log(243.226562,2),math.log(218.513672,2),math.log(222.949219,2),math.log(244.115723,2),math.log(264.644043,2),math.log(249.609253,2),math.log(234.122375,2),math.log(230.963470,2)]
t_37 = [math.log(288.000000,2),math.log(272.000000,2),math.log(220.000000,2),math.log(242.000000,2),math.log(205.000000,2),math.log(233.000000,2),math.log(248.250000,2),math.log(271.625000,2),math.log(249.875000,2),math.log(286.750000,2),math.log(221.312500,2),math.log(247.304688,2),math.log(269.343750,2),math.log(250.548828,2),math.log(244.342773,2),math.log(234.249023,2),math.log(250.043945,2),math.log(240.385254,2),math.log(248.649780,2),math.log(269.812469,2)]
t_38 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(263.000000,2),math.log(266.000000,2),math.log(291.750000,2),math.log(281.875000,2),math.log(274.812500,2),math.log(261.281250,2),math.log(258.578125,2),math.log(240.085938,2),math.log(237.148438,2),math.log(252.455078,2),math.log(268.926758,2),math.log(248.416992,2),math.log(271.227051,2),math.log(256.167358,2),math.log(300.887085,2),math.log(244.589661,2)]
t_39 = [math.log(240.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(249.750000,2),math.log(259.000000,2),math.log(292.375000,2),math.log(261.593750,2),math.log(242.218750,2),math.log(247.070312,2),math.log(268.863281,2),math.log(251.751953,2),math.log(272.696289,2),math.log(281.894531,2),math.log(287.538574,2),math.log(309.126709,2),math.log(273.876526,2),math.log(279.024139,2)]
t_40 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(276.000000,2),math.log(244.000000,2),math.log(256.500000,2),math.log(252.750000,2),math.log(265.500000,2),math.log(273.562500,2),math.log(239.406250,2),math.log(261.406250,2),math.log(255.726562,2),math.log(272.164062,2),math.log(252.748047,2),math.log(266.588867,2),math.log(243.642578,2),math.log(234.157715,2),math.log(220.196899,2),math.log(219.322205,2),math.log(257.231476,2)]
t_41 = [math.log(272.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(274.000000,2),math.log(309.000000,2),math.log(266.500000,2),math.log(257.500000,2),math.log(238.250000,2),math.log(220.312500,2),math.log(265.031250,2),math.log(258.437500,2),math.log(249.234375,2),math.log(273.730469,2),math.log(239.357422,2),math.log(236.208984,2),math.log(221.184570,2),math.log(230.094238,2),math.log(214.106934,2),math.log(236.784424,2),math.log(299.200226,2)]
t_42 = [math.log(240.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(228.000000,2),math.log(231.500000,2),math.log(223.250000,2),math.log(211.625000,2),math.log(252.562500,2),math.log(259.531250,2),math.log(238.437500,2),math.log(260.132812,2),math.log(265.417969,2),math.log(262.216797,2),math.log(234.161133,2),math.log(239.861328,2),math.log(286.022949,2),math.log(244.022095,2),math.log(236.753601,2),math.log(235.768188,2)]
t_43 = [math.log(224.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(266.000000,2),math.log(267.000000,2),math.log(271.000000,2),math.log(235.000000,2),math.log(247.125000,2),math.log(267.562500,2),math.log(236.125000,2),math.log(255.531250,2),math.log(279.601562,2),math.log(238.988281,2),math.log(234.037109,2),math.log(263.863281,2),math.log(293.245117,2),math.log(277.707275,2),math.log(267.759766,2),math.log(254.015503,2),math.log(240.753906,2)]
t_44 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(258.000000,2),math.log(253.000000,2),math.log(241.625000,2),math.log(223.125000,2),math.log(226.875000,2),math.log(259.609375,2),math.log(264.062500,2),math.log(290.859375,2),math.log(261.220703,2),math.log(277.882812,2),math.log(258.472168,2),math.log(262.004883,2),math.log(276.337891,2),math.log(265.748962,2),math.log(228.621216,2)]
t_45 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(230.500000,2),math.log(271.250000,2),math.log(295.000000,2),math.log(285.750000,2),math.log(295.906250,2),math.log(259.234375,2),math.log(252.906250,2),math.log(273.773438,2),math.log(267.132812,2),math.log(246.061523,2),math.log(278.741699,2),math.log(254.225586,2),math.log(251.781006,2),math.log(256.968445,2),math.log(240.654480,2)]
t_46 = [math.log(240.000000,2),math.log(296.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(228.000000,2),math.log(255.500000,2),math.log(232.000000,2),math.log(194.125000,2),math.log(241.062500,2),math.log(231.625000,2),math.log(202.812500,2),math.log(222.648438,2),math.log(257.066406,2),math.log(251.193359,2),math.log(243.113281,2),math.log(292.187012,2),math.log(267.986816,2),math.log(292.405518,2),math.log(263.836365,2),math.log(257.217163,2)]
t_47 = [math.log(224.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(258.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(250.500000,2),math.log(230.375000,2),math.log(223.500000,2),math.log(226.750000,2),math.log(242.343750,2),math.log(259.656250,2),math.log(228.937500,2),math.log(225.699219,2),math.log(228.814453,2),math.log(260.912109,2),math.log(256.701416,2),math.log(215.040283,2),math.log(251.030945,2),math.log(246.224915,2)]
t_48 = [math.log(224.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(242.000000,2),math.log(258.000000,2),math.log(249.000000,2),math.log(264.500000,2),math.log(260.125000,2),math.log(231.125000,2),math.log(240.406250,2),math.log(269.328125,2),math.log(275.375000,2),math.log(258.750000,2),math.log(238.093750,2),math.log(258.948242,2),math.log(285.492188,2),math.log(253.591309,2),math.log(234.897339,2),math.log(223.634155,2),math.log(225.864258,2)]
t_49 = [math.log(272.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(253.500000,2),math.log(277.875000,2),math.log(247.937500,2),math.log(263.875000,2),math.log(269.828125,2),math.log(273.000000,2),math.log(264.914062,2),math.log(236.328125,2),math.log(230.751953,2),math.log(249.452148,2),math.log(254.893555,2),math.log(248.962036,2),math.log(261.232178,2),math.log(271.974457,2)]
t_50 = [math.log(272.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(274.000000,2),math.log(273.000000,2),math.log(235.250000,2),math.log(202.375000,2),math.log(221.625000,2),math.log(218.125000,2),math.log(213.687500,2),math.log(205.234375,2),math.log(225.828125,2),math.log(254.082031,2),math.log(227.078125,2),math.log(237.886230,2),math.log(245.399414,2),math.log(257.693115,2),math.log(255.342163,2),math.log(271.904968,2)]
t_51 = [math.log(272.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(286.000000,2),math.log(280.000000,2),math.log(302.500000,2),math.log(270.000000,2),math.log(283.000000,2),math.log(299.937500,2),math.log(276.656250,2),math.log(283.656250,2),math.log(266.976562,2),math.log(259.542969,2),math.log(256.556641,2),math.log(243.423828,2),math.log(291.457520,2),math.log(259.993896,2),math.log(255.847046,2),math.log(242.612488,2),math.log(253.664337,2)]
t_52 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(282.000000,2),math.log(265.000000,2),math.log(277.500000,2),math.log(284.250000,2),math.log(266.875000,2),math.log(294.062500,2),math.log(278.062500,2),math.log(281.718750,2),math.log(256.742188,2),math.log(223.585938,2),math.log(229.244141,2),math.log(215.012695,2),math.log(230.100586,2),math.log(231.472412,2),math.log(251.348877,2),math.log(231.501465,2),math.log(244.988892,2)]
t_53 = [math.log(224.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(192.000000,2),math.log(222.000000,2),math.log(228.000000,2),math.log(240.500000,2),math.log(265.250000,2),math.log(258.937500,2),math.log(260.750000,2),math.log(260.343750,2),math.log(227.726562,2),math.log(241.859375,2),math.log(231.478516,2),math.log(256.864258,2),math.log(290.719238,2),math.log(282.060059,2),math.log(262.839233,2),math.log(271.814148,2),math.log(261.880859,2)]
t_54 = [math.log(272.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(229.000000,2),math.log(248.500000,2),math.log(235.250000,2),math.log(266.375000,2),math.log(243.312500,2),math.log(230.531250,2),math.log(261.500000,2),math.log(264.679688,2),math.log(259.222656,2),math.log(282.289062,2),math.log(301.394531,2),math.log(246.676758,2),math.log(225.274170,2),math.log(305.297607,2),math.log(277.538086,2),math.log(239.121735,2)]
t_55 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(258.000000,2),math.log(257.500000,2),math.log(236.750000,2),math.log(221.625000,2),math.log(234.375000,2),math.log(277.343750,2),math.log(257.562500,2),math.log(232.539062,2),math.log(225.957031,2),math.log(225.566406,2),math.log(255.461914,2),math.log(237.382324,2),math.log(256.984619,2),math.log(268.439209,2),math.log(231.563477,2),math.log(245.266235,2)]
t_56 = [math.log(256.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(271.000000,2),math.log(255.000000,2),math.log(295.250000,2),math.log(275.625000,2),math.log(286.750000,2),math.log(240.750000,2),math.log(248.937500,2),math.log(245.187500,2),math.log(243.062500,2),math.log(228.679688,2),math.log(259.826172,2),math.log(275.571777,2),math.log(249.755615,2),math.log(235.300781,2),math.log(254.638245,2),math.log(282.273773,2)]
t_57 = [math.log(336.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(274.000000,2),math.log(304.000000,2),math.log(271.500000,2),math.log(267.250000,2),math.log(235.375000,2),math.log(269.500000,2),math.log(270.750000,2),math.log(264.156250,2),math.log(273.773438,2),math.log(257.542969,2),math.log(256.564453,2),math.log(266.593750,2),math.log(257.778809,2),math.log(220.273438,2),math.log(240.262695,2),math.log(273.600464,2),math.log(243.801727,2)]
t_58 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(267.000000,2),math.log(296.000000,2),math.log(247.250000,2),math.log(252.500000,2),math.log(238.812500,2),math.log(230.562500,2),math.log(270.335938,2),math.log(268.566406,2),math.log(296.658203,2),math.log(265.911133,2),math.log(229.697266,2),math.log(223.502197,2),math.log(245.885742,2),math.log(271.505737,2),math.log(266.451752,2)]
t_59 = [math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(248.000000,2),math.log(219.500000,2),math.log(239.250000,2),math.log(259.250000,2),math.log(246.312500,2),math.log(250.765625,2),math.log(226.789062,2),math.log(245.304688,2),math.log(260.857422,2),math.log(287.112305,2),math.log(266.085449,2),math.log(265.609619,2),math.log(276.356934,2),math.log(268.579346,2),math.log(261.323334,2)]
t_60 = [math.log(224.000000,2),math.log(216.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(258.000000,2),math.log(241.000000,2),math.log(269.500000,2),math.log(245.875000,2),math.log(273.625000,2),math.log(264.375000,2),math.log(270.359375,2),math.log(256.179688,2),math.log(242.441406,2),math.log(226.279297,2),math.log(253.948242,2),math.log(239.735840,2),math.log(239.106689,2),math.log(286.155029,2),math.log(258.239807,2),math.log(291.077576,2)]
t_61 = [math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(299.000000,2),math.log(249.000000,2),math.log(274.500000,2),math.log(233.750000,2),math.log(259.687500,2),math.log(260.750000,2),math.log(245.031250,2),math.log(251.140625,2),math.log(250.195312,2),math.log(260.384766,2),math.log(263.333008,2),math.log(258.133301,2),math.log(275.625244,2),math.log(249.635986,2),math.log(239.538940,2),math.log(239.694061,2)]
t_62 = [math.log(256.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(275.000000,2),math.log(284.500000,2),math.log(259.000000,2),math.log(246.375000,2),math.log(250.000000,2),math.log(254.281250,2),math.log(297.484375,2),math.log(255.500000,2),math.log(237.632812,2),math.log(210.484375,2),math.log(227.630859,2),math.log(238.299805,2),math.log(247.155029,2),math.log(237.406372,2),math.log(270.155884,2),math.log(290.309326,2)]
t_63 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(254.000000,2),math.log(273.500000,2),math.log(236.000000,2),math.log(236.625000,2),math.log(237.500000,2),math.log(247.718750,2),math.log(267.734375,2),math.log(250.351562,2),math.log(255.910156,2),math.log(273.484375,2),math.log(265.452148,2),math.log(300.593262,2),math.log(290.848633,2),math.log(266.957520,2),math.log(230.358582,2),math.log(210.349121,2)]
t_64 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(226.000000,2),math.log(219.000000,2),math.log(208.000000,2),math.log(218.000000,2),math.log(258.750000,2),math.log(254.875000,2),math.log(245.093750,2),math.log(249.265625,2),math.log(255.875000,2),math.log(293.203125,2),math.log(278.775391,2),math.log(267.320312,2),math.log(261.984375,2),math.log(266.069580,2),math.log(231.777588,2),math.log(226.676758,2),math.log(281.003937,2)]
t_65 = [math.log(288.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(268.000000,2),math.log(238.000000,2),math.log(261.000000,2),math.log(256.000000,2),math.log(280.875000,2),math.log(255.625000,2),math.log(270.812500,2),math.log(250.453125,2),math.log(258.265625,2),math.log(263.140625,2),math.log(244.802734,2),math.log(250.521484,2),math.log(249.046387,2),math.log(256.775879,2),math.log(246.671021,2),math.log(254.543884,2),math.log(287.204681,2)]
t_66 = [math.log(272.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(240.000000,2),math.log(222.000000,2),math.log(197.000000,2),math.log(237.250000,2),math.log(223.375000,2),math.log(220.187500,2),math.log(201.718750,2),math.log(175.953125,2),math.log(208.023438,2),math.log(245.085938,2),math.log(248.140625,2),math.log(240.076172,2),math.log(230.861328,2),math.log(266.448975,2),math.log(271.221680,2),math.log(295.306641,2),math.log(256.947235,2)]
t_67 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(281.000000,2),math.log(259.500000,2),math.log(255.250000,2),math.log(270.375000,2),math.log(275.812500,2),math.log(259.656250,2),math.log(284.546875,2),math.log(251.718750,2),math.log(242.792969,2),math.log(254.339844,2),math.log(247.210938,2),math.log(224.627930,2),math.log(281.028564,2),math.log(240.742310,2),math.log(226.819763,2),math.log(219.524231,2)]
t_68 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(268.000000,2),math.log(261.000000,2),math.log(286.000000,2),math.log(250.250000,2),math.log(230.625000,2),math.log(255.312500,2),math.log(246.125000,2),math.log(272.421875,2),math.log(273.164062,2),math.log(262.269531,2),math.log(242.685547,2),math.log(261.990234,2),math.log(260.110840,2),math.log(272.563232,2),math.log(262.920776,2),math.log(224.378296,2),math.log(285.764191,2)]
t_69 = [math.log(272.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(266.000000,2),math.log(283.000000,2),math.log(258.000000,2),math.log(274.000000,2),math.log(243.500000,2),math.log(233.312500,2),math.log(233.218750,2),math.log(226.421875,2),math.log(221.929688,2),math.log(242.347656,2),math.log(225.197266,2),math.log(275.481445,2),math.log(221.435059,2),math.log(257.692383,2),math.log(221.980103,2),math.log(231.806763,2),math.log(236.847076,2)]
t_70 = [math.log(224.000000,2),math.log(232.000000,2),math.log(284.000000,2),math.log(284.000000,2),math.log(274.000000,2),math.log(265.000000,2),math.log(247.500000,2),math.log(247.250000,2),math.log(239.875000,2),math.log(274.781250,2),math.log(282.500000,2),math.log(269.132812,2),math.log(266.167969,2),math.log(279.302734,2),math.log(239.441406,2),math.log(259.284668,2),math.log(247.452637,2),math.log(283.675049,2),math.log(242.067322,2),math.log(243.229614,2)]
t_71 = [math.log(240.000000,2),math.log(272.000000,2),math.log(284.000000,2),math.log(268.000000,2),math.log(271.000000,2),math.log(260.000000,2),math.log(241.000000,2),math.log(228.375000,2),math.log(257.500000,2),math.log(272.343750,2),math.log(265.421875,2),math.log(232.187500,2),math.log(229.011719,2),math.log(246.392578,2),math.log(236.361328,2),math.log(253.114258,2),math.log(263.607422,2),math.log(274.456787,2),math.log(295.204529,2),math.log(299.409027,2)]
t_72 = [math.log(304.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(270.000000,2),math.log(270.500000,2),math.log(278.500000,2),math.log(261.625000,2),math.log(280.312500,2),math.log(252.656250,2),math.log(279.546875,2),math.log(299.382812,2),math.log(319.941406,2),math.log(249.162109,2),math.log(299.308594,2),math.log(252.160645,2),math.log(277.179688,2),math.log(268.917236,2),math.log(244.484375,2),math.log(216.186462,2)]
t_73 = [math.log(272.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(233.000000,2),math.log(280.000000,2),math.log(256.750000,2),math.log(261.125000,2),math.log(264.375000,2),math.log(228.531250,2),math.log(273.359375,2),math.log(255.117188,2),math.log(240.207031,2),math.log(245.671875,2),math.log(202.599609,2),math.log(219.303711,2),math.log(234.086914,2),math.log(238.295532,2),math.log(236.725342,2),math.log(276.022125,2)]
t_74 = [math.log(272.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(234.000000,2),math.log(194.000000,2),math.log(224.500000,2),math.log(264.500000,2),math.log(290.750000,2),math.log(243.750000,2),math.log(238.906250,2),math.log(223.812500,2),math.log(229.429688,2),math.log(251.378906,2),math.log(300.431641,2),math.log(291.539062,2),math.log(254.408691,2),math.log(252.493408,2),math.log(275.741455,2),math.log(271.737732,2),math.log(254.461273,2)]
t_75 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(258.000000,2),math.log(288.000000,2),math.log(261.500000,2),math.log(269.750000,2),math.log(279.750000,2),math.log(274.500000,2),math.log(280.531250,2),math.log(292.500000,2),math.log(263.976562,2),math.log(261.519531,2),math.log(263.539062,2),math.log(261.000000,2),math.log(218.443359,2),math.log(219.364014,2),math.log(215.316406,2),math.log(248.054932,2),math.log(231.022217,2)]
t_76 = [math.log(256.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(243.000000,2),math.log(262.500000,2),math.log(246.500000,2),math.log(246.375000,2),math.log(268.062500,2),math.log(236.562500,2),math.log(233.453125,2),math.log(254.054688,2),math.log(257.035156,2),math.log(286.916016,2),math.log(264.656250,2),math.log(259.643066,2),math.log(240.430420,2),math.log(273.056152,2),math.log(303.290344,2),math.log(279.041656,2)]
t_77 = [math.log(272.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(271.000000,2),math.log(253.000000,2),math.log(248.750000,2),math.log(260.250000,2),math.log(260.187500,2),math.log(283.437500,2),math.log(341.625000,2),math.log(301.593750,2),math.log(271.828125,2),math.log(262.927734,2),math.log(286.072266,2),math.log(280.300781,2),math.log(252.764893,2),math.log(212.527466,2),math.log(224.396606,2),math.log(243.941040,2)]
t_78 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(230.000000,2),math.log(267.000000,2),math.log(251.000000,2),math.log(228.500000,2),math.log(209.250000,2),math.log(216.062500,2),math.log(269.218750,2),math.log(260.515625,2),math.log(292.914062,2),math.log(284.761719,2),math.log(282.873047,2),math.log(272.419922,2),math.log(271.155762,2),math.log(247.964600,2),math.log(254.667358,2),math.log(253.878540,2),math.log(295.879364,2)]
t_79 = [math.log(240.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(279.000000,2),math.log(262.500000,2),math.log(276.500000,2),math.log(293.875000,2),math.log(285.625000,2),math.log(274.250000,2),math.log(273.265625,2),math.log(271.492188,2),math.log(253.289062,2),math.log(263.777344,2),math.log(262.759766,2),math.log(292.324707,2),math.log(280.974121,2),math.log(317.351318,2),math.log(265.247192,2),math.log(269.615662,2)]
t_80 = [math.log(240.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(249.000000,2),math.log(225.000000,2),math.log(241.250000,2),math.log(238.625000,2),math.log(285.562500,2),math.log(280.187500,2),math.log(293.078125,2),math.log(254.695312,2),math.log(274.996094,2),math.log(248.371094,2),math.log(270.027344,2),math.log(273.489746,2),math.log(287.678711,2),math.log(277.671265,2),math.log(268.700012,2),math.log(290.976868,2)]
t_81 = [math.log(240.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(251.000000,2),math.log(251.000000,2),math.log(270.250000,2),math.log(245.750000,2),math.log(291.375000,2),math.log(296.437500,2),math.log(251.546875,2),math.log(264.476562,2),math.log(247.968750,2),math.log(228.279297,2),math.log(206.633789,2),math.log(222.195801,2),math.log(225.449219,2),math.log(229.959839,2),math.log(254.987244,2),math.log(258.036560,2)]
t_82 = [math.log(272.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(255.000000,2),math.log(265.500000,2),math.log(263.250000,2),math.log(270.125000,2),math.log(255.687500,2),math.log(263.656250,2),math.log(233.546875,2),math.log(245.296875,2),math.log(248.718750,2),math.log(240.324219,2),math.log(237.031250,2),math.log(241.303223,2),math.log(226.418701,2),math.log(221.791382,2),math.log(232.419678,2),math.log(230.111664,2)]
t_83 = [math.log(288.000000,2),math.log(248.000000,2),math.log(288.000000,2),math.log(230.000000,2),math.log(220.000000,2),math.log(270.500000,2),math.log(259.500000,2),math.log(239.125000,2),math.log(208.812500,2),math.log(211.062500,2),math.log(223.296875,2),math.log(194.273438,2),math.log(204.703125,2),math.log(252.662109,2),math.log(246.096680,2),math.log(248.276855,2),math.log(252.697021,2),math.log(283.030518,2),math.log(262.191650,2),math.log(230.863983,2)]
t_84 = [math.log(272.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(220.000000,2),math.log(259.000000,2),math.log(263.000000,2),math.log(242.750000,2),math.log(222.250000,2),math.log(252.312500,2),math.log(235.625000,2),math.log(265.500000,2),math.log(279.695312,2),math.log(246.687500,2),math.log(205.804688,2),math.log(205.582031,2),math.log(218.647949,2),math.log(271.500488,2),math.log(310.045166,2),math.log(328.943787,2),math.log(237.452850,2)]
t_85 = [math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(230.000000,2),math.log(260.500000,2),math.log(301.000000,2),math.log(254.125000,2),math.log(279.062500,2),math.log(243.656250,2),math.log(250.656250,2),math.log(237.796875,2),math.log(244.906250,2),math.log(256.222656,2),math.log(272.493164,2),math.log(236.747070,2),math.log(278.429443,2),math.log(264.215088,2),math.log(281.570496,2),math.log(269.857666,2)]
t_86 = [math.log(240.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(286.000000,2),math.log(306.000000,2),math.log(279.500000,2),math.log(259.000000,2),math.log(227.250000,2),math.log(232.187500,2),math.log(247.656250,2),math.log(261.468750,2),math.log(248.773438,2),math.log(254.449219,2),math.log(266.025391,2),math.log(244.987305,2),math.log(264.869629,2),math.log(263.651123,2),math.log(287.044067,2),math.log(286.183044,2),math.log(267.391998,2)]
t_87 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(232.000000,2),math.log(288.000000,2),math.log(252.500000,2),math.log(247.375000,2),math.log(247.843750,2),math.log(228.593750,2),math.log(255.601562,2),math.log(261.152344,2),math.log(266.427734,2),math.log(257.562500,2),math.log(249.103516,2),math.log(224.797363,2),math.log(235.177368,2),math.log(271.320251,2),math.log(272.461548,2)]
t_88 = [math.log(272.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(239.000000,2),math.log(272.500000,2),math.log(295.000000,2),math.log(284.375000,2),math.log(286.000000,2),math.log(286.187500,2),math.log(244.250000,2),math.log(222.804688,2),math.log(259.972656,2),math.log(284.535156,2),math.log(284.385742,2),math.log(281.800293,2),math.log(272.594971,2),math.log(274.079224,2),math.log(258.807922,2),math.log(272.528137,2)]
t_89 = [math.log(224.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(306.000000,2),math.log(290.000000,2),math.log(255.000000,2),math.log(254.375000,2),math.log(226.937500,2),math.log(231.625000,2),math.log(247.750000,2),math.log(233.531250,2),math.log(245.839844,2),math.log(249.763672,2),math.log(261.155273,2),math.log(265.137695,2),math.log(268.706787,2),math.log(226.526245,2),math.log(258.374817,2),math.log(299.962585,2)]
t_90 = [math.log(240.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(232.000000,2),math.log(237.000000,2),math.log(266.000000,2),math.log(239.750000,2),math.log(253.625000,2),math.log(299.312500,2),math.log(280.250000,2),math.log(271.250000,2),math.log(277.335938,2),math.log(253.175781,2),math.log(284.591797,2),math.log(303.305664,2),math.log(300.141602,2),math.log(270.486084,2),math.log(241.380737,2),math.log(254.191650,2),math.log(232.614502,2)]
t_91 = [math.log(256.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(260.000000,2),math.log(221.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(260.250000,2),math.log(268.312500,2),math.log(283.406250,2),math.log(278.437500,2),math.log(234.273438,2),math.log(222.843750,2),math.log(215.076172,2),math.log(224.153320,2),math.log(235.181641,2),math.log(248.923828,2),math.log(266.533203,2),math.log(259.920776,2),math.log(250.085052,2)]
t_92 = [math.log(240.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(222.000000,2),math.log(241.000000,2),math.log(270.000000,2),math.log(246.750000,2),math.log(230.000000,2),math.log(246.500000,2),math.log(222.750000,2),math.log(219.406250,2),math.log(228.226562,2),math.log(223.472656,2),math.log(224.341797,2),math.log(233.132812,2),math.log(233.948242,2),math.log(261.504150,2),math.log(238.264771,2),math.log(257.702271,2),math.log(261.767181,2)]
t_93 = [math.log(272.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(212.000000,2),math.log(222.000000,2),math.log(243.500000,2),math.log(258.000000,2),math.log(262.875000,2),math.log(271.687500,2),math.log(280.156250,2),math.log(238.625000,2),math.log(293.632812,2),math.log(253.027344,2),math.log(240.789062,2),math.log(297.853516,2),math.log(291.970215,2),math.log(334.008301,2),math.log(290.999146,2),math.log(258.355957,2),math.log(229.730774,2)]
t_94 = [math.log(272.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(240.000000,2),math.log(257.000000,2),math.log(257.875000,2),math.log(211.875000,2),math.log(201.687500,2),math.log(237.515625,2),math.log(252.554688,2),math.log(243.125000,2),math.log(278.939453,2),math.log(255.302734,2),math.log(231.756836,2),math.log(211.024902,2),math.log(240.388184,2),math.log(230.666260,2),math.log(218.661682,2)]
t_95 = [math.log(224.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(277.500000,2),math.log(270.750000,2),math.log(276.687500,2),math.log(299.281250,2),math.log(263.250000,2),math.log(250.640625,2),math.log(263.312500,2),math.log(270.007812,2),math.log(263.682617,2),math.log(257.520508,2),math.log(234.310547,2),math.log(230.792725,2),math.log(247.376343,2),math.log(262.858612,2)]
t_96 = [math.log(240.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(276.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(259.750000,2),math.log(253.875000,2),math.log(288.062500,2),math.log(276.875000,2),math.log(239.078125,2),math.log(262.609375,2),math.log(249.164062,2),math.log(235.296875,2),math.log(243.746094,2),math.log(245.731934,2),math.log(252.741699,2),math.log(264.464478,2),math.log(280.451294,2),math.log(317.362701,2)]
t_97 = [math.log(224.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(276.000000,2),math.log(281.000000,2),math.log(307.000000,2),math.log(267.250000,2),math.log(231.500000,2),math.log(242.687500,2),math.log(225.531250,2),math.log(248.234375,2),math.log(251.429688,2),math.log(221.046875,2),math.log(250.994141,2),math.log(250.138672,2),math.log(215.956543,2),math.log(250.657715,2),math.log(243.851929,2),math.log(235.206177,2),math.log(266.608551,2)]
t_98 = [math.log(224.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(222.000000,2),math.log(231.000000,2),math.log(286.000000,2),math.log(256.750000,2),math.log(233.375000,2),math.log(248.562500,2),math.log(266.281250,2),math.log(247.625000,2),math.log(237.796875,2),math.log(219.816406,2),math.log(225.933594,2),math.log(231.261719,2),math.log(248.384277,2),math.log(277.667969,2),math.log(264.341919,2),math.log(266.503540,2),math.log(283.827423,2)]
t_99 = [math.log(272.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(293.000000,2),math.log(287.000000,2),math.log(258.500000,2),math.log(277.625000,2),math.log(304.500000,2),math.log(289.031250,2),math.log(246.500000,2),math.log(224.882812,2),math.log(232.492188,2),math.log(209.007812,2),math.log(222.820312,2),math.log(279.098633,2),math.log(260.741943,2),math.log(275.837402,2),math.log(241.938110,2),math.log(252.443451,2)]
t_100 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(308.000000,2),math.log(312.000000,2),math.log(275.500000,2),math.log(240.250000,2),math.log(242.125000,2),math.log(238.812500,2),math.log(230.843750,2),math.log(225.468750,2),math.log(212.914062,2),math.log(209.097656,2),math.log(238.511719,2),math.log(273.572266,2),math.log(284.373047,2),math.log(261.318604,2),math.log(248.604248,2),math.log(268.251038,2),math.log(255.908264,2)]
t_101 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(305.000000,2),math.log(288.250000,2),math.log(272.875000,2),math.log(270.125000,2),math.log(301.718750,2),math.log(317.046875,2),math.log(252.210938,2),math.log(276.917969,2),math.log(297.714844,2),math.log(298.746094,2),math.log(249.003418,2),math.log(220.713135,2),math.log(218.497925,2),math.log(212.090515,2),math.log(271.055511,2)]
t_102 = [math.log(288.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(254.000000,2),math.log(275.000000,2),math.log(268.000000,2),math.log(279.500000,2),math.log(264.125000,2),math.log(256.812500,2),math.log(257.343750,2),math.log(237.359375,2),math.log(228.742188,2),math.log(231.164062,2),math.log(269.546875,2),math.log(266.492188,2),math.log(241.099121,2),math.log(306.670166,2),math.log(268.796143,2),math.log(233.488342,2),math.log(268.187469,2)]
t_103 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(286.000000,2),math.log(273.000000,2),math.log(266.000000,2),math.log(263.500000,2),math.log(281.250000,2),math.log(238.125000,2),math.log(229.500000,2),math.log(266.312500,2),math.log(231.507812,2),math.log(284.644531,2),math.log(252.853516,2),math.log(254.417969,2),math.log(258.672363,2),math.log(265.512939,2),math.log(265.476562,2),math.log(258.798523,2),math.log(239.131561,2)]
t_104 = [math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(277.500000,2),math.log(266.000000,2),math.log(280.875000,2),math.log(298.750000,2),math.log(333.281250,2),math.log(283.296875,2),math.log(259.718750,2),math.log(277.816406,2),math.log(239.246094,2),math.log(267.574219,2),math.log(249.059570,2),math.log(282.788818,2),math.log(248.711792,2),math.log(256.345642,2),math.log(253.610962,2)]
t_105 = [math.log(272.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(230.000000,2),math.log(213.000000,2),math.log(239.000000,2),math.log(252.500000,2),math.log(276.875000,2),math.log(264.125000,2),math.log(281.406250,2),math.log(308.156250,2),math.log(304.882812,2),math.log(299.589844,2),math.log(261.595703,2),math.log(267.365234,2),math.log(268.057129,2),math.log(277.822754,2),math.log(246.457153,2),math.log(244.734314,2),math.log(253.399902,2)]
t_106 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(252.000000,2),math.log(280.000000,2),math.log(291.750000,2),math.log(262.750000,2),math.log(278.500000,2),math.log(236.031250,2),math.log(236.828125,2),math.log(214.289062,2),math.log(215.984375,2),math.log(197.755859,2),math.log(235.965820,2),math.log(254.608398,2),math.log(249.095947,2),math.log(297.292725,2),math.log(312.324280,2),math.log(295.118408,2)]
t_107 = [math.log(240.000000,2),math.log(280.000000,2),math.log(292.000000,2),math.log(282.000000,2),math.log(249.000000,2),math.log(251.000000,2),math.log(221.750000,2),math.log(245.750000,2),math.log(241.062500,2),math.log(258.250000,2),math.log(234.562500,2),math.log(251.679688,2),math.log(269.351562,2),math.log(272.835938,2),math.log(270.572266,2),math.log(270.470703,2),math.log(267.929199,2),math.log(264.917480,2),math.log(284.016907,2),math.log(245.285858,2)]
t_108 = [math.log(272.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(227.000000,2),math.log(262.500000,2),math.log(262.000000,2),math.log(268.875000,2),math.log(259.062500,2),math.log(273.687500,2),math.log(301.296875,2),math.log(254.093750,2),math.log(270.527344,2),math.log(275.583984,2),math.log(272.837891,2),math.log(252.484375,2),math.log(238.428711,2),math.log(269.412720,2),math.log(243.156555,2),math.log(264.727905,2)]
t_109 = [math.log(256.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(240.000000,2),math.log(234.500000,2),math.log(240.000000,2),math.log(269.000000,2),math.log(253.750000,2),math.log(223.375000,2),math.log(211.687500,2),math.log(228.000000,2),math.log(239.964844,2),math.log(251.675781,2),math.log(237.321289,2),math.log(276.567383,2),math.log(262.096680,2),math.log(263.080688,2),math.log(236.636597,2),math.log(224.465515,2)]
t_110 = [math.log(224.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(224.000000,2),math.log(230.000000,2),math.log(208.000000,2),math.log(270.250000,2),math.log(252.125000,2),math.log(259.125000,2),math.log(308.437500,2),math.log(276.546875,2),math.log(278.679688,2),math.log(240.964844,2),math.log(256.185547,2),math.log(274.727539,2),math.log(241.234863,2),math.log(257.244873,2),math.log(269.337891,2),math.log(250.489868,2),math.log(266.073486,2)]
t_111 = [math.log(272.000000,2),math.log(336.000000,2),math.log(292.000000,2),math.log(276.000000,2),math.log(306.000000,2),math.log(275.500000,2),math.log(267.500000,2),math.log(268.875000,2),math.log(290.562500,2),math.log(304.187500,2),math.log(265.187500,2),math.log(276.000000,2),math.log(263.296875,2),math.log(264.009766,2),math.log(261.187500,2),math.log(290.943848,2),math.log(271.623779,2),math.log(252.805054,2),math.log(288.641296,2),math.log(262.966980,2)]
t_112 = [math.log(224.000000,2),math.log(296.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(273.500000,2),math.log(273.250000,2),math.log(268.250000,2),math.log(274.250000,2),math.log(254.937500,2),math.log(237.906250,2),math.log(216.234375,2),math.log(198.082031,2),math.log(241.457031,2),math.log(276.210938,2),math.log(240.855469,2),math.log(244.040283,2),math.log(274.879639,2),math.log(270.563477,2),math.log(282.006927,2)]
t_113 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(270.000000,2),math.log(271.000000,2),math.log(249.000000,2),math.log(240.750000,2),math.log(262.500000,2),math.log(218.000000,2),math.log(205.343750,2),math.log(272.671875,2),math.log(253.195312,2),math.log(243.113281,2),math.log(239.873047,2),math.log(241.087891,2),math.log(289.078125,2),math.log(294.259033,2),math.log(243.204224,2),math.log(273.947510,2),math.log(272.261353,2)]
t_114 = [math.log(224.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(247.000000,2),math.log(241.500000,2),math.log(265.500000,2),math.log(300.750000,2),math.log(280.812500,2),math.log(268.500000,2),math.log(268.343750,2),math.log(265.015625,2),math.log(258.792969,2),math.log(278.599609,2),math.log(268.575195,2),math.log(259.950195,2),math.log(286.082520,2),math.log(264.940186,2),math.log(234.515381,2),math.log(230.562531,2)]
t_115 = [math.log(288.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(266.000000,2),math.log(245.000000,2),math.log(255.500000,2),math.log(252.000000,2),math.log(230.625000,2),math.log(196.562500,2),math.log(241.718750,2),math.log(234.109375,2),math.log(270.468750,2),math.log(257.945312,2),math.log(253.955078,2),math.log(244.089844,2),math.log(239.553711,2),math.log(269.917236,2),math.log(273.954590,2),math.log(297.790833,2),math.log(303.203003,2)]
t_116 = [math.log(224.000000,2),math.log(208.000000,2),math.log(224.000000,2),math.log(266.000000,2),math.log(237.000000,2),math.log(256.500000,2),math.log(287.500000,2),math.log(267.625000,2),math.log(268.812500,2),math.log(259.656250,2),math.log(223.984375,2),math.log(257.664062,2),math.log(237.125000,2),math.log(223.960938,2),math.log(234.988281,2),math.log(247.896484,2),math.log(248.168457,2),math.log(265.001221,2),math.log(257.984802,2),math.log(245.906311,2)]
t_117 = [math.log(272.000000,2),math.log(272.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(242.250000,2),math.log(235.250000,2),math.log(264.375000,2),math.log(297.750000,2),math.log(274.671875,2),math.log(257.656250,2),math.log(258.292969,2),math.log(249.414062,2),math.log(260.013672,2),math.log(221.601074,2),math.log(231.507080,2),math.log(262.305786,2),math.log(228.476257,2),math.log(275.829102,2)]
t_118 = [math.log(240.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(276.000000,2),math.log(237.000000,2),math.log(238.500000,2),math.log(245.250000,2),math.log(258.000000,2),math.log(290.625000,2),math.log(231.031250,2),math.log(238.515625,2),math.log(251.656250,2),math.log(255.132812,2),math.log(267.826172,2),math.log(227.345703,2),math.log(210.057129,2),math.log(251.575439,2),math.log(270.801758,2),math.log(263.033875,2),math.log(228.140442,2)]
t_119 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(270.000000,2),math.log(296.500000,2),math.log(247.000000,2),math.log(209.625000,2),math.log(234.187500,2),math.log(227.875000,2),math.log(214.921875,2),math.log(237.234375,2),math.log(253.277344,2),math.log(266.279297,2),math.log(258.819336,2),math.log(278.383301,2),math.log(253.281250,2),math.log(254.555054,2),math.log(276.505310,2),math.log(293.766022,2)]
t_120 = [math.log(224.000000,2),math.log(240.000000,2),math.log(288.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(270.000000,2),math.log(264.000000,2),math.log(262.125000,2),math.log(257.250000,2),math.log(252.218750,2),math.log(242.140625,2),math.log(263.210938,2),math.log(240.363281,2),math.log(251.181641,2),math.log(251.978516,2),math.log(269.405762,2),math.log(268.647949,2),math.log(260.724243,2),math.log(230.999695,2),math.log(239.610291,2)]
t_121 = [math.log(224.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(238.000000,2),math.log(267.000000,2),math.log(268.000000,2),math.log(273.250000,2),math.log(259.250000,2),math.log(264.625000,2),math.log(261.187500,2),math.log(246.375000,2),math.log(207.359375,2),math.log(217.871094,2),math.log(223.888672,2),math.log(245.350586,2),math.log(253.346680,2),math.log(256.573975,2),math.log(257.211670,2),math.log(267.599060,2),math.log(258.955933,2)]
t_122 = [math.log(272.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(266.000000,2),math.log(274.000000,2),math.log(257.500000,2),math.log(271.250000,2),math.log(251.500000,2),math.log(232.437500,2),math.log(242.312500,2),math.log(231.000000,2),math.log(278.015625,2),math.log(282.523438,2),math.log(261.871094,2),math.log(252.079102,2),math.log(273.246582,2),math.log(295.211426,2),math.log(300.991089,2),math.log(261.185181,2),math.log(306.032990,2)]
t_123 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(262.000000,2),math.log(288.500000,2),math.log(283.000000,2),math.log(245.500000,2),math.log(262.875000,2),math.log(272.218750,2),math.log(287.875000,2),math.log(263.640625,2),math.log(257.714844,2),math.log(274.744141,2),math.log(251.148438,2),math.log(289.734375,2),math.log(259.669189,2),math.log(267.455200,2),math.log(275.884705,2),math.log(269.082275,2)]
t_124 = [math.log(320.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(224.000000,2),math.log(224.500000,2),math.log(267.000000,2),math.log(256.125000,2),math.log(275.437500,2),math.log(252.968750,2),math.log(272.765625,2),math.log(257.328125,2),math.log(270.523438,2),math.log(238.757812,2),math.log(237.985352,2),math.log(256.822754,2),math.log(256.807617,2),math.log(264.436523,2),math.log(259.740967,2),math.log(309.483795,2)]
t_125 = [math.log(304.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(266.000000,2),math.log(271.000000,2),math.log(218.500000,2),math.log(227.250000,2),math.log(267.875000,2),math.log(331.375000,2),math.log(303.031250,2),math.log(266.250000,2),math.log(250.070312,2),math.log(238.484375,2),math.log(243.441406,2),math.log(219.186523,2),math.log(224.487305,2),math.log(237.047852,2),math.log(241.061768,2),math.log(236.548889,2),math.log(267.003235,2)]
t_126 = [math.log(256.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(281.500000,2),math.log(265.500000,2),math.log(272.375000,2),math.log(279.437500,2),math.log(270.656250,2),math.log(248.828125,2),math.log(237.968750,2),math.log(250.699219,2),math.log(236.615234,2),math.log(264.157227,2),math.log(274.516602,2),math.log(247.286133,2),math.log(252.468506,2),math.log(250.022461,2),math.log(280.980927,2)]
t_127 = [math.log(256.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(298.000000,2),math.log(279.000000,2),math.log(256.000000,2),math.log(280.250000,2),math.log(278.000000,2),math.log(242.312500,2),math.log(244.750000,2),math.log(241.656250,2),math.log(247.062500,2),math.log(230.097656,2),math.log(254.070312,2),math.log(220.029297,2),math.log(239.146484,2),math.log(265.781982,2),math.log(240.439819,2),math.log(228.364380,2),math.log(243.002838,2)]
t_128 = [math.log(256.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(300.000000,2),math.log(278.000000,2),math.log(273.500000,2),math.log(266.000000,2),math.log(232.375000,2),math.log(246.125000,2),math.log(279.875000,2),math.log(255.312500,2),math.log(254.140625,2),math.log(230.136719,2),math.log(221.042969,2),math.log(230.758789,2),math.log(254.911621,2),math.log(268.152588,2),math.log(269.537598,2),math.log(235.668884,2),math.log(231.391693,2)]
t_129 = [math.log(272.000000,2),math.log(280.000000,2),math.log(300.000000,2),math.log(280.000000,2),math.log(258.000000,2),math.log(268.000000,2),math.log(230.250000,2),math.log(235.000000,2),math.log(267.000000,2),math.log(254.062500,2),math.log(283.687500,2),math.log(303.203125,2),math.log(240.625000,2),math.log(269.054688,2),math.log(257.189453,2),math.log(246.830566,2),math.log(223.912109,2),math.log(268.213013,2),math.log(262.554077,2),math.log(257.349945,2)]
t_130 = [math.log(240.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(249.000000,2),math.log(242.000000,2),math.log(233.500000,2),math.log(227.000000,2),math.log(259.812500,2),math.log(263.750000,2),math.log(250.140625,2),math.log(221.070312,2),math.log(264.769531,2),math.log(284.800781,2),math.log(268.346680,2),math.log(253.617188,2),math.log(228.548096,2),math.log(245.994873,2),math.log(270.174377,2),math.log(258.515320,2)]
t_131 = [math.log(240.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(224.000000,2),math.log(266.500000,2),math.log(262.500000,2),math.log(254.125000,2),math.log(247.000000,2),math.log(267.437500,2),math.log(258.000000,2),math.log(246.781250,2),math.log(244.378906,2),math.log(243.492188,2),math.log(256.428711,2),math.log(243.894531,2),math.log(237.710938,2),math.log(246.358643,2),math.log(257.770996,2),math.log(267.038055,2)]
t_132 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(260.000000,2),math.log(271.000000,2),math.log(302.000000,2),math.log(250.500000,2),math.log(225.000000,2),math.log(256.687500,2),math.log(288.718750,2),math.log(284.656250,2),math.log(279.343750,2),math.log(279.031250,2),math.log(269.650391,2),math.log(275.983398,2),math.log(290.412109,2),math.log(283.673584,2),math.log(260.147339,2),math.log(266.366882,2),math.log(281.864044,2)]
t_133 = [math.log(272.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(217.000000,2),math.log(236.500000,2),math.log(223.750000,2),math.log(253.000000,2),math.log(262.687500,2),math.log(234.625000,2),math.log(240.640625,2),math.log(248.093750,2),math.log(273.449219,2),math.log(296.753906,2),math.log(297.425781,2),math.log(267.816895,2),math.log(255.286133,2),math.log(260.181030,2),math.log(249.983948,2),math.log(232.782410,2)]
t_134 = [math.log(272.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(239.000000,2),math.log(285.000000,2),math.log(266.000000,2),math.log(233.500000,2),math.log(247.562500,2),math.log(301.156250,2),math.log(275.515625,2),math.log(285.390625,2),math.log(270.347656,2),math.log(256.589844,2),math.log(241.334961,2),math.log(282.377930,2),math.log(241.585693,2),math.log(257.911865,2),math.log(272.962891,2),math.log(284.953613,2)]
t_135 = [math.log(240.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(251.500000,2),math.log(245.750000,2),math.log(212.375000,2),math.log(240.687500,2),math.log(259.812500,2),math.log(232.687500,2),math.log(235.718750,2),math.log(269.628906,2),math.log(248.375000,2),math.log(253.409180,2),math.log(230.239258,2),math.log(251.871094,2),math.log(276.493286,2),math.log(247.385925,2),math.log(226.957703,2)]
t_136 = [math.log(272.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(285.000000,2),math.log(282.000000,2),math.log(244.750000,2),math.log(268.250000,2),math.log(271.625000,2),math.log(260.468750,2),math.log(231.859375,2),math.log(236.671875,2),math.log(225.914062,2),math.log(197.925781,2),math.log(207.293945,2),math.log(212.369141,2),math.log(224.496338,2),math.log(231.361206,2),math.log(264.581665,2),math.log(247.832153,2)]
t_137 = [math.log(240.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(258.500000,2),math.log(229.250000,2),math.log(250.500000,2),math.log(284.000000,2),math.log(262.062500,2),math.log(219.781250,2),math.log(259.796875,2),math.log(265.367188,2),math.log(239.691406,2),math.log(257.196289,2),math.log(261.812500,2),math.log(256.531250,2),math.log(273.893311,2),math.log(255.548950,2),math.log(226.453033,2)]
t_138 = [math.log(256.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(282.000000,2),math.log(274.000000,2),math.log(226.000000,2),math.log(226.500000,2),math.log(265.625000,2),math.log(242.187500,2),math.log(233.781250,2),math.log(218.578125,2),math.log(215.281250,2),math.log(221.371094,2),math.log(246.705078,2),math.log(211.768555,2),math.log(236.845215,2),math.log(234.496582,2),math.log(203.048218,2),math.log(268.324036,2),math.log(252.764771,2)]
t_139 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(247.500000,2),math.log(221.500000,2),math.log(247.750000,2),math.log(256.875000,2),math.log(273.843750,2),math.log(284.625000,2),math.log(290.007812,2),math.log(253.867188,2),math.log(263.583984,2),math.log(271.122070,2),math.log(244.640137,2),math.log(275.429932,2),math.log(259.830444,2),math.log(234.039917,2),math.log(213.034637,2)]
t_140 = [math.log(320.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(264.250000,2),math.log(268.375000,2),math.log(263.312500,2),math.log(293.031250,2),math.log(276.890625,2),math.log(232.117188,2),math.log(288.265625,2),math.log(305.501953,2),math.log(301.660156,2),math.log(282.516113,2),math.log(242.230225,2),math.log(239.520508,2),math.log(237.382202,2),math.log(231.452087,2)]
t_141 = [math.log(240.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(238.000000,2),math.log(269.500000,2),math.log(258.000000,2),math.log(277.250000,2),math.log(281.375000,2),math.log(253.781250,2),math.log(265.968750,2),math.log(271.281250,2),math.log(217.089844,2),math.log(257.636719,2),math.log(268.978516,2),math.log(245.999512,2),math.log(259.038086,2),math.log(253.304810,2),math.log(252.262024,2),math.log(225.780609,2)]
t_142 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(219.000000,2),math.log(237.000000,2),math.log(233.250000,2),math.log(211.625000,2),math.log(264.750000,2),math.log(246.000000,2),math.log(246.796875,2),math.log(276.554688,2),math.log(275.468750,2),math.log(245.810547,2),math.log(221.183594,2),math.log(209.020996,2),math.log(239.377441,2),math.log(272.697510,2),math.log(305.969360,2),math.log(307.886688,2)]
t_143 = [math.log(240.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(234.000000,2),math.log(273.000000,2),math.log(271.000000,2),math.log(281.500000,2),math.log(232.375000,2),math.log(217.687500,2),math.log(215.406250,2),math.log(235.390625,2),math.log(230.742188,2),math.log(254.449219,2),math.log(254.095703,2),math.log(267.011719,2),math.log(275.256836,2),math.log(314.462891,2),math.log(282.314697,2),math.log(269.912354,2),math.log(269.061371,2)]
t_144 = [math.log(288.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(249.000000,2),math.log(261.500000,2),math.log(247.250000,2),math.log(236.125000,2),math.log(253.125000,2),math.log(237.625000,2),math.log(218.671875,2),math.log(233.375000,2),math.log(243.000000,2),math.log(261.896484,2),math.log(226.389648,2),math.log(251.699707,2),math.log(256.026611,2),math.log(276.933594,2),math.log(242.476746,2),math.log(264.364990,2)]
t_145 = [math.log(272.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(256.000000,2),math.log(250.500000,2),math.log(290.750000,2),math.log(284.375000,2),math.log(306.812500,2),math.log(317.375000,2),math.log(266.875000,2),math.log(239.843750,2),math.log(246.273438,2),math.log(265.695312,2),math.log(262.895508,2),math.log(255.491211,2),math.log(256.846924,2),math.log(242.048706,2),math.log(244.157043,2),math.log(273.251740,2)]
t_146 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(226.500000,2),math.log(282.500000,2),math.log(305.625000,2),math.log(278.250000,2),math.log(284.343750,2),math.log(256.453125,2),math.log(263.515625,2),math.log(236.691406,2),math.log(245.603516,2),math.log(257.347656,2),math.log(261.336426,2),math.log(265.164795,2),math.log(278.440552,2),math.log(246.730835,2),math.log(263.262390,2)]
t_147 = [math.log(240.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(316.000000,2),math.log(267.500000,2),math.log(241.500000,2),math.log(244.750000,2),math.log(279.125000,2),math.log(246.718750,2),math.log(237.859375,2),math.log(264.742188,2),math.log(281.050781,2),math.log(280.003906,2),math.log(242.078125,2),math.log(235.166992,2),math.log(232.107910,2),math.log(226.104858,2),math.log(251.853699,2),math.log(273.207031,2)]
t_148 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(241.000000,2),math.log(265.000000,2),math.log(272.250000,2),math.log(272.250000,2),math.log(254.000000,2),math.log(240.656250,2),math.log(256.437500,2),math.log(232.007812,2),math.log(262.945312,2),math.log(291.978516,2),math.log(274.958984,2),math.log(250.422363,2),math.log(230.452637,2),math.log(234.029541,2),math.log(196.475281,2),math.log(192.350952,2)]
t_149 = [math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(268.000000,2),math.log(259.000000,2),math.log(252.000000,2),math.log(223.250000,2),math.log(263.375000,2),math.log(275.000000,2),math.log(255.843750,2),math.log(280.093750,2),math.log(274.585938,2),math.log(276.144531,2),math.log(264.849609,2),math.log(267.409180,2),math.log(262.051270,2),math.log(235.168213,2),math.log(270.656006,2),math.log(275.301147,2),math.log(262.567932,2)]
t_150 = [math.log(240.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(257.000000,2),math.log(282.000000,2),math.log(240.500000,2),math.log(216.750000,2),math.log(235.375000,2),math.log(248.781250,2),math.log(226.000000,2),math.log(248.843750,2),math.log(240.902344,2),math.log(265.396484,2),math.log(252.644531,2),math.log(294.122070,2),math.log(297.371826,2),math.log(266.477051,2),math.log(283.946228,2),math.log(257.346252,2)]
t_151 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(278.000000,2),math.log(268.000000,2),math.log(273.000000,2),math.log(273.000000,2),math.log(253.375000,2),math.log(214.312500,2),math.log(243.718750,2),math.log(256.093750,2),math.log(266.320312,2),math.log(297.003906,2),math.log(267.664062,2),math.log(274.779297,2),math.log(258.953125,2),math.log(249.726318,2),math.log(221.870361,2),math.log(228.659851,2),math.log(267.893372,2)]
t_152 = [math.log(256.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(280.000000,2),math.log(275.000000,2),math.log(262.750000,2),math.log(243.125000,2),math.log(259.875000,2),math.log(271.906250,2),math.log(251.343750,2),math.log(250.539062,2),math.log(226.488281,2),math.log(226.062500,2),math.log(230.431641,2),math.log(212.525879,2),math.log(235.110352,2),math.log(239.508911,2),math.log(252.819336,2),math.log(315.573395,2)]
t_153 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(324.500000,2),math.log(289.000000,2),math.log(259.250000,2),math.log(234.062500,2),math.log(235.187500,2),math.log(262.890625,2),math.log(249.539062,2),math.log(252.289062,2),math.log(255.830078,2),math.log(239.602539,2),math.log(289.345215,2),math.log(314.423828,2),math.log(274.022461,2),math.log(237.619995,2),math.log(241.049316,2)]
t_154 = [math.log(272.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(247.000000,2),math.log(248.500000,2),math.log(188.750000,2),math.log(200.000000,2),math.log(229.125000,2),math.log(236.000000,2),math.log(242.500000,2),math.log(266.234375,2),math.log(252.042969,2),math.log(228.060547,2),math.log(241.111328,2),math.log(249.108887,2),math.log(278.443359,2),math.log(268.184814,2),math.log(262.296082,2),math.log(246.367310,2)]
t_155 = [math.log(256.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(261.500000,2),math.log(256.500000,2),math.log(237.750000,2),math.log(235.625000,2),math.log(280.750000,2),math.log(264.187500,2),math.log(268.437500,2),math.log(262.621094,2),math.log(257.238281,2),math.log(273.186523,2),math.log(265.655762,2),math.log(259.571045,2),math.log(224.356079,2),math.log(251.173340,2),math.log(242.835663,2)]
t_156 = [math.log(224.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(274.000000,2),math.log(278.000000,2),math.log(274.500000,2),math.log(260.000000,2),math.log(234.875000,2),math.log(233.250000,2),math.log(226.031250,2),math.log(273.265625,2),math.log(274.648438,2),math.log(293.214844,2),math.log(293.804688,2),math.log(274.009766,2),math.log(276.533203,2),math.log(269.406982,2),math.log(254.172485,2),math.log(235.043091,2),math.log(232.490601,2)]
t_157 = [math.log(304.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(306.000000,2),math.log(301.000000,2),math.log(269.000000,2),math.log(282.500000,2),math.log(287.125000,2),math.log(264.187500,2),math.log(225.062500,2),math.log(233.984375,2),math.log(246.570312,2),math.log(234.753906,2),math.log(250.484375,2),math.log(244.789062,2),math.log(250.802734,2),math.log(277.639648,2),math.log(245.430054,2),math.log(234.403381,2),math.log(253.006989,2)]
t_158 = [math.log(240.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(254.000000,2),math.log(298.000000,2),math.log(314.500000,2),math.log(300.875000,2),math.log(243.750000,2),math.log(243.437500,2),math.log(238.343750,2),math.log(255.351562,2),math.log(260.980469,2),math.log(249.710938,2),math.log(279.389648,2),math.log(262.086914,2),math.log(238.112549,2),math.log(251.819824,2),math.log(230.619507,2),math.log(303.054291,2)]
t_159 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(257.000000,2),math.log(239.500000,2),math.log(244.250000,2),math.log(262.000000,2),math.log(247.875000,2),math.log(245.437500,2),math.log(245.546875,2),math.log(273.054688,2),math.log(275.210938,2),math.log(283.734375,2),math.log(289.649414,2),math.log(278.364746,2),math.log(282.754883,2),math.log(300.463867,2),math.log(287.231934,2),math.log(269.380096,2)]
t_160 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(271.000000,2),math.log(293.000000,2),math.log(255.000000,2),math.log(230.375000,2),math.log(252.250000,2),math.log(261.875000,2),math.log(281.593750,2),math.log(272.195312,2),math.log(271.429688,2),math.log(241.720703,2),math.log(231.886719,2),math.log(281.614746,2),math.log(274.083008,2),math.log(302.437988,2),math.log(273.541443,2),math.log(255.296051,2)]
t_161 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(230.750000,2),math.log(219.750000,2),math.log(270.375000,2),math.log(271.312500,2),math.log(283.390625,2),math.log(283.765625,2),math.log(287.625000,2),math.log(307.804688,2),math.log(292.920898,2),math.log(274.620117,2),math.log(256.966797,2),math.log(269.556030,2),math.log(259.845215,2),math.log(302.843781,2)]
t_162 = [math.log(224.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(249.000000,2),math.log(252.000000,2),math.log(234.250000,2),math.log(244.875000,2),math.log(228.875000,2),math.log(230.906250,2),math.log(237.859375,2),math.log(249.617188,2),math.log(246.714844,2),math.log(259.003906,2),math.log(258.147461,2),math.log(307.842773,2),math.log(254.689697,2),math.log(227.463623,2),math.log(276.585022,2),math.log(247.364288,2)]
t_163 = [math.log(272.000000,2),math.log(288.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(304.000000,2),math.log(264.500000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(288.125000,2),math.log(259.750000,2),math.log(246.640625,2),math.log(233.734375,2),math.log(270.222656,2),math.log(258.576172,2),math.log(246.703125,2),math.log(264.248047,2),math.log(291.301514,2),math.log(275.914429,2),math.log(316.249451,2),math.log(282.823181,2)]
t_164 = [math.log(256.000000,2),math.log(264.000000,2),math.log(220.000000,2),math.log(204.000000,2),math.log(207.000000,2),math.log(212.000000,2),math.log(221.250000,2),math.log(254.500000,2),math.log(223.187500,2),math.log(249.281250,2),math.log(225.218750,2),math.log(228.789062,2),math.log(224.628906,2),math.log(243.843750,2),math.log(245.914062,2),math.log(232.895996,2),math.log(271.972900,2),math.log(261.577271,2),math.log(284.861877,2),math.log(254.650848,2)]
t_165 = [math.log(288.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(218.000000,2),math.log(231.000000,2),math.log(216.000000,2),math.log(242.500000,2),math.log(244.500000,2),math.log(243.812500,2),math.log(284.937500,2),math.log(247.187500,2),math.log(271.257812,2),math.log(308.433594,2),math.log(292.142578,2),math.log(271.742188,2),math.log(273.484375,2),math.log(271.860840,2),math.log(278.759399,2),math.log(268.548828,2),math.log(252.377625,2)]
t_166 = [math.log(224.000000,2),math.log(256.000000,2),math.log(316.000000,2),math.log(328.000000,2),math.log(313.000000,2),math.log(303.000000,2),math.log(284.750000,2),math.log(251.625000,2),math.log(218.750000,2),math.log(236.843750,2),math.log(238.390625,2),math.log(228.492188,2),math.log(236.207031,2),math.log(250.718750,2),math.log(263.225586,2),math.log(217.057617,2),math.log(207.622314,2),math.log(238.770874,2),math.log(224.388611,2),math.log(271.979980,2)]
t_167 = [math.log(224.000000,2),math.log(216.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(257.000000,2),math.log(261.000000,2),math.log(243.000000,2),math.log(284.875000,2),math.log(273.250000,2),math.log(276.875000,2),math.log(245.890625,2),math.log(279.710938,2),math.log(280.648438,2),math.log(243.718750,2),math.log(283.356445,2),math.log(288.410645,2),math.log(280.896973,2),math.log(259.605835,2),math.log(251.250977,2),math.log(244.493927,2)]
t_168 = [math.log(224.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(257.000000,2),math.log(251.000000,2),math.log(244.625000,2),math.log(249.250000,2),math.log(272.625000,2),math.log(292.843750,2),math.log(290.226562,2),math.log(240.687500,2),math.log(235.054688,2),math.log(254.669922,2),math.log(244.994629,2),math.log(234.166748,2),math.log(265.413330,2),math.log(277.904358,2),math.log(242.248291,2)]
t_169 = [math.log(256.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(280.000000,2),math.log(266.500000,2),math.log(272.500000,2),math.log(266.625000,2),math.log(257.937500,2),math.log(228.843750,2),math.log(222.140625,2),math.log(211.140625,2),math.log(228.074219,2),math.log(238.474609,2),math.log(223.763672,2),math.log(261.561523,2),math.log(285.235840,2),math.log(309.414673,2),math.log(289.851929,2),math.log(298.578888,2)]
t_170 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(270.000000,2),math.log(233.000000,2),math.log(222.500000,2),math.log(241.750000,2),math.log(266.750000,2),math.log(257.875000,2),math.log(265.781250,2),math.log(253.109375,2),math.log(261.656250,2),math.log(284.832031,2),math.log(280.843750,2),math.log(290.111328,2),math.log(263.491211,2),math.log(293.770020,2),math.log(267.875732,2),math.log(286.290833,2),math.log(285.339874,2)]
t_171 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(280.000000,2),math.log(324.000000,2),math.log(299.500000,2),math.log(263.250000,2),math.log(206.875000,2),math.log(226.687500,2),math.log(246.000000,2),math.log(268.156250,2),math.log(236.242188,2),math.log(247.003906,2),math.log(226.875000,2),math.log(256.070312,2),math.log(255.097168,2),math.log(255.899658,2),math.log(264.537964,2),math.log(257.873535,2),math.log(231.796692,2)]
t_172 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(254.000000,2),math.log(252.000000,2),math.log(225.500000,2),math.log(210.250000,2),math.log(219.500000,2),math.log(247.687500,2),math.log(262.843750,2),math.log(259.437500,2),math.log(239.320312,2),math.log(278.460938,2),math.log(260.082031,2),math.log(259.681641,2),math.log(222.324707,2),math.log(235.266113,2),math.log(252.805786,2),math.log(283.467346,2),math.log(299.169037,2)]
t_173 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(294.000000,2),math.log(278.000000,2),math.log(288.500000,2),math.log(267.500000,2),math.log(252.500000,2),math.log(275.500000,2),math.log(271.031250,2),math.log(247.578125,2),math.log(253.117188,2),math.log(300.988281,2),math.log(269.986328,2),math.log(240.902344,2),math.log(238.272949,2),math.log(254.771484,2),math.log(257.350464,2),math.log(234.324341,2),math.log(228.120361,2)]
t_174 = [math.log(240.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(250.000000,2),math.log(253.000000,2),math.log(268.500000,2),math.log(234.750000,2),math.log(232.125000,2),math.log(249.812500,2),math.log(261.750000,2),math.log(275.453125,2),math.log(284.101562,2),math.log(281.238281,2),math.log(242.771484,2),math.log(231.065430,2),math.log(231.957031,2),math.log(227.214355,2),math.log(210.721069,2),math.log(205.196045,2),math.log(238.996155,2)]
t_175 = [math.log(256.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(230.000000,2),math.log(247.000000,2),math.log(218.500000,2),math.log(213.500000,2),math.log(219.750000,2),math.log(229.375000,2),math.log(252.843750,2),math.log(216.578125,2),math.log(216.179688,2),math.log(202.453125,2),math.log(230.648438,2),math.log(250.954102,2),math.log(228.336914,2),math.log(249.081787,2),math.log(252.096436,2),math.log(275.133667,2),math.log(245.324860,2)]
t_176 = [math.log(272.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(258.000000,2),math.log(253.000000,2),math.log(257.500000,2),math.log(235.500000,2),math.log(270.625000,2),math.log(285.687500,2),math.log(284.093750,2),math.log(264.765625,2),math.log(305.125000,2),math.log(260.144531,2),math.log(259.792969,2),math.log(312.525391,2),math.log(283.439941,2),math.log(289.064697,2),math.log(250.923950,2),math.log(235.313049,2),math.log(233.342163,2)]
t_177 = [math.log(256.000000,2),math.log(280.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(247.000000,2),math.log(260.000000,2),math.log(248.250000,2),math.log(278.875000,2),math.log(231.937500,2),math.log(233.218750,2),math.log(240.203125,2),math.log(251.804688,2),math.log(244.933594,2),math.log(244.955078,2),math.log(256.814453,2),math.log(243.322754,2),math.log(236.060791,2),math.log(205.322754,2),math.log(210.653687,2),math.log(240.521973,2)]
t_178 = [math.log(288.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(239.500000,2),math.log(261.750000,2),math.log(266.000000,2),math.log(236.625000,2),math.log(269.968750,2),math.log(311.281250,2),math.log(294.234375,2),math.log(272.687500,2),math.log(301.761719,2),math.log(261.243164,2),math.log(255.421387,2),math.log(259.286621,2),math.log(249.909424,2),math.log(233.170166,2),math.log(242.154877,2)]
t_179 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(234.000000,2),math.log(266.500000,2),math.log(285.500000,2),math.log(245.750000,2),math.log(222.187500,2),math.log(240.718750,2),math.log(238.750000,2),math.log(242.476562,2),math.log(273.570312,2),math.log(259.861328,2),math.log(291.748047,2),math.log(264.993652,2),math.log(267.040283,2),math.log(262.389771,2),math.log(251.389099,2),math.log(253.005646,2)]
t_180 = [math.log(256.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(238.000000,2),math.log(237.000000,2),math.log(232.000000,2),math.log(235.250000,2),math.log(243.625000,2),math.log(274.250000,2),math.log(260.093750,2),math.log(253.375000,2),math.log(255.789062,2),math.log(269.339844,2),math.log(276.888672,2),math.log(264.724609,2),math.log(250.115723,2),math.log(277.565918,2),math.log(280.937988,2),math.log(252.541504,2),math.log(292.125458,2)]
t_181 = [math.log(224.000000,2),math.log(208.000000,2),math.log(228.000000,2),math.log(254.000000,2),math.log(205.000000,2),math.log(246.500000,2),math.log(220.500000,2),math.log(244.000000,2),math.log(225.062500,2),math.log(263.875000,2),math.log(238.562500,2),math.log(277.195312,2),math.log(285.804688,2),math.log(272.439453,2),math.log(253.954102,2),math.log(289.104004,2),math.log(271.241943,2),math.log(284.290894,2),math.log(288.028442,2),math.log(251.934052,2)]
t_182 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(274.000000,2),math.log(255.500000,2),math.log(250.250000,2),math.log(256.375000,2),math.log(272.562500,2),math.log(247.562500,2),math.log(270.890625,2),math.log(244.703125,2),math.log(315.128906,2),math.log(352.259766,2),math.log(287.447266,2),math.log(290.059570,2),math.log(293.343018,2),math.log(267.437622,2),math.log(265.811707,2),math.log(259.105347,2)]
t_183 = [math.log(256.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(256.000000,2),math.log(226.500000,2),math.log(255.750000,2),math.log(248.750000,2),math.log(285.250000,2),math.log(266.531250,2),math.log(235.937500,2),math.log(240.578125,2),math.log(222.773438,2),math.log(234.410156,2),math.log(216.299805,2),math.log(232.091797,2),math.log(213.887451,2),math.log(242.464111,2),math.log(264.384460,2),math.log(290.699982,2)]
t_184 = [math.log(256.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(248.000000,2),math.log(280.500000,2),math.log(275.000000,2),math.log(251.250000,2),math.log(280.000000,2),math.log(271.031250,2),math.log(271.015625,2),math.log(281.414062,2),math.log(307.621094,2),math.log(269.361328,2),math.log(305.636719,2),math.log(307.604004,2),math.log(285.206299,2),math.log(285.135986,2),math.log(284.980164,2),math.log(275.920074,2)]
t_185 = [math.log(224.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(279.000000,2),math.log(280.500000,2),math.log(270.250000,2),math.log(265.875000,2),math.log(248.250000,2),math.log(238.656250,2),math.log(225.890625,2),math.log(236.351562,2),math.log(251.695312,2),math.log(302.072266,2),math.log(275.298828,2),math.log(241.606934,2),math.log(248.077148,2),math.log(226.028809,2),math.log(225.404175,2),math.log(234.315643,2)]
t_186 = [math.log(240.000000,2),math.log(216.000000,2),math.log(236.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(261.500000,2),math.log(261.500000,2),math.log(270.375000,2),math.log(248.187500,2),math.log(247.203125,2),math.log(253.781250,2),math.log(238.000000,2),math.log(262.308594,2),math.log(277.450195,2),math.log(243.238770,2),math.log(250.660400,2),math.log(277.599121,2),math.log(287.938660,2),math.log(283.617462,2)]
t_187 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(262.000000,2),math.log(238.000000,2),math.log(240.500000,2),math.log(258.750000,2),math.log(278.875000,2),math.log(295.437500,2),math.log(251.437500,2),math.log(275.796875,2),math.log(258.531250,2),math.log(260.519531,2),math.log(293.687500,2),math.log(278.055664,2),math.log(281.477051,2),math.log(291.320312,2),math.log(263.777466,2),math.log(244.801208,2),math.log(265.604584,2)]
t_188 = [math.log(240.000000,2),math.log(312.000000,2),math.log(312.000000,2),math.log(258.000000,2),math.log(245.000000,2),math.log(218.000000,2),math.log(205.500000,2),math.log(236.625000,2),math.log(243.625000,2),math.log(235.812500,2),math.log(286.031250,2),math.log(274.304688,2),math.log(261.191406,2),math.log(254.382812,2),math.log(254.448242,2),math.log(248.704102,2),math.log(267.327148,2),math.log(277.416992,2),math.log(256.270386,2),math.log(236.545502,2)]
t_189 = [math.log(224.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(218.000000,2),math.log(244.000000,2),math.log(262.000000,2),math.log(230.250000,2),math.log(222.125000,2),math.log(224.593750,2),math.log(267.593750,2),math.log(268.515625,2),math.log(254.308594,2),math.log(275.322266,2),math.log(259.753906,2),math.log(268.431152,2),math.log(297.376221,2),math.log(259.443604,2),math.log(225.505981,2),math.log(252.141205,2)]
t_190 = [math.log(272.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(272.000000,2),math.log(261.000000,2),math.log(251.500000,2),math.log(263.000000,2),math.log(272.500000,2),math.log(261.500000,2),math.log(249.218750,2),math.log(237.453125,2),math.log(237.390625,2),math.log(257.003906,2),math.log(279.089844,2),math.log(236.412109,2),math.log(257.528320,2),math.log(218.940186,2),math.log(231.192993,2),math.log(223.734436,2),math.log(224.662354,2)]
t_191 = [math.log(272.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(302.000000,2),math.log(293.000000,2),math.log(289.500000,2),math.log(300.250000,2),math.log(301.250000,2),math.log(254.937500,2),math.log(265.312500,2),math.log(241.796875,2),math.log(236.976562,2),math.log(220.460938,2),math.log(232.763672,2),math.log(243.917969,2),math.log(273.858398,2),math.log(260.175293,2),math.log(267.557861,2),math.log(277.119690,2),math.log(255.158630,2)]
t_192 = [math.log(272.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(285.000000,2),math.log(277.125000,2),math.log(295.125000,2),math.log(269.062500,2),math.log(285.312500,2),math.log(250.976562,2),math.log(229.902344,2),math.log(229.634766,2),math.log(242.763672,2),math.log(275.558105,2),math.log(264.623291,2),math.log(273.747192,2),math.log(280.342834,2),math.log(271.214264,2)]
t_193 = [math.log(240.000000,2),math.log(264.000000,2),math.log(224.000000,2),math.log(222.000000,2),math.log(211.000000,2),math.log(219.500000,2),math.log(211.750000,2),math.log(224.875000,2),math.log(281.687500,2),math.log(298.437500,2),math.log(240.187500,2),math.log(270.648438,2),math.log(255.464844,2),math.log(274.968750,2),math.log(272.277344,2),math.log(267.911133,2),math.log(291.836914,2),math.log(261.196777,2),math.log(255.285950,2),math.log(247.785583,2)]
t_194 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(280.000000,2),math.log(258.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(269.875000,2),math.log(226.875000,2),math.log(249.625000,2),math.log(241.781250,2),math.log(268.804688,2),math.log(240.421875,2),math.log(234.119141,2),math.log(257.248047,2),math.log(274.625000,2),math.log(276.125244,2),math.log(247.780151,2),math.log(257.357666,2),math.log(273.346069,2)]
t_195 = [math.log(240.000000,2),math.log(216.000000,2),math.log(264.000000,2),math.log(266.000000,2),math.log(244.000000,2),math.log(228.500000,2),math.log(212.250000,2),math.log(233.500000,2),math.log(262.937500,2),math.log(271.125000,2),math.log(240.812500,2),math.log(228.359375,2),math.log(257.605469,2),math.log(277.847656,2),math.log(280.397461,2),math.log(288.350586,2),math.log(271.950195,2),math.log(268.190186,2),math.log(258.073486,2),math.log(243.233185,2)]
t_196 = [math.log(256.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(280.000000,2),math.log(266.000000,2),math.log(243.750000,2),math.log(230.250000,2),math.log(212.062500,2),math.log(222.468750,2),math.log(221.953125,2),math.log(290.289062,2),math.log(286.394531,2),math.log(248.546875,2),math.log(241.417969,2),math.log(244.914062,2),math.log(286.462891,2),math.log(288.818848,2),math.log(278.204285,2),math.log(250.195923,2)]
t_197 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(257.000000,2),math.log(289.500000,2),math.log(263.250000,2),math.log(284.000000,2),math.log(310.375000,2),math.log(263.531250,2),math.log(259.515625,2),math.log(263.023438,2),math.log(282.675781,2),math.log(292.623047,2),math.log(239.042969,2),math.log(198.376953,2),math.log(236.969727,2),math.log(238.477173,2),math.log(254.660095,2),math.log(258.721039,2)]
t_198 = [math.log(288.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(237.000000,2),math.log(273.000000,2),math.log(261.750000,2),math.log(264.625000,2),math.log(272.500000,2),math.log(260.968750,2),math.log(272.859375,2),math.log(250.992188,2),math.log(252.109375,2),math.log(224.218750,2),math.log(215.158203,2),math.log(268.313477,2),math.log(268.228027,2),math.log(257.781494,2),math.log(260.021362,2),math.log(255.038818,2)]
t_199 = [math.log(272.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(268.500000,2),math.log(285.250000,2),math.log(234.375000,2),math.log(268.437500,2),math.log(257.687500,2),math.log(242.343750,2),math.log(258.968750,2),math.log(264.937500,2),math.log(234.070312,2),math.log(252.328125,2),math.log(226.499023,2),math.log(268.305664,2),math.log(262.123291,2),math.log(217.257812,2),math.log(212.517548,2)]
t_200 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(293.000000,2),math.log(249.000000,2),math.log(261.250000,2),math.log(306.375000,2),math.log(277.687500,2),math.log(260.562500,2),math.log(281.500000,2),math.log(266.937500,2),math.log(281.191406,2),math.log(255.304688,2),math.log(242.672852,2),math.log(232.874023,2),math.log(228.500244,2),math.log(252.328979,2),math.log(275.908020,2),math.log(269.250732,2)]
t_201 = [math.log(240.000000,2),math.log(224.000000,2),math.log(204.000000,2),math.log(222.000000,2),math.log(235.000000,2),math.log(279.000000,2),math.log(247.500000,2),math.log(264.875000,2),math.log(248.500000,2),math.log(278.562500,2),math.log(289.578125,2),math.log(313.382812,2),math.log(289.203125,2),math.log(259.492188,2),math.log(242.112305,2),math.log(283.687012,2),math.log(267.500488,2),math.log(236.129639,2),math.log(278.738831,2),math.log(251.213837,2)]
t_202 = [math.log(256.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(245.000000,2),math.log(204.500000,2),math.log(226.750000,2),math.log(240.125000,2),math.log(250.250000,2),math.log(228.281250,2),math.log(235.937500,2),math.log(233.578125,2),math.log(223.601562,2),math.log(224.064453,2),math.log(260.986328,2),math.log(251.654297,2),math.log(245.799561,2),math.log(246.112061,2),math.log(240.571106,2),math.log(238.600952,2)]
t_203 = [math.log(320.000000,2),math.log(320.000000,2),math.log(292.000000,2),math.log(252.000000,2),math.log(247.000000,2),math.log(255.500000,2),math.log(267.250000,2),math.log(280.125000,2),math.log(292.500000,2),math.log(309.625000,2),math.log(284.156250,2),math.log(272.062500,2),math.log(270.503906,2),math.log(257.671875,2),math.log(296.629883,2),math.log(303.349121,2),math.log(328.517334,2),math.log(300.458740,2),math.log(263.331543,2),math.log(277.095154,2)]
t_204 = [math.log(224.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(271.500000,2),math.log(252.750000,2),math.log(246.125000,2),math.log(260.750000,2),math.log(220.843750,2),math.log(228.468750,2),math.log(238.273438,2),math.log(225.492188,2),math.log(222.619141,2),math.log(264.688477,2),math.log(253.471191,2),math.log(267.527100,2),math.log(271.101562,2),math.log(236.449219,2),math.log(263.740997,2)]
t_205 = [math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(266.000000,2),math.log(261.000000,2),math.log(251.000000,2),math.log(257.000000,2),math.log(276.625000,2),math.log(246.125000,2),math.log(250.562500,2),math.log(273.015625,2),math.log(243.039062,2),math.log(250.035156,2),math.log(256.873047,2),math.log(287.823242,2),math.log(255.816406,2),math.log(234.298584,2),math.log(258.505005,2),math.log(275.366455,2),math.log(248.995514,2)]
t_206 = [math.log(240.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(272.000000,2),math.log(258.500000,2),math.log(241.000000,2),math.log(232.125000,2),math.log(221.062500,2),math.log(250.281250,2),math.log(256.171875,2),math.log(261.789062,2),math.log(307.261719,2),math.log(273.488281,2),math.log(239.794922,2),math.log(293.167969,2),math.log(241.495605,2),math.log(241.362183,2),math.log(240.327759,2),math.log(252.182312,2)]
t_207 = [math.log(304.000000,2),math.log(296.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(198.000000,2),math.log(225.500000,2),math.log(239.500000,2),math.log(226.500000,2),math.log(230.437500,2),math.log(253.093750,2),math.log(247.390625,2),math.log(282.359375,2),math.log(242.425781,2),math.log(202.871094,2),math.log(220.924805,2),math.log(204.821777,2),math.log(243.202148,2),math.log(264.067139,2),math.log(293.078308,2),math.log(283.780212,2)]
t_208 = [math.log(224.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(270.000000,2),math.log(245.000000,2),math.log(229.000000,2),math.log(242.750000,2),math.log(239.125000,2),math.log(268.875000,2),math.log(290.343750,2),math.log(289.687500,2),math.log(275.687500,2),math.log(244.277344,2),math.log(214.623047,2),math.log(222.236328,2),math.log(234.874023,2),math.log(254.104492,2),math.log(258.004639,2),math.log(271.065674,2),math.log(223.532623,2)]
t_209 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(263.000000,2),math.log(270.750000,2),math.log(258.625000,2),math.log(244.375000,2),math.log(258.031250,2),math.log(264.015625,2),math.log(243.570312,2),math.log(242.324219,2),math.log(285.031250,2),math.log(269.738281,2),math.log(287.786621,2),math.log(279.063965,2),math.log(246.935181,2),math.log(227.850281,2),math.log(212.951202,2)]
t_210 = [math.log(272.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(271.000000,2),math.log(263.000000,2),math.log(251.500000,2),math.log(272.500000,2),math.log(245.750000,2),math.log(225.437500,2),math.log(208.718750,2),math.log(239.796875,2),math.log(262.089844,2),math.log(211.044922,2),math.log(237.101562,2),math.log(251.267090,2),math.log(217.003662,2),math.log(214.065186,2),math.log(205.969971,2),math.log(210.625000,2)]
t_211 = [math.log(304.000000,2),math.log(296.000000,2),math.log(288.000000,2),math.log(278.000000,2),math.log(204.000000,2),math.log(212.000000,2),math.log(192.000000,2),math.log(223.500000,2),math.log(246.562500,2),math.log(217.187500,2),math.log(216.125000,2),math.log(229.664062,2),math.log(261.574219,2),math.log(258.214844,2),math.log(254.297852,2),math.log(254.473145,2),math.log(281.886475,2),math.log(276.226929,2),math.log(259.528320,2),math.log(251.705322,2)]
t_212 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(227.000000,2),math.log(234.500000,2),math.log(241.750000,2),math.log(262.000000,2),math.log(264.500000,2),math.log(265.843750,2),math.log(262.437500,2),math.log(280.656250,2),math.log(283.496094,2),math.log(322.449219,2),math.log(301.025391,2),math.log(275.022461,2),math.log(234.497559,2),math.log(214.238647,2),math.log(253.259644,2),math.log(254.598511,2)]
t_213 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(255.000000,2),math.log(281.000000,2),math.log(259.750000,2),math.log(231.500000,2),math.log(224.437500,2),math.log(254.062500,2),math.log(264.578125,2),math.log(274.398438,2),math.log(281.511719,2),math.log(253.101562,2),math.log(242.574219,2),math.log(248.968750,2),math.log(248.531250,2),math.log(256.005005,2),math.log(263.780090,2),math.log(270.201416,2)]
t_214 = [math.log(304.000000,2),math.log(304.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(275.000000,2),math.log(254.000000,2),math.log(278.000000,2),math.log(281.875000,2),math.log(245.312500,2),math.log(227.843750,2),math.log(229.093750,2),math.log(237.726562,2),math.log(263.449219,2),math.log(240.771484,2),math.log(277.735352,2),math.log(253.160156,2),math.log(269.176514,2),math.log(276.987427,2),math.log(263.532043,2),math.log(258.876251,2)]
t_215 = [math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(273.000000,2),math.log(267.750000,2),math.log(227.375000,2),math.log(223.562500,2),math.log(248.187500,2),math.log(213.546875,2),math.log(259.359375,2),math.log(277.406250,2),math.log(280.736328,2),math.log(250.342773,2),math.log(278.797363,2),math.log(287.671631,2),math.log(263.958252,2),math.log(257.688477,2),math.log(262.531311,2)]
t_216 = [math.log(272.000000,2),math.log(288.000000,2),math.log(324.000000,2),math.log(320.000000,2),math.log(282.000000,2),math.log(292.500000,2),math.log(284.500000,2),math.log(263.875000,2),math.log(259.312500,2),math.log(286.375000,2),math.log(252.765625,2),math.log(236.468750,2),math.log(282.902344,2),math.log(278.009766,2),math.log(309.520508,2),math.log(256.041992,2),math.log(272.417480,2),math.log(245.244995,2),math.log(225.789551,2),math.log(234.650238,2)]
t_217 = [math.log(288.000000,2),math.log(280.000000,2),math.log(236.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(242.500000,2),math.log(244.500000,2),math.log(249.000000,2),math.log(261.562500,2),math.log(229.875000,2),math.log(240.578125,2),math.log(239.265625,2),math.log(229.816406,2),math.log(239.134766,2),math.log(261.939453,2),math.log(246.793945,2),math.log(267.806641,2),math.log(324.455933,2),math.log(308.982117,2),math.log(269.905853,2)]
t_218 = [math.log(288.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(223.000000,2),math.log(232.500000,2),math.log(236.250000,2),math.log(209.000000,2),math.log(242.500000,2),math.log(278.187500,2),math.log(243.234375,2),math.log(257.437500,2),math.log(281.382812,2),math.log(236.343750,2),math.log(276.607422,2),math.log(268.583984,2),math.log(279.912109,2),math.log(252.528198,2),math.log(228.436340,2),math.log(215.290283,2)]
t_219 = [math.log(288.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(280.000000,2),math.log(234.000000,2),math.log(250.000000,2),math.log(242.500000,2),math.log(233.125000,2),math.log(225.812500,2),math.log(222.000000,2),math.log(237.140625,2),math.log(227.476562,2),math.log(241.425781,2),math.log(252.636719,2),math.log(238.887695,2),math.log(222.874512,2),math.log(241.514160,2),math.log(258.406006,2),math.log(247.163391,2),math.log(228.959625,2)]
t_220 = [math.log(288.000000,2),math.log(288.000000,2),math.log(292.000000,2),math.log(276.000000,2),math.log(281.000000,2),math.log(284.000000,2),math.log(271.000000,2),math.log(237.250000,2),math.log(260.062500,2),math.log(269.937500,2),math.log(229.531250,2),math.log(280.921875,2),math.log(264.347656,2),math.log(253.498047,2),math.log(267.712891,2),math.log(278.407715,2),math.log(274.245117,2),math.log(306.612305,2),math.log(299.283813,2),math.log(280.958923,2)]
t_221 = [math.log(256.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(222.000000,2),math.log(228.000000,2),math.log(220.500000,2),math.log(227.750000,2),math.log(244.500000,2),math.log(234.937500,2),math.log(249.531250,2),math.log(263.546875,2),math.log(226.578125,2),math.log(251.363281,2),math.log(259.978516,2),math.log(250.483398,2),math.log(228.920898,2),math.log(285.911377,2),math.log(264.278442,2),math.log(254.587097,2),math.log(259.778351,2)]
t_222 = [math.log(224.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(266.000000,2),math.log(254.000000,2),math.log(243.500000,2),math.log(253.000000,2),math.log(276.000000,2),math.log(280.125000,2),math.log(263.468750,2),math.log(220.234375,2),math.log(252.093750,2),math.log(236.601562,2),math.log(235.769531,2),math.log(231.184570,2),math.log(246.004883,2),math.log(246.243408,2),math.log(257.276367,2),math.log(294.968872,2),math.log(301.258118,2)]
t_223 = [math.log(256.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(271.000000,2),math.log(234.500000,2),math.log(243.000000,2),math.log(252.500000,2),math.log(257.312500,2),math.log(256.718750,2),math.log(248.375000,2),math.log(258.578125,2),math.log(274.570312,2),math.log(270.060547,2),math.log(259.918945,2),math.log(277.161621,2),math.log(280.322021,2),math.log(328.626221,2),math.log(271.471008,2),math.log(245.942139,2)]
t_224 = [math.log(256.000000,2),math.log(328.000000,2),math.log(284.000000,2),math.log(322.000000,2),math.log(286.000000,2),math.log(263.000000,2),math.log(286.750000,2),math.log(260.250000,2),math.log(246.000000,2),math.log(243.562500,2),math.log(229.796875,2),math.log(267.289062,2),math.log(291.199219,2),math.log(240.113281,2),math.log(244.874023,2),math.log(260.128418,2),math.log(297.764160,2),math.log(273.157349,2),math.log(254.056030,2),math.log(258.548584,2)]
t_225 = [math.log(240.000000,2),math.log(240.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(279.000000,2),math.log(229.500000,2),math.log(231.750000,2),math.log(239.875000,2),math.log(242.312500,2),math.log(256.937500,2),math.log(265.218750,2),math.log(274.039062,2),math.log(233.476562,2),math.log(250.490234,2),math.log(253.346680,2),math.log(245.099609,2),math.log(254.068848,2),math.log(243.412231,2),math.log(246.080383,2),math.log(241.311188,2)]
t_226 = [math.log(272.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(279.000000,2),math.log(267.000000,2),math.log(258.750000,2),math.log(269.875000,2),math.log(286.750000,2),math.log(257.812500,2),math.log(232.765625,2),math.log(251.398438,2),math.log(317.394531,2),math.log(302.486328,2),math.log(274.971680,2),math.log(282.793457,2),math.log(252.693604,2),math.log(263.945801,2),math.log(264.872559,2),math.log(247.662323,2)]
t_227 = [math.log(272.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(257.000000,2),math.log(275.500000,2),math.log(274.000000,2),math.log(255.250000,2),math.log(243.062500,2),math.log(245.656250,2),math.log(252.281250,2),math.log(225.929688,2),math.log(248.722656,2),math.log(257.701172,2),math.log(254.449219,2),math.log(294.188965,2),math.log(288.269043,2),math.log(280.120850,2),math.log(259.846436,2),math.log(225.418732,2)]
t_228 = [math.log(304.000000,2),math.log(320.000000,2),math.log(316.000000,2),math.log(290.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(272.500000,2),math.log(244.375000,2),math.log(250.250000,2),math.log(265.281250,2),math.log(242.640625,2),math.log(244.828125,2),math.log(249.722656,2),math.log(279.494141,2),math.log(276.084961,2),math.log(278.378906,2),math.log(269.348877,2),math.log(281.808472,2),math.log(263.967285,2),math.log(251.525513,2)]
t_229 = [math.log(304.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(214.000000,2),math.log(242.000000,2),math.log(245.000000,2),math.log(228.000000,2),math.log(230.750000,2),math.log(229.937500,2),math.log(223.968750,2),math.log(275.015625,2),math.log(288.757812,2),math.log(282.410156,2),math.log(275.523438,2),math.log(293.685547,2),math.log(270.678711,2),math.log(245.993896,2),math.log(237.006470,2),math.log(244.358643,2),math.log(245.834930,2)]
t_230 = [math.log(240.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(265.000000,2),math.log(269.000000,2),math.log(276.500000,2),math.log(312.625000,2),math.log(296.875000,2),math.log(293.593750,2),math.log(288.062500,2),math.log(243.664062,2),math.log(272.835938,2),math.log(226.169922,2),math.log(244.506836,2),math.log(267.001953,2),math.log(241.228027,2),math.log(258.220581,2),math.log(243.476929,2),math.log(252.488342,2)]
t_231 = [math.log(224.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(231.000000,2),math.log(215.500000,2),math.log(247.500000,2),math.log(285.625000,2),math.log(284.000000,2),math.log(254.906250,2),math.log(267.187500,2),math.log(248.992188,2),math.log(232.632812,2),math.log(231.435547,2),math.log(254.023438,2),math.log(292.121094,2),math.log(272.224121,2),math.log(230.912109,2),math.log(278.300171,2),math.log(297.662079,2)]
t_232 = [math.log(224.000000,2),math.log(232.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(254.000000,2),math.log(264.500000,2),math.log(271.250000,2),math.log(235.000000,2),math.log(254.562500,2),math.log(233.625000,2),math.log(246.414062,2),math.log(275.980469,2),math.log(273.449219,2),math.log(256.226562,2),math.log(218.758789,2),math.log(219.627197,2),math.log(221.859131,2),math.log(227.319153,2),math.log(219.682739,2)]
t_233 = [math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(296.000000,2),math.log(275.000000,2),math.log(280.750000,2),math.log(286.125000,2),math.log(299.250000,2),math.log(320.062500,2),math.log(265.765625,2),math.log(289.609375,2),math.log(268.054688,2),math.log(234.050781,2),math.log(256.954102,2),math.log(251.008789,2),math.log(292.937256,2),math.log(301.429321,2),math.log(285.615173,2),math.log(266.145172,2)]
t_234 = [math.log(352.000000,2),math.log(312.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(258.000000,2),math.log(248.500000,2),math.log(238.750000,2),math.log(229.500000,2),math.log(246.187500,2),math.log(224.968750,2),math.log(230.250000,2),math.log(279.078125,2),math.log(231.933594,2),math.log(220.599609,2),math.log(230.938477,2),math.log(229.069336,2),math.log(251.373291,2),math.log(223.659668,2),math.log(223.512695,2),math.log(274.658325,2)]
t_235 = [math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(271.500000,2),math.log(270.750000,2),math.log(230.000000,2),math.log(225.062500,2),math.log(233.531250,2),math.log(258.765625,2),math.log(241.882812,2),math.log(193.750000,2),math.log(242.357422,2),math.log(268.742188,2),math.log(239.415039,2),math.log(246.503418,2),math.log(221.822388,2),math.log(236.959656,2),math.log(227.566711,2)]
t_236 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(230.000000,2),math.log(216.000000,2),math.log(231.500000,2),math.log(267.750000,2),math.log(238.500000,2),math.log(226.312500,2),math.log(197.656250,2),math.log(200.734375,2),math.log(224.015625,2),math.log(291.769531,2),math.log(277.273438,2),math.log(279.295898,2),math.log(228.935059,2),math.log(218.814697,2),math.log(235.532593,2),math.log(243.690369,2),math.log(269.215668,2)]
t_237 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(250.000000,2),math.log(267.000000,2),math.log(233.000000,2),math.log(265.250000,2),math.log(258.625000,2),math.log(255.750000,2),math.log(272.593750,2),math.log(278.171875,2),math.log(263.773438,2),math.log(235.886719,2),math.log(223.357422,2),math.log(243.965820,2),math.log(235.949707,2),math.log(236.780762,2),math.log(225.102539,2),math.log(245.191406,2),math.log(236.550537,2)]
t_238 = [math.log(288.000000,2),math.log(272.000000,2),math.log(304.000000,2),math.log(328.000000,2),math.log(297.000000,2),math.log(287.500000,2),math.log(294.250000,2),math.log(273.250000,2),math.log(251.937500,2),math.log(247.312500,2),math.log(262.843750,2),math.log(238.929688,2),math.log(230.843750,2),math.log(226.875000,2),math.log(246.144531,2),math.log(242.166504,2),math.log(214.245117,2),math.log(201.753418,2),math.log(231.588257,2),math.log(251.053131,2)]
t_239 = [math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(304.000000,2),math.log(290.000000,2),math.log(265.500000,2),math.log(218.500000,2),math.log(236.750000,2),math.log(247.437500,2),math.log(236.125000,2),math.log(255.187500,2),math.log(264.898438,2),math.log(282.035156,2),math.log(259.531250,2),math.log(250.996094,2),math.log(261.734863,2),math.log(269.498047,2),math.log(247.820435,2),math.log(246.890137,2),math.log(243.464783,2)]
t_240 = [math.log(240.000000,2),math.log(240.000000,2),math.log(216.000000,2),math.log(234.000000,2),math.log(262.000000,2),math.log(232.500000,2),math.log(236.750000,2),math.log(250.625000,2),math.log(232.250000,2),math.log(247.781250,2),math.log(276.937500,2),math.log(276.273438,2),math.log(259.179688,2),math.log(274.925781,2),math.log(316.698242,2),math.log(257.586914,2),math.log(249.893555,2),math.log(225.833862,2),math.log(232.115356,2),math.log(189.791168,2)]
t_241 = [math.log(240.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(221.000000,2),math.log(204.500000,2),math.log(260.000000,2),math.log(261.375000,2),math.log(261.750000,2),math.log(274.781250,2),math.log(318.250000,2),math.log(300.476562,2),math.log(280.566406,2),math.log(253.927734,2),math.log(248.359375,2),math.log(297.459961,2),math.log(239.138672,2),math.log(236.941406,2),math.log(260.295105,2),math.log(243.577271,2)]
t_242 = [math.log(224.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(284.000000,2),math.log(267.000000,2),math.log(260.000000,2),math.log(223.500000,2),math.log(222.125000,2),math.log(219.000000,2),math.log(214.156250,2),math.log(215.750000,2),math.log(232.734375,2),math.log(246.515625,2),math.log(259.664062,2),math.log(241.981445,2),math.log(252.663086,2),math.log(239.328369,2),math.log(248.070435,2),math.log(273.091492,2),math.log(247.700684,2)]
t_243 = [math.log(224.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(276.000000,2),math.log(271.000000,2),math.log(251.500000,2),math.log(289.500000,2),math.log(253.000000,2),math.log(239.125000,2),math.log(250.875000,2),math.log(244.296875,2),math.log(229.890625,2),math.log(240.152344,2),math.log(264.283203,2),math.log(256.621094,2),math.log(241.452637,2),math.log(241.602295,2),math.log(272.248657,2),math.log(252.787964,2),math.log(274.266327,2)]
t_244 = [math.log(224.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(278.750000,2),math.log(279.500000,2),math.log(236.000000,2),math.log(231.562500,2),math.log(236.515625,2),math.log(227.804688,2),math.log(257.816406,2),math.log(250.482422,2),math.log(288.080078,2),math.log(269.250488,2),math.log(264.431641,2),math.log(246.362793,2),math.log(280.424011,2),math.log(294.262482,2)]
t_245 = [math.log(288.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(263.000000,2),math.log(290.750000,2),math.log(276.750000,2),math.log(268.812500,2),math.log(230.531250,2),math.log(234.687500,2),math.log(252.867188,2),math.log(244.312500,2),math.log(258.998047,2),math.log(238.600586,2),math.log(241.319824,2),math.log(255.588135,2),math.log(209.908081,2),math.log(228.683594,2),math.log(258.611847,2)]
t_246 = [math.log(288.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(298.500000,2),math.log(306.750000,2),math.log(269.375000,2),math.log(267.250000,2),math.log(223.843750,2),math.log(226.437500,2),math.log(249.226562,2),math.log(255.640625,2),math.log(250.992188,2),math.log(260.026367,2),math.log(251.717285,2),math.log(245.730957,2),math.log(218.530396,2),math.log(224.812988,2),math.log(240.962524,2)]
t_247 = [math.log(256.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(218.000000,2),math.log(227.000000,2),math.log(246.000000,2),math.log(236.500000,2),math.log(252.875000,2),math.log(281.937500,2),math.log(249.000000,2),math.log(256.437500,2),math.log(247.640625,2),math.log(199.339844,2),math.log(242.890625,2),math.log(259.535156,2),math.log(236.617676,2),math.log(250.225586,2),math.log(237.862427,2),math.log(264.870728,2),math.log(287.208130,2)]
t_248 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(287.000000,2),math.log(295.500000,2),math.log(275.750000,2),math.log(260.000000,2),math.log(269.062500,2),math.log(251.062500,2),math.log(268.250000,2),math.log(299.742188,2),math.log(252.195312,2),math.log(232.736328,2),math.log(249.381836,2),math.log(230.374023,2),math.log(268.652588,2),math.log(260.127441,2),math.log(255.291748,2),math.log(263.429474,2)]
t_249 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(259.000000,2),math.log(288.500000,2),math.log(260.500000,2),math.log(233.125000,2),math.log(261.500000,2),math.log(271.843750,2),math.log(278.406250,2),math.log(259.195312,2),math.log(239.347656,2),math.log(292.546875,2),math.log(261.312500,2),math.log(263.748535,2),math.log(250.296875,2),math.log(241.464844,2),math.log(241.039185,2),math.log(257.161926,2)]
t_250 = [math.log(240.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(247.000000,2),math.log(249.750000,2),math.log(259.125000,2),math.log(223.687500,2),math.log(211.312500,2),math.log(261.875000,2),math.log(241.976562,2),math.log(243.332031,2),math.log(237.937500,2),math.log(240.226562,2),math.log(247.244141,2),math.log(250.255127,2),math.log(253.794067,2),math.log(247.410889,2),math.log(231.865570,2)]
t_251 = [math.log(240.000000,2),math.log(280.000000,2),math.log(292.000000,2),math.log(230.000000,2),math.log(266.000000,2),math.log(222.500000,2),math.log(220.250000,2),math.log(229.875000,2),math.log(218.375000,2),math.log(234.406250,2),math.log(277.203125,2),math.log(267.296875,2),math.log(240.785156,2),math.log(287.167969,2),math.log(303.249023,2),math.log(286.312012,2),math.log(264.301025,2),math.log(265.700928,2),math.log(285.562134,2),math.log(229.467743,2)]
t_252 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(274.000000,2),math.log(262.000000,2),math.log(244.500000,2),math.log(251.500000,2),math.log(254.000000,2),math.log(249.062500,2),math.log(283.718750,2),math.log(325.546875,2),math.log(314.890625,2),math.log(290.015625,2),math.log(241.859375,2),math.log(235.294922,2),math.log(260.398438,2),math.log(269.180176,2),math.log(274.262085,2),math.log(252.199402,2),math.log(229.304993,2)]
t_253 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(267.000000,2),math.log(217.000000,2),math.log(234.250000,2),math.log(241.250000,2),math.log(236.187500,2),math.log(252.218750,2),math.log(249.218750,2),math.log(252.484375,2),math.log(254.699219,2),math.log(250.457031,2),math.log(287.088867,2),math.log(274.422363,2),math.log(215.751465,2),math.log(205.785767,2),math.log(221.796875,2),math.log(241.553375,2)]
t_254 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(285.000000,2),math.log(288.000000,2),math.log(309.000000,2),math.log(240.500000,2),math.log(227.000000,2),math.log(227.812500,2),math.log(230.203125,2),math.log(257.304688,2),math.log(258.031250,2),math.log(244.134766,2),math.log(266.910156,2),math.log(238.373535,2),math.log(247.856201,2),math.log(231.292847,2),math.log(255.002014,2),math.log(248.047913,2)]
t_255 = [math.log(272.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(294.000000,2),math.log(268.000000,2),math.log(240.500000,2),math.log(226.250000,2),math.log(223.250000,2),math.log(237.187500,2),math.log(258.812500,2),math.log(265.937500,2),math.log(278.226562,2),math.log(275.832031,2),math.log(270.447266,2),math.log(267.448242,2),math.log(282.902344,2),math.log(274.189941,2),math.log(254.788696,2),math.log(250.321411,2),math.log(269.342316,2)]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00001534
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00001534)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00001534
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00001534)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00001534
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00001534)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00001534
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00001534)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00001534
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00001534)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00001534
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00001534)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00001534
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00001534)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00001534
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00001534)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00001534
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00001534)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00001534
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00001534)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00001534
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00001534)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00001534
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00001534)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00001534
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00001534)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00001534
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00001534)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00001534
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00001534)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00001534
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00001534)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00001534
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00001534)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00001534
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00001534)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00001534
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00001534)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00001534
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00001534)**2)


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

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.001, linestyle="-", c="red",alpha = .15)
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
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 10 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
