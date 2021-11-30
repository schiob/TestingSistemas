package main

import "fmt"

func sum(num1, num2 int) int {
	return num1 + num2
}

func main() {
	fmt.Printf("Result: %v\n", sum(1, 2))
}
