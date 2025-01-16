# Using numPy to provide descriptive statistics on a large dataset (2,000 values)
import numpy as np
import matplotlib.pyplot as plt


HousePrices=[1059033.558,1505890.915,1058987.988,1260616.807,630943.4893,1068138.074,1502055.817,1573936.564,798869.5328,1545154.813,1707045.722,663732.3969,1042814.098,1291331.518,1402818.21,1306674.66,1556786.6,528485.2467,1019425.937,1030591.429,2146925.34,929247.5995,718887.2315,743999.8192,895737.1334,1453974.506,1125692.507,975429.4928,1240763.766,1577017.76,1246830.188,1170720.894,1071279.21,534305.1323,936368.9634,1199193.831,1233220.009,1081150.125,524712.7661,302355.836,1026817.4,1762214.68,882057.1706,1744932.211,1153871.47,1499988.88,1109588.38,980177.3051,1323952.027,1662494.736,1417819.74,549976.1456,1054770.981,1415647.553,948788.2757,1159596.519,1547133.396,1186688.506,772111.9721,1172730.156,1111085.017,1022781.171,1274474.546,1213530.85,1411730.477,858685.5659,1200961.821,1520234.229,1360908.32,1360920.53,1146532.455,1789098.521,852099.464,746096.7289,1534479.907,1215608.531,941594.3284,1204598.037,1597655.258,1492011.496,1421216.504,1132522.901,1102821.438,1856211.35,1687998.933,1063423.007,1177289.886,1173474.379,1637259.999,1238938.291,201898.0866,1439506.102,585608.6326,1294685.159,2014851.344,1840236.006,1441421.913,1498640.551,954746.5764,1124635.932,1169944.248,1114430.953,1783534.839,1302933.248,1241483.612,954114.544,1555320.5,404976.3659,1073183.76,1422195.879,340605.2113,1170959.526,942838.1647,1401613.92,1175504.486,608794.2467,946943.0362,1819900.637,1463130.273,1252391.18,1714445.175,1291759.393,1809154.289,1200539.361,1300265.21,997448.7281,2152959.409,1629983.847,497579.4466,890112.5493,1064685.699,1530124.016,1246246.828,1240754.932,1760734.69,1393746.76,1172385.898,483986.109,1388530.157,1721739.384,1276448.792,1161742.677,786407.9451,1604920.973,1230149.137,1051644.554,1415073.614,1043483.915,1544379.748,1352135.967,1505727.431,1416965.979,1046721.976,939040.0036,1383031.332,1072503.238,1134397.758,734827.508,991892.3175,1057252.583,1237224.859,1442632.541,1877402.32,1394518.415,953939.3299,1219778.034,1287325.382,1739893.555,1213382.223,1007478.748,1528756.126,1182459.772,1474546.762,1078016.94,1453381.624,1495012.965,714148.4148,894292.0474,1159841.831,1195986.299,1381430.63,1534889.853,1494125.33,1356146.261,1454943.074,774118.1878,889113.2389,1211102.211,658646.1847,1400104.871,1262017.792,553077.2126,1203247.89,1115323.015,1301881.417,1006687.387,749383.0726,1075596.587,739870.7936,1442945.145,828497.0671,1373290.861,925566.3313,1552536.764,1335904.501,960808.2911,1405933.019,619087.6936,1329273.228,1261843.844,1175781.418,1437053.557,1594415.226,931357.9954,798639.6542,1451739.625,1278991.689,885920.5532,1425632.542,901881.7427,1521730.791,716771.0057,1696717.107,819598.0078,1584213.957,798892.515,601973.0017,1456486.293,1702406.039,1566471.008,1592210.176,937628.3467,1558547.578,1156329.274,1514349.692,1039107.326,809089.6719,675536.3915,1373589.804,1690091.019,1253370.149,774073.5619,1741959.834,1705762.788,1071109.917,1118047.991,1165253.033,1280910.19,841122.8824,1228810.745,1086072.071,1204372.295,1345004.12,1116902.345,822431.7303,1360623.694,2298379.487,1400498.268,566848.7321,1367586.278,1113373.52,721974.5515,685503.9903,152071.8747,1280431.574,568703.1838,1200764.844,1607161.637,1421715.415,311111.2006,1338044.383,1417870.983,796389.438,1310207.133,994897.7278,1202987.829,768751.9005,1211655.305,1540418.222,712228.4243,1525533.407,1034218.402,874103.6606,1912825.285,1754770.59,1340066.913,1446756.863,1592768.242,660364.9813,861321.5807,1648246.774,977135.8857,1591934.19,695386.331,568977.0728,935590.8043,984311.7745,1796245.808,720080.2321,783808.4025,1598615.974,1564125.238,929480.6299,1414495.343,837668.1026,1197515.454,1232004.83,1285933.408,1361521.983,1090826.374,1475319.699,1066659.383,1117432.98,1420283.559,840272.8649,1024907.94,1494241.226,1125880.487,1082455.018,1554634.995,1011365.365,1432756.517,1612717.553,973299.8618,679228.9927,1270999.939,910211.0189,1026271.796,1496729.536,1490539.058,1491838.494,996771.2482,1064854.309,985749.7874,1952622.402,1754969.162,1122240.364,1236931.728,966084.4204,852268.6717,1280669.873,1190213.513,1123851.141,1689120.427,1573347.788,1696977.663,1414286.724,755292.1144,714706.4289,944001.5583,1523136.485,1422916.811,1945618.658,1726719.067,1051123.833,2249122.541,1523915.145,1039517.534,818057.8953,1115466.585,1258178.804,1435423.708,1153470.44,1425603.495,1048350.692,1214482.379,821859.0657,753652.2718,1220001.334,1075675.108,1396082.352,1137801.933,1159953.593,1487849.876,1103072.439,897291.1153,1214320.574,1364363.375,1249092.928,946479.2349,1659805.184,1285399.565,898281.9025,1483848.169,1353488.416,1268703.811,1448573.845,1343605.8,1511537.745,1662038.759,1166673.195,1375633.373,839638.461,1638265.395,1385400.456,1153233.241,1370178.474,1181877.183,894251.0686,1421135.815,1028964.474,923508.1257,1599634.465,1369186.07,1748782.809,1150877.735,1110598.755,1159207.085,1811377.221,1267443.398,1352547.693,599504.0193,717213.2688,1008712.575,1071596.112,1397341.856,1313304.588,2106510.863,1306458.906,1354928.95,1582765.592,847155.0413,1342245.969,1363086.905,1275318.562,1285923.734,1789607.526,1196064.33,1917583.999,1370274.387,1677204.246,1439714.281,1012262.712,1511743.129,1131154.518,764860.4627,1681316.362,291724.2456,1013252.209,1194709.628,1463003.056,1453327.916,1291506.386,1625508.013,566896.2123,1468513.244,1573105.981,968360.5234,1309985.887,1361219.3,1465120.47,1571464.965,1629098.182,1182335.68,1010813.709,924728.5374,1382110.278,1366727.663,1297849.764,1196687.687,1281113.315,1530729.578,1208664.863,1417275.667,1195601.962,2469065.594,1223100.542,1220276.551,1311765.141,1198313.598,1187609.122,1399662.584,1597776.771,1355022.283,1137059.188,1053815.097,1242421.532,1222041.016,1025461.134,859427.9793,1279803.95,1671669.452,1525601.791,998773.9973,1012321.574,1252419.196,1869313.107,1800685.922,1393100.423,1166558.374,988175.0074,1540480.613,866142.1839,557362.2043,1033290.975,1084945.4,1365081.178,1239459.815,2056692.768,1045395.329,1679204.741,1158742.83,1647278.685,1702090.635,1379386.383,1358526.741,991398.8219,957117.6472,1638969.269,714142.2407,760876.0222,1343537.178,1056993.649,1088222.421,1308983.632,1548322.501,1411749.107,1601904.357,1277297.483,1061552.022,1115013.147,1020842.531,1440961.857,817377.311,1381536.934,1273067.036,1376714.674,1293746.876,1750908.224,555811.4067,1578829.012,911202.1683,1628751.935,1245400.955,993725.2172,1816099.138,1570583.34,1626321.321,1262494.287,1185226.617,1360329.359,1350459.116,1556987.724,886036.1295,1129613.01,1070240.02,1587015.357,1146321.581,1377447.349,1113570.852,1593836.785,1560746.866,977980.9211,1292592.392,1458912.584,1037780.48,1792254.818,882170.3184,1883481.075,1268600.361,1157189.438,1180989.324,1813043.926,866666.0554,1671350.14,1137467.586,711499.2446,1940195.374,1496466.357,1448995.115,924271.7911,1747004.583,1576286.214,1712280.706,1852375.507,1007596.043,1034779.19,1006544.527,736798.5333,1109006.287,1384140.227,2084883.79,801194.6198,1412242.755,1890789.177,1841904.243,1467075.169,661043.3565,978035.3448,1250882.292,1409238.798,1162746.621,878862.7457,1338424.788,1094347.968,1195897.741,1050239.904,914231.2923,864483.7585,1599478.986,1336356.233,1808341.466,1424283.373,1471799.676,1347622.483,1163741.658,1450624.524,982298.0366,868314.4736,1231511.931,663128.8401,1210496.625,1409033.071,1356384.668,1125476.202,1129975.817,1003642.627,1306367.811,1775874.76,1036685.241,1869929.202,1381085.729,2252243.34,787039.6447,957283.6564,1173695.292,1713161.699,1325503.454,1501497.532,1573580.234,693566.7573,1524586.787,1048818.21,1310764.112,1537329.57,1244881.363,732733.2363,1095806.626,476006.4445,1599911.368,1675825.721,1175868.999,1135079.345,1833208.579,1120349.773,1080735.984,1168574.666,1919693.23,1466605.774,1234037.236,1269486.337,1176111.788,1371298.425,1246509.14,1020268.855,1130415.41,890559.861,1417158.537,1376492.925,1306207.111,1275208.577,902520.94,872312.1738,994517.0453,1289008.217,1610006.605,1843720.648,1891949.348,1451078.093,1481940.762,1144477.879,1279945.51,1193021.312,1167119.109,1225612.763,1131618.913,1697501.605,1365496.885,622449.6452,1551094.815,1299126.83,1290324.649,1183884.005,1305934.325,1279117.965,786559.0249,1588196.233,976649.0166,1250866.567,1046627.052,1115935.277,1077813.593,1047689.266,2332110.74,956435.2633,1892623.546,283208.1322,1176021.375,783818.682,1625703.075,1961846.905,1084556.029,1428247.074,1634945.808,915992.5578,1042373.524,879618.3222,1210431.684,1059262.039,972417.8089,1242979.154,1096846.086,1392685.285,1080464.852,821413.1935,2237778.026,1518319.641,1503552.206,1219154.403,1276259.018,1400496.655,1127174.713,1251663.851,1469354.782,946556.2637,1150658.595,1325819.913,1150093.889,1009142.338,1705276.19,829794.8233,1046442.634,1152269.431,1091479.56,1039915.341,565732.8175,1739628.383,1442128.732,1004124.909,1143621.36,1060241.2,1548962.888,1056984.182,1447353.264,1251566.478,751969.2117,764955.4982,1539958.931,962747.1639,1353854.478,1850525.573,1778411.665,1369006.115,1197975.085,1930143.831,1481946.194,1347578.53,1358646.746,931768.0455,1205962.995,792146.076,1618670.884,864446.7942,662630.3439,1485145.661,1047226.967,1392793.814,943575.1307,1793398.718,881273.1168,2138713.943,1540869.872,1707650.436,1025705.134,1541186.254,1930344.449,1481146.95,1099725.283,1190867.437,1070318.815,1358213.906,1198725.487,1774715.484,1538903.993,1462360.601,953261.9162,1427108.501,769576.8637,668255.4804,800809.1317,1427202.279,783566.3279,949072.2496,1693591.835,1675557.271,1943359.768,1106261.274,978766.9139,997827.2538,1062206.321,1382172.294,1281741.163,1592664.7,1247557.695,779207.5546,1222760.858,1380715.315,704884.1544,1530480.688,1780415.438,1709667.189,852565.6269,1185310.267,1795093.034,956241.9913,1224454.547,552279.214,1186357.179,1582261.701,1478028.174,1386306.103,1424786.509,1206937.316,1209287.535,1029869.764,300464.0987,1294278.118,1251757.193,1128403.366,1363669.069,1177744.973,980274.0699,1524115.891,1311902.534,1119992.619,1538922.903,843633.1982,903301.9933,1161995.728,733299.7945,1837930.801,962028.7008,1477765.148,1419345.607,539483.3966,1097701.943,1412274.486,1013443.438,893919.0388,1234531.601,864702.9339,977024.1102,936148.5119,1056976.975,1040607.312,1641101.519,503065.5056,1296146.939,1164209.619,999814.8898,1060897.689,1848633.724,617157.9103,857697.1255,1253434.398,1635092.433,1524845.422,763869.6667,1376637.506,1244440.135,693931.5015,1277744.739,1539329.319,903881.6639,896944.2443,1184758.842,1731437.416,762144.9261,1270905.02,1000043.903,1967637.287,1114779.247,671661.7134,1214986.886,1053236.6,1515005.384,1732196.217,1587122.369,1184893.56,1314348.699,717825.3597,1441736.761,1119542.311,850977.0123,1655466.736,1641739.518,1369976.501,1465835.843,1789334.851,863297.1767,1425366.413,2271112.744,1370699.722,1566740.128,1436995.2,1345962.955,1265180.909,1061222.537,1383967.463,1051519.066,1550359.548,1375057.083,1882978.9,1274053.64,1426434.644,913587.0974,1116730.867,1226586.921,1836978.483,1452153.849,1294750.368,1059870.965,1615346.75,1107692.003,2330289.701,1116193.293,1072253.834,1626941.788,1669681.231,806121.8394,1680252.737,1186441.756,1766248.403,1641055.939,1120894.804,1325706.901,1593347.849,605073.4908,1064509.523,872365.8799,1117741.757,1935172.995,1668670.656,1072704.89,1914746.582,839194.0689,1285157.87,1433614.967,1459342.887,1652845.981,725830.602,1378863.688,1003941.929,729882.6249,1270047.528,1695706.132,714822.5872,1462899.031,1127260.126,1014226.299,852982.5644,830286.7066,1938866.49,1247645.41,813415.1281,679373.4015,814879.2063,1489540.135,1468738.755,1859883.661,1558758.796,2120888.345,790598.827,1137465.336,1369753.282,1433221.122,1373048.099,941950.5795,948279.9394,1365036.084,1289082.363,1398979.249,1559678.613,1485677.064,1553592.98,1179278.094,1262465.989,1663509.393,930011.5709,1584167.851,2185480.091,1529028.714,998240.8508,513215.9882,1136448.409,1898668.844,1255576.273,1367641.27,1788285.239,1230363.234,1000216.858,587007.8442,1734373.044,762167.2533,1532845.723,1243501.651,1628878.094,1767330.934,1308752.504,1311681.42,1567368.285,1126821.109,1473761.532,1366000.57,1677612.442,1789973.205,1961715.867,673225.1119,1230391.468,1124818.114,1090996.143,1570154.414,685123.1393,845553.3695,974805.9937,1247660.99,1381417.25,1726364.398,961539.0599,1359978.16,1384466.437,1531447.285,1418595.727,1476386.996,1168355.32,1222701.012,987447.7775,982790.871,527749.4039,1391232.527,1094321.883,1610217.177,1768705.125,1236258.08,1329007.203,1704126.876,1321888.268,1113936.638,1043628.37,1663653.71,969678.5673,1183014.509,957814.6031,912891.6806,1479758.318,1431507.623,1747911.496,1563083.336,1425745.297,804453.8698,1060440.596,954737.1411,1152604.142,955943.809,433247.1566,1718876.795,1236874.809,682200.3006,1141916.525,1162735.272,1681340.635,945981.5296,854045.0138,1372994.29,414571.2229,1240319.692,1640646.67,1537335.897,1337966.927,1085113.451,905328.7691,494742.5436,1237360.718,864899.485,1002192.582,800110.1189,1410331.825,1036382.766,437146.0204,624432.966,1179440.832,1740404.967,706135.1446,870252.411,1106149.686,1192677.55,2026303.098,1311473.323,1123386.531,1205750.232,1582140.06,573434.6642,1735826.005,1052185.176,1151281.847,1531216.894,1103352.601,308199.8912,1423296.118,1315684.457,637951.9056,1027191.029,729678.6262,1676770.331,1569121.917,874969.6969,1172413.197,1538985.189,1286572.979,1646033.41,1147313.02,976483.5805,1073350.044,1084255.678,1432252.081,1676070.943,1580557.01,1549873.88,1989672.524,1286980.807,1752967.605,1529711.14,1710612.03,774009.5476,1536143.592,1662939.097,1443027.263,1282258.093,1245967.799,1025908.914,1380070.45,288708.9121,1247581.212,1767399.29,1588549.501,1685217.105,928950.0032,1565931.192,926882.9195,1770616.93,1279353.925,530764.6725,1874895.602,1422890.021,1245788.303,1248130.521,1535564.552,1709441.806,1433260.228,1282758.903,1682708.617,624482.7636,1651684.774,768034.5331,1001876.606,1500821.469,1273988.483,1031046.365,1508198.672,773996.4762,1723706.759,1260826.638,1367142.717,1303091.91,1341870.354,1188416.806,1155077.131,1048969.493,1319478.287,1022408.901,1394970.599,1183343.566,1259919.983,579585.698,1591188.348,1437153.959,851018.9558,1321037.414,1112286.046,1509968.985,959625.5302,1032180.378,1232014.527,1575100.913,1257433.086,2173808.628,1115549.268,1397956.196,1003905.06,1614373.964,1463367.821,966620.5141,1453663.252,1321388.619,910512.6354,1029354.495,1608889.263,1458009.211,2198564.573,1281777.581,1196643.385,1578493.708,430088.2507,677988.2555,1085534.179,1634781.274,1167449.99,1067727.095,887739.4321,842924.5538,864067.0615,508951.5669,1223777.498,1029037.429,1487997.879,1836419.641,1148066.813,1318681.04,1174481.066,1522954.939,1132146.32,1212461.526,864132.0331,1336377.825,1747244.863,1398353.591,2020158.363,877779.3441,1255202.11,1173413.55,1326680.244,1585521.989,1106336.838,962501.9015,1408074.53,1266209.753,1741052.96,1636559.241,2318285.703,1409892.09,1166198.116,1393995.962,1462608.696,1922281.305,1587406.303,967868.5146,1426545.967,1725429.749,1753820.622,321058.9607,1089601.882,1137523.111,1371670.389,1595620.557,1899948.059,674657.9107,1555490.621,1194191.879,1482107.37,1154917.394,1050838.704,31140.51762,1748864.715,1287030.932,1237246.145,1259733.644,1028914.315,1388218.529,637189.9594,1717570.53,729688.5926,2049146.63,1340705.119,980983.211,1518169.444,1002840.229,1499920.594,1496577.459,1526915.349,917610.8884,1572990.374,959416.4367,960083.9969,1526025.659,1006885.844,1105105.053,625880.7321,1799827.22,1152798.579,846095.9673,1387864.89,1414286.722,1273308.71,1489648.018,1765988.264,934111.6355,1095879.443,876348.8176,854945.5067,1349743.146,970825.5964,1796009.504,934492.3424,584061.2474,895845.5655,696040.1299,1204137.323,1413729.757,607873.7728,971099.4754,1714055.837,1956438.651,2013015.746,1390497.566,1529452.062,1143215.029,1949577.954,1057799.242,1585873.833,1168993.759,1431915.977,1409439.076,1496724.381,1566567.883,986113.2395,885611.5783,1102259.539,1268125.838,1580691.617,1128644.462,1524689.063,1176420.559,1456273.724,1777516.449,1237902.82,1385783.517,1035125.857,1358899.686,1311145.968,919926.9985,985866.0316,1196204.886,1435981.22,752800.1475,324981.993,1127637.557,239319.9342,529282.0844,1455691.797,1371527.327,1231452.189,1102641.114,758262.6121,476971.4559,1706689.94,1079745.119,766594.3397,905045.2177,1425114.718,1512542.441,1650342.131,1112548.479,942508.9622,1642844.649,1078713.227,1333865.438,684049.9193,1311067.446,1172133.487,1419536.259,1288426.694,1500939.827,1000087.121,1457767.533,747933.4869,1024738.285,1517666.855,953840.6976,1375497.973,1645530.056,1727006.951,1597330.411,1688279.308,1398310.2,1100093.909,1505560.54,1105990.694,789043.8512,756319.734,1856782.783,1222020.821,1043968.399,1673294.246,1325860.533,1236044.316,1030759.7,1609581.804,1292287.095,1057697.703,768152.791,1513427.551,1429497.617,1376969.929,614700.7371,780608.9935,856548.9441,1656080.089,1249914.079,817460.4216,990893.1601,972079.5876,1349989.647,1303542.283,593766.1848,1243918.811,1395855.656,1112314.303,850010.1816,931787.6179,1011140.799,1190442.123,916140.2212,1222045.091,1232156.012,652752.9727,1219846.919,2050988.497,1359052.846,1308773.078,1573998.902,1182980.604,1029861.623,1085943.076,1713351.394,1297619.348,1096052.868,1920527.53,1035171.06,1218011.061,1106705.011,664978.8738,1316129.309,1398760.047,759799.8758,776906.3269,971928.9869,1180091.498,1201785.667,1591234.773,143027.3645,1091143.399,1249173.691,2002028.632,824540.8964,1511526.921,994257.5352,1345296.554,1166399.672,1820981.219,1023965.403,889385.9016,616738.2083,1784260.849,1050541.314,1389223.607,1423908.258,1069238.5,1007856.266,924346.1648,1453312.468,782656.0804,803689.1519,1439875.64,1270869.783,1347279.207,2186194.793,1082486.679,1700109.608,1623100.84,943309.4486,1409684.485,1326481.675,404643.6022,1176655.085,633875.9302,1390251.42,861138.1836,1151233.095,686644.6104,1261681.961,1327811.343,1339096.077,987355.9609,1384478.305,1168919.401,1522099.831,1260374.966,857762.317,1126450.426,1574084.927,469262.8156,1114169.037,1792368.627,1383842.185,691318.2401,1245070.338,2220799.069,854815.1175,2092348.377,781213.0669,726883.8689,1640990.378,1535781.96,1737759.05,1550702.478,1348873.427,955445.8537,1467910.569,1742938.776,1795630.913,1305972.22,1433542.021,921396.9753,1405399.855,1088548.827,738030.6499,2235294.718,1564252.526,1309937.399,1660770.002,1485418.102,886124.7256,1411024.044,671343.9418,992585.3823,944590.1588,1399909.049,865099.5234,1394423.556,813807.6997,1316180.494,1212205.341,1769484.893,541953.9057,1494101.445,856022.8625,1427842.506,1228138.129,1168627.651,1389287.474,1243981.946,1584439.713,1622837.353,1031146.755,1098518.134,909781.4668,1431517.439,1636996.074,1658974.567,1168887.459,1720258.777,1129408.87,778836.9229,1276471.581,839426.1222,794075.8615,1372549.782,1084539.387,211017.9705,1186372.179,1140918.805,1471828.129,803259.6126,1124719.49,1396401.022,802274.1289,1646662.911,1202621.178,1066768,1153135.22,1706110.86,1543913.433,302307.4011,1134055.403,1352756.753,1772390.553,1014450.654,781137.4618,921238.3583,790555.5204,1420648.281,377618.9699,945079.5323,1630952.884,1009972.083,1372806.616,560598.5384,1484653.884,940138.9614,1354077.498,1400961.279,1426832.049,1031737.385,1244248.525,1070868.067,493350.0312,1228323.225,1427026.945,1504664.281,689155.5684,1481171.234,1092649.709,962581.6883,688479.2926,1363106.125,826328.1084,1434575.11,1509422.58,395440.2022,1765809.432,1135676.183,1006227.535,576387.1752,1044615.522,1765352.366,1049632.181,1456969.577,1331374.948,1779874.754,1601152.932,1702528.794,1123765.346,1042144.231,869026.582,1352993.625,945931.1936,1653381.313,1258957.62,724121.6734,1067871.687,842235.8034,954154.2069,1356691.387,1202992.884,1502447.917,1947338.44,1153516.919,414165.2204,723089.9525,1193482.503,1380602.556,151527.0826,1114729.725,984421.2253,875904.5286,788427.8399,1444701.328,1450393.53,921321.015,1160146.171,1222689.523,2004396.372,454055.6559,1698198.751,1193106.94,1275403.464,810751.725,642862.7138,1086825.754,773360.698,1500962.615,768301.802,1781211.414,1420469.727,1380215.515,1090805.374,886815.9436,1007224.929,1077754.226,1253648.324,1102943.351,744132.7042,1845630.071,873588.1297,755678.3301,1101826.315,1618994.276,1127873.577,749847.1904,984672.2998,534077.4555,1242114.101,1273631.267,1095597.944,1364738.296,1037147.467,1228517.207,759360.6548,1140579.618,810741.5185,642855.1696,1562950.322,1599851.895,1332669.235,665160.0759,1591383.735,1144507.423,1619721.716,1251688.616,1882806.934,1016163.177,1721005.42,890138.2114,1272719.632,1582605.535,1170204.339,1166750.313,319495.6676,704698.3621,945614.5659,2054897.009,1280230.625,850114.5963,1637649.905,1742431.663,942093.9245,1388782.887,996506.0709,790802.801,718650.6438,1517141.623,496359.9708,820611.4709,1122320.933,846939.4288,1540762.269,963531.9152,1590804.044,1283415.266,1447920.68,742858.6356,1400609.034,1638577.417,1235475.55,1249417.897,1499356.12,1005843.917,623721.613,922514.088,1638606.834,1249223.831,1928301.782,1487729.592,896303.7992,1903813.793,1069851.162,829868.2304,1181338.161,1401767.904,1235501.486,1522083.944,656971.5307,1660678.035,606191.8669,1011331.164,1529830.368,1489520.019,1468267.23,978312.7484,1181637.949,1015233.032,1139615.72,984349.6142,1765281.093,1327975.249,804170.2016,1467271.556,1478823.647,1367312.132,1162469.887,1473278.441,897479.9502,1568578.512,1421518.602,1199144.788,1596180.568,1264972.442,1135465.473,1359838.999,88591.77016,1822448.617,1720734.403,1224397.427,1209571.072,1698820.102,1860358.468,1168444.882,764756.0935,977242.2697,1079158.653,1383395.287,992053.0502,1574919.906,1174311.556,795082.8102,1170573.77,1998368.741,842086.6733,849656.9232,908616.4826,1524257.706,685880.3213,771310.0004,1308243.922,1312063.756,1467849.818,902350.4197,926880.8506,1323326.403,1504026.27,1003266.876,592397.7261,1339142.805,1212939.954,753930.5825,1538401.817,1295728.088,1472887.247,831762.7909,1610577.497,881446.1155,1666462.622,1085218.859,1712929.654,1444403.664,1884674.241,1014548.233,1084013.785,1279777.379,1967384.778,1002974.215,979568.6285,565937.2006,1092130.981,1869113.611,1817829.53,1392207.648,1389773.873,956009.1436,945833.1891,1383766.082,1400268.142,1144937.614,1118165.866,1047012.271,1096069.287,1386473.365,945831.1863,1311379.596,885661.5908,1507331.288,1643291.722,987746.924,612211.5924,836235.0305,1495518.624,911071.8336,1360787.871,1455107.451,1327969.286,1838503.994,1727211.089,1093344.577,943485.0473,1100632.391,1269811.089,1321008.593,978241.2891,952533.5782,1434015.033,1008649.929,2007556.286,882666.5815,1246218.31,880682.302,840124.8423,1469767.647,1824987.706,1404896.376,1290043.367,1410362.613,1058269.019,1464929.162,1777009.712,826194.6782,1851575.868,1552915.164,922478.9145,1753427.937,1387701.111,1801916.346,1237115.741,1009606.284,1601678.263,483458.5483,925394.135,1143377.602,1283401.789,1031367.589,1153605.031,995137.2024,1006580.48,987434.7498,897013.181,1560838.45,1349818.25,883147.471,926482.4677,1100152.088,674197.852,1587350.294,1276987.492,982344.8121,1153433.081,799124.8492,1169640.324,1591203.49,1450769.841,1381442.758,1930805.947,1280548.089,916344.2938,1170892.98,1616382.932,1056518.913,1583897.538,619407.4863,1043415.992,1222344.208,1433538.321,1474417.272,1827899.186,1130537.993,758886.6888,1210400.127,674817.5428,1232209.476,2105205.856,1662585.938,1443907.747,781482.5832,1557794.021,1476277.527,1412449.479,1438290.851,1667560.879,1131532.919,1154270.485,1650770.93,1387987.803,1325294.121,825095.1086,944186.1591,1608726.681,1050223.668,1417691.113,1386351.145,1015546.309,991934.0654,1267433.909,1491811.661,1222887.121,1114901.973,1024787.942,675489.7527,1515157.081,491085.826,737147.0943,1208875.084,1073355.784,554702.6802,1225796.414,1282339.35,1409824.638,1448668.424,728402.0001,1381482.685,1424994.375,1741105.641,1361230.121]

