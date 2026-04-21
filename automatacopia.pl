transition(q0,c,q1).
transition(q1,a,q2).
transition(q1,e,q11).
transition(q2,l,q3).
transition(q2,r,q8).
transition(q3,e,q4).
transition(q3,m,q6).
transition(q4,n,q5).
transition(q6,a,q7).
transition(q8,c,q9).
transition(q9,a,q10).
transition(q11,l,q12).
transition(q11,r,q15).
transition(q12,e,q13).
transition(q13,b,q14).
transition(q15,t,q16).
transition(q16,a,q17).
transition(q17,r,q18).

%Estados finales
final_state(q5).
final_state(q7).
final_state(q10).
final_state(q14).
final_state(q18).

%para revisar una cadena 
recover_automaton(ListtoCheck) :-
    automatonCheck(ListtoCheck, q0).

%Caso base
automatonCheck([], InitialState) :-
    final_state(InitialState).

automatonCheck([Symbol | RestofList], InitialState):-
    transition(InitialState, Symbol, NextState),
    automatonCheck(RestofList, NextState).






