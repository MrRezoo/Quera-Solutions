package main

import (
	"fmt"
)

func HelloCodeCup(n int) string {
	return fmt.Sprintf("Hello CodeCup %d", n)
}

func main() {
	str := HelloCodeCup(6)
	fmt.Println(str)
}
