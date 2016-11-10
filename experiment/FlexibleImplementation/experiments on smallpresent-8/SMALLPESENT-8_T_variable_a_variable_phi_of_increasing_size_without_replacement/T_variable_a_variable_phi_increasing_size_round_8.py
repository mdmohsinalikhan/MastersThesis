import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(238.000000,2),math.log(234.500000,2),math.log(208.250000,2),math.log(198.625000,2),math.log(205.750000,2),math.log(240.812500,2),math.log(241.859375,2),math.log(256.664062,2),math.log(240.746094,2),math.log(247.482422,2),math.log(250.622070,2),math.log(238.944336,2),math.log(238.910889,2),math.log(223.007690,2),math.log(259.468689,2),math.log(308.875854,2)]
t_1 = [math.log(288.000000,2),math.log(288.000000,2),math.log(296.000000,2),math.log(338.000000,2),math.log(316.000000,2),math.log(305.000000,2),math.log(262.500000,2),math.log(244.875000,2),math.log(254.875000,2),math.log(252.750000,2),math.log(253.171875,2),math.log(253.460938,2),math.log(265.523438,2),math.log(260.191406,2),math.log(290.864258,2),math.log(275.013184,2),math.log(276.058350,2),math.log(288.379761,2),math.log(323.467468,2),math.log(385.653381,2)]
t_2 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(284.000000,2),math.log(274.000000,2),math.log(252.500000,2),math.log(210.750000,2),math.log(235.750000,2),math.log(239.312500,2),math.log(228.093750,2),math.log(246.687500,2),math.log(219.453125,2),math.log(274.351562,2),math.log(268.513672,2),math.log(240.532227,2),math.log(253.416504,2),math.log(261.940918,2),math.log(294.409546,2),math.log(278.190430,2),math.log(270.235992,2)]
t_3 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(260.000000,2),math.log(263.000000,2),math.log(247.750000,2),math.log(236.500000,2),math.log(251.125000,2),math.log(240.343750,2),math.log(213.046875,2),math.log(249.789062,2),math.log(276.511719,2),math.log(241.669922,2),math.log(283.480469,2),math.log(279.045410,2),math.log(288.388672,2),math.log(278.292358,2),math.log(328.439880,2),math.log(312.234497,2)]
t_4 = [math.log(256.000000,2),math.log(280.000000,2),math.log(300.000000,2),math.log(252.000000,2),math.log(233.000000,2),math.log(272.500000,2),math.log(265.500000,2),math.log(277.375000,2),math.log(257.937500,2),math.log(243.687500,2),math.log(242.765625,2),math.log(249.085938,2),math.log(263.078125,2),math.log(232.052734,2),math.log(248.137695,2),math.log(267.150879,2),math.log(260.942139,2),math.log(245.261230,2),math.log(320.434265,2),math.log(317.756866,2)]
t_5 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(255.000000,2),math.log(273.000000,2),math.log(268.000000,2),math.log(241.750000,2),math.log(238.687500,2),math.log(244.812500,2),math.log(229.375000,2),math.log(212.617188,2),math.log(237.183594,2),math.log(243.412109,2),math.log(259.397461,2),math.log(253.656738,2),math.log(250.001465,2),math.log(268.768921,2),math.log(281.884155,2),math.log(321.284729,2)]
t_6 = [math.log(256.000000,2),math.log(216.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(221.000000,2),math.log(216.000000,2),math.log(234.500000,2),math.log(248.625000,2),math.log(248.687500,2),math.log(267.000000,2),math.log(257.453125,2),math.log(274.273438,2),math.log(282.757812,2),math.log(278.250000,2),math.log(268.724609,2),math.log(283.607910,2),math.log(299.342773,2),math.log(305.585815,2),math.log(350.423889,2),math.log(358.990631,2)]
t_7 = [math.log(240.000000,2),math.log(232.000000,2),math.log(204.000000,2),math.log(242.000000,2),math.log(251.000000,2),math.log(243.000000,2),math.log(268.500000,2),math.log(286.125000,2),math.log(316.750000,2),math.log(302.500000,2),math.log(254.234375,2),math.log(241.718750,2),math.log(251.347656,2),math.log(265.677734,2),math.log(254.915039,2),math.log(295.965332,2),math.log(265.899902,2),math.log(283.648193,2),math.log(299.726624,2),math.log(344.114838,2)]
t_8 = [math.log(272.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(260.000000,2),math.log(268.750000,2),math.log(301.125000,2),math.log(304.062500,2),math.log(309.500000,2),math.log(281.390625,2),math.log(267.406250,2),math.log(228.796875,2),math.log(227.464844,2),math.log(235.608398,2),math.log(273.888184,2),math.log(256.500977,2),math.log(247.520142,2),math.log(270.627869,2),math.log(327.046326,2)]
t_9 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(269.000000,2),math.log(241.000000,2),math.log(253.250000,2),math.log(261.750000,2),math.log(236.375000,2),math.log(269.218750,2),math.log(248.859375,2),math.log(252.882812,2),math.log(267.652344,2),math.log(264.531250,2),math.log(298.339844,2),math.log(271.821777,2),math.log(272.454102,2),math.log(284.062744,2),math.log(333.029358,2),math.log(349.097900,2)]
t_10 = [math.log(224.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(232.000000,2),math.log(230.000000,2),math.log(270.500000,2),math.log(273.250000,2),math.log(232.375000,2),math.log(223.187500,2),math.log(279.468750,2),math.log(255.812500,2),math.log(241.953125,2),math.log(241.453125,2),math.log(307.300781,2),math.log(329.444336,2),math.log(287.004883,2),math.log(309.244141,2),math.log(378.307007,2),math.log(426.167297,2),math.log(602.914551,2)]
t_11 = [math.log(304.000000,2),math.log(304.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(262.000000,2),math.log(266.000000,2),math.log(255.750000,2),math.log(232.687500,2),math.log(264.468750,2),math.log(251.484375,2),math.log(270.929688,2),math.log(258.632812,2),math.log(236.248047,2),math.log(282.675781,2),math.log(272.444824,2),math.log(272.445801,2),math.log(305.414062,2),math.log(327.179443,2),math.log(370.514404,2)]
t_12 = [math.log(256.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(229.000000,2),math.log(212.000000,2),math.log(235.250000,2),math.log(213.000000,2),math.log(216.937500,2),math.log(202.312500,2),math.log(233.437500,2),math.log(267.625000,2),math.log(280.847656,2),math.log(255.035156,2),math.log(264.214844,2),math.log(283.449219,2),math.log(284.655762,2),math.log(277.518921,2),math.log(267.263733,2),math.log(312.731049,2)]
t_13 = [math.log(256.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(283.000000,2),math.log(260.000000,2),math.log(240.750000,2),math.log(238.250000,2),math.log(215.750000,2),math.log(229.687500,2),math.log(242.000000,2),math.log(258.539062,2),math.log(246.953125,2),math.log(256.570312,2),math.log(272.004883,2),math.log(297.148926,2),math.log(302.024658,2),math.log(305.115234,2),math.log(287.370422,2),math.log(341.879578,2)]
t_14 = [math.log(256.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(246.000000,2),math.log(242.000000,2),math.log(221.500000,2),math.log(243.750000,2),math.log(236.750000,2),math.log(244.250000,2),math.log(253.718750,2),math.log(222.437500,2),math.log(225.789062,2),math.log(255.136719,2),math.log(248.201172,2),math.log(227.951172,2),math.log(230.964844,2),math.log(262.721924,2),math.log(246.821167,2),math.log(294.065552,2),math.log(371.026550,2)]
t_15 = [math.log(224.000000,2),math.log(248.000000,2),math.log(288.000000,2),math.log(228.000000,2),math.log(223.000000,2),math.log(220.500000,2),math.log(265.000000,2),math.log(271.250000,2),math.log(245.250000,2),math.log(274.968750,2),math.log(234.046875,2),math.log(262.593750,2),math.log(263.195312,2),math.log(255.855469,2),math.log(243.414062,2),math.log(234.667969,2),math.log(245.861816,2),math.log(263.548096,2),math.log(314.142029,2),math.log(384.613464,2)]
t_16 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(239.000000,2),math.log(231.000000,2),math.log(240.500000,2),math.log(264.250000,2),math.log(259.625000,2),math.log(261.593750,2),math.log(263.234375,2),math.log(285.875000,2),math.log(282.109375,2),math.log(286.058594,2),math.log(256.931641,2),math.log(292.879883,2),math.log(296.008301,2),math.log(261.777710,2),math.log(307.424927,2),math.log(320.071838,2)]
t_17 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(265.000000,2),math.log(218.000000,2),math.log(242.000000,2),math.log(238.750000,2),math.log(240.625000,2),math.log(203.281250,2),math.log(215.046875,2),math.log(210.390625,2),math.log(203.343750,2),math.log(220.921875,2),math.log(226.488281,2),math.log(271.048340,2),math.log(246.583008,2),math.log(244.748779,2),math.log(244.755127,2),math.log(304.915741,2)]
t_18 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(242.000000,2),math.log(237.000000,2),math.log(223.250000,2),math.log(262.750000,2),math.log(280.437500,2),math.log(267.593750,2),math.log(223.531250,2),math.log(232.734375,2),math.log(254.132812,2),math.log(242.406250,2),math.log(225.073242,2),math.log(222.072266,2),math.log(256.272217,2),math.log(229.243530,2),math.log(253.967651,2),math.log(294.011322,2)]
t_19 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(242.000000,2),math.log(271.000000,2),math.log(234.500000,2),math.log(248.500000,2),math.log(249.937500,2),math.log(266.937500,2),math.log(234.750000,2),math.log(252.203125,2),math.log(228.832031,2),math.log(219.613281,2),math.log(247.693359,2),math.log(240.098633,2),math.log(243.758301,2),math.log(269.683472,2),math.log(279.860474,2),math.log(285.794495,2)]
t_20 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(265.000000,2),math.log(264.500000,2),math.log(217.500000,2),math.log(245.500000,2),math.log(233.875000,2),math.log(241.031250,2),math.log(232.703125,2),math.log(277.718750,2),math.log(266.363281,2),math.log(273.425781,2),math.log(258.872070,2),math.log(266.385742,2),math.log(239.775879,2),math.log(313.068481,2),math.log(268.153076,2),math.log(349.296051,2)]
t_21 = [math.log(288.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(265.000000,2),math.log(278.250000,2),math.log(243.500000,2),math.log(235.562500,2),math.log(227.125000,2),math.log(285.531250,2),math.log(266.062500,2),math.log(248.390625,2),math.log(250.017578,2),math.log(243.041992,2),math.log(233.680664,2),math.log(257.340576,2),math.log(259.282104,2),math.log(279.547546,2),math.log(343.026276,2)]
t_22 = [math.log(272.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(270.000000,2),math.log(253.000000,2),math.log(267.000000,2),math.log(284.500000,2),math.log(247.500000,2),math.log(287.312500,2),math.log(298.250000,2),math.log(272.765625,2),math.log(241.968750,2),math.log(231.285156,2),math.log(245.513672,2),math.log(248.434570,2),math.log(249.141113,2),math.log(249.958008,2),math.log(246.168213,2),math.log(284.431641,2),math.log(340.154999,2)]
t_23 = [math.log(272.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(278.000000,2),math.log(233.000000,2),math.log(249.500000,2),math.log(213.250000,2),math.log(233.750000,2),math.log(260.687500,2),math.log(233.093750,2),math.log(259.593750,2),math.log(257.562500,2),math.log(240.359375,2),math.log(234.144531,2),math.log(261.638672,2),math.log(244.313965,2),math.log(257.954346,2),math.log(255.381714,2),math.log(250.825684,2),math.log(284.592682,2)]
t_24 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(282.000000,2),math.log(277.000000,2),math.log(257.000000,2),math.log(223.250000,2),math.log(235.375000,2),math.log(249.875000,2),math.log(246.375000,2),math.log(246.140625,2),math.log(236.593750,2),math.log(291.472656,2),math.log(288.777344,2),math.log(301.373047,2),math.log(231.838867,2),math.log(228.251465,2),math.log(218.645020,2),math.log(242.828125,2),math.log(290.812775,2)]
t_25 = [math.log(224.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(266.000000,2),math.log(249.000000,2),math.log(228.500000,2),math.log(260.000000,2),math.log(230.625000,2),math.log(225.562500,2),math.log(226.687500,2),math.log(265.375000,2),math.log(244.914062,2),math.log(244.125000,2),math.log(239.769531,2),math.log(238.469727,2),math.log(272.082031,2),math.log(252.796631,2),math.log(280.827881,2),math.log(306.129517,2),math.log(323.575684,2)]
t_26 = [math.log(256.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(296.000000,2),math.log(263.000000,2),math.log(296.000000,2),math.log(281.250000,2),math.log(274.625000,2),math.log(276.687500,2),math.log(302.968750,2),math.log(281.031250,2),math.log(257.890625,2),math.log(264.234375,2),math.log(247.855469,2),math.log(241.905273,2),math.log(239.893555,2),math.log(264.117676,2),math.log(262.082275,2),math.log(341.954224,2),math.log(451.642792,2)]
t_27 = [math.log(256.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(248.000000,2),math.log(233.500000,2),math.log(248.500000,2),math.log(247.875000,2),math.log(269.125000,2),math.log(293.000000,2),math.log(283.031250,2),math.log(277.265625,2),math.log(238.843750,2),math.log(247.349609,2),math.log(248.640625,2),math.log(260.831543,2),math.log(274.030273,2),math.log(270.750977,2),math.log(270.683289,2),math.log(335.691772,2)]
t_28 = [math.log(272.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(250.000000,2),math.log(273.000000,2),math.log(270.500000,2),math.log(269.500000,2),math.log(257.750000,2),math.log(283.250000,2),math.log(281.156250,2),math.log(270.421875,2),math.log(235.609375,2),math.log(263.375000,2),math.log(242.068359,2),math.log(260.143555,2),math.log(248.180664,2),math.log(308.128662,2),math.log(349.448975,2),math.log(328.794556,2),math.log(340.233917,2)]
t_29 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(267.000000,2),math.log(249.000000,2),math.log(233.750000,2),math.log(255.625000,2),math.log(229.812500,2),math.log(279.375000,2),math.log(259.031250,2),math.log(268.304688,2),math.log(287.375000,2),math.log(310.027344,2),math.log(287.947266,2),math.log(280.365723,2),math.log(292.798096,2),math.log(288.419800,2),math.log(338.507263,2),math.log(369.538757,2)]
t_30 = [math.log(240.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(278.000000,2),math.log(255.000000,2),math.log(255.000000,2),math.log(228.250000,2),math.log(226.500000,2),math.log(277.687500,2),math.log(291.937500,2),math.log(253.109375,2),math.log(283.460938,2),math.log(302.273438,2),math.log(305.837891,2),math.log(272.229492,2),math.log(243.358887,2),math.log(253.786865,2),math.log(302.553467,2),math.log(328.388733,2),math.log(402.511475,2)]
t_31 = [math.log(240.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(304.000000,2),math.log(289.000000,2),math.log(272.500000,2),math.log(251.000000,2),math.log(234.000000,2),math.log(248.875000,2),math.log(243.843750,2),math.log(261.781250,2),math.log(227.117188,2),math.log(235.089844,2),math.log(220.677734,2),math.log(242.663086,2),math.log(244.570312,2),math.log(247.637695,2),math.log(260.567993,2),math.log(279.800415,2),math.log(331.988495,2)]
t_32 = [math.log(288.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(263.000000,2),math.log(288.000000,2),math.log(267.750000,2),math.log(223.375000,2),math.log(257.062500,2),math.log(244.500000,2),math.log(229.750000,2),math.log(268.960938,2),math.log(237.691406,2),math.log(200.373047,2),math.log(230.160156,2),math.log(207.661133,2),math.log(224.080566,2),math.log(255.331909,2),math.log(297.411011,2),math.log(289.490814,2)]
t_33 = [math.log(256.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(242.000000,2),math.log(288.000000,2),math.log(294.500000,2),math.log(280.250000,2),math.log(264.500000,2),math.log(246.187500,2),math.log(256.531250,2),math.log(271.890625,2),math.log(253.781250,2),math.log(239.171875,2),math.log(250.593750,2),math.log(265.595703,2),math.log(231.403809,2),math.log(275.431641,2),math.log(326.305298,2),math.log(312.182251,2),math.log(339.538422,2)]
t_34 = [math.log(288.000000,2),math.log(336.000000,2),math.log(284.000000,2),math.log(290.000000,2),math.log(276.000000,2),math.log(295.000000,2),math.log(324.750000,2),math.log(280.375000,2),math.log(246.375000,2),math.log(265.312500,2),math.log(251.765625,2),math.log(256.953125,2),math.log(235.644531,2),math.log(231.755859,2),math.log(241.763672,2),math.log(253.377930,2),math.log(251.844727,2),math.log(256.420776,2),math.log(289.350647,2),math.log(353.244568,2)]
t_35 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(214.000000,2),math.log(268.500000,2),math.log(255.750000,2),math.log(266.375000,2),math.log(279.437500,2),math.log(248.906250,2),math.log(284.640625,2),math.log(263.078125,2),math.log(246.246094,2),math.log(233.613281,2),math.log(242.627930,2),math.log(255.169434,2),math.log(269.313232,2),math.log(272.535278,2),math.log(239.791931,2),math.log(296.236908,2)]
t_36 = [math.log(256.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(252.000000,2),math.log(230.000000,2),math.log(219.250000,2),math.log(229.625000,2),math.log(243.312500,2),math.log(240.718750,2),math.log(229.312500,2),math.log(236.546875,2),math.log(234.519531,2),math.log(268.697266,2),math.log(274.556641,2),math.log(286.712891,2),math.log(282.134521,2),math.log(288.239868,2),math.log(336.053894,2),math.log(418.226807,2)]
t_37 = [math.log(288.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(239.000000,2),math.log(216.500000,2),math.log(232.000000,2),math.log(278.500000,2),math.log(241.500000,2),math.log(257.625000,2),math.log(251.265625,2),math.log(230.609375,2),math.log(235.128906,2),math.log(232.130859,2),math.log(252.782227,2),math.log(237.975586,2),math.log(292.474609,2),math.log(310.696899,2),math.log(261.661560,2),math.log(298.051880,2)]
t_38 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(263.000000,2),math.log(257.500000,2),math.log(237.750000,2),math.log(253.375000,2),math.log(259.562500,2),math.log(258.187500,2),math.log(270.734375,2),math.log(268.960938,2),math.log(258.695312,2),math.log(239.400391,2),math.log(249.706055,2),math.log(246.512207,2),math.log(265.735840,2),math.log(248.251831,2),math.log(305.672546,2),math.log(392.615784,2)]
t_39 = [math.log(256.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(220.000000,2),math.log(234.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(263.875000,2),math.log(266.875000,2),math.log(265.062500,2),math.log(263.218750,2),math.log(255.117188,2),math.log(263.183594,2),math.log(255.941406,2),math.log(273.237305,2),math.log(288.351074,2),math.log(265.635254,2),math.log(309.859863,2),math.log(281.955750,2),math.log(342.829407,2)]
t_40 = [math.log(272.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(280.000000,2),math.log(267.000000,2),math.log(262.000000,2),math.log(238.750000,2),math.log(257.125000,2),math.log(260.812500,2),math.log(261.343750,2),math.log(267.703125,2),math.log(257.203125,2),math.log(234.062500,2),math.log(199.939453,2),math.log(242.182617,2),math.log(250.422852,2),math.log(252.561035,2),math.log(237.765503,2),math.log(235.063904,2),math.log(295.805206,2)]
t_41 = [math.log(272.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(282.000000,2),math.log(290.000000,2),math.log(269.000000,2),math.log(283.750000,2),math.log(254.000000,2),math.log(225.750000,2),math.log(209.937500,2),math.log(253.375000,2),math.log(273.179688,2),math.log(267.285156,2),math.log(269.748047,2),math.log(269.746094,2),math.log(257.379883,2),math.log(263.020752,2),math.log(279.768433,2),math.log(296.937500,2),math.log(343.279877,2)]
t_42 = [math.log(272.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(257.000000,2),math.log(271.500000,2),math.log(245.000000,2),math.log(251.875000,2),math.log(254.750000,2),math.log(295.187500,2),math.log(296.453125,2),math.log(283.046875,2),math.log(267.828125,2),math.log(303.800781,2),math.log(320.965820,2),math.log(295.235352,2),math.log(275.649170,2),math.log(305.333740,2),math.log(320.615051,2),math.log(404.647308,2)]
t_43 = [math.log(256.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(262.000000,2),math.log(278.000000,2),math.log(287.500000,2),math.log(262.750000,2),math.log(262.125000,2),math.log(275.187500,2),math.log(291.468750,2),math.log(296.796875,2),math.log(267.757812,2),math.log(261.695312,2),math.log(278.619141,2),math.log(233.623047,2),math.log(270.531250,2),math.log(262.664062,2),math.log(264.335938,2),math.log(267.122986,2),math.log(303.883362,2)]
t_44 = [math.log(240.000000,2),math.log(240.000000,2),math.log(212.000000,2),math.log(224.000000,2),math.log(223.000000,2),math.log(229.000000,2),math.log(216.750000,2),math.log(228.125000,2),math.log(236.187500,2),math.log(236.875000,2),math.log(235.906250,2),math.log(257.718750,2),math.log(275.656250,2),math.log(249.148438,2),math.log(240.602539,2),math.log(242.536621,2),math.log(257.482910,2),math.log(255.682251,2),math.log(294.189697,2),math.log(307.226257,2)]
t_45 = [math.log(240.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(268.000000,2),math.log(257.000000,2),math.log(268.000000,2),math.log(288.000000,2),math.log(278.625000,2),math.log(241.125000,2),math.log(250.000000,2),math.log(264.890625,2),math.log(255.812500,2),math.log(223.714844,2),math.log(237.693359,2),math.log(240.556641,2),math.log(247.080078,2),math.log(279.122314,2),math.log(286.613159,2),math.log(310.754883,2),math.log(396.867950,2)]
t_46 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(235.000000,2),math.log(223.000000,2),math.log(243.250000,2),math.log(241.375000,2),math.log(263.687500,2),math.log(266.625000,2),math.log(240.296875,2),math.log(273.078125,2),math.log(278.355469,2),math.log(236.687500,2),math.log(264.940430,2),math.log(264.779785,2),math.log(255.730225,2),math.log(275.401001,2),math.log(307.832764,2),math.log(362.405060,2)]
t_47 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(230.000000,2),math.log(227.000000,2),math.log(239.500000,2),math.log(247.000000,2),math.log(236.125000,2),math.log(250.562500,2),math.log(268.500000,2),math.log(240.531250,2),math.log(255.031250,2),math.log(243.761719,2),math.log(253.705078,2),math.log(257.932617,2),math.log(270.495605,2),math.log(262.870605,2),math.log(286.776001,2),math.log(263.649902,2),math.log(281.712952,2)]
t_48 = [math.log(272.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(262.000000,2),math.log(249.000000,2),math.log(275.000000,2),math.log(278.750000,2),math.log(293.375000,2),math.log(292.062500,2),math.log(287.312500,2),math.log(251.937500,2),math.log(261.164062,2),math.log(229.484375,2),math.log(223.505859,2),math.log(216.822266,2),math.log(217.595703,2),math.log(236.011475,2),math.log(272.661133,2),math.log(250.830933,2),math.log(323.462769,2)]
t_49 = [math.log(224.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(262.000000,2),math.log(249.000000,2),math.log(277.500000,2),math.log(267.750000,2),math.log(253.875000,2),math.log(255.812500,2),math.log(254.218750,2),math.log(264.812500,2),math.log(244.734375,2),math.log(223.949219,2),math.log(242.412109,2),math.log(243.595703,2),math.log(241.138672,2),math.log(263.247559,2),math.log(233.692627,2),math.log(279.742065,2),math.log(268.469604,2)]
t_50 = [math.log(288.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(254.000000,2),math.log(234.750000,2),math.log(220.375000,2),math.log(224.750000,2),math.log(229.781250,2),math.log(234.656250,2),math.log(261.007812,2),math.log(278.699219,2),math.log(264.859375,2),math.log(248.411133,2),math.log(282.763184,2),math.log(266.018555,2),math.log(306.490234,2),math.log(300.466614,2),math.log(310.344666,2)]
t_51 = [math.log(256.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(229.000000,2),math.log(208.000000,2),math.log(233.250000,2),math.log(236.250000,2),math.log(301.000000,2),math.log(266.781250,2),math.log(253.609375,2),math.log(256.335938,2),math.log(246.882812,2),math.log(255.837891,2),math.log(228.603516,2),math.log(216.838379,2),math.log(236.742676,2),math.log(286.270508,2),math.log(316.419556,2),math.log(366.749695,2)]
t_52 = [math.log(240.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(254.000000,2),math.log(248.000000,2),math.log(230.500000,2),math.log(217.500000,2),math.log(258.125000,2),math.log(244.812500,2),math.log(277.125000,2),math.log(288.812500,2),math.log(252.968750,2),math.log(241.820312,2),math.log(263.919922,2),math.log(240.518555,2),math.log(245.274414,2),math.log(254.356934,2),math.log(264.668945,2),math.log(258.458069,2),math.log(286.768402,2)]
t_53 = [math.log(256.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(263.000000,2),math.log(251.500000,2),math.log(237.250000,2),math.log(249.875000,2),math.log(264.062500,2),math.log(211.000000,2),math.log(220.562500,2),math.log(220.695312,2),math.log(261.453125,2),math.log(249.822266,2),math.log(274.066406,2),math.log(245.854492,2),math.log(251.306396,2),math.log(250.729980,2),math.log(291.679077,2),math.log(341.501312,2)]
t_54 = [math.log(256.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(258.000000,2),math.log(281.000000,2),math.log(282.500000,2),math.log(254.750000,2),math.log(262.375000,2),math.log(266.000000,2),math.log(253.968750,2),math.log(237.640625,2),math.log(243.742188,2),math.log(240.914062,2),math.log(236.335938,2),math.log(305.173828,2),math.log(283.074219,2),math.log(278.900879,2),math.log(297.870972,2),math.log(320.968750,2),math.log(311.824188,2)]
t_55 = [math.log(272.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(262.000000,2),math.log(253.000000,2),math.log(269.500000,2),math.log(291.250000,2),math.log(234.750000,2),math.log(228.312500,2),math.log(234.312500,2),math.log(235.265625,2),math.log(216.109375,2),math.log(243.968750,2),math.log(248.443359,2),math.log(252.779297,2),math.log(269.574707,2),math.log(252.773926,2),math.log(270.016113,2),math.log(276.812256,2),math.log(323.870667,2)]
t_56 = [math.log(224.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(270.000000,2),math.log(271.000000,2),math.log(281.250000,2),math.log(300.500000,2),math.log(273.375000,2),math.log(265.500000,2),math.log(270.859375,2),math.log(266.656250,2),math.log(285.417969,2),math.log(298.541016,2),math.log(289.065430,2),math.log(287.901855,2),math.log(289.186279,2),math.log(282.536865,2),math.log(306.780090,2),math.log(336.345917,2)]
t_57 = [math.log(272.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(242.250000,2),math.log(237.875000,2),math.log(252.375000,2),math.log(248.375000,2),math.log(263.546875,2),math.log(266.781250,2),math.log(229.335938,2),math.log(256.744141,2),math.log(249.616211,2),math.log(270.964355,2),math.log(284.355713,2),math.log(287.176880,2),math.log(292.885986,2),math.log(315.268890,2)]
t_58 = [math.log(256.000000,2),math.log(288.000000,2),math.log(304.000000,2),math.log(274.000000,2),math.log(256.000000,2),math.log(268.500000,2),math.log(300.000000,2),math.log(305.250000,2),math.log(274.125000,2),math.log(313.125000,2),math.log(291.890625,2),math.log(271.695312,2),math.log(306.378906,2),math.log(268.517578,2),math.log(226.604492,2),math.log(241.312988,2),math.log(298.400635,2),math.log(368.093872,2),math.log(417.346069,2),math.log(603.047333,2)]
t_59 = [math.log(272.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(239.000000,2),math.log(238.500000,2),math.log(239.500000,2),math.log(274.750000,2),math.log(279.812500,2),math.log(283.156250,2),math.log(278.875000,2),math.log(288.500000,2),math.log(253.699219,2),math.log(255.808594,2),math.log(240.832031,2),math.log(260.254883,2),math.log(264.337646,2),math.log(318.670288,2),math.log(394.052124,2),math.log(486.135498,2)]
t_60 = [math.log(240.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(216.000000,2),math.log(208.000000,2),math.log(254.500000,2),math.log(225.500000,2),math.log(244.250000,2),math.log(214.625000,2),math.log(222.875000,2),math.log(249.953125,2),math.log(252.710938,2),math.log(281.378906,2),math.log(262.099609,2),math.log(245.269531,2),math.log(287.789551,2),math.log(251.865234,2),math.log(283.097900,2),math.log(273.034119,2),math.log(288.559998,2)]
t_61 = [math.log(224.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(253.000000,2),math.log(265.000000,2),math.log(261.000000,2),math.log(258.875000,2),math.log(296.312500,2),math.log(282.187500,2),math.log(257.171875,2),math.log(253.906250,2),math.log(227.320312,2),math.log(241.515625,2),math.log(263.684570,2),math.log(273.168945,2),math.log(261.938477,2),math.log(283.264771,2),math.log(333.566711,2),math.log(400.713196,2)]
t_62 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(242.000000,2),math.log(260.000000,2),math.log(274.750000,2),math.log(264.250000,2),math.log(272.437500,2),math.log(285.656250,2),math.log(309.765625,2),math.log(321.867188,2),math.log(308.355469,2),math.log(280.947266,2),math.log(274.710938,2),math.log(262.021973,2),math.log(249.570312,2),math.log(248.999146,2),math.log(307.981506,2),math.log(365.996979,2)]
t_63 = [math.log(256.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(222.000000,2),math.log(214.500000,2),math.log(252.000000,2),math.log(242.250000,2),math.log(260.375000,2),math.log(231.468750,2),math.log(254.843750,2),math.log(256.523438,2),math.log(269.531250,2),math.log(262.146484,2),math.log(289.135742,2),math.log(254.705566,2),math.log(269.703369,2),math.log(318.014648,2),math.log(386.699280,2),math.log(482.757843,2)]
t_64 = [math.log(240.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(241.000000,2),math.log(293.000000,2),math.log(299.250000,2),math.log(260.625000,2),math.log(299.687500,2),math.log(249.750000,2),math.log(249.406250,2),math.log(245.726562,2),math.log(254.445312,2),math.log(263.611328,2),math.log(292.468750,2),math.log(302.423828,2),math.log(279.874268,2),math.log(276.592041,2),math.log(284.879639,2),math.log(292.628082,2)]
t_65 = [math.log(288.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(232.000000,2),math.log(202.000000,2),math.log(238.500000,2),math.log(266.250000,2),math.log(256.062500,2),math.log(277.718750,2),math.log(282.484375,2),math.log(271.359375,2),math.log(253.046875,2),math.log(251.699219,2),math.log(261.457031,2),math.log(232.687500,2),math.log(236.042969,2),math.log(228.550537,2),math.log(252.546814,2),math.log(277.686371,2)]
t_66 = [math.log(256.000000,2),math.log(264.000000,2),math.log(216.000000,2),math.log(242.000000,2),math.log(219.000000,2),math.log(253.000000,2),math.log(246.250000,2),math.log(250.750000,2),math.log(253.875000,2),math.log(264.000000,2),math.log(242.593750,2),math.log(273.273438,2),math.log(291.800781,2),math.log(255.656250,2),math.log(273.848633,2),math.log(264.722656,2),math.log(255.583984,2),math.log(248.887573,2),math.log(296.054321,2),math.log(331.475952,2)]
t_67 = [math.log(272.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(242.000000,2),math.log(253.000000,2),math.log(237.500000,2),math.log(238.500000,2),math.log(288.562500,2),math.log(265.812500,2),math.log(264.734375,2),math.log(303.890625,2),math.log(304.027344,2),math.log(288.207031,2),math.log(292.988281,2),math.log(303.227539,2),math.log(303.629150,2),math.log(311.511841,2),math.log(342.654541,2),math.log(447.197815,2)]
t_68 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(290.000000,2),math.log(255.000000,2),math.log(249.000000,2),math.log(261.750000,2),math.log(232.750000,2),math.log(224.625000,2),math.log(264.843750,2),math.log(254.468750,2),math.log(248.320312,2),math.log(282.902344,2),math.log(237.906250,2),math.log(281.518555,2),math.log(288.863281,2),math.log(261.319092,2),math.log(285.378052,2),math.log(276.179443,2),math.log(295.810944,2)]
t_69 = [math.log(288.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(240.000000,2),math.log(233.000000,2),math.log(247.500000,2),math.log(260.250000,2),math.log(246.875000,2),math.log(254.625000,2),math.log(256.218750,2),math.log(273.484375,2),math.log(264.320312,2),math.log(271.394531,2),math.log(283.806641,2),math.log(265.628906,2),math.log(276.096680,2),math.log(281.796631,2),math.log(266.984497,2),math.log(249.930115,2),math.log(295.277710,2)]
t_70 = [math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(266.500000,2),math.log(251.750000,2),math.log(268.000000,2),math.log(289.500000,2),math.log(248.562500,2),math.log(212.000000,2),math.log(288.570312,2),math.log(289.128906,2),math.log(259.816406,2),math.log(251.247070,2),math.log(239.222168,2),math.log(255.292480,2),math.log(283.872559,2),math.log(310.056702,2),math.log(332.228607,2)]
t_71 = [math.log(272.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(302.000000,2),math.log(270.000000,2),math.log(272.000000,2),math.log(252.625000,2),math.log(235.812500,2),math.log(250.000000,2),math.log(265.531250,2),math.log(257.593750,2),math.log(253.738281,2),math.log(265.732422,2),math.log(219.038086,2),math.log(208.166016,2),math.log(246.353760,2),math.log(276.747192,2),math.log(336.050049,2),math.log(426.685883,2)]
t_72 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(238.000000,2),math.log(239.500000,2),math.log(249.500000,2),math.log(269.375000,2),math.log(269.812500,2),math.log(275.531250,2),math.log(248.546875,2),math.log(277.781250,2),math.log(277.945312,2),math.log(290.826172,2),math.log(283.147461,2),math.log(308.148438,2),math.log(293.937744,2),math.log(279.818237,2),math.log(302.294983,2),math.log(382.924377,2)]
t_73 = [math.log(256.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(261.000000,2),math.log(266.500000,2),math.log(273.250000,2),math.log(265.375000,2),math.log(246.312500,2),math.log(251.562500,2),math.log(217.218750,2),math.log(252.570312,2),math.log(249.523438,2),math.log(259.355469,2),math.log(269.919922,2),math.log(285.944824,2),math.log(233.468750,2),math.log(239.445679,2),math.log(283.658203,2),math.log(311.455933,2)]
t_74 = [math.log(256.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(290.000000,2),math.log(297.000000,2),math.log(261.250000,2),math.log(273.000000,2),math.log(265.625000,2),math.log(241.531250,2),math.log(241.062500,2),math.log(233.492188,2),math.log(249.382812,2),math.log(227.986328,2),math.log(284.099609,2),math.log(300.770996,2),math.log(297.930664,2),math.log(329.815430,2),math.log(348.934143,2),math.log(483.468018,2)]
t_75 = [math.log(256.000000,2),math.log(272.000000,2),math.log(308.000000,2),math.log(240.000000,2),math.log(242.000000,2),math.log(269.500000,2),math.log(267.250000,2),math.log(245.500000,2),math.log(275.500000,2),math.log(265.281250,2),math.log(246.359375,2),math.log(257.281250,2),math.log(260.726562,2),math.log(240.007812,2),math.log(268.032227,2),math.log(258.445312,2),math.log(258.662598,2),math.log(284.729126,2),math.log(309.177979,2),math.log(369.781403,2)]
t_76 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(230.000000,2),math.log(229.000000,2),math.log(263.500000,2),math.log(276.750000,2),math.log(227.750000,2),math.log(239.750000,2),math.log(221.093750,2),math.log(230.968750,2),math.log(251.664062,2),math.log(254.738281,2),math.log(249.832031,2),math.log(259.570312,2),math.log(251.056152,2),math.log(249.048828,2),math.log(270.841553,2),math.log(279.067017,2),math.log(301.660431,2)]
t_77 = [math.log(240.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(240.000000,2),math.log(249.500000,2),math.log(257.250000,2),math.log(268.625000,2),math.log(271.937500,2),math.log(292.343750,2),math.log(271.781250,2),math.log(276.289062,2),math.log(285.320312,2),math.log(266.609375,2),math.log(259.146484,2),math.log(267.901855,2),math.log(275.340088,2),math.log(300.942749,2),math.log(325.412720,2),math.log(326.861237,2)]
t_78 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(243.000000,2),math.log(229.000000,2),math.log(241.000000,2),math.log(242.750000,2),math.log(284.312500,2),math.log(282.031250,2),math.log(268.031250,2),math.log(266.242188,2),math.log(267.628906,2),math.log(244.687500,2),math.log(229.386719,2),math.log(248.719238,2),math.log(237.319092,2),math.log(283.549561,2),math.log(307.463135,2),math.log(324.071747,2)]
t_79 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(235.000000,2),math.log(214.500000,2),math.log(293.000000,2),math.log(255.875000,2),math.log(262.312500,2),math.log(257.750000,2),math.log(228.125000,2),math.log(244.578125,2),math.log(255.308594,2),math.log(229.482422,2),math.log(226.855469,2),math.log(221.777344,2),math.log(245.118164,2),math.log(257.941162,2),math.log(275.340942,2),math.log(334.983673,2)]
t_80 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(219.000000,2),math.log(213.000000,2),math.log(216.250000,2),math.log(242.750000,2),math.log(246.500000,2),math.log(245.750000,2),math.log(217.125000,2),math.log(271.875000,2),math.log(267.218750,2),math.log(287.486328,2),math.log(241.696289,2),math.log(244.056152,2),math.log(294.519531,2),math.log(271.863892,2),math.log(265.270569,2),math.log(309.243073,2)]
t_81 = [math.log(272.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(253.500000,2),math.log(244.250000,2),math.log(227.875000,2),math.log(216.687500,2),math.log(246.906250,2),math.log(244.859375,2),math.log(266.773438,2),math.log(278.929688,2),math.log(261.019531,2),math.log(262.287109,2),math.log(284.200684,2),math.log(276.294678,2),math.log(289.706787,2),math.log(299.029602,2),math.log(307.530914,2)]
t_82 = [math.log(272.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(280.000000,2),math.log(302.000000,2),math.log(287.500000,2),math.log(276.000000,2),math.log(279.875000,2),math.log(270.375000,2),math.log(257.781250,2),math.log(246.671875,2),math.log(279.523438,2),math.log(257.613281,2),math.log(248.238281,2),math.log(232.161133,2),math.log(245.477539,2),math.log(238.299316,2),math.log(215.960571,2),math.log(252.983459,2),math.log(298.457275,2)]
t_83 = [math.log(272.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(276.000000,2),math.log(292.000000,2),math.log(285.000000,2),math.log(283.500000,2),math.log(264.375000,2),math.log(241.750000,2),math.log(232.875000,2),math.log(250.140625,2),math.log(227.921875,2),math.log(250.824219,2),math.log(255.294922,2),math.log(221.342773,2),math.log(225.872559,2),math.log(235.666748,2),math.log(235.399414,2),math.log(270.174316,2),math.log(323.634064,2)]
t_84 = [math.log(256.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(246.000000,2),math.log(279.000000,2),math.log(234.000000,2),math.log(242.000000,2),math.log(277.750000,2),math.log(249.625000,2),math.log(267.781250,2),math.log(292.812500,2),math.log(284.828125,2),math.log(285.417969,2),math.log(274.099609,2),math.log(278.575195,2),math.log(262.813965,2),math.log(276.452393,2),math.log(261.232056,2),math.log(258.713318,2),math.log(320.514954,2)]
t_85 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(259.000000,2),math.log(282.750000,2),math.log(259.500000,2),math.log(235.062500,2),math.log(241.437500,2),math.log(278.968750,2),math.log(273.492188,2),math.log(241.597656,2),math.log(249.669922,2),math.log(261.033203,2),math.log(260.017090,2),math.log(249.583740,2),math.log(288.234619,2),math.log(290.929504,2),math.log(328.290009,2)]
t_86 = [math.log(288.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(303.000000,2),math.log(278.500000,2),math.log(279.500000,2),math.log(279.750000,2),math.log(269.937500,2),math.log(258.031250,2),math.log(258.015625,2),math.log(245.078125,2),math.log(276.753906,2),math.log(256.718750,2),math.log(268.193359,2),math.log(289.477051,2),math.log(306.784424,2),math.log(314.284058,2),math.log(336.933472,2),math.log(384.614197,2)]
t_87 = [math.log(240.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(316.000000,2),math.log(272.500000,2),math.log(223.500000,2),math.log(273.500000,2),math.log(280.125000,2),math.log(272.093750,2),math.log(252.218750,2),math.log(249.273438,2),math.log(266.000000,2),math.log(238.748047,2),math.log(243.480469,2),math.log(260.672852,2),math.log(286.487793,2),math.log(306.140503,2),math.log(312.644592,2),math.log(365.858276,2)]
t_88 = [math.log(304.000000,2),math.log(288.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(235.000000,2),math.log(224.500000,2),math.log(211.000000,2),math.log(207.125000,2),math.log(224.125000,2),math.log(242.281250,2),math.log(230.171875,2),math.log(230.945312,2),math.log(225.484375,2),math.log(233.257812,2),math.log(231.699219,2),math.log(255.920410,2),math.log(296.866211,2),math.log(252.718262,2),math.log(296.947327,2),math.log(281.579865,2)]
t_89 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(220.000000,2),math.log(217.000000,2),math.log(263.500000,2),math.log(279.250000,2),math.log(276.125000,2),math.log(279.187500,2),math.log(266.562500,2),math.log(260.687500,2),math.log(237.062500,2),math.log(244.179688,2),math.log(265.908203,2),math.log(247.141602,2),math.log(268.017090,2),math.log(247.152588,2),math.log(266.521240,2),math.log(294.218018,2),math.log(278.521332,2)]
t_90 = [math.log(224.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(226.000000,2),math.log(269.000000,2),math.log(242.000000,2),math.log(240.250000,2),math.log(254.875000,2),math.log(259.125000,2),math.log(285.937500,2),math.log(305.437500,2),math.log(241.632812,2),math.log(237.589844,2),math.log(212.685547,2),math.log(226.017578,2),math.log(216.552734,2),math.log(236.138916,2),math.log(269.105591,2),math.log(333.929565,2),math.log(427.901123,2)]
t_91 = [math.log(272.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(288.000000,2),math.log(255.000000,2),math.log(235.000000,2),math.log(259.500000,2),math.log(252.500000,2),math.log(264.937500,2),math.log(291.718750,2),math.log(260.218750,2),math.log(255.867188,2),math.log(267.757812,2),math.log(292.552734,2),math.log(261.004883,2),math.log(277.181641,2),math.log(240.388672,2),math.log(251.896484,2),math.log(287.524414,2),math.log(301.931091,2)]
t_92 = [math.log(272.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(259.000000,2),math.log(258.500000,2),math.log(270.250000,2),math.log(252.375000,2),math.log(254.187500,2),math.log(257.062500,2),math.log(244.656250,2),math.log(247.882812,2),math.log(250.976562,2),math.log(249.732422,2),math.log(267.458984,2),math.log(249.415527,2),math.log(261.283203,2),math.log(246.048950,2),math.log(271.397278,2),math.log(271.441681,2)]
t_93 = [math.log(272.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(235.000000,2),math.log(255.500000,2),math.log(268.750000,2),math.log(282.375000,2),math.log(277.312500,2),math.log(280.875000,2),math.log(221.625000,2),math.log(257.117188,2),math.log(213.222656,2),math.log(251.060547,2),math.log(277.253906,2),math.log(260.282227,2),math.log(293.294189,2),math.log(320.845581,2),math.log(333.095581,2),math.log(387.660645,2)]
t_94 = [math.log(256.000000,2),math.log(304.000000,2),math.log(312.000000,2),math.log(314.000000,2),math.log(294.000000,2),math.log(257.000000,2),math.log(270.000000,2),math.log(237.000000,2),math.log(243.750000,2),math.log(219.156250,2),math.log(225.187500,2),math.log(220.820312,2),math.log(241.667969,2),math.log(280.251953,2),math.log(271.083008,2),math.log(268.629395,2),math.log(264.311768,2),math.log(298.408081,2),math.log(307.303894,2),math.log(354.267853,2)]
t_95 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(246.000000,2),math.log(228.000000,2),math.log(222.500000,2),math.log(232.375000,2),math.log(236.750000,2),math.log(209.968750,2),math.log(253.734375,2),math.log(226.445312,2),math.log(260.335938,2),math.log(233.390625,2),math.log(244.095703,2),math.log(226.783691,2),math.log(256.390869,2),math.log(264.861328,2),math.log(260.137024,2),math.log(357.853729,2)]
t_96 = [math.log(272.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(324.000000,2),math.log(306.000000,2),math.log(294.500000,2),math.log(227.000000,2),math.log(202.125000,2),math.log(233.875000,2),math.log(224.687500,2),math.log(247.796875,2),math.log(259.093750,2),math.log(296.496094,2),math.log(297.312500,2),math.log(264.997070,2),math.log(299.207520,2),math.log(244.761230,2),math.log(250.467285,2),math.log(293.354126,2),math.log(348.347809,2)]
t_97 = [math.log(256.000000,2),math.log(288.000000,2),math.log(268.000000,2),math.log(234.000000,2),math.log(219.000000,2),math.log(254.500000,2),math.log(216.250000,2),math.log(223.375000,2),math.log(253.125000,2),math.log(257.343750,2),math.log(243.687500,2),math.log(245.484375,2),math.log(260.683594,2),math.log(229.539062,2),math.log(253.895508,2),math.log(241.581543,2),math.log(252.251465,2),math.log(254.186523,2),math.log(256.187439,2),math.log(362.662384,2)]
t_98 = [math.log(272.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(302.000000,2),math.log(271.000000,2),math.log(267.500000,2),math.log(257.000000,2),math.log(222.375000,2),math.log(250.937500,2),math.log(241.906250,2),math.log(249.000000,2),math.log(260.414062,2),math.log(268.257812,2),math.log(289.322266,2),math.log(261.005859,2),math.log(238.712402,2),math.log(241.709473,2),math.log(286.559448,2),math.log(257.179321,2),math.log(281.150177,2)]
t_99 = [math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(259.500000,2),math.log(257.250000,2),math.log(257.375000,2),math.log(233.187500,2),math.log(256.406250,2),math.log(268.859375,2),math.log(294.093750,2),math.log(260.242188,2),math.log(272.712891,2),math.log(248.912109,2),math.log(258.348145,2),math.log(263.098389,2),math.log(278.149902,2),math.log(297.682251,2),math.log(372.827209,2)]
t_100 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(238.000000,2),math.log(285.000000,2),math.log(263.500000,2),math.log(286.500000,2),math.log(250.000000,2),math.log(253.437500,2),math.log(275.218750,2),math.log(296.437500,2),math.log(295.929688,2),math.log(304.449219,2),math.log(263.982422,2),math.log(254.847656,2),math.log(229.976562,2),math.log(232.915771,2),math.log(255.342285,2),math.log(274.247986,2),math.log(317.854126,2)]
t_101 = [math.log(288.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(258.000000,2),math.log(251.000000,2),math.log(212.500000,2),math.log(242.250000,2),math.log(238.500000,2),math.log(241.750000,2),math.log(238.250000,2),math.log(266.734375,2),math.log(293.500000,2),math.log(276.851562,2),math.log(261.193359,2),math.log(282.851562,2),math.log(253.341309,2),math.log(271.228271,2),math.log(258.972778,2),math.log(298.050354,2),math.log(278.033234,2)]
t_102 = [math.log(224.000000,2),math.log(208.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(251.000000,2),math.log(228.000000,2),math.log(262.750000,2),math.log(241.625000,2),math.log(224.375000,2),math.log(205.468750,2),math.log(240.703125,2),math.log(220.812500,2),math.log(267.781250,2),math.log(291.798828,2),math.log(293.884766,2),math.log(271.439453,2),math.log(214.811768,2),math.log(237.241211,2),math.log(262.441284,2),math.log(321.053925,2)]
t_103 = [math.log(240.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(298.000000,2),math.log(285.000000,2),math.log(253.250000,2),math.log(250.250000,2),math.log(255.062500,2),math.log(244.281250,2),math.log(227.625000,2),math.log(242.640625,2),math.log(229.429688,2),math.log(248.462891,2),math.log(279.350586,2),math.log(269.560547,2),math.log(276.863525,2),math.log(281.189087,2),math.log(304.151001,2),math.log(327.227478,2)]
t_104 = [math.log(288.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(228.000000,2),math.log(206.000000,2),math.log(213.750000,2),math.log(251.375000,2),math.log(223.312500,2),math.log(215.312500,2),math.log(212.500000,2),math.log(239.781250,2),math.log(225.281250,2),math.log(259.847656,2),math.log(259.147461,2),math.log(259.372559,2),math.log(252.723389,2),math.log(258.941650,2),math.log(291.699524,2),math.log(302.423187,2)]
t_105 = [math.log(224.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(229.000000,2),math.log(218.000000,2),math.log(209.750000,2),math.log(228.375000,2),math.log(231.000000,2),math.log(265.656250,2),math.log(275.203125,2),math.log(248.882812,2),math.log(249.863281,2),math.log(249.238281,2),math.log(297.066406,2),math.log(258.592285,2),math.log(253.575684,2),math.log(275.455566,2),math.log(308.070374,2),math.log(306.200928,2)]
t_106 = [math.log(288.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(241.000000,2),math.log(275.000000,2),math.log(306.750000,2),math.log(286.375000,2),math.log(238.562500,2),math.log(252.187500,2),math.log(217.390625,2),math.log(233.234375,2),math.log(256.210938,2),math.log(244.968750,2),math.log(240.019531,2),math.log(260.637695,2),math.log(280.182129,2),math.log(316.269897,2),math.log(397.321777,2),math.log(437.401581,2)]
t_107 = [math.log(240.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(254.000000,2),math.log(250.000000,2),math.log(212.000000,2),math.log(259.000000,2),math.log(257.125000,2),math.log(258.000000,2),math.log(237.750000,2),math.log(226.234375,2),math.log(243.960938,2),math.log(250.015625,2),math.log(260.058594,2),math.log(252.824219,2),math.log(274.170410,2),math.log(227.454590,2),math.log(259.741577,2),math.log(301.447632,2),math.log(358.105225,2)]
t_108 = [math.log(320.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(270.000000,2),math.log(286.000000,2),math.log(286.000000,2),math.log(290.750000,2),math.log(251.750000,2),math.log(196.312500,2),math.log(246.312500,2),math.log(242.421875,2),math.log(262.125000,2),math.log(258.886719,2),math.log(290.689453,2),math.log(264.579102,2),math.log(233.812012,2),math.log(237.691650,2),math.log(235.489136,2),math.log(231.501709,2),math.log(321.040344,2)]
t_109 = [math.log(240.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(294.000000,2),math.log(281.000000,2),math.log(279.000000,2),math.log(300.625000,2),math.log(232.125000,2),math.log(235.937500,2),math.log(254.468750,2),math.log(255.218750,2),math.log(273.968750,2),math.log(254.667969,2),math.log(258.433594,2),math.log(272.654785,2),math.log(270.026611,2),math.log(344.303467,2),math.log(359.316589,2),math.log(419.245300,2)]
t_110 = [math.log(224.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(285.000000,2),math.log(276.750000,2),math.log(277.000000,2),math.log(315.000000,2),math.log(309.281250,2),math.log(280.750000,2),math.log(247.710938,2),math.log(263.953125,2),math.log(248.589844,2),math.log(240.769531,2),math.log(254.985840,2),math.log(269.192139,2),math.log(274.190063,2),math.log(277.549561,2),math.log(322.534058,2)]
t_111 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(214.000000,2),math.log(241.000000,2),math.log(260.500000,2),math.log(309.000000,2),math.log(284.750000,2),math.log(249.812500,2),math.log(227.687500,2),math.log(249.390625,2),math.log(289.656250,2),math.log(252.281250,2),math.log(278.865234,2),math.log(274.899414,2),math.log(269.514648,2),math.log(296.911377,2),math.log(254.353882,2),math.log(294.205811,2),math.log(383.276611,2)]
t_112 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(246.000000,2),math.log(255.500000,2),math.log(219.750000,2),math.log(255.875000,2),math.log(251.125000,2),math.log(272.968750,2),math.log(306.890625,2),math.log(287.726562,2),math.log(277.308594,2),math.log(270.142578,2),math.log(256.526367,2),math.log(319.361816,2),math.log(331.049072,2),math.log(323.120605,2),math.log(270.771851,2),math.log(331.471252,2)]
t_113 = [math.log(240.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(245.000000,2),math.log(249.000000,2),math.log(273.750000,2),math.log(255.375000,2),math.log(255.687500,2),math.log(202.156250,2),math.log(247.828125,2),math.log(234.484375,2),math.log(224.421875,2),math.log(246.552734,2),math.log(214.415039,2),math.log(248.414062,2),math.log(249.194824,2),math.log(302.559570,2),math.log(296.632507,2),math.log(292.628357,2)]
t_114 = [math.log(240.000000,2),math.log(312.000000,2),math.log(304.000000,2),math.log(354.000000,2),math.log(283.000000,2),math.log(240.000000,2),math.log(223.500000,2),math.log(253.125000,2),math.log(267.000000,2),math.log(232.562500,2),math.log(244.515625,2),math.log(234.804688,2),math.log(225.316406,2),math.log(207.326172,2),math.log(251.245117,2),math.log(246.166992,2),math.log(259.400391,2),math.log(274.324097,2),math.log(264.151123,2),math.log(273.574341,2)]
t_115 = [math.log(240.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(256.000000,2),math.log(240.250000,2),math.log(294.875000,2),math.log(262.812500,2),math.log(241.812500,2),math.log(250.546875,2),math.log(227.976562,2),math.log(212.554688,2),math.log(209.935547,2),math.log(219.120117,2),math.log(271.066895,2),math.log(308.750732,2),math.log(339.309082,2),math.log(373.641174,2),math.log(498.947876,2)]
t_116 = [math.log(256.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(238.000000,2),math.log(245.000000,2),math.log(244.500000,2),math.log(241.000000,2),math.log(264.500000,2),math.log(288.562500,2),math.log(272.968750,2),math.log(291.562500,2),math.log(232.148438,2),math.log(269.058594,2),math.log(257.792969,2),math.log(287.170898,2),math.log(292.700195,2),math.log(226.078857,2),math.log(232.714355,2),math.log(228.691284,2),math.log(235.233185,2)]
t_117 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(274.000000,2),math.log(260.000000,2),math.log(224.500000,2),math.log(242.250000,2),math.log(237.437500,2),math.log(270.375000,2),math.log(243.640625,2),math.log(250.992188,2),math.log(234.878906,2),math.log(264.771484,2),math.log(269.898438,2),math.log(244.336426,2),math.log(242.416992,2),math.log(270.904419,2),math.log(295.144714,2),math.log(306.609192,2)]
t_118 = [math.log(288.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(275.000000,2),math.log(251.000000,2),math.log(265.000000,2),math.log(238.750000,2),math.log(234.125000,2),math.log(214.781250,2),math.log(217.125000,2),math.log(218.125000,2),math.log(213.226562,2),math.log(229.890625,2),math.log(273.121094,2),math.log(270.100098,2),math.log(305.807617,2),math.log(343.858154,2),math.log(280.934753,2),math.log(313.228668,2)]
t_119 = [math.log(224.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(266.000000,2),math.log(248.000000,2),math.log(281.500000,2),math.log(254.000000,2),math.log(235.750000,2),math.log(251.937500,2),math.log(280.875000,2),math.log(311.578125,2),math.log(303.781250,2),math.log(301.253906,2),math.log(278.863281,2),math.log(272.699219,2),math.log(268.955078,2),math.log(282.037354,2),math.log(279.917725,2),math.log(305.704712,2),math.log(358.889557,2)]
t_120 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(241.000000,2),math.log(244.000000,2),math.log(257.000000,2),math.log(263.625000,2),math.log(236.812500,2),math.log(243.812500,2),math.log(271.312500,2),math.log(224.835938,2),math.log(213.511719,2),math.log(201.382812,2),math.log(243.406250,2),math.log(270.721191,2),math.log(249.384033,2),math.log(277.765625,2),math.log(317.948059,2),math.log(320.929413,2)]
t_121 = [math.log(272.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(241.500000,2),math.log(235.000000,2),math.log(260.375000,2),math.log(249.125000,2),math.log(286.062500,2),math.log(244.593750,2),math.log(254.937500,2),math.log(243.546875,2),math.log(270.398438,2),math.log(247.367188,2),math.log(280.337402,2),math.log(299.833740,2),math.log(325.681519,2),math.log(341.035645,2),math.log(379.749542,2)]
t_122 = [math.log(304.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(262.000000,2),math.log(294.000000,2),math.log(271.000000,2),math.log(254.750000,2),math.log(240.375000,2),math.log(266.750000,2),math.log(278.812500,2),math.log(262.671875,2),math.log(243.601562,2),math.log(244.808594,2),math.log(266.355469,2),math.log(240.552734,2),math.log(254.505371,2),math.log(278.216553,2),math.log(311.341675,2),math.log(406.365906,2),math.log(584.818268,2)]
t_123 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(268.000000,2),math.log(235.000000,2),math.log(276.000000,2),math.log(277.375000,2),math.log(305.312500,2),math.log(289.218750,2),math.log(323.109375,2),math.log(293.218750,2),math.log(261.496094,2),math.log(239.628906,2),math.log(223.933594,2),math.log(246.570312,2),math.log(257.108154,2),math.log(319.557373,2),math.log(381.741882,2),math.log(456.628479,2)]
t_124 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(278.000000,2),math.log(230.000000,2),math.log(235.000000,2),math.log(228.750000,2),math.log(256.875000,2),math.log(265.500000,2),math.log(239.406250,2),math.log(244.843750,2),math.log(258.937500,2),math.log(254.640625,2),math.log(248.652344,2),math.log(250.501953,2),math.log(277.477051,2),math.log(309.096191,2),math.log(292.754517,2),math.log(302.105896,2),math.log(367.568970,2)]
t_125 = [math.log(256.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(270.000000,2),math.log(257.000000,2),math.log(207.750000,2),math.log(274.000000,2),math.log(262.312500,2),math.log(280.843750,2),math.log(258.703125,2),math.log(314.187500,2),math.log(299.300781,2),math.log(291.332031,2),math.log(261.373047,2),math.log(285.270020,2),math.log(255.926758,2),math.log(264.080688,2),math.log(300.298950,2),math.log(347.296722,2)]
t_126 = [math.log(240.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(222.000000,2),math.log(244.000000,2),math.log(256.500000,2),math.log(252.000000,2),math.log(239.875000,2),math.log(243.000000,2),math.log(249.218750,2),math.log(262.937500,2),math.log(231.156250,2),math.log(197.121094,2),math.log(218.763672,2),math.log(241.120117,2),math.log(223.639648,2),math.log(222.610596,2),math.log(227.846436,2),math.log(309.243958,2),math.log(405.187958,2)]
t_127 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(246.000000,2),math.log(263.000000,2),math.log(233.000000,2),math.log(212.000000,2),math.log(231.250000,2),math.log(245.937500,2),math.log(219.000000,2),math.log(253.750000,2),math.log(212.835938,2),math.log(236.503906,2),math.log(232.818359,2),math.log(256.574219,2),math.log(235.615234,2),math.log(244.583984,2),math.log(287.645386,2),math.log(362.780396,2),math.log(516.011047,2)]
t_128 = [math.log(304.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(276.000000,2),math.log(242.000000,2),math.log(238.000000,2),math.log(244.000000,2),math.log(252.125000,2),math.log(233.562500,2),math.log(233.031250,2),math.log(240.937500,2),math.log(268.812500,2),math.log(235.441406,2),math.log(243.894531,2),math.log(266.639648,2),math.log(239.623535,2),math.log(243.339111,2),math.log(240.584961,2),math.log(267.291870,2),math.log(294.183807,2)]
t_129 = [math.log(240.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(253.500000,2),math.log(241.250000,2),math.log(266.625000,2),math.log(237.812500,2),math.log(250.906250,2),math.log(272.984375,2),math.log(267.781250,2),math.log(222.757812,2),math.log(212.501953,2),math.log(219.541016,2),math.log(248.922363,2),math.log(204.124756,2),math.log(269.536987,2),math.log(284.001343,2),math.log(355.603027,2)]
t_130 = [math.log(240.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(268.500000,2),math.log(281.750000,2),math.log(274.000000,2),math.log(270.750000,2),math.log(252.968750,2),math.log(247.562500,2),math.log(287.007812,2),math.log(230.898438,2),math.log(271.820312,2),math.log(295.191406,2),math.log(337.590820,2),math.log(288.274414,2),math.log(273.075928,2),math.log(309.324097,2),math.log(298.718994,2)]
t_131 = [math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(271.000000,2),math.log(258.500000,2),math.log(240.250000,2),math.log(276.375000,2),math.log(255.250000,2),math.log(283.187500,2),math.log(285.953125,2),math.log(299.523438,2),math.log(289.609375,2),math.log(266.292969,2),math.log(253.917969,2),math.log(263.674805,2),math.log(279.878174,2),math.log(303.730835,2),math.log(334.916077,2),math.log(353.233612,2)]
t_132 = [math.log(272.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(272.000000,2),math.log(255.500000,2),math.log(259.750000,2),math.log(269.000000,2),math.log(261.937500,2),math.log(218.625000,2),math.log(205.109375,2),math.log(248.898438,2),math.log(246.089844,2),math.log(247.150391,2),math.log(263.211914,2),math.log(259.068848,2),math.log(261.520508,2),math.log(224.411621,2),math.log(256.670654,2),math.log(318.093201,2)]
t_133 = [math.log(224.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(262.000000,2),math.log(293.000000,2),math.log(264.000000,2),math.log(259.000000,2),math.log(256.750000,2),math.log(258.062500,2),math.log(266.562500,2),math.log(251.843750,2),math.log(270.335938,2),math.log(251.445312,2),math.log(242.177734,2),math.log(263.946289,2),math.log(241.393555,2),math.log(285.189209,2),math.log(261.505493,2),math.log(270.847839,2),math.log(269.227936,2)]
t_134 = [math.log(256.000000,2),math.log(256.000000,2),math.log(292.000000,2),math.log(274.000000,2),math.log(255.000000,2),math.log(295.000000,2),math.log(267.000000,2),math.log(264.250000,2),math.log(247.812500,2),math.log(217.625000,2),math.log(226.296875,2),math.log(240.023438,2),math.log(208.531250,2),math.log(233.720703,2),math.log(264.953125,2),math.log(261.957520,2),math.log(265.678467,2),math.log(288.387939,2),math.log(341.409241,2),math.log(391.599823,2)]
t_135 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(278.000000,2),math.log(244.000000,2),math.log(233.500000,2),math.log(217.000000,2),math.log(197.875000,2),math.log(219.437500,2),math.log(235.125000,2),math.log(253.500000,2),math.log(238.429688,2),math.log(275.707031,2),math.log(252.888672,2),math.log(260.206055,2),math.log(252.087891,2),math.log(251.065430,2),math.log(253.421631,2),math.log(278.759766,2),math.log(334.340973,2)]
t_136 = [math.log(224.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(248.000000,2),math.log(263.000000,2),math.log(263.000000,2),math.log(227.750000,2),math.log(226.875000,2),math.log(232.062500,2),math.log(251.031250,2),math.log(238.312500,2),math.log(284.593750,2),math.log(258.960938,2),math.log(276.712891,2),math.log(242.269531,2),math.log(238.556152,2),math.log(278.245361,2),math.log(293.516357,2),math.log(278.168274,2),math.log(312.763397,2)]
t_137 = [math.log(320.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(246.000000,2),math.log(243.000000,2),math.log(281.500000,2),math.log(247.375000,2),math.log(235.312500,2),math.log(230.468750,2),math.log(268.796875,2),math.log(273.445312,2),math.log(234.343750,2),math.log(247.783203,2),math.log(250.285156,2),math.log(266.866699,2),math.log(283.334717,2),math.log(294.694580,2),math.log(294.321289,2),math.log(379.708862,2)]
t_138 = [math.log(272.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(276.000000,2),math.log(253.000000,2),math.log(267.750000,2),math.log(253.500000,2),math.log(226.312500,2),math.log(249.125000,2),math.log(247.750000,2),math.log(238.898438,2),math.log(229.347656,2),math.log(280.042969,2),math.log(301.413086,2),math.log(297.079102,2),math.log(288.955811,2),math.log(319.279419,2),math.log(368.712158,2),math.log(470.985016,2)]
t_139 = [math.log(256.000000,2),math.log(216.000000,2),math.log(224.000000,2),math.log(250.000000,2),math.log(243.000000,2),math.log(251.000000,2),math.log(222.000000,2),math.log(231.375000,2),math.log(256.250000,2),math.log(263.031250,2),math.log(233.687500,2),math.log(244.734375,2),math.log(230.246094,2),math.log(236.179688,2),math.log(245.674805,2),math.log(254.608887,2),math.log(258.118164,2),math.log(274.824219,2),math.log(327.726501,2),math.log(364.717041,2)]
t_140 = [math.log(224.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(246.000000,2),math.log(264.000000,2),math.log(275.000000,2),math.log(262.250000,2),math.log(293.000000,2),math.log(271.375000,2),math.log(259.531250,2),math.log(271.843750,2),math.log(273.375000,2),math.log(255.707031,2),math.log(221.437500,2),math.log(227.820312,2),math.log(230.759766,2),math.log(229.039795,2),math.log(212.173584,2),math.log(237.729492,2),math.log(286.236420,2)]
t_141 = [math.log(240.000000,2),math.log(216.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(308.000000,2),math.log(336.000000,2),math.log(280.500000,2),math.log(277.500000,2),math.log(249.750000,2),math.log(255.687500,2),math.log(254.703125,2),math.log(273.570312,2),math.log(251.664062,2),math.log(220.388672,2),math.log(230.440430,2),math.log(240.916992,2),math.log(292.858398,2),math.log(274.397827,2),math.log(256.397339,2),math.log(364.608612,2)]
t_142 = [math.log(240.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(278.000000,2),math.log(249.000000,2),math.log(262.000000,2),math.log(211.625000,2),math.log(245.375000,2),math.log(243.312500,2),math.log(257.187500,2),math.log(256.859375,2),math.log(257.554688,2),math.log(273.886719,2),math.log(263.474609,2),math.log(220.450195,2),math.log(272.377197,2),math.log(264.407959,2),math.log(286.663513,2),math.log(362.371216,2)]
t_143 = [math.log(272.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(224.000000,2),math.log(234.000000,2),math.log(225.000000,2),math.log(229.500000,2),math.log(258.125000,2),math.log(248.812500,2),math.log(274.968750,2),math.log(246.359375,2),math.log(224.679688,2),math.log(271.980469,2),math.log(242.546875,2),math.log(256.351562,2),math.log(261.006836,2),math.log(242.551758,2),math.log(257.632202,2),math.log(270.697937,2),math.log(307.251251,2)]
t_144 = [math.log(272.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(262.000000,2),math.log(255.000000,2),math.log(245.500000,2),math.log(264.750000,2),math.log(253.125000,2),math.log(261.375000,2),math.log(242.156250,2),math.log(280.484375,2),math.log(264.375000,2),math.log(267.062500,2),math.log(257.310547,2),math.log(236.041016,2),math.log(231.805176,2),math.log(280.393799,2),math.log(289.366455,2),math.log(237.559326,2),math.log(285.424377,2)]
t_145 = [math.log(256.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(270.000000,2),math.log(284.000000,2),math.log(284.500000,2),math.log(282.500000,2),math.log(279.500000,2),math.log(273.562500,2),math.log(248.375000,2),math.log(274.500000,2),math.log(286.929688,2),math.log(275.628906,2),math.log(223.937500,2),math.log(225.801758,2),math.log(242.184570,2),math.log(250.171143,2),math.log(270.411621,2),math.log(247.786377,2),math.log(307.131104,2)]
t_146 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(246.000000,2),math.log(265.000000,2),math.log(275.000000,2),math.log(284.875000,2),math.log(222.500000,2),math.log(257.406250,2),math.log(285.656250,2),math.log(260.453125,2),math.log(245.019531,2),math.log(228.679688,2),math.log(236.866211,2),math.log(230.387695,2),math.log(219.385498,2),math.log(265.436768,2),math.log(276.492615,2),math.log(299.861450,2)]
t_147 = [math.log(240.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(212.000000,2),math.log(217.000000,2),math.log(232.000000,2),math.log(273.250000,2),math.log(251.500000,2),math.log(253.937500,2),math.log(272.406250,2),math.log(297.062500,2),math.log(252.250000,2),math.log(257.085938,2),math.log(254.339844,2),math.log(277.619141,2),math.log(270.236816,2),math.log(282.769043,2),math.log(309.584106,2),math.log(342.252014,2),math.log(403.859985,2)]
t_148 = [math.log(224.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(242.000000,2),math.log(230.000000,2),math.log(246.000000,2),math.log(256.500000,2),math.log(252.375000,2),math.log(240.187500,2),math.log(266.500000,2),math.log(264.015625,2),math.log(255.945312,2),math.log(262.812500,2),math.log(272.978516,2),math.log(259.751953,2),math.log(243.587891,2),math.log(223.260986,2),math.log(228.852417,2),math.log(250.615967,2),math.log(283.197571,2)]
t_149 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(244.000000,2),math.log(230.000000,2),math.log(238.500000,2),math.log(227.500000,2),math.log(225.625000,2),math.log(239.375000,2),math.log(244.312500,2),math.log(219.453125,2),math.log(226.078125,2),math.log(220.261719,2),math.log(231.339844,2),math.log(226.586914,2),math.log(232.030762,2),math.log(226.218750,2),math.log(243.580688,2),math.log(246.944031,2),math.log(255.590027,2)]
t_150 = [math.log(272.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(278.000000,2),math.log(270.000000,2),math.log(237.000000,2),math.log(245.750000,2),math.log(274.625000,2),math.log(245.500000,2),math.log(268.531250,2),math.log(234.531250,2),math.log(261.851562,2),math.log(271.304688,2),math.log(267.541016,2),math.log(251.000000,2),math.log(238.691895,2),math.log(276.434326,2),math.log(307.377197,2),math.log(332.504272,2),math.log(338.945984,2)]
t_151 = [math.log(336.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(228.000000,2),math.log(224.000000,2),math.log(236.500000,2),math.log(247.250000,2),math.log(246.250000,2),math.log(246.000000,2),math.log(247.656250,2),math.log(291.265625,2),math.log(284.000000,2),math.log(285.257812,2),math.log(289.841797,2),math.log(320.699219,2),math.log(270.853027,2),math.log(265.432617,2),math.log(272.043701,2),math.log(265.616760,2),math.log(316.426575,2)]
t_152 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(260.000000,2),math.log(275.000000,2),math.log(277.750000,2),math.log(259.000000,2),math.log(274.812500,2),math.log(267.750000,2),math.log(247.156250,2),math.log(228.890625,2),math.log(236.062500,2),math.log(245.792969,2),math.log(251.839844,2),math.log(268.765137,2),math.log(273.810547,2),math.log(242.521606,2),math.log(244.582397,2),math.log(255.769073,2)]
t_153 = [math.log(272.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(240.000000,2),math.log(262.000000,2),math.log(256.500000,2),math.log(234.000000,2),math.log(266.187500,2),math.log(275.125000,2),math.log(240.937500,2),math.log(249.375000,2),math.log(255.605469,2),math.log(236.013672,2),math.log(273.948242,2),math.log(299.135742,2),math.log(285.690918,2),math.log(299.976562,2),math.log(340.104675,2),math.log(315.140015,2)]
t_154 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(259.000000,2),math.log(289.000000,2),math.log(256.000000,2),math.log(262.750000,2),math.log(278.312500,2),math.log(271.562500,2),math.log(219.203125,2),math.log(253.828125,2),math.log(269.628906,2),math.log(250.578125,2),math.log(283.034180,2),math.log(248.053223,2),math.log(249.061523,2),math.log(275.959717,2),math.log(315.325684,2),math.log(436.025787,2)]
t_155 = [math.log(240.000000,2),math.log(240.000000,2),math.log(284.000000,2),math.log(242.000000,2),math.log(208.000000,2),math.log(231.000000,2),math.log(240.000000,2),math.log(247.500000,2),math.log(235.687500,2),math.log(248.250000,2),math.log(239.609375,2),math.log(237.273438,2),math.log(264.652344,2),math.log(303.185547,2),math.log(315.468750,2),math.log(291.868652,2),math.log(312.490967,2),math.log(339.904419,2),math.log(405.081482,2),math.log(425.916870,2)]
t_156 = [math.log(240.000000,2),math.log(216.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(232.000000,2),math.log(209.500000,2),math.log(210.750000,2),math.log(243.750000,2),math.log(245.937500,2),math.log(278.281250,2),math.log(278.921875,2),math.log(302.640625,2),math.log(279.203125,2),math.log(268.642578,2),math.log(258.789062,2),math.log(296.120605,2),math.log(278.501953,2),math.log(288.644775,2),math.log(333.057373,2),math.log(343.724335,2)]
t_157 = [math.log(256.000000,2),math.log(256.000000,2),math.log(288.000000,2),math.log(298.000000,2),math.log(265.000000,2),math.log(215.500000,2),math.log(259.750000,2),math.log(222.375000,2),math.log(230.812500,2),math.log(247.250000,2),math.log(262.015625,2),math.log(251.531250,2),math.log(242.402344,2),math.log(249.140625,2),math.log(271.263672,2),math.log(258.809082,2),math.log(237.780029,2),math.log(270.401855,2),math.log(324.497192,2),math.log(347.479706,2)]
t_158 = [math.log(288.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(250.000000,2),math.log(227.500000,2),math.log(253.250000,2),math.log(262.000000,2),math.log(252.062500,2),math.log(294.437500,2),math.log(275.703125,2),math.log(258.187500,2),math.log(240.261719,2),math.log(239.037109,2),math.log(249.956055,2),math.log(238.996094,2),math.log(278.449219,2),math.log(303.301025,2),math.log(313.752014,2),math.log(426.232056,2)]
t_159 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(254.000000,2),math.log(241.000000,2),math.log(256.500000,2),math.log(242.500000,2),math.log(251.250000,2),math.log(248.500000,2),math.log(236.437500,2),math.log(253.125000,2),math.log(220.351562,2),math.log(212.988281,2),math.log(236.289062,2),math.log(250.501953,2),math.log(280.372070,2),math.log(271.866943,2),math.log(278.791992,2),math.log(253.038025,2),math.log(335.452881,2)]
t_160 = [math.log(320.000000,2),math.log(336.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(276.500000,2),math.log(276.750000,2),math.log(230.500000,2),math.log(264.937500,2),math.log(255.218750,2),math.log(270.937500,2),math.log(268.914062,2),math.log(228.660156,2),math.log(266.621094,2),math.log(233.163086,2),math.log(282.685059,2),math.log(256.484131,2),math.log(279.572876,2),math.log(267.107727,2),math.log(316.820679,2)]
t_161 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(240.500000,2),math.log(250.750000,2),math.log(260.000000,2),math.log(216.000000,2),math.log(234.062500,2),math.log(224.140625,2),math.log(205.273438,2),math.log(220.945312,2),math.log(252.324219,2),math.log(244.935547,2),math.log(217.587402,2),math.log(251.870117,2),math.log(291.433838,2),math.log(349.203918,2),math.log(381.574646,2)]
t_162 = [math.log(240.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(250.000000,2),math.log(264.000000,2),math.log(259.500000,2),math.log(215.250000,2),math.log(219.250000,2),math.log(209.062500,2),math.log(225.750000,2),math.log(228.125000,2),math.log(228.500000,2),math.log(236.269531,2),math.log(234.623047,2),math.log(238.178711,2),math.log(241.936035,2),math.log(268.359863,2),math.log(305.165894,2),math.log(296.265991,2),math.log(301.059418,2)]
t_163 = [math.log(256.000000,2),math.log(320.000000,2),math.log(308.000000,2),math.log(250.000000,2),math.log(253.000000,2),math.log(247.500000,2),math.log(241.250000,2),math.log(230.875000,2),math.log(224.187500,2),math.log(279.468750,2),math.log(252.062500,2),math.log(234.437500,2),math.log(253.582031,2),math.log(258.896484,2),math.log(283.882812,2),math.log(299.720703,2),math.log(272.674561,2),math.log(238.639038,2),math.log(265.148315,2),math.log(297.485443,2)]
t_164 = [math.log(272.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(282.000000,2),math.log(275.000000,2),math.log(268.000000,2),math.log(251.000000,2),math.log(233.250000,2),math.log(237.812500,2),math.log(249.906250,2),math.log(250.453125,2),math.log(250.210938,2),math.log(274.937500,2),math.log(247.107422,2),math.log(253.688477,2),math.log(250.728027,2),math.log(277.769043,2),math.log(290.684692,2),math.log(267.696045,2),math.log(271.506744,2)]
t_165 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(215.000000,2),math.log(224.500000,2),math.log(251.500000,2),math.log(240.500000,2),math.log(244.437500,2),math.log(251.718750,2),math.log(262.562500,2),math.log(252.625000,2),math.log(237.949219,2),math.log(230.658203,2),math.log(256.548828,2),math.log(229.206543,2),math.log(251.166992,2),math.log(271.169067,2),math.log(311.728088,2),math.log(377.613281,2)]
t_166 = [math.log(272.000000,2),math.log(320.000000,2),math.log(292.000000,2),math.log(298.000000,2),math.log(317.000000,2),math.log(273.500000,2),math.log(284.000000,2),math.log(258.875000,2),math.log(256.375000,2),math.log(264.968750,2),math.log(264.640625,2),math.log(261.921875,2),math.log(271.796875,2),math.log(251.041016,2),math.log(239.270508,2),math.log(241.415039,2),math.log(261.680420,2),math.log(283.986450,2),math.log(343.040649,2),math.log(429.753754,2)]
t_167 = [math.log(288.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(276.000000,2),math.log(275.000000,2),math.log(269.500000,2),math.log(272.250000,2),math.log(266.250000,2),math.log(270.312500,2),math.log(277.343750,2),math.log(312.046875,2),math.log(248.070312,2),math.log(255.859375,2),math.log(270.123047,2),math.log(250.481445,2),math.log(293.932617,2),math.log(256.318359,2),math.log(255.818115,2),math.log(285.177856,2),math.log(333.894104,2)]
t_168 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(281.500000,2),math.log(251.250000,2),math.log(277.875000,2),math.log(287.437500,2),math.log(258.218750,2),math.log(251.671875,2),math.log(242.437500,2),math.log(237.273438,2),math.log(244.054688,2),math.log(291.320312,2),math.log(307.226074,2),math.log(287.070312,2),math.log(293.329590,2),math.log(287.242310,2),math.log(294.818176,2)]
t_169 = [math.log(240.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(222.000000,2),math.log(281.000000,2),math.log(295.500000,2),math.log(292.250000,2),math.log(261.375000,2),math.log(238.750000,2),math.log(237.562500,2),math.log(268.828125,2),math.log(259.328125,2),math.log(259.636719,2),math.log(264.544922,2),math.log(270.114258,2),math.log(244.169434,2),math.log(281.451904,2),math.log(306.199707,2),math.log(364.956970,2),math.log(404.851379,2)]
t_170 = [math.log(320.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(268.000000,2),math.log(296.000000,2),math.log(314.500000,2),math.log(268.000000,2),math.log(265.250000,2),math.log(239.437500,2),math.log(234.921875,2),math.log(247.109375,2),math.log(263.726562,2),math.log(261.140625,2),math.log(245.157227,2),math.log(238.184570,2),math.log(250.400635,2),math.log(239.368896,2),math.log(253.767395,2),math.log(354.087494,2)]
t_171 = [math.log(288.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(250.000000,2),math.log(238.000000,2),math.log(230.000000,2),math.log(255.750000,2),math.log(246.875000,2),math.log(256.812500,2),math.log(255.562500,2),math.log(245.500000,2),math.log(233.937500,2),math.log(222.867188,2),math.log(237.853516,2),math.log(240.942383,2),math.log(259.406250,2),math.log(278.534912,2),math.log(322.814331,2),math.log(387.726868,2),math.log(463.330383,2)]
t_172 = [math.log(240.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(238.000000,2),math.log(208.000000,2),math.log(220.500000,2),math.log(237.250000,2),math.log(246.625000,2),math.log(243.687500,2),math.log(230.031250,2),math.log(247.890625,2),math.log(238.312500,2),math.log(256.300781,2),math.log(266.414062,2),math.log(222.828125,2),math.log(228.623047,2),math.log(220.458252,2),math.log(228.949829,2),math.log(262.627014,2),math.log(325.224915,2)]
t_173 = [math.log(224.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(222.000000,2),math.log(226.000000,2),math.log(298.000000,2),math.log(265.500000,2),math.log(251.375000,2),math.log(286.250000,2),math.log(263.625000,2),math.log(252.890625,2),math.log(264.687500,2),math.log(268.882812,2),math.log(222.160156,2),math.log(256.153320,2),math.log(259.005371,2),math.log(297.341553,2),math.log(335.072754,2),math.log(389.612366,2),math.log(426.832458,2)]
t_174 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(276.000000,2),math.log(275.500000,2),math.log(273.250000,2),math.log(316.500000,2),math.log(296.562500,2),math.log(281.906250,2),math.log(283.359375,2),math.log(260.835938,2),math.log(231.503906,2),math.log(245.685547,2),math.log(234.422852,2),math.log(252.608398,2),math.log(291.817871,2),math.log(278.109253,2),math.log(323.536499,2),math.log(426.566254,2)]
t_175 = [math.log(256.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(246.000000,2),math.log(266.000000,2),math.log(286.000000,2),math.log(282.250000,2),math.log(278.875000,2),math.log(244.875000,2),math.log(239.875000,2),math.log(272.671875,2),math.log(236.000000,2),math.log(234.242188,2),math.log(228.521484,2),math.log(242.947266,2),math.log(283.044922,2),math.log(259.866211,2),math.log(232.347046,2),math.log(238.537048,2),math.log(320.121552,2)]
t_176 = [math.log(272.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(242.000000,2),math.log(265.000000,2),math.log(231.750000,2),math.log(235.625000,2),math.log(239.250000,2),math.log(221.125000,2),math.log(217.843750,2),math.log(219.468750,2),math.log(237.507812,2),math.log(242.279297,2),math.log(271.938477,2),math.log(271.572266,2),math.log(272.630615,2),math.log(277.956177,2),math.log(299.395752,2),math.log(344.439423,2)]
t_177 = [math.log(272.000000,2),math.log(224.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(255.000000,2),math.log(275.500000,2),math.log(247.250000,2),math.log(231.375000,2),math.log(214.562500,2),math.log(266.437500,2),math.log(241.515625,2),math.log(327.859375,2),math.log(332.761719,2),math.log(327.464844,2),math.log(317.907227,2),math.log(282.617188,2),math.log(263.053467,2),math.log(258.093506,2),math.log(263.605774,2),math.log(338.736755,2)]
t_178 = [math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(278.000000,2),math.log(258.000000,2),math.log(274.500000,2),math.log(246.500000,2),math.log(234.375000,2),math.log(231.937500,2),math.log(209.187500,2),math.log(264.171875,2),math.log(253.718750,2),math.log(238.539062,2),math.log(258.195312,2),math.log(247.745117,2),math.log(236.208008,2),math.log(240.715576,2),math.log(301.930054,2),math.log(266.615967,2),math.log(307.284241,2)]
t_179 = [math.log(272.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(242.000000,2),math.log(253.000000,2),math.log(297.500000,2),math.log(281.500000,2),math.log(248.500000,2),math.log(272.375000,2),math.log(280.718750,2),math.log(255.000000,2),math.log(246.031250,2),math.log(277.234375,2),math.log(268.000000,2),math.log(280.295898,2),math.log(292.065430,2),math.log(276.634766,2),math.log(288.450195,2),math.log(321.101562,2),math.log(358.594513,2)]
t_180 = [math.log(272.000000,2),math.log(272.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(254.000000,2),math.log(268.750000,2),math.log(261.250000,2),math.log(281.437500,2),math.log(299.156250,2),math.log(242.390625,2),math.log(260.367188,2),math.log(274.937500,2),math.log(257.326172,2),math.log(238.448242,2),math.log(209.438477,2),math.log(238.410156,2),math.log(251.374146,2),math.log(295.053040,2),math.log(276.406250,2)]
t_181 = [math.log(256.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(280.000000,2),math.log(243.500000,2),math.log(256.250000,2),math.log(241.125000,2),math.log(234.187500,2),math.log(287.718750,2),math.log(295.515625,2),math.log(245.992188,2),math.log(258.289062,2),math.log(281.205078,2),math.log(282.386719,2),math.log(280.354980,2),math.log(276.568604,2),math.log(283.449951,2),math.log(290.305969,2),math.log(349.668976,2)]
t_182 = [math.log(224.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(247.000000,2),math.log(249.500000,2),math.log(261.500000,2),math.log(240.750000,2),math.log(231.062500,2),math.log(274.031250,2),math.log(260.765625,2),math.log(247.859375,2),math.log(269.609375,2),math.log(255.285156,2),math.log(245.630859,2),math.log(258.035156,2),math.log(299.676514,2),math.log(276.306519,2),math.log(315.799561,2),math.log(353.556366,2)]
t_183 = [math.log(224.000000,2),math.log(200.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(251.000000,2),math.log(241.500000,2),math.log(276.000000,2),math.log(291.375000,2),math.log(279.625000,2),math.log(255.218750,2),math.log(273.156250,2),math.log(224.359375,2),math.log(238.167969,2),math.log(231.302734,2),math.log(268.252930,2),math.log(244.914062,2),math.log(219.704590,2),math.log(253.431152,2),math.log(282.082458,2),math.log(302.252869,2)]
t_184 = [math.log(224.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(243.000000,2),math.log(247.000000,2),math.log(271.500000,2),math.log(265.875000,2),math.log(261.250000,2),math.log(237.968750,2),math.log(233.921875,2),math.log(230.562500,2),math.log(232.656250,2),math.log(241.925781,2),math.log(261.845703,2),math.log(318.006836,2),math.log(309.495117,2),math.log(301.841309,2),math.log(333.820312,2),math.log(372.963226,2)]
t_185 = [math.log(256.000000,2),math.log(280.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(293.000000,2),math.log(282.000000,2),math.log(261.000000,2),math.log(289.375000,2),math.log(306.625000,2),math.log(256.843750,2),math.log(237.843750,2),math.log(235.648438,2),math.log(292.296875,2),math.log(257.751953,2),math.log(273.570312,2),math.log(250.592285,2),math.log(271.920166,2),math.log(288.952759,2),math.log(311.565369,2),math.log(360.140442,2)]
t_186 = [math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(258.000000,2),math.log(227.500000,2),math.log(252.250000,2),math.log(255.750000,2),math.log(273.812500,2),math.log(242.562500,2),math.log(239.296875,2),math.log(262.031250,2),math.log(257.609375,2),math.log(254.478516,2),math.log(289.773438,2),math.log(281.800781,2),math.log(278.451172,2),math.log(312.661377,2),math.log(376.571899,2),math.log(476.839905,2)]
t_187 = [math.log(240.000000,2),math.log(256.000000,2),math.log(224.000000,2),math.log(268.000000,2),math.log(238.000000,2),math.log(253.500000,2),math.log(216.500000,2),math.log(208.250000,2),math.log(228.187500,2),math.log(256.437500,2),math.log(238.015625,2),math.log(256.210938,2),math.log(282.761719,2),math.log(281.238281,2),math.log(289.166016,2),math.log(272.026367,2),math.log(275.349609,2),math.log(286.128052,2),math.log(306.028687,2),math.log(358.091858,2)]
t_188 = [math.log(272.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(269.000000,2),math.log(290.000000,2),math.log(275.000000,2),math.log(288.000000,2),math.log(282.187500,2),math.log(257.125000,2),math.log(215.093750,2),math.log(193.890625,2),math.log(244.929688,2),math.log(233.878906,2),math.log(241.604492,2),math.log(234.382324,2),math.log(221.558350,2),math.log(229.898193,2),math.log(258.871094,2),math.log(314.318298,2)]
t_189 = [math.log(240.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(276.000000,2),math.log(273.500000,2),math.log(291.750000,2),math.log(236.375000,2),math.log(229.062500,2),math.log(242.156250,2),math.log(232.562500,2),math.log(241.476562,2),math.log(235.609375,2),math.log(248.566406,2),math.log(269.423828,2),math.log(294.953125,2),math.log(312.437012,2),math.log(300.251831,2),math.log(285.057861,2),math.log(340.710083,2)]
t_190 = [math.log(288.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(255.000000,2),math.log(258.000000,2),math.log(272.000000,2),math.log(247.750000,2),math.log(239.625000,2),math.log(271.562500,2),math.log(244.046875,2),math.log(262.328125,2),math.log(252.835938,2),math.log(237.429688,2),math.log(252.248047,2),math.log(253.590820,2),math.log(275.934326,2),math.log(259.555176,2),math.log(291.708069,2),math.log(356.374664,2)]
t_191 = [math.log(288.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(282.000000,2),math.log(269.000000,2),math.log(234.500000,2),math.log(258.750000,2),math.log(229.750000,2),math.log(238.250000,2),math.log(225.593750,2),math.log(280.078125,2),math.log(235.023438,2),math.log(244.250000,2),math.log(233.619141,2),math.log(202.058594,2),math.log(272.349609,2),math.log(291.473389,2),math.log(288.055908,2),math.log(278.922424,2),math.log(335.423706,2)]
t_192 = [math.log(224.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(290.000000,2),math.log(257.000000,2),math.log(232.500000,2),math.log(238.750000,2),math.log(249.000000,2),math.log(241.437500,2),math.log(264.687500,2),math.log(244.843750,2),math.log(243.132812,2),math.log(219.664062,2),math.log(243.835938,2),math.log(243.628906,2),math.log(223.871094,2),math.log(240.054199,2),math.log(251.274658,2),math.log(277.555420,2),math.log(309.489838,2)]
t_193 = [math.log(240.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(278.000000,2),math.log(289.000000,2),math.log(305.500000,2),math.log(242.000000,2),math.log(260.500000,2),math.log(268.375000,2),math.log(259.375000,2),math.log(245.578125,2),math.log(236.125000,2),math.log(272.640625,2),math.log(291.585938,2),math.log(267.523438,2),math.log(248.663574,2),math.log(245.866455,2),math.log(295.952026,2),math.log(321.663208,2),math.log(325.245087,2)]
t_194 = [math.log(288.000000,2),math.log(296.000000,2),math.log(304.000000,2),math.log(278.000000,2),math.log(242.000000,2),math.log(243.500000,2),math.log(250.750000,2),math.log(231.875000,2),math.log(256.875000,2),math.log(273.062500,2),math.log(245.000000,2),math.log(264.695312,2),math.log(260.308594,2),math.log(253.263672,2),math.log(254.010742,2),math.log(282.899414,2),math.log(290.845459,2),math.log(286.471558,2),math.log(312.484924,2),math.log(365.710876,2)]
t_195 = [math.log(240.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(216.000000,2),math.log(233.000000,2),math.log(248.000000,2),math.log(251.500000,2),math.log(256.875000,2),math.log(222.562500,2),math.log(246.875000,2),math.log(270.578125,2),math.log(265.195312,2),math.log(266.230469,2),math.log(261.544922,2),math.log(302.333984,2),math.log(291.043945,2),math.log(284.939941,2),math.log(315.713623,2),math.log(317.923340,2),math.log(332.411835,2)]
t_196 = [math.log(256.000000,2),math.log(296.000000,2),math.log(292.000000,2),math.log(256.000000,2),math.log(257.000000,2),math.log(255.500000,2),math.log(252.000000,2),math.log(274.625000,2),math.log(296.750000,2),math.log(294.593750,2),math.log(295.578125,2),math.log(239.812500,2),math.log(237.292969,2),math.log(243.085938,2),math.log(242.672852,2),math.log(249.487305,2),math.log(311.241699,2),math.log(298.830566,2),math.log(357.481018,2),math.log(376.040894,2)]
t_197 = [math.log(224.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(253.000000,2),math.log(268.000000,2),math.log(248.000000,2),math.log(248.875000,2),math.log(236.437500,2),math.log(210.062500,2),math.log(219.156250,2),math.log(250.156250,2),math.log(247.378906,2),math.log(254.500000,2),math.log(269.094727,2),math.log(276.299805,2),math.log(281.220947,2),math.log(274.896362,2),math.log(247.424255,2),math.log(288.298401,2)]
t_198 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(230.000000,2),math.log(263.000000,2),math.log(260.000000,2),math.log(248.750000,2),math.log(263.062500,2),math.log(246.046875,2),math.log(252.804688,2),math.log(254.796875,2),math.log(277.136719,2),math.log(265.294922,2),math.log(279.352051,2),math.log(265.996094,2),math.log(282.957031,2),math.log(315.053345,2),math.log(355.005737,2)]
t_199 = [math.log(240.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(254.000000,2),math.log(249.000000,2),math.log(227.500000,2),math.log(233.750000,2),math.log(239.125000,2),math.log(263.875000,2),math.log(240.625000,2),math.log(230.203125,2),math.log(277.898438,2),math.log(240.667969,2),math.log(242.488281,2),math.log(243.857422,2),math.log(242.851562,2),math.log(235.753418,2),math.log(328.287842,2),math.log(326.082581,2),math.log(423.013397,2)]
t_200 = [math.log(240.000000,2),math.log(240.000000,2),math.log(308.000000,2),math.log(294.000000,2),math.log(309.000000,2),math.log(278.500000,2),math.log(274.000000,2),math.log(257.750000,2),math.log(195.937500,2),math.log(194.156250,2),math.log(242.828125,2),math.log(265.046875,2),math.log(264.140625,2),math.log(243.511719,2),math.log(236.024414,2),math.log(266.415527,2),math.log(246.040527,2),math.log(266.635254,2),math.log(290.026733,2),math.log(338.861145,2)]
t_201 = [math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(269.000000,2),math.log(250.750000,2),math.log(243.125000,2),math.log(253.625000,2),math.log(265.000000,2),math.log(245.578125,2),math.log(263.687500,2),math.log(228.984375,2),math.log(269.789062,2),math.log(247.932617,2),math.log(267.203613,2),math.log(252.285156,2),math.log(327.991089,2),math.log(290.343201,2),math.log(342.823517,2)]
t_202 = [math.log(256.000000,2),math.log(280.000000,2),math.log(292.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(266.000000,2),math.log(259.000000,2),math.log(262.000000,2),math.log(264.125000,2),math.log(270.937500,2),math.log(227.546875,2),math.log(234.296875,2),math.log(227.128906,2),math.log(273.349609,2),math.log(236.095703,2),math.log(238.623535,2),math.log(260.989990,2),math.log(301.385498,2),math.log(338.089417,2),math.log(473.021851,2)]
t_203 = [math.log(240.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(267.000000,2),math.log(287.000000,2),math.log(267.750000,2),math.log(241.250000,2),math.log(244.000000,2),math.log(240.312500,2),math.log(255.375000,2),math.log(265.750000,2),math.log(291.355469,2),math.log(321.507812,2),math.log(282.766602,2),math.log(284.076660,2),math.log(294.778076,2),math.log(327.600952,2),math.log(342.130676,2),math.log(417.162872,2)]
t_204 = [math.log(272.000000,2),math.log(280.000000,2),math.log(236.000000,2),math.log(232.000000,2),math.log(229.000000,2),math.log(246.000000,2),math.log(263.250000,2),math.log(239.000000,2),math.log(290.062500,2),math.log(267.250000,2),math.log(264.250000,2),math.log(251.281250,2),math.log(278.027344,2),math.log(257.759766,2),math.log(248.731445,2),math.log(259.524414,2),math.log(265.406250,2),math.log(286.773804,2),math.log(293.931641,2),math.log(304.978027,2)]
t_205 = [math.log(256.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(214.000000,2),math.log(262.000000,2),math.log(241.000000,2),math.log(214.250000,2),math.log(225.875000,2),math.log(258.406250,2),math.log(245.093750,2),math.log(227.625000,2),math.log(275.878906,2),math.log(281.488281,2),math.log(267.051758,2),math.log(289.674316,2),math.log(278.741211,2),math.log(296.526978,2),math.log(304.230957,2),math.log(350.290741,2)]
t_206 = [math.log(272.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(241.000000,2),math.log(244.500000,2),math.log(299.750000,2),math.log(287.500000,2),math.log(264.125000,2),math.log(277.625000,2),math.log(283.734375,2),math.log(250.906250,2),math.log(244.589844,2),math.log(264.130859,2),math.log(248.459961,2),math.log(266.233398,2),math.log(313.884033,2),math.log(281.786743,2),math.log(329.084290,2),math.log(352.455811,2)]
t_207 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(286.000000,2),math.log(261.500000,2),math.log(262.750000,2),math.log(291.500000,2),math.log(262.250000,2),math.log(240.062500,2),math.log(227.359375,2),math.log(233.062500,2),math.log(257.421875,2),math.log(234.414062,2),math.log(251.067383,2),math.log(253.023438,2),math.log(260.315186,2),math.log(303.737793,2),math.log(304.837463,2),math.log(383.208740,2)]
t_208 = [math.log(240.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(238.000000,2),math.log(243.500000,2),math.log(227.750000,2),math.log(204.375000,2),math.log(222.500000,2),math.log(270.156250,2),math.log(272.000000,2),math.log(260.945312,2),math.log(239.402344,2),math.log(229.755859,2),math.log(249.722656,2),math.log(248.251953,2),math.log(257.243896,2),math.log(278.416748,2),math.log(299.427002,2),math.log(300.885620,2)]
t_209 = [math.log(240.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(294.000000,2),math.log(269.000000,2),math.log(242.000000,2),math.log(269.500000,2),math.log(314.125000,2),math.log(289.437500,2),math.log(277.406250,2),math.log(277.218750,2),math.log(229.484375,2),math.log(195.843750,2),math.log(234.429688,2),math.log(263.268555,2),math.log(304.468262,2),math.log(289.294922,2),math.log(290.955566,2),math.log(344.295166,2),math.log(345.341064,2)]
t_210 = [math.log(272.000000,2),math.log(288.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(295.000000,2),math.log(269.500000,2),math.log(271.750000,2),math.log(251.875000,2),math.log(250.500000,2),math.log(283.562500,2),math.log(268.906250,2),math.log(217.203125,2),math.log(214.542969,2),math.log(240.453125,2),math.log(261.345703,2),math.log(242.227539,2),math.log(251.547363,2),math.log(251.666260,2),math.log(296.003723,2),math.log(257.212280,2)]
t_211 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(216.000000,2),math.log(240.000000,2),math.log(241.500000,2),math.log(255.000000,2),math.log(268.375000,2),math.log(251.750000,2),math.log(221.906250,2),math.log(236.828125,2),math.log(259.398438,2),math.log(267.757812,2),math.log(264.597656,2),math.log(270.459961,2),math.log(278.967285,2),math.log(266.735107,2),math.log(262.893188,2),math.log(279.892761,2),math.log(300.010956,2)]
t_212 = [math.log(256.000000,2),math.log(264.000000,2),math.log(304.000000,2),math.log(270.000000,2),math.log(249.000000,2),math.log(251.500000,2),math.log(284.000000,2),math.log(284.875000,2),math.log(256.375000,2),math.log(267.343750,2),math.log(302.171875,2),math.log(310.640625,2),math.log(314.625000,2),math.log(291.998047,2),math.log(313.787109,2),math.log(306.478516,2),math.log(286.480469,2),math.log(284.049316,2),math.log(333.288208,2),math.log(329.699158,2)]
t_213 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(260.000000,2),math.log(248.000000,2),math.log(279.000000,2),math.log(248.250000,2),math.log(248.000000,2),math.log(275.062500,2),math.log(247.031250,2),math.log(281.359375,2),math.log(267.109375,2),math.log(230.480469,2),math.log(247.654297,2),math.log(225.280273,2),math.log(235.333496,2),math.log(242.368652,2),math.log(256.025024,2),math.log(277.815674,2),math.log(312.329956,2)]
t_214 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(231.000000,2),math.log(271.000000,2),math.log(249.250000,2),math.log(251.125000,2),math.log(244.562500,2),math.log(256.562500,2),math.log(265.046875,2),math.log(246.429688,2),math.log(253.074219,2),math.log(237.019531,2),math.log(233.241211,2),math.log(222.345215,2),math.log(238.745117,2),math.log(282.119751,2),math.log(274.050659,2),math.log(348.279510,2)]
t_215 = [math.log(272.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(273.000000,2),math.log(251.000000,2),math.log(241.250000,2),math.log(248.000000,2),math.log(275.062500,2),math.log(268.031250,2),math.log(266.906250,2),math.log(302.960938,2),math.log(241.355469,2),math.log(230.642578,2),math.log(227.486328,2),math.log(266.333496,2),math.log(240.361084,2),math.log(256.437744,2),math.log(289.148560,2),math.log(334.693451,2)]
t_216 = [math.log(256.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(250.000000,2),math.log(244.000000,2),math.log(287.000000,2),math.log(266.750000,2),math.log(272.500000,2),math.log(290.750000,2),math.log(219.937500,2),math.log(222.781250,2),math.log(260.765625,2),math.log(242.945312,2),math.log(259.695312,2),math.log(246.103516,2),math.log(225.959473,2),math.log(258.051270,2),math.log(263.244385,2),math.log(248.454529,2),math.log(321.765564,2)]
t_217 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(235.000000,2),math.log(247.000000,2),math.log(232.500000,2),math.log(264.125000,2),math.log(271.312500,2),math.log(287.031250,2),math.log(294.625000,2),math.log(278.132812,2),math.log(261.480469,2),math.log(267.283203,2),math.log(254.860352,2),math.log(244.687012,2),math.log(282.739746,2),math.log(284.890503,2),math.log(302.410950,2),math.log(298.632538,2)]
t_218 = [math.log(240.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(257.000000,2),math.log(262.500000,2),math.log(257.000000,2),math.log(294.875000,2),math.log(250.312500,2),math.log(261.781250,2),math.log(253.609375,2),math.log(247.632812,2),math.log(233.851562,2),math.log(246.376953,2),math.log(260.741211,2),math.log(242.705078,2),math.log(255.390625,2),math.log(320.437744,2),math.log(423.931824,2),math.log(532.894897,2)]
t_219 = [math.log(240.000000,2),math.log(216.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(303.000000,2),math.log(277.500000,2),math.log(266.250000,2),math.log(268.500000,2),math.log(259.375000,2),math.log(223.093750,2),math.log(263.109375,2),math.log(291.703125,2),math.log(268.894531,2),math.log(285.455078,2),math.log(273.347656,2),math.log(258.646484,2),math.log(278.091553,2),math.log(254.406128,2),math.log(292.494995,2),math.log(310.669525,2)]
t_220 = [math.log(288.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(265.000000,2),math.log(238.500000,2),math.log(217.500000,2),math.log(252.000000,2),math.log(265.125000,2),math.log(258.406250,2),math.log(290.859375,2),math.log(239.664062,2),math.log(245.820312,2),math.log(254.501953,2),math.log(249.038086,2),math.log(216.185059,2),math.log(257.260010,2),math.log(252.314209,2),math.log(276.956055,2),math.log(298.760406,2)]
t_221 = [math.log(240.000000,2),math.log(224.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(299.000000,2),math.log(275.500000,2),math.log(277.250000,2),math.log(260.125000,2),math.log(260.062500,2),math.log(259.312500,2),math.log(291.046875,2),math.log(275.695312,2),math.log(255.406250,2),math.log(231.533203,2),math.log(233.307617,2),math.log(250.575684,2),math.log(261.280273,2),math.log(240.009033,2),math.log(290.569641,2),math.log(313.246552,2)]
t_222 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(276.000000,2),math.log(270.000000,2),math.log(235.500000,2),math.log(233.750000,2),math.log(233.375000,2),math.log(235.125000,2),math.log(235.734375,2),math.log(264.601562,2),math.log(279.640625,2),math.log(233.132812,2),math.log(249.113281,2),math.log(261.977051,2),math.log(282.811768,2),math.log(261.132446,2),math.log(331.021484,2),math.log(410.480377,2)]
t_223 = [math.log(256.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(278.000000,2),math.log(266.000000,2),math.log(279.000000,2),math.log(281.000000,2),math.log(246.250000,2),math.log(237.687500,2),math.log(229.750000,2),math.log(201.671875,2),math.log(225.554688,2),math.log(273.652344,2),math.log(267.384766,2),math.log(247.899414,2),math.log(257.078125,2),math.log(277.212158,2),math.log(308.919434,2),math.log(340.627258,2),math.log(382.448486,2)]
t_224 = [math.log(272.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(282.000000,2),math.log(281.000000,2),math.log(285.500000,2),math.log(288.250000,2),math.log(289.875000,2),math.log(287.687500,2),math.log(284.531250,2),math.log(270.968750,2),math.log(285.406250,2),math.log(284.882812,2),math.log(268.494141,2),math.log(251.958008,2),math.log(277.717773,2),math.log(281.316895,2),math.log(286.862305,2),math.log(334.058716,2),math.log(315.601105,2)]
t_225 = [math.log(288.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(258.000000,2),math.log(271.000000,2),math.log(276.000000,2),math.log(269.500000,2),math.log(276.125000,2),math.log(260.937500,2),math.log(240.718750,2),math.log(249.250000,2),math.log(224.960938,2),math.log(227.011719,2),math.log(273.000000,2),math.log(257.670898,2),math.log(251.304688,2),math.log(266.690674,2),math.log(280.501343,2),math.log(311.464661,2),math.log(399.057678,2)]
t_226 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(257.000000,2),math.log(246.000000,2),math.log(246.750000,2),math.log(241.750000,2),math.log(240.062500,2),math.log(243.812500,2),math.log(306.781250,2),math.log(237.781250,2),math.log(237.109375,2),math.log(266.619141,2),math.log(260.740234,2),math.log(298.801270,2),math.log(295.056885,2),math.log(295.272827,2),math.log(291.541382,2),math.log(298.322601,2)]
t_227 = [math.log(288.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(273.000000,2),math.log(278.000000,2),math.log(245.750000,2),math.log(222.125000,2),math.log(227.000000,2),math.log(245.781250,2),math.log(228.156250,2),math.log(252.765625,2),math.log(238.777344,2),math.log(237.486328,2),math.log(251.255859,2),math.log(235.761719,2),math.log(273.289795,2),math.log(290.317505,2),math.log(262.541992,2),math.log(283.863617,2)]
t_228 = [math.log(272.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(282.000000,2),math.log(254.000000,2),math.log(267.500000,2),math.log(301.500000,2),math.log(297.125000,2),math.log(249.562500,2),math.log(276.812500,2),math.log(261.781250,2),math.log(239.000000,2),math.log(227.558594,2),math.log(229.101562,2),math.log(242.601562,2),math.log(249.504883,2),math.log(276.612793,2),math.log(251.002197,2),math.log(301.845825,2),math.log(362.563995,2)]
t_229 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(224.000000,2),math.log(269.000000,2),math.log(278.500000,2),math.log(262.625000,2),math.log(287.500000,2),math.log(265.218750,2),math.log(270.359375,2),math.log(245.765625,2),math.log(283.144531,2),math.log(294.556641,2),math.log(246.586914,2),math.log(249.437988,2),math.log(261.558350,2),math.log(280.248413,2),math.log(311.533325,2),math.log(274.750885,2)]
t_230 = [math.log(240.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(224.000000,2),math.log(246.000000,2),math.log(237.000000,2),math.log(231.000000,2),math.log(225.250000,2),math.log(247.875000,2),math.log(243.718750,2),math.log(245.968750,2),math.log(249.945312,2),math.log(249.093750,2),math.log(257.626953,2),math.log(216.906250,2),math.log(216.459961,2),math.log(253.361816,2),math.log(249.501831,2),math.log(337.702148,2),math.log(378.906464,2)]
t_231 = [math.log(272.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(271.000000,2),math.log(246.500000,2),math.log(254.000000,2),math.log(255.375000,2),math.log(250.875000,2),math.log(254.500000,2),math.log(277.187500,2),math.log(253.070312,2),math.log(283.445312,2),math.log(283.500000,2),math.log(290.748047,2),math.log(272.636230,2),math.log(286.330322,2),math.log(298.155518,2),math.log(296.357788,2),math.log(315.603302,2)]
t_232 = [math.log(224.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(246.000000,2),math.log(244.000000,2),math.log(250.750000,2),math.log(245.750000,2),math.log(232.187500,2),math.log(247.093750,2),math.log(252.203125,2),math.log(234.273438,2),math.log(249.042969,2),math.log(253.289062,2),math.log(241.915039,2),math.log(245.231934,2),math.log(270.886719,2),math.log(277.200806,2),math.log(287.428406,2),math.log(270.803131,2)]
t_233 = [math.log(272.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(282.000000,2),math.log(254.000000,2),math.log(290.500000,2),math.log(274.250000,2),math.log(289.750000,2),math.log(283.437500,2),math.log(233.750000,2),math.log(288.609375,2),math.log(265.906250,2),math.log(271.894531,2),math.log(314.042969,2),math.log(253.894531,2),math.log(268.761719,2),math.log(292.206787,2),math.log(313.876465,2),math.log(346.772705,2),math.log(399.860291,2)]
t_234 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(260.000000,2),math.log(259.000000,2),math.log(229.000000,2),math.log(262.750000,2),math.log(224.875000,2),math.log(267.593750,2),math.log(246.328125,2),math.log(283.625000,2),math.log(292.988281,2),math.log(254.236328,2),math.log(221.799805,2),math.log(233.265137,2),math.log(276.724609,2),math.log(315.911011,2),math.log(323.799011,2),math.log(484.523224,2)]
t_235 = [math.log(240.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(274.000000,2),math.log(275.000000,2),math.log(302.500000,2),math.log(271.250000,2),math.log(275.625000,2),math.log(261.812500,2),math.log(261.843750,2),math.log(248.750000,2),math.log(237.984375,2),math.log(217.371094,2),math.log(261.509766,2),math.log(237.965820,2),math.log(284.634766,2),math.log(298.104248,2),math.log(296.589966,2),math.log(310.312683,2),math.log(403.417419,2)]
t_236 = [math.log(240.000000,2),math.log(224.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(275.000000,2),math.log(295.000000,2),math.log(292.750000,2),math.log(277.625000,2),math.log(332.687500,2),math.log(272.375000,2),math.log(264.312500,2),math.log(229.078125,2),math.log(255.371094,2),math.log(264.447266,2),math.log(238.146484,2),math.log(246.572754,2),math.log(238.674805,2),math.log(238.161865,2),math.log(320.078491,2),math.log(349.838623,2)]
t_237 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(242.000000,2),math.log(275.000000,2),math.log(285.250000,2),math.log(270.000000,2),math.log(275.625000,2),math.log(253.000000,2),math.log(265.140625,2),math.log(288.367188,2),math.log(273.402344,2),math.log(294.806641,2),math.log(270.437500,2),math.log(244.783691,2),math.log(240.164795,2),math.log(277.970215,2),math.log(320.567078,2),math.log(380.235901,2)]
t_238 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(268.000000,2),math.log(255.000000,2),math.log(256.000000,2),math.log(280.750000,2),math.log(285.500000,2),math.log(269.875000,2),math.log(294.125000,2),math.log(292.906250,2),math.log(248.820312,2),math.log(263.253906,2),math.log(252.994141,2),math.log(281.772461,2),math.log(256.572754,2),math.log(220.570068,2),math.log(246.321655,2),math.log(238.227905,2),math.log(303.059204,2)]
t_239 = [math.log(224.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(243.000000,2),math.log(259.500000,2),math.log(282.500000,2),math.log(277.500000,2),math.log(258.437500,2),math.log(274.187500,2),math.log(248.656250,2),math.log(258.593750,2),math.log(267.914062,2),math.log(246.994141,2),math.log(245.507812,2),math.log(258.355469,2),math.log(275.155518,2),math.log(265.622437,2),math.log(295.466187,2),math.log(345.861938,2)]
t_240 = [math.log(256.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(261.000000,2),math.log(240.250000,2),math.log(252.500000,2),math.log(272.062500,2),math.log(261.093750,2),math.log(273.031250,2),math.log(303.625000,2),math.log(281.402344,2),math.log(269.294922,2),math.log(276.189453,2),math.log(295.676270,2),math.log(267.195068,2),math.log(269.199097,2),math.log(258.729797,2),math.log(300.935883,2)]
t_241 = [math.log(240.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(252.000000,2),math.log(215.000000,2),math.log(235.000000,2),math.log(241.000000,2),math.log(248.500000,2),math.log(267.812500,2),math.log(269.718750,2),math.log(295.171875,2),math.log(287.757812,2),math.log(257.742188,2),math.log(272.121094,2),math.log(287.846680,2),math.log(263.675781,2),math.log(258.644531,2),math.log(323.143066,2),math.log(362.943848,2),math.log(402.152802,2)]
t_242 = [math.log(256.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(208.000000,2),math.log(235.000000,2),math.log(256.000000,2),math.log(253.500000,2),math.log(254.375000,2),math.log(302.687500,2),math.log(268.468750,2),math.log(280.125000,2),math.log(254.539062,2),math.log(249.777344,2),math.log(238.802734,2),math.log(244.976562,2),math.log(286.500488,2),math.log(300.102783,2),math.log(310.004761,2),math.log(298.211609,2),math.log(318.631714,2)]
t_243 = [math.log(272.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(257.000000,2),math.log(258.000000,2),math.log(259.250000,2),math.log(258.750000,2),math.log(258.125000,2),math.log(245.625000,2),math.log(260.296875,2),math.log(246.929688,2),math.log(229.837891,2),math.log(230.892578,2),math.log(266.657715,2),math.log(261.090576,2),math.log(275.483765,2),math.log(253.521484,2),math.log(290.102051,2)]
t_244 = [math.log(288.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(245.000000,2),math.log(267.000000,2),math.log(298.500000,2),math.log(277.250000,2),math.log(275.875000,2),math.log(260.468750,2),math.log(249.781250,2),math.log(254.781250,2),math.log(226.835938,2),math.log(216.091797,2),math.log(249.248047,2),math.log(250.767578,2),math.log(258.632324,2),math.log(289.827515,2),math.log(286.878906,2),math.log(300.748077,2)]
t_245 = [math.log(256.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(253.000000,2),math.log(247.500000,2),math.log(257.500000,2),math.log(280.250000,2),math.log(290.562500,2),math.log(249.281250,2),math.log(268.328125,2),math.log(262.843750,2),math.log(243.859375,2),math.log(273.617188,2),math.log(285.634766,2),math.log(288.858887,2),math.log(290.962402,2),math.log(275.583740,2),math.log(310.427673,2),math.log(324.404175,2)]
t_246 = [math.log(240.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(246.000000,2),math.log(244.000000,2),math.log(241.500000,2),math.log(251.250000,2),math.log(249.750000,2),math.log(233.125000,2),math.log(209.437500,2),math.log(274.203125,2),math.log(262.679688,2),math.log(260.125000,2),math.log(216.841797,2),math.log(250.499023,2),math.log(272.151367,2),math.log(269.292236,2),math.log(297.043701,2),math.log(327.875671,2),math.log(413.521332,2)]
t_247 = [math.log(320.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(280.000000,2),math.log(255.000000,2),math.log(272.750000,2),math.log(240.500000,2),math.log(229.000000,2),math.log(252.218750,2),math.log(276.812500,2),math.log(283.031250,2),math.log(284.691406,2),math.log(239.736328,2),math.log(247.706055,2),math.log(233.140625,2),math.log(279.850098,2),math.log(322.727051,2),math.log(336.262329,2),math.log(357.027405,2)]
t_248 = [math.log(240.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(250.000000,2),math.log(249.000000,2),math.log(227.000000,2),math.log(248.500000,2),math.log(255.750000,2),math.log(258.250000,2),math.log(273.437500,2),math.log(279.109375,2),math.log(250.335938,2),math.log(225.738281,2),math.log(221.226562,2),math.log(223.089844,2),math.log(230.373535,2),math.log(248.247559,2),math.log(264.992554,2),math.log(284.870850,2),math.log(309.240295,2)]
t_249 = [math.log(240.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(223.000000,2),math.log(235.000000,2),math.log(247.000000,2),math.log(264.500000,2),math.log(276.750000,2),math.log(298.593750,2),math.log(284.875000,2),math.log(277.000000,2),math.log(274.824219,2),math.log(229.402344,2),math.log(257.144531,2),math.log(249.331055,2),math.log(253.695068,2),math.log(229.818115,2),math.log(272.197449,2),math.log(310.325287,2)]
t_250 = [math.log(256.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(277.000000,2),math.log(296.000000,2),math.log(274.250000,2),math.log(263.625000,2),math.log(236.218750,2),math.log(230.500000,2),math.log(221.101562,2),math.log(238.746094,2),math.log(250.304688,2),math.log(292.534180,2),math.log(266.125977,2),math.log(308.795166,2),math.log(299.540527,2),math.log(349.073425,2),math.log(414.008972,2)]
t_251 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(222.000000,2),math.log(234.000000,2),math.log(278.500000,2),math.log(277.750000,2),math.log(267.625000,2),math.log(255.187500,2),math.log(254.500000,2),math.log(272.343750,2),math.log(269.218750,2),math.log(275.359375,2),math.log(247.388672,2),math.log(297.268555,2),math.log(275.495117,2),math.log(292.608643,2),math.log(276.983765,2),math.log(283.768188,2),math.log(297.210419,2)]
t_252 = [math.log(256.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(227.000000,2),math.log(229.500000,2),math.log(206.500000,2),math.log(201.375000,2),math.log(237.000000,2),math.log(245.187500,2),math.log(245.343750,2),math.log(279.414062,2),math.log(271.902344,2),math.log(263.103516,2),math.log(255.144531,2),math.log(269.638184,2),math.log(263.826416,2),math.log(302.936157,2),math.log(256.665894,2),math.log(316.741058,2)]
t_253 = [math.log(256.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(242.000000,2),math.log(271.000000,2),math.log(240.500000,2),math.log(262.750000,2),math.log(292.375000,2),math.log(288.687500,2),math.log(277.468750,2),math.log(264.328125,2),math.log(244.523438,2),math.log(250.050781,2),math.log(290.443359,2),math.log(280.221680,2),math.log(279.909668,2),math.log(273.669434,2),math.log(304.647461,2),math.log(349.128418,2),math.log(484.666351,2)]
t_254 = [math.log(256.000000,2),math.log(272.000000,2),math.log(312.000000,2),math.log(268.000000,2),math.log(249.000000,2),math.log(259.500000,2),math.log(252.000000,2),math.log(253.875000,2),math.log(301.375000,2),math.log(288.593750,2),math.log(265.000000,2),math.log(289.812500,2),math.log(261.121094,2),math.log(262.306641,2),math.log(249.957031,2),math.log(258.741211,2),math.log(268.043701,2),math.log(273.698975,2),math.log(315.907410,2),math.log(415.868591,2)]
t_255 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(245.000000,2),math.log(241.500000,2),math.log(252.250000,2),math.log(266.937500,2),math.log(257.531250,2),math.log(227.781250,2),math.log(244.093750,2),math.log(262.167969,2),math.log(258.003906,2),math.log(283.023438,2),math.log(296.326660,2),math.log(316.587646,2),math.log(344.246826,2),math.log(369.477661,2),math.log(415.057495,2)]




#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00002073
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00002073)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00002073
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00002073)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00002073
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00002073)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00002073
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00002073)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00002073
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00002073)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00002073
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00002073)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00002073
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00002073)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00002073
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00002073)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00002073
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00002073)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00002073
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00002073)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00002073
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00002073)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00002073
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00002073)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00002073
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00002073)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00002073
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00002073)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00002073
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00002073)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00002073
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00002073)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00002073
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00002073)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00002073
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00002073)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00002073
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00002073)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00002073
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00002073)**2)


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
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha= 1)
plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha= 1)
plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha= 1)


#Formatting the plot
plt.xlabel('$log_2(|\phi|)$')
plt.ylabel('$log_2(T(\phi,a))$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 8 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(8.5,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
