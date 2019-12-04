import lib
from collections import Counter

def check(pw):
    try:
        asstr = str(pw)
        assert len(asstr) == 6, "not long enough"
        # check 2 adjacent digits are the same
        assert len(set(asstr)) < len(asstr), "no repeats"
        c = Counter()
        for i in asstr:
            c[i] += 1

        # assert there is a double
        # n.b. this is a hack -- it does not guarantee they are consecutive!
        # However, the precondition that the numbers are sorted means that if
        # some number is going to be repeated, it needs to be here.
        counts = dict(c).values()
        assert 2 in counts

        # always increase or stay the same
        assert "".join(sorted(asstr)) == asstr
        return True
    except AssertionError:
        return False


def first(data, debug=False):
  c = 0
  print(check(112233))
  print(check(123444))
  print(check(111122))
  for pw in range(387638, 919124):
      if check(pw) is True:
          c += 1
  return c


if __name__ == "__main__":
  args = lib.parse_args()
  data = args.data or lib.load_data(4)
  ans = first(data, debug=args.debug)
  print(ans)
