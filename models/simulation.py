from models.species import Species
import numpy as np
class Simulation:
    def __init__(self, prey, predator, interaction_rate, predation_success):
        self.prey = prey
        self.predator = predator
        self.interaction_rate = interaction_rate
        self.predation_success = predation_success
        self.time = [0]
        
    def step(self, t):
    # Predator-prey interactions
        #Read optional numeric modifiers from the species variant 
        prey_variant = self.prey.variant if isinstance(self.prey.variant, dict) else {}
        predator_variant = self.predator.variant if isinstance(self.predator.variant, dict) else {}

        prey_camouflage = float(prey_variant.get('camouflage', 1.0 )) #reduces encounter rate (0..1) 
        predator_feeding_bonus = float(predator_variant.get('feeding_bonus', 1.0 )) #scales birth boost

        effective_interaction_rate = self.interaction_rate * prey_camouflage
        effective_predation_success = self.predation_success * predator_feeding_bonus

        interactions = min(len(self.prey.ages), len(self.predator.ages))
        events = np.random.rand(interactions) < effective_interaction_rate 
        prey_eaten = int(min(np.sum(events) * effective_predation_success, len(self.prey.ages)))   
        # Remove eaten prey 
        if prey_eaten > 0:
            self.prey.ages = self.prey.ages[:-prey_eaten]
        # Predator birth boost from feeding (apply feeding bonus) 
        for _ in range(prey_eaten):
            # Add stochasticity: feeding isn't always equally nutritious/effective
            random_effectiveness = np.random.uniform(0.5, 1.5)
            if np.random.rand() < (self.predator.birth_rate * predator_feeding_bonus * random_effectiveness):
                self.predator.ages = np.concatenate((self.predator.ages, np.zeros(1, dtype=int)))
        # Apply internal birth/death dynamics
        self.prey.step() 
        self.predator.step(reproduce=False)
        self.time.append(t) 