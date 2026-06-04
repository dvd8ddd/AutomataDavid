El problema que escogí se llama Mahmoud and a Dictionary. En este problema se tiene un conjunto de palabras y diferentes relaciones entre ellas. Las relaciones pueden indicar que dos palabras son sinónimos o que son antónimos. A partir de estas relaciones iniciales, el sistema debe ser capaz de deducir nuevas relaciones automáticamente usando lógica transitiva (Russell & Norvig, 2020, p. 258). 

Por ejemplo: “happy” es un sinónimo de “joyful” y “joyful” es un antónimo de “sad”, entonces automáticamente “happy” también será antónimo de “sad”.

Lo más importante del problema es revisar que no se generen contradicciones. Puede ocurrir que se intente agregar una relación que rompa la consistencia del conocimiento almacenado. (Brachman & Levesque, 2004, p. 41). 

Ejemplo: Si previamente se sabía que dos palabras eran opuestas y después se intenta registrar que significan lo mismo, esa nueva relación debe rechazarse. 

El programa tiene que responder YES cuando una relación es válida y no cuando genera contradicción. Al final también se deben responder consultas indicando si dos palabras son sinónimos, antónimos o si no existe relación conocida entre ellas.

Decidí escoger este problema sacado de Codeforces usando programación lógica en Prolog porque el comportamiento del problema se parece mucho a una base de datos, me refiero a que tiene algo ya escrito o justificado y solo se tiene que mandar a llamar para verificar que si exista una relación. Cada relación puede representarse como un hecho y las inferencias se pueden obtener mediante reglas lógicas. Lo que permite que Prolog deduzca automáticamente nuevas relaciones sin necesidad de programar una por una.

Ejemplo:
love sinónimo de like=YES
like antónimo de hate=YES
love antónimo de hate= inferido automáticamente
love sinónimo de hate= NO

**Modelo de la solución:**

Para resolverlo usé programación lógica en Prolog, porque el problema se puede representar fácilmente con hechos y reglas. En lugar de usar estructuras avanzadas como Union-Find con paridades, representé directamente las relaciones entre palabras mediante predicados dinámicos.

synonym(X, Y).
antonym(X, Y).

Donde synonym(X, Y) significa que dos palabras son sinónimas y antonym(X, Y) significa que dos palabras son antónimas. El programa incluye 20 pares de sinónimos y 20 pares de antónimos.

synonym(love, like).
antonym(love, hate).

**Reglas de inferencia**

Con estos hechos, Prolog puede sacar conclusiones sin tener que escribir cada caso manualmente

same(X, Y) :- synonym(X, Y).
same(X, Y) :- synonym(Y, X).
opposite(X, Y) :- antonym(X, Y).
opposite(X, Y) :- antonym(Y, X).

Las reglas same y opposite hacen que las relaciones sean simétricas, si A es sinónimo de B, entonces B también es sinónimo de A, sin necesidad de declararlo dos veces.

También se agregan reglas transitivas. Por ejemplo, si x es sinónimo de Y y Y es antónimo de Z:

opposite(X,Z) :-
      same(X, Y),
      antonym(Y, Z).


Esto permite deducir automáticamente que happy es antónimo de sad, porque happy es sinónimo de joyful, o que hablando de otro ejemplo like es antónimo de hate porque like es sinónimo de love y love es antónimo de hate.

**Respuesta**
El predicado answer/2 clasifica la relación entre dos palabras e imprime:
answer(X, Y) :-
    same(X, Y),
    writeln('1 -> son sinonimos').
answer(X, Y) :-
    opposite(X, Y),
    writeln('2 -> son antonimos').
answer(X, Y) :-
    \+ same(X, Y),
    \+ opposite(X, Y),
    writeln('3 -> No tienen relación').

\+ es el operador de negación por falla

Si no existe ninguna relación conocida entre dos palabras (como phone y computer), el sistema responde con la opción 3 usando negación por falla, que es una forma de razonamiento por omisión de Prolog.

**Ejecución con main**
El predicado main/0 ejecuta 10 pruebas que demuestran los tres casos posibles:

| Prueba | Par              | Resultado esperado |
|---------|------------------|--------------------|
| 1       | love / like      | Sinónimos          |
| 2       | like / hate      | Antónimos          |
| 3       | big / small      | Antónimos          |
| 5       | happy / sad      | Antónimos          |
| 10      | phone / computer | Sin relación       |

Con esto, el programa no solo guarda relaciones directas,  sino que tambien puede deducir otras por medio de reglas; si se consulta una relación que no fue declarada como tal pero se puede obtener mediante sinónimos o antónimos. Prolog la encuentra automáticamente. Si no existe ninguna relación ni directa , ni inferida el sistema lo indica sin generar una contradicción.



**Complejidad de tiempo**
En cuanto a la complejidad, cada consulta se puede aproximar a O(1) , porque la base de conocimiento o de "datos" para decirlo de forma más sencilla tiene una cantidad fija de hechos y reglas. En otras palabras no crece dependiendo de lo que escriba el usuario, solo revisa lo que ya está declarado. Aunque Prolog internamente revisa los hechos y reglas que ya fueron declarados previamente para encontrar una coincidencia. Por eso, el tiempo de búsqueda puede considerarse constante. De igual manera, la complejidad espacial también es O(1) debido a que el espacio utilizado en la memoria permanece fijo y no aumenta dependiendo del número de consultas realizadas (Clocksin & Mellish, 2003).


**Comparación con paradigma imperativo**

Otra forma de resolver este problema sería usando programación imperativa por ejemplo en C++ o en Java. En ese caso se podrían usar arreglos, grafos o una estructura Union-Find para guardar las relaciones entre palabras. Esta opción puede ser más rápida cuando hay muchos datos, pero también hace que el código sea más largo y un tanto difícil de manejar, porque las relaciones e inferencias se tienen que controlar manualmente con ciclos y condiciones.

En cambio, con Prolog las relaciones pueden modelarse directamente como hechos y reglas lógicas. Esto hace que la solución sea más sencilla de leer, ya que Prolog puede deducir automáticamente nuevas relaciones mediante inferencia lógica.

**Referencias**


Codeforces. (2016). Mahmoud and a Dictionary (Problem 766D). https://codeforces.com/problemset/problem/766/D 


Alonso Jiménez, J. A. (2006). Introducción a la programación lógica con Prolog. https://www.cs.us.es/~jalonso/pub/2006-int_prolog.pdf 


Tutorial Prolog – Paradigmas de programación. https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/tutoriales/prolog-gh-pages/TutorialProlog2017I.pdf 


¿Qué es la programación lógica y por qué es importante? https://keepcoding.io/blog/que-es-la-programacion-logica/ 


Clocksin, W. F., & Mellish, C. S. (2003). Programming in Prolog: Using the ISO standard (5th ed.). Springer.  https://link.springer.com/book/10.1007/978-3-642-55481-0 


Russell, S., & Norvig, P. (2021). Artificial intelligence: A modern approach (4th ed.). Pearson. https://aima.cs.berkeley.edu 


Sterling, L., & Shapiro, E. (1994). The art of Prolog (2nd ed.). MIT Press. 
https://mitpress.mit.edu/9780262691635/the-art-of-prolog/ 


Deransart, P., Ed-Dbali, A., & Cervoni, L. (1996). Prolog: The standard: Reference manual. Springer.https://research.ebsco.com/c/oefy3m/search/details/o7hjbgng3b?q=prolog


