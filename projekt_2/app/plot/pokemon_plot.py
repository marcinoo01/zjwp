import seaborn as sns

from projekt_2.app.model.redis_handler import RedisHandler
import matplotlib.pyplot as plt
import pandas as pd

from projekt_2.app.model.redis_handler import r

redis_handler = RedisHandler(r)


def plot_pokemon_statistics():
    pokemons = redis_handler.get_data('pokemons')
    speeds = [pokemon['stats']['speed'] for pokemon in pokemons]
    attacks = [pokemon['stats']['attack'] for pokemon in pokemons]

    type_counts = {}
    for pokemon in pokemons:
        for poke_type in pokemon['types']:
            type_counts[poke_type] = type_counts.get(poke_type, 0) + 1

    type_attack_totals = {}
    type_attack_counts = {}
    for pokemon in pokemons:
        for poke_type in pokemon['types']:
            type_attack_totals[poke_type] = type_attack_totals.get(poke_type, 0) + pokemon['stats']['attack']
            type_attack_counts[poke_type] = type_attack_counts.get(poke_type, 0) + 1
    average_attack_by_type = {t: type_attack_totals[t] / type_attack_counts[t] for t in type_attack_totals}

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.hist(speeds, bins=10, color='blue', edgecolor='black')
    plt.title("Speed Distribution")
    plt.xlabel("Speed")
    plt.ylabel("Number of Pokémon")

    plt.subplot(2, 2, 2)
    plt.hist(attacks, bins=10, color='green', edgecolor='black')
    plt.title("Attack Distribution")
    plt.xlabel("Attack")
    plt.ylabel("Number of Pokémon")

    plt.subplot(2, 2, 3)
    types = list(average_attack_by_type.keys())
    avg_attacks = list(average_attack_by_type.values())
    plt.bar(types, avg_attacks, color='purple', edgecolor='black')
    plt.title("Average Attack by Type")
    plt.xlabel("Pokémon Type")
    plt.ylabel("Average Attack")
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 4)
    plt.pie(type_counts.values(), labels=type_counts.keys(), autopct='%1.1f%%', startangle=90)
    plt.title("Pokémon Type Distribution")

    plt.tight_layout()
    plt.show()


def calculate_correlations():
    pokemons = redis_handler.get_data('pokemons')

    df = pd.DataFrame([pokemon['stats'] for pokemon in pokemons])
    correlation_matrix = df.corr()
    return correlation_matrix


def plot_correlation_heatmap():
    pokemons = redis_handler.get_data('pokemons')

    df = pd.DataFrame([pokemon['stats'] for pokemon in pokemons])
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Between Pokémon Stats")
    plt.show()
