package main

import (
  "fmt"
  "io/ioutil"
  "strings"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}


func main() {
  dat, err := ioutil.ReadFile("../data/ADVENT_DAY.txt")
  check(err)

  for _, v := range strings.Split(string(dat), "\n") {
    if v == "" {
      continue
    }
    fmt.Println(v)
  }
}
