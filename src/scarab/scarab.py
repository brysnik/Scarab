"""
Scarab node
"""

from argparse import ArgumentParser


def parse_args():
    args = ArgumentParser(description=__doc__)
    args.add_argument(
        "TASK",
        help="Filepath to task definition or entry point",
    )
    return args.parse_args()


def main():
    args = parse_args()
    return 0


if __name__ == "__main__":
    print("Running main")
    exit(main())
