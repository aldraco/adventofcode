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

// Calculate fuel quantity, given a mass.
func calcFuel(m int64) int64 {
  return (m / 3) - 2
}

func calcTotalFuel(m int64) int64 {
  var total int64
  newFuel := calcFuel(m)
  for (newFuel >= 0) {
    total += newFuel
    newFuel = calcFuel(newFuel)
  }
  return total
}

func main() {
  dat, err := ioutil.ReadFile("../data/1.txt")
  check(err)

  var total int64
  for _, v := range strings.Split(string(dat), "\n") {
    if v == "" {
      continue
    }
    val, err := strconv.ParseInt(v, 10, 0)
    check(err)
    total += calcTotalFuel(val)
  }
fmt.Println(total)
}
