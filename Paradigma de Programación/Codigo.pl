%================================
% Problema Mahmoud and a Dictionary
%================================

% Sinonimos
synonym(love, like).
synonym(big, large).
synonym(happy, joyful).
synonym(smart, intelligent).
synonym(fast, quick).
synonym(small, tiny).
synonym(begin, start).
synonym(end, finish).
synonym(car, automobile).
synonym(child, kid).
synonym(home, house).
synonym(angry, mad).
synonym(pretty, beautiful).
synonym(sad, unhappy).
synonym(job, work).
synonym(student, pupil).
synonym(friend, buddy).
synonym(cold, chilly).
synonym(hot, warm).
synonym(buy, purchase).

% Antonimos
antonym(love, hate).
antonym(happy, sad).
antonym(big, small).
antonym(light, dark).
antonym(hot, cold).
antonym(fast, slow).
antonym(young, old).
antonym(rich, poor).
antonym(clean, dirty).
antonym(open, closed).
antonym(strong, weak).
antonym(early, late).
antonym(up, down).
antonym(good, bad).
antonym(inside, outside).
antonym(true, false).
antonym(friend, enemy).
antonym(day, night).
antonym(win, lose).
antonym(start, finish).

same(X, Y) :- synonym(X, Y).
same(X, Y) :- synonym(Y, X).

opposite(X, Y) :- antonym(X, Y).
opposite(X, Y) :- antonym(Y, X).

opposite(X, Z) :-
    same(X, Y),
    antonym(Y, Z).


answer(X, Y) :-
    same(X, Y),
    writeln('1 -> son sinonimos').

answer(X, Y) :-
    opposite(X, Y),
    writeln('2 -> son antonimos').

answer(X, Y) :-
    \+ same(X, Y),
    \+ opposite(X, Y),
    writeln('3 -> No tienen relacion').

main :-
    writeln('Prueba 1'),
    write('love y like ->'),
    answer(love, like),

    writeln('Prueba 2'),
    write('like y hate ->'),
    answer(like, hate),

    writeln('Prueba 3'),
    write('big y small ->'),
    answer(big, small),

    writeln('Prueba 4'),
    write('happy y joyful ->'),
    answer(happy, joyful),

    writeln('Prueba 5'),
    write('happy, sad ->'),
    answer(happy, sad),

    writeln('Prueba 6'),
    write('car y automobile ->'),
    answer(car, automobile),

    writeln('Prueba 7'),
    write('friend y enemy ->'),
    answer(friend, enemy),

    writeln('Prueba 8'),
    write('hot y cold ->'),
    answer(hot, cold),

    writeln('Prueba 9'),
    write('student y pupil ->'),
    answer(student, pupil),

    writeln('Prueba 10'),
    write('phone y computer ->'),
    answer(phone, computer).
