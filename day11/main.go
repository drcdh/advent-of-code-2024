package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Input struct {
    Stone, Blinks int
}

var cache = make(map[Input]int)

func count_stones(s, b int) int {
    if v, ok := cache[Input{s, b}]; ok {
        return v
    }
    if b == 0 {
        return 1
    }
    if s == 0 {
        return count_stones(1, b-1)
    }
    s_str := strconv.Itoa(s)
    l := len(s_str)
    if l%2 == 0 {
        l_s, _ := strconv.Atoi(s_str[:l/2])
        r_s, _ := strconv.Atoi(s_str[l/2:])
        v := count_stones(l_s, b-1) + count_stones(r_s, b-1)
        cache[Input{s, b}] = v
        return v
    } else {
        v := count_stones(s*2024, b-1)
        cache[Input{s, b}] = v
        return v
    }
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    if scanner.Scan() {
        result := 0
        for s := range strings.Fields(scanner.Text()) {
            result += count_stones(s, 75)
        }
        fmt.Println("Result: ", result)
    }
}

