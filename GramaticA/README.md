#David ALejandro Robles Camacho A01277315

El Quenya es el idioma de los Altos Elfos, los Noldor, quienes viajaron a la Tierra Media desde Valinor. Para el habla o comunicación cotidiana entre los elfos, el idioma fue reemplazado en gran medida por su lengua hermana, el Sindarin. Por esta razón, Tolkien lo consideraba una especie de “latin-élfico”, utilizado principalmente en contextos formales, literarios y rituales.(Tolkien, 1954; Noel, 1974). 

Generalmente se dividen las etapas del desarrollo del Quenya en tres periodos:
-Qenya Temprano (1910s-1920s)
-Quenya Medio (1930s-1940s)
-Quenya Tardío (1950s-1972)

Esta evolución muestra como Tolkien fue modificando y refinando el idioma a lo largo del tiempo dentro de su obra.

Como primer idioma con un sistema de escritura, el Quenya tenía una extensa tradición literaria, mayor que la de otros idiomas élficos. El Quenya se mantuvo como idioma de los eruditos, que se fue extendiendo y llegó especialmente a los Numenoreanos. El idioma también era un idioma ritual prominente en la academia y la religión.

Estructura Gramatical:

El quenya es principalmente un idioma “aglutinante”, un término lingüístico para idiomas que modifican palabras con numerosos sufijos que alteran el significado, a diferencia del inglés que es un idioma “aislante” con pocos sufijos gramaticales.

Reglas del plural:
El plural se forma principalmente agregando sufijos a la raíz del sustantivo. Los sufijos más comunes son -r, -i y -li. En general, -r se usa con palabras que terminan en vocal, mientras que -i aparece en otros tipos de sustantivos. El sufijo -li se relaciona con una forma plural partitiva. Esto coincide con la idea de que el Quenya es un idioma aglutinante, donde las palabras cambian mediante terminaciones.(Gilson, 1996; Tolkien Gateway, s.f.). 

Ejemplo:
nara: narar
dor: dori
rima: rimali

Conjunciones
ar: y
hya: o


Orden de palabras:
El Quenya era un idioma aglutinante con orden SVO (sujeto-verbo-objeto). Esto significa que primero aparece quien realiza la acción, después el verbo y finalmente el elemento que recibe la acción.

Ejemplo: 
narar martir lumar
sujeto: narar
verbo: martir
objeto: lumar

Sustantivos: 
En Quenya, los sustantivos nombran personas, objetos o lugares y pueden cambiar mediante sufijos para indicar número, como singular o plural.
elen → estrella
aran → rey
cirya → barco / nave
alda → árbol
taurë → bosque / selva
macil → espada
lassë → hoja
nér → hombre / varón


Verbos:

Se dividen en tres grupos: 
-Los verbos básicos derivados de una raíz verbal primitiva
-Los verbos derivados añadiendo un sufijo verbal a otra raíz
-Los verbos u o a, que tienen una adición vocálica a la raíz. 

Ejemplo:
mat= comer
cen=ver
tec=escribir
nor=correr
tulta=convocar, enviar a buscar
laita= alabar, bendecir
orya= levantarse, surgir
liru= cantar alegremente

Para este proyecto se toma una versión simplificada de estas características, enfocándose únicamente en la estructura básica de sujeto, verbo y objeto, así como en el uso de algunos sustantivos, verbos y conjunciones. 


Gramática:
El análisis de oraciones dentro de una gramática se relaciona con una de las fases fundamentales en el procesamiento del lenguaje: el análisis sintáctico. Esta etapa se encarga de verificar si una secuencia de oraciones cumple con las reglas definidas por una gramática formal, a diferencia del análisis léxico, que únicamente identifica los elementos básicos de la entrada.

En este proyecto se emplea una gramática libre de contexto, la cual permite describir la estructura de un lenguaje. En el caso del Quenya, estas estructuras pueden entenderse a partir de estudios lingüísticos como La lengua de los Elfos: una gramática para el quenya de J.R.R Tolkien de González Baixauli, donde se describen las bases gramaticales del idioma y su organización (González Baixauli, s.f.). 

El analizador sintáctico toma una oración, la descompone en tokens y determina si puede generarse a partir de dichas reglas. Si la estructura es válida, se construye un árbol sintáctico que representa la jerarquía de la oración. (Jurafsky & Martin, 2009). 

Para garantizar su funcionamiento adecuado, la gramática debe diseñarse de forma clara y sin ambigüedades, evitando que una misma entrada produzca múltiples interpretaciones. Esto facilita la construcción del árbol sintáctico y permite representar de manera ordenada la relación entre los elementos del lenguaje (Aho et al., 2006). 

