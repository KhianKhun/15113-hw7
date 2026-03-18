from __future__ import annotations

from pathlib import Path

from src.board import BoardState

# Map legend
# # = wall, B = box, T = target, P = player
# * = box on target, + = player on target
VALID_CHARS = {"#", " ", "B", "T", "P", "*", "+"}


def load_level(path: str | Path) -> BoardState:
    level_path = Path(path)
    raw_lines = level_path.read_text(encoding="utf-8").splitlines()
    lines = [line.rstrip("\n") for line in raw_lines if line.strip() != ""]
    if not lines:
        raise ValueError(f"Level file is empty: {level_path}")

    width = max(len(line) for line in lines)
    height = len(lines)

    walls: set[tuple[int, int]] = set()
    boxes: set[tuple[int, int]] = set()
    targets: set[tuple[int, int]] = set()
    player: tuple[int, int] | None = None

    for row_index, line in enumerate(lines):
        padded = line.ljust(width)
        y = height - 1 - row_index
        for x, ch in enumerate(padded):
            if ch not in VALID_CHARS:
                raise ValueError(f"Invalid map char '{ch}' in {level_path}")
            pos = (x, y)
            if ch == "#":
                walls.add(pos)
            elif ch == "B":
                boxes.add(pos)
            elif ch == "T":
                targets.add(pos)
            elif ch == "P":
                if player is not None:
                    raise ValueError("Level must contain exactly one player.")
                player = pos
            elif ch == "*":
                boxes.add(pos)
                targets.add(pos)
            elif ch == "+":
                targets.add(pos)
                if player is not None:
                    raise ValueError("Level must contain exactly one player.")
                player = pos

    if player is None:
        raise ValueError("Level must contain one player.")
    if len(boxes) == 0:
        raise ValueError("Level must contain at least one box.")
    if len(boxes) != len(targets):
        raise ValueError("The number of boxes must equal the number of targets.")

    return BoardState(
        width=width,
        height=height,
        walls=walls,
        boxes=boxes,
        targets=targets,
        player=player,
    )
