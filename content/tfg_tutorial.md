Title: Escribe tu TFG usando LaTeX y Git
Date: 2018-09-27 12:47
Modified: 2018-10-07 20:07
Tags: workflow, open source, git, latex
Category: software
Authors: Carlos Molina
Summary: Consejos y experiencias sobre realizar mi Trabajo de Fin de Grado con LaTeX y Git.

Este año he tenido que escribir y defender mi Trabajo de Fin de Grado para terminar
el Grado en Física por la Universidad de Sevilla. Y para evitar acabar con
algo como ésto:

![meme]({static}/images/tfg_meme_versiones.jpg)

se me ocurrió usar LaTeX y un sistema de control de versiones como Git. Bueno,
realmente lo de usar LaTeX ya lo tenía claro desde el principio, ya que me
parece la mejor forma de escribir artículos científicos, tesis, libros y documentos
en general. Por otro lado, para que un gestor de versiones enfocado a código fuente
es necesario que haya un código, me explico, que sería menos efectivo hacer un control
de versiones con Git de un archivo de texto de Microsoft Word o LibreOffice, ya
que éstos encapsulan el archivo en un binario codificado.

Usando Git iba a ser capáz de llevar un control de versiones exhaustivo, muy útil a
la hora de escribir un trabajo de éstas características. Quiero escribir éste artículo
para aquellos que tengan que realizar su Trabajo de Fin de Grado, Master o Tesis, con
el objetivo de mostrarles la forma en que yo lo he hecho, que es más fácil de lo
que pueden creer. Va dirigido sobre todo a aquellos que ya saben usar LaTeX, pero que
nunca han trabajado con un gestor de versiones. Me consta que, por ejemplo, en física
y otras carreras científicas o técnicas, es relativamente común saber usar LaTeX,
pero es mucho más raro el uso de controles de versiones, más habitual entre programadores
e informáticos.

Aprender LaTeX no es tan dificil por otra parte. Yo digo que sé usarlo, pero realmente
cada vez que me pongo a escribir, estoy contínuamente consultando manuales, tutoriales
y foros para las dudas que me surgen. Y esa es realmente la forma de aprender,
yo no he asistido a ningún curso ni nada por el estilo. Así, que si no lo usas todavía,
atrévete a probarlo, verás que con poco esfuerzo consigues un texto muy bonito, y con
la ventaja de que está escrito en un código, que cada vez que lo compilas, el resultado
es exáctamente el mismo, nada de esos problemas de los procesadores de texto tradicionales,
que mueves un párrafo y todas las tablas e imágenes se te van a la página que no quieres
o cosas así.

# Monta el proyecto

Para empezar, decir que mi entorno de trabajo habitual es Linux, así que voy a explicar
cómo lo he hecho en mi caso, aunque por supuesto, también se puede usar LaTeX y Git en
Windows.

Primero de todo vamos a instalar Git (si es que no lo tenemos ya), y a crearnos una
cuenta de GitHub. Ésto último no es realmente necesario, sirve para subir una copia
de nuestro repositorio a los servidores de GitHub por si queremos tenerlo disponible con
compañeros, o desde otro ordenador, o simplemente tener una copia de seguridad. Hay otras
opciones, otros servicios como GitLab u otros, pero no bueno, yo usé mi cuenta de GitHub.

Para empezar créate un directorio TFG/ donde tendremos todo el trabajo. Como queremos
tener un control de versiones de (casi) todo lo que hay aquí dentro, vamos a inicializar un
repositorio de Git aquí.

```
mkdir TFG
cd TFG/
git init
```

Para sincronizar éste nuevo repositorio con uno nuevo que hayamos creado en GitHub,
podemos hacer

```
git remote add origin <URL>
```
con la URL de nuestro repositorio, algo así como https://github.com/usuario/TFG

Si queremos podemos inicializarlo de otra forma. Creamos primero el repo en GitHub
y luego vamos al icono de "Clone or download", copiamos la URL y sin haber creado
el directorio TFG/ hacemos:

```
git clone <URL>
```

