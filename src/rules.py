from __future__ import annotations

from src.board import BoardState, Coord

Direction = tuple[int, int]

DIRECTIONS: dict[str, Direction] = {
    "Up": (0, 1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (1, 0),
}


def add(a: Coord, b: Direction) -> Coord:
    return (a[0] + b[0], a[1] + b[1])


def try_move(board: BoardState, direction: Direction) -> bool:
    next_pos = add(board.player, direction)
    if not board.in_bounds(next_pos) or board.has_wall(next_pos):
        return False

    if board.has_box(next_pos):
        push_to = add(next_pos, direction)
        if (
            not board.in_bounds(push_to)
            or board.has_wall(push_to)
            or board.has_box(push_to)
        ):
            return False
        board.boxes.remove(next_pos)
        board.boxes.add(push_to)

    board.player = next_pos
    return True
