from models.species import Species 
from models.simulation import Simulation 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import numpy as np
from pathlib import Path

# If you get very boring results, try running a few more times
# please.  The randomness varies between runs.

# Beware of modifying these to be too large, as the program
# took up 24GB of RAM on my PC when I adjusted them incorrectly

n_simulations = 10
timesteps = 60
all_data = []

print(f"Running {n_simulations} simulations with randomized parameters...")

for i in range(n_simulations):
    # Reasonable guidelines for each sim
    prey_birth = np.random.uniform(0.4, 0.6)
    prey_death = np.random.uniform(0.04, 0.06)
    prey_pop = int(np.random.uniform(80, 180))
    camouflage = np.random.uniform(0.5, 0.85)
    
    pred_birth = np.random.uniform(0.15, 0.5)
    pred_death = np.random.uniform(0.08, 0.12)
    pred_pop = int(np.random.uniform(60, 80))
    feeding_bonus = np.random.uniform(1.45, 1.56)
    
    interaction = np.random.uniform(0.8, 1.0)
    success = np.random.uniform(0.5, 0.7)

    # Initialize populations 
    prey = Species("Prey", birth_rate=prey_birth, death_rate=prey_death, latency_period=3, 
                   initial_population=prey_pop, species_variant={'camouflage': camouflage}) 
    predator = Species("Predator", birth_rate=pred_birth, death_rate=pred_death, latency_period=5, 
                       initial_population=pred_pop, species_variant={'feeding_bonus': feeding_bonus}) 

    sim = Simulation(prey, predator, interaction_rate=interaction, predation_success=success) 

    print(f'==== SIMULATION {i+1} ====')
    for t in range(timesteps): 
        sim.step(t)
        
        if t % 10 == 0:
            print(f"Step {t} | Prey: {prey.population[-1]} | Predator: {predator.population[-1]}")

        # Collect data
        all_data.append({'Simulation': i, 'Time': t, 'Population': prey.population[-1], 'Species': 'Prey', 'camouflage': camouflage})
        all_data.append({'Simulation': i, 'Time': t, 'Population': predator.population[-1], 'Species': 'Predator', 'feeding_bonus': feeding_bonus})
    

# Stochastic thingy
df = pd.DataFrame(all_data)

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Time', y='Population', hue='Species', units='Simulation', estimator=None, alpha=0.4, linewidth=1)
plt.title(f'Stochastic Predator Prey Simulation - Individual Runs ({n_simulations} Runs)')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Time', y='Population', hue='Species')
plt.title(f'Stochastic Predator Prey Simulation - Aggregated ({n_simulations} Runs)')

plt.show()

# Save results to CSV

data = {
    "time": df.Time,
    "prey_population": df[df.Species == 'Prey'].Population,
    "predator_population": df[df.Species == 'Predator'].Population,
    "camouflage": camouflage,
    "feeding_bonus": feeding_bonus,
    }
csv_df = pd.DataFrame(data)
path = Path('data/simulation_results.csv')
df.to_csv(path, index=False)
print(f"Saving results to {path}")