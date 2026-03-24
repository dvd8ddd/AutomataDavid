# AutomataDavid
El lenguaje elegido para esta evidencia es el lenguaje elven, tambien conocido como lenguaje Élfico el cual fue creado por J.R.R Tolkien para los elfos de la película El señor de los Anillos. Este no solo es un idioma, sino un conjunto de lenguas, entre las que destacan el quenya y el sindarin. Estas lenguas fueron diseñadas ccn estructuras complejas, incluyendo reglas gramaticales y sistemas de escritura propios y su principal característica es que suena elegante y antiguo. (Tolkien and Elvish Writing, 2019).

Las palabras en elven son:

-Calen

-Calma

-Carca

-Celeb

-Certar


| Estado | Entrada| Siguiente |
| ------------ | ------------ | ------------ |
| q0 | c | q1
| q1 | a | q2
| q1 | e | q11
| q2 | l | q3
| q2 | r | q8
| q3 | e | q4
| q3 | m | q6
| q4 | n | q5
| q6 | a | q7
| q8 | c | q9
| q9 | a | q10
| q11 | l | q12
| q11 | r | q15
| q12 | e | q13
| q13 | b | q14
| q15 | t | q16
| q16 | a | q17
| q17 | r | q18

Estados de aceptación:
q5,q7,q10,q14,q18

Recorrido de cada palabra:

-Calen:
q0,q1,q2,q3,q4,q5

-Calma:
q0,q1,q2,q3,q6,q7

-Carca:
q0,q1,q2,q8,q9,q10

-Celeb:
q0,q1,q11,q12,q13,q14

-Certar:
q0,q1,q11,q15,q16,q17,q18

Palabras aceptadas:

calen

calma

carca

celeb

certar

Palabras rechazadas:
cale

calena

caleb

carce

cele

certa

casa

calor

celebb

Tabla de Resultados:

| Cadena | Resultado |
| ------------ | ------------ |
| calen  | Aceptada |
| calma  | Aceptada |
| carca | Aceptada |
| celeb  | Aceptada |
| certar  | Aceptada |
| cale  | Rechazada |
| calena  | Rechazada |
| caleb  | Rechazada |
| carce  | Rechazada |
| cele  | Rechazada |
| certa  | Rechazada |
| casa  | Rechazada |
| calor  | Rechazada |
| calebb  | Rechazada |

Imagen del autómata:
![AutomataDavid](https://github.com/user-attachments/assets/ed689f69-e581-4932-bc2c-f8acb523783a)

Explicación del diseño:

De acuerdo con GeeksforGeeks (2026), un autómata finito reconoce cadenas por medio de estados, transiciones y estados de aceptación. Con base a esto, el diseño de este autómata se hizo agrupando las palabras según los prefijos que comparten. Todas las palabras comienzan con C, por lo que el estado inicial es q0 despues pasa a q1. Posteriormente el autómata se divide en dos ramas; una con las palabras que comienzan con CA y la otra que empieza con CE.

En la rama CA se reconocen calen, calma y carca mientras que en la otra rama (CE) se reconoce celeb y certar. Los estados finales del autómata son q5, q7, q10, q14 y q18 representan el final de cada palabra válida. Así que el autómata permite reconocer únicamente las palabras definidas y rechaza cualquier otra cadena que no siga esas transiciones.

Buenas prácticas y complejidad:

En la implementación del autómata en prolog se siguieron buenas prácticas de programación ya que el código se organizó de manera clara. Primero se definieron las transiciones del autómata, después los estados finales y finalmente los predicados encargados de validar las cadenas. Se utilizaron nombres como transition, final_state, recover_automaton y automatonCheck, lo que facilita la lectura y comprensión del programa.

Codigo de la expresion regular:

^(calen|calma|carca|celeb|certar)$

Programación y pruebas de la expresion regular:

La expresión regular se programó para reconocer únicamente las palabras válidas del lenguaje elven (calen, calma, carca, celeb y certar). El símbolo ^ indica el inicio de la cadena, () indica el grupo de caracteres, el operador | permite elegir entre distintas palabras válidas y por último $ indica el final de la cadena.

Evaluar soluciones:

La solución mediante el autómata resultó correcta, ya que aceptó únicamente las palabras válidas del lenguaje definido: calen, calma, carca, celeb y certar. En las pruebas realizadas también rechazó correctamente las cadenas inválidas como cale, calena,caleb, carce, cele, certa, casa, calor, celebb. 
Por otra parte, la solución con expresión regular también fue adecuada ya que reconoció exactamente las mismas palabras válidas y rechazó las palabras incorrectas. Esto demuestra que ambas representaciones describen el lenguaje de forma consistente.

Comparar soluciones:

El autómata finito y la expresión regular son dos formas de representar el mismo lenguaje. El autómata permite ver con mayor claridad los estados, las transiciones y el recorrido de cada cadena, mientras que la expresión regular resume el lenguaje de mejor forma más compacta (GeeksforGeeks, 2026). 
Además la University of Illinois explica que los lenguajes regulares pueden representarse mediante DFA (autómata finito determinista) o NFA (autómata finito no determinista) o una expresión regular, lo que confirma que ambas soluciones utilizadas son válidas. (University of Illinois,2013).

Conclusiones 

En este trabajo se comprobó que el lenguaje propuesto puede representarse tanto con un autómata finito como una expresión regular. Ambas soluciones aceptaron correctamente las palabras válidas y rechazaron las cadenas incorrectas, por lo que resultaron adecuadas para describir el lenguaje definido.

El autómata finito se entiende mejor porque se puede dibujar y ver como funciona paso a paso, en cambio, la expresión regular es más corta y directa, por lo que resulta útil para escribir el código de forma más simple o para usarlo en programación (GeeksforGeeks,2026) . En general, este trabajo ayudó a comprender cómo se aplican los lenguajes regulares mediante dos herramientas distintas pero equivalentes.


Referencias

GeeksforGeeks. (2026, 7 de marzo). Introduction of finite automata.
https://www.geeksforgeeks.org/theory-of-computation/introduction-of-finite-automata/

Gonzalez, T. (2024). Diseño de Autómatas Finitos Deterministas (DFA): una guía completa. ACADEMIA SANROQUE. https://academiasanroque.com/diseno-de-automatas-finitos-deterministas-dfa-una-guia-completa/

Valdés Aguirre (2025). Automata and Prolog:
https://docs.google.com/document/d/1RMGCGPHs4aLyfOTcwZJHSzQQlBP1uJYJe72jLIdcO7g/edit?tab=t.0

University of Illinois (2013). Equivalence of finite automata and regular expressions:
https://courses.grainger.illinois.edu/cs373/fa2013/Lectures/lec07.pdf

Eibe Frank. (s. f.). En Chapter 6 Formal Language Theory
https://www.its.caltech.edu/~matilde/FormalLanguageTheory.pdf 

Viewsproject, (2019). Tolkien and Elvish Writing. https://crewsproject.wordpress.com/2019/07/29/tolkien-and-elvish-writing/

