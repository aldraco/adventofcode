#! /bin/bash
set -ex

# Clean up
echo "Cleaning up pycache"
rm -rf __pycache__

# Create the new module for the day
FILENAME="advent${1}.py"

# Put some basic template stuff in there
cat > $FILENAME <<- EOM
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
EOM
