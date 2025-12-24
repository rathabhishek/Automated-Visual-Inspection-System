import pandas as pd

from color_detection import get_color_name


def test_get_color_name_matches_closest():
    # Construct a tiny color DB with three entries
    df = pd.DataFrame(
        {
            "color": ["c1", "c2", "c3"],
            "color_name": ["Redish", "Greenish", "Bluish"],
            "hex": ["#ff0000", "#00ff00", "#0000ff"],
            "R": [250, 10, 10],
            "G": [10, 250, 10],
            "B": [10, 10, 250],
        }
    )

    assert get_color_name(df, 255, 5, 5) == "Redish"
    assert get_color_name(df, 5, 255, 5) == "Greenish"
    assert get_color_name(df, 5, 5, 255) == "Bluish"
