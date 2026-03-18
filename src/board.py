from __future__ import annotations

from dataclasses import dataclass, field

Coord = tuple[int, int]


@dataclass
class BoardState:
    width: int
    height: int
    walls: set[Coord] = field(default_factory=set)
    boxes: set[Coord] = field(default_factory=set)
    targets: set[Coord] = field(default_factory=set)
    player: Coord = (0, 0)

    def in_bounds(self, pos: Coord) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def has_wall(self, pos: Coord) -> bool:
        return pos in self.walls

    def has_box(self, pos: Coord) -> bool:
        return pos in self.boxes

    def has_target(self, pos: Coord) -> bool:
        return pos in self.targets

    def is_completed(self) -> bool:
        return len(self.targets) > 0 and self.boxes == self.targets
