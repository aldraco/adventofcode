import lib


def first(data, debug=False):
  pass


def second(data, debug=False):
  pass


if __name__ == "__main__":
  args = lib.parse_args()
  ans = first(args.data, debug=args.debug)
  print(ans)
  ans2 = second(args.data, debug=args.debug)
  print(ans2)
