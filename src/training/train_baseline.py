from pathlib import Path

import pandas as pd


def main() -> None:
    interactions = pd.DataFrame(
        {
            "user_id": [1, 1, 2, 2, 3, 3, 3],
            "track_id": [10, 20, 10, 30, 20, 30, 40],
        }
    )

    popularity = (
        interactions.groupby("track_id")
        .size()
        .sort_values(ascending=False)
        .reset_index(name="score")
    )

    output_path = Path("models/popularity.csv")
    output_path.parent.mkdir(exist_ok=True)
    popularity.to_csv(output_path, index=False)

    print(f"Saved popularity model to {output_path}")


if __name__ == "__main__":
    main()
