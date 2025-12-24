import os

from color_detection import load_color_db


def test_load_colors_csv_exists_and_loads():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(repo_root, "colors.csv")
    assert os.path.exists(csv_path), "colors.csv must exist in the repo root for this test"
    df = load_color_db(csv_path)
    assert not df.empty
