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
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_poisoning="N"))
    def return_atum(self):
        print("O animal é um atum.")
        self.declare(Fact(ask_to_repeat="S"))

    @Rule(Fact(is_boned="N"))
    def ask_flat(self):
        self.declare(Fact(has_flat_body=input("O peixe tem corpo achatado? ")))
    
    @Rule(Fact(has_flat_body="S"))
    def return_arraia(self):
        print("O animal é uma arraia.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(has_flat_body="N"))
    def return_tubarao(self):
        print("O animal é um tubarão.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_fish="N"))
    def ask_reptile(self):
        self.declare(Fact(is_reptile=input("O animal é um réptil? ")))
    
    @Rule(Fact(is_reptile="S"))
    def ask_members(self):
        self.declare(Fact(has_four_members=input("O réptil tem quatro membros? ")))
    
    @Rule(Fact(has_four_members="S"))
    def ask_scaled(self):
        self.declare(Fact(is_scaled=input("O réptil é escamado? ")))
    
    @Rule(Fact(is_scaled="S"))
    def return_camaleao(self):
        print("O animal é um camaleão.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_scaled="N"))
    def ask_shell(self):
        self.declare(Fact(has_shell=input("O réptil tem carapaça? ")))
    
    @Rule(Fact(has_shell="S"))
    def return_tartaruga(self):
        print("O animal é uma tartaruga.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(has_shell="N"))
    def return_jacare(self):
        print("O animal é um jacaré.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(has_four_members="N"))
    def return_cobra(self):
        print("O animal é uma cobra.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_reptile="N"))
    def ask_mammal(self):
        self.declare(Fact(is_mammal=input("O animal é um mamífero? ")))
    
    @Rule(Fact(is_mammal="N"))
    def ask_flying(self):
        self.declare(Fact(is_flying=input("A ave voa? ")))
    
    @Rule(Fact(is_flying="S"))
    def ask_falconiform(self):
        self.declare(Fact(is_falconiform=input("A ave é um falconiforme? ")))
    
    @Rule(Fact(is_falconiform="S"))
    def return_gaviao(self):
        print("O animal é um gavião.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_falconiform="N"))
    def ask_immovable_on_air(self):
        self.declare(Fact(can_immovable_flying=input("A ave pode ficar imóvel no ar? ")))
    
    @Rule(Fact(can_immovable_flying="S"))
    def return_beija_flor(self):
        print("O animal é um beija-flor.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(can_immovable_flying="N"))
    def return_gaivota(self):
        print("O animal é uma gaivota.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_flying="N"))
    def return_pinguim(self):
        print("O animal é um pinguim.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_mammal="S"))
    def ask_primal(self):
        self.declare(Fact(is_primal=input("O mamífero é um primata? ")))
    
    @Rule(Fact(is_primal="N"))
    def ask_aquatic(self):
        self.declare(Fact(is_aquatic=input("O mamífero é aquático? ")))
    
    @Rule(Fact(is_aquatic="N"))
    def ask_nocturnal(self):
        self.declare(Fact(is_nocturnal=input("O mamífero é noturno? ")))
    
    @Rule(Fact(is_nocturnal="N"))
    def ask_canine(self):
        self.declare(Fact(is_canine=input("O mamífero é um canino? ")))
    
    @Rule(Fact(is_canine="N"))
    def return_urso(self):
        print("O animal é um urso.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_canine="S"))
    def return_cao(self):
        print("O animal é um cão.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_nocturnal="S"))
    def return_morcego(self):
        print("O animal é um morcego.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_aquatic="S"))
    def return_baleia(self):
        print("O animal é uma baleia.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(is_primal="S"))
    def return_humano(self):
        print("O animal é um humano.")
        self.declare(Fact(ask_to_repeat="S"))
    
    @Rule(Fact(ask_to_repeat="S"))
    def ask_to_repeat(self):
        self.declare(Fact(can_repeat=input("Deseja identificar outro animal? ")))
    
    @Rule(Fact(can_repeat="S"))
    def start_repeat(self):
        self.reset()
        self.run()
    
    @Rule(Fact(can_repeat="N"))
    def end_run(self):
        print("Tchau.")

engine = AnimalClassifierEngine()
engine.reset()
engine.run()
