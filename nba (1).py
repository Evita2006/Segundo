import pandas as pd

df = pd.read_csv("games.csv") # dataset descargado de Kaggle
season = df [df [ 'SEASON' ] == 2019]
season['TOTAL_POINTS' ] = season['HOME_PTS' ] + season[ 'AWAY_PTS' ]

sample = season[ ['GAME_DATE', 'HOME_TEAM', 'AWAY_TEAM', 'TOTAL_POINTS' ]].head(500)

# Ordenar con algoritmo nativo de Python
#sorted_games = samlpe.sort_values(by="TOTAL_POINTS", ascending=False)

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j][key] < arr[j + 1][key]: # descendente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejecutar bubble sort sobre la muestra
sorted_games = bubble_sort(sample, "TOTAL_POINTS" )

# Mostrar el top 10 partidos con más puntos totales
for g in sorted_games[:10]:
    print(f"{g['GAME_DATE' ]}: {g['HOME_TEAM' ]} {g[ 'HOME_PTS' ]}
    f"{g['AWAY_TEAM' ]} {g[ 'AWAY_PTS' ]}
    f"(Total: {g['TOTAL_POINTS' ]} )")|


print(sorted_games.head( ))