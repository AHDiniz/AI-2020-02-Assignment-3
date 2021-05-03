#!/usr/bin/python3.8

from pyknow import *

# Peixes: tubarão, arraia, baiacu, atum
# Anfíbios: sapo, salamandra
# Répteis: jacaré, cobra, tartaruga, camaleão
# Aves: pinguim, gavião, beija-flor, gaivota
# Mamíferos: baleia, morcego, humano, urso, cão

class AnimalClassifierEngine(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start")
    
    @Rule(Fact(action="start"))
    def ask_fish(self):
        self.declare(Fact(is_fish=input("O animal é um peixe? ")))
    
    @Rule(Fact(is_fish="S"))
    def ask_boned(self):
        self.declare(Fact(is_boned=input("O peixe é ósseo? ")))
    
    @Rule(Fact(is_boned="S"))
    def ask_poisoning(self):
        self.declare(Fact(is_poisoning=input("O peixe é venenoso? ")))
    
    @Rule(Fact(is_poisoning="S"))
    def return_baiacu(self):
        print("O animal é um baiacu.")
    
    @Rule(Fact(is_poisoning="N"))
    def return_atum(self):
        print("O animal é um atum.")

    @Rule(Fact(is_boned="N"))
    def ask_flat(self):
        self.declare(Fact(has_flat_body=input("O peixe tem corpo achatado? ")))
    
    @Rule(Fact(has_flat_body="S"))
    def return_arraia(self):
        print("O animal é uma arraia.")
    
    @Rule(Fact(has_flat_body="N"))
    def return_tubarao(self):
        print("O animal é um tubarão.")
    
    @Rule(Fact(is_fish="N"))
    def ask_reptile(self):
        self.declare(Fact(is_reptile=input("O animal é um réptil? ")))
    
    @Rule(Fact(is_reptile="S"))
    def ask_members(self):
        self.declare(Fact(has_four_members=input("O animal tem quatro membros? ")))
    
    @Rule(Fact(has_four_members="S"))
    def ask_scaled(self):
        self.declare(Fact(is_scaled=input("O animal é escamado? ")))

engine = AnimalClassifierEngine()
engine.reset()
engine.run()
