import pandas as pd

df = pd.read_csv("games.csv") # dataset descargado de Kaggle
season = df[df['SEASON'] == 2019].copy()
season['TOTAL_POINTS'] = season['PTS_home'] + season['PTS_away']

sample = season[['GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'PTS_home', 'PTS_away', 'TOTAL_POINTS']].head(500)

# Ordenar con algoritmo nativo de Python
# sorted_games = sample.sort_values(by="TOTAL_POINTS", ascending=False)

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]: # descendente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Convert sample DataFrame to list of dicts for bubble sort
sample_list = sample.to_dict('records')
sorted_list = bubble_sort(sample_list, "TOTAL_POINTS")

# Mostrar el top 10 partidos con más puntos totales
for g in sorted_list[:10]:
    print(f"{g['GAME_DATE_EST']}: {g['HOME_TEAM_ID']} {g['PTS_home']} vs {g['VISITOR_TEAM_ID']} {g['PTS_away']} (Total: {g['TOTAL_POINTS']})")

# Convert sorted list back to DataFrame for .head()
sorted_games_df = pd.DataFrame(sorted_list)
print(sorted_games_df.head())
