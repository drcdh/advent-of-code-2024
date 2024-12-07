// Disclaimer: I used ChatGPT for help with the boilerplate stuff

package main

import (
	"bufio"
	"fmt"
    "math"
	"os"
    "sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var l1 []int
	var l2 []int

    c2 := map[int]int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fields := strings.Fields(line)
		if len(fields) != 2 {
			fmt.Println("Skipping invalid line:", line)
			continue
		}

		num1, err1 := strconv.Atoi(fields[0])
		num2, err2 := strconv.Atoi(fields[1])
		if err1 != nil || err2 != nil {
			fmt.Println("Skipping invalid numbers on line:", line)
			continue
		}

		l1 = append(l1, num1)
		l2 = append(l2, num2)

        c2[num2] = c2[num2] + 1
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

    sort.Ints(l1)
    sort.Ints(l2)

    diff_sum := 0
    sim_sum := 0
    for i := 0; i < len(l1); i++ {
        diff_sum += int(math.Abs(float64(l1[i] - l2[i])))
        sim_sum += l1[i] * c2[l1[i]]
    }

	fmt.Println("Part A:", diff_sum)
	fmt.Println("Part B:", sim_sum)
}

