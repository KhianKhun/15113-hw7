from src.level_loader import load_level


def test_level_loader_uses_bottom_left_origin() -> None:
    board = load_level("assets/maps/level_01.txt")

    assert board.player == (3, 2)
    assert (3, 3) in board.boxes
    assert (3, 4) in board.targets
    assert (0, 0) in board.walls
