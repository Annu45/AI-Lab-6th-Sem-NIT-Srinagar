start :-
    write('Do you have fever? (yes/no): '), read(Fever),
    write('Do you have cough? (yes/no): '), read(Cough),
    write('Do you have headache? (yes/no): '), read(Headache),
    diagnose(Fever, Cough, Headache).

diagnose(yes, yes, yes) :-
    write('You may have Flu.'), nl.

diagnose(yes, yes, no) :-
    write('You may have Cold.'), nl.

diagnose(no, no, yes) :-
    write('You may have Migraine.'), nl.

diagnose(_, _, _) :-
    write('Consult a doctor.'), nl.
