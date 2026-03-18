from src.game import SokobanGame


def main() -> None:
    game = SokobanGame(level_path="assets/maps/level_01.txt")
    game.run()


if __name__ == "__main__":
    main()