npHousePrices = np.array(HousePrices)      
housePricesSampleSize = np.size(npHousePrices)     
housePricesAverage = np.mean(npHousePrices)    
housePricesMin = np.min(npHousePrices)     
housePricesMax = np.max(npHousePrices)      

print("Descriptive Statistics for House Prices:\n")
print(f"Sample Size of Data: {housePricesSampleSize}")    
print(f"Average Price of Houses: ${housePricesAverage:.2f}")
print(f"Minimum House Price: ${housePricesMin:.2f}")
print(f"Maximum House Price: ${housePricesMax:.2f}")

housePriceBins = 40     
frequency, binEdges = np.histogram(npHousePrices, bins=housePriceBins)        

plt.hist(npHousePrices, bins=housePriceBins, edgecolor="black")     
plt.title("Distribution of House Prices")       
plt.xlabel("House Price")       
plt.ylabel("Frequency")         

print("\nHouse Price Distribution (Frequency Counts per Bin):") 

binIndex = 0        
for count in frequency:     
    lowerEdge = binEdges[binIndex]     
    upperEdge = binEdges[binIndex + 1]      
    print(f"Bin {binIndex + 1} (${lowerEdge:,.2f} - ${upperEdge:,.2f}): {count}")       
    binIndex +=1       

plt.show()   

