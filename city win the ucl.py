import numpy as np
import pandas as pd
import tensorflow as tf
import requests

def fetch_city_squad():
    try:
        url = "https://www.besoccer.com/team/squad/manchester-city"
        tables = pd.read_html(url)
        df = tables[0]
        df.columns = [str(c).strip() for c in df.columns]
        name_cols = [c for c in df.columns if "Player" in c or "Name" in c]
        name_col = name_cols[0]
        df = df[[name_col]].rename(columns={name_col: "Player"})
        df = df.dropna(subset=["Player"]).drop_duplicates(subset=["Player"])
        squad_list = df["Player"].tolist()
    except:
        squad_list = ["Erling Haaland", "Phil Foden", "Rodri", "Kevin De Bruyne", "Bernardo Silva"]

    new_signings = ["Marc Guéhi", "Antoine Semenyo"]
    for player in new_signings:
        if player not in squad_list:
            squad_list.append(player)
    return squad_list

def build_model(n):
    m = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(16,)),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(n, activation="softmax")
    ])
    return m

def simulate_match(r, players, model):
    print(f"\n=== {r} ===")
    g = np.random.randint(0, 6)
    if g == 0:
        print("Manchester City scored 0 goals.")
        return []
    noise = np.random.randn(1, 16).astype("float32")
    p = model(noise).numpy().flatten()
    p = p / p.sum()
    idx = np.random.choice(len(players), size=g, p=p)
    scorers = [players[i] for i in idx]
    print(f"Manchester City scored {g} goals.")
    for i, s in enumerate(scorers, 1):
        print(f"Goal {i}: {s}")
    return scorers

def run_ucl():
    players = fetch_city_squad()
    model = build_model(len(players))
    rounds = [
        "Round of 16 - Leg 1", "Round of 16 - Leg 2",
        "Quarterfinal - Leg 1", "Quarterfinal - Leg 2",
        "Semifinal - Leg 1", "Semifinal - Leg 2",
        "Final"
    ]
    for r in rounds:
        s = simulate_match(r, players, model)
        if r == "Final":
            if len(s) > 0:
                print("\nManchester City WIN the Champions League Final!")
            else:
                print("\nManchester City fail to win the final.")

run_ucl()
