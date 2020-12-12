import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--day", "-d",
        required=True,
        type=int, 
        help="The Day of the calendar to calculate"
    )

    parser.add_argument(
        "--input-file", "-f",
        required=True,
        type=str,
        help="The input for the day's puzzle"
    )

    return parser
