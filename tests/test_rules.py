from src.board import BoardState
from src.rules import try_move


def test_push_box_success() -> None:
    board = BoardState(
        width=6,
        height=5,
        walls={(0, 0)},
        boxes={(2, 1)},
        targets={(3, 1)},
        player=(1, 1),
    )

    moved = try_move(board, (1, 0))
    assert moved is True
    assert board.player == (2, 1)
    assert (3, 1) in board.boxes


def test_push_box_blocked_by_wall() -> None:
    board = BoardState(
        width=6,
        height=5,
        walls={(3, 1)},
        boxes={(2, 1)},
        targets={(4, 1)},
        player=(1, 1),
    )

    moved = try_move(board, (1, 0))
    assert moved is False
    assert board.player == (1, 1)
    assert (2, 1) in board.boxes
