import argparse
import collections

import dietitian.core


Range = collections.namedtuple("Range", ["low", "high"])


def parse_range_argument(value):
    low, high = tuple(map(int, value.split("-")))
    assert low < high
    return Range(low, high)


parser = argparse.ArgumentParser(description="diet optimizer")
parser.add_argument(
    "-p",
    "--protein",
    type=parse_range_argument,
    default=Range(240, 261),
    help="target range for protein in gramms (e.g. 240-261)")
parser.add_argument(
    "-f",
    "--fat",
    type=parse_range_argument,
    default=Range(70, 81),
    help="target range for fat in gramms (e.g. 70-81)")
parser.add_argument(
    "-c",
    "--carbohydrate",
    type=parse_range_argument,
    default=Range(95, 106),
    help="target range for carbohydrate in gramms (e.g. 95-106)")
parser.add_argument(
    "path",
    help="menu file")

dietitian.core.run(parser.parse_args())
