import lib
import math

def _calc_fuel(mass):
  # divide by 3, round down, subtract 2
  return (math.floor(mass // 3)) - 2

def first(data, debug=False):
  data = data or lib.load_data("1")
  return sum(_calc_fuel(int(m)) for m in data)

def second(data, debug=False):
  data = data or lib.load_data("1")
  total = 0
  for m in data:
    if isinstance(m, str):
      m = int(m)
    fuel_input = m
    while True:
      new_fuel = _calc_fuel(fuel_input)
      if debug:
         print("new fuel: {}".format(new_fuel))
      if new_fuel <= 0:
        break
      else:
        total += new_fuel
        fuel_input = new_fuel
  return total

if __name__ == "__main__":
  args = lib.parse_args()
  ans = first(args.data, debug=args.debug)
  print(ans)
  ans2 = second(args.data, debug=args.debug)
  print(ans2)
