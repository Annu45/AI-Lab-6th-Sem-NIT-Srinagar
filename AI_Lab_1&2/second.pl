symptom(john,fever).
symptom(john,cough).
symptom(john,headache).

symptom(mary,sneezing).
symptom(mary,runny_nose).

diagnosis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, headache).

diagnosis(Patient, cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

diagnosis(Patient, allergy) :-
    symptom(Patient, sneezing),
    symptom(Patient, fever).
%?- diagnosis(john,Disease). %Disease = flu
%?- diagnosis(mary,Disease). %Disease=cold. %Disease=allergy
