% Facts: student(Name, CGPA, Income, Category)

student(annu, 8.5, 250000, obc).
student(rahul, 7.2, 200000, general).
student(sneha, 9.1, 400000, sc).
student(amit, 6.8, 150000, st).
student(priya, 8.2, 500000, general).

% Rule 1: Merit-based eligibility
merit_eligible(Name) :-
    student(Name, CGPA, _, _),
    CGPA >= 8.0.

% Rule 2: Income-based eligibility
income_eligible(Name) :-
    student(Name, _, Income, _),
    Income =< 300000.

% Rule 3: Reserved category eligibility
reserved_category(Name) :-
    student(Name, _, _, Cat),
    member(Cat, [sc, st, obc]).

% Final combined scholarship eligibility
scholarship(Name) :-
    merit_eligible(Name);
    income_eligible(Name);
    reserved_category(Name).
