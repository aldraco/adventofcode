package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func readData(filename string) []int64 {
	data, _ := ioutil.ReadFile(filename)

	result := make([]int64, 0)
	for _, v := range strings.Split(string(data), "\n") {
		if v == "" {
			continue
		}
		val, _ := strconv.ParseInt(v, 10, 0)
		result = append(result, val)
	}

	return result
}

func countIncreases(readings []int64) int {
	increases := 0
	for idx := 1; idx < len(readings); idx++ {
		if readings[idx] > readings[idx-1] {
			increases = increases + 1
		}
	}

	return increases
}

func countIncreasesInThree(readings []int64) int {
	increases := 0
	prevWindow := readings[0] + readings[1] + readings[2]
	for i := 3; i < len(readings); i++ {
		currentWindow := prevWindow - readings[i-3] + readings[i]
		if currentWindow > prevWindow {
			increases++
		}
	}
	return increases

}

func main() {
	readings := readData("data.txt")

	fmt.Println(countIncreases(readings))
	fmt.Println(countIncreasesInThree(readings))

}
