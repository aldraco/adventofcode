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

func OpToInt(orig []string) []int {
	r := make([]int, len(orig))
	for i, v := range orig {
		val, err := strconv.Atoi(strings.TrimSpace(v))
		check(err)
		r[i] = val
	}
	return r
}

func main() {
	var i int
	var j int
out:
	for i = 0; i <= 99; i++ {
		for j = 0; j <= 99; j++ {
			fmt.Println(i, j)
			t := calc(i, j)
			if t == 19690720 {
				fmt.Println("Works!")
				break out
			}
		}
	}
}

func calc(def1 int, def2 int) int {
	dat, err := ioutil.ReadFile("../data/2.txt")
	check(err)

	compMem := OpToInt(strings.Split(string(dat), ","))
	compMem[1] = def1
	compMem[2] = def2

	i := 0
	opSize := 4
	op := make([]int, opSize)

	for len(compMem) > i {
		op = compMem[i : i+opSize]

		if op[0] == 99 {
			break
		} else if op[0] == 1 {
			compMem[op[3]] = compMem[op[1]] + compMem[op[2]]
		} else if op[0] == 2 {
			compMem[op[3]] = compMem[op[1]] * compMem[op[2]]
		}
		i = i + 4
	}
	return compMem[0]
}