from models.species import Species 
from models.simulation import Simulation 
import matplotlib.pyplot as plt 
import pandas as pd
from pathlib import Path

# Initialize populations 
prey = Species("Prey", birth_rate=0.3, death_rate=0.05, latency_period=3, 
initial_population=100, species_variant={'camouflage': 0.7}) 
predator = Species("Predator", birth_rate=0.1, death_rate=0.1, latency_period=5, 
initial_population=20, species_variant={'feeding_bonus': 1.5}) 


# Create simulation 
sim = Simulation(prey, predator, interaction_rate=0.02, predation_success=0.8) 


# Run for N steps 
timesteps = 40
for t in range(timesteps): 
    print(f"Step {t}")
    sim.step(t) 


# Plot results 
plt.plot(sim.time, prey.population, label='Prey') 
plt.plot(sim.time, predator.population, label='Predator') 
plt.xlabel('Time') 
plt.ylabel('Population') 
plt.legend() 
plt.title('Predator–Prey Simulation with Reproductive Latency') 
plt.show()

# Save results to CSV
data = { 
    'Time': sim.time, 
    'Prey Population': prey.population,
    'Prey Camouflage' : prey.variant.get('camouflage', None),
    'Predator Population': predator.population,
    'Predator Variant' : predator.variant.get('feeding_bonus', None)
}
df = pd.DataFrame(data)
path = Path('data/simulation_results.csv')
df.to_csv(path, index=False)
print(f"Saving results to {path}")