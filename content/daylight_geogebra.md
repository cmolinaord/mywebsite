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
