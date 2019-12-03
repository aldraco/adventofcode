package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// Convert a 4-Array of string to ints.
func OpToInt(orig []string) []int {
	r := make([]int, len(orig))
	for i, v := range orig {
		val, err := strconv.Atoi(strings.TrimSpace(v))
		check(err)
		r[i] = val
	}
	return r
}

// Calculate solution for part 2, day 2.
func main() {
	var i int
	var j int
out:
	for i = 0; i <= 99; i++ {
		for j = 0; j <= 99; j++ {
			t := calc(i, j)
			if t == 19690720 {
        fmt.Println(i, j)
				fmt.Println("Works!")
				break out
			}
		}
	}
}

// Calculate the final computer memory state, given memory values for pos 1 and 2.
func calc(def1 int, def2 int) int {
	dat, err := ioutil.ReadFile("../data/2.txt")
	check(err)

	compMem := OpToInt(strings.Split(string(dat), ","))
	compMem[1], compMem[2] = def1, def2

	opSize := 4
	op := make([]int, opSize)

  out:
	for i := 0; i < len(compMem); i += opSize {
		op = compMem[i : i+opSize]

    switch op[0] {
    case 99:
      break out
    case 1:
      compMem[op[3]] = compMem[op[1]] + compMem[op[2]]
    case 2:
      compMem[op[3]] = compMem[op[1]] * compMem[op[2]]
    default:
      fmt.Println("Something is wrong.")
    }
	}
  return compMem[0]
}
