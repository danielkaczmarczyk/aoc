package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := os.ReadFile("./input")
	check(err)

	floor := 0

	for _, c := range dat {
		char := string(c)
		if char == `(` {
			floor += 1
		} else if char == `)` {
			floor -= 1
		}
	}

	fmt.Println(floor)
}
