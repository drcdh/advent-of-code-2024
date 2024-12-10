package main

import (
    "bufio"
    "fmt"
    "os"
    "slices"
)

func print_diskmap(ids, sizes []int) {
    for i, id := range ids {
        for j := 0; j < sizes[i]; j++ {
            if id == -1 {
                fmt.Printf(".")
            } else {
                fmt.Printf("%d", id)
            }
        }
    }
    fmt.Println()
}

func defrag(line string) {
    var ids []int
    var sizes []int
    for i, char := range line {
        size := int(char) - 48
        //fmt.Printf("%d %d\n", i, size)
        sizes = append(sizes, size)
        if i%2 == 0 {
            ids = append(ids, i/2)
        } else {
            ids = append(ids, -1)
        }
    }
    //print_diskmap(ids, sizes)
    moved := map[int]bool{}
    out:
    for {
        move_made := false
        for j := len(sizes)-1; j >= 0; j-- {
            r_id := ids[j]
            r_size := sizes[j]
            if r_id == -1 || moved[r_id] {
                continue
            }
            for i := 0; i < j; i++ {
                l_id := ids[i]
                l_size := sizes[i]
                if l_id >= 0 {
                    continue
                }
                if l_size >= r_size {
                    ids[i] = -1
                    sizes[i] = l_size - r_size
                    ids[j] = -1
                    ids = slices.Insert(ids, i, r_id)
                    sizes = slices.Insert(sizes, i, r_size)
                    moved[r_id] = true
                    move_made = true
                    break
                }
            }
            if move_made {
                break
            }
            if j <= 0 {
                break out
            }
        }
    }
    //print_diskmap(ids, sizes)

    checksum := 0
    b := 0
    for i, id := range(ids) {
        for j := 0; j < sizes[i]; j++ {
            if id >= 0 {
                checksum += b*id
            }
            b++
        }
    }
    fmt.Println(checksum)
}

func main() {
    filepath := "input"
    //filepath := "test"
    file, err := os.Open(filepath)
    if err != nil {
        fmt.Println("Error opening file: ", err)
        return
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    if scanner.Scan() {
        line := scanner.Text()

        defrag(line)
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file: ", err)
    }
}

