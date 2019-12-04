import lib
from collections import Counter

def check(pw):
    try:
        # check 2 adjacent digits are the same
        c = Counter()
        for i in pw:
            c[i] += 1

        # assert there is a double
        # n.b. this is a hack -- it does not guarantee they are consecutive!
        # However, the precondition that the numbers are sorted means that if
        # some number is going to be repeated, it needs to be here.
        counts = dict(c).values()
        assert 2 in counts

        # always increase or stay the same
        assert "".join(sorted(pw)) == pw
        return 1
    except AssertionError:
        return 0


def first(data, debug=False):
  print(sum(check(str(pw)) for pw in range(387638, 919124)))


if __name__ == "__main__":
  args = lib.parse_args()
  data = args.data or lib.load_data(4)
  ans = first(data, debug=args.debug)
  print(ans)