Lo que creará el directorio TFG (o el nombre del directorio) con el proyecto vacío
inicializado, listo para empezar. Para saber más sobre como crear repositorios y como
manejarlos, os recomiendo mirar la docuentación de Git y GitHub, que están muy bien:
* [Git en español](https://git-scm.com/book/es/v2)
* [GitHub](https://help.github.com/)

Dentro de esta carpeta iremos creando varios subdirectorios para organizar todo
lo que el proyecto necesita, código fuente Latex, imágenes, el resultado en PDF...

Para empezar a escribir en Latex, créate un directorio tex/ y uno pdf/
```
mkdir tex pdf
```

En tex/ podemos empezar a escribir en archivos .tex, nuetro trabajo. Mi recomendación
es dividir el proyecto en varios archivos, por ejemplo uno por cada capítulo, otro
para la portada, y tener un archivo principal que llame a los otros en órden.

![tex_folder]({static}/images/tfg_folders_tex.png)

En mi caso, el fichero tfg.tex llama a los otros capítulos y también a un archivo
mi_estilo.sty dónde agrupo las librerías y comandos que usa mi documento de LaTeX.

# Trabaja en el proyecto

Una vez montado el entorno podemos empezar a escribir nuestro trabajo, usando las
reglas de LaTeX, que si no lo conocéis podéis echarle un vistazo a estos manuales:

* [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
* [LaTeX in 30 minutes](https://es.sharelatex.com/learn/Learn_LaTeX_in_30_minutes)

Decir que yo he usado LaTeX en su forma más básica, sin la ayuda de ningún procesador
de texto LaTeX, como pueden ser Texmaker, LyX, Overleaf o ShareLaTeX, éstos 2 últimos
online.

La forma en la que yo he trabajado ha sido escribir directamente código LaTeX en
archivos de texto plano mediante un editor de texto que a mi me gusta mucho llamado
[Atom](https://atom.io/). De hecho es el editor que suelo usar para todos mis proyectos
de programación, es bastante configurable, y puedes añadirle extensiones y plug-ins
para por ejemplo resaltar el texto con colores segun el lenguaje de programación.
Yo lo uso para Latex, Python, C, bash...

En un entorno como Linux, a mi me gusta crear alias a los proyectos en los que trabajo,
para acceder a ellos de manera muy cómoda desde la terminal escribiendo algo así como:
```
load_projectX
```

El alias, que se define por ejemplo en tu ```~/.bashrc``` tendría la forma:
```
alias load_tfg='export WORKDIR="~/Documents/TFG" && cdw && atom . '
```
Que automáticamente nos llevaría a la carpeta del proyecto (Documents/TFG) en tu home,
y una vez allí lanzaría el editor de texto atom para empezar a trabajar.
He incluido también un alias, cdw, que simpelemente hace:
```
alias cdw='cd $WORKDIR'
```

Una vez introducido como monto el entorno para empezar a trabajar, voy a dar algunos
consejos que he adquirido tras la experiencia de hacer este trabajo en LATEX.

## Crea tantas carpetas como sea preciso
En mi opinión prefiero tener más carpetas, pero tenerlo más ordenado. Me explico.
En mi caso, como he comentado antes, yo creé la carpeta tex/ para todos los archivos ```.tex```
con el código LaTeX, incluída la bibliografía.tex (sobre la que ahora dedicaré un
apartado propio) y la configuración de estilo en ```mi_estilo.sty```.

El resto de carpetas serán del estilo, img/ (para imágenes jpg, png), svg/ (para los
archivos de graficos vectoriales, que como son un código, se puede tener un control
de versiones bueno), y cualquier otro archivo que uséis en vuestro trabajo, como
datos experimentales en CSV, texto, scripts de Matlab o similares.
También recomiendo, en el caso de imágenes retocadas o con varias capas, que podamos
haber creado con Gimp (o su version privativa Photoshop), mantener los archivos originales
con todas las capas y la máxima resolución, ya que quizás necesitemos cambiar la imagen
un poco en el transcurso del proyecto.

Yo también creé un directorio scripts/ para posibles scripts que me ayudaran a la
revisión o mejora del documento. En el siguiente apartado explicaré uno que usé.

## Crea un Makefile bonito que te ayude a compilar fácilmente
El Makefile, para los que no estéis al corriente de lo que es, se trata de un
mecanismo de ayuda a la compilación de programas, muy usado por ejemplo en C/C++.
La idea es que el makefile te verifica si hay cosas ya compiladas para no repetir
trabajo inutil. En el caso de LATEX ya existe un paquete que te ayuda a eso, y
por ejemplo administra bien el tema de las referencias, tablas de contenido y eso.
Si no lo sabéis, para que las referencias y las tablas de contenido se muestren bien
en el documento final, latex debe hacer dos o más compilaciones, ya que la primera
encuentra donde están las cosas referenciadas y las guarda en algún archivo temporal,
y luego las referencia realmente.

Si usaís el compliador de latex "tal cual" (pdflatex ejemplo.tex), puede que la primera vez os aparezcan
referencias a sitios perdidos o desconocidos así: [?]

El paquete que he comentado que se encarga de arreglar esto es **latexmk**, y
creo que suele venir instalado junto al paquete básico de latex; si al
escribir latexmk en un terminal no os hace nada, buscar info por internet, debe ser fácil.

Pues bien, yo en mi Makefile (que simplemente es un archivo llamado makefile en la raíz
del proyecto), he puesto estas primeras líneas:
```
OUTPUT_DIR = pdf
SRC_DIR = tex
TEX = latexmk -cd- -pdf -outdir=$(OUTPUT_DIR) --shell-escape
```
Son variables de entorno, tal como pueden declararse en un shell bash. Las 2 primeras
definen los directorios donde están los pdf de salida y el código latex, respectivamente.
TEX es la variable que va a llamar a la función de compilado LATEX. El parámetro
-cd- es para que no cambie al directorio de origen cuando se haga la compilación.
-pdf- especifica que se cree un documento PDF, y --shell-escape permite que
se ejecuten bien algunos comandos de shell que son necesarios para la bibliografía.

Las siguientes lineas definen los comandos de compilación:
```
#tfg
##############################
tfg: $(OUTPUT_DIR)/tfg.pdf

$(OUTPUT_DIR)/tfg.pdf: $(SRC_DIR)/tfg.tex
	mkdir -p $(OUTPUT_DIR)
	$(TEX) $(SRC_DIR)/tfg.tex

tfg_prev: tfg
	$(TEX) $(SRC_DIR)/tfg.tex -pv

```

De esta forma, si luego escribes ```make tfg```, se compilará el PDF sólo si el
PDF existente no es el más reciente, y además solo se recompilarán las partes nuevas,
por ejemplo, si las referencias ya están correctas, no necesita recompilarse, y será
un poco más eficiente.

Si haces ```make tfg_prev```, después de comprobar que esté actualizado (y recompilar
en caso negativo), abrirá el documento usando el lector de pdf que tengamos configurado
mediante el archivo de configuración de latexmk, ```.latexmkrc```, cuyo contenido será:
```
$pdf_previewer = evince;
```

Otros comandos que he incluido en mi Makefile son, por ejemplo, para limpiar toda
compilación, PDFs y/o archivos temporales.

Y luego creé otros comandos que me podría ayudar a revisar mi trabajo. Por ejemplo,
en los puntos del código Latex que yo dejaba pendiente de revisar, ampliar, o corregir
añadía un par de líneas comentadas de la siguiente forma:
```
%WARNING
Revisar este punto porque tal y cual
```
Así que en el Makefile, creando un objetivo tal que así:
```
debug_warnings:
	echo "Mostrando lineas con WARNINGS:"
	grep -n -A1 "^%WARNING" $(SRC_DIR)/*.tex | grep -v "WARNING" | sed 's/-%/: /'
	echo " "
```
Con lo que, al ejecutar el comando ```make_debug_warnings```, me aparecería:
```
Mostrando lineas con WARNINGS:
tex/archivo_con_warnings.tex-25: Revisar este punto porque tal y cual
tex/otro_archivo.tex-63: Otro error que corregir aqui
```
Monstrando en que archivo y en que línea están los warnings, con la idea de
revisarlos (y eliminar las anotaciones) antes de imprimir la versión definitiva.

Otra cosa que quiero mencionar es un script interesante que creé y que lo llamaba mediante
este comando:
```
debug_figures_unused:
	./scripts/search_unused.sh
```
El script es un sencillo programa en bash que va a buscar en las carpetas de imágenes
cuales de ellas no están referidas en el código latex, siendo una forma más
de revisar que las imágenes que he incluído son las que quiero incluir y que no
he dejado ninguna imágen interesante sin usar. Lo ideal, sería mantener limpio el
directorio de imágenes, y quitar las que realmente no quiera usar, para que esta lista
se reduzca a cero si todo está bien.

```
let N=0
let n=0

echo "Figuras no usadas:"
for fig in $(ls {svg,img}/*); do
	let N=N+1
	grep $fig tex/*.tex &> /dev/null
	if [[ $? == 1 ]]; then
		let n=n+1
		echo "   $fig";
	fi;
done

echo " "
echo $n figuras no usadas de $N
```

En el apartado de bibliografía comentaré dos comando más del Makefile relacionados con la bibliografía.

## .gitignore

El .gitignore es la forma de decirle a git que ignore algunos archivos/directorios y
no los incluya en el repositorio. En nuestro caso es recomendable no incluir los PDF,
ya que se pueden compilar cada vez que queramos. También incluiremos algunos resultados
de la compilación que son auxiliares. En mi caso también he incluido el directorio svg-inkscape/
que contiene resultados intermedios de la compilación de los SVG que se incluyen
en el documento, y que los proceso con una libreria de Inkscape/latex.
Así quedaría mi .gitignore:

```
*.log
*.aux
*.gz
*.toc
pdf*
*.tex.bak
svg-inkscape
```

## BibTEX

Para la bibliografía, un tema que es importante a la hora de realizar trabajos
de investigación, he usado principalmente el gestor bibliográfico
[Mendeley](https://www.mendeley.com/), que te ayuda a organizar y buscar tus
documentos bibliográficos y referencias. Nos lo explicaron en una sesión informativa
sobre los TFG organizada por la [Biblioteca](https://bib.us.es) de la
[Universidad de Sevilla](www.us.es), y la verdad es que me ha gustado bastante, sobre
después de que lo recomendaran también otros profesores investigadores de la facultad
a los que aprecio mucho, como es Rocio del Rio, de microelectrónica.

Mandeley también está disponible para Linux, pero también existen otros gestores
de biblografía que no conozco. Pues eso, que para combinar este gestor, o cualquier
otro, lo que yo hice es exportar la lista de libros, artículos y referencias que
tenía en una carpeta de Mendeley mediante el plug-in para LaTeX (BibTEX). Esto
te crea un artículo ```nombre.bib``` que lo guardas donde quieras, y luego lo
incluyes en el código para que automáticamente se genere la página de "Bibliografía",
con el formato adecuado (en mi caso especifiqué el que usan en la publicaciones de
[IEEE](https://ieeexplore.ieee.org/Xplore/home.jsp)), simplemente añadiendo ésta
línea a ```mi_estilo.sty```:

```
% BibTeX
\bibliographystyle{doc/myIEEEtran}
```
En el código LATEX, en el sitio donde queramos incluir nuestra página de bibliografía
simplemente debemos escribir:
```
\bibliography{doc/TFG}
```
indicando la ruta donde se encuentra el archivo que antes exportamos desde Mendeley,
mi caso se llama "TFG.bib" y está en el directorio doc/, junto a los artículos que
consulté.

Por último, con el objetivo de revisar la bibliografía y, como con las imágenes,
evitar olvidos y/o fallos, en el Makefile creé los siguientes comandos:
```
list_bibliography_available:
	cat doc/TFG.bib |grep ^@ |cut -d{ -f2 |cut -d, -f1

list_bibliography_used:
	grep -n "\cite" tex/*.tex
```
El primero lista todos los documentos exportados en el archivo .bib, y el
segundo busca en el código LATEX las citas a bibliografía que has incluído.

## Ponle una buena portada

Con Latex, lo bueno es que las posibilidades son casi infinitas, y además existe
una amplísima comunidad de gente haciendo cosas muy buenas y compartiéndolas. La
filosofía del software libre.

Para el caso concreto de la portada, puedes usar el típico comando básico:
```
\maketitle
```
Que si has especificado título, autor y fecha en la cabecera (antes de ```\begin{document}```),
te crea una página de título bastante simple pero correcta en muchos casos.
Pero para el TFG yo quería una portada un poco más personalizada, con el logo de
la universidad, y poder elegir dónde colocar título, autor, tutor, fecha...

En el Wikilibro de Latex que comenté antes hay una
[buena explicación](https://en.wikibooks.org/wiki/LaTeX/Title_Creation) sobre la
creación de títulos personalizados. Pero en concreto yo busqué alguna plantilla
en la que basarme. Hay una [página muy interesante con plantillas de LATEX](https://www.latextemplates.com),
en la que encontré una [plantilla que me gustó](https://www.latextemplates.com/template/academic-title-page).

Tras añadirle la foto y retocarla un poco, me quedó algo así:
![portada]({static}/images/tfg_titlepage.png)

También es verdad que esto de la portada depende de la Universidad, facultad o
incluso departamento, quizás en unos casos estás más obligado a seguir un estilo
específico o incluso te den una plantilla exacta. Ya cada cual que haga lo que
buenamente pueda o quiera.

# Consejos finales

Como recomendación final, solo tengo que deciros que lo importante es ir haciendo
cosas desde bien pronto, y no dejar que al final se te acumule todo con exémenes,
y otras asignaturas. Sé que esto es lo de siempre, y que al final a todos nos pasa.
A mí también pienso que podría haber acabado el trabajo un poco mejor con un poco
más de tiempo. Pero realmente no es que me faltara tiempo, porque hubo algunos
meses en los que hize muchísimo menos que en el último mes o últimas 2 semanas.
Sólo es cuestion de organizarse.

Por otro lado, os dejo un enlace a mi cuenta de GitHub, donde está accesible mi TFG
y todo el código LATEX bajo la licencia CreativeCommons CC-BY-SA-4.0, para que
podáis consultar realmente como lo he hecho y usarlo en vuestro trabajo, tras mencionarme,
como indican las siglas BY (by attributtion) de la licencia.

[https://github.com/cmolinaord/TFG](https://github.com/cmolinaord/TFG)

Espero que os sirva de ayuda, y ya sabéis, para cualquier duda, ponte en contacto
conmigo a través de lo que quieras, o deja un comentario aquí. También puedes pasarselo
a compañeros o compartirlo en tus redes.

Gracias!
