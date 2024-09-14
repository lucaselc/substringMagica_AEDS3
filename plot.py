#!/usr/bin/env python
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('times.db')
cursor = conn.cursor()

# Query to get data from the tables
query = """
SELECT configuration.haystack_length, configuration.needle_length, time.user, time.system, time.clock, configuration.strat
FROM time
JOIN configuration ON time.config_id = configuration.id
"""

cursor.execute(query)
data = cursor.fetchall()

# Close the connection
conn.close()

# Process data
strategies = {}
for row in data:
    haystack_length, needle_length, user, system, clock, strat = row
    if strat not in strategies:
        strategies[strat] = {'haystack_length': [], 'user': [], 'system': [], 'clock': []}
    strategies[strat]['haystack_length'].append(haystack_length)
    strategies[strat]['user'].append(user)
    strategies[strat]['system'].append(system)
    strategies[strat]['clock'].append(clock)

# Function to aggregate data by 'haystack_length' and calculate averages
def aggregate_data(haystack_length_list, time_list):
    haystack_length_dict = {}
    for n, time in zip(haystack_length_list, time_list):
        if n not in haystack_length_dict:
            haystack_length_dict[n] = []
        haystack_length_dict[n].append(time)
    haystack_values = sorted(haystack_length_dict.keys())
    avg_times = [np.mean(haystack_length_dict[n]) for n in haystack_values]
    return haystack_values, avg_times

plt.figure(figsize=(10, 6))

# Plot data for each strategy
for strat, times in strategies.items():
    n_values, clock_avg = aggregate_data(times['haystack_length'], times['clock'])

    print(strat)

    plt.plot(n_values, clock_avg, label=f'Tempo de médio da estratégia {strat}', marker='o')

# Adding labels and title
plt.xlabel('Tamanho das Entradas (n)')
plt.ylabel('Tempo médio (segundos)')
plt.title(f'Tempo médio pelo Número de Entradas')
plt.legend()
plt.grid(True)

# Show plot
plt.savefig(f'img/tp3.svg')

