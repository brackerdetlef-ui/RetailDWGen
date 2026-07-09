============================================================
RetailDWGen
Nummernkreise
============================================================

HAUPTVERWALTUNG
===============

000     Hauptverwaltung / Zentrale


FILIALEN
=========

100     Filiale 1
200     Filiale 2
300     Filiale 3
...
10000   Filiale 100

Schema

Filialcode = Filialnummer × 100


LAGER
======

101     Hauptlager Filiale 1
201     Hauptlager Filiale 2
301     Hauptlager Filiale 3

110     Verkaufslager Filiale 1
111     Verkaufslager Filiale 1 - Bereich 1
112     Verkaufslager Filiale 1 - Bereich 2
113     Verkaufslager Filiale 1 - Bereich 3

210     Verkaufslager Filiale 2
211     Verkaufslager Filiale 2 - Bereich 1
212     Verkaufslager Filiale 2 - Bereich 2
213     Verkaufslager Filiale 2 - Bereich 3

120     Retourenlager Filiale 1
121     Retourenlager Bereich 1
122     Retourenlager Bereich 2

130     Kommissionierung Filiale 1
131     Kommissionierung Bereich 1

140     Sperrlager Filiale 1
141     Sperrlager Bereich 1


ALLGEMEINES SCHEMA
==================

XX00    Filiale
XX01    Hauptlager

XX10    Verkaufslager
XX11    Verkaufslager Bereich 1
XX12    Verkaufslager Bereich 2
XX13    Verkaufslager Bereich 3

XX20    Retourenlager
XX21    Retourenlager Bereich 1

XX30    Kommissionierung

XX40    Sperrlager

XX50    Kühl-/Tiefkühllager

XX60    Wareneingang

XX70    Warenausgang

XX80    Inventur

XX90    Reserve

============================================================
Diese Datei dokumentiert ausschließlich die fachlichen
Nummernkreise von RetailDWGen.

Die Organisationsstruktur (Verkauf, Einkauf,
Materialwirtschaft usw.) wird in 'organisation.yaml'
definiert.
============================================================
