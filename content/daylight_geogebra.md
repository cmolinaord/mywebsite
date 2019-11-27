Title: Calculando la duración de un día con Geogebra
Date: 2019-11-27 13:24
Modified: 2019-11-27 13:24
Tags: science
Category: geogebra
Authors: Carlos Molina
Summary: Un script de geogebra que calcula la duración del día en función de la latitud y de la inclinación del Sol.

Hace un tiempo tuve que enfrentarme a un problema sobre calcular la duración del
día en función de la latitud del lugar donde estés en la tierra y del ángulo
que forma el plano de la eclíptica con el ecuador terrestre, que varía con el momento del año.

Éste ángulo, para que nos entendamos, varía en función de la fecha ya que el
eje de rotación de la Tierra está inclinado unos 23 grados respecto al plano en
el que rota la Tierra alrededor del Sol. De esta manera, habrá momentos en el año
en los que el eje de la Tierra vea una inclinación de +23 a -23 grados con respecto
al ecuador. En el solsticio de verano (en el hemisferio norte), en torno al 21 de Junio,
el Sol estará con la máxima inclinación hacia el norte (+21º), por eso es verano en el
hemisferio norte, porque los rayos nos llegan más verticales (vemos el Sol más alto).
En el de invierno, en torno al 21 de diciembre, el Sol tendrá la mínima inclinación (-23º).
En los puntos intermedios, los equinoccios, en torno al 20 de Marzo y el 22 de Septiembre,
el Sol cruza por el ecuador, por lo que la inclinación es 0º, lo que hace que para cualquier
latitud, amanezca y anochezca en el mismo instante, por lo que el día dura lo mismo para
toda la Tierra, exactamente 12 horas, y también son los únicos momentos en los que
el Sol amanece y se pone, justo en el Este y el Oeste, respectivamente.

Para entender todo esto un poco mejor, me puse a hacer este diagrama usando Geogebra.
En él podemos cambiar la inclinación relativa del Sol y el ecuador, y la latitud
del punto en la Tierra que queramos calcular.

Puede ser un poco engorroso entender el diagrama porque en la misma esfera he
representado la Tierra vista desde arriba (desde el polo Norte) y desde un lateral
(con el polo Norte arriba).

Primero nos debemos fijar en las líneas azules y el punto "Sun", que podemos
mover para ajustar la inclinación entre los máximos permitidos (+23.4 a -23.4).
Luego moveremos el punto azul "A", para ajustar la latitud. De esta forma, la línea
horizontal punteada en azul nos va a hacer un corte transversal de la Tierra, que
es representa en amarillo (visto desde arriba), indicando los ángulos en los que
hay luz, entre la salida y la puesta de Sol.

<!DOCTYPE html>
<html>
<head>
<meta name=viewport content="width=device-width,initial-scale=1">
<meta charset="utf-8"/>
<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>

</head>
<body>
<div id="ggbApplet"></div>

<script>
var parameters = {
"id": "ggbApplet",
"width":1000,
"height":624,
"showMenuBar":false,
"showAlgebraInput":false,
"showToolBar":false,
"customToolBar":"0 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24  20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49  50 , 71  14  68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6",
"showToolBarHelp":false,
"showResetIcon":false,
"enableLabelDrags":false,
"enableShiftDragZoom":true,
"enableRightClick":false,
"errorDialogsActive":false,
"useBrowserForJS":false,
"allowStyleBar":false,
"preventFocus":false,
"showZoomButtons":true,
"capturingThreshold":3,
// add code here to run when the applet starts
"appletOnLoad":function(api){ /* api.evalCommand('Segment((1,2),(3,4))');*/ },
"showFullscreenButton":true,
"scale":1,
"disableAutoScale":false,
"allowUpscale":false,
"clickToLoad":false,
"appName":"classic",
"showSuggestionButtons":false,
"buttonRounding":0.7,
"buttonShadows":false,
"language":"en",
// use this instead of ggbBase64 to load a material from geogebra.org
// "material_id":"RHYH3UQ8",
// use this instead of ggbBase64 to load a .ggb file
// "filename":"myfile.ggb",
"ggbBase64":"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",
};
// is3D=is 3D applet using 3D view, AV=Algebra View, SV=Spreadsheet View, CV=CAS View, EV2=Graphics View 2, CP=Construction Protocol, PC=Probability Calculator DA=Data Analysis, FI=Function Inspector, macro=Macros
var views = {'is3D': 0,'AV': 0,'SV': 0,'CV': 0,'EV2': 0,'CP': 1,'PC': 0,'DA': 0,'FI': 0,'macro': 0};
var applet = new GGBApplet(parameters, '5.0', views);
window.onload = function() {applet.inject('ggbApplet')};
applet.setPreviewImage('data:image/gif;base64,R0lGODlhAQABAAAAADs=','https://www.geogebra.org/images/GeoGebra_loading.png','https://www.geogebra.org/images/applet_play.png');
</script>
</body>
</html>
