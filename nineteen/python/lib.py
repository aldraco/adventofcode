import argparse

FILE_INPUT_SLUG = "../data/{}.txt"


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file")
  parser.add_argument("--data", nargs="+")
  parser.add_argument("--debug", "-d", action="store_true")
  return parser.parse_args()


def load_data(day):
  with open(FILE_INPUT_SLUG.format(day), 'r') as f:
    data = f.readlines()
  for line in data:
    yield line.strip()
