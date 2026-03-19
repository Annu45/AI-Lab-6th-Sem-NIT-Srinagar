% Facts
male(john).
male(paul).
male(mike).

female(mary).
female(lisa).
female(anna).

parent(john, paul).
parent(mary, paul).
parent(paul, mike).
parent(lisa, mike).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
