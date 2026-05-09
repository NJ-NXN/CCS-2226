% Define the genders
male(arthur).
male(bob).
male(charlie).
male(frank).
male(harry).

female(martha).
female(diana).
female(eve).
female(grace).

% Define parent relationships ( parent(Parent, Child) )
% Generation 1 (Grandparents) to Generation 2 (Parents/Aunts/Uncles)
parent(arthur, bob).
parent(arthur, charlie).
parent(arthur, diana).
parent(martha, bob).
parent(martha, charlie).
parent(martha, diana).

% Generation 2 to Generation 3 (Grandchildren)
% Bob's kids
parent(bob, eve).
parent(bob, frank).

% Diana's kids
parent(diana, grace).
parent(diana, harry).
% (Charlie has no kids in this tree)


% Defining the complex family logic 
% The ':-' symbol means "IF". The ',' symbol means "AND".

% 1. Child
child(Child, Parent) :- 
    parent(Parent, Child).

% 2. Grandparent
grandparent(Grandparent, Grandchild) :- 
    parent(Grandparent, Parent), 
    parent(Parent, Grandchild).

% 3. Grandchild
grandchild(Grandchild, Grandparent) :- 
    grandparent(Grandparent, Grandchild).

% 4. Sibling (They share a parent, and X is not the same person as Y)
sibling(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

% 5. Uncle (An uncle is a male sibling of someone's parent)
uncle(Uncle, Person) :- 
    male(Uncle), 
    sibling(Uncle, Parent), 
    parent(Parent, Person).

% 6. Aunt (An aunt is a female sibling of someone's parent)
aunt(Aunt, Person) :- 
    female(Aunt), 
    sibling(Aunt, Parent), 
    parent(Parent, Person).

% 7. Cousin (A cousin is the child of a parent's sibling)
cousin(Cousin, Person) :- 
    parent(Parent1, Person), 
    sibling(Parent1, Parent2), 
    parent(Parent2, Cousin).