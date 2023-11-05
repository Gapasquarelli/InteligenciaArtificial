:- discontiguous pai/2.
:- discontiguous mae/2.
:- discontiguous casado/2.

% Fatos conhecidos da família Machado

% Pedro e Antonia são pais de João, Clara, Francisco e Ana
pai(pedro, joao).
pai(pedro, clara).
pai(pedro, francisco).
pai(pedro, ana).

mae(antonia, joao).
mae(antonia, clara).
mae(antonia, francisco).
mae(antonia, ana).

% Ana tem duas filhas, Helena e Joana
mae(ana, helena).
mae(ana, joana).

% João é pai do Mário
pai(joao, mario).

% Mário e Helena têm um filho, Carlos
pai(mario, carlos).
mae(helena, carlos).

% Francisco casou-se com Milene, mas não teve filhos
casado(francisco, milene).
casado(milene, francisco).

% Clara é mãe de Pietro e Enzo
mae(clara, pietro).
mae(clara, enzo).

% Pietro casou-se com Francisca, e Enzo casou-se com Antonia
casado(pietro, francisca).
casado(enzo, antonia).
casado(francisca, pietro).
casado(antonia, enzo).


% Pedro e Antonia são pais de João, Clara, Francisco e Ana
pai(pedro, joao).
pai(pedro, clara).
pai(pedro, francisco).
pai(pedro, ana).
mae(antonia, joao).
mae(antonia, clara).
mae(antonia, francisco).
mae(antonia, ana).

% Ana tem duas filhas, Helena e Joana
mae(ana, helena).
mae(ana, joana).

% João é pai do Mário
pai(joao, mario).

% Mário e Helena têm um filho, Carlos
pai(mario, carlos).
mae(helena, carlos).

% Francisco casou-se com Milene, mas não teve filhos
casado(francisco, milene).
casado(milene, francisco).

% Clara é mãe de Pietro e Enzo
mae(clara, pietro).
mae(clara, enzo).

% Pietro casou-se com Francisca, e Enzo casou-se com Antonia
casado(pietro, francisca).
casado(enzo, antonia).
casado(francisca, pietro).
casado(antonia, enzo).

% Regras de parentesco

% Avós
avo(Avo, Neto) :- pai(Avo, Pai), pai(Pai, Neto).
avo(Avo, Neto) :- mae(Avo, Pai), pai(Pai, Neto).
avo(Avo, Neto) :- pai(Avo, Mae), mae(Mae, Neto).
avo(Avo, Neto) :- mae(Avo, Mae), mae(Mae, Neto).

% Avô
avo_homem(Avo, Neto) :- avo(Avo, Neto), male(Avo).

% Avó
avo_mulher(Avo, Neto) :- avo(Avo, Neto), female(Avo).

% Tios e Tias
tio(Tio, Sobrinho) :- pai(Pai, Sobrinho), pai(Avo, Pai), pai(Avo, Tio), Tio \= Pai, male(Tio).
tio(Tio, Sobrinho) :- mae(Mae, Sobrinho), pai(Avo, Mae), pai(Avo, Tio), Tio \= Mae, male(Tio).
tia(Tia, Sobrinho) :- pai(Pai, Sobrinho), mae(Avo, Pai), mae(Avo, Tia), Tia \= Pai, female(Tia).
tia(Tia, Sobrinho) :- mae(Mae, Sobrinho), mae(Avo, Mae), mae(Avo, Tia), Tia \= Mae, female(Tia).

% Primos
primo(Primo, Pessoa) :- tio(Tio, Pessoa), pai(Tio, Primo), male(Primo).
primo(Primo, Pessoa) :- tia(Tia, Pessoa), mae(Tia, Primo), male(Primo).
prima(Prima, Pessoa) :- tio(Tio, Pessoa), pai(Tio, Prima), female(Prima).
prima(Prima, Pessoa) :- tia(Tia, Pessoa), mae(Tia, Prima), female(Prima).

% Descendentes
descendente(Des, Anc) :- pai(Anc, Des).
descendente(Des, Anc) :- mae(Anc, Des).
descendente(Des, Anc) :- pai(X, Des), descendente(X, Anc).
descendente(Des, Anc) :- mae(X, Des), descendente(X, Anc).

% Ascendentes
ascendente(Anc, Des) :- descendente(Des, Anc).

%Generos
male(pedro).
male(joao).
male(francisco).
male(mario).
male(pietro).
male(enzo).
male(carlos).

female(antonia).
female(clara).
female(ana).
female(helena).
female(joana).
female(milene).
female(francisca).