Gramatica inicial:
Imagen del autómata:
![gramatica]
La gramática propuesta permite formar oraciones simples a partir de un sujeto, un verbo y en algunos casos un objeto. Su regla principal permite dos estructuras: una oración completa con objeto y una oración corta sin objeto. Esto hace que el lenguaje sea fácil de analizar y adecuado para representar ejemplos básicos.

El elemento NSC se utiliza para presentar un grupo nominal este grupo puede estar formado por un solo sustantivo o por varios sustantivos que están unidos mediante conectores como ar y hya. 

Ejemplo:
angmari hosta valnori hya arnori ar istari

En este ejemplo hay más de un conector, lo que genera confusión. Por esta razón, es importante revisar la gramática y asegurarse de que las reglas generen árboles sintácticos claros.


Complejidad y jerarquía de Chomsky:
La gramática que se usó en el proyecto es una gramática libre de contexto, también conocida como tipo 2 en la jerarquía de Chomsky. Esto se debe a que del lado izquierdo de cada regla siempre hay un solo símbolo, no terminal, mientras que del lado derecho puede haber varios símbolos ya sean terminales o no terminales.
No se considera una gramática regular porque algunas reglas tiene  más de un elemento del lado derecho:
Ejemplo:
NSC -> NSCP NSC_A 
Esta gramática se adapta mejor como CFG ya que permite representar estructuras un poco más completas, como sujeto, verbo, objeto y conjunciones.

Ambigüedad y recursión izquierda:
En la gramática se redujo la ambigüedad al definir una estructura clara para las conjunciones. La regla NSC_A -> Conj NSCP NSC_A | Empty permite agregar más sustantivos de forma ordenada, evitando que una misma oración tenga varias interpretaciones posibles. De esta manera, cada oración válida genera un árbol sintáctico más consistente.
Además, en el código se evita la recursión izquierda, ya que puede generar problemas en el análisis sintáctico. En su lugar se utiliza la recursión hacia la derecha, lo que permite procesar oraciones de forma más ordenada y facilita la construcción del árbol sintáctico

Explicación gramatical:
La gramática implementada corresponde a un gramática libre de contexto, ya que todas sus reglas siguen la forma A→ α , donde un símbolo no terminal se sustituye por una combinación de terminales y no terminales.
La estructura principal del lenguaje se define mediante la regla:
S → NSC VS NSC | NSC VS 
Esto indica que una oración puede formarse por un sujeto, un verbo y un objeto. Esta estructura sigue el orden SVO.
NSC representa un grupo donde puede estar compuesto por uno o varios sustantivos:
Esto se logra mediante las reglas:
NSC → NSCP NSC_A
 NSC_A → Conj NSCP NSC_A | Empty
Estas reglas permiten que los sustantivos se unan mediante conjunciones como ar y hya.
NSCP representa un sustantivo simple:
NSCP–NS
A su vez, los sustantivos que están representados como NS se dividen en tres tipos y cada una tiene sus propias combinaciones::
.Vo: sustantivos que terminan en vocal, su combinación es VoR VoE
E: raíces cortas, su combinación es ER EE
C: raíces más complejas y largas, su combinación es CR CE
Estas terminaciones permiten generar formas como plural o variaciones simples mediante sufijos como r, i o li, reflejando la naturaleza aglutinante del lenguaje.
Los verbos (VS) representan acciones dentro de la oración y forman el núcleo del predicado. Ejemplos de estos son: martir, harya, hosta, síla, entre otros.
Finalmente, el símbolo EMPTY representa una producción vacia, lo que permite que ciertas  reglas sean opcionales dentro de la gramática

Implementación:
Para llevar a cabo la creación del árbol sintáctico y de la gramática se creo un código en el lenguaje Python, que previamente nos proporcionó el profesor para guiarnos
Oraciones correctas:
narar martir lumar → los fuegos actúan sobre las nubes
selar harya tular → las luces tienen llegadas
vasali hosta rimali → los aires reúnen bordes
sorar síla → los vientos brillan
tilali savin yarali → las chispas conocen las sangres
dori martir sili → las tierras actúan sobre los brillos
dore harya tale → la tierra tiene pies
doreli hosta miri → las tierras reúnen joyas
lini síla → los cantos brillan
galeli savin tiri → las luces conocen vigilancias
beli martir cari → las fuerzas actúan sobre acciones
bele harya care → la fuerza tiene acción
beleli hosta careli → las fuerzas reúnen acciones
tiri síla → las vigilancias brillan
mire savin lini → la joya conoce los cantos
balrogi martir gondori → los demonios de fuego actúan sobre los reinos
thandori harya istari → los escudos tienen magos
morguli hosta valnori → las magias oscuras reúnen protectores
gondorli síla → los reinos brillan
istari savin durini → los magos conocen a los reyes enanos
angmari martir belgari → las tierras oscuras actúan sobre guerreros
belgarli harya arnorli → los guerreros tienen reinos antiguos
valnori hosta balrogli → los protectores reúnen demonios de fuego
arnori síla → los reinos antiguos brillan
durinli savin morgulli → los reyes enanos conocen magias oscuras
narar martir lumar ar selar → los fuegos actúan sobre las nubes y las luces
vasali hosta rimali ar tilali → los aires reúnen bordes y chispas
dori martir sili hya lini → las tierras actúan sobre los brillos o los cantos
balrogi harya gondori ar istari → los demonios de fuego tienen reinos y magos
angmari hosta valnori hya arnori → las tierras oscuras reúnen protectores o reinos antiguos

