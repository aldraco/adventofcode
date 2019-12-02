import lib


def first(data, debug=False):
  pass

def second(data, debug=False):
  pass

if __name__ == "__main__":
  args = lib.parse_args()
  data = args.data or lib.load_data(ADVENT_DAY)
  ans = first(data, debug=args.debug)
  print(ans)
  ans2 = second(data, debug=args.debug)
  print(ans2)
