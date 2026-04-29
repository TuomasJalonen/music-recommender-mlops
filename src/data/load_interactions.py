from pathlib import Path
import pandas as pd


def load_interactions(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, header=0, names=["user_id", "artist_name", "track_name", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["user_id", "track_name", "timestamp"])
    df["track_id"] = df["artist_name"] + " - " + df["track_name"]

    return df
