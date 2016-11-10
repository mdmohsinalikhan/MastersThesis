import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(240.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(290.000000,2),math.log(292.000000,2),math.log(248.000000,2),math.log(289.500000,2),math.log(278.000000,2),math.log(243.937500,2),math.log(278.156250,2),math.log(259.593750,2),math.log(260.015625,2),math.log(281.957031,2),math.log(311.023438,2),math.log(283.994141,2),math.log(267.063965,2),math.log(283.708740,2),math.log(321.101074,2),math.log(319.035339,2),math.log(268.947540,2)]
t_1 = [math.log(224.000000,2),math.log(216.000000,2),math.log(256.000000,2),math.log(222.000000,2),math.log(220.000000,2),math.log(245.000000,2),math.log(257.250000,2),math.log(257.000000,2),math.log(247.562500,2),math.log(245.406250,2),math.log(245.421875,2),math.log(271.593750,2),math.log(259.140625,2),math.log(260.099609,2),math.log(276.787109,2),math.log(247.816895,2),math.log(227.222168,2),math.log(240.256348,2),math.log(257.178833,2),math.log(297.095093,2)]
t_2 = [math.log(272.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(270.000000,2),math.log(258.000000,2),math.log(227.000000,2),math.log(221.750000,2),math.log(236.000000,2),math.log(222.875000,2),math.log(228.781250,2),math.log(264.078125,2),math.log(254.210938,2),math.log(263.625000,2),math.log(249.408203,2),math.log(245.348633,2),math.log(254.937500,2),math.log(240.677979,2),math.log(269.790161,2),math.log(249.588989,2),math.log(266.919159,2)]
t_3 = [math.log(240.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(274.000000,2),math.log(283.000000,2),math.log(280.000000,2),math.log(269.125000,2),math.log(266.625000,2),math.log(272.406250,2),math.log(246.937500,2),math.log(252.742188,2),math.log(246.906250,2),math.log(275.382812,2),math.log(269.364258,2),math.log(287.033691,2),math.log(263.396973,2),math.log(261.299805,2),math.log(263.875244,2),math.log(221.294952,2)]
t_4 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(270.000000,2),math.log(241.500000,2),math.log(223.875000,2),math.log(228.687500,2),math.log(273.468750,2),math.log(237.187500,2),math.log(199.484375,2),math.log(222.140625,2),math.log(209.300781,2),math.log(238.030273,2),math.log(252.112793,2),math.log(260.232666,2),math.log(262.954468,2),math.log(253.219421,2),math.log(235.015717,2)]
t_5 = [math.log(256.000000,2),math.log(248.000000,2),math.log(288.000000,2),math.log(296.000000,2),math.log(262.000000,2),math.log(260.000000,2),math.log(258.750000,2),math.log(278.500000,2),math.log(251.500000,2),math.log(247.437500,2),math.log(249.250000,2),math.log(249.601562,2),math.log(259.472656,2),math.log(256.632812,2),math.log(255.108398,2),math.log(235.346680,2),math.log(242.629883,2),math.log(253.899536,2),math.log(248.119446,2),math.log(285.408020,2)]
t_6 = [math.log(272.000000,2),math.log(304.000000,2),math.log(296.000000,2),math.log(252.000000,2),math.log(267.000000,2),math.log(297.500000,2),math.log(249.250000,2),math.log(244.875000,2),math.log(210.562500,2),math.log(271.562500,2),math.log(254.625000,2),math.log(271.429688,2),math.log(246.324219,2),math.log(244.966797,2),math.log(261.246094,2),math.log(281.415527,2),math.log(312.639160,2),math.log(300.174072,2),math.log(288.546326,2),math.log(268.616333,2)]
t_7 = [math.log(272.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(258.000000,2),math.log(251.000000,2),math.log(232.000000,2),math.log(242.250000,2),math.log(252.875000,2),math.log(258.562500,2),math.log(256.062500,2),math.log(252.328125,2),math.log(232.492188,2),math.log(243.207031,2),math.log(231.298828,2),math.log(219.748047,2),math.log(225.920898,2),math.log(263.268799,2),math.log(292.096436,2),math.log(265.728210,2),math.log(253.924438,2)]
t_8 = [math.log(272.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(261.000000,2),math.log(251.500000,2),math.log(267.500000,2),math.log(262.250000,2),math.log(238.937500,2),math.log(236.843750,2),math.log(208.781250,2),math.log(236.492188,2),math.log(216.707031,2),math.log(203.027344,2),math.log(220.317383,2),math.log(231.927246,2),math.log(216.339111,2),math.log(236.189575,2),math.log(237.551025,2),math.log(206.629822,2)]
t_9 = [math.log(272.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(245.000000,2),math.log(271.500000,2),math.log(235.500000,2),math.log(256.500000,2),math.log(231.062500,2),math.log(218.312500,2),math.log(208.359375,2),math.log(221.687500,2),math.log(236.347656,2),math.log(284.529297,2),math.log(284.788086,2),math.log(273.359375,2),math.log(288.414062,2),math.log(308.597778,2),math.log(272.154236,2),math.log(266.297699,2)]
t_10 = [math.log(240.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(250.000000,2),math.log(269.000000,2),math.log(274.000000,2),math.log(259.000000,2),math.log(269.375000,2),math.log(278.875000,2),math.log(234.031250,2),math.log(275.890625,2),math.log(262.359375,2),math.log(256.984375,2),math.log(245.343750,2),math.log(260.213867,2),math.log(238.633301,2),math.log(252.303223,2),math.log(263.108398,2),math.log(286.461853,2),math.log(381.633362,2)]
t_11 = [math.log(256.000000,2),math.log(232.000000,2),math.log(204.000000,2),math.log(250.000000,2),math.log(251.000000,2),math.log(270.000000,2),math.log(247.000000,2),math.log(236.125000,2),math.log(208.375000,2),math.log(243.718750,2),math.log(252.140625,2),math.log(270.382812,2),math.log(249.597656,2),math.log(224.441406,2),math.log(261.309570,2),math.log(278.542969,2),math.log(310.926758,2),math.log(266.812866,2),math.log(300.459656,2),math.log(302.155853,2)]
t_12 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(212.000000,2),math.log(228.000000,2),math.log(220.000000,2),math.log(230.500000,2),math.log(227.500000,2),math.log(268.687500,2),math.log(263.406250,2),math.log(227.000000,2),math.log(253.804688,2),math.log(214.234375,2),math.log(216.935547,2),math.log(221.724609,2),math.log(230.805664,2),math.log(194.432373,2),math.log(236.978638,2),math.log(230.439758,2),math.log(258.712463,2)]
t_13 = [math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(254.000000,2),math.log(248.500000,2),math.log(274.750000,2),math.log(281.750000,2),math.log(311.000000,2),math.log(292.312500,2),math.log(238.734375,2),math.log(233.328125,2),math.log(292.652344,2),math.log(275.722656,2),math.log(256.898438,2),math.log(300.760742,2),math.log(293.471436,2),math.log(275.361938,2),math.log(262.269897,2),math.log(260.375763,2)]
t_14 = [math.log(256.000000,2),math.log(264.000000,2),math.log(340.000000,2),math.log(298.000000,2),math.log(250.000000,2),math.log(266.000000,2),math.log(254.750000,2),math.log(252.750000,2),math.log(244.687500,2),math.log(225.500000,2),math.log(273.328125,2),math.log(233.906250,2),math.log(288.800781,2),math.log(279.685547,2),math.log(268.579102,2),math.log(273.853516,2),math.log(259.310547,2),math.log(289.954834,2),math.log(312.339111,2),math.log(288.424744,2)]
t_15 = [math.log(256.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(262.000000,2),math.log(260.000000,2),math.log(255.500000,2),math.log(239.000000,2),math.log(230.375000,2),math.log(228.937500,2),math.log(219.468750,2),math.log(285.906250,2),math.log(262.445312,2),math.log(266.117188,2),math.log(254.974609,2),math.log(229.129883,2),math.log(271.342773,2),math.log(261.911133,2),math.log(262.179932,2),math.log(284.762268,2),math.log(335.452820,2)]
t_16 = [math.log(256.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(278.000000,2),math.log(287.000000,2),math.log(263.500000,2),math.log(208.250000,2),math.log(261.125000,2),math.log(238.000000,2),math.log(245.531250,2),math.log(257.500000,2),math.log(286.007812,2),math.log(265.566406,2),math.log(246.607422,2),math.log(254.566406,2),math.log(264.172852,2),math.log(267.617676,2),math.log(265.304565,2),math.log(239.500122,2),math.log(249.217255,2)]
t_17 = [math.log(288.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(290.000000,2),math.log(281.000000,2),math.log(262.000000,2),math.log(242.500000,2),math.log(238.750000,2),math.log(261.187500,2),math.log(252.562500,2),math.log(270.328125,2),math.log(219.484375,2),math.log(219.160156,2),math.log(236.869141,2),math.log(274.900391,2),math.log(242.975586,2),math.log(246.567627,2),math.log(257.571777,2),math.log(256.564331,2),math.log(274.480743,2)]
t_18 = [math.log(320.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(255.000000,2),math.log(222.000000,2),math.log(238.750000,2),math.log(240.375000,2),math.log(245.312500,2),math.log(276.812500,2),math.log(267.375000,2),math.log(245.898438,2),math.log(274.902344,2),math.log(269.451172,2),math.log(273.992188,2),math.log(250.426758,2),math.log(232.665527,2),math.log(199.698120,2),math.log(239.469238,2),math.log(242.951935,2)]
t_19 = [math.log(240.000000,2),math.log(296.000000,2),math.log(292.000000,2),math.log(290.000000,2),math.log(293.000000,2),math.log(258.500000,2),math.log(237.000000,2),math.log(244.750000,2),math.log(251.687500,2),math.log(257.031250,2),math.log(243.421875,2),math.log(247.218750,2),math.log(278.445312,2),math.log(254.843750,2),math.log(236.552734,2),math.log(275.009277,2),math.log(236.279785,2),math.log(240.170288,2),math.log(237.391357,2),math.log(247.826355,2)]
t_20 = [math.log(224.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(218.000000,2),math.log(231.000000,2),math.log(225.500000,2),math.log(226.250000,2),math.log(238.750000,2),math.log(246.750000,2),math.log(232.031250,2),math.log(219.500000,2),math.log(269.734375,2),math.log(312.589844,2),math.log(306.591797,2),math.log(282.708008,2),math.log(249.826660,2),math.log(219.652832,2),math.log(271.976929,2),math.log(291.205872,2),math.log(334.028351,2)]
t_21 = [math.log(272.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(264.000000,2),math.log(239.000000,2),math.log(242.000000,2),math.log(249.500000,2),math.log(255.375000,2),math.log(248.000000,2),math.log(265.718750,2),math.log(261.296875,2),math.log(281.203125,2),math.log(247.996094,2),math.log(229.890625,2),math.log(264.380859,2),math.log(278.021484,2),math.log(300.222900,2),math.log(316.212036,2),math.log(233.307068,2),math.log(259.698425,2)]
t_22 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(232.000000,2),math.log(241.000000,2),math.log(243.500000,2),math.log(235.000000,2),math.log(207.500000,2),math.log(241.187500,2),math.log(277.718750,2),math.log(293.718750,2),math.log(278.781250,2),math.log(285.390625,2),math.log(271.957031,2),math.log(263.433594,2),math.log(255.287598,2),math.log(273.067139,2),math.log(269.645874,2),math.log(285.606506,2),math.log(251.944427,2)]
t_23 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(282.000000,2),math.log(264.000000,2),math.log(258.500000,2),math.log(265.500000,2),math.log(257.125000,2),math.log(217.000000,2),math.log(202.125000,2),math.log(222.812500,2),math.log(259.585938,2),math.log(261.324219,2),math.log(260.052734,2),math.log(253.153320,2),math.log(267.310059,2),math.log(274.141602,2),math.log(261.176636,2),math.log(331.889465,2),math.log(306.679169,2)]
t_24 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(234.000000,2),math.log(208.000000,2),math.log(216.750000,2),math.log(240.875000,2),math.log(247.625000,2),math.log(247.687500,2),math.log(261.437500,2),math.log(271.765625,2),math.log(277.390625,2),math.log(271.246094,2),math.log(266.495117,2),math.log(238.043457,2),math.log(264.720947,2),math.log(223.679810,2),math.log(244.870789,2),math.log(267.081482,2)]
t_25 = [math.log(256.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(240.000000,2),math.log(231.000000,2),math.log(243.500000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(219.812500,2),math.log(290.500000,2),math.log(262.390625,2),math.log(279.781250,2),math.log(280.039062,2),math.log(276.429688,2),math.log(256.039062,2),math.log(256.599609,2),math.log(246.524658,2),math.log(232.810547,2),math.log(240.179749,2),math.log(242.079010,2)]
t_26 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(265.000000,2),math.log(234.000000,2),math.log(237.250000,2),math.log(256.000000,2),math.log(236.187500,2),math.log(256.437500,2),math.log(253.328125,2),math.log(248.218750,2),math.log(251.921875,2),math.log(271.056641,2),math.log(238.133789,2),math.log(279.624512,2),math.log(267.107910,2),math.log(247.804688,2),math.log(253.205933,2),math.log(315.395264,2)]
t_27 = [math.log(224.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(236.000000,2),math.log(245.000000,2),math.log(263.500000,2),math.log(255.500000,2),math.log(226.625000,2),math.log(248.312500,2),math.log(257.406250,2),math.log(231.343750,2),math.log(266.109375,2),math.log(290.722656,2),math.log(298.228516,2),math.log(306.305664,2),math.log(302.732422,2),math.log(266.294434,2),math.log(261.530029,2),math.log(268.591736,2),math.log(272.236908,2)]
t_28 = [math.log(288.000000,2),math.log(296.000000,2),math.log(276.000000,2),math.log(258.000000,2),math.log(284.000000,2),math.log(255.000000,2),math.log(273.250000,2),math.log(290.750000,2),math.log(276.562500,2),math.log(229.062500,2),math.log(225.718750,2),math.log(246.375000,2),math.log(289.484375,2),math.log(260.466797,2),math.log(264.977539,2),math.log(262.606445,2),math.log(241.393799,2),math.log(214.953735,2),math.log(213.290466,2),math.log(242.804108,2)]
t_29 = [math.log(224.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(241.000000,2),math.log(261.500000,2),math.log(233.500000,2),math.log(244.375000,2),math.log(263.687500,2),math.log(270.906250,2),math.log(272.968750,2),math.log(255.968750,2),math.log(250.773438,2),math.log(230.525391,2),math.log(236.677734,2),math.log(274.257324,2),math.log(292.303955,2),math.log(247.260376,2),math.log(254.705444,2),math.log(267.883728,2)]
t_30 = [math.log(224.000000,2),math.log(224.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(258.000000,2),math.log(255.500000,2),math.log(258.750000,2),math.log(227.000000,2),math.log(221.875000,2),math.log(247.156250,2),math.log(234.859375,2),math.log(261.890625,2),math.log(227.449219,2),math.log(248.662109,2),math.log(271.652344,2),math.log(302.413574,2),math.log(302.001953,2),math.log(261.446777,2),math.log(256.269897,2),math.log(279.248596,2)]
t_31 = [math.log(240.000000,2),math.log(304.000000,2),math.log(260.000000,2),math.log(278.000000,2),math.log(281.000000,2),math.log(278.000000,2),math.log(264.000000,2),math.log(241.875000,2),math.log(259.062500,2),math.log(246.437500,2),math.log(254.687500,2),math.log(254.101562,2),math.log(249.703125,2),math.log(277.574219,2),math.log(234.392578,2),math.log(255.363281,2),math.log(246.598145,2),math.log(243.310791,2),math.log(252.877075,2),math.log(255.219971,2)]
t_32 = [math.log(240.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(238.000000,2),math.log(232.000000,2),math.log(262.000000,2),math.log(275.000000,2),math.log(297.375000,2),math.log(291.562500,2),math.log(264.125000,2),math.log(262.500000,2),math.log(260.984375,2),math.log(228.328125,2),math.log(242.070312,2),math.log(262.023438,2),math.log(300.700195,2),math.log(259.389648,2),math.log(245.930786,2),math.log(248.402893,2),math.log(291.808899,2)]
t_33 = [math.log(288.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(267.000000,2),math.log(242.000000,2),math.log(262.250000,2),math.log(260.125000,2),math.log(269.937500,2),math.log(271.000000,2),math.log(248.000000,2),math.log(244.679688,2),math.log(254.410156,2),math.log(246.455078,2),math.log(264.475586,2),math.log(302.925293,2),math.log(278.707764,2),math.log(291.060181,2),math.log(303.257690,2),math.log(334.000732,2)]
t_34 = [math.log(224.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(276.000000,2),math.log(306.000000,2),math.log(307.500000,2),math.log(267.750000,2),math.log(278.500000,2),math.log(261.000000,2),math.log(241.187500,2),math.log(224.437500,2),math.log(242.968750,2),math.log(277.804688,2),math.log(284.472656,2),math.log(288.435547,2),math.log(262.618652,2),math.log(276.142578,2),math.log(273.764771,2),math.log(253.588928,2),math.log(255.142914,2)]
t_35 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(273.000000,2),math.log(254.250000,2),math.log(263.625000,2),math.log(265.687500,2),math.log(235.093750,2),math.log(244.796875,2),math.log(250.914062,2),math.log(295.554688,2),math.log(261.375000,2),math.log(239.173828,2),math.log(258.079102,2),math.log(268.413574,2),math.log(253.168945,2),math.log(241.453796,2),math.log(233.960815,2)]
t_36 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(310.000000,2),math.log(278.000000,2),math.log(275.000000,2),math.log(269.500000,2),math.log(267.500000,2),math.log(258.687500,2),math.log(255.343750,2),math.log(256.484375,2),math.log(265.296875,2),math.log(242.960938,2),math.log(257.451172,2),math.log(243.946289,2),math.log(250.351562,2),math.log(251.242432,2),math.log(235.493408,2),math.log(242.798645,2),math.log(244.339355,2)]
t_37 = [math.log(288.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(246.000000,2),math.log(221.000000,2),math.log(226.000000,2),math.log(218.500000,2),math.log(253.625000,2),math.log(280.562500,2),math.log(250.875000,2),math.log(228.796875,2),math.log(266.695312,2),math.log(230.519531,2),math.log(223.234375,2),math.log(217.161133,2),math.log(213.154785,2),math.log(206.195312,2),math.log(229.565552,2),math.log(240.059998,2),math.log(270.495117,2)]
t_38 = [math.log(240.000000,2),math.log(216.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(246.000000,2),math.log(224.000000,2),math.log(263.750000,2),math.log(263.125000,2),math.log(220.625000,2),math.log(239.593750,2),math.log(259.750000,2),math.log(267.640625,2),math.log(263.484375,2),math.log(264.523438,2),math.log(277.943359,2),math.log(264.999512,2),math.log(278.638672,2),math.log(282.553833,2),math.log(258.022705,2),math.log(283.744415,2)]
t_39 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(261.000000,2),math.log(240.000000,2),math.log(266.750000,2),math.log(274.625000,2),math.log(270.312500,2),math.log(247.250000,2),math.log(233.625000,2),math.log(238.585938,2),math.log(231.808594,2),math.log(240.144531,2),math.log(241.368164,2),math.log(236.951660,2),math.log(257.663574,2),math.log(241.951660,2),math.log(252.879150,2),math.log(224.019409,2)]
t_40 = [math.log(240.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(251.000000,2),math.log(247.000000,2),math.log(225.750000,2),math.log(222.625000,2),math.log(223.125000,2),math.log(272.031250,2),math.log(288.750000,2),math.log(243.406250,2),math.log(223.343750,2),math.log(218.158203,2),math.log(219.214844,2),math.log(214.353516,2),math.log(233.467529,2),math.log(258.313721,2),math.log(264.247986,2),math.log(266.494629,2)]
t_41 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(298.000000,2),math.log(265.000000,2),math.log(285.500000,2),math.log(266.250000,2),math.log(252.375000,2),math.log(238.625000,2),math.log(271.000000,2),math.log(231.281250,2),math.log(250.000000,2),math.log(242.601562,2),math.log(247.718750,2),math.log(245.082031,2),math.log(228.281738,2),math.log(260.033203,2),math.log(250.441040,2),math.log(267.607117,2),math.log(279.226654,2)]
t_42 = [math.log(224.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(231.000000,2),math.log(245.000000,2),math.log(251.250000,2),math.log(260.000000,2),math.log(248.500000,2),math.log(246.562500,2),math.log(238.125000,2),math.log(248.007812,2),math.log(281.972656,2),math.log(286.169922,2),math.log(258.656250,2),math.log(226.448242,2),math.log(276.868408,2),math.log(293.487549,2),math.log(292.281006,2),math.log(310.346375,2)]
t_43 = [math.log(256.000000,2),math.log(288.000000,2),math.log(304.000000,2),math.log(264.000000,2),math.log(237.000000,2),math.log(279.000000,2),math.log(271.250000,2),math.log(277.250000,2),math.log(308.062500,2),math.log(295.281250,2),math.log(279.109375,2),math.log(236.531250,2),math.log(242.851562,2),math.log(231.537109,2),math.log(241.396484,2),math.log(283.033203,2),math.log(256.254150,2),math.log(291.012817,2),math.log(281.694153,2),math.log(343.112305,2)]
t_44 = [math.log(224.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(266.000000,2),math.log(285.500000,2),math.log(261.000000,2),math.log(262.250000,2),math.log(283.625000,2),math.log(283.156250,2),math.log(278.250000,2),math.log(266.765625,2),math.log(223.562500,2),math.log(235.349609,2),math.log(231.890625,2),math.log(233.304688,2),math.log(254.074951,2),math.log(264.799194,2),math.log(265.905518,2),math.log(280.430817,2)]
t_45 = [math.log(240.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(312.000000,2),math.log(274.000000,2),math.log(258.750000,2),math.log(211.000000,2),math.log(206.000000,2),math.log(210.406250,2),math.log(261.843750,2),math.log(254.664062,2),math.log(289.726562,2),math.log(285.916016,2),math.log(247.452148,2),math.log(232.428223,2),math.log(213.486328,2),math.log(273.067871,2),math.log(298.996033,2),math.log(256.799072,2)]
t_46 = [math.log(272.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(220.500000,2),math.log(226.500000,2),math.log(237.875000,2),math.log(261.375000,2),math.log(246.718750,2),math.log(271.859375,2),math.log(278.421875,2),math.log(258.062500,2),math.log(280.798828,2),math.log(271.133789,2),math.log(278.632324,2),math.log(288.259277,2),math.log(276.365234,2),math.log(274.822632,2),math.log(276.727875,2)]
t_47 = [math.log(256.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(222.000000,2),math.log(219.000000,2),math.log(224.500000,2),math.log(236.250000,2),math.log(251.125000,2),math.log(280.937500,2),math.log(229.843750,2),math.log(230.250000,2),math.log(253.093750,2),math.log(241.636719,2),math.log(256.279297,2),math.log(278.115234,2),math.log(238.549316,2),math.log(268.194580,2),math.log(284.304932,2),math.log(305.094238,2),math.log(299.838715,2)]
t_48 = [math.log(240.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(290.000000,2),math.log(283.000000,2),math.log(318.000000,2),math.log(312.500000,2),math.log(276.375000,2),math.log(253.750000,2),math.log(275.187500,2),math.log(273.093750,2),math.log(237.562500,2),math.log(250.054688,2),math.log(250.775391,2),math.log(230.192383,2),math.log(237.018066,2),math.log(239.197266,2),math.log(239.051758,2),math.log(202.318237,2),math.log(222.264221,2)]
t_49 = [math.log(240.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(254.500000,2),math.log(240.250000,2),math.log(257.000000,2),math.log(242.625000,2),math.log(260.625000,2),math.log(251.390625,2),math.log(265.906250,2),math.log(244.343750,2),math.log(239.632812,2),math.log(212.445312,2),math.log(208.435059,2),math.log(209.268799,2),math.log(243.079834,2),math.log(244.161743,2),math.log(254.741272,2)]
t_50 = [math.log(288.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(267.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(298.125000,2),math.log(240.750000,2),math.log(270.000000,2),math.log(274.468750,2),math.log(277.531250,2),math.log(236.625000,2),math.log(232.679688,2),math.log(255.526367,2),math.log(280.667969,2),math.log(313.258789,2),math.log(251.360962,2),math.log(271.981812,2),math.log(246.243744,2)]
t_51 = [math.log(256.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(278.000000,2),math.log(279.000000,2),math.log(269.500000,2),math.log(244.750000,2),math.log(243.000000,2),math.log(249.875000,2),math.log(242.968750,2),math.log(246.375000,2),math.log(234.460938,2),math.log(255.414062,2),math.log(241.636719,2),math.log(257.133789,2),math.log(262.225586,2),math.log(241.034912,2),math.log(249.386963,2),math.log(262.054565,2),math.log(232.278473,2)]
t_52 = [math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(218.000000,2),math.log(241.000000,2),math.log(261.500000,2),math.log(256.750000,2),math.log(228.875000,2),math.log(258.125000,2),math.log(295.375000,2),math.log(247.078125,2),math.log(240.500000,2),math.log(221.996094,2),math.log(246.541016,2),math.log(288.417969,2),math.log(244.519531,2),math.log(269.866211,2),math.log(236.869385,2),math.log(210.050720,2),math.log(258.462128,2)]
t_53 = [math.log(240.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(212.000000,2),math.log(205.500000,2),math.log(237.500000,2),math.log(252.375000,2),math.log(256.687500,2),math.log(244.250000,2),math.log(246.328125,2),math.log(252.523438,2),math.log(238.859375,2),math.log(227.152344,2),math.log(249.341797,2),math.log(256.699219,2),math.log(271.575928,2),math.log(289.469604,2),math.log(292.321960,2),math.log(280.123566,2)]
t_54 = [math.log(240.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(286.000000,2),math.log(266.000000,2),math.log(278.000000,2),math.log(272.750000,2),math.log(262.875000,2),math.log(276.937500,2),math.log(270.468750,2),math.log(205.859375,2),math.log(227.468750,2),math.log(208.105469,2),math.log(229.781250,2),math.log(222.092773,2),math.log(239.469238,2),math.log(247.590820,2),math.log(239.666748,2),math.log(250.776550,2),math.log(216.279999,2)]
t_55 = [math.log(272.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(246.000000,2),math.log(258.000000,2),math.log(232.250000,2),math.log(285.000000,2),math.log(283.812500,2),math.log(260.625000,2),math.log(251.640625,2),math.log(274.617188,2),math.log(228.843750,2),math.log(240.341797,2),math.log(212.799805,2),math.log(247.523926,2),math.log(223.301270,2),math.log(245.178955,2),math.log(267.355408,2),math.log(278.534454,2)]
t_56 = [math.log(272.000000,2),math.log(304.000000,2),math.log(276.000000,2),math.log(242.000000,2),math.log(252.000000,2),math.log(278.500000,2),math.log(268.000000,2),math.log(259.125000,2),math.log(244.625000,2),math.log(279.125000,2),math.log(267.062500,2),math.log(267.687500,2),math.log(265.570312,2),math.log(251.275391,2),math.log(217.102539,2),math.log(204.518555,2),math.log(222.264648,2),math.log(238.549805,2),math.log(232.084045,2),math.log(265.195099,2)]
t_57 = [math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(285.000000,2),math.log(264.500000,2),math.log(234.750000,2),math.log(249.875000,2),math.log(257.812500,2),math.log(281.375000,2),math.log(284.640625,2),math.log(228.695312,2),math.log(219.964844,2),math.log(208.488281,2),math.log(210.104492,2),math.log(259.710938,2),math.log(229.260498,2),math.log(229.068481,2),math.log(257.604309,2),math.log(244.942993,2)]
t_58 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(266.000000,2),math.log(243.000000,2),math.log(254.000000,2),math.log(234.125000,2),math.log(241.312500,2),math.log(240.968750,2),math.log(258.125000,2),math.log(254.601562,2),math.log(226.066406,2),math.log(251.908203,2),math.log(282.975586,2),math.log(238.740234,2),math.log(269.752930,2),math.log(285.006104,2),math.log(289.809265,2),math.log(358.676880,2)]
t_59 = [math.log(240.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(238.000000,2),math.log(258.000000,2),math.log(243.000000,2),math.log(236.000000,2),math.log(233.875000,2),math.log(264.625000,2),math.log(261.812500,2),math.log(285.406250,2),math.log(290.742188,2),math.log(289.457031,2),math.log(224.951172,2),math.log(248.543945,2),math.log(281.871582,2),math.log(265.023682,2),math.log(269.623779,2),math.log(278.782837,2),math.log(322.909546,2)]
t_60 = [math.log(256.000000,2),math.log(240.000000,2),math.log(228.000000,2),math.log(234.000000,2),math.log(252.000000,2),math.log(269.500000,2),math.log(222.500000,2),math.log(231.625000,2),math.log(234.625000,2),math.log(257.843750,2),math.log(263.406250,2),math.log(255.921875,2),math.log(251.902344,2),math.log(247.031250,2),math.log(218.510742,2),math.log(252.191895,2),math.log(215.245605,2),math.log(230.945190,2),math.log(212.709351,2),math.log(236.526794,2)]
t_61 = [math.log(240.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(251.000000,2),math.log(303.500000,2),math.log(247.000000,2),math.log(242.000000,2),math.log(249.000000,2),math.log(256.937500,2),math.log(269.171875,2),math.log(252.835938,2),math.log(245.375000,2),math.log(257.826172,2),math.log(266.860352,2),math.log(239.832031,2),math.log(237.096436,2),math.log(282.708008,2),math.log(282.723145,2),math.log(296.298401,2)]
t_62 = [math.log(256.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(258.000000,2),math.log(224.500000,2),math.log(222.750000,2),math.log(228.625000,2),math.log(239.250000,2),math.log(213.687500,2),math.log(260.203125,2),math.log(241.937500,2),math.log(241.964844,2),math.log(253.232422,2),math.log(257.086914,2),math.log(259.155762,2),math.log(275.315430,2),math.log(332.912720,2),math.log(312.907227,2),math.log(306.892120,2)]
t_63 = [math.log(224.000000,2),math.log(224.000000,2),math.log(264.000000,2),math.log(222.000000,2),math.log(262.000000,2),math.log(239.500000,2),math.log(246.500000,2),math.log(240.750000,2),math.log(229.312500,2),math.log(259.843750,2),math.log(241.640625,2),math.log(225.812500,2),math.log(267.332031,2),math.log(261.677734,2),math.log(224.697266,2),math.log(240.141602,2),math.log(254.237549,2),math.log(276.972168,2),math.log(297.227478,2),math.log(298.484833,2)]
t_64 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(277.000000,2),math.log(285.500000,2),math.log(274.500000,2),math.log(290.875000,2),math.log(270.875000,2),math.log(283.937500,2),math.log(261.515625,2),math.log(264.218750,2),math.log(296.605469,2),math.log(263.318359,2),math.log(243.902344,2),math.log(267.985352,2),math.log(270.531250,2),math.log(256.863037,2),math.log(257.408020,2),math.log(234.077026,2)]
t_65 = [math.log(272.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(306.000000,2),math.log(248.000000,2),math.log(278.000000,2),math.log(236.000000,2),math.log(276.375000,2),math.log(288.312500,2),math.log(276.031250,2),math.log(266.687500,2),math.log(305.031250,2),math.log(305.105469,2),math.log(265.027344,2),math.log(259.974609,2),math.log(251.058594,2),math.log(253.852783,2),math.log(264.254150,2),math.log(262.260986,2),math.log(254.715149,2)]
t_66 = [math.log(224.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(296.000000,2),math.log(270.000000,2),math.log(258.500000,2),math.log(270.500000,2),math.log(274.250000,2),math.log(276.125000,2),math.log(267.687500,2),math.log(278.468750,2),math.log(243.343750,2),math.log(260.402344,2),math.log(245.390625,2),math.log(271.181641,2),math.log(276.732910,2),math.log(281.107910,2),math.log(244.965088,2),math.log(264.646362,2),math.log(247.347839,2)]
t_67 = [math.log(240.000000,2),math.log(224.000000,2),math.log(260.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(203.000000,2),math.log(267.250000,2),math.log(310.750000,2),math.log(268.625000,2),math.log(232.843750,2),math.log(275.500000,2),math.log(257.476562,2),math.log(256.152344,2),math.log(255.812500,2),math.log(246.643555,2),math.log(266.356445,2),math.log(251.784912,2),math.log(252.463257,2),math.log(238.961121,2),math.log(258.910187,2)]
t_68 = [math.log(272.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(246.000000,2),math.log(267.500000,2),math.log(263.500000,2),math.log(212.875000,2),math.log(255.062500,2),math.log(278.437500,2),math.log(280.296875,2),math.log(229.484375,2),math.log(200.109375,2),math.log(203.427734,2),math.log(219.673828,2),math.log(259.256836,2),math.log(246.916748,2),math.log(260.674194,2),math.log(264.158752,2),math.log(279.491058,2)]
t_69 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(262.000000,2),math.log(272.000000,2),math.log(237.500000,2),math.log(260.000000,2),math.log(236.000000,2),math.log(231.750000,2),math.log(244.375000,2),math.log(247.640625,2),math.log(220.554688,2),math.log(218.792969,2),math.log(247.373047,2),math.log(247.601562,2),math.log(259.247559,2),math.log(248.472900,2),math.log(257.868652,2),math.log(237.642334,2),math.log(249.083649,2)]
t_70 = [math.log(272.000000,2),math.log(288.000000,2),math.log(300.000000,2),math.log(302.000000,2),math.log(278.000000,2),math.log(268.500000,2),math.log(280.250000,2),math.log(296.375000,2),math.log(277.125000,2),math.log(254.781250,2),math.log(262.031250,2),math.log(260.156250,2),math.log(278.105469,2),math.log(257.658203,2),math.log(257.527344,2),math.log(242.777344,2),math.log(259.929932,2),math.log(244.857788,2),math.log(238.830078,2),math.log(261.101410,2)]
t_71 = [math.log(256.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(222.000000,2),math.log(241.000000,2),math.log(277.000000,2),math.log(252.500000,2),math.log(249.000000,2),math.log(224.312500,2),math.log(244.125000,2),math.log(240.906250,2),math.log(238.484375,2),math.log(227.171875,2),math.log(241.929688,2),math.log(234.671875,2),math.log(247.748047,2),math.log(249.897705,2),math.log(240.954346,2),math.log(250.399048,2),math.log(266.412079,2)]
t_72 = [math.log(224.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(296.000000,2),math.log(274.000000,2),math.log(286.750000,2),math.log(257.125000,2),math.log(263.062500,2),math.log(230.843750,2),math.log(276.171875,2),math.log(255.437500,2),math.log(259.468750,2),math.log(252.107422,2),math.log(205.061523,2),math.log(245.519043,2),math.log(241.986816,2),math.log(241.003662,2),math.log(316.045288,2),math.log(293.827271,2)]
t_73 = [math.log(272.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(260.000000,2),math.log(291.500000,2),math.log(243.750000,2),math.log(239.500000,2),math.log(238.750000,2),math.log(234.781250,2),math.log(242.796875,2),math.log(235.601562,2),math.log(230.339844,2),math.log(275.552734,2),math.log(259.816406,2),math.log(251.883789,2),math.log(260.600830,2),math.log(232.388794,2),math.log(214.526855,2),math.log(240.953796,2)]
t_74 = [math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(274.000000,2),math.log(264.000000,2),math.log(262.750000,2),math.log(296.625000,2),math.log(253.375000,2),math.log(260.468750,2),math.log(274.609375,2),math.log(276.125000,2),math.log(284.019531,2),math.log(271.593750,2),math.log(263.762695,2),math.log(254.809570,2),math.log(259.998779,2),math.log(261.211548,2),math.log(278.339233,2),math.log(304.536377,2)]
t_75 = [math.log(256.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(242.000000,2),math.log(274.500000,2),math.log(264.250000,2),math.log(306.125000,2),math.log(293.875000,2),math.log(299.906250,2),math.log(278.000000,2),math.log(247.531250,2),math.log(240.664062,2),math.log(262.505859,2),math.log(289.977539,2),math.log(285.204102,2),math.log(255.835693,2),math.log(241.413818,2),math.log(279.678711,2),math.log(287.847412,2)]
t_76 = [math.log(304.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(290.000000,2),math.log(262.500000,2),math.log(237.250000,2),math.log(221.750000,2),math.log(265.562500,2),math.log(263.500000,2),math.log(241.140625,2),math.log(267.062500,2),math.log(257.375000,2),math.log(242.718750,2),math.log(258.315430,2),math.log(255.631348,2),math.log(255.155762,2),math.log(254.246338,2),math.log(256.189453,2),math.log(275.225769,2)]
t_77 = [math.log(336.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(270.000000,2),math.log(295.250000,2),math.log(284.750000,2),math.log(247.750000,2),math.log(257.562500,2),math.log(254.171875,2),math.log(235.867188,2),math.log(260.941406,2),math.log(265.763672,2),math.log(252.391602,2),math.log(248.899414,2),math.log(255.329590,2),math.log(272.658081,2),math.log(302.455688,2),math.log(283.665771,2)]
t_78 = [math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(260.000000,2),math.log(239.000000,2),math.log(296.000000,2),math.log(264.500000,2),math.log(262.250000,2),math.log(279.625000,2),math.log(292.875000,2),math.log(279.609375,2),math.log(271.265625,2),math.log(266.812500,2),math.log(231.654297,2),math.log(238.458984,2),math.log(217.545898,2),math.log(249.442383,2),math.log(256.470581,2),math.log(274.239746,2),math.log(279.985107,2)]
t_79 = [math.log(240.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(228.000000,2),math.log(266.000000,2),math.log(262.250000,2),math.log(272.125000,2),math.log(285.437500,2),math.log(300.156250,2),math.log(276.531250,2),math.log(278.812500,2),math.log(271.761719,2),math.log(278.242188,2),math.log(257.301758,2),math.log(260.131836,2),math.log(255.152588,2),math.log(271.661621,2),math.log(256.056763,2),math.log(236.425354,2)]
t_80 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(217.000000,2),math.log(255.500000,2),math.log(257.750000,2),math.log(245.750000,2),math.log(251.500000,2),math.log(235.937500,2),math.log(236.062500,2),math.log(240.289062,2),math.log(279.867188,2),math.log(255.890625,2),math.log(266.833008,2),math.log(266.824219,2),math.log(282.489258,2),math.log(231.463989,2),math.log(257.796814,2),math.log(261.565735,2)]
t_81 = [math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(216.500000,2),math.log(233.750000,2),math.log(217.875000,2),math.log(221.250000,2),math.log(214.437500,2),math.log(209.406250,2),math.log(220.492188,2),math.log(272.281250,2),math.log(239.759766,2),math.log(273.707031,2),math.log(230.371094,2),math.log(259.564941,2),math.log(270.346680,2),math.log(279.890686,2),math.log(293.316498,2)]
t_82 = [math.log(240.000000,2),math.log(232.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(222.000000,2),math.log(252.000000,2),math.log(238.250000,2),math.log(268.375000,2),math.log(259.687500,2),math.log(243.562500,2),math.log(225.968750,2),math.log(236.531250,2),math.log(257.945312,2),math.log(298.806641,2),math.log(270.352539,2),math.log(251.468262,2),math.log(315.919922,2),math.log(248.910278,2),math.log(267.602112,2),math.log(255.146271,2)]
t_83 = [math.log(272.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(268.500000,2),math.log(265.750000,2),math.log(255.875000,2),math.log(257.312500,2),math.log(213.281250,2),math.log(210.812500,2),math.log(234.632812,2),math.log(249.160156,2),math.log(226.867188,2),math.log(215.239258,2),math.log(228.059570,2),math.log(248.258545,2),math.log(239.600342,2),math.log(202.226440,2),math.log(248.399994,2)]
t_84 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(238.000000,2),math.log(259.000000,2),math.log(266.500000,2),math.log(268.250000,2),math.log(319.750000,2),math.log(274.562500,2),math.log(255.250000,2),math.log(231.375000,2),math.log(199.609375,2),math.log(233.367188,2),math.log(245.392578,2),math.log(253.823242,2),math.log(262.552734,2),math.log(239.580811,2),math.log(251.220947,2),math.log(238.976379,2),math.log(269.393799,2)]
t_85 = [math.log(256.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(261.000000,2),math.log(236.500000,2),math.log(238.000000,2),math.log(249.125000,2),math.log(263.875000,2),math.log(284.031250,2),math.log(273.171875,2),math.log(253.125000,2),math.log(297.648438,2),math.log(263.205078,2),math.log(257.026367,2),math.log(232.157715,2),math.log(253.881104,2),math.log(245.336060,2),math.log(237.475098,2),math.log(245.500793,2)]
t_86 = [math.log(256.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(245.000000,2),math.log(242.000000,2),math.log(223.000000,2),math.log(214.625000,2),math.log(255.687500,2),math.log(266.000000,2),math.log(255.703125,2),math.log(264.960938,2),math.log(264.988281,2),math.log(239.355469,2),math.log(247.929688,2),math.log(226.974121,2),math.log(249.882812,2),math.log(249.235229,2),math.log(277.072571,2),math.log(292.761108,2)]
t_87 = [math.log(288.000000,2),math.log(304.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(254.500000,2),math.log(240.000000,2),math.log(255.187500,2),math.log(257.656250,2),math.log(259.671875,2),math.log(265.382812,2),math.log(262.625000,2),math.log(240.412109,2),math.log(267.667969,2),math.log(264.058105,2),math.log(289.008057,2),math.log(239.094604,2),math.log(251.480835,2),math.log(252.452606,2)]
t_88 = [math.log(272.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(283.000000,2),math.log(286.500000,2),math.log(275.750000,2),math.log(273.500000,2),math.log(267.687500,2),math.log(225.000000,2),math.log(227.546875,2),math.log(238.015625,2),math.log(266.859375,2),math.log(266.173828,2),math.log(220.930664,2),math.log(241.677246,2),math.log(246.093262,2),math.log(255.197632,2),math.log(287.395325,2),math.log(274.376251,2)]
t_89 = [math.log(240.000000,2),math.log(248.000000,2),math.log(300.000000,2),math.log(272.000000,2),math.log(289.000000,2),math.log(277.500000,2),math.log(232.000000,2),math.log(204.625000,2),math.log(213.062500,2),math.log(212.250000,2),math.log(254.765625,2),math.log(234.937500,2),math.log(207.015625,2),math.log(218.462891,2),math.log(269.324219,2),math.log(242.056152,2),math.log(238.078857,2),math.log(228.947876,2),math.log(265.589111,2),math.log(231.119904,2)]
t_90 = [math.log(256.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(234.000000,2),math.log(237.000000,2),math.log(247.500000,2),math.log(263.250000,2),math.log(267.125000,2),math.log(289.687500,2),math.log(237.562500,2),math.log(263.421875,2),math.log(237.937500,2),math.log(253.582031,2),math.log(248.070312,2),math.log(251.441406,2),math.log(263.604492,2),math.log(250.210449,2),math.log(261.106445,2),math.log(259.622620,2),math.log(284.833191,2)]
t_91 = [math.log(272.000000,2),math.log(256.000000,2),math.log(228.000000,2),math.log(210.000000,2),math.log(237.000000,2),math.log(235.000000,2),math.log(217.000000,2),math.log(265.625000,2),math.log(256.187500,2),math.log(235.812500,2),math.log(270.609375,2),math.log(253.515625,2),math.log(263.074219,2),math.log(267.203125,2),math.log(226.112305,2),math.log(230.382324,2),math.log(233.987793,2),math.log(264.849976,2),math.log(227.750366,2),math.log(326.195221,2)]
t_92 = [math.log(240.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(278.000000,2),math.log(261.000000,2),math.log(255.000000,2),math.log(218.500000,2),math.log(258.500000,2),math.log(269.812500,2),math.log(247.593750,2),math.log(268.328125,2),math.log(220.304688,2),math.log(222.015625,2),math.log(247.583984,2),math.log(275.086914,2),math.log(281.986328,2),math.log(263.759277,2),math.log(270.027832,2),math.log(272.033203,2),math.log(267.485016,2)]
t_93 = [math.log(368.000000,2),math.log(312.000000,2),math.log(244.000000,2),math.log(238.000000,2),math.log(232.000000,2),math.log(275.500000,2),math.log(279.750000,2),math.log(222.125000,2),math.log(273.437500,2),math.log(294.031250,2),math.log(276.671875,2),math.log(256.648438,2),math.log(258.843750,2),math.log(233.005859,2),math.log(260.511719,2),math.log(275.845215,2),math.log(278.899170,2),math.log(291.078247,2),math.log(268.879089,2),math.log(287.617432,2)]
t_94 = [math.log(240.000000,2),math.log(320.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(228.000000,2),math.log(220.000000,2),math.log(228.500000,2),math.log(213.375000,2),math.log(236.875000,2),math.log(247.812500,2),math.log(270.171875,2),math.log(254.367188,2),math.log(257.691406,2),math.log(284.859375,2),math.log(274.134766,2),math.log(269.303223,2),math.log(272.447021,2),math.log(288.958008,2),math.log(301.547607,2),math.log(288.421356,2)]
t_95 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(260.500000,2),math.log(260.000000,2),math.log(250.250000,2),math.log(255.625000,2),math.log(207.656250,2),math.log(270.703125,2),math.log(244.679688,2),math.log(285.277344,2),math.log(306.912109,2),math.log(287.391602,2),math.log(330.515137,2),math.log(295.844971,2),math.log(253.850464,2),math.log(286.438110,2),math.log(310.744110,2)]
t_96 = [math.log(288.000000,2),math.log(296.000000,2),math.log(260.000000,2),math.log(252.000000,2),math.log(257.000000,2),math.log(246.500000,2),math.log(230.000000,2),math.log(233.750000,2),math.log(226.937500,2),math.log(238.250000,2),math.log(232.765625,2),math.log(246.781250,2),math.log(253.960938,2),math.log(217.976562,2),math.log(221.573242,2),math.log(226.853516,2),math.log(249.569092,2),math.log(266.558472,2),math.log(336.099609,2),math.log(279.260284,2)]
t_97 = [math.log(224.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(242.000000,2),math.log(261.250000,2),math.log(225.250000,2),math.log(253.375000,2),math.log(226.781250,2),math.log(212.703125,2),math.log(232.085938,2),math.log(233.562500,2),math.log(210.945312,2),math.log(236.915039,2),math.log(230.823242,2),math.log(226.906494,2),math.log(221.243408,2),math.log(229.061035,2),math.log(253.078033,2)]
t_98 = [math.log(256.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(271.000000,2),math.log(239.000000,2),math.log(250.750000,2),math.log(269.375000,2),math.log(278.562500,2),math.log(265.031250,2),math.log(290.828125,2),math.log(258.664062,2),math.log(278.511719,2),math.log(262.779297,2),math.log(247.229492,2),math.log(220.904785,2),math.log(231.421631,2),math.log(244.051392,2),math.log(245.705566,2),math.log(282.557251,2)]
t_99 = [math.log(304.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(262.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(271.500000,2),math.log(235.625000,2),math.log(230.687500,2),math.log(223.281250,2),math.log(239.125000,2),math.log(253.000000,2),math.log(256.144531,2),math.log(264.603516,2),math.log(294.403320,2),math.log(281.732910,2),math.log(256.322998,2),math.log(264.670288,2),math.log(302.844971,2),math.log(248.673401,2)]
t_100 = [math.log(240.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(210.000000,2),math.log(223.000000,2),math.log(231.000000,2),math.log(285.250000,2),math.log(326.500000,2),math.log(317.000000,2),math.log(306.312500,2),math.log(245.859375,2),math.log(207.757812,2),math.log(230.328125,2),math.log(224.832031,2),math.log(234.056641,2),math.log(231.161621,2),math.log(180.257812,2),math.log(198.463379,2),math.log(221.576660,2),math.log(232.119904,2)]
t_101 = [math.log(272.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(212.000000,2),math.log(242.000000,2),math.log(238.500000,2),math.log(252.750000,2),math.log(250.125000,2),math.log(235.937500,2),math.log(218.468750,2),math.log(261.984375,2),math.log(300.984375,2),math.log(279.035156,2),math.log(311.976562,2),math.log(300.655273,2),math.log(253.474121,2),math.log(233.865234,2),math.log(221.985107,2),math.log(223.211304,2),math.log(232.157227,2)]
t_102 = [math.log(224.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(244.500000,2),math.log(223.250000,2),math.log(201.750000,2),math.log(235.750000,2),math.log(241.250000,2),math.log(280.625000,2),math.log(279.164062,2),math.log(283.148438,2),math.log(248.609375,2),math.log(222.748047,2),math.log(267.561035,2),math.log(250.712646,2),math.log(263.289185,2),math.log(294.504028,2),math.log(275.103851,2)]
t_103 = [math.log(256.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(246.000000,2),math.log(230.000000,2),math.log(226.000000,2),math.log(217.500000,2),math.log(233.375000,2),math.log(236.750000,2),math.log(237.062500,2),math.log(213.828125,2),math.log(235.460938,2),math.log(260.558594,2),math.log(253.513672,2),math.log(258.113281,2),math.log(277.417480,2),math.log(262.885986,2),math.log(257.095703,2),math.log(275.325500,2),math.log(273.287872,2)]
t_104 = [math.log(240.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(276.000000,2),math.log(226.000000,2),math.log(255.250000,2),math.log(279.125000,2),math.log(270.750000,2),math.log(258.593750,2),math.log(261.906250,2),math.log(273.812500,2),math.log(258.656250,2),math.log(242.984375,2),math.log(255.601562,2),math.log(257.733887,2),math.log(262.003662,2),math.log(262.768555,2),math.log(268.195862,2),math.log(270.730560,2)]
t_105 = [math.log(256.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(262.000000,2),math.log(286.000000,2),math.log(299.500000,2),math.log(258.000000,2),math.log(225.125000,2),math.log(257.687500,2),math.log(242.500000,2),math.log(277.796875,2),math.log(265.296875,2),math.log(254.511719,2),math.log(261.306641,2),math.log(263.124023,2),math.log(283.835449,2),math.log(240.490723,2),math.log(255.576050,2),math.log(253.350220,2),math.log(235.656464,2)]
t_106 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(212.000000,2),math.log(251.000000,2),math.log(244.000000,2),math.log(254.500000,2),math.log(268.875000,2),math.log(235.218750,2),math.log(278.984375,2),math.log(253.453125,2),math.log(217.140625,2),math.log(242.882812,2),math.log(236.707031,2),math.log(251.223633,2),math.log(280.240723,2),math.log(269.516113,2),math.log(277.569031,2),math.log(260.697021,2)]
t_107 = [math.log(240.000000,2),math.log(264.000000,2),math.log(292.000000,2),math.log(318.000000,2),math.log(292.000000,2),math.log(282.500000,2),math.log(299.000000,2),math.log(293.875000,2),math.log(258.500000,2),math.log(267.718750,2),math.log(250.890625,2),math.log(240.914062,2),math.log(249.691406,2),math.log(255.984375,2),math.log(246.170898,2),math.log(311.332520,2),math.log(248.094727,2),math.log(308.641479,2),math.log(282.020264,2),math.log(278.708008,2)]
t_108 = [math.log(240.000000,2),math.log(232.000000,2),math.log(208.000000,2),math.log(262.000000,2),math.log(271.000000,2),math.log(270.000000,2),math.log(270.250000,2),math.log(267.500000,2),math.log(262.437500,2),math.log(305.750000,2),math.log(254.296875,2),math.log(283.445312,2),math.log(268.140625,2),math.log(247.935547,2),math.log(249.837891,2),math.log(257.327637,2),math.log(289.589355,2),math.log(301.227173,2),math.log(279.296021,2),math.log(273.688965,2)]
t_109 = [math.log(256.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(268.000000,2),math.log(269.000000,2),math.log(269.000000,2),math.log(236.000000,2),math.log(271.875000,2),math.log(259.375000,2),math.log(281.812500,2),math.log(263.765625,2),math.log(286.664062,2),math.log(271.617188,2),math.log(252.070312,2),math.log(234.520508,2),math.log(264.452148,2),math.log(261.678467,2),math.log(269.484985,2),math.log(246.606934,2),math.log(303.111420,2)]
t_110 = [math.log(224.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(263.000000,2),math.log(293.000000,2),math.log(267.250000,2),math.log(243.875000,2),math.log(294.687500,2),math.log(255.437500,2),math.log(276.328125,2),math.log(257.664062,2),math.log(265.742188,2),math.log(287.681641,2),math.log(277.368164,2),math.log(269.967285,2),math.log(278.902100,2),math.log(279.455688,2),math.log(288.032104,2),math.log(284.381012,2)]
t_111 = [math.log(240.000000,2),math.log(272.000000,2),math.log(300.000000,2),math.log(288.000000,2),math.log(267.000000,2),math.log(248.000000,2),math.log(239.000000,2),math.log(223.750000,2),math.log(220.500000,2),math.log(242.937500,2),math.log(250.125000,2),math.log(231.960938,2),math.log(252.382812,2),math.log(239.494141,2),math.log(236.228516,2),math.log(246.195312,2),math.log(254.452148,2),math.log(264.899414,2),math.log(250.042480,2),math.log(253.164673,2)]
t_112 = [math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(271.000000,2),math.log(239.500000,2),math.log(269.750000,2),math.log(274.250000,2),math.log(246.687500,2),math.log(237.515625,2),math.log(225.140625,2),math.log(270.617188,2),math.log(285.052734,2),math.log(254.285156,2),math.log(269.590332,2),math.log(230.465820,2),math.log(253.924805,2),math.log(241.861572,2),math.log(281.110992,2)]
t_113 = [math.log(272.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(272.500000,2),math.log(296.500000,2),math.log(271.625000,2),math.log(253.375000,2),math.log(251.031250,2),math.log(267.953125,2),math.log(308.257812,2),math.log(298.679688,2),math.log(285.935547,2),math.log(287.743164,2),math.log(268.926270,2),math.log(251.788818,2),math.log(254.977783,2),math.log(247.986328,2),math.log(242.695648,2)]
t_114 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(243.000000,2),math.log(277.000000,2),math.log(305.500000,2),math.log(298.750000,2),math.log(276.062500,2),math.log(280.125000,2),math.log(264.375000,2),math.log(229.843750,2),math.log(234.097656,2),math.log(237.728516,2),math.log(265.690430,2),math.log(278.787109,2),math.log(240.857910,2),math.log(220.894287,2),math.log(232.202271,2),math.log(260.403320,2)]
t_115 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(298.000000,2),math.log(312.000000,2),math.log(241.500000,2),math.log(277.500000,2),math.log(246.375000,2),math.log(244.562500,2),math.log(229.062500,2),math.log(224.968750,2),math.log(258.468750,2),math.log(253.832031,2),math.log(246.150391,2),math.log(251.990234,2),math.log(270.205078,2),math.log(244.017090,2),math.log(277.214844,2),math.log(310.885315,2),math.log(309.916626,2)]
t_116 = [math.log(240.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(262.000000,2),math.log(246.000000,2),math.log(250.500000,2),math.log(251.750000,2),math.log(283.625000,2),math.log(267.562500,2),math.log(280.156250,2),math.log(251.343750,2),math.log(264.984375,2),math.log(250.058594,2),math.log(239.398438,2),math.log(254.362305,2),math.log(227.934082,2),math.log(243.850342,2),math.log(241.331543,2),math.log(258.831055,2),math.log(242.820251,2)]
t_117 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(222.000000,2),math.log(237.000000,2),math.log(242.500000,2),math.log(247.750000,2),math.log(248.000000,2),math.log(259.062500,2),math.log(272.843750,2),math.log(258.046875,2),math.log(246.367188,2),math.log(259.031250,2),math.log(238.826172,2),math.log(258.795898,2),math.log(247.758301,2),math.log(262.646484,2),math.log(264.979614,2),math.log(243.368225,2),math.log(237.747070,2)]
t_118 = [math.log(272.000000,2),math.log(264.000000,2),math.log(232.000000,2),math.log(280.000000,2),math.log(235.000000,2),math.log(233.500000,2),math.log(271.000000,2),math.log(270.375000,2),math.log(279.750000,2),math.log(247.656250,2),math.log(264.234375,2),math.log(250.179688,2),math.log(238.417969,2),math.log(259.851562,2),math.log(279.200195,2),math.log(290.357910,2),math.log(287.913086,2),math.log(276.325195,2),math.log(256.405151,2),math.log(248.324768,2)]
t_119 = [math.log(256.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(214.000000,2),math.log(252.500000,2),math.log(243.500000,2),math.log(242.000000,2),math.log(259.625000,2),math.log(264.031250,2),math.log(255.328125,2),math.log(285.820312,2),math.log(248.632812,2),math.log(285.302734,2),math.log(252.939453,2),math.log(280.124023,2),math.log(262.300049,2),math.log(280.092896,2),math.log(272.766541,2),math.log(303.595917,2)]
t_120 = [math.log(240.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(250.000000,2),math.log(291.000000,2),math.log(275.500000,2),math.log(216.000000,2),math.log(214.125000,2),math.log(215.562500,2),math.log(205.906250,2),math.log(230.656250,2),math.log(255.519531,2),math.log(260.238281,2),math.log(285.498047,2),math.log(313.343750,2),math.log(307.761963,2),math.log(280.521851,2),math.log(249.714478,2),math.log(270.450317,2)]
t_121 = [math.log(240.000000,2),math.log(224.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(290.000000,2),math.log(289.000000,2),math.log(269.500000,2),math.log(254.750000,2),math.log(245.500000,2),math.log(284.625000,2),math.log(287.906250,2),math.log(285.937500,2),math.log(264.421875,2),math.log(259.123047,2),math.log(290.017578,2),math.log(256.663086,2),math.log(269.043213,2),math.log(302.167480,2),math.log(304.673645,2),math.log(273.459717,2)]
t_122 = [math.log(224.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(230.000000,2),math.log(257.000000,2),math.log(241.000000,2),math.log(248.250000,2),math.log(276.250000,2),math.log(283.687500,2),math.log(290.031250,2),math.log(256.437500,2),math.log(224.023438,2),math.log(240.417969,2),math.log(253.160156,2),math.log(230.572266,2),math.log(236.267090,2),math.log(262.932129,2),math.log(273.064453,2),math.log(325.261414,2),math.log(371.696167,2)]
t_123 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(221.000000,2),math.log(208.000000,2),math.log(222.750000,2),math.log(224.625000,2),math.log(230.875000,2),math.log(232.625000,2),math.log(235.109375,2),math.log(242.601562,2),math.log(260.722656,2),math.log(272.583984,2),math.log(255.208008,2),math.log(276.394531,2),math.log(238.235352,2),math.log(268.336426,2),math.log(270.473389,2),math.log(257.898041,2)]
t_124 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(249.000000,2),math.log(246.000000,2),math.log(231.500000,2),math.log(264.375000,2),math.log(261.062500,2),math.log(264.031250,2),math.log(288.109375,2),math.log(281.265625,2),math.log(263.234375,2),math.log(261.117188,2),math.log(245.651367,2),math.log(248.246582,2),math.log(262.201172,2),math.log(267.994141,2),math.log(251.561890,2),math.log(259.886841,2)]
t_125 = [math.log(256.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(240.000000,2),math.log(251.000000,2),math.log(219.000000,2),math.log(239.750000,2),math.log(255.250000,2),math.log(249.437500,2),math.log(244.093750,2),math.log(274.375000,2),math.log(262.375000,2),math.log(247.777344,2),math.log(280.687500,2),math.log(239.416992,2),math.log(233.785156,2),math.log(207.421143,2),math.log(216.267334,2),math.log(201.508423,2),math.log(246.384521,2)]
t_126 = [math.log(240.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(270.000000,2),math.log(281.000000,2),math.log(301.000000,2),math.log(281.750000,2),math.log(279.500000,2),math.log(258.750000,2),math.log(278.468750,2),math.log(293.320312,2),math.log(278.566406,2),math.log(280.488281,2),math.log(263.184570,2),math.log(275.406738,2),math.log(250.334229,2),math.log(250.692383,2),math.log(270.569031,2),math.log(272.614563,2)]
t_127 = [math.log(256.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(226.000000,2),math.log(222.375000,2),math.log(239.312500,2),math.log(241.406250,2),math.log(243.546875,2),math.log(255.617188,2),math.log(282.363281,2),math.log(269.748047,2),math.log(280.459961,2),math.log(261.697754,2),math.log(256.029541,2),math.log(267.183594,2),math.log(267.227478,2),math.log(287.524963,2)]
t_128 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(270.000000,2),math.log(271.500000,2),math.log(277.000000,2),math.log(274.000000,2),math.log(265.062500,2),math.log(257.750000,2),math.log(253.265625,2),math.log(259.140625,2),math.log(252.148438,2),math.log(270.058594,2),math.log(254.733398,2),math.log(244.968750,2),math.log(257.736572,2),math.log(254.310547,2),math.log(255.313599,2),math.log(265.182098,2)]
t_129 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(284.000000,2),math.log(238.000000,2),math.log(248.000000,2),math.log(251.000000,2),math.log(241.000000,2),math.log(265.687500,2),math.log(281.343750,2),math.log(241.187500,2),math.log(246.468750,2),math.log(226.339844,2),math.log(223.912109,2),math.log(262.292969,2),math.log(224.841797,2),math.log(206.364258,2),math.log(224.984375,2),math.log(237.009094,2),math.log(234.345795,2)]
t_130 = [math.log(256.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(220.000000,2),math.log(259.000000,2),math.log(270.500000,2),math.log(287.250000,2),math.log(259.500000,2),math.log(237.187500,2),math.log(241.062500,2),math.log(232.796875,2),math.log(244.398438,2),math.log(264.625000,2),math.log(278.640625,2),math.log(255.770508,2),math.log(236.824219,2),math.log(250.340820,2),math.log(295.715942,2),math.log(256.964172,2),math.log(246.827484,2)]
t_131 = [math.log(256.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(243.000000,2),math.log(236.500000,2),math.log(247.250000,2),math.log(254.250000,2),math.log(252.437500,2),math.log(212.937500,2),math.log(237.296875,2),math.log(230.320312,2),math.log(221.304688,2),math.log(218.636719,2),math.log(216.701172,2),math.log(227.032715,2),math.log(235.499023,2),math.log(216.290283,2),math.log(258.859863,2),math.log(297.822571,2)]
t_132 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(230.000000,2),math.log(250.000000,2),math.log(246.500000,2),math.log(221.500000,2),math.log(198.000000,2),math.log(198.125000,2),math.log(227.156250,2),math.log(227.281250,2),math.log(226.656250,2),math.log(217.941406,2),math.log(227.191406,2),math.log(219.229492,2),math.log(193.713379,2),math.log(242.792969,2),math.log(291.537964,2),math.log(276.131226,2),math.log(277.528473,2)]
t_133 = [math.log(304.000000,2),math.log(296.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(258.000000,2),math.log(255.000000,2),math.log(238.250000,2),math.log(269.750000,2),math.log(270.062500,2),math.log(286.156250,2),math.log(268.953125,2),math.log(243.359375,2),math.log(248.906250,2),math.log(267.757812,2),math.log(255.676758,2),math.log(251.669922,2),math.log(265.593262,2),math.log(248.180908,2),math.log(255.149170,2),math.log(261.451721,2)]
t_134 = [math.log(224.000000,2),math.log(232.000000,2),math.log(300.000000,2),math.log(270.000000,2),math.log(271.000000,2),math.log(270.000000,2),math.log(275.250000,2),math.log(277.000000,2),math.log(268.062500,2),math.log(242.656250,2),math.log(258.187500,2),math.log(238.679688,2),math.log(215.890625,2),math.log(228.671875,2),math.log(259.911133,2),math.log(268.194336,2),math.log(288.206055,2),math.log(249.320190,2),math.log(256.875061,2),math.log(307.030426,2)]
t_135 = [math.log(240.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(238.000000,2),math.log(246.000000,2),math.log(279.500000,2),math.log(266.750000,2),math.log(236.125000,2),math.log(254.875000,2),math.log(239.343750,2),math.log(250.531250,2),math.log(244.398438,2),math.log(247.816406,2),math.log(223.353516,2),math.log(273.423828,2),math.log(266.801270,2),math.log(305.220215,2),math.log(261.664795,2),math.log(260.969543,2),math.log(293.469849,2)]
t_136 = [math.log(304.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(310.000000,2),math.log(259.000000,2),math.log(251.000000,2),math.log(238.500000,2),math.log(229.625000,2),math.log(267.312500,2),math.log(243.500000,2),math.log(233.203125,2),math.log(275.062500,2),math.log(275.167969,2),math.log(282.820312,2),math.log(221.502930,2),math.log(213.858398,2),math.log(267.534912,2),math.log(271.440552,2),math.log(252.224182,2),math.log(256.577698,2)]
t_137 = [math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(216.000000,2),math.log(255.000000,2),math.log(267.500000,2),math.log(264.250000,2),math.log(243.500000,2),math.log(240.250000,2),math.log(247.312500,2),math.log(244.312500,2),math.log(236.171875,2),math.log(262.070312,2),math.log(267.775391,2),math.log(248.187500,2),math.log(247.715820,2),math.log(234.859863,2),math.log(247.578247,2),math.log(265.251465,2),math.log(227.890625,2)]
t_138 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(256.000000,2),math.log(276.500000,2),math.log(264.500000,2),math.log(294.125000,2),math.log(276.000000,2),math.log(284.468750,2),math.log(283.687500,2),math.log(227.023438,2),math.log(224.851562,2),math.log(261.101562,2),math.log(258.472656,2),math.log(262.884766,2),math.log(314.947021,2),math.log(312.670898,2),math.log(331.149719,2),math.log(289.243439,2)]
t_139 = [math.log(240.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(234.000000,2),math.log(233.000000,2),math.log(232.500000,2),math.log(234.500000,2),math.log(224.625000,2),math.log(229.375000,2),math.log(252.625000,2),math.log(241.687500,2),math.log(268.609375,2),math.log(265.285156,2),math.log(279.007812,2),math.log(261.511719,2),math.log(255.920410,2),math.log(263.581299,2),math.log(246.428833,2),math.log(237.607910,2),math.log(245.700439,2)]
t_140 = [math.log(336.000000,2),math.log(312.000000,2),math.log(296.000000,2),math.log(278.000000,2),math.log(255.000000,2),math.log(233.000000,2),math.log(235.500000,2),math.log(235.125000,2),math.log(232.000000,2),math.log(219.718750,2),math.log(248.312500,2),math.log(261.187500,2),math.log(246.164062,2),math.log(221.216797,2),math.log(235.788086,2),math.log(227.020996,2),math.log(218.596436,2),math.log(244.658325,2),math.log(270.332153,2),math.log(281.901123,2)]
t_141 = [math.log(256.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(246.000000,2),math.log(214.000000,2),math.log(205.500000,2),math.log(246.750000,2),math.log(226.375000,2),math.log(213.687500,2),math.log(195.031250,2),math.log(237.937500,2),math.log(230.812500,2),math.log(249.929688,2),math.log(268.761719,2),math.log(251.530273,2),math.log(223.796387,2),math.log(222.920898,2),math.log(235.787231,2),math.log(254.321594,2),math.log(300.085724,2)]
t_142 = [math.log(272.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(232.000000,2),math.log(245.500000,2),math.log(253.625000,2),math.log(271.000000,2),math.log(277.593750,2),math.log(250.968750,2),math.log(234.718750,2),math.log(271.339844,2),math.log(263.433594,2),math.log(274.430664,2),math.log(241.784668,2),math.log(240.919189,2),math.log(259.736328,2),math.log(233.146851,2),math.log(282.773010,2)]
t_143 = [math.log(272.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(284.000000,2),math.log(243.000000,2),math.log(285.500000,2),math.log(306.000000,2),math.log(300.000000,2),math.log(257.937500,2),math.log(277.312500,2),math.log(245.671875,2),math.log(271.312500,2),math.log(296.589844,2),math.log(301.728516,2),math.log(282.582031,2),math.log(294.935059,2),math.log(322.802002,2),math.log(259.489258,2),math.log(260.540100,2),math.log(248.385376,2)]
t_144 = [math.log(256.000000,2),math.log(264.000000,2),math.log(300.000000,2),math.log(290.000000,2),math.log(268.000000,2),math.log(307.500000,2),math.log(296.000000,2),math.log(257.375000,2),math.log(227.687500,2),math.log(269.062500,2),math.log(249.343750,2),math.log(239.828125,2),math.log(260.355469,2),math.log(232.390625,2),math.log(213.902344,2),math.log(233.235840,2),math.log(186.706299,2),math.log(217.975464,2),math.log(220.890686,2),math.log(260.396820,2)]
t_145 = [math.log(256.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(216.000000,2),math.log(284.000000,2),math.log(289.500000,2),math.log(254.500000,2),math.log(231.375000,2),math.log(244.625000,2),math.log(259.000000,2),math.log(261.656250,2),math.log(207.320312,2),math.log(215.425781,2),math.log(236.556641,2),math.log(258.174805,2),math.log(236.819824,2),math.log(213.106445,2),math.log(199.108521,2),math.log(245.615967,2),math.log(231.010498,2)]
t_146 = [math.log(240.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(240.000000,2),math.log(213.000000,2),math.log(244.000000,2),math.log(281.500000,2),math.log(240.750000,2),math.log(245.500000,2),math.log(243.687500,2),math.log(290.281250,2),math.log(264.343750,2),math.log(251.238281,2),math.log(239.037109,2),math.log(245.751953,2),math.log(266.566895,2),math.log(253.657471,2),math.log(244.888428,2),math.log(292.859314,2),math.log(281.388916,2)]
t_147 = [math.log(224.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(246.000000,2),math.log(270.000000,2),math.log(238.500000,2),math.log(242.000000,2),math.log(243.750000,2),math.log(288.125000,2),math.log(227.531250,2),math.log(206.187500,2),math.log(242.140625,2),math.log(241.281250,2),math.log(231.603516,2),math.log(204.592773,2),math.log(217.727051,2),math.log(241.333984,2),math.log(260.515747,2),math.log(269.209961,2),math.log(253.571075,2)]
t_148 = [math.log(304.000000,2),math.log(312.000000,2),math.log(296.000000,2),math.log(270.000000,2),math.log(234.000000,2),math.log(284.500000,2),math.log(235.250000,2),math.log(258.750000,2),math.log(264.312500,2),math.log(256.937500,2),math.log(246.312500,2),math.log(223.992188,2),math.log(245.718750,2),math.log(255.638672,2),math.log(270.793945,2),math.log(221.965332,2),math.log(266.652344,2),math.log(224.813599,2),math.log(229.746887,2),math.log(235.786224,2)]
t_149 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(220.000000,2),math.log(202.000000,2),math.log(210.500000,2),math.log(222.750000,2),math.log(223.125000,2),math.log(268.375000,2),math.log(266.656250,2),math.log(280.046875,2),math.log(284.890625,2),math.log(278.347656,2),math.log(303.296875,2),math.log(327.242188,2),math.log(311.450684,2),math.log(277.169922,2),math.log(254.828369,2),math.log(230.108887,2),math.log(252.708984,2)]
t_150 = [math.log(272.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(220.000000,2),math.log(221.000000,2),math.log(256.000000,2),math.log(275.750000,2),math.log(281.375000,2),math.log(264.125000,2),math.log(261.531250,2),math.log(246.640625,2),math.log(260.789062,2),math.log(282.585938,2),math.log(268.892578,2),math.log(304.934570,2),math.log(296.160156,2),math.log(295.297119,2),math.log(275.543091,2),math.log(286.628357,2),math.log(247.381378,2)]
t_151 = [math.log(256.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(246.000000,2),math.log(277.000000,2),math.log(249.000000,2),math.log(253.625000,2),math.log(242.312500,2),math.log(239.812500,2),math.log(242.578125,2),math.log(243.226562,2),math.log(195.875000,2),math.log(209.392578,2),math.log(231.387695,2),math.log(237.780762,2),math.log(306.718994,2),math.log(246.389771,2),math.log(206.589355,2),math.log(247.287567,2)]
t_152 = [math.log(256.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(274.000000,2),math.log(288.000000,2),math.log(275.500000,2),math.log(258.625000,2),math.log(261.250000,2),math.log(262.281250,2),math.log(250.625000,2),math.log(237.492188,2),math.log(248.480469,2),math.log(250.205078,2),math.log(290.833008,2),math.log(291.281738,2),math.log(251.505859,2),math.log(232.519653,2),math.log(273.159668,2),math.log(341.899811,2)]
t_153 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(226.000000,2),math.log(271.000000,2),math.log(244.000000,2),math.log(292.500000,2),math.log(243.875000,2),math.log(279.125000,2),math.log(266.218750,2),math.log(254.656250,2),math.log(242.945312,2),math.log(262.269531,2),math.log(242.029297,2),math.log(261.136719,2),math.log(294.567383,2),math.log(279.249268,2),math.log(274.552734,2),math.log(259.815063,2),math.log(274.270905,2)]
t_154 = [math.log(240.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(278.000000,2),math.log(277.000000,2),math.log(257.500000,2),math.log(235.250000,2),math.log(225.125000,2),math.log(258.812500,2),math.log(279.625000,2),math.log(254.656250,2),math.log(227.796875,2),math.log(260.578125,2),math.log(261.539062,2),math.log(242.146484,2),math.log(262.373535,2),math.log(244.606201,2),math.log(269.142700,2),math.log(337.351929,2),math.log(309.487305,2)]
t_155 = [math.log(272.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(274.000000,2),math.log(268.000000,2),math.log(242.500000,2),math.log(256.250000,2),math.log(239.625000,2),math.log(273.437500,2),math.log(267.468750,2),math.log(246.718750,2),math.log(240.265625,2),math.log(232.964844,2),math.log(236.042969,2),math.log(261.236328,2),math.log(248.763672,2),math.log(277.393555,2),math.log(271.648926,2),math.log(300.066956,2),math.log(272.354309,2)]
t_156 = [math.log(256.000000,2),math.log(240.000000,2),math.log(292.000000,2),math.log(310.000000,2),math.log(262.000000,2),math.log(256.500000,2),math.log(248.000000,2),math.log(244.875000,2),math.log(242.562500,2),math.log(251.656250,2),math.log(259.796875,2),math.log(266.390625,2),math.log(276.582031,2),math.log(271.554688,2),math.log(259.814453,2),math.log(246.192383,2),math.log(264.977051,2),math.log(276.540649,2),math.log(293.562317,2),math.log(275.051208,2)]
t_157 = [math.log(224.000000,2),math.log(216.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(263.000000,2),math.log(257.500000,2),math.log(236.250000,2),math.log(217.625000,2),math.log(243.062500,2),math.log(234.906250,2),math.log(244.562500,2),math.log(250.343750,2),math.log(229.753906,2),math.log(237.187500,2),math.log(224.053711,2),math.log(241.449707,2),math.log(273.888428,2),math.log(282.376587,2),math.log(295.483643,2),math.log(279.371216,2)]
t_158 = [math.log(304.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(254.000000,2),math.log(291.000000,2),math.log(268.500000,2),math.log(277.500000,2),math.log(281.000000,2),math.log(251.500000,2),math.log(254.531250,2),math.log(250.281250,2),math.log(250.039062,2),math.log(247.332031,2),math.log(233.980469,2),math.log(263.874023,2),math.log(261.611816,2),math.log(280.816895,2),math.log(275.673706,2),math.log(302.083801,2),math.log(333.486053,2)]
t_159 = [math.log(272.000000,2),math.log(280.000000,2),math.log(312.000000,2),math.log(324.000000,2),math.log(301.000000,2),math.log(258.000000,2),math.log(263.750000,2),math.log(239.375000,2),math.log(235.312500,2),math.log(239.312500,2),math.log(279.593750,2),math.log(243.984375,2),math.log(239.156250,2),math.log(231.835938,2),math.log(299.248047,2),math.log(257.396973,2),math.log(280.459229,2),math.log(285.160645,2),math.log(262.707336,2),math.log(244.557617,2)]
t_160 = [math.log(224.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(226.000000,2),math.log(234.000000,2),math.log(224.000000,2),math.log(219.250000,2),math.log(252.125000,2),math.log(287.500000,2),math.log(250.781250,2),math.log(286.234375,2),math.log(280.375000,2),math.log(258.304688,2),math.log(256.626953,2),math.log(253.754883,2),math.log(261.249512,2),math.log(261.781738,2),math.log(297.265381,2),math.log(262.909119,2),math.log(265.564758,2)]
t_161 = [math.log(256.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(320.000000,2),math.log(284.000000,2),math.log(274.000000,2),math.log(227.500000,2),math.log(200.875000,2),math.log(216.937500,2),math.log(257.906250,2),math.log(224.984375,2),math.log(245.687500,2),math.log(282.335938,2),math.log(295.060547,2),math.log(270.398438,2),math.log(248.794922,2),math.log(242.864014,2),math.log(275.793579,2),math.log(302.513123,2),math.log(315.484406,2)]
t_162 = [math.log(240.000000,2),math.log(264.000000,2),math.log(308.000000,2),math.log(276.000000,2),math.log(300.000000,2),math.log(285.500000,2),math.log(250.750000,2),math.log(236.125000,2),math.log(224.125000,2),math.log(242.468750,2),math.log(310.796875,2),math.log(274.289062,2),math.log(255.195312,2),math.log(258.550781,2),math.log(299.481445,2),math.log(279.418945,2),math.log(260.935059,2),math.log(239.957764,2),math.log(258.827087,2),math.log(302.752472,2)]
t_163 = [math.log(272.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(256.000000,2),math.log(245.000000,2),math.log(271.000000,2),math.log(237.000000,2),math.log(228.750000,2),math.log(221.812500,2),math.log(240.000000,2),math.log(256.671875,2),math.log(265.578125,2),math.log(267.636719,2),math.log(244.562500,2),math.log(255.268555,2),math.log(288.725098,2),math.log(251.890869,2),math.log(256.503784,2),math.log(252.832092,2),math.log(293.574158,2)]
t_164 = [math.log(224.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(234.000000,2),math.log(258.000000,2),math.log(236.500000,2),math.log(214.625000,2),math.log(232.937500,2),math.log(236.906250,2),math.log(231.937500,2),math.log(265.554688,2),math.log(229.265625,2),math.log(235.273438,2),math.log(254.935547,2),math.log(252.438477,2),math.log(265.531250,2),math.log(240.540039,2),math.log(258.357788,2),math.log(267.007843,2)]
t_165 = [math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(258.000000,2),math.log(248.000000,2),math.log(273.625000,2),math.log(282.125000,2),math.log(277.312500,2),math.log(255.765625,2),math.log(263.867188,2),math.log(259.757812,2),math.log(278.150391,2),math.log(303.743164,2),math.log(242.118164,2),math.log(257.266602,2),math.log(287.048706,2),math.log(291.428894,2),math.log(271.688965,2)]
t_166 = [math.log(240.000000,2),math.log(280.000000,2),math.log(296.000000,2),math.log(248.000000,2),math.log(269.000000,2),math.log(308.500000,2),math.log(270.000000,2),math.log(252.500000,2),math.log(253.687500,2),math.log(231.468750,2),math.log(225.500000,2),math.log(261.343750,2),math.log(291.777344,2),math.log(274.509766,2),math.log(281.832031,2),math.log(264.621582,2),math.log(258.856934,2),math.log(219.491821,2),math.log(255.780273,2),math.log(304.092957,2)]
t_167 = [math.log(256.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(237.000000,2),math.log(217.750000,2),math.log(188.000000,2),math.log(230.781250,2),math.log(246.734375,2),math.log(292.953125,2),math.log(293.832031,2),math.log(306.431641,2),math.log(308.477539,2),math.log(275.131836,2),math.log(251.028076,2),math.log(278.468628,2),math.log(290.304321,2),math.log(301.751282,2)]
t_168 = [math.log(272.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(258.000000,2),math.log(233.000000,2),math.log(249.500000,2),math.log(264.500000,2),math.log(258.000000,2),math.log(248.187500,2),math.log(245.875000,2),math.log(223.062500,2),math.log(253.664062,2),math.log(255.945312,2),math.log(256.740234,2),math.log(239.135742,2),math.log(264.239258,2),math.log(234.610840,2),math.log(254.538086,2),math.log(279.484375,2),math.log(310.109558,2)]
t_169 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(286.000000,2),math.log(287.000000,2),math.log(288.000000,2),math.log(258.500000,2),math.log(274.250000,2),math.log(246.312500,2),math.log(258.937500,2),math.log(267.296875,2),math.log(234.421875,2),math.log(249.710938,2),math.log(247.511719,2),math.log(283.209961,2),math.log(227.609863,2),math.log(234.063477,2),math.log(281.655518,2),math.log(245.242432,2),math.log(299.249329,2)]
t_170 = [math.log(272.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(292.000000,2),math.log(279.000000,2),math.log(259.000000,2),math.log(267.500000,2),math.log(287.250000,2),math.log(286.625000,2),math.log(258.468750,2),math.log(227.593750,2),math.log(230.375000,2),math.log(259.878906,2),math.log(292.746094,2),math.log(290.525391,2),math.log(310.795898,2),math.log(315.529297,2),math.log(298.256104,2),math.log(268.313110,2),math.log(306.322845,2)]
t_171 = [math.log(240.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(257.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(241.375000,2),math.log(218.375000,2),math.log(224.781250,2),math.log(253.125000,2),math.log(244.546875,2),math.log(301.671875,2),math.log(258.380859,2),math.log(247.672852,2),math.log(256.265137,2),math.log(231.506104,2),math.log(251.613159,2),math.log(302.943909,2),math.log(278.400879,2)]
t_172 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(209.500000,2),math.log(254.000000,2),math.log(243.750000,2),math.log(253.375000,2),math.log(268.093750,2),math.log(244.328125,2),math.log(212.453125,2),math.log(232.558594,2),math.log(265.876953,2),math.log(248.102539,2),math.log(281.645020,2),math.log(252.919434,2),math.log(224.340820,2),math.log(272.927795,2),math.log(287.622131,2)]
t_173 = [math.log(272.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(280.000000,2),math.log(265.000000,2),math.log(229.500000,2),math.log(198.250000,2),math.log(199.000000,2),math.log(220.875000,2),math.log(248.593750,2),math.log(241.562500,2),math.log(241.960938,2),math.log(250.714844,2),math.log(219.744141,2),math.log(223.315430,2),math.log(240.273926,2),math.log(252.416016,2),math.log(220.204590,2),math.log(215.860474,2),math.log(272.285736,2)]
t_174 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(262.000000,2),math.log(282.000000,2),math.log(293.500000,2),math.log(257.750000,2),math.log(244.500000,2),math.log(242.750000,2),math.log(237.468750,2),math.log(222.500000,2),math.log(213.875000,2),math.log(234.691406,2),math.log(273.302734,2),math.log(263.967773,2),math.log(245.742188,2),math.log(238.584961,2),math.log(201.810303,2),math.log(239.149658,2),math.log(266.524292,2)]
t_175 = [math.log(256.000000,2),math.log(256.000000,2),math.log(216.000000,2),math.log(210.000000,2),math.log(218.000000,2),math.log(208.000000,2),math.log(203.500000,2),math.log(237.000000,2),math.log(266.375000,2),math.log(275.718750,2),math.log(276.593750,2),math.log(259.601562,2),math.log(256.042969,2),math.log(263.855469,2),math.log(212.072266,2),math.log(212.744629,2),math.log(236.321045,2),math.log(249.496948,2),math.log(257.619812,2),math.log(254.969971,2)]
t_176 = [math.log(256.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(302.000000,2),math.log(236.000000,2),math.log(222.500000,2),math.log(224.250000,2),math.log(229.875000,2),math.log(220.437500,2),math.log(212.968750,2),math.log(196.296875,2),math.log(213.929688,2),math.log(268.863281,2),math.log(228.751953,2),math.log(227.939453,2),math.log(217.965332,2),math.log(226.432129,2),math.log(262.082642,2),math.log(251.861145,2),math.log(260.478729,2)]
t_177 = [math.log(256.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(242.000000,2),math.log(242.000000,2),math.log(247.000000,2),math.log(270.000000,2),math.log(284.750000,2),math.log(287.250000,2),math.log(244.250000,2),math.log(271.781250,2),math.log(238.632812,2),math.log(243.117188,2),math.log(255.785156,2),math.log(271.296875,2),math.log(232.752930,2),math.log(230.377930,2),math.log(207.737427,2),math.log(227.311401,2),math.log(268.910980,2)]
t_178 = [math.log(224.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(224.000000,2),math.log(282.500000,2),math.log(269.500000,2),math.log(244.375000,2),math.log(245.562500,2),math.log(224.437500,2),math.log(215.859375,2),math.log(238.125000,2),math.log(257.738281,2),math.log(278.683594,2),math.log(246.653320,2),math.log(258.067871,2),math.log(279.409912,2),math.log(255.158325,2),math.log(245.593384,2),math.log(280.637604,2)]
t_179 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(294.500000,2),math.log(270.125000,2),math.log(271.687500,2),math.log(291.531250,2),math.log(276.281250,2),math.log(280.210938,2),math.log(259.617188,2),math.log(268.474609,2),math.log(247.141602,2),math.log(265.970703,2),math.log(270.395020,2),math.log(288.293091,2),math.log(315.615051,2),math.log(283.282928,2)]
t_180 = [math.log(288.000000,2),math.log(296.000000,2),math.log(280.000000,2),math.log(278.000000,2),math.log(241.000000,2),math.log(241.000000,2),math.log(240.000000,2),math.log(280.750000,2),math.log(266.250000,2),math.log(231.125000,2),math.log(225.156250,2),math.log(225.539062,2),math.log(238.796875,2),math.log(200.615234,2),math.log(222.584961,2),math.log(253.988281,2),math.log(231.590820,2),math.log(265.017090,2),math.log(246.004395,2),math.log(274.466766,2)]
t_181 = [math.log(224.000000,2),math.log(192.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(246.000000,2),math.log(249.500000,2),math.log(237.250000,2),math.log(229.000000,2),math.log(229.187500,2),math.log(235.500000,2),math.log(232.281250,2),math.log(249.445312,2),math.log(245.066406,2),math.log(268.300781,2),math.log(270.340820,2),math.log(259.919922,2),math.log(247.449219,2),math.log(263.017944,2),math.log(282.543823,2),math.log(296.117706,2)]
t_182 = [math.log(272.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(242.000000,2),math.log(251.000000,2),math.log(231.500000,2),math.log(254.375000,2),math.log(224.187500,2),math.log(266.093750,2),math.log(259.343750,2),math.log(247.609375,2),math.log(256.253906,2),math.log(258.554688,2),math.log(267.230469,2),math.log(257.744629,2),math.log(266.053467,2),math.log(274.670776,2),math.log(269.291931,2),math.log(263.297150,2)]
t_183 = [math.log(272.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(250.000000,2),math.log(242.000000,2),math.log(261.500000,2),math.log(265.500000,2),math.log(246.750000,2),math.log(240.875000,2),math.log(234.656250,2),math.log(262.109375,2),math.log(296.976562,2),math.log(317.792969,2),math.log(282.529297,2),math.log(287.348633,2),math.log(260.275391,2),math.log(249.657959,2),math.log(276.640259,2),math.log(266.486145,2),math.log(243.956482,2)]
t_184 = [math.log(224.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(264.000000,2),math.log(303.000000,2),math.log(268.000000,2),math.log(296.250000,2),math.log(254.250000,2),math.log(271.937500,2),math.log(283.156250,2),math.log(251.078125,2),math.log(254.226562,2),math.log(250.871094,2),math.log(251.853516,2),math.log(250.232422,2),math.log(272.439453,2),math.log(292.874512,2),math.log(274.867188,2),math.log(292.720032,2),math.log(267.744904,2)]
t_185 = [math.log(256.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(253.000000,2),math.log(267.500000,2),math.log(287.750000,2),math.log(250.625000,2),math.log(231.312500,2),math.log(209.093750,2),math.log(231.531250,2),math.log(267.125000,2),math.log(270.742188,2),math.log(274.068359,2),math.log(294.179688,2),math.log(260.496582,2),math.log(266.267090,2),math.log(243.471069,2),math.log(248.047974,2),math.log(272.430206,2)]
t_186 = [math.log(272.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(230.000000,2),math.log(268.000000,2),math.log(237.000000,2),math.log(255.750000,2),math.log(269.000000,2),math.log(253.500000,2),math.log(234.093750,2),math.log(242.171875,2),math.log(236.859375,2),math.log(271.050781,2),math.log(251.046875,2),math.log(277.792969,2),math.log(232.724121,2),math.log(230.772705,2),math.log(252.778076,2),math.log(271.959656,2),math.log(293.076721,2)]
t_187 = [math.log(256.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(251.000000,2),math.log(264.500000,2),math.log(274.000000,2),math.log(272.125000,2),math.log(271.750000,2),math.log(270.031250,2),math.log(277.640625,2),math.log(296.960938,2),math.log(276.156250,2),math.log(263.802734,2),math.log(275.497070,2),math.log(274.638672,2),math.log(240.067383,2),math.log(252.638672,2),math.log(300.135559,2),math.log(277.451477,2)]
t_188 = [math.log(224.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(252.000000,2),math.log(278.000000,2),math.log(262.000000,2),math.log(253.750000,2),math.log(212.875000,2),math.log(238.375000,2),math.log(242.000000,2),math.log(248.359375,2),math.log(256.085938,2),math.log(232.769531,2),math.log(246.341797,2),math.log(239.873047,2),math.log(270.332031,2),math.log(236.489746,2),math.log(240.444824,2),math.log(266.968201,2),math.log(233.291656,2)]
t_189 = [math.log(256.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(254.000000,2),math.log(226.500000,2),math.log(234.000000,2),math.log(254.500000,2),math.log(278.000000,2),math.log(289.406250,2),math.log(277.015625,2),math.log(252.687500,2),math.log(249.843750,2),math.log(274.949219,2),math.log(251.079102,2),math.log(261.814941,2),math.log(293.572510,2),math.log(296.130249,2),math.log(254.849121,2),math.log(255.069702,2)]
t_190 = [math.log(304.000000,2),math.log(304.000000,2),math.log(292.000000,2),math.log(294.000000,2),math.log(244.000000,2),math.log(239.500000,2),math.log(227.250000,2),math.log(264.625000,2),math.log(266.000000,2),math.log(232.593750,2),math.log(219.671875,2),math.log(225.171875,2),math.log(254.898438,2),math.log(261.130859,2),math.log(277.800781,2),math.log(275.761230,2),math.log(270.810303,2),math.log(278.822876,2),math.log(257.007996,2),math.log(261.933075,2)]
t_191 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(238.000000,2),math.log(244.000000,2),math.log(205.000000,2),math.log(217.000000,2),math.log(231.875000,2),math.log(233.937500,2),math.log(279.843750,2),math.log(297.734375,2),math.log(256.500000,2),math.log(266.593750,2),math.log(279.894531,2),math.log(284.897461,2),math.log(242.411133,2),math.log(228.392334,2),math.log(217.864868,2),math.log(286.623901,2),math.log(283.768127,2)]
t_192 = [math.log(240.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(270.000000,2),math.log(240.000000,2),math.log(249.000000,2),math.log(226.750000,2),math.log(250.625000,2),math.log(227.125000,2),math.log(237.000000,2),math.log(230.593750,2),math.log(240.437500,2),math.log(255.617188,2),math.log(277.140625,2),math.log(256.194336,2),math.log(288.303223,2),math.log(284.695557,2),math.log(304.006348,2),math.log(303.627014,2),math.log(298.023712,2)]
t_193 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(292.000000,2),math.log(231.500000,2),math.log(252.500000,2),math.log(228.687500,2),math.log(286.406250,2),math.log(253.421875,2),math.log(219.296875,2),math.log(267.238281,2),math.log(251.298828,2),math.log(243.619141,2),math.log(274.169434,2),math.log(232.775391,2),math.log(272.304688,2),math.log(257.818787,2),math.log(242.975708,2)]
t_194 = [math.log(224.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(252.000000,2),math.log(275.000000,2),math.log(254.000000,2),math.log(253.000000,2),math.log(230.125000,2),math.log(276.125000,2),math.log(235.187500,2),math.log(239.062500,2),math.log(238.125000,2),math.log(257.972656,2),math.log(277.851562,2),math.log(262.755859,2),math.log(248.193359,2),math.log(235.045654,2),math.log(212.946533,2),math.log(233.549561,2),math.log(260.586151,2)]
t_195 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(292.000000,2),math.log(256.500000,2),math.log(254.500000,2),math.log(285.875000,2),math.log(297.625000,2),math.log(246.312500,2),math.log(242.984375,2),math.log(254.523438,2),math.log(243.750000,2),math.log(276.044922,2),math.log(305.921875,2),math.log(255.035645,2),math.log(271.926270,2),math.log(276.034302,2),math.log(309.348450,2),math.log(309.868896,2)]
t_196 = [math.log(288.000000,2),math.log(304.000000,2),math.log(332.000000,2),math.log(294.000000,2),math.log(234.000000,2),math.log(225.000000,2),math.log(265.750000,2),math.log(240.125000,2),math.log(224.687500,2),math.log(246.812500,2),math.log(266.093750,2),math.log(249.554688,2),math.log(233.421875,2),math.log(250.750000,2),math.log(265.742188,2),math.log(243.647461,2),math.log(213.305664,2),math.log(245.711304,2),math.log(270.276062,2),math.log(283.390045,2)]
t_197 = [math.log(272.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(255.000000,2),math.log(258.750000,2),math.log(265.000000,2),math.log(289.062500,2),math.log(283.312500,2),math.log(271.343750,2),math.log(278.695312,2),math.log(241.402344,2),math.log(225.083984,2),math.log(278.199219,2),math.log(265.880859,2),math.log(257.661865,2),math.log(239.237549,2),math.log(247.679382,2),math.log(240.350494,2)]
t_198 = [math.log(288.000000,2),math.log(296.000000,2),math.log(240.000000,2),math.log(242.000000,2),math.log(305.000000,2),math.log(258.500000,2),math.log(244.250000,2),math.log(259.750000,2),math.log(238.250000,2),math.log(240.406250,2),math.log(232.390625,2),math.log(247.289062,2),math.log(297.574219,2),math.log(258.998047,2),math.log(257.686523,2),math.log(254.514648,2),math.log(250.802979,2),math.log(283.536987,2),math.log(338.811707,2),math.log(306.489075,2)]
t_199 = [math.log(240.000000,2),math.log(248.000000,2),math.log(228.000000,2),math.log(260.000000,2),math.log(245.000000,2),math.log(237.000000,2),math.log(214.000000,2),math.log(249.500000,2),math.log(254.875000,2),math.log(223.218750,2),math.log(219.812500,2),math.log(250.593750,2),math.log(262.996094,2),math.log(259.564453,2),math.log(287.494141,2),math.log(286.628906,2),math.log(247.464600,2),math.log(267.650879,2),math.log(269.598938,2),math.log(298.609924,2)]
t_200 = [math.log(224.000000,2),math.log(224.000000,2),math.log(260.000000,2),math.log(220.000000,2),math.log(225.000000,2),math.log(233.500000,2),math.log(269.000000,2),math.log(259.375000,2),math.log(273.000000,2),math.log(239.406250,2),math.log(238.921875,2),math.log(251.570312,2),math.log(255.085938,2),math.log(298.341797,2),math.log(270.763672,2),math.log(262.312500,2),math.log(268.330566,2),math.log(247.113525,2),math.log(218.871216,2),math.log(216.599426,2)]
t_201 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(216.000000,2),math.log(230.000000,2),math.log(229.500000,2),math.log(257.125000,2),math.log(239.750000,2),math.log(248.187500,2),math.log(267.406250,2),math.log(273.492188,2),math.log(295.585938,2),math.log(268.417969,2),math.log(281.665039,2),math.log(240.988281,2),math.log(261.871582,2),math.log(272.744995,2),math.log(299.186279,2),math.log(293.821838,2)]
t_202 = [math.log(240.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(272.000000,2),math.log(277.500000,2),math.log(263.000000,2),math.log(287.250000,2),math.log(264.000000,2),math.log(284.062500,2),math.log(311.937500,2),math.log(307.109375,2),math.log(250.394531,2),math.log(254.783203,2),math.log(291.317383,2),math.log(280.075684,2),math.log(305.177490,2),math.log(342.205566,2),math.log(348.928162,2),math.log(358.187866,2)]
t_203 = [math.log(272.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(280.000000,2),math.log(251.000000,2),math.log(236.000000,2),math.log(243.750000,2),math.log(250.625000,2),math.log(262.687500,2),math.log(275.031250,2),math.log(284.437500,2),math.log(266.796875,2),math.log(257.207031,2),math.log(236.406250,2),math.log(267.068359,2),math.log(255.581543,2),math.log(232.593018,2),math.log(235.307007,2),math.log(261.857849,2),math.log(272.083191,2)]
t_204 = [math.log(240.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(230.000000,2),math.log(245.000000,2),math.log(244.000000,2),math.log(205.750000,2),math.log(225.250000,2),math.log(249.437500,2),math.log(240.656250,2),math.log(236.656250,2),math.log(249.906250,2),math.log(272.007812,2),math.log(260.386719,2),math.log(246.951172,2),math.log(235.415527,2),math.log(252.739258,2),math.log(260.794922,2),math.log(279.899841,2),math.log(287.394226,2)]
t_205 = [math.log(256.000000,2),math.log(232.000000,2),math.log(284.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(228.000000,2),math.log(207.250000,2),math.log(240.125000,2),math.log(234.750000,2),math.log(201.593750,2),math.log(212.656250,2),math.log(246.453125,2),math.log(276.320312,2),math.log(263.666016,2),math.log(299.601562,2),math.log(262.387207,2),math.log(246.796143,2),math.log(220.551880,2),math.log(294.432556,2),math.log(297.828430,2)]
t_206 = [math.log(240.000000,2),math.log(240.000000,2),math.log(296.000000,2),math.log(270.000000,2),math.log(268.000000,2),math.log(235.000000,2),math.log(238.750000,2),math.log(280.625000,2),math.log(286.625000,2),math.log(283.656250,2),math.log(288.187500,2),math.log(283.945312,2),math.log(268.156250,2),math.log(239.654297,2),math.log(230.792969,2),math.log(243.088867,2),math.log(217.560059,2),math.log(224.202515,2),math.log(262.560669,2),math.log(272.625885,2)]
t_207 = [math.log(256.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(250.000000,2),math.log(249.000000,2),math.log(234.500000,2),math.log(250.000000,2),math.log(255.875000,2),math.log(242.937500,2),math.log(241.156250,2),math.log(245.875000,2),math.log(253.109375,2),math.log(241.378906,2),math.log(285.626953,2),math.log(270.590820,2),math.log(256.282227,2),math.log(264.408936,2),math.log(258.609131,2),math.log(263.760010,2),math.log(302.968231,2)]
t_208 = [math.log(256.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(290.000000,2),math.log(273.000000,2),math.log(259.000000,2),math.log(274.250000,2),math.log(282.375000,2),math.log(274.687500,2),math.log(244.812500,2),math.log(265.656250,2),math.log(292.835938,2),math.log(269.683594,2),math.log(239.128906,2),math.log(276.697266,2),math.log(274.768066,2),math.log(267.307373,2),math.log(271.329590,2),math.log(246.058838,2),math.log(264.601074,2)]
t_209 = [math.log(288.000000,2),math.log(280.000000,2),math.log(240.000000,2),math.log(194.000000,2),math.log(224.000000,2),math.log(244.500000,2),math.log(225.500000,2),math.log(227.875000,2),math.log(210.250000,2),math.log(190.500000,2),math.log(214.078125,2),math.log(222.796875,2),math.log(194.875000,2),math.log(213.185547,2),math.log(243.530273,2),math.log(228.083008,2),math.log(247.668457,2),math.log(195.744385,2),math.log(241.841614,2),math.log(236.331421,2)]
t_210 = [math.log(256.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(286.000000,2),math.log(276.000000,2),math.log(257.000000,2),math.log(267.500000,2),math.log(236.125000,2),math.log(224.937500,2),math.log(218.312500,2),math.log(254.312500,2),math.log(289.648438,2),math.log(280.160156,2),math.log(293.619141,2),math.log(276.425781,2),math.log(278.256348,2),math.log(247.295166,2),math.log(245.096313,2),math.log(267.810120,2),math.log(234.783844,2)]
t_211 = [math.log(240.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(258.000000,2),math.log(263.000000,2),math.log(264.000000,2),math.log(259.500000,2),math.log(263.750000,2),math.log(283.625000,2),math.log(278.281250,2),math.log(255.218750,2),math.log(234.492188,2),math.log(281.195312,2),math.log(238.636719,2),math.log(265.432617,2),math.log(241.210449,2),math.log(248.366211,2),math.log(262.160156,2),math.log(240.637878,2),math.log(276.962494,2)]
t_212 = [math.log(240.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(290.000000,2),math.log(240.000000,2),math.log(282.000000,2),math.log(257.750000,2),math.log(237.875000,2),math.log(243.375000,2),math.log(246.437500,2),math.log(239.187500,2),math.log(271.226562,2),math.log(237.929688,2),math.log(212.335938,2),math.log(218.794922,2),math.log(249.504883,2),math.log(264.643311,2),math.log(245.437988,2),math.log(258.932617,2),math.log(244.377197,2)]
t_213 = [math.log(256.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(240.000000,2),math.log(209.000000,2),math.log(245.500000,2),math.log(221.500000,2),math.log(246.250000,2),math.log(242.000000,2),math.log(254.343750,2),math.log(261.515625,2),math.log(270.804688,2),math.log(258.597656,2),math.log(259.373047,2),math.log(235.156250,2),math.log(250.598145,2),math.log(256.428711,2),math.log(281.227417,2),math.log(322.801270,2),math.log(263.160400,2)]
t_214 = [math.log(256.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(246.000000,2),math.log(286.500000,2),math.log(287.000000,2),math.log(259.125000,2),math.log(238.312500,2),math.log(255.312500,2),math.log(218.406250,2),math.log(240.015625,2),math.log(256.703125,2),math.log(260.482422,2),math.log(273.731445,2),math.log(277.523926,2),math.log(270.198486,2),math.log(243.178467,2),math.log(259.412598,2),math.log(314.611572,2)]
t_215 = [math.log(224.000000,2),math.log(216.000000,2),math.log(228.000000,2),math.log(238.000000,2),math.log(227.000000,2),math.log(252.500000,2),math.log(257.250000,2),math.log(266.625000,2),math.log(255.562500,2),math.log(235.968750,2),math.log(285.828125,2),math.log(290.070312,2),math.log(297.187500,2),math.log(254.724609,2),math.log(247.934570,2),math.log(261.176270,2),math.log(291.510742,2),math.log(269.255981,2),math.log(232.513489,2),math.log(240.531433,2)]
t_216 = [math.log(272.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(218.000000,2),math.log(203.000000,2),math.log(221.000000,2),math.log(269.500000,2),math.log(264.625000,2),math.log(265.062500,2),math.log(224.687500,2),math.log(245.453125,2),math.log(260.242188,2),math.log(249.765625,2),math.log(239.460938,2),math.log(238.255859,2),math.log(253.971191,2),math.log(265.660645,2),math.log(226.245972,2),math.log(229.275940,2),math.log(251.680664,2)]
t_217 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(300.000000,2),math.log(263.000000,2),math.log(238.000000,2),math.log(234.250000,2),math.log(244.375000,2),math.log(257.000000,2),math.log(241.500000,2),math.log(277.109375,2),math.log(275.000000,2),math.log(266.230469,2),math.log(271.357422,2),math.log(242.788086,2),math.log(267.410645,2),math.log(284.831543,2),math.log(296.853271,2),math.log(300.263916,2),math.log(246.091156,2)]
t_218 = [math.log(288.000000,2),math.log(320.000000,2),math.log(248.000000,2),math.log(202.000000,2),math.log(231.000000,2),math.log(223.000000,2),math.log(213.500000,2),math.log(219.500000,2),math.log(227.375000,2),math.log(220.906250,2),math.log(218.531250,2),math.log(221.859375,2),math.log(266.691406,2),math.log(244.673828,2),math.log(252.533203,2),math.log(242.758789,2),math.log(249.747803,2),math.log(267.816406,2),math.log(281.260071,2),math.log(275.279205,2)]
t_219 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(234.000000,2),math.log(261.000000,2),math.log(243.500000,2),math.log(235.000000,2),math.log(259.500000,2),math.log(266.250000,2),math.log(284.812500,2),math.log(247.203125,2),math.log(267.781250,2),math.log(286.820312,2),math.log(250.017578,2),math.log(284.788086,2),math.log(242.990234,2),math.log(235.565430,2),math.log(236.211182,2),math.log(242.563782,2),math.log(294.959656,2)]
t_220 = [math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(273.000000,2),math.log(269.500000,2),math.log(257.250000,2),math.log(282.750000,2),math.log(259.437500,2),math.log(301.937500,2),math.log(231.203125,2),math.log(290.921875,2),math.log(269.355469,2),math.log(249.488281,2),math.log(257.806641,2),math.log(249.632812,2),math.log(284.996582,2),math.log(278.549194,2),math.log(263.992554,2),math.log(265.170197,2)]
t_221 = [math.log(288.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(252.000000,2),math.log(298.000000,2),math.log(295.000000,2),math.log(253.000000,2),math.log(252.125000,2),math.log(288.375000,2),math.log(283.500000,2),math.log(292.890625,2),math.log(309.398438,2),math.log(274.144531,2),math.log(283.914062,2),math.log(266.915039,2),math.log(287.428711,2),math.log(280.380371,2),math.log(314.651001,2),math.log(288.934265,2),math.log(283.880157,2)]
t_222 = [math.log(240.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(258.000000,2),math.log(251.000000,2),math.log(266.000000,2),math.log(250.000000,2),math.log(241.750000,2),math.log(235.812500,2),math.log(267.468750,2),math.log(266.484375,2),math.log(272.421875,2),math.log(270.343750,2),math.log(234.916016,2),math.log(252.106445,2),math.log(272.962402,2),math.log(275.344238,2),math.log(279.528564,2),math.log(258.966492,2),math.log(258.856049,2)]
t_223 = [math.log(240.000000,2),math.log(240.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(275.000000,2),math.log(266.000000,2),math.log(289.250000,2),math.log(323.625000,2),math.log(312.625000,2),math.log(298.875000,2),math.log(275.750000,2),math.log(299.171875,2),math.log(268.445312,2),math.log(239.101562,2),math.log(270.826172,2),math.log(259.202637,2),math.log(245.570312,2),math.log(259.430908,2),math.log(247.027039,2),math.log(254.451233,2)]
t_224 = [math.log(256.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(228.000000,2),math.log(208.000000,2),math.log(216.500000,2),math.log(194.500000,2),math.log(228.625000,2),math.log(227.437500,2),math.log(242.687500,2),math.log(227.718750,2),math.log(208.476562,2),math.log(240.519531,2),math.log(265.855469,2),math.log(255.692383,2),math.log(242.403320,2),math.log(235.363281,2),math.log(262.990967,2),math.log(244.220398,2),math.log(297.991119,2)]
t_225 = [math.log(256.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(314.000000,2),math.log(252.000000,2),math.log(259.500000,2),math.log(241.000000,2),math.log(240.375000,2),math.log(267.812500,2),math.log(300.062500,2),math.log(255.750000,2),math.log(246.453125,2),math.log(270.605469,2),math.log(262.070312,2),math.log(220.899414,2),math.log(233.609863,2),math.log(248.968018,2),math.log(239.945435,2),math.log(218.929016,2),math.log(203.096802,2)]
t_226 = [math.log(256.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(230.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(238.500000,2),math.log(228.125000,2),math.log(224.187500,2),math.log(242.343750,2),math.log(241.781250,2),math.log(257.406250,2),math.log(292.378906,2),math.log(274.324219,2),math.log(278.934570,2),math.log(292.331543,2),math.log(231.672852,2),math.log(237.098145,2),math.log(256.170227,2),math.log(251.546631,2)]
t_227 = [math.log(240.000000,2),math.log(232.000000,2),math.log(224.000000,2),math.log(230.000000,2),math.log(202.000000,2),math.log(243.500000,2),math.log(235.500000,2),math.log(263.000000,2),math.log(292.250000,2),math.log(265.750000,2),math.log(248.390625,2),math.log(245.367188,2),math.log(274.730469,2),math.log(248.574219,2),math.log(233.779297,2),math.log(266.536621,2),math.log(258.802002,2),math.log(218.673706,2),math.log(254.024963,2),math.log(273.591339,2)]
t_228 = [math.log(272.000000,2),math.log(272.000000,2),math.log(288.000000,2),math.log(332.000000,2),math.log(302.000000,2),math.log(298.000000,2),math.log(298.500000,2),math.log(321.250000,2),math.log(301.312500,2),math.log(270.531250,2),math.log(260.500000,2),math.log(265.781250,2),math.log(238.683594,2),math.log(233.943359,2),math.log(247.696289,2),math.log(243.294922,2),math.log(264.985352,2),math.log(249.959961,2),math.log(262.421143,2),math.log(284.507507,2)]
t_229 = [math.log(224.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(220.000000,2),math.log(269.000000,2),math.log(248.000000,2),math.log(217.750000,2),math.log(257.750000,2),math.log(253.625000,2),math.log(226.718750,2),math.log(234.390625,2),math.log(219.210938,2),math.log(261.152344,2),math.log(244.130859,2),math.log(273.472656,2),math.log(240.075195,2),math.log(243.306152,2),math.log(263.450928,2),math.log(261.291748,2),math.log(295.680359,2)]
t_230 = [math.log(256.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(235.000000,2),math.log(254.000000,2),math.log(248.250000,2),math.log(240.375000,2),math.log(227.125000,2),math.log(251.968750,2),math.log(245.453125,2),math.log(240.515625,2),math.log(250.585938,2),math.log(237.076172,2),math.log(283.958984,2),math.log(282.647949,2),math.log(265.866455,2),math.log(246.994995,2),math.log(283.425110,2),math.log(262.336456,2)]
t_231 = [math.log(256.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(236.000000,2),math.log(269.000000,2),math.log(295.500000,2),math.log(223.500000,2),math.log(251.375000,2),math.log(254.750000,2),math.log(253.062500,2),math.log(251.734375,2),math.log(264.601562,2),math.log(263.992188,2),math.log(262.271484,2),math.log(243.895508,2),math.log(256.266113,2),math.log(255.939697,2),math.log(265.113159,2),math.log(265.729004,2),math.log(275.734802,2)]
t_232 = [math.log(224.000000,2),math.log(264.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(261.000000,2),math.log(289.500000,2),math.log(242.750000,2),math.log(237.875000,2),math.log(231.000000,2),math.log(251.031250,2),math.log(256.562500,2),math.log(262.695312,2),math.log(280.265625,2),math.log(293.384766,2),math.log(266.727539,2),math.log(261.597168,2),math.log(270.006348,2),math.log(272.164673,2),math.log(259.806702,2),math.log(263.303406,2)]
t_233 = [math.log(336.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(294.000000,2),math.log(291.000000,2),math.log(289.000000,2),math.log(297.250000,2),math.log(289.375000,2),math.log(273.062500,2),math.log(246.375000,2),math.log(257.703125,2),math.log(245.351562,2),math.log(260.148438,2),math.log(267.732422,2),math.log(248.041992,2),math.log(217.742188,2),math.log(233.933838,2),math.log(276.883301,2),math.log(267.075073,2),math.log(230.984070,2)]
t_234 = [math.log(224.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(258.000000,2),math.log(239.000000,2),math.log(260.500000,2),math.log(230.500000,2),math.log(206.125000,2),math.log(211.750000,2),math.log(209.343750,2),math.log(209.125000,2),math.log(235.179688,2),math.log(262.296875,2),math.log(234.515625,2),math.log(257.973633,2),math.log(257.950195,2),math.log(265.364014,2),math.log(237.603271,2),math.log(299.450623,2),math.log(353.826599,2)]
t_235 = [math.log(224.000000,2),math.log(240.000000,2),math.log(224.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(262.000000,2),math.log(259.500000,2),math.log(239.875000,2),math.log(243.125000,2),math.log(252.750000,2),math.log(231.640625,2),math.log(220.718750,2),math.log(236.953125,2),math.log(234.201172,2),math.log(286.954102,2),math.log(262.262695,2),math.log(259.554443,2),math.log(239.922485,2),math.log(234.748901,2),math.log(244.561920,2)]
t_236 = [math.log(272.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(278.000000,2),math.log(254.000000,2),math.log(235.500000,2),math.log(238.250000,2),math.log(239.625000,2),math.log(269.937500,2),math.log(260.468750,2),math.log(255.640625,2),math.log(287.789062,2),math.log(278.238281,2),math.log(297.435547,2),math.log(257.545898,2),math.log(269.666992,2),math.log(289.047363,2),math.log(251.104736,2),math.log(236.050293,2),math.log(263.682251,2)]
t_237 = [math.log(240.000000,2),math.log(272.000000,2),math.log(308.000000,2),math.log(272.000000,2),math.log(283.000000,2),math.log(283.000000,2),math.log(264.500000,2),math.log(231.625000,2),math.log(256.937500,2),math.log(214.250000,2),math.log(232.250000,2),math.log(209.859375,2),math.log(236.945312,2),math.log(263.417969,2),math.log(274.028320,2),math.log(256.523926,2),math.log(201.010010,2),math.log(257.855957,2),math.log(261.732666,2),math.log(277.009979,2)]
t_238 = [math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(250.000000,2),math.log(253.000000,2),math.log(260.500000,2),math.log(260.500000,2),math.log(290.000000,2),math.log(267.187500,2),math.log(260.031250,2),math.log(240.218750,2),math.log(208.687500,2),math.log(216.320312,2),math.log(253.474609,2),math.log(258.902344,2),math.log(287.265625,2),math.log(246.447998,2),math.log(247.522339,2),math.log(252.895752,2),math.log(266.830658,2)]
t_239 = [math.log(256.000000,2),math.log(288.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(313.000000,2),math.log(285.500000,2),math.log(271.250000,2),math.log(235.875000,2),math.log(254.468750,2),math.log(264.125000,2),math.log(270.750000,2),math.log(244.957031,2),math.log(226.027344,2),math.log(255.993164,2),math.log(292.055664,2),math.log(257.847900,2),math.log(249.578003,2),math.log(238.722595,2),math.log(271.940216,2)]
t_240 = [math.log(256.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(255.000000,2),math.log(245.000000,2),math.log(227.000000,2),math.log(236.000000,2),math.log(218.000000,2),math.log(213.750000,2),math.log(231.296875,2),math.log(243.101562,2),math.log(274.457031,2),math.log(251.736328,2),math.log(235.344727,2),math.log(246.153809,2),math.log(250.792480,2),math.log(267.306519,2),math.log(275.346130,2),math.log(294.085266,2)]
t_241 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(280.000000,2),math.log(267.000000,2),math.log(269.000000,2),math.log(255.000000,2),math.log(267.375000,2),math.log(258.625000,2),math.log(234.375000,2),math.log(218.179688,2),math.log(224.261719,2),math.log(254.115234,2),math.log(244.620117,2),math.log(267.098145,2),math.log(264.926270,2),math.log(238.466431,2),math.log(251.358276,2),math.log(290.280121,2)]
t_242 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(283.000000,2),math.log(245.000000,2),math.log(269.000000,2),math.log(287.000000,2),math.log(249.125000,2),math.log(246.187500,2),math.log(213.781250,2),math.log(244.718750,2),math.log(222.070312,2),math.log(211.568359,2),math.log(234.405273,2),math.log(246.727051,2),math.log(248.666260,2),math.log(251.678467,2),math.log(283.136658,2),math.log(268.389801,2)]
t_243 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(265.000000,2),math.log(268.250000,2),math.log(222.750000,2),math.log(219.625000,2),math.log(264.562500,2),math.log(262.890625,2),math.log(247.375000,2),math.log(253.812500,2),math.log(252.375000,2),math.log(232.186523,2),math.log(229.842285,2),math.log(270.596191,2),math.log(279.740479,2),math.log(277.053711,2),math.log(265.072693,2)]
t_244 = [math.log(272.000000,2),math.log(288.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(268.000000,2),math.log(268.500000,2),math.log(256.500000,2),math.log(274.875000,2),math.log(278.562500,2),math.log(284.093750,2),math.log(256.890625,2),math.log(259.617188,2),math.log(259.664062,2),math.log(247.406250,2),math.log(262.318359,2),math.log(274.996582,2),math.log(272.938232,2),math.log(277.090576,2),math.log(277.974731,2),math.log(255.105927,2)]
t_245 = [math.log(256.000000,2),math.log(232.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(250.500000,2),math.log(234.000000,2),math.log(272.125000,2),math.log(289.937500,2),math.log(271.406250,2),math.log(259.640625,2),math.log(235.734375,2),math.log(244.625000,2),math.log(251.117188,2),math.log(262.991211,2),math.log(241.171875,2),math.log(244.438965,2),math.log(229.926270,2),math.log(240.915283,2),math.log(278.649963,2)]
t_246 = [math.log(240.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(198.000000,2),math.log(217.000000,2),math.log(238.500000,2),math.log(268.500000,2),math.log(253.500000,2),math.log(247.437500,2),math.log(249.562500,2),math.log(235.937500,2),math.log(225.609375,2),math.log(248.472656,2),math.log(261.025391,2),math.log(296.743164,2),math.log(301.401367,2),math.log(288.694336,2),math.log(263.986328,2),math.log(258.706787,2),math.log(260.659790,2)]
t_247 = [math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(274.000000,2),math.log(280.000000,2),math.log(242.500000,2),math.log(263.500000,2),math.log(246.625000,2),math.log(247.125000,2),math.log(215.562500,2),math.log(253.750000,2),math.log(231.843750,2),math.log(244.402344,2),math.log(245.027344,2),math.log(258.013672,2),math.log(260.749023,2),math.log(294.502197,2),math.log(294.214966,2),math.log(287.693054,2),math.log(286.355286,2)]
t_248 = [math.log(288.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(236.000000,2),math.log(216.000000,2),math.log(228.000000,2),math.log(237.500000,2),math.log(250.750000,2),math.log(279.375000,2),math.log(307.125000,2),math.log(298.781250,2),math.log(294.703125,2),math.log(254.777344,2),math.log(225.994141,2),math.log(276.682617,2),math.log(229.421875,2),math.log(205.051270,2),math.log(262.081909,2),math.log(231.065613,2),math.log(240.633667,2)]
t_249 = [math.log(288.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(254.000000,2),math.log(264.000000,2),math.log(269.000000,2),math.log(223.250000,2),math.log(261.375000,2),math.log(308.125000,2),math.log(290.656250,2),math.log(300.765625,2),math.log(272.570312,2),math.log(233.218750,2),math.log(252.279297,2),math.log(279.679688,2),math.log(243.112305,2),math.log(261.772705,2),math.log(274.617310,2),math.log(275.267090,2),math.log(313.611908,2)]
t_250 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(255.000000,2),math.log(249.500000,2),math.log(246.500000,2),math.log(266.875000,2),math.log(231.562500,2),math.log(240.500000,2),math.log(252.718750,2),math.log(269.734375,2),math.log(260.757812,2),math.log(270.029297,2),math.log(292.603516,2),math.log(281.948730,2),math.log(259.109863,2),math.log(233.657349,2),math.log(254.625793,2),math.log(290.957764,2)]
t_251 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(234.000000,2),math.log(202.000000,2),math.log(225.000000,2),math.log(274.750000,2),math.log(276.625000,2),math.log(284.687500,2),math.log(226.281250,2),math.log(269.812500,2),math.log(257.718750,2),math.log(258.062500,2),math.log(240.328125,2),math.log(250.659180,2),math.log(296.270020,2),math.log(286.395996,2),math.log(294.636230,2),math.log(252.086304,2),math.log(284.339813,2)]
t_252 = [math.log(224.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(245.000000,2),math.log(231.000000,2),math.log(231.750000,2),math.log(238.375000,2),math.log(281.812500,2),math.log(284.406250,2),math.log(248.203125,2),math.log(228.437500,2),math.log(246.804688,2),math.log(275.822266,2),math.log(250.042969,2),math.log(232.844238,2),math.log(243.526855,2),math.log(261.387695,2),math.log(251.375122,2),math.log(275.987946,2)]
t_253 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(267.000000,2),math.log(236.000000,2),math.log(275.000000,2),math.log(268.625000,2),math.log(230.312500,2),math.log(277.281250,2),math.log(262.734375,2),math.log(280.500000,2),math.log(280.359375,2),math.log(257.050781,2),math.log(279.380859,2),math.log(269.846680,2),math.log(270.217529,2),math.log(262.763184,2),math.log(283.278809,2),math.log(281.115723,2)]
t_254 = [math.log(240.000000,2),math.log(248.000000,2),math.log(288.000000,2),math.log(270.000000,2),math.log(292.000000,2),math.log(270.500000,2),math.log(240.250000,2),math.log(263.875000,2),math.log(251.687500,2),math.log(202.187500,2),math.log(249.765625,2),math.log(247.148438,2),math.log(261.804688,2),math.log(271.421875,2),math.log(220.794922,2),math.log(251.607422,2),math.log(268.130371,2),math.log(264.668701,2),math.log(297.139648,2),math.log(253.765106,2)]
t_255 = [math.log(240.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(226.000000,2),math.log(218.000000,2),math.log(232.000000,2),math.log(211.250000,2),math.log(225.625000,2),math.log(259.312500,2),math.log(220.156250,2),math.log(259.421875,2),math.log(256.031250,2),math.log(270.289062,2),math.log(256.328125,2),math.log(256.204102,2),math.log(235.871094,2),math.log(206.800293,2),math.log(223.978394,2),math.log(253.789917,2),math.log(297.855804,2)]




#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00001625
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00001625)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00001625
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00001625)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00001625
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00001625)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00001625
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00001625)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00001625
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00001625)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00001625
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00001625)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00001625
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00001625)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00001625
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00001625)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00001625
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00001625)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00001625
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00001625)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00001625
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00001625)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00001625
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00001625)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00001625
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00001625)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00001625
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00001625)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00001625
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00001625)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00001625
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00001625)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00001625
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00001625)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00001625
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00001625)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00001625
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00001625)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00001625
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00001625)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 9 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