# Analysis: 

# For my historgram, I used 40 bins, as I believe it gave me the best output with the most smooth data to see trends compared to the other numbers of bins. 
# The most noticeable part of the data shows us that a majority of the houses in this dataset fall within the middle range of prices. 
# Bins 16-25 have a frequency of at least 100 with the max being 149. 
# The sum value of 1217 frequencies throughout all 10 bins. 
# The minimum house price of bin 16 is $945,362.42, with the maximum house price of bin 25 being $1,554,843.69. 
# So, about 60% of the data points (house prices) fall within the previously stated range of middle-upper priced houses, even though the 10 bins only account for 25% of the bins. 
# This tells us that the housing market in this dataset is concentrated around the relatively narrow price range ($945,362.42-$1,554,843.69) of homes. 
# The histogram also indicates that there are very few low-end priced homes (under ~$400,000 or bins 1-6), suggesting a scarcity in affordable options for this market. 
# Also, there aren't many luxury priced homes (over ~$2,000,000 or bins 33-40) shown in the histogram, but there is a slightly larger presence of them compared to the cheaper homes. 
# Overall, the lack of affordable homes, and the prominence of middle-upper priced homes aligns with my earlier statement of this data having a market with solid middle-upper range demand in housing, appealing to higher-income buyers. 
# This could likely lead these prices to rise in the future, due to competitve demand. 
# If this dataset represents a particular geographic area, I believe it would reflect a higher-income upper middle class neighborhood.






