import lib
import copy

OPS = {
    1: lambda x, y: (x + y),
    2: lambda x, y: (x * y),
}


def first(data, hack1=12, hack2=2, debug=False):
  output = [int(a) for a in data]
  datagen = (d for d in output)
  # hacks
  output[1] = hack1
  output[2] = hack2
  while True:
      try:
          cmd = [next(datagen) for _ in range(4)]
          op_, in1, in2, out = cmd
          if op_ == 99:
              raise StopIteration
          op = OPS.get(op_, None)
          if not op:
              raise ValueError("Unknown OP code {}".format(op_))
          output[out] = op(output[in1], output[in2])

      except StopIteration:
          break
  return output[0]


def second(data, debug=False):
  # try a bunch of values for a and b
  for i in range(100):
      for j in range(100):
          tester = first(data, hack1=i, hack2=j)
          if tester == 19690720:
             return (i, j)

if __name__ == "__main__":
  args = lib.parse_args()
  data = args.data or list(lib.load_data(2))[0]
  # some data cleaning is needed
  data = data.split(",")
  ans = first(data, debug=args.debug)
  print(ans)
  ans2 = second(data, debug=args.debug)
  print(ans2)
