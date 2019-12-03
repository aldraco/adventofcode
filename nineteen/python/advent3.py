import lib

def manhattan(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


class Point:
    def __init__(self, x, y, step=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y <= other.y)

    def __gt__(self, other):
        return not self < other

    def modify(self, instruction):
        direction = instruction[0]
        amt = int(instruction[1:])
        if direction == "U":
            # increase Y
            return Point(self.x, self.y + amt, step=None)
        elif direction == "D":
            return Point(self.x, self.y - amt, step=None)
        elif direction == "R":
            return Point(self.x + amt, self.y, step=None)
        elif direction == "L":
            return Point(self.x - amt, self.y, step=None)


class Span:
    """A line, from one point to another."""
    def __init__(self, p1, p2, base_step=None):
        # Always sort points X-wise, Y-wise
        if p1 < p2:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

        self.vertical = p1.x == p2.x
        self.horizontal = not self.vertical
        self._points = None
        self._origin = p1

        self.base_step = base_step

    def __repr__(self):
        return f"{self.p1} to {self.p2}"

    def __str__(self):
        return self.__repr__()


    def perpendicular(self, other):
        """Perpendicularity does not concern intersection."""
        return (self.p1.x == self.p2.x and other.p1.y == other.p2.y) or (self.p1.y == self.p2.y and other.p1.x == other.p2.x)

    def intersects(self, other):
        """Does this Span intersect with the other one?
        If it does, return the set of Points where they occupy
        the same space.
        """
        return [pt for pt in other.points if self.contains(pt)]

    def steps_to_point(self, point):
        if not self.contains(point):
            return None
        if self.vertical:
            return self.base_step + abs(point.y - self._origin.y)
        else:
            return self.base_step + abs(point.x - self._origin.x)

    @property
    def points(self):
        if self._points is None:
            if self.vertical:
                # go up
                points = [Point(self.p1.x, i) for i in range(self.p1.y, self.p2.y + 1)]
            else:
                points = [Point(i, self.p1.y) for i in range(self.p1.x, self.p2.x + 1)]
            self._points = points
        return self._points

    def contains(self, p):
        """Is this point contained on this span?"""
        if self.vertical:
            return p.x == self.p1.x and self.p1.y <= p.y <= self.p2.y
        else:
            return p.y == self.p1.y and self.p1.x <= p.x <= self.p2.x


def first(data, debug=False):
  origin = Point(0, 0)
  instructions = data[0].split(",")
  spans = []
  old = origin
  for inst in instructions:
      new = old.modify(inst)
      n = Span(old, new)
      spans.append(n)
      old = new

  spans2 = []
  old = origin
  instructions2 = data[1].split(",")
  for inst in instructions2:
    new = old.modify(inst)
    n = Span(old, new)
    spans2.append(n)
    old = new

  # now find intersection points
  pts_to_check = []
  for a in spans:
      for b in spans2:
          pts = a.intersects(b)
          if pts:
              pts_to_check += pts

  min = None  # will be a Tuple
  for pt in pts_to_check:
      if pt == origin:
          continue
      dist = manhattan(pt, origin)
      if not min or dist < min[0]:
          min = (dist, pt)
  return min[0]


def second(data, debug=False):
  origin = Point(0, 0)

  instructions = data[0].split(",")
  spans = []
  old = origin
  steps = 0
  for inst in instructions:
      new = old.modify(inst)
      n = Span(old, new, base_step=steps)
      spans.append(n)
      old = new
      steps += int(inst[1:])

  spans2 = []
  old = origin
  steps = 0
  instructions2 = data[1].split(",")
  for inst in instructions2:
    new = old.modify(inst)
    n = Span(old, new, base_step=steps)
    spans2.append(n)
    old = new
    steps += int(inst[1:])

  # now find intersection points
  pts_to_check = []
  for a in spans:
      for b in spans2:
          pts = a.intersects(b)
          if pts:
              pts = [(a, b, p) for p in pts]
              pts_to_check += pts

  min = None
  for a, b, pt in pts_to_check:
      if pt == origin:
          continue
      dist = (a.steps_to_point(pt)) + (b.steps_to_point(pt))
      if not min or dist < min[0]:
          min = (dist, pt)
  return min[0]

if __name__ == "__main__":
  args = lib.parse_args()
  data = args.data or lib.load_data(3)
  data = list(data)

  ans = first(data, debug=args.debug)
  print(ans)
  ans2 = second(data, debug=args.debug)
  print(ans2)
