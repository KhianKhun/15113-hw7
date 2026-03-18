from __future__ import annotations

import tkinter as tk

from src.board import BoardState, Coord
from src.constants import (
    COLOR_BG,
    COLOR_BOX,
    COLOR_BOX_ON_TARGET,
    COLOR_FLOOR,
    COLOR_GRID,
    COLOR_PLAYER,
    COLOR_TARGET,
    COLOR_WALL,
    MARGIN_X,
    MARGIN_Y,
    TILE_SIZE,
)


class TkRenderer:
    def __init__(self, root: tk.Tk, board: BoardState) -> None:
        self.board = board
        self.width_px = MARGIN_X * 2 + board.width * TILE_SIZE
        self.height_px = MARGIN_Y * 2 + board.height * TILE_SIZE + 44

        self.canvas = tk.Canvas(
            root,
            width=self.width_px,
            height=self.height_px,
            bg=COLOR_BG,
            highlightthickness=0,
        )
        self.canvas.pack()

    def to_canvas_xy(self, pos: Coord) -> tuple[int, int, int, int]:
        x, y = pos
        x1 = MARGIN_X + x * TILE_SIZE
        y1 = self.height_px - 44 - MARGIN_Y - (y + 1) * TILE_SIZE
        x2 = x1 + TILE_SIZE
        y2 = y1 + TILE_SIZE
        return x1, y1, x2, y2

    def draw(self, steps: int, won: bool) -> None:
        c = self.canvas
        c.delete("all")

        for y in range(self.board.height):
            for x in range(self.board.width):
                x1, y1, x2, y2 = self.to_canvas_xy((x, y))
                c.create_rectangle(x1, y1, x2, y2, fill=COLOR_FLOOR, outline=COLOR_GRID)

        for pos in self.board.targets:
            x1, y1, x2, y2 = self.to_canvas_xy(pos)
            c.create_oval(
                x1 + 12,
                y1 + 12,
                x2 - 12,
                y2 - 12,
                fill=COLOR_TARGET,
                outline="",
            )

        for pos in self.board.walls:
            x1, y1, x2, y2 = self.to_canvas_xy(pos)
            c.create_rectangle(x1, y1, x2, y2, fill=COLOR_WALL, outline=COLOR_GRID)

        for pos in self.board.boxes:
            x1, y1, x2, y2 = self.to_canvas_xy(pos)
            fill = COLOR_BOX_ON_TARGET if pos in self.board.targets else COLOR_BOX
            c.create_rectangle(
                x1 + 8,
                y1 + 8,
                x2 - 8,
                y2 - 8,
                fill=fill,
                outline="#3d2a1b",
                width=2,
            )

        px1, py1, px2, py2 = self.to_canvas_xy(self.board.player)
        c.create_oval(px1 + 8, py1 + 8, px2 - 8, py2 - 8, fill=COLOR_PLAYER, outline="")

        status = f"Steps: {steps}   Position: {self.board.player}"
        if won:
            status += "   You win!"
        c.create_text(
            MARGIN_X,
            self.height_px - 20,
            text=status,
            anchor="w",
            font=("Consolas", 12, "bold"),
            fill="#2f2418",
        )

        if won:
            c.create_text(
                self.width_px // 2,
                (self.height_px - 44) // 2,
                text="Press R to restart",
                anchor="center",
                font=("Times New Roman", 34, "bold"),
                fill="#2f2418",
            )