Se incluye una gran cantidad de oraciones dentro del programa con el objetivo de probar de manera más completa el funcionamiento de la gramática. Y al tener múltiples ejemplos, es posible verificar que las reglas definidas funcionan correctamente.
Oraciones incorrectas:
narar corre lumar
martir narar lumar
sorar lumar síla
dori ar martir sili
balrogi harya ar istari
gondori savin istari ar
valnori hya hosta arnori

Interpretación de resultados: 
Los resultados muestran que la gramática funciona correctamente. Las oraciones válidas generan un árbol sintáctico, mientras que las oraciones incorrectas son rechazadas por el programa.


Buenas prácticas:
El código usa funciones para separar partes del programa como separate() para dividir palabras con terminaciones y analyze() para revisar si una oración es válida. También se incluyen pruebas automáticas con oraciones correctas e incorrectas, lo que facilita comprobar que la gramática funciona.

Analysis
ANÁLISIS ASINTÓTICO:
Primero, es importante mencionar que algunas palabras del lenguaje deben separarse en raíz y terminación para que la gramática pueda reconocerlas correctamente. Por ejemplo, una palabra como narar se transforma en nara r. Esto se hace dentro de la función separate(), donde el programa revisa las palabras ingresadas y reemplaza aquellas que tienen una terminación definida.
Antes de iniciar, es importante mencionar que algunas palabras del lenguaje deben separarse en raíz y terminación para que la gramática pueda reconocerlas correctamente. Por ejemplo, una palabra como narrar se transforma en nara r. Esto se hace dentro de la función separate(), donde el programa revisa las palabras ingresadas y reemplaza aquellas que no tienen una terminación definida.
Este proceso utiliza un ciclo que recorre el diccionario de terminaciones, por lo que su complejidad depende de las palabras registradas en el diccionario.
En las pruebas automáticas, el programa recorre la lista de oraciones con un ciclo for y analiza cada una con el parser. Como la gramática no genera múltiples árboles por oración válida, la complejidad general se mantiene en O(n)

Otros métodos:
Por supuesto existen otras formas de implementar este tipo de programa. Se podrían utilizar otras librerías de Python o incluso otros lenguajes de programación como JS. Una alternativa sería usar herramientas para crear parsers, como Peggy en Node.JS , donde la gramática se define en un archivo separado.

Sin embargo, para este proyecto se eligió Python con NLTK porque permite definir la gramática y analizar las oraciones dentro de un mismo archivo. Lo que facilita la visualización. Además NLTK incluye herramientas para trabajar con gramáticas libres de contexto y generar árboles sintácticos. 

En conclusión, usar Python y NLTK fue una opción adecuada porque permite implementar la gramática de forma clara, probar oraciones válidas e inválidas, y visualizar los árboles sintácticos de manera directa. En lo personal algo que me ayudó a concluir el programa es que las funciones de Python son muy intuitivas.











































Referencias

Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). Compilers: Principles, techniques, and tools (2nd ed.). Pearson.
https://www.pearson.com/en-us/subject-catalog/p/compilers-principles-techniques-and-tools/P200000003472

Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed. draft). Stanford University.
https://web.stanford.edu/~jurafsky/slp3/

Gilson, C., Hostetter, C. F., Wynne, P., & Smith, A. R. (Eds.). (1988–presente). Vinyar Tengwar. Elvish Linguistic Fellowship.
https://www.elvish.org/VT/

González Baixauli, L. (1999). La lengua de los Elfos: Una gramática para el quenya de J.R.R. Tolkien: Tengwesta kwenyava. Minotauro. 
https://research.ebsco.com/c/oefy3m/search/details/dtl4tfmgur/details?q=Lengua+de+los+Elfos
Mccullough, B. (s.f.). Frases y vocabulario en élfico. Scribd. https://es.scribd.com/doc/247032936/Palabras-en-Elfico?utm_source=

Fandom. (s.f.). Elvish word list. The One Wiki to Rule Them All.
https://lotr.fandom.com/wiki/Elvish_word_list?utm_source=

Tolkien Gateway. (s.f.). Quenya/Grammar.
https://tolkiengateway.net/wiki/Quenya/Grammar 
