from __future__ import annotations

import tkinter as tk

from src.level_loader import load_level
from src.player import PlayerController
from src.renderer import TkRenderer


class SokobanGame:
    def __init__(self, level_path: str) -> None:
        self.level_path = level_path
        self.root = tk.Tk()
        self.root.title("Sokoban - Coordinate Driven")
        self.board = load_level(self.level_path)
        self.player = PlayerController(self.board)
        self.renderer = TkRenderer(self.root, self.board)

        self.root.bind("<KeyPress>", self.on_keypress)
        self.renderer.draw(self.player.steps, self.board.is_completed())

    def reset(self) -> None:
        self.board = load_level(self.level_path)
        self.player = PlayerController(self.board)
        self.renderer.board = self.board
        self.renderer.draw(self.player.steps, self.board.is_completed())

    def on_keypress(self, event: tk.Event) -> None:
        if event.keysym.lower() == "r":
            self.reset()
            return

        if self.board.is_completed():
            return

        moved = self.player.handle_key(event.keysym)
        if moved:
            self.renderer.draw(self.player.steps, self.board.is_completed())

    def run(self) -> None:
        self.root.mainloop()
