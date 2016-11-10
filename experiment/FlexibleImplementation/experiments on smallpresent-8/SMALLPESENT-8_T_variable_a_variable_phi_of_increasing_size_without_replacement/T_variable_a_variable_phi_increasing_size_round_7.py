import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(256.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(252.500000,2),math.log(244.750000,2),math.log(260.875000,2),math.log(263.000000,2),math.log(229.937500,2),math.log(235.718750,2),math.log(251.679688,2),math.log(223.433594,2),math.log(254.457031,2),math.log(299.069336,2),math.log(265.128418,2),math.log(268.717285,2),math.log(293.332397,2),math.log(320.820618,2),math.log(438.875793,2)]
t_1 = [math.log(240.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(266.000000,2),math.log(271.000000,2),math.log(253.500000,2),math.log(236.500000,2),math.log(254.000000,2),math.log(207.812500,2),math.log(247.343750,2),math.log(280.343750,2),math.log(245.914062,2),math.log(250.175781,2),math.log(245.884766,2),math.log(249.706055,2),math.log(266.636230,2),math.log(234.906982,2),math.log(253.239258,2),math.log(332.425903,2),math.log(440.645782,2)]
t_2 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(258.000000,2),math.log(245.000000,2),math.log(250.000000,2),math.log(254.750000,2),math.log(222.375000,2),math.log(229.062500,2),math.log(246.671875,2),math.log(226.007812,2),math.log(221.734375,2),math.log(256.552734,2),math.log(242.972656,2),math.log(222.207520,2),math.log(282.814697,2),math.log(299.090820,2),math.log(387.236267,2),math.log(520.341614,2)]
t_3 = [math.log(256.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(248.500000,2),math.log(246.750000,2),math.log(232.250000,2),math.log(237.187500,2),math.log(264.406250,2),math.log(248.062500,2),math.log(220.757812,2),math.log(247.089844,2),math.log(265.316406,2),math.log(253.714844,2),math.log(272.225586,2),math.log(312.050781,2),math.log(360.606812,2),math.log(483.024048,2),math.log(722.568451,2)]
t_4 = [math.log(272.000000,2),math.log(304.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(234.500000,2),math.log(261.500000,2),math.log(274.625000,2),math.log(295.562500,2),math.log(297.625000,2),math.log(242.015625,2),math.log(212.875000,2),math.log(231.007812,2),math.log(234.298828,2),math.log(225.271484,2),math.log(228.549316,2),math.log(269.448242,2),math.log(318.599487,2),math.log(415.925293,2),math.log(548.206238,2)]
t_5 = [math.log(240.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(242.000000,2),math.log(254.000000,2),math.log(242.000000,2),math.log(239.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(257.437500,2),math.log(208.250000,2),math.log(231.492188,2),math.log(222.742188,2),math.log(249.054688,2),math.log(277.609375,2),math.log(224.084473,2),math.log(297.363770,2),math.log(348.329834,2),math.log(414.593750,2),math.log(524.401733,2)]
t_6 = [math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(274.000000,2),math.log(242.000000,2),math.log(251.500000,2),math.log(287.875000,2),math.log(260.687500,2),math.log(255.687500,2),math.log(254.687500,2),math.log(238.242188,2),math.log(281.839844,2),math.log(264.070312,2),math.log(282.511719,2),math.log(322.552246,2),math.log(339.004883,2),math.log(376.838623,2),math.log(485.825317,2),math.log(670.134094,2)]
t_7 = [math.log(272.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(290.000000,2),math.log(264.500000,2),math.log(254.250000,2),math.log(231.000000,2),math.log(218.625000,2),math.log(235.718750,2),math.log(249.375000,2),math.log(300.671875,2),math.log(295.476562,2),math.log(311.025391,2),math.log(310.272461,2),math.log(342.014160,2),math.log(323.134277,2),math.log(422.360840,2),math.log(567.429749,2),math.log(907.888336,2)]
t_8 = [math.log(272.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(252.000000,2),math.log(230.000000,2),math.log(233.000000,2),math.log(245.250000,2),math.log(246.250000,2),math.log(216.875000,2),math.log(235.093750,2),math.log(251.312500,2),math.log(258.304688,2),math.log(232.367188,2),math.log(240.964844,2),math.log(313.926758,2),math.log(329.390625,2),math.log(354.157471,2),math.log(352.440796,2),math.log(383.011292,2),math.log(503.085571,2)]
t_9 = [math.log(288.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(246.000000,2),math.log(245.000000,2),math.log(253.500000,2),math.log(250.000000,2),math.log(254.125000,2),math.log(234.687500,2),math.log(242.406250,2),math.log(229.031250,2),math.log(224.523438,2),math.log(234.007812,2),math.log(296.316406,2),math.log(305.041016,2),math.log(258.647461,2),math.log(280.854980,2),math.log(318.758057,2),math.log(400.557983,2),math.log(502.275726,2)]
t_10 = [math.log(272.000000,2),math.log(272.000000,2),math.log(316.000000,2),math.log(274.000000,2),math.log(246.000000,2),math.log(263.500000,2),math.log(250.750000,2),math.log(272.500000,2),math.log(281.187500,2),math.log(246.593750,2),math.log(269.968750,2),math.log(252.156250,2),math.log(262.953125,2),math.log(232.552734,2),math.log(262.002930,2),math.log(290.803711,2),math.log(337.805908,2),math.log(428.184326,2),math.log(694.026001,2),math.log(1193.423798,2)]
t_11 = [math.log(240.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(253.000000,2),math.log(252.500000,2),math.log(225.500000,2),math.log(267.500000,2),math.log(251.562500,2),math.log(263.500000,2),math.log(272.562500,2),math.log(307.203125,2),math.log(320.148438,2),math.log(331.564453,2),math.log(318.031250,2),math.log(342.485352,2),math.log(393.274170,2),math.log(479.068970,2),math.log(790.411133,2),math.log(1355.027344,2)]
t_12 = [math.log(256.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(216.000000,2),math.log(222.000000,2),math.log(223.750000,2),math.log(231.125000,2),math.log(238.562500,2),math.log(271.218750,2),math.log(238.078125,2),math.log(238.515625,2),math.log(242.343750,2),math.log(256.458984,2),math.log(268.555664,2),math.log(268.253418,2),math.log(223.693604,2),math.log(271.868042,2),math.log(352.058838,2),math.log(483.846222,2)]
t_13 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(224.000000,2),math.log(257.000000,2),math.log(261.500000,2),math.log(269.250000,2),math.log(253.250000,2),math.log(238.250000,2),math.log(226.625000,2),math.log(272.015625,2),math.log(295.843750,2),math.log(270.566406,2),math.log(303.652344,2),math.log(307.166016,2),math.log(309.634277,2),math.log(319.818359,2),math.log(348.732178,2),math.log(468.725952,2),math.log(630.027313,2)]
t_14 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(282.250000,2),math.log(250.375000,2),math.log(249.125000,2),math.log(236.843750,2),math.log(242.250000,2),math.log(259.890625,2),math.log(248.789062,2),math.log(232.583984,2),math.log(269.987305,2),math.log(289.244141,2),math.log(327.181641,2),math.log(364.940186,2),math.log(443.896118,2),math.log(654.854309,2)]
t_15 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(302.000000,2),math.log(276.750000,2),math.log(283.500000,2),math.log(259.812500,2),math.log(237.812500,2),math.log(253.187500,2),math.log(281.351562,2),math.log(301.226562,2),math.log(265.392578,2),math.log(269.151367,2),math.log(301.814941,2),math.log(320.630371,2),math.log(383.185303,2),math.log(476.428589,2),math.log(685.341888,2)]
t_16 = [math.log(224.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(259.500000,2),math.log(227.750000,2),math.log(232.500000,2),math.log(260.812500,2),math.log(263.250000,2),math.log(266.171875,2),math.log(263.554688,2),math.log(286.093750,2),math.log(240.541016,2),math.log(236.632812,2),math.log(236.379883,2),math.log(274.022949,2),math.log(319.015015,2),math.log(415.561462,2),math.log(629.007904,2)]
t_17 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(263.000000,2),math.log(284.000000,2),math.log(250.750000,2),math.log(249.875000,2),math.log(231.375000,2),math.log(258.781250,2),math.log(262.812500,2),math.log(233.898438,2),math.log(237.160156,2),math.log(269.203125,2),math.log(268.016602,2),math.log(279.824219,2),math.log(265.203857,2),math.log(329.564697,2),math.log(418.906616,2),math.log(585.431824,2)]
t_18 = [math.log(272.000000,2),math.log(288.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(220.000000,2),math.log(254.000000,2),math.log(236.500000,2),math.log(214.125000,2),math.log(253.375000,2),math.log(246.468750,2),math.log(255.796875,2),math.log(292.601562,2),math.log(267.960938,2),math.log(292.757812,2),math.log(271.989258,2),math.log(250.151367,2),math.log(265.529785,2),math.log(299.389526,2),math.log(448.088684,2),math.log(732.633331,2)]
t_19 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(278.000000,2),math.log(271.000000,2),math.log(275.000000,2),math.log(318.250000,2),math.log(313.875000,2),math.log(247.500000,2),math.log(306.437500,2),math.log(282.859375,2),math.log(230.726562,2),math.log(239.976562,2),math.log(211.455078,2),math.log(226.218750,2),math.log(281.113770,2),math.log(275.395264,2),math.log(325.402710,2),math.log(405.543823,2),math.log(573.040283,2)]
t_20 = [math.log(240.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(267.000000,2),math.log(265.250000,2),math.log(303.375000,2),math.log(295.562500,2),math.log(305.062500,2),math.log(290.828125,2),math.log(281.523438,2),math.log(291.523438,2),math.log(255.578125,2),math.log(287.313477,2),math.log(266.778809,2),math.log(264.360840,2),math.log(310.721313,2),math.log(403.766296,2),math.log(574.447540,2)]
t_21 = [math.log(256.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(235.000000,2),math.log(241.500000,2),math.log(240.500000,2),math.log(212.625000,2),math.log(248.437500,2),math.log(277.781250,2),math.log(286.015625,2),math.log(296.742188,2),math.log(348.945312,2),math.log(312.222656,2),math.log(301.541992,2),math.log(251.534180,2),math.log(291.522949,2),math.log(294.536133,2),math.log(383.742493,2),math.log(531.669708,2)]
t_22 = [math.log(272.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(240.000000,2),math.log(283.000000,2),math.log(269.000000,2),math.log(225.250000,2),math.log(252.500000,2),math.log(244.250000,2),math.log(255.781250,2),math.log(269.421875,2),math.log(236.945312,2),math.log(248.828125,2),math.log(219.832031,2),math.log(230.477539,2),math.log(291.254883,2),math.log(319.658203,2),math.log(358.223755,2),math.log(560.607666,2),math.log(780.582611,2)]
t_23 = [math.log(304.000000,2),math.log(280.000000,2),math.log(228.000000,2),math.log(228.000000,2),math.log(261.000000,2),math.log(256.500000,2),math.log(268.250000,2),math.log(266.375000,2),math.log(215.562500,2),math.log(245.375000,2),math.log(226.734375,2),math.log(199.109375,2),math.log(238.679688,2),math.log(255.849609,2),math.log(245.386719,2),math.log(274.604980,2),math.log(299.534180,2),math.log(425.568359,2),math.log(532.709412,2),math.log(871.709900,2)]
t_24 = [math.log(256.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(294.000000,2),math.log(285.000000,2),math.log(259.000000,2),math.log(262.500000,2),math.log(257.500000,2),math.log(254.062500,2),math.log(270.093750,2),math.log(268.578125,2),math.log(266.585938,2),math.log(275.808594,2),math.log(257.287109,2),math.log(331.208008,2),math.log(312.661621,2),math.log(316.549316,2),math.log(343.882690,2),math.log(412.958008,2),math.log(674.109375,2)]
t_25 = [math.log(224.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(263.000000,2),math.log(248.750000,2),math.log(273.500000,2),math.log(239.562500,2),math.log(284.968750,2),math.log(293.359375,2),math.log(282.312500,2),math.log(277.785156,2),math.log(259.119141,2),math.log(298.535156,2),math.log(308.486816,2),math.log(322.526123,2),math.log(370.713989,2),math.log(415.822449,2),math.log(618.143341,2)]
t_26 = [math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(286.000000,2),math.log(280.000000,2),math.log(293.500000,2),math.log(291.625000,2),math.log(245.375000,2),math.log(248.031250,2),math.log(234.203125,2),math.log(245.593750,2),math.log(258.003906,2),math.log(209.474609,2),math.log(241.928711,2),math.log(283.386230,2),math.log(295.728027,2),math.log(419.881958,2),math.log(620.660034,2),math.log(988.406189,2)]
t_27 = [math.log(272.000000,2),math.log(272.000000,2),math.log(284.000000,2),math.log(276.000000,2),math.log(291.000000,2),math.log(269.500000,2),math.log(239.500000,2),math.log(285.625000,2),math.log(254.125000,2),math.log(260.562500,2),math.log(257.343750,2),math.log(253.429688,2),math.log(265.863281,2),math.log(348.419922,2),math.log(363.257812,2),math.log(380.339355,2),math.log(374.092773,2),math.log(542.798218,2),math.log(862.414978,2),math.log(1356.667969,2)]
t_28 = [math.log(272.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(250.000000,2),math.log(235.000000,2),math.log(226.000000,2),math.log(228.250000,2),math.log(266.625000,2),math.log(253.250000,2),math.log(270.156250,2),math.log(267.859375,2),math.log(238.468750,2),math.log(266.402344,2),math.log(279.503906,2),math.log(253.687500,2),math.log(281.630859,2),math.log(284.806641,2),math.log(335.265869,2),math.log(406.958435,2),math.log(682.119720,2)]
t_29 = [math.log(240.000000,2),math.log(216.000000,2),math.log(228.000000,2),math.log(250.000000,2),math.log(257.000000,2),math.log(232.500000,2),math.log(267.250000,2),math.log(265.125000,2),math.log(303.750000,2),math.log(237.062500,2),math.log(242.500000,2),math.log(266.375000,2),math.log(247.738281,2),math.log(270.208984,2),math.log(288.084961,2),math.log(328.436523,2),math.log(342.964844,2),math.log(418.177734,2),math.log(594.926025,2),math.log(935.009399,2)]
t_30 = [math.log(256.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(270.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(232.750000,2),math.log(239.750000,2),math.log(264.812500,2),math.log(279.062500,2),math.log(290.437500,2),math.log(295.140625,2),math.log(268.496094,2),math.log(259.535156,2),math.log(259.707031,2),math.log(291.131348,2),math.log(334.274414,2),math.log(488.019165,2),math.log(630.484741,2),math.log(1138.262482,2)]
t_31 = [math.log(304.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(264.000000,2),math.log(221.500000,2),math.log(240.250000,2),math.log(251.875000,2),math.log(260.875000,2),math.log(268.187500,2),math.log(260.781250,2),math.log(273.000000,2),math.log(308.058594,2),math.log(301.615234,2),math.log(296.846680,2),math.log(317.914551,2),math.log(362.659668,2),math.log(363.708740,2),math.log(456.813110,2),math.log(683.483551,2)]
t_32 = [math.log(272.000000,2),math.log(296.000000,2),math.log(268.000000,2),math.log(318.000000,2),math.log(291.000000,2),math.log(316.000000,2),math.log(272.500000,2),math.log(246.250000,2),math.log(247.000000,2),math.log(283.468750,2),math.log(281.843750,2),math.log(291.710938,2),math.log(264.855469,2),math.log(266.472656,2),math.log(238.994141,2),math.log(236.185547,2),math.log(299.715820,2),math.log(334.438843,2),math.log(395.559692,2),math.log(477.581116,2)]
t_33 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(222.000000,2),math.log(211.000000,2),math.log(244.000000,2),math.log(234.750000,2),math.log(274.500000,2),math.log(255.000000,2),math.log(282.406250,2),math.log(280.250000,2),math.log(270.453125,2),math.log(264.718750,2),math.log(253.548828,2),math.log(299.052734,2),math.log(309.375000,2),math.log(367.574951,2),math.log(459.332153,2),math.log(589.503601,2),math.log(808.775360,2)]
t_34 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(279.000000,2),math.log(304.000000,2),math.log(263.250000,2),math.log(264.500000,2),math.log(267.312500,2),math.log(245.937500,2),math.log(253.390625,2),math.log(249.390625,2),math.log(295.761719,2),math.log(274.845703,2),math.log(269.383789,2),math.log(310.610840,2),math.log(297.273438,2),math.log(344.007935,2),math.log(403.526978,2),math.log(549.369690,2)]
t_35 = [math.log(256.000000,2),math.log(304.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(275.000000,2),math.log(277.000000,2),math.log(264.250000,2),math.log(271.750000,2),math.log(274.500000,2),math.log(246.562500,2),math.log(242.593750,2),math.log(244.789062,2),math.log(270.148438,2),math.log(253.314453,2),math.log(259.742188,2),math.log(287.655762,2),math.log(338.746094,2),math.log(328.491333,2),math.log(450.708191,2),math.log(641.477692,2)]
t_36 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(262.000000,2),math.log(243.000000,2),math.log(223.000000,2),math.log(215.500000,2),math.log(276.500000,2),math.log(283.250000,2),math.log(305.875000,2),math.log(293.421875,2),math.log(272.171875,2),math.log(269.867188,2),math.log(251.802734,2),math.log(236.015625,2),math.log(241.733887,2),math.log(313.868164,2),math.log(399.642456,2),math.log(446.641541,2),math.log(649.834106,2)]
t_37 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(222.000000,2),math.log(246.000000,2),math.log(249.000000,2),math.log(257.500000,2),math.log(253.875000,2),math.log(274.250000,2),math.log(242.093750,2),math.log(218.640625,2),math.log(247.773438,2),math.log(241.433594,2),math.log(271.968750,2),math.log(246.930664,2),math.log(253.138672,2),math.log(262.698730,2),math.log(320.779053,2),math.log(403.072693,2),math.log(584.598572,2)]
t_38 = [math.log(240.000000,2),math.log(312.000000,2),math.log(300.000000,2),math.log(290.000000,2),math.log(259.000000,2),math.log(249.000000,2),math.log(243.750000,2),math.log(273.500000,2),math.log(222.000000,2),math.log(278.750000,2),math.log(266.218750,2),math.log(259.140625,2),math.log(279.058594,2),math.log(298.757812,2),math.log(311.677734,2),math.log(312.008789,2),math.log(357.270752,2),math.log(384.467896,2),math.log(475.553345,2),math.log(625.148132,2)]
t_39 = [math.log(272.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(296.000000,2),math.log(297.000000,2),math.log(267.000000,2),math.log(214.000000,2),math.log(241.375000,2),math.log(283.000000,2),math.log(258.468750,2),math.log(250.359375,2),math.log(263.539062,2),math.log(282.882812,2),math.log(279.681641,2),math.log(319.407227,2),math.log(323.238281,2),math.log(364.203369,2),math.log(476.713257,2),math.log(622.589417,2),math.log(962.301483,2)]
t_40 = [math.log(240.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(218.000000,2),math.log(258.500000,2),math.log(310.250000,2),math.log(299.500000,2),math.log(297.437500,2),math.log(292.500000,2),math.log(271.828125,2),math.log(276.914062,2),math.log(293.582031,2),math.log(283.542969,2),math.log(287.724609,2),math.log(264.829590,2),math.log(321.210205,2),math.log(311.706543,2),math.log(371.799255,2),math.log(479.699951,2)]
t_41 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(234.000000,2),math.log(267.000000,2),math.log(247.750000,2),math.log(258.375000,2),math.log(284.250000,2),math.log(275.531250,2),math.log(281.484375,2),math.log(272.750000,2),math.log(219.281250,2),math.log(209.810547,2),math.log(228.616211,2),math.log(245.358887,2),math.log(303.652344,2),math.log(405.868042,2),math.log(587.659912,2),math.log(858.317291,2)]
t_42 = [math.log(256.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(286.000000,2),math.log(281.000000,2),math.log(249.500000,2),math.log(262.500000,2),math.log(264.500000,2),math.log(280.875000,2),math.log(289.656250,2),math.log(265.437500,2),math.log(263.671875,2),math.log(228.605469,2),math.log(253.242188,2),math.log(283.770508,2),math.log(294.985352,2),math.log(319.483398,2),math.log(405.205444,2),math.log(553.561523,2),math.log(753.368744,2)]
t_43 = [math.log(256.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(242.000000,2),math.log(230.000000,2),math.log(250.000000,2),math.log(247.000000,2),math.log(252.625000,2),math.log(279.750000,2),math.log(250.656250,2),math.log(243.062500,2),math.log(282.562500,2),math.log(255.855469,2),math.log(271.445312,2),math.log(284.619141,2),math.log(312.591309,2),math.log(323.620850,2),math.log(398.155884,2),math.log(556.090515,2),math.log(873.451202,2)]
t_44 = [math.log(224.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(253.000000,2),math.log(241.000000,2),math.log(212.000000,2),math.log(223.625000,2),math.log(200.687500,2),math.log(211.250000,2),math.log(230.718750,2),math.log(247.218750,2),math.log(234.097656,2),math.log(252.509766,2),math.log(263.388672,2),math.log(329.406250,2),math.log(320.463867,2),math.log(336.821655,2),math.log(426.856567,2),math.log(484.129639,2)]
t_45 = [math.log(272.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(271.000000,2),math.log(272.500000,2),math.log(269.250000,2),math.log(255.875000,2),math.log(257.500000,2),math.log(239.718750,2),math.log(226.093750,2),math.log(248.437500,2),math.log(261.707031,2),math.log(263.193359,2),math.log(282.950195,2),math.log(295.602539,2),math.log(311.541748,2),math.log(400.625610,2),math.log(594.486511,2),math.log(986.338379,2)]
t_46 = [math.log(240.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(258.000000,2),math.log(279.500000,2),math.log(269.000000,2),math.log(279.625000,2),math.log(262.312500,2),math.log(257.343750,2),math.log(226.937500,2),math.log(232.312500,2),math.log(233.097656,2),math.log(238.166016,2),math.log(256.907227,2),math.log(291.910156,2),math.log(305.695312,2),math.log(297.059448,2),math.log(366.559875,2),math.log(520.792572,2)]
t_47 = [math.log(272.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(266.000000,2),math.log(265.000000,2),math.log(269.250000,2),math.log(281.875000,2),math.log(275.750000,2),math.log(251.625000,2),math.log(254.812500,2),math.log(256.664062,2),math.log(233.441406,2),math.log(232.632812,2),math.log(236.005859,2),math.log(249.774902,2),math.log(275.140869,2),math.log(325.151123,2),math.log(449.304016,2),math.log(666.472961,2)]
t_48 = [math.log(272.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(219.000000,2),math.log(220.500000,2),math.log(245.250000,2),math.log(233.125000,2),math.log(246.250000,2),math.log(225.687500,2),math.log(269.171875,2),math.log(252.351562,2),math.log(255.136719,2),math.log(266.003906,2),math.log(308.076172,2),math.log(279.320801,2),math.log(229.567383,2),math.log(291.587646,2),math.log(354.690796,2),math.log(424.375092,2)]
t_49 = [math.log(224.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(283.000000,2),math.log(268.500000,2),math.log(275.000000,2),math.log(255.125000,2),math.log(258.937500,2),math.log(257.468750,2),math.log(263.656250,2),math.log(270.000000,2),math.log(285.968750,2),math.log(270.429688,2),math.log(229.766602,2),math.log(270.049316,2),math.log(294.116211,2),math.log(365.635254,2),math.log(577.696594,2),math.log(837.781342,2)]
t_50 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(228.000000,2),math.log(201.000000,2),math.log(259.500000,2),math.log(252.500000,2),math.log(266.250000,2),math.log(241.375000,2),math.log(239.343750,2),math.log(247.640625,2),math.log(265.648438,2),math.log(290.691406,2),math.log(303.595703,2),math.log(283.137695,2),math.log(255.675781,2),math.log(299.324707,2),math.log(343.216919,2),math.log(385.827148,2),math.log(511.961945,2)]
t_51 = [math.log(272.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(233.000000,2),math.log(237.500000,2),math.log(257.750000,2),math.log(275.625000,2),math.log(265.687500,2),math.log(273.906250,2),math.log(264.343750,2),math.log(286.710938,2),math.log(266.207031,2),math.log(249.210938,2),math.log(267.143555,2),math.log(264.489258,2),math.log(296.150391,2),math.log(351.867798,2),math.log(433.750305,2),math.log(599.151855,2)]
t_52 = [math.log(240.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(278.000000,2),math.log(265.000000,2),math.log(235.000000,2),math.log(285.250000,2),math.log(250.750000,2),math.log(275.437500,2),math.log(260.875000,2),math.log(275.328125,2),math.log(282.343750,2),math.log(273.613281,2),math.log(264.285156,2),math.log(311.465820,2),math.log(290.219238,2),math.log(275.734863,2),math.log(331.723633,2),math.log(410.942871,2),math.log(509.429779,2)]
t_53 = [math.log(240.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(278.000000,2),math.log(281.000000,2),math.log(296.500000,2),math.log(264.250000,2),math.log(235.000000,2),math.log(250.625000,2),math.log(273.281250,2),math.log(239.015625,2),math.log(275.804688,2),math.log(318.933594,2),math.log(291.546875,2),math.log(313.015625,2),math.log(316.017090,2),math.log(344.098389,2),math.log(446.040283,2),math.log(599.116455,2),math.log(863.013702,2)]
t_54 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(286.000000,2),math.log(288.000000,2),math.log(305.250000,2),math.log(301.375000,2),math.log(279.187500,2),math.log(267.562500,2),math.log(253.281250,2),math.log(286.593750,2),math.log(276.207031,2),math.log(280.076172,2),math.log(311.800781,2),math.log(352.572754,2),math.log(375.947266,2),math.log(475.249756,2),math.log(713.617920,2),math.log(1210.763519,2)]
t_55 = [math.log(320.000000,2),math.log(304.000000,2),math.log(252.000000,2),math.log(238.000000,2),math.log(264.000000,2),math.log(242.500000,2),math.log(247.750000,2),math.log(260.625000,2),math.log(215.125000,2),math.log(194.968750,2),math.log(213.718750,2),math.log(228.945312,2),math.log(262.007812,2),math.log(255.160156,2),math.log(265.807617,2),math.log(315.912598,2),math.log(343.472656,2),math.log(337.373413,2),math.log(421.010559,2),math.log(631.857819,2)]
t_56 = [math.log(256.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(282.000000,2),math.log(280.000000,2),math.log(289.000000,2),math.log(254.750000,2),math.log(198.875000,2),math.log(206.750000,2),math.log(203.781250,2),math.log(253.687500,2),math.log(240.656250,2),math.log(204.753906,2),math.log(212.212891,2),math.log(228.249023,2),math.log(280.562012,2),math.log(255.697998,2),math.log(317.263550,2),math.log(354.050598,2),math.log(368.949310,2)]
t_57 = [math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(262.000000,2),math.log(308.000000,2),math.log(266.000000,2),math.log(260.500000,2),math.log(222.625000,2),math.log(218.875000,2),math.log(236.593750,2),math.log(236.828125,2),math.log(259.132812,2),math.log(276.031250,2),math.log(267.322266,2),math.log(262.694336,2),math.log(355.147949,2),math.log(418.550781,2),math.log(488.387329,2),math.log(719.966431,2),math.log(1189.718872,2)]
t_58 = [math.log(224.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(268.000000,2),math.log(225.000000,2),math.log(246.500000,2),math.log(242.000000,2),math.log(248.500000,2),math.log(254.562500,2),math.log(253.156250,2),math.log(246.093750,2),math.log(256.539062,2),math.log(278.804688,2),math.log(272.964844,2),math.log(281.150391,2),math.log(299.332031,2),math.log(364.784668,2),math.log(399.957031,2),math.log(596.585266,2),math.log(942.765533,2)]
t_59 = [math.log(288.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(257.000000,2),math.log(307.000000,2),math.log(284.750000,2),math.log(226.000000,2),math.log(232.000000,2),math.log(240.562500,2),math.log(242.500000,2),math.log(249.039062,2),math.log(221.214844,2),math.log(210.244141,2),math.log(267.760742,2),math.log(268.386230,2),math.log(292.000488,2),math.log(383.786499,2),math.log(538.489197,2),math.log(831.248840,2)]
t_60 = [math.log(240.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(263.000000,2),math.log(261.500000,2),math.log(262.750000,2),math.log(266.812500,2),math.log(225.406250,2),math.log(212.640625,2),math.log(239.359375,2),math.log(237.484375,2),math.log(246.847656,2),math.log(248.440430,2),math.log(278.809570,2),math.log(303.736816,2),math.log(314.169189,2),math.log(474.666565,2),math.log(702.265625,2)]
t_61 = [math.log(256.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(294.000000,2),math.log(279.000000,2),math.log(306.000000,2),math.log(279.750000,2),math.log(272.000000,2),math.log(246.812500,2),math.log(260.937500,2),math.log(251.031250,2),math.log(261.078125,2),math.log(282.406250,2),math.log(276.498047,2),math.log(296.256836,2),math.log(304.316406,2),math.log(365.596436,2),math.log(441.094238,2),math.log(690.647339,2),math.log(1153.331818,2)]
t_62 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(231.000000,2),math.log(199.000000,2),math.log(229.750000,2),math.log(231.500000,2),math.log(225.250000,2),math.log(211.625000,2),math.log(249.046875,2),math.log(218.460938,2),math.log(251.210938,2),math.log(247.957031,2),math.log(239.484375,2),math.log(300.473145,2),math.log(375.691895,2),math.log(443.382935,2),math.log(617.837952,2),math.log(901.980316,2)]
t_63 = [math.log(224.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(267.000000,2),math.log(280.000000,2),math.log(282.250000,2),math.log(265.875000,2),math.log(291.562500,2),math.log(244.218750,2),math.log(216.781250,2),math.log(238.281250,2),math.log(266.207031,2),math.log(243.677734,2),math.log(295.179688,2),math.log(295.023438,2),math.log(333.597168,2),math.log(449.430908,2),math.log(574.844788,2),math.log(902.810394,2)]
t_64 = [math.log(224.000000,2),math.log(256.000000,2),math.log(296.000000,2),math.log(288.000000,2),math.log(239.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(258.000000,2),math.log(263.312500,2),math.log(268.500000,2),math.log(247.796875,2),math.log(249.367188,2),math.log(277.753906,2),math.log(261.146484,2),math.log(242.006836,2),math.log(268.685547,2),math.log(310.541260,2),math.log(359.290771,2),math.log(398.664612,2),math.log(388.254791,2)]
t_65 = [math.log(272.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(269.000000,2),math.log(243.000000,2),math.log(252.500000,2),math.log(269.500000,2),math.log(304.125000,2),math.log(275.718750,2),math.log(279.515625,2),math.log(267.687500,2),math.log(263.125000,2),math.log(266.976562,2),math.log(230.679688,2),math.log(236.766602,2),math.log(229.045166,2),math.log(288.954102,2),math.log(355.394714,2),math.log(469.276520,2)]
t_66 = [math.log(272.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(270.500000,2),math.log(273.000000,2),math.log(271.500000,2),math.log(262.125000,2),math.log(290.906250,2),math.log(265.437500,2),math.log(285.976562,2),math.log(271.957031,2),math.log(301.695312,2),math.log(290.482422,2),math.log(284.751465,2),math.log(315.212891,2),math.log(391.154419,2),math.log(465.626709,2),math.log(713.480988,2)]
t_67 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(249.000000,2),math.log(229.500000,2),math.log(268.250000,2),math.log(244.375000,2),math.log(232.812500,2),math.log(257.500000,2),math.log(253.687500,2),math.log(276.570312,2),math.log(293.925781,2),math.log(319.646484,2),math.log(324.977539,2),math.log(371.949707,2),math.log(426.902344,2),math.log(540.014648,2),math.log(711.839172,2),math.log(1098.168732,2)]
t_68 = [math.log(256.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(242.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(256.000000,2),math.log(255.125000,2),math.log(266.625000,2),math.log(253.062500,2),math.log(256.203125,2),math.log(262.476562,2),math.log(278.238281,2),math.log(290.876953,2),math.log(272.845703,2),math.log(287.562988,2),math.log(270.614746,2),math.log(334.965698,2),math.log(439.100098,2),math.log(639.215057,2)]
t_69 = [math.log(240.000000,2),math.log(304.000000,2),math.log(272.000000,2),math.log(254.000000,2),math.log(279.000000,2),math.log(268.000000,2),math.log(254.500000,2),math.log(270.250000,2),math.log(271.625000,2),math.log(251.187500,2),math.log(285.718750,2),math.log(264.390625,2),math.log(255.746094,2),math.log(255.693359,2),math.log(270.535156,2),math.log(263.319336,2),math.log(308.211914,2),math.log(339.427612,2),math.log(426.461121,2),math.log(532.528870,2)]
t_70 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(238.000000,2),math.log(216.500000,2),math.log(252.500000,2),math.log(255.375000,2),math.log(274.312500,2),math.log(250.093750,2),math.log(263.656250,2),math.log(249.101562,2),math.log(237.734375,2),math.log(278.685547,2),math.log(280.650391,2),math.log(286.418457,2),math.log(303.058105,2),math.log(353.270264,2),math.log(443.731323,2),math.log(639.441010,2)]
t_71 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(273.000000,2),math.log(273.500000,2),math.log(260.000000,2),math.log(229.625000,2),math.log(250.375000,2),math.log(263.687500,2),math.log(252.796875,2),math.log(254.507812,2),math.log(259.046875,2),math.log(239.000000,2),math.log(269.844727,2),math.log(268.927734,2),math.log(333.037842,2),math.log(519.797363,2),math.log(809.262451,2),math.log(1498.462891,2)]
t_72 = [math.log(288.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(240.000000,2),math.log(263.000000,2),math.log(253.500000,2),math.log(250.000000,2),math.log(259.500000,2),math.log(252.875000,2),math.log(267.687500,2),math.log(219.609375,2),math.log(234.656250,2),math.log(257.042969,2),math.log(272.277344,2),math.log(281.312500,2),math.log(290.160156,2),math.log(325.526611,2),math.log(400.210327,2),math.log(583.962463,2),math.log(953.998138,2)]
t_73 = [math.log(224.000000,2),math.log(216.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(292.000000,2),math.log(303.000000,2),math.log(287.750000,2),math.log(266.125000,2),math.log(275.125000,2),math.log(249.687500,2),math.log(247.890625,2),math.log(252.937500,2),math.log(285.816406,2),math.log(259.259766,2),math.log(241.792969,2),math.log(255.745117,2),math.log(284.644043,2),math.log(310.314697,2),math.log(347.892883,2),math.log(448.501007,2)]
t_74 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(266.000000,2),math.log(276.000000,2),math.log(250.500000,2),math.log(259.500000,2),math.log(278.875000,2),math.log(302.812500,2),math.log(276.062500,2),math.log(266.937500,2),math.log(339.085938,2),math.log(304.074219,2),math.log(283.416016,2),math.log(278.258789,2),math.log(319.590820,2),math.log(348.698975,2),math.log(508.019409,2),math.log(783.365784,2),math.log(1298.408295,2)]
t_75 = [math.log(224.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(239.000000,2),math.log(286.000000,2),math.log(274.000000,2),math.log(243.250000,2),math.log(232.250000,2),math.log(267.750000,2),math.log(258.218750,2),math.log(256.117188,2),math.log(252.398438,2),math.log(262.056641,2),math.log(356.672852,2),math.log(397.144531,2),math.log(558.259521,2),math.log(728.998169,2),math.log(1270.167175,2),math.log(2293.442261,2)]
t_76 = [math.log(256.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(261.500000,2),math.log(227.000000,2),math.log(260.875000,2),math.log(228.250000,2),math.log(242.875000,2),math.log(255.593750,2),math.log(236.757812,2),math.log(241.820312,2),math.log(243.726562,2),math.log(252.401367,2),math.log(283.951172,2),math.log(274.173340,2),math.log(287.138550,2),math.log(337.591980,2),math.log(440.279907,2)]
t_77 = [math.log(256.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(256.000000,2),math.log(287.000000,2),math.log(314.000000,2),math.log(282.250000,2),math.log(255.500000,2),math.log(272.500000,2),math.log(249.875000,2),math.log(233.328125,2),math.log(226.273438,2),math.log(263.687500,2),math.log(248.916016,2),math.log(263.975586,2),math.log(231.727051,2),math.log(296.872070,2),math.log(313.702393,2),math.log(410.931580,2),math.log(636.342316,2)]
t_78 = [math.log(272.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(309.000000,2),math.log(287.500000,2),math.log(261.000000,2),math.log(282.750000,2),math.log(287.125000,2),math.log(253.812500,2),math.log(248.484375,2),math.log(282.781250,2),math.log(253.109375,2),math.log(260.595703,2),math.log(276.768555,2),math.log(289.994141,2),math.log(290.693115,2),math.log(360.638184,2),math.log(429.326050,2),math.log(633.379425,2)]
t_79 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(254.000000,2),math.log(236.000000,2),math.log(259.000000,2),math.log(243.750000,2),math.log(233.375000,2),math.log(206.437500,2),math.log(253.437500,2),math.log(245.421875,2),math.log(269.171875,2),math.log(271.457031,2),math.log(275.195312,2),math.log(283.682617,2),math.log(290.759277,2),math.log(334.778564,2),math.log(441.811646,2),math.log(535.500977,2),math.log(818.799438,2)]
t_80 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(232.500000,2),math.log(225.750000,2),math.log(243.500000,2),math.log(263.187500,2),math.log(317.375000,2),math.log(285.500000,2),math.log(283.218750,2),math.log(278.152344,2),math.log(282.697266,2),math.log(300.624023,2),math.log(325.425293,2),math.log(292.423340,2),math.log(318.262817,2),math.log(374.438416,2),math.log(589.374176,2)]
t_81 = [math.log(240.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(239.000000,2),math.log(220.125000,2),math.log(238.625000,2),math.log(273.906250,2),math.log(275.734375,2),math.log(242.609375,2),math.log(265.343750,2),math.log(287.341797,2),math.log(312.263672,2),math.log(299.883301,2),math.log(285.909912,2),math.log(355.030518,2),math.log(518.825989,2),math.log(759.275085,2)]
t_82 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(221.000000,2),math.log(252.250000,2),math.log(249.750000,2),math.log(232.500000,2),math.log(248.125000,2),math.log(264.281250,2),math.log(225.265625,2),math.log(215.078125,2),math.log(195.794922,2),math.log(211.464844,2),math.log(228.212891,2),math.log(301.790527,2),math.log(354.522461,2),math.log(375.424438,2),math.log(563.129822,2)]
t_83 = [math.log(304.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(255.000000,2),math.log(250.500000,2),math.log(266.500000,2),math.log(262.000000,2),math.log(265.937500,2),math.log(257.593750,2),math.log(222.562500,2),math.log(193.859375,2),math.log(209.949219,2),math.log(243.455078,2),math.log(228.643555,2),math.log(262.007324,2),math.log(308.983887,2),math.log(336.036743,2),math.log(442.517883,2),math.log(732.488495,2)]
t_84 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(282.000000,2),math.log(282.500000,2),math.log(278.250000,2),math.log(276.250000,2),math.log(270.000000,2),math.log(264.250000,2),math.log(282.812500,2),math.log(282.546875,2),math.log(249.199219,2),math.log(267.468750,2),math.log(260.217773,2),math.log(270.593262,2),math.log(282.844727,2),math.log(319.876465,2),math.log(416.604065,2),math.log(571.647034,2)]
t_85 = [math.log(256.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(277.000000,2),math.log(288.500000,2),math.log(255.750000,2),math.log(266.000000,2),math.log(297.000000,2),math.log(269.562500,2),math.log(246.281250,2),math.log(228.601562,2),math.log(245.015625,2),math.log(238.306641,2),math.log(258.467773,2),math.log(275.041016,2),math.log(288.903564,2),math.log(336.629761,2),math.log(463.172180,2),math.log(710.496552,2)]
t_86 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(258.000000,2),math.log(309.000000,2),math.log(273.000000,2),math.log(254.000000,2),math.log(236.500000,2),math.log(274.875000,2),math.log(252.750000,2),math.log(258.734375,2),math.log(248.820312,2),math.log(273.449219,2),math.log(240.837891,2),math.log(258.372070,2),math.log(279.990723,2),math.log(295.169189,2),math.log(334.648804,2),math.log(398.707336,2),math.log(618.904724,2)]
t_87 = [math.log(240.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(266.000000,2),math.log(247.000000,2),math.log(262.500000,2),math.log(265.250000,2),math.log(278.125000,2),math.log(273.625000,2),math.log(242.125000,2),math.log(276.109375,2),math.log(245.601562,2),math.log(292.855469,2),math.log(320.996094,2),math.log(278.336914,2),math.log(304.432617,2),math.log(346.048828,2),math.log(430.676270,2),math.log(658.064270,2),math.log(1067.920197,2)]
t_88 = [math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(276.000000,2),math.log(245.000000,2),math.log(264.250000,2),math.log(261.500000,2),math.log(259.937500,2),math.log(249.406250,2),math.log(263.781250,2),math.log(250.117188,2),math.log(229.546875,2),math.log(260.607422,2),math.log(298.011719,2),math.log(312.762695,2),math.log(314.120850,2),math.log(373.705811,2),math.log(483.072388,2),math.log(618.266174,2)]
t_89 = [math.log(272.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(254.000000,2),math.log(222.000000,2),math.log(245.000000,2),math.log(255.750000,2),math.log(272.562500,2),math.log(268.593750,2),math.log(238.671875,2),math.log(275.218750,2),math.log(242.070312,2),math.log(288.441406,2),math.log(278.550781,2),math.log(296.769531,2),math.log(357.489502,2),math.log(380.559692,2),math.log(512.162842,2),math.log(717.782837,2)]
t_90 = [math.log(272.000000,2),math.log(264.000000,2),math.log(312.000000,2),math.log(274.000000,2),math.log(270.000000,2),math.log(279.500000,2),math.log(253.500000,2),math.log(231.750000,2),math.log(230.312500,2),math.log(251.406250,2),math.log(219.750000,2),math.log(210.476562,2),math.log(248.714844,2),math.log(253.921875,2),math.log(228.646484,2),math.log(293.733887,2),math.log(336.166016,2),math.log(494.798096,2),math.log(693.711548,2),math.log(1195.368439,2)]
t_91 = [math.log(224.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(304.000000,2),math.log(284.000000,2),math.log(252.000000,2),math.log(230.750000,2),math.log(208.250000,2),math.log(239.500000,2),math.log(212.875000,2),math.log(286.625000,2),math.log(249.281250,2),math.log(253.578125,2),math.log(288.990234,2),math.log(339.392578,2),math.log(356.498535,2),math.log(441.703125,2),math.log(666.520508,2),math.log(1070.353882,2),math.log(1763.455261,2)]
t_92 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(285.000000,2),math.log(265.500000,2),math.log(289.250000,2),math.log(269.000000,2),math.log(279.625000,2),math.log(287.593750,2),math.log(264.046875,2),math.log(298.140625,2),math.log(250.402344,2),math.log(251.341797,2),math.log(274.418945,2),math.log(305.296875,2),math.log(302.610596,2),math.log(398.872803,2),math.log(520.621704,2),math.log(769.879425,2)]
t_93 = [math.log(240.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(263.000000,2),math.log(253.500000,2),math.log(276.500000,2),math.log(254.000000,2),math.log(259.937500,2),math.log(264.156250,2),math.log(243.328125,2),math.log(248.265625,2),math.log(235.761719,2),math.log(249.767578,2),math.log(265.069336,2),math.log(289.992188,2),math.log(351.462402,2),math.log(482.535645,2),math.log(742.600281,2),math.log(1179.996063,2)]
t_94 = [math.log(272.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(266.000000,2),math.log(282.000000,2),math.log(249.500000,2),math.log(249.875000,2),math.log(241.375000,2),math.log(217.593750,2),math.log(231.906250,2),math.log(242.984375,2),math.log(264.531250,2),math.log(272.750000,2),math.log(307.140625,2),math.log(293.755859,2),math.log(312.319580,2),math.log(394.327393,2),math.log(534.004639,2),math.log(894.437714,2)]
t_95 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(262.000000,2),math.log(245.000000,2),math.log(251.000000,2),math.log(242.000000,2),math.log(231.000000,2),math.log(269.437500,2),math.log(274.562500,2),math.log(271.906250,2),math.log(304.554688,2),math.log(322.574219,2),math.log(267.121094,2),math.log(260.889648,2),math.log(288.594727,2),math.log(286.971680,2),math.log(369.857544,2),math.log(470.733887,2),math.log(640.292114,2)]
t_96 = [math.log(224.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(231.000000,2),math.log(213.000000,2),math.log(261.250000,2),math.log(252.625000,2),math.log(275.000000,2),math.log(270.093750,2),math.log(299.484375,2),math.log(251.578125,2),math.log(257.765625,2),math.log(247.460938,2),math.log(280.949219,2),math.log(258.258789,2),math.log(243.545410,2),math.log(264.139526,2),math.log(324.137024,2),math.log(473.529236,2)]
t_97 = [math.log(272.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(241.000000,2),math.log(218.250000,2),math.log(244.375000,2),math.log(216.250000,2),math.log(212.750000,2),math.log(216.359375,2),math.log(235.554688,2),math.log(241.902344,2),math.log(218.964844,2),math.log(268.115234,2),math.log(271.589355,2),math.log(265.065186,2),math.log(310.918335,2),math.log(403.193909,2),math.log(518.171448,2)]
t_98 = [math.log(240.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(290.000000,2),math.log(321.000000,2),math.log(291.500000,2),math.log(241.500000,2),math.log(238.250000,2),math.log(228.437500,2),math.log(226.281250,2),math.log(235.906250,2),math.log(268.421875,2),math.log(268.636719,2),math.log(265.890625,2),math.log(269.257812,2),math.log(289.970703,2),math.log(316.864014,2),math.log(342.853516,2),math.log(444.888306,2),math.log(677.848541,2)]
t_99 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(294.000000,2),math.log(298.000000,2),math.log(276.000000,2),math.log(275.000000,2),math.log(277.875000,2),math.log(245.625000,2),math.log(218.187500,2),math.log(238.156250,2),math.log(255.242188,2),math.log(253.914062,2),math.log(286.687500,2),math.log(267.189453,2),math.log(309.817383,2),math.log(338.619141,2),math.log(437.397949,2),math.log(570.695801,2),math.log(912.722504,2)]
t_100 = [math.log(224.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(235.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(233.000000,2),math.log(270.062500,2),math.log(256.343750,2),math.log(232.531250,2),math.log(238.640625,2),math.log(217.945312,2),math.log(205.451172,2),math.log(251.074219,2),math.log(264.492188,2),math.log(252.454590,2),math.log(297.561768,2),math.log(330.614014,2),math.log(450.172974,2)]
t_101 = [math.log(272.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(232.000000,2),math.log(274.000000,2),math.log(235.000000,2),math.log(263.250000,2),math.log(270.125000,2),math.log(258.375000,2),math.log(232.906250,2),math.log(261.359375,2),math.log(258.757812,2),math.log(274.503906,2),math.log(269.894531,2),math.log(293.138672,2),math.log(288.027344,2),math.log(272.232910,2),math.log(333.284424,2),math.log(378.220642,2),math.log(542.502014,2)]
t_102 = [math.log(256.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(254.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(245.750000,2),math.log(243.500000,2),math.log(262.250000,2),math.log(235.875000,2),math.log(231.171875,2),math.log(238.093750,2),math.log(232.035156,2),math.log(274.931641,2),math.log(250.820312,2),math.log(285.339355,2),math.log(317.008789,2),math.log(366.107910,2),math.log(456.677612,2),math.log(606.902069,2)]
t_103 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(269.000000,2),math.log(260.000000,2),math.log(249.000000,2),math.log(267.875000,2),math.log(277.750000,2),math.log(263.468750,2),math.log(280.890625,2),math.log(267.695312,2),math.log(285.085938,2),math.log(324.865234,2),math.log(327.794922,2),math.log(403.444824,2),math.log(429.395264,2),math.log(595.735229,2),math.log(852.716125,2),math.log(1404.367096,2)]
t_104 = [math.log(272.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(264.000000,2),math.log(243.000000,2),math.log(229.000000,2),math.log(263.750000,2),math.log(261.250000,2),math.log(272.437500,2),math.log(258.437500,2),math.log(242.546875,2),math.log(258.328125,2),math.log(275.511719,2),math.log(282.919922,2),math.log(297.192383,2),math.log(326.189453,2),math.log(306.201904,2),math.log(347.308472,2),math.log(447.218140,2),math.log(668.848877,2)]
t_105 = [math.log(288.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(266.000000,2),math.log(242.000000,2),math.log(223.500000,2),math.log(229.375000,2),math.log(263.937500,2),math.log(259.218750,2),math.log(307.468750,2),math.log(296.351562,2),math.log(268.847656,2),math.log(282.906250,2),math.log(238.116211,2),math.log(277.314941,2),math.log(289.207275,2),math.log(344.623291,2),math.log(426.194275,2),math.log(563.081085,2)]
t_106 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(258.000000,2),math.log(235.000000,2),math.log(240.000000,2),math.log(259.000000,2),math.log(259.875000,2),math.log(262.250000,2),math.log(287.406250,2),math.log(267.343750,2),math.log(235.093750,2),math.log(249.714844,2),math.log(298.197266,2),math.log(283.234375,2),math.log(316.918945,2),math.log(377.539551,2),math.log(516.047119,2),math.log(821.339783,2),math.log(1194.266388,2)]
t_107 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(214.000000,2),math.log(236.000000,2),math.log(213.000000,2),math.log(221.000000,2),math.log(236.875000,2),math.log(236.437500,2),math.log(222.125000,2),math.log(226.921875,2),math.log(245.750000,2),math.log(236.433594,2),math.log(229.412109,2),math.log(248.482422,2),math.log(293.641113,2),math.log(411.759277,2),math.log(620.325562,2),math.log(1018.827148,2),math.log(1773.492615,2)]
t_108 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(242.000000,2),math.log(262.000000,2),math.log(275.000000,2),math.log(237.125000,2),math.log(243.625000,2),math.log(229.250000,2),math.log(245.265625,2),math.log(261.226562,2),math.log(283.488281,2),math.log(285.949219,2),math.log(308.760742,2),math.log(292.038086,2),math.log(273.573730,2),math.log(327.561279,2),math.log(398.210754,2),math.log(585.500031,2)]
t_109 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(262.000000,2),math.log(260.000000,2),math.log(282.500000,2),math.log(267.250000,2),math.log(268.625000,2),math.log(260.250000,2),math.log(247.125000,2),math.log(252.203125,2),math.log(248.328125,2),math.log(259.257812,2),math.log(258.572266,2),math.log(269.681641,2),math.log(316.430664,2),math.log(351.837891,2),math.log(502.681885,2),math.log(610.207825,2),math.log(995.281525,2)]
t_110 = [math.log(256.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(240.000000,2),math.log(277.000000,2),math.log(206.500000,2),math.log(220.125000,2),math.log(231.250000,2),math.log(228.625000,2),math.log(240.062500,2),math.log(237.585938,2),math.log(238.945312,2),math.log(255.794922,2),math.log(289.496094,2),math.log(289.993164,2),math.log(315.753906,2),math.log(475.688354,2),math.log(699.548218,2),math.log(976.971558,2)]
t_111 = [math.log(256.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(208.000000,2),math.log(231.000000,2),math.log(231.500000,2),math.log(232.500000,2),math.log(221.375000,2),math.log(209.375000,2),math.log(251.531250,2),math.log(267.203125,2),math.log(256.617188,2),math.log(237.164062,2),math.log(284.283203,2),math.log(271.504883,2),math.log(264.419922,2),math.log(321.212891,2),math.log(414.738281,2),math.log(425.905396,2),math.log(615.504944,2)]
t_112 = [math.log(256.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(226.000000,2),math.log(252.000000,2),math.log(251.000000,2),math.log(269.500000,2),math.log(279.625000,2),math.log(253.312500,2),math.log(231.156250,2),math.log(266.718750,2),math.log(292.851562,2),math.log(289.046875,2),math.log(273.816406,2),math.log(252.622070,2),math.log(263.716309,2),math.log(279.416016,2),math.log(330.362671,2),math.log(377.280884,2),math.log(449.121460,2)]
t_113 = [math.log(256.000000,2),math.log(280.000000,2),math.log(320.000000,2),math.log(286.000000,2),math.log(262.000000,2),math.log(260.500000,2),math.log(215.500000,2),math.log(210.500000,2),math.log(250.062500,2),math.log(221.843750,2),math.log(226.500000,2),math.log(231.148438,2),math.log(216.687500,2),math.log(228.640625,2),math.log(258.303711,2),math.log(247.046387,2),math.log(292.809814,2),math.log(357.867920,2),math.log(456.180298,2),math.log(608.644775,2)]
t_114 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(295.000000,2),math.log(274.500000,2),math.log(259.750000,2),math.log(239.375000,2),math.log(253.125000,2),math.log(256.437500,2),math.log(248.203125,2),math.log(248.523438,2),math.log(261.921875,2),math.log(291.214844,2),math.log(270.779297,2),math.log(275.689453,2),math.log(309.239990,2),math.log(339.156860,2),math.log(400.983948,2),math.log(562.712555,2)]
t_115 = [math.log(256.000000,2),math.log(232.000000,2),math.log(216.000000,2),math.log(230.000000,2),math.log(235.000000,2),math.log(251.500000,2),math.log(268.750000,2),math.log(249.250000,2),math.log(264.312500,2),math.log(272.781250,2),math.log(287.015625,2),math.log(245.195312,2),math.log(240.949219,2),math.log(235.189453,2),math.log(262.142578,2),math.log(293.006836,2),math.log(333.842773,2),math.log(436.322632,2),math.log(641.080994,2),math.log(1015.919861,2)]
t_116 = [math.log(272.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(223.000000,2),math.log(248.500000,2),math.log(223.250000,2),math.log(249.500000,2),math.log(249.375000,2),math.log(268.968750,2),math.log(233.515625,2),math.log(277.656250,2),math.log(262.730469,2),math.log(291.687500,2),math.log(324.416992,2),math.log(293.120117,2),math.log(348.562744,2),math.log(359.245239,2),math.log(392.203796,2),math.log(570.055664,2)]
t_117 = [math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(266.000000,2),math.log(228.000000,2),math.log(225.000000,2),math.log(226.875000,2),math.log(206.812500,2),math.log(239.000000,2),math.log(237.750000,2),math.log(215.851562,2),math.log(224.308594,2),math.log(273.216797,2),math.log(252.542969,2),math.log(279.907715,2),math.log(284.355713,2),math.log(324.058960,2),math.log(454.954163,2),math.log(665.703186,2)]
t_118 = [math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(271.000000,2),math.log(250.500000,2),math.log(196.750000,2),math.log(186.375000,2),math.log(216.437500,2),math.log(196.187500,2),math.log(214.500000,2),math.log(241.867188,2),math.log(248.898438,2),math.log(231.849609,2),math.log(297.522461,2),math.log(341.417480,2),math.log(383.332520,2),math.log(451.864868,2),math.log(577.191223,2),math.log(853.944458,2)]
t_119 = [math.log(240.000000,2),math.log(224.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(237.000000,2),math.log(227.000000,2),math.log(236.250000,2),math.log(223.125000,2),math.log(261.187500,2),math.log(295.406250,2),math.log(305.781250,2),math.log(309.062500,2),math.log(302.277344,2),math.log(306.078125,2),math.log(316.800781,2),math.log(329.931152,2),math.log(370.190918,2),math.log(524.109253,2),math.log(708.017395,2),math.log(1112.274445,2)]
t_120 = [math.log(256.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(243.000000,2),math.log(225.500000,2),math.log(251.750000,2),math.log(230.500000,2),math.log(236.500000,2),math.log(243.218750,2),math.log(274.953125,2),math.log(226.078125,2),math.log(234.437500,2),math.log(249.564453,2),math.log(283.046875,2),math.log(307.708008,2),math.log(325.902588,2),math.log(351.184692,2),math.log(369.386597,2),math.log(540.011383,2)]
t_121 = [math.log(240.000000,2),math.log(224.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(252.500000,2),math.log(249.250000,2),math.log(236.500000,2),math.log(200.250000,2),math.log(241.625000,2),math.log(216.546875,2),math.log(234.195312,2),math.log(271.058594,2),math.log(264.335938,2),math.log(307.072266,2),math.log(328.568848,2),math.log(370.118164,2),math.log(412.889404,2),math.log(586.059631,2),math.log(851.624146,2)]
t_122 = [math.log(272.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(233.000000,2),math.log(254.000000,2),math.log(252.250000,2),math.log(255.500000,2),math.log(244.000000,2),math.log(223.250000,2),math.log(259.890625,2),math.log(260.015625,2),math.log(275.054688,2),math.log(303.916016,2),math.log(307.247070,2),math.log(294.345215,2),math.log(377.757568,2),math.log(559.554688,2),math.log(856.238403,2),math.log(1403.872620,2)]
t_123 = [math.log(224.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(278.000000,2),math.log(292.000000,2),math.log(302.500000,2),math.log(305.875000,2),math.log(286.750000,2),math.log(279.312500,2),math.log(271.750000,2),math.log(218.820312,2),math.log(251.925781,2),math.log(286.574219,2),math.log(332.977539,2),math.log(376.180664,2),math.log(507.886719,2),math.log(671.213867,2),math.log(1038.618469,2),math.log(1803.067780,2)]
t_124 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(282.000000,2),math.log(229.000000,2),math.log(252.500000,2),math.log(270.500000,2),math.log(284.125000,2),math.log(252.062500,2),math.log(237.968750,2),math.log(267.765625,2),math.log(280.804688,2),math.log(286.335938,2),math.log(310.361328,2),math.log(295.352539,2),math.log(320.822754,2),math.log(396.508301,2),math.log(455.901611,2),math.log(592.303650,2),math.log(914.934326,2)]
t_125 = [math.log(224.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(278.000000,2),math.log(280.000000,2),math.log(271.500000,2),math.log(237.500000,2),math.log(225.375000,2),math.log(212.125000,2),math.log(247.406250,2),math.log(258.812500,2),math.log(254.843750,2),math.log(253.476562,2),math.log(251.218750,2),math.log(245.262695,2),math.log(311.973145,2),math.log(359.089111,2),math.log(461.478882,2),math.log(712.185181,2),math.log(1216.477448,2)]
t_126 = [math.log(288.000000,2),math.log(296.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(277.000000,2),math.log(250.000000,2),math.log(216.750000,2),math.log(231.875000,2),math.log(227.437500,2),math.log(225.937500,2),math.log(249.781250,2),math.log(250.414062,2),math.log(269.796875,2),math.log(263.593750,2),math.log(239.444336,2),math.log(335.181641,2),math.log(384.339355,2),math.log(503.563843,2),math.log(734.968140,2),math.log(1148.928802,2)]
t_127 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(222.000000,2),math.log(218.000000,2),math.log(230.000000,2),math.log(210.500000,2),math.log(190.125000,2),math.log(226.687500,2),math.log(214.812500,2),math.log(271.968750,2),math.log(258.265625,2),math.log(292.488281,2),math.log(263.050781,2),math.log(281.499023,2),math.log(263.868652,2),math.log(336.531006,2),math.log(400.462769,2),math.log(652.342346,2),math.log(965.402313,2)]
t_128 = [math.log(288.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(300.000000,2),math.log(311.000000,2),math.log(247.500000,2),math.log(230.750000,2),math.log(234.875000,2),math.log(240.687500,2),math.log(297.937500,2),math.log(267.421875,2),math.log(260.000000,2),math.log(242.746094,2),math.log(288.791016,2),math.log(260.415039,2),math.log(288.728516,2),math.log(301.011475,2),math.log(272.044189,2),math.log(301.465027,2),math.log(333.458832,2)]
t_129 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(280.000000,2),math.log(262.000000,2),math.log(282.500000,2),math.log(280.250000,2),math.log(290.250000,2),math.log(290.937500,2),math.log(294.906250,2),math.log(284.640625,2),math.log(280.742188,2),math.log(248.105469,2),math.log(258.798828,2),math.log(281.672852,2),math.log(249.687012,2),math.log(266.422363,2),math.log(271.842529,2),math.log(337.544434,2),math.log(452.864014,2)]
t_130 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(243.000000,2),math.log(229.000000,2),math.log(215.750000,2),math.log(252.000000,2),math.log(261.250000,2),math.log(243.312500,2),math.log(239.921875,2),math.log(250.718750,2),math.log(272.984375,2),math.log(279.603516,2),math.log(218.047852,2),math.log(239.627441,2),math.log(269.210449,2),math.log(292.540894,2),math.log(318.534241,2),math.log(391.881653,2)]
t_131 = [math.log(272.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(264.750000,2),math.log(272.125000,2),math.log(288.375000,2),math.log(308.000000,2),math.log(274.656250,2),math.log(278.742188,2),math.log(297.402344,2),math.log(269.951172,2),math.log(278.784180,2),math.log(289.209473,2),math.log(306.916748,2),math.log(383.867554,2),math.log(435.114319,2),math.log(650.827759,2)]
t_132 = [math.log(304.000000,2),math.log(312.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(283.000000,2),math.log(292.500000,2),math.log(298.000000,2),math.log(295.125000,2),math.log(257.062500,2),math.log(245.781250,2),math.log(247.687500,2),math.log(266.765625,2),math.log(268.246094,2),math.log(260.093750,2),math.log(246.905273,2),math.log(243.645020,2),math.log(281.149414,2),math.log(239.404907,2),math.log(285.091553,2),math.log(372.286835,2)]
t_133 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(298.000000,2),math.log(317.500000,2),math.log(276.250000,2),math.log(260.250000,2),math.log(248.562500,2),math.log(253.937500,2),math.log(287.671875,2),math.log(274.195312,2),math.log(274.785156,2),math.log(265.335938,2),math.log(237.422852,2),math.log(288.020508,2),math.log(289.810303,2),math.log(296.012573,2),math.log(314.939819,2),math.log(420.187958,2)]
t_134 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(267.000000,2),math.log(273.500000,2),math.log(251.500000,2),math.log(219.000000,2),math.log(235.250000,2),math.log(267.031250,2),math.log(262.468750,2),math.log(273.757812,2),math.log(253.976562,2),math.log(272.996094,2),math.log(242.863281,2),math.log(273.837402,2),math.log(305.027832,2),math.log(404.082153,2),math.log(445.841675,2),math.log(654.209656,2)]
t_135 = [math.log(240.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(226.000000,2),math.log(211.000000,2),math.log(215.000000,2),math.log(208.750000,2),math.log(215.250000,2),math.log(261.500000,2),math.log(277.812500,2),math.log(262.750000,2),math.log(274.429688,2),math.log(254.667969,2),math.log(284.941406,2),math.log(262.018555,2),math.log(288.887695,2),math.log(352.506592,2),math.log(437.677368,2),math.log(658.671021,2),math.log(975.406067,2)]
t_136 = [math.log(224.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(260.000000,2),math.log(269.000000,2),math.log(276.000000,2),math.log(280.125000,2),math.log(250.250000,2),math.log(264.125000,2),math.log(214.953125,2),math.log(221.625000,2),math.log(241.445312,2),math.log(222.812500,2),math.log(258.214844,2),math.log(262.968262,2),math.log(285.131348,2),math.log(307.763428,2),math.log(378.209045,2),math.log(590.777710,2)]
t_137 = [math.log(240.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(244.000000,2),math.log(249.000000,2),math.log(269.500000,2),math.log(258.000000,2),math.log(281.375000,2),math.log(276.062500,2),math.log(237.937500,2),math.log(281.671875,2),math.log(250.171875,2),math.log(218.070312,2),math.log(245.423828,2),math.log(266.522461,2),math.log(282.844727,2),math.log(294.121094,2),math.log(299.560547,2),math.log(382.769043,2),math.log(568.783905,2)]
t_138 = [math.log(240.000000,2),math.log(248.000000,2),math.log(300.000000,2),math.log(246.000000,2),math.log(269.000000,2),math.log(279.500000,2),math.log(292.250000,2),math.log(246.750000,2),math.log(268.125000,2),math.log(241.468750,2),math.log(249.312500,2),math.log(257.492188,2),math.log(231.175781,2),math.log(269.949219,2),math.log(272.279297,2),math.log(296.743652,2),math.log(370.273926,2),math.log(445.313599,2),math.log(686.486206,2),math.log(1061.454498,2)]
t_139 = [math.log(240.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(233.000000,2),math.log(227.000000,2),math.log(221.250000,2),math.log(242.250000,2),math.log(270.500000,2),math.log(268.468750,2),math.log(258.671875,2),math.log(251.046875,2),math.log(255.011719,2),math.log(277.458984,2),math.log(306.907227,2),math.log(332.382324,2),math.log(376.017578,2),math.log(515.207153,2),math.log(830.098755,2),math.log(1513.313354,2)]
t_140 = [math.log(256.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(249.000000,2),math.log(251.000000,2),math.log(230.750000,2),math.log(269.000000,2),math.log(263.187500,2),math.log(316.843750,2),math.log(323.562500,2),math.log(284.640625,2),math.log(282.996094,2),math.log(275.289062,2),math.log(265.718750,2),math.log(291.648438,2),math.log(268.264404,2),math.log(308.289917,2),math.log(336.165100,2),math.log(416.882690,2)]
t_141 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(219.000000,2),math.log(232.000000,2),math.log(260.250000,2),math.log(281.125000,2),math.log(242.937500,2),math.log(260.656250,2),math.log(265.656250,2),math.log(246.765625,2),math.log(259.835938,2),math.log(269.488281,2),math.log(241.816406,2),math.log(282.205078,2),math.log(314.574219,2),math.log(371.252075,2),math.log(456.627502,2),math.log(635.931213,2)]
t_142 = [math.log(240.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(248.000000,2),math.log(262.500000,2),math.log(248.000000,2),math.log(249.875000,2),math.log(274.437500,2),math.log(226.468750,2),math.log(223.906250,2),math.log(239.781250,2),math.log(273.730469,2),math.log(249.156250,2),math.log(228.997070,2),math.log(259.393066,2),math.log(242.186279,2),math.log(265.490356,2),math.log(380.806885,2),math.log(569.448517,2)]
t_143 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(248.000000,2),math.log(273.000000,2),math.log(260.500000,2),math.log(288.500000,2),math.log(228.875000,2),math.log(234.250000,2),math.log(228.265625,2),math.log(251.351562,2),math.log(240.734375,2),math.log(246.716797,2),math.log(283.608398,2),math.log(301.729004,2),math.log(330.640381,2),math.log(368.516357,2),math.log(485.975586,2),math.log(621.920502,2)]
t_144 = [math.log(256.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(248.000000,2),math.log(265.000000,2),math.log(257.500000,2),math.log(256.250000,2),math.log(241.000000,2),math.log(243.687500,2),math.log(258.687500,2),math.log(281.484375,2),math.log(257.421875,2),math.log(258.289062,2),math.log(274.916016,2),math.log(262.631836,2),math.log(270.024902,2),math.log(324.398926,2),math.log(383.751831,2),math.log(495.870300,2),math.log(722.074127,2)]
t_145 = [math.log(320.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(240.000000,2),math.log(235.000000,2),math.log(266.500000,2),math.log(275.750000,2),math.log(283.125000,2),math.log(262.937500,2),math.log(243.406250,2),math.log(279.750000,2),math.log(319.593750,2),math.log(269.578125,2),math.log(289.439453,2),math.log(276.912109,2),math.log(287.944336,2),math.log(339.203613,2),math.log(368.219849,2),math.log(432.533386,2),math.log(561.665192,2)]
t_146 = [math.log(256.000000,2),math.log(216.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(257.000000,2),math.log(246.000000,2),math.log(270.750000,2),math.log(247.875000,2),math.log(268.812500,2),math.log(273.750000,2),math.log(257.250000,2),math.log(255.679688,2),math.log(268.761719,2),math.log(259.824219,2),math.log(281.451172,2),math.log(303.003906,2),math.log(349.564697,2),math.log(438.304688,2),math.log(586.817383,2),math.log(813.837036,2)]
t_147 = [math.log(272.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(314.000000,2),math.log(287.000000,2),math.log(271.000000,2),math.log(263.500000,2),math.log(264.000000,2),math.log(265.375000,2),math.log(276.312500,2),math.log(289.796875,2),math.log(290.390625,2),math.log(270.472656,2),math.log(309.365234,2),math.log(293.060547,2),math.log(302.964844,2),math.log(355.265869,2),math.log(446.664917,2),math.log(636.152771,2),math.log(1030.193390,2)]
t_148 = [math.log(240.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(237.000000,2),math.log(253.500000,2),math.log(251.500000,2),math.log(279.375000,2),math.log(271.375000,2),math.log(258.531250,2),math.log(261.656250,2),math.log(233.164062,2),math.log(222.234375,2),math.log(256.511719,2),math.log(281.850586,2),math.log(323.806152,2),math.log(333.579346,2),math.log(301.876831,2),math.log(419.430420,2),math.log(586.040314,2)]
t_149 = [math.log(240.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(227.000000,2),math.log(240.000000,2),math.log(264.500000,2),math.log(271.750000,2),math.log(248.250000,2),math.log(258.750000,2),math.log(256.031250,2),math.log(242.718750,2),math.log(256.601562,2),math.log(272.679688,2),math.log(280.402344,2),math.log(296.356445,2),math.log(303.891602,2),math.log(326.245239,2),math.log(398.536133,2),math.log(496.273651,2)]
t_150 = [math.log(240.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(239.000000,2),math.log(229.500000,2),math.log(246.750000,2),math.log(238.000000,2),math.log(254.562500,2),math.log(225.406250,2),math.log(247.531250,2),math.log(278.000000,2),math.log(262.285156,2),math.log(251.125000,2),math.log(251.505859,2),math.log(281.296387,2),math.log(288.973633,2),math.log(346.280273,2),math.log(448.384827,2),math.log(588.189667,2)]
t_151 = [math.log(256.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(244.000000,2),math.log(275.000000,2),math.log(242.500000,2),math.log(236.500000,2),math.log(266.000000,2),math.log(256.500000,2),math.log(242.906250,2),math.log(241.281250,2),math.log(242.484375,2),math.log(243.636719,2),math.log(246.099609,2),math.log(234.019531,2),math.log(265.450195,2),math.log(367.759033,2),math.log(546.089478,2),math.log(814.020325,2),math.log(1278.295349,2)]
t_152 = [math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(231.000000,2),math.log(286.000000,2),math.log(267.250000,2),math.log(224.125000,2),math.log(258.312500,2),math.log(244.843750,2),math.log(217.375000,2),math.log(200.968750,2),math.log(239.800781,2),math.log(266.958984,2),math.log(259.012695,2),math.log(296.640625,2),math.log(366.591797,2),math.log(443.968018,2),math.log(634.546448,2),math.log(1002.230011,2)]
t_153 = [math.log(288.000000,2),math.log(304.000000,2),math.log(260.000000,2),math.log(228.000000,2),math.log(245.000000,2),math.log(242.000000,2),math.log(261.500000,2),math.log(279.000000,2),math.log(258.125000,2),math.log(271.750000,2),math.log(273.375000,2),math.log(233.546875,2),math.log(251.015625,2),math.log(233.919922,2),math.log(219.447266,2),math.log(275.270508,2),math.log(267.824463,2),math.log(337.504395,2),math.log(432.801208,2),math.log(673.821777,2)]
t_154 = [math.log(352.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(270.000000,2),math.log(263.000000,2),math.log(276.000000,2),math.log(262.000000,2),math.log(270.750000,2),math.log(258.812500,2),math.log(262.406250,2),math.log(254.875000,2),math.log(258.070312,2),math.log(255.664062,2),math.log(261.501953,2),math.log(287.788086,2),math.log(345.827148,2),math.log(433.533691,2),math.log(588.975220,2),math.log(926.261536,2),math.log(1420.400085,2)]
t_155 = [math.log(256.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(225.000000,2),math.log(253.500000,2),math.log(248.500000,2),math.log(243.125000,2),math.log(271.000000,2),math.log(299.468750,2),math.log(294.875000,2),math.log(273.867188,2),math.log(290.753906,2),math.log(290.744141,2),math.log(391.891602,2),math.log(404.396973,2),math.log(524.043701,2),math.log(787.087280,2),math.log(1297.823730,2),math.log(2334.251587,2)]
t_156 = [math.log(272.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(238.000000,2),math.log(242.000000,2),math.log(262.000000,2),math.log(271.125000,2),math.log(253.187500,2),math.log(230.406250,2),math.log(232.078125,2),math.log(214.234375,2),math.log(216.242188,2),math.log(242.966797,2),math.log(278.209961,2),math.log(316.033691,2),math.log(323.563965,2),math.log(433.120850,2),math.log(634.172485,2),math.log(958.064178,2)]
t_157 = [math.log(256.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(230.000000,2),math.log(239.000000,2),math.log(253.000000,2),math.log(260.250000,2),math.log(257.750000,2),math.log(301.812500,2),math.log(256.375000,2),math.log(273.375000,2),math.log(304.609375,2),math.log(280.921875,2),math.log(272.062500,2),math.log(282.362305,2),math.log(297.917480,2),math.log(341.738525,2),math.log(441.383545,2),math.log(671.739258,2),math.log(1110.694489,2)]
t_158 = [math.log(288.000000,2),math.log(280.000000,2),math.log(308.000000,2),math.log(342.000000,2),math.log(265.000000,2),math.log(233.500000,2),math.log(252.250000,2),math.log(267.000000,2),math.log(286.812500,2),math.log(281.250000,2),math.log(253.046875,2),math.log(259.039062,2),math.log(272.722656,2),math.log(292.212891,2),math.log(310.129883,2),math.log(337.513184,2),math.log(402.271240,2),math.log(524.166504,2),math.log(742.309937,2),math.log(1316.517212,2)]
t_159 = [math.log(288.000000,2),math.log(280.000000,2),math.log(240.000000,2),math.log(218.000000,2),math.log(234.000000,2),math.log(259.000000,2),math.log(258.250000,2),math.log(237.625000,2),math.log(191.187500,2),math.log(203.937500,2),math.log(231.421875,2),math.log(277.203125,2),math.log(279.960938,2),math.log(257.978516,2),math.log(230.581055,2),math.log(276.600098,2),math.log(384.329102,2),math.log(425.690674,2),math.log(556.287048,2),math.log(877.539154,2)]
t_160 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(220.000000,2),math.log(216.000000,2),math.log(239.500000,2),math.log(238.000000,2),math.log(267.000000,2),math.log(264.000000,2),math.log(307.968750,2),math.log(276.812500,2),math.log(262.500000,2),math.log(224.738281,2),math.log(234.869141,2),math.log(234.783203,2),math.log(269.322266,2),math.log(285.483643,2),math.log(397.721680,2),math.log(603.862549,2),math.log(868.965912,2)]
t_161 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(239.000000,2),math.log(255.000000,2),math.log(285.000000,2),math.log(263.500000,2),math.log(234.187500,2),math.log(226.687500,2),math.log(242.171875,2),math.log(265.203125,2),math.log(290.203125,2),math.log(295.839844,2),math.log(285.319336,2),math.log(360.660645,2),math.log(432.199951,2),math.log(502.866455,2),math.log(752.226868,2),math.log(1228.484100,2)]
t_162 = [math.log(240.000000,2),math.log(216.000000,2),math.log(208.000000,2),math.log(234.000000,2),math.log(254.000000,2),math.log(271.500000,2),math.log(254.000000,2),math.log(263.875000,2),math.log(246.125000,2),math.log(249.593750,2),math.log(265.843750,2),math.log(310.703125,2),math.log(289.785156,2),math.log(301.623047,2),math.log(237.769531,2),math.log(223.656738,2),math.log(271.337646,2),math.log(337.778687,2),math.log(467.402649,2),math.log(730.825806,2)]
t_163 = [math.log(240.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(278.000000,2),math.log(299.000000,2),math.log(299.000000,2),math.log(284.750000,2),math.log(262.750000,2),math.log(322.812500,2),math.log(300.343750,2),math.log(290.187500,2),math.log(244.937500,2),math.log(265.585938,2),math.log(227.044922,2),math.log(255.343750,2),math.log(291.704590,2),math.log(339.917969,2),math.log(476.005493,2),math.log(626.108398,2),math.log(1081.276245,2)]
t_164 = [math.log(240.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(244.000000,2),math.log(227.000000,2),math.log(252.500000,2),math.log(262.000000,2),math.log(239.875000,2),math.log(243.062500,2),math.log(261.468750,2),math.log(241.609375,2),math.log(229.820312,2),math.log(246.757812,2),math.log(240.173828,2),math.log(245.136719,2),math.log(267.187012,2),math.log(340.282471,2),math.log(397.058960,2),math.log(573.100220,2),math.log(942.529236,2)]
t_165 = [math.log(256.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(216.000000,2),math.log(282.000000,2),math.log(235.000000,2),math.log(225.500000,2),math.log(245.125000,2),math.log(238.750000,2),math.log(222.000000,2),math.log(259.546875,2),math.log(229.179688,2),math.log(255.347656,2),math.log(254.193359,2),math.log(275.997070,2),math.log(280.432617,2),math.log(305.538330,2),math.log(382.144287,2),math.log(553.682678,2),math.log(900.619080,2)]
t_166 = [math.log(288.000000,2),math.log(288.000000,2),math.log(240.000000,2),math.log(290.000000,2),math.log(215.000000,2),math.log(220.000000,2),math.log(237.750000,2),math.log(230.625000,2),math.log(218.687500,2),math.log(260.593750,2),math.log(286.171875,2),math.log(280.742188,2),math.log(220.511719,2),math.log(297.951172,2),math.log(284.807617,2),math.log(329.118164,2),math.log(300.649170,2),math.log(398.818848,2),math.log(734.654297,2),math.log(1210.739014,2)]
t_167 = [math.log(320.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(292.000000,2),math.log(269.000000,2),math.log(252.500000,2),math.log(252.000000,2),math.log(232.500000,2),math.log(239.062500,2),math.log(240.687500,2),math.log(218.390625,2),math.log(248.640625,2),math.log(254.875000,2),math.log(238.066406,2),math.log(261.329102,2),math.log(303.916504,2),math.log(380.034912,2),math.log(521.636230,2),math.log(784.839722,2),math.log(1324.754456,2)]
t_168 = [math.log(288.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(264.000000,2),math.log(266.000000,2),math.log(231.500000,2),math.log(242.250000,2),math.log(286.937500,2),math.log(297.593750,2),math.log(268.781250,2),math.log(229.421875,2),math.log(250.644531,2),math.log(250.562500,2),math.log(225.745117,2),math.log(241.125977,2),math.log(266.286621,2),math.log(369.404907,2),math.log(452.948669,2),math.log(714.128632,2)]
t_169 = [math.log(256.000000,2),math.log(272.000000,2),math.log(304.000000,2),math.log(274.000000,2),math.log(286.000000,2),math.log(265.500000,2),math.log(262.000000,2),math.log(275.750000,2),math.log(246.500000,2),math.log(235.468750,2),math.log(226.140625,2),math.log(236.937500,2),math.log(286.695312,2),math.log(281.998047,2),math.log(294.665039,2),math.log(332.759277,2),math.log(384.164551,2),math.log(542.553711,2),math.log(858.727844,2),math.log(1476.634033,2)]
t_170 = [math.log(240.000000,2),math.log(256.000000,2),math.log(312.000000,2),math.log(284.000000,2),math.log(285.000000,2),math.log(279.500000,2),math.log(255.500000,2),math.log(278.625000,2),math.log(253.000000,2),math.log(226.406250,2),math.log(231.984375,2),math.log(264.882812,2),math.log(242.234375,2),math.log(252.451172,2),math.log(253.725586,2),math.log(262.220215,2),math.log(331.003662,2),math.log(451.382080,2),math.log(615.432495,2),math.log(969.286102,2)]
t_171 = [math.log(272.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(259.000000,2),math.log(207.000000,2),math.log(219.750000,2),math.log(239.250000,2),math.log(280.937500,2),math.log(311.375000,2),math.log(304.687500,2),math.log(276.867188,2),math.log(245.636719,2),math.log(299.572266,2),math.log(323.555664,2),math.log(370.358887,2),math.log(432.402588,2),math.log(598.941650,2),math.log(875.022461,2),math.log(1489.538513,2)]
t_172 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(265.000000,2),math.log(272.500000,2),math.log(256.500000,2),math.log(254.875000,2),math.log(268.687500,2),math.log(249.468750,2),math.log(240.703125,2),math.log(235.562500,2),math.log(221.750000,2),math.log(272.003906,2),math.log(285.583984,2),math.log(348.215332,2),math.log(407.416504,2),math.log(546.597778,2),math.log(761.356934,2),math.log(1297.823578,2)]
t_173 = [math.log(320.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(267.000000,2),math.log(252.000000,2),math.log(246.500000,2),math.log(282.250000,2),math.log(265.250000,2),math.log(234.562500,2),math.log(232.046875,2),math.log(235.046875,2),math.log(231.621094,2),math.log(275.398438,2),math.log(290.287109,2),math.log(345.637207,2),math.log(492.390381,2),math.log(672.869263,2),math.log(1066.372742,2),math.log(1710.017181,2)]
t_174 = [math.log(224.000000,2),math.log(216.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(261.000000,2),math.log(282.000000,2),math.log(264.250000,2),math.log(227.375000,2),math.log(265.562500,2),math.log(267.593750,2),math.log(257.859375,2),math.log(235.085938,2),math.log(231.992188,2),math.log(302.341797,2),math.log(331.893555,2),math.log(355.447754,2),math.log(357.530029,2),math.log(441.294922,2),math.log(642.152954,2),math.log(1073.992798,2)]
t_175 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(258.000000,2),math.log(267.000000,2),math.log(257.500000,2),math.log(270.250000,2),math.log(241.000000,2),math.log(258.875000,2),math.log(294.093750,2),math.log(320.078125,2),math.log(270.203125,2),math.log(250.476562,2),math.log(282.871094,2),math.log(261.804688,2),math.log(285.163574,2),math.log(385.382568,2),math.log(443.526367,2),math.log(544.413330,2),math.log(881.918579,2)]
t_176 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(236.000000,2),math.log(243.000000,2),math.log(249.500000,2),math.log(270.500000,2),math.log(237.437500,2),math.log(249.718750,2),math.log(241.578125,2),math.log(231.632812,2),math.log(235.023438,2),math.log(279.263672,2),math.log(248.718750,2),math.log(285.278809,2),math.log(343.152100,2),math.log(396.071045,2),math.log(436.528870,2),math.log(605.797058,2)]
t_177 = [math.log(256.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(251.000000,2),math.log(277.500000,2),math.log(253.500000,2),math.log(228.500000,2),math.log(232.250000,2),math.log(261.531250,2),math.log(255.281250,2),math.log(233.093750,2),math.log(251.707031,2),math.log(306.964844,2),math.log(260.499023,2),math.log(287.632324,2),math.log(361.663818,2),math.log(475.171021,2),math.log(556.638855,2),math.log(790.691315,2)]
t_178 = [math.log(256.000000,2),math.log(288.000000,2),math.log(304.000000,2),math.log(298.000000,2),math.log(271.000000,2),math.log(283.000000,2),math.log(270.500000,2),math.log(258.500000,2),math.log(262.250000,2),math.log(246.187500,2),math.log(268.187500,2),math.log(244.609375,2),math.log(266.628906,2),math.log(261.455078,2),math.log(288.264648,2),math.log(326.475098,2),math.log(343.423340,2),math.log(328.203369,2),math.log(412.228516,2),math.log(575.155060,2)]
t_179 = [math.log(240.000000,2),math.log(288.000000,2),math.log(292.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(245.000000,2),math.log(268.250000,2),math.log(214.500000,2),math.log(240.750000,2),math.log(231.187500,2),math.log(283.843750,2),math.log(266.015625,2),math.log(305.738281,2),math.log(286.304688,2),math.log(307.646484,2),math.log(352.925781,2),math.log(353.537109,2),math.log(448.996338,2),math.log(635.489075,2),math.log(998.897308,2)]
t_180 = [math.log(240.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(244.000000,2),math.log(251.000000,2),math.log(254.000000,2),math.log(253.250000,2),math.log(229.750000,2),math.log(274.625000,2),math.log(272.250000,2),math.log(269.468750,2),math.log(282.625000,2),math.log(299.058594,2),math.log(235.185547,2),math.log(279.207031,2),math.log(293.086914,2),math.log(306.450439,2),math.log(305.088257,2),math.log(354.783203,2),math.log(535.487823,2)]
t_181 = [math.log(320.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(255.000000,2),math.log(234.500000,2),math.log(240.750000,2),math.log(256.375000,2),math.log(245.875000,2),math.log(250.500000,2),math.log(251.875000,2),math.log(225.757812,2),math.log(275.902344,2),math.log(289.867188,2),math.log(270.596680,2),math.log(275.522461,2),math.log(317.651123,2),math.log(348.484985,2),math.log(530.460266,2),math.log(826.001312,2)]
t_182 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(274.500000,2),math.log(258.250000,2),math.log(276.500000,2),math.log(265.750000,2),math.log(245.875000,2),math.log(212.265625,2),math.log(237.546875,2),math.log(254.753906,2),math.log(274.308594,2),math.log(291.721680,2),math.log(337.722168,2),math.log(356.188477,2),math.log(406.249268,2),math.log(580.800476,2),math.log(1007.791901,2)]
t_183 = [math.log(256.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(283.000000,2),math.log(231.500000,2),math.log(247.750000,2),math.log(266.875000,2),math.log(223.250000,2),math.log(239.781250,2),math.log(236.640625,2),math.log(249.187500,2),math.log(236.488281,2),math.log(250.509766,2),math.log(250.335938,2),math.log(294.857422,2),math.log(291.698975,2),math.log(392.332153,2),math.log(572.215088,2),math.log(922.720642,2)]
t_184 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(270.000000,2),math.log(265.500000,2),math.log(242.750000,2),math.log(242.750000,2),math.log(265.812500,2),math.log(259.468750,2),math.log(250.937500,2),math.log(253.664062,2),math.log(290.824219,2),math.log(282.082031,2),math.log(265.991211,2),math.log(297.113770,2),math.log(304.783936,2),math.log(317.395630,2),math.log(474.807251,2),math.log(671.426361,2)]
t_185 = [math.log(224.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(243.000000,2),math.log(242.000000,2),math.log(255.000000,2),math.log(259.375000,2),math.log(267.937500,2),math.log(288.875000,2),math.log(245.234375,2),math.log(219.335938,2),math.log(220.300781,2),math.log(234.312500,2),math.log(268.970703,2),math.log(312.185547,2),math.log(375.811035,2),math.log(521.582764,2),math.log(848.716980,2),math.log(1425.858154,2)]
t_186 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(199.000000,2),math.log(215.000000,2),math.log(229.250000,2),math.log(265.750000,2),math.log(248.937500,2),math.log(230.218750,2),math.log(229.937500,2),math.log(276.648438,2),math.log(254.292969,2),math.log(275.982422,2),math.log(328.289062,2),math.log(336.581543,2),math.log(404.029785,2),math.log(529.757935,2),math.log(777.775574,2),math.log(1276.364166,2)]
t_187 = [math.log(256.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(236.000000,2),math.log(226.000000,2),math.log(260.000000,2),math.log(229.750000,2),math.log(232.500000,2),math.log(273.312500,2),math.log(278.906250,2),math.log(294.171875,2),math.log(288.078125,2),math.log(257.414062,2),math.log(246.546875,2),math.log(297.292969,2),math.log(365.946289,2),math.log(448.743652,2),math.log(662.942749,2),math.log(1000.209045,2),math.log(1689.791809,2)]
t_188 = [math.log(224.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(262.250000,2),math.log(257.250000,2),math.log(248.437500,2),math.log(262.781250,2),math.log(294.968750,2),math.log(260.984375,2),math.log(258.730469,2),math.log(281.708984,2),math.log(290.797852,2),math.log(292.586426,2),math.log(333.623047,2),math.log(418.085938,2),math.log(672.139282,2),math.log(1074.135040,2)]
t_189 = [math.log(256.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(268.000000,2),math.log(247.500000,2),math.log(252.750000,2),math.log(250.375000,2),math.log(216.812500,2),math.log(236.250000,2),math.log(255.640625,2),math.log(287.507812,2),math.log(253.093750,2),math.log(285.296875,2),math.log(286.350586,2),math.log(300.868164,2),math.log(428.299805,2),math.log(557.571777,2),math.log(858.704895,2),math.log(1449.167267,2)]
t_190 = [math.log(224.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(235.000000,2),math.log(231.500000,2),math.log(229.250000,2),math.log(215.750000,2),math.log(218.312500,2),math.log(195.781250,2),math.log(237.593750,2),math.log(202.726562,2),math.log(273.730469,2),math.log(284.851562,2),math.log(275.487305,2),math.log(300.462402,2),math.log(411.962646,2),math.log(551.736938,2),math.log(823.838745,2),math.log(1369.149872,2)]
t_191 = [math.log(288.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(274.000000,2),math.log(257.000000,2),math.log(244.500000,2),math.log(262.000000,2),math.log(216.500000,2),math.log(261.375000,2),math.log(240.187500,2),math.log(271.906250,2),math.log(288.226562,2),math.log(308.898438,2),math.log(269.244141,2),math.log(280.902344,2),math.log(292.089355,2),math.log(324.156982,2),math.log(425.136475,2),math.log(661.857544,2),math.log(986.167480,2)]
t_192 = [math.log(240.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(227.000000,2),math.log(216.000000,2),math.log(209.750000,2),math.log(231.625000,2),math.log(259.500000,2),math.log(279.562500,2),math.log(294.015625,2),math.log(277.234375,2),math.log(284.167969,2),math.log(251.998047,2),math.log(271.032227,2),math.log(288.430664,2),math.log(310.934570,2),math.log(318.778320,2),math.log(387.232117,2),math.log(535.325195,2)]
t_193 = [math.log(256.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(288.000000,2),math.log(266.000000,2),math.log(249.500000,2),math.log(258.500000,2),math.log(286.750000,2),math.log(275.875000,2),math.log(243.718750,2),math.log(233.515625,2),math.log(238.179688,2),math.log(215.269531,2),math.log(225.091797,2),math.log(233.090820,2),math.log(281.691895,2),math.log(303.159912,2),math.log(331.222900,2),math.log(456.069397,2),math.log(666.209625,2)]
t_194 = [math.log(240.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(278.000000,2),math.log(282.000000,2),math.log(289.000000,2),math.log(296.250000,2),math.log(256.750000,2),math.log(244.562500,2),math.log(236.250000,2),math.log(242.296875,2),math.log(281.117188,2),math.log(279.488281,2),math.log(271.197266,2),math.log(267.966797,2),math.log(283.975586,2),math.log(336.608154,2),math.log(418.648804,2),math.log(434.548767,2),math.log(668.792236,2)]
t_195 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(222.000000,2),math.log(238.000000,2),math.log(239.500000,2),math.log(268.250000,2),math.log(234.500000,2),math.log(241.750000,2),math.log(253.281250,2),math.log(259.625000,2),math.log(246.257812,2),math.log(259.394531,2),math.log(256.322266,2),math.log(235.483398,2),math.log(271.517578,2),math.log(312.233154,2),math.log(418.831299,2),math.log(583.784790,2),math.log(853.260864,2)]
t_196 = [math.log(272.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(233.000000,2),math.log(267.000000,2),math.log(261.750000,2),math.log(265.875000,2),math.log(284.375000,2),math.log(252.093750,2),math.log(259.250000,2),math.log(231.398438,2),math.log(228.171875,2),math.log(263.320312,2),math.log(259.175781,2),math.log(275.533203,2),math.log(330.465576,2),math.log(376.547241,2),math.log(522.054321,2),math.log(761.309906,2)]
t_197 = [math.log(256.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(286.000000,2),math.log(275.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(249.750000,2),math.log(238.375000,2),math.log(213.000000,2),math.log(247.265625,2),math.log(210.210938,2),math.log(212.789062,2),math.log(284.294922,2),math.log(282.326172,2),math.log(287.668457,2),math.log(301.348633,2),math.log(298.816284,2),math.log(372.426086,2),math.log(482.128052,2)]
t_198 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(241.000000,2),math.log(253.500000,2),math.log(247.000000,2),math.log(239.750000,2),math.log(234.437500,2),math.log(254.656250,2),math.log(243.468750,2),math.log(243.156250,2),math.log(247.582031,2),math.log(275.306641,2),math.log(275.712891,2),math.log(264.439453,2),math.log(302.542480,2),math.log(324.778809,2),math.log(474.537170,2),math.log(799.990204,2)]
t_199 = [math.log(240.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(263.000000,2),math.log(237.000000,2),math.log(268.000000,2),math.log(265.750000,2),math.log(198.937500,2),math.log(262.406250,2),math.log(264.828125,2),math.log(224.421875,2),math.log(258.007812,2),math.log(246.824219,2),math.log(269.751953,2),math.log(336.661133,2),math.log(364.674316,2),math.log(466.708496,2),math.log(674.560486,2),math.log(1115.633362,2)]
t_200 = [math.log(224.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(277.000000,2),math.log(253.500000,2),math.log(257.000000,2),math.log(281.375000,2),math.log(306.000000,2),math.log(273.312500,2),math.log(282.515625,2),math.log(275.335938,2),math.log(251.332031,2),math.log(273.460938,2),math.log(230.848633,2),math.log(228.919434,2),math.log(295.772217,2),math.log(349.785278,2),math.log(442.529541,2),math.log(747.118896,2)]
t_201 = [math.log(240.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(234.000000,2),math.log(243.000000,2),math.log(241.000000,2),math.log(234.250000,2),math.log(208.875000,2),math.log(205.062500,2),math.log(229.218750,2),math.log(200.296875,2),math.log(256.718750,2),math.log(252.011719,2),math.log(287.332031,2),math.log(275.598633,2),math.log(250.724121,2),math.log(295.892090,2),math.log(371.738647,2),math.log(490.647400,2),math.log(686.773865,2)]
t_202 = [math.log(288.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(272.000000,2),math.log(270.500000,2),math.log(280.250000,2),math.log(256.125000,2),math.log(256.750000,2),math.log(263.281250,2),math.log(261.093750,2),math.log(236.203125,2),math.log(250.714844,2),math.log(241.152344,2),math.log(266.692383,2),math.log(337.788086,2),math.log(392.459717,2),math.log(506.213989,2),math.log(776.679749,2),math.log(1178.608643,2)]
t_203 = [math.log(256.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(238.000000,2),math.log(233.000000,2),math.log(240.000000,2),math.log(251.250000,2),math.log(247.500000,2),math.log(248.062500,2),math.log(232.875000,2),math.log(242.906250,2),math.log(292.156250,2),math.log(244.636719,2),math.log(245.289062,2),math.log(275.412109,2),math.log(330.660156,2),math.log(394.684082,2),math.log(564.714600,2),math.log(820.563232,2),math.log(1331.017578,2)]
t_204 = [math.log(256.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(256.000000,2),math.log(241.500000,2),math.log(251.000000,2),math.log(289.125000,2),math.log(322.250000,2),math.log(312.125000,2),math.log(287.390625,2),math.log(278.460938,2),math.log(275.453125,2),math.log(301.722656,2),math.log(272.428711,2),math.log(289.413086,2),math.log(299.458008,2),math.log(306.680542,2),math.log(336.583618,2),math.log(469.912903,2)]
t_205 = [math.log(272.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(255.000000,2),math.log(267.500000,2),math.log(288.750000,2),math.log(236.750000,2),math.log(229.812500,2),math.log(227.187500,2),math.log(229.828125,2),math.log(247.023438,2),math.log(245.875000,2),math.log(293.195312,2),math.log(292.737305,2),math.log(336.588379,2),math.log(363.188232,2),math.log(400.762451,2),math.log(607.851624,2),math.log(873.794159,2)]
t_206 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(225.000000,2),math.log(245.000000,2),math.log(251.500000,2),math.log(251.750000,2),math.log(247.687500,2),math.log(262.687500,2),math.log(253.203125,2),math.log(286.617188,2),math.log(265.429688,2),math.log(269.097656,2),math.log(261.954102,2),math.log(266.254395,2),math.log(312.552734,2),math.log(344.660767,2),math.log(380.329468,2),math.log(583.811859,2)]
t_207 = [math.log(256.000000,2),math.log(224.000000,2),math.log(260.000000,2),math.log(248.000000,2),math.log(274.000000,2),math.log(294.500000,2),math.log(282.250000,2),math.log(256.750000,2),math.log(222.250000,2),math.log(249.531250,2),math.log(251.500000,2),math.log(219.109375,2),math.log(216.425781,2),math.log(248.474609,2),math.log(239.357422,2),math.log(253.372559,2),math.log(310.067139,2),math.log(341.773926,2),math.log(422.178040,2),math.log(522.584717,2)]
t_208 = [math.log(256.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(237.000000,2),math.log(259.500000,2),math.log(264.000000,2),math.log(259.500000,2),math.log(252.250000,2),math.log(254.531250,2),math.log(240.031250,2),math.log(242.867188,2),math.log(240.238281,2),math.log(238.960938,2),math.log(259.912109,2),math.log(283.343750,2),math.log(260.175293,2),math.log(319.381836,2),math.log(461.496704,2),math.log(747.104736,2)]
t_209 = [math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(235.000000,2),math.log(208.500000,2),math.log(283.500000,2),math.log(249.250000,2),math.log(230.062500,2),math.log(240.531250,2),math.log(265.796875,2),math.log(270.375000,2),math.log(287.468750,2),math.log(273.261719,2),math.log(273.122070,2),math.log(292.635254,2),math.log(358.121582,2),math.log(415.399658,2),math.log(551.047058,2),math.log(796.128235,2)]
t_210 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(254.000000,2),math.log(234.000000,2),math.log(221.750000,2),math.log(206.125000,2),math.log(230.500000,2),math.log(239.343750,2),math.log(278.625000,2),math.log(306.281250,2),math.log(284.093750,2),math.log(243.587891,2),math.log(232.974609,2),math.log(260.920898,2),math.log(262.033447,2),math.log(259.478760,2),math.log(353.179626,2),math.log(588.348053,2)]
t_211 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(272.000000,2),math.log(259.000000,2),math.log(276.500000,2),math.log(246.750000,2),math.log(281.875000,2),math.log(223.000000,2),math.log(256.531250,2),math.log(244.359375,2),math.log(258.343750,2),math.log(233.035156,2),math.log(208.701172,2),math.log(229.127930,2),math.log(273.142578,2),math.log(314.852783,2),math.log(364.180542,2),math.log(463.861328,2),math.log(645.582489,2)]
t_212 = [math.log(240.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(231.000000,2),math.log(225.000000,2),math.log(187.500000,2),math.log(233.750000,2),math.log(224.500000,2),math.log(265.187500,2),math.log(245.500000,2),math.log(263.359375,2),math.log(308.437500,2),math.log(265.271484,2),math.log(251.181641,2),math.log(284.539062,2),math.log(341.164795,2),math.log(368.347534,2),math.log(429.258972,2),math.log(576.013550,2)]
t_213 = [math.log(304.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(304.000000,2),math.log(253.000000,2),math.log(254.000000,2),math.log(298.750000,2),math.log(239.125000,2),math.log(263.375000,2),math.log(240.968750,2),math.log(250.515625,2),math.log(237.914062,2),math.log(242.734375,2),math.log(297.488281,2),math.log(285.704102,2),math.log(253.803223,2),math.log(300.858643,2),math.log(329.315063,2),math.log(419.075745,2),math.log(573.549988,2)]
t_214 = [math.log(288.000000,2),math.log(312.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(290.000000,2),math.log(286.000000,2),math.log(254.750000,2),math.log(271.500000,2),math.log(278.312500,2),math.log(265.562500,2),math.log(230.609375,2),math.log(236.914062,2),math.log(247.804688,2),math.log(217.121094,2),math.log(283.749023,2),math.log(316.988281,2),math.log(335.722168,2),math.log(399.563110,2),math.log(483.716980,2),math.log(736.898071,2)]
t_215 = [math.log(224.000000,2),math.log(256.000000,2),math.log(304.000000,2),math.log(280.000000,2),math.log(267.000000,2),math.log(261.000000,2),math.log(264.500000,2),math.log(250.875000,2),math.log(252.562500,2),math.log(293.312500,2),math.log(239.109375,2),math.log(230.171875,2),math.log(258.929688,2),math.log(251.486328,2),math.log(253.758789,2),math.log(300.028809,2),math.log(312.034424,2),math.log(360.892090,2),math.log(412.413879,2),math.log(612.968781,2)]
t_216 = [math.log(256.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(264.000000,2),math.log(257.000000,2),math.log(234.250000,2),math.log(225.250000,2),math.log(213.250000,2),math.log(257.281250,2),math.log(207.390625,2),math.log(254.078125,2),math.log(289.382812,2),math.log(270.425781,2),math.log(258.399414,2),math.log(248.572754,2),math.log(259.185303,2),math.log(363.167603,2),math.log(476.505493,2),math.log(616.061859,2)]
t_217 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(246.000000,2),math.log(237.500000,2),math.log(253.500000,2),math.log(295.875000,2),math.log(264.625000,2),math.log(281.875000,2),math.log(276.093750,2),math.log(325.109375,2),math.log(288.191406,2),math.log(295.923828,2),math.log(274.782227,2),math.log(304.971191,2),math.log(325.554199,2),math.log(428.399292,2),math.log(618.106689,2),math.log(1105.525513,2)]
t_218 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(239.500000,2),math.log(233.125000,2),math.log(238.562500,2),math.log(265.812500,2),math.log(295.375000,2),math.log(298.023438,2),math.log(231.316406,2),math.log(269.060547,2),math.log(318.076172,2),math.log(319.425293,2),math.log(363.731934,2),math.log(430.131348,2),math.log(628.002441,2),math.log(1082.563049,2)]
t_219 = [math.log(240.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(217.000000,2),math.log(242.500000,2),math.log(214.500000,2),math.log(222.125000,2),math.log(266.000000,2),math.log(266.218750,2),math.log(279.171875,2),math.log(269.007812,2),math.log(265.847656,2),math.log(271.632812,2),math.log(280.263672,2),math.log(310.370605,2),math.log(355.610840,2),math.log(467.856445,2),math.log(672.669983,2),math.log(935.788055,2)]
t_220 = [math.log(256.000000,2),math.log(296.000000,2),math.log(268.000000,2),math.log(236.000000,2),math.log(249.000000,2),math.log(252.500000,2),math.log(251.000000,2),math.log(268.750000,2),math.log(273.437500,2),math.log(228.031250,2),math.log(227.187500,2),math.log(248.070312,2),math.log(240.792969,2),math.log(268.468750,2),math.log(244.839844,2),math.log(278.932129,2),math.log(362.686279,2),math.log(450.894897,2),math.log(589.630859,2),math.log(965.179626,2)]
t_221 = [math.log(256.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(254.000000,2),math.log(270.000000,2),math.log(273.000000,2),math.log(263.750000,2),math.log(265.437500,2),math.log(264.812500,2),math.log(260.140625,2),math.log(302.046875,2),math.log(292.058594,2),math.log(248.136719,2),math.log(258.410156,2),math.log(246.520020,2),math.log(299.467773,2),math.log(353.391846,2),math.log(553.585388,2),math.log(880.313904,2)]
t_222 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(254.000000,2),math.log(280.000000,2),math.log(259.000000,2),math.log(240.500000,2),math.log(255.625000,2),math.log(275.062500,2),math.log(258.687500,2),math.log(229.781250,2),math.log(241.054688,2),math.log(259.828125,2),math.log(282.861328,2),math.log(293.910156,2),math.log(275.079102,2),math.log(271.796875,2),math.log(347.615234,2),math.log(427.727966,2),math.log(691.255981,2)]
t_223 = [math.log(240.000000,2),math.log(216.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(242.000000,2),math.log(263.000000,2),math.log(286.250000,2),math.log(260.000000,2),math.log(268.562500,2),math.log(241.468750,2),math.log(222.562500,2),math.log(231.375000,2),math.log(252.035156,2),math.log(256.675781,2),math.log(294.358398,2),math.log(318.556152,2),math.log(367.799561,2),math.log(447.423462,2),math.log(623.656433,2),math.log(982.630219,2)]
t_224 = [math.log(224.000000,2),math.log(304.000000,2),math.log(236.000000,2),math.log(272.000000,2),math.log(279.000000,2),math.log(290.000000,2),math.log(264.500000,2),math.log(308.250000,2),math.log(301.250000,2),math.log(287.718750,2),math.log(258.656250,2),math.log(270.625000,2),math.log(278.160156,2),math.log(272.324219,2),math.log(291.447266,2),math.log(310.034668,2),math.log(361.535889,2),math.log(392.963013,2),math.log(480.909546,2),math.log(619.602783,2)]
t_225 = [math.log(304.000000,2),math.log(312.000000,2),math.log(288.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(271.500000,2),math.log(269.000000,2),math.log(248.375000,2),math.log(231.500000,2),math.log(229.250000,2),math.log(218.968750,2),math.log(269.148438,2),math.log(268.519531,2),math.log(226.662109,2),math.log(243.637695,2),math.log(254.184570,2),math.log(298.578369,2),math.log(339.053345,2),math.log(571.477478,2),math.log(907.787567,2)]
t_226 = [math.log(336.000000,2),math.log(296.000000,2),math.log(284.000000,2),math.log(254.000000,2),math.log(272.000000,2),math.log(266.500000,2),math.log(259.000000,2),math.log(255.875000,2),math.log(230.250000,2),math.log(251.125000,2),math.log(244.500000,2),math.log(242.867188,2),math.log(214.601562,2),math.log(241.123047,2),math.log(227.991211,2),math.log(276.168457,2),math.log(277.116211,2),math.log(320.586304,2),math.log(390.128906,2),math.log(480.542175,2)]
t_227 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(242.000000,2),math.log(257.500000,2),math.log(253.125000,2),math.log(242.187500,2),math.log(230.656250,2),math.log(270.593750,2),math.log(285.359375,2),math.log(281.164062,2),math.log(274.195312,2),math.log(296.004883,2),math.log(309.618652,2),math.log(366.917969,2),math.log(534.556885,2),math.log(752.492798,2),math.log(1251.815552,2)]
t_228 = [math.log(240.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(238.000000,2),math.log(246.500000,2),math.log(274.000000,2),math.log(242.125000,2),math.log(220.687500,2),math.log(234.968750,2),math.log(269.562500,2),math.log(269.078125,2),math.log(254.464844,2),math.log(271.765625,2),math.log(302.451172,2),math.log(285.827637,2),math.log(294.205566,2),math.log(373.337769,2),math.log(389.057495,2),math.log(679.097870,2)]
t_229 = [math.log(288.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(257.000000,2),math.log(252.000000,2),math.log(246.750000,2),math.log(238.625000,2),math.log(261.437500,2),math.log(272.625000,2),math.log(280.000000,2),math.log(263.898438,2),math.log(241.136719,2),math.log(207.382812,2),math.log(201.966797,2),math.log(227.251465,2),math.log(290.944336,2),math.log(369.691406,2),math.log(431.501648,2),math.log(579.576019,2)]
t_230 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(253.000000,2),math.log(245.000000,2),math.log(239.750000,2),math.log(255.875000,2),math.log(209.500000,2),math.log(224.500000,2),math.log(232.640625,2),math.log(211.343750,2),math.log(229.378906,2),math.log(255.535156,2),math.log(254.325195,2),math.log(313.608887,2),math.log(356.897217,2),math.log(437.421387,2),math.log(669.636658,2),math.log(1023.039337,2)]
t_231 = [math.log(272.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(278.000000,2),math.log(243.000000,2),math.log(275.500000,2),math.log(283.750000,2),math.log(278.375000,2),math.log(291.000000,2),math.log(277.406250,2),math.log(264.843750,2),math.log(268.906250,2),math.log(257.414062,2),math.log(271.746094,2),math.log(255.531250,2),math.log(289.500488,2),math.log(369.096680,2),math.log(494.031982,2),math.log(803.621643,2),math.log(1398.061218,2)]
t_232 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(282.000000,2),math.log(269.000000,2),math.log(251.500000,2),math.log(243.250000,2),math.log(259.125000,2),math.log(256.875000,2),math.log(269.000000,2),math.log(243.265625,2),math.log(259.859375,2),math.log(240.613281,2),math.log(220.626953,2),math.log(256.687500,2),math.log(250.617676,2),math.log(276.668457,2),math.log(340.963257,2),math.log(379.549438,2),math.log(512.110291,2)]
t_233 = [math.log(272.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(243.000000,2),math.log(259.500000,2),math.log(230.750000,2),math.log(238.750000,2),math.log(264.562500,2),math.log(238.531250,2),math.log(262.687500,2),math.log(266.718750,2),math.log(241.882812,2),math.log(230.070312,2),math.log(284.247070,2),math.log(347.970703,2),math.log(381.088379,2),math.log(452.645630,2),math.log(660.544312,2),math.log(1043.915649,2)]
t_234 = [math.log(320.000000,2),math.log(288.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(239.000000,2),math.log(271.000000,2),math.log(263.000000,2),math.log(243.500000,2),math.log(237.000000,2),math.log(266.500000,2),math.log(244.234375,2),math.log(244.179688,2),math.log(262.582031,2),math.log(249.974609,2),math.log(244.576172,2),math.log(282.028320,2),math.log(303.719482,2),math.log(380.520874,2),math.log(487.043518,2),math.log(774.144775,2)]
t_235 = [math.log(240.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(267.000000,2),math.log(223.500000,2),math.log(250.750000,2),math.log(238.125000,2),math.log(225.062500,2),math.log(253.312500,2),math.log(226.375000,2),math.log(284.671875,2),math.log(316.656250,2),math.log(285.603516,2),math.log(293.013672,2),math.log(326.344238,2),math.log(449.069580,2),math.log(554.251587,2),math.log(930.979553,2),math.log(1578.842041,2)]
t_236 = [math.log(256.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(222.000000,2),math.log(220.000000,2),math.log(230.000000,2),math.log(265.000000,2),math.log(273.750000,2),math.log(248.000000,2),math.log(292.343750,2),math.log(267.343750,2),math.log(266.960938,2),math.log(242.367188,2),math.log(268.945312,2),math.log(234.322266,2),math.log(275.838867,2),math.log(303.695312,2),math.log(386.210693,2),math.log(534.929321,2),math.log(888.718079,2)]
t_237 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(247.000000,2),math.log(276.500000,2),math.log(242.500000,2),math.log(227.750000,2),math.log(271.312500,2),math.log(234.500000,2),math.log(236.812500,2),math.log(272.851562,2),math.log(278.058594,2),math.log(291.046875,2),math.log(299.889648,2),math.log(328.038086,2),math.log(371.230957,2),math.log(433.638428,2),math.log(586.060913,2),math.log(975.612854,2)]
t_238 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(228.000000,2),math.log(216.250000,2),math.log(222.125000,2),math.log(207.125000,2),math.log(241.187500,2),math.log(221.000000,2),math.log(267.554688,2),math.log(313.597656,2),math.log(292.320312,2),math.log(288.914062,2),math.log(311.610840,2),math.log(305.651367,2),math.log(324.562256,2),math.log(344.068542,2),math.log(545.186584,2)]
t_239 = [math.log(256.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(298.000000,2),math.log(308.000000,2),math.log(272.500000,2),math.log(266.250000,2),math.log(273.000000,2),math.log(264.500000,2),math.log(284.250000,2),math.log(270.406250,2),math.log(275.078125,2),math.log(267.558594,2),math.log(280.740234,2),math.log(252.605469,2),math.log(266.404297,2),math.log(284.229736,2),math.log(370.433716,2),math.log(541.164368,2),math.log(886.943695,2)]
t_240 = [math.log(272.000000,2),math.log(264.000000,2),math.log(220.000000,2),math.log(262.000000,2),math.log(249.000000,2),math.log(222.500000,2),math.log(236.250000,2),math.log(218.625000,2),math.log(208.375000,2),math.log(199.250000,2),math.log(223.015625,2),math.log(241.242188,2),math.log(217.371094,2),math.log(237.291016,2),math.log(204.649414,2),math.log(239.844727,2),math.log(249.080078,2),math.log(284.437622,2),math.log(378.263611,2),math.log(490.423584,2)]
t_241 = [math.log(256.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(220.000000,2),math.log(212.000000,2),math.log(219.000000,2),math.log(255.750000,2),math.log(266.625000,2),math.log(287.687500,2),math.log(266.343750,2),math.log(263.500000,2),math.log(259.867188,2),math.log(250.625000,2),math.log(262.208984,2),math.log(274.253906,2),math.log(300.794434,2),math.log(363.646729,2),math.log(478.520020,2),math.log(593.158691,2),math.log(1001.678497,2)]
t_242 = [math.log(288.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(252.000000,2),math.log(281.000000,2),math.log(271.000000,2),math.log(270.750000,2),math.log(264.750000,2),math.log(229.125000,2),math.log(232.656250,2),math.log(274.546875,2),math.log(276.140625,2),math.log(256.550781,2),math.log(274.177734,2),math.log(255.186523,2),math.log(257.319336,2),math.log(287.032959,2),math.log(372.955933,2),math.log(460.789429,2),math.log(753.307831,2)]
t_243 = [math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(258.000000,2),math.log(253.000000,2),math.log(222.500000,2),math.log(244.000000,2),math.log(247.312500,2),math.log(253.625000,2),math.log(257.671875,2),math.log(284.367188,2),math.log(249.230469,2),math.log(275.593750,2),math.log(261.757812,2),math.log(236.453613,2),math.log(270.454834,2),math.log(314.844116,2),math.log(441.099731,2),math.log(653.018829,2)]
t_244 = [math.log(304.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(258.000000,2),math.log(237.500000,2),math.log(216.750000,2),math.log(214.250000,2),math.log(216.000000,2),math.log(224.531250,2),math.log(274.593750,2),math.log(270.765625,2),math.log(236.375000,2),math.log(228.130859,2),math.log(249.818359,2),math.log(262.708496,2),math.log(298.025635,2),math.log(353.697754,2),math.log(474.326843,2),math.log(742.716705,2)]
t_245 = [math.log(256.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(284.000000,2),math.log(295.500000,2),math.log(296.000000,2),math.log(302.375000,2),math.log(254.750000,2),math.log(250.281250,2),math.log(269.562500,2),math.log(276.273438,2),math.log(252.777344,2),math.log(285.361328,2),math.log(276.021484,2),math.log(313.267090,2),math.log(350.029053,2),math.log(407.036987,2),math.log(551.712158,2),math.log(833.890686,2)]
t_246 = [math.log(272.000000,2),math.log(264.000000,2),math.log(308.000000,2),math.log(316.000000,2),math.log(267.000000,2),math.log(241.500000,2),math.log(243.250000,2),math.log(202.125000,2),math.log(225.500000,2),math.log(207.781250,2),math.log(254.015625,2),math.log(257.210938,2),math.log(274.937500,2),math.log(279.937500,2),math.log(288.007812,2),math.log(340.873535,2),math.log(421.437744,2),math.log(515.570679,2),math.log(680.641174,2),math.log(1196.053711,2)]
t_247 = [math.log(240.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(298.000000,2),math.log(289.000000,2),math.log(254.000000,2),math.log(256.750000,2),math.log(231.375000,2),math.log(228.437500,2),math.log(267.375000,2),math.log(255.218750,2),math.log(267.281250,2),math.log(297.843750,2),math.log(244.523438,2),math.log(272.399414,2),math.log(281.270508,2),math.log(319.308350,2),math.log(368.565308,2),math.log(501.443420,2),math.log(865.556641,2)]
t_248 = [math.log(336.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(292.000000,2),math.log(301.000000,2),math.log(282.500000,2),math.log(259.500000,2),math.log(263.625000,2),math.log(279.125000,2),math.log(247.781250,2),math.log(247.343750,2),math.log(252.976562,2),math.log(248.488281,2),math.log(265.621094,2),math.log(256.169922,2),math.log(284.131836,2),math.log(258.899414,2),math.log(324.569214,2),math.log(373.450928,2),math.log(556.361267,2)]
t_249 = [math.log(288.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(262.000000,2),math.log(236.000000,2),math.log(235.000000,2),math.log(231.500000,2),math.log(271.750000,2),math.log(271.546875,2),math.log(214.085938,2),math.log(226.250000,2),math.log(248.931641,2),math.log(279.146484,2),math.log(294.410645,2),math.log(378.028809,2),math.log(532.212402,2),math.log(723.823364,2),math.log(1198.401581,2)]
t_250 = [math.log(288.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(252.000000,2),math.log(233.000000,2),math.log(251.750000,2),math.log(244.625000,2),math.log(267.312500,2),math.log(272.531250,2),math.log(267.031250,2),math.log(271.085938,2),math.log(293.511719,2),math.log(289.117188,2),math.log(289.461914,2),math.log(281.237793,2),math.log(294.555664,2),math.log(381.816284,2),math.log(512.364807,2),math.log(767.694214,2)]
t_251 = [math.log(224.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(303.500000,2),math.log(312.000000,2),math.log(312.625000,2),math.log(303.500000,2),math.log(290.437500,2),math.log(234.578125,2),math.log(250.585938,2),math.log(242.425781,2),math.log(255.519531,2),math.log(274.336914,2),math.log(299.229492,2),math.log(352.216553,2),math.log(373.188965,2),math.log(438.665405,2),math.log(627.064026,2)]
t_252 = [math.log(272.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(250.000000,2),math.log(236.500000,2),math.log(235.250000,2),math.log(199.375000,2),math.log(241.687500,2),math.log(282.781250,2),math.log(273.687500,2),math.log(273.195312,2),math.log(261.703125,2),math.log(240.707031,2),math.log(243.767578,2),math.log(226.758301,2),math.log(305.879639,2),math.log(369.102905,2),math.log(436.978943,2),math.log(649.862122,2)]
t_253 = [math.log(256.000000,2),math.log(264.000000,2),math.log(292.000000,2),math.log(276.000000,2),math.log(236.000000,2),math.log(238.500000,2),math.log(231.000000,2),math.log(270.500000,2),math.log(283.687500,2),math.log(261.562500,2),math.log(255.218750,2),math.log(295.789062,2),math.log(245.566406,2),math.log(249.767578,2),math.log(287.146484,2),math.log(273.882324,2),math.log(356.766357,2),math.log(490.967773,2),math.log(787.474670,2),math.log(1281.081635,2)]
t_254 = [math.log(256.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(195.250000,2),math.log(197.125000,2),math.log(252.875000,2),math.log(245.406250,2),math.log(233.718750,2),math.log(246.289062,2),math.log(245.761719,2),math.log(233.736328,2),math.log(257.218750,2),math.log(239.995605,2),math.log(309.219238,2),math.log(345.642944,2),math.log(499.919434,2),math.log(779.639130,2)]
t_255 = [math.log(288.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(224.000000,2),math.log(238.000000,2),math.log(250.000000,2),math.log(291.750000,2),math.log(293.250000,2),math.log(299.437500,2),math.log(262.437500,2),math.log(268.828125,2),math.log(267.242188,2),math.log(241.062500,2),math.log(242.339844,2),math.log(285.342773,2),math.log(326.844727,2),math.log(408.841797,2),math.log(496.161133,2),math.log(709.038025,2),math.log(1276.321411,2)]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00004981
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00004981)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00004981
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00004981)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00004981
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00004981)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00004981
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00004981)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00004981
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00004981)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00004981
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00004981)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00004981
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00004981)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00004981
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00004981)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00004981
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00004981)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00004981
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00004981)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00004981
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00004981)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00004981
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00004981)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00004981
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00004981)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00004981
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00004981)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00004981
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00004981)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00004981
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00004981)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00004981
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00004981)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00004981
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00004981)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00004981
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00004981)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00004981
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00004981)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 7 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
