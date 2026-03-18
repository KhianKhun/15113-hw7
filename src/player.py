from __future__ import annotations

from dataclasses import dataclass

from src.board import BoardState
from src.rules import DIRECTIONS, try_move


@dataclass
class PlayerController:
    board: BoardState
    steps: int = 0

    def handle_key(self, keysym: str) -> bool:
        if keysym not in DIRECTIONS:
            return False
        moved = try_move(self.board, DIRECTIONS[keysym])
        if moved:
            self.steps += 1
        return moved
