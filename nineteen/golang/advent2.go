package main

import (
  "fmt"
  "io/ioutil"
  "strings"
  "strconv"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}

func OpToInt(orig []string) []int64 {
  r := make([]int64, len(orig))
  for i, v := range orig {
    val, err := strconv.ParseInt(strings.TrimSpace(v), 10, 64)
    check(err)
    r[i] = val
  }
  return r
}

func main() {
  dat, err := ioutil.ReadFile("../data/2.txt")
  check(err)

  compMem := OpToInt(strings.Split(string(dat), ","))
  compMem[1] = 12
  compMem[2] = 2

  i := 0
  opSize := 4
  op := make([]int64, opSize)

  for len(compMem) > i {
    op = compMem[i:i+opSize]

    if op[0] == 99 {
      fmt.Println("Exiting code.")
      break
    } else if op[0] == 1 {
      compMem[op[3]] = compMem[op[1]] + compMem[op[2]]
    } else if op[0] == 2 {
      compMem[op[3]] = compMem[op[1]] * compMem[op[2]]
    }
    i = i + 4
  }
  fmt.Println(compMem[0])
}
