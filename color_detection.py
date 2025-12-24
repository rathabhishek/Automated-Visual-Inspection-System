"""Color detection CLI — refactored for safety and reuse.

Small, local utility to pick a color from an image. This module is intentionally
lightweight and prepared for packaging (containerization) and integration with
cloud/event-driven pipelines.
"""

from __future__ import annotations

import argparse
import logging
import os
from typing import Tuple

import cv2
import pandas as pd

LOGGER = logging.getLogger(__name__)


def load_color_db(csv_path: str) -> pd.DataFrame:
    index = ["color", "color_name", "hex", "R", "G", "B"]
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Color DB not found: {csv_path}")
    return pd.read_csv(csv_path, names=index, header=None)


def get_color_name(csv: pd.DataFrame, R: int, G: int, B: int) -> str:
    # Manhattan distance on RGB space (sufficient for demo)
    minimum = float("inf")
    cname = "Unknown"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = str(csv.loc[i, "color_name"])
    return cname


def run_interactive(image_path: str, color_db_path: str) -> None:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Unable to read image: {image_path}")

    csv = load_color_db(color_db_path)

    clicked = False
    r = g = b = xpos = ypos = 0


    def draw_function(event, x, y, flags, param):
        nonlocal clicked, r, g, b, xpos, ypos
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicked = True
            xpos = x
            ypos = y
            b, g, r = img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)


    cv2.namedWindow("image")
    cv2.setMouseCallback("image", draw_function)

    while True:
        cv2.imshow("image", img)
        if clicked:
            cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
            text = f"{get_color_name(csv, r, g, b)} R={r} G={g} B={b}"
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            if r + g + b >= 600:
                cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            clicked = False

        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


def main() -> None:
    parser = argparse.ArgumentParser(description="Color detection demo")
    parser.add_argument("-i", "--image", required=True, help="Image path")
    parser.add_argument(
        "--colors-csv",
        default=os.path.join(os.path.dirname(__file__), "colors.csv"),
        help="Path to colors.csv",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    LOGGER.info("Starting color detection")

    try:
        run_interactive(args.image, args.colors_csv)
    except Exception as exc:  # keep broad handling for the CLI wrapper
        LOGGER.error("Error running color detection: %s", exc)
        raise


if __name__ == "__main__":
    main()
