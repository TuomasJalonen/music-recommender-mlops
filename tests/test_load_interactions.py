import pandas as pd
import pytest

from data.load_interactions import load_interactions


@pytest.fixture
def csv_path(tmp_path, request):
    path = tmp_path / "listening_history.csv"
    request.cls.df.to_csv(path, index=False)
    return path


class TestLoadInteractions:
    df = pd.DataFrame(
        {
            "user_id": [0, 1, 2, 3, 4, 5],
            "artist_name": [
                "Michael Jackson",
                "Stevie Wonder",
                "Earth, Wind & Fire",
                "Rush",
                "Iron Maiden",
                "Michael Jackson",
            ],
            "track_name": ["Beat It", "Sir Duke", "Let's Groove", "Freewill", "", "Beat it"],
            "timestamp": [
                "2026-04-29 09:00:00",
                "",
                "2026-04-28 20:00:00",
                "2026-04-28 10:00:00",
                "",
                "2026-04-29 09:05:00",
            ],
        }
    )

    def test_columns_exist(self, csv_path):
        result = load_interactions(csv_path)

        assert "user_id" in result.columns
        assert "track_name" in result.columns
        assert "timestamp" in result.columns
        assert "track_id" in result.columns

    def test_datetime(self, csv_path):
        result = load_interactions(csv_path)

        assert pd.api.types.is_datetime64_any_dtype(result["timestamp"])

    def test_missing_rows(self, csv_path):
        result = load_interactions(csv_path)

        assert 1 not in result["user_id"].values
        assert 4 not in result["user_id"].values

    def test_row_count(self, csv_path):
        result = load_interactions(csv_path)

        assert len(result) == 4
