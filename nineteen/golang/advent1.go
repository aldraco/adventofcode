package main

import (
  "fmt"
  "io/ioutil"
  "strings"
  "strconv"
  "os"
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

// Calculate the total fuel, as the fuel adds to the total mass.
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

  // Determine which fuel algorithm to use.
  var program int
  fmt.Sscan(os.Args[1], &program)

  var total int64
  for _, v := range strings.Split(string(dat), "\n") {
    if v == "" {
      continue
    }
    val, err := strconv.ParseInt(v, 10, 0)
    check(err)
    switch program {
    case 1:
      total += calcFuel(val)
    case 2:
      total += calcTotalFuel(val)
    default:
      fmt.Println("Please choose 1 or 2.")
    }
  }
fmt.Println(total)
}
