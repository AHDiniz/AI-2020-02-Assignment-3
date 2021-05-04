#!/usr/bin/python3.8

from pyknow import *

class AnimalClassifierEngine(KnowledgeEngine):
    
    # Start up rule:
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start")
    
    # The first rule asks if the animal is a fish:
    @Rule(Fact(action="start"))
    def ask_fish(self):
        self.declare(Fact(is_fish=input("O animal é um peixe? ")))
    
    # Rules that are triggered when the animal is a fish:
    @Rule(Fact(is_fish="S"))
    def ask_boned(self):
        self.declare(Fact(is_boned=input("O peixe é ósseo? "))) # Asking the type of bones
    
    # If the fish is boned:
    @Rule(Fact(is_boned="S"))
    def ask_poisoning(self):
        self.declare(Fact(is_poisoning=input("O peixe é venenoso? "))) # Asking if the fish is poisonous
    
    # If the fish is poisonous:
    @Rule(Fact(is_poisoning="S"))
    def return_baiacu(self):
        print("O animal é um baiacu.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the fish is not poisonous:
    @Rule(Fact(is_poisoning="N"))
    def return_atum(self):
        print("O animal é um atum.")
        self.declare(Fact(ask_to_repeat="S"))

    # If the fish is cartilaginous:
    @Rule(Fact(is_boned="N"))
    def ask_flat(self):
        self.declare(Fact(has_flat_body=input("O peixe tem corpo achatado? "))) # Asking if the fish has a flat body
    
    # If the fish has a flat body:
    @Rule(Fact(has_flat_body="S"))
    def return_arraia(self):
        print("O animal é uma arraia.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the fish doesn't have a flat body:
    @Rule(Fact(has_flat_body="N"))
    def return_tubarao(self):
        print("O animal é um tubarão.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the animal is not a fish:
    @Rule(Fact(is_fish="N"))
    def ask_anfibious(self):
        self.declare(Fact(is_anfibious=input("O animal é um anfíbio? "))) # Asking if the animal is an anfibious

    # If the animal is anfibious:
    @Rule(Fact(is_anfibious="S"))
    def ask_tail(self):
        self.declare(Fact(has_tail=input("O animal tem cauda? "))) # Asking if the anfibious has a tail

    # If the animal has a tail:
    @Rule(Fact(has_tail="S"))
    def return_salamandra(self):
        print("O animal é uma salamandra.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the animal doesn't have a tail:
    @Rule(Fact(has_tail="N"))
    def return_sapo(self):
        print("O animal é um sapo.")
        self.declare(Fact(ask_to_repeat="S"))

    # If the animal is not a fish:
    @Rule(Fact(is_anifibious="N"))
    def ask_reptile(self):
        self.declare(Fact(is_reptile=input("O animal é um réptil? "))) # Asking if the animal is a reptile

    # If the animal is a reptile:    
    @Rule(Fact(is_reptile="S"))
    def ask_members(self):
        self.declare(Fact(has_four_members=input("O réptil tem quatro membros? "))) # Asking if the animal has four members
    
    # If the reptile has four members:
    @Rule(Fact(has_four_members="S"))
    def ask_scaled(self):
        self.declare(Fact(is_scaled=input("O réptil é escamado? "))) # Asking if the reptile has scales
    
    # If the animal has scales:
    @Rule(Fact(is_scaled="S"))
    def return_camaleao(self):
        print("O animal é um camaleão.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the reptile is not scaled:
    @Rule(Fact(is_scaled="N"))
    def ask_shell(self):
        self.declare(Fact(has_shell=input("O réptil tem carapaça? "))) # Asking if the reptile has a shell
    
    # If the reptile has a shell:
    @Rule(Fact(has_shell="S"))
    def return_tartaruga(self):
        print("O animal é uma tartaruga.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the reptile doesn't have a shell:
    @Rule(Fact(has_shell="N"))
    def return_jacare(self):
        print("O animal é um jacaré.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the reptile doesn't have four members:
    @Rule(Fact(has_four_members="N"))
    def return_cobra(self):
        print("O animal é uma cobra.")
        self.declare(Fact(ask_to_repeat="S"))
    
    # If the animal is not a reptile:
    @Rule(Fact(is_reptile="N"))
    def ask_mammal(self):
        self.declare(Fact(is_mammal=input("O animal é um mamífero? "))) # Asking if the animal is a mammal
    
    # If the animal is not a mammal, it's a bird:
    @Rule(Fact(is_mammal="N"))
    def ask_flying(self):
        self.declare(Fact(is_flying=input("A ave voa? "))) # Asking if the bird flies
    
    # If the bird flies:
    @Rule(Fact(is_flying="S"))
    def ask_falconiform(self):
        self.declare(Fact(is_falconiform=input("A ave é um falconiforme? "))) # Asking if the bird is falconiform
    
    # If the bird is falconiform:
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
        self.declare(Fact(is_primate=input("O mamífero é um primata? ")))
    
    @Rule(Fact(is_primate="N"))
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
    
    @Rule(Fact(is_primate="S"))
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
