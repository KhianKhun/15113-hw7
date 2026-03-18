# Sokoban

A coordinate-driven Sokoban game implemented with Python and `tkinter`.

## Run the Game

```bash
python run.py
```

Optional (for tests):

```bash
py -3 -m pip install -r requirements.txt
```

## Controls

- `Up Arrow`: move up
- `Down Arrow`: move down
- `Left Arrow`: move left
- `Right Arrow`: move right
- `R`: reset/restart the current level

Behavior notes:

- When all boxes are on targets, the game shows `You win!`.
- After winning, movement input is locked.
- The center of the screen shows `Press R to restart`.

## Project Structure

```text
15113-hw7/
├─ assets/
│  ├─ maps/
│  │  ├─ generated/
│  │  ├─ level_01.txt
│  │  ├─ level_02.txt
│  │  └─ level_03.txt
│  └─ sprites/
│     ├─ box.png
│     ├─ box_on_target.png
│     ├─ floor.png
│     ├─ player.png
│     ├─ target.png
│     └─ wall.png
├─ config/
│  └─ generator.yaml
├─ src/
│  ├─ generator/
│  │  ├─ __init__.py
│  │  ├─ difficulty.py
│  │  ├─ map_serializer.py
│  │  ├─ random_map_generator.py
│  │  └─ solver_check.py
│  ├─ __init__.py
│  ├─ board.py
│  ├─ constants.py
│  ├─ game.py
│  ├─ level_loader.py
│  ├─ player.py
│  ├─ renderer.py
│  └─ rules.py
├─ tests/
│  ├─ test_level_loader.py
│  ├─ test_random_map_generator.py
│  ├─ test_rules.py
│  └─ test_solver_check.py
├─ requirements.txt
├─ run.py
└─ README.md
```

## What Each Part Does

- `run.py`
  - Program entry point. Starts the game loop.

- `src/board.py`
  - Defines `BoardState` data: board size, walls, boxes, targets, player position.
  - Includes utility checks like `in_bounds` and win condition checks.

- `src/rules.py`
  - Core Sokoban movement and push logic.
  - Validates collision, bounds, and box push conditions before updating coordinates.

- `src/player.py`
  - Maps keyboard directions to movement vectors.
  - Tracks step count and delegates movement to rules.

- `src/level_loader.py`
  - Parses level text files into board coordinates.
  - Uses bottom-left logical origin `(0, 0)`.

- `src/renderer.py`
  - Draws board state with `tkinter`.
  - Converts logical coordinates into canvas positions.
  - Displays status text and centered restart message after win.

- `src/game.py`
  - High-level game orchestration.
  - Binds key events, processes reset, and locks movement after winning.

- `src/constants.py`
  - Shared render constants (tile size, margins, colors).

- `assets/maps/`
  - Level definitions in plain text.

- `assets/maps/generated/`
  - Reserved output directory for future random level generation.

- `src/generator/*`
  - Reserved modules for random map generation, solvability checks, and difficulty tuning.

- `tests/*`
  - Unit tests for level loading and movement rules.

## Core Game Logic

The game is built on coordinate updates, not direct sprite movement.

1. Coordinate model
   - Player: one coordinate `(x, y)`
   - Boxes: set of coordinates
   - Walls: set of coordinates
   - Targets: set of coordinates

2. Movement rules
   - Compute `next = player + direction`.
   - If `next` is out of bounds or a wall: reject move.
   - If `next` is a box:
     - Compute `push_to = next + direction`.
     - If `push_to` is blocked (wall/box/out of bounds): reject move.
     - Else move the box to `push_to`.
   - Move player to `next`.

3. Win condition
   - Win when `boxes == targets`.

4. Post-win behavior
   - Movement keys are ignored.
   - Center message `Press R to restart` is shown.
   - Press `R` to reload the level.
