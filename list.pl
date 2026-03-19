% Length
len([], 0).
len([_|T], N) :- len(T, N1), N is N1 + 1.

% Sum
sum([], 0).
sum([H|T], S) :- sum(T, S1), S is S1 + H.

% Membership
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% Sorted check
sorted([]).
sorted([_]).
sorted([A,B|T]) :- A =< B, sorted([B|T]).

% Append
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).
% -------- CONCATENATE TWO LISTS ---
concatenate([], L, L).
concatenate([H|T], L2, [H|R]) :-
    concatenate(T, L2, R).

