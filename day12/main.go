package main

import (
    "bufio"
    "fmt"
    "os"
    "slices"
)

type Region = map[Plot]bool

type Plot struct {
    x, y int
}

func adjacent_to_any(p Plot, region Region) bool {
    for rp, _ := range region {
        switch rp {
            case Plot{p.x, p.y-1}:
                return true
            case Plot{p.x, p.y+1}:
                return true
            case Plot{p.x-1, p.y}:
                return true
            case Plot{p.x+1, p.y}:
                return true
            default:
        }
    }
    return false
}

func _perimeter(p Plot, region Region) int {
    per := 0
    if !region[Plot{p.x-1,p.y}] {
        per += 1
    }
    if !region[Plot{p.x+1,p.y}] {
        per += 1
    }
    if !region[Plot{p.x,p.y-1}] {
        per += 1
    }
    if !region[Plot{p.x,p.y+1}] {
        per += 1
    }
    return per
}

func perimeter(region Region) int {
    per := 0
    for p, _ := range region {
        per += _perimeter(p, region)
    }
    return per
}

func cost(region Region) int {
    return perimeter(region)*len(region)
}

func _corners(p Plot, region Region) int {
    c := 0
    if !region[Plot{p.x-1, p.y}] && !region[Plot{p.x, p.y-1}] {
        c += 1
    }
    if !region[Plot{p.x-1, p.y}] && !region[Plot{p.x, p.y+1}] {
        c += 1
    }
    if !region[Plot{p.x+1, p.y}] && !region[Plot{p.x, p.y-1}] {
        c += 1
    }
    if !region[Plot{p.x+1, p.y}] && !region[Plot{p.x, p.y+1}] {
        c += 1
    }
    if region[Plot{p.x-1, p.y}] && region[Plot{p.x, p.y-1}] && !region[Plot{p.x-1, p.y-1}] {
        c += 1
    }
    if region[Plot{p.x-1, p.y}] && region[Plot{p.x, p.y+1}] && !region[Plot{p.x-1, p.y+1}] {
        c += 1
    }
    if region[Plot{p.x+1, p.y}] && region[Plot{p.x, p.y-1}] && !region[Plot{p.x+1, p.y-1}] {
        c += 1
    }
    if region[Plot{p.x+1, p.y}] && region[Plot{p.x, p.y+1}] && !region[Plot{p.x+1, p.y+1}] {
        c += 1
    }
    return c
}

func sides(region Region) int {
    s := 0
    for p, _ := range region {
        s += _corners(p, region)
    }
    return s
}

func discount_cost(region Region) int {
    return sides(region)*len(region)
}

func main() {
    filepath := os.Args[1]
    file, err := os.Open(filepath)
    if err != nil {
        fmt.Println("Error opening file: ", err)
        return
    }
    defer file.Close()

    regions := make(map[rune][]Region)

    scanner := bufio.NewScanner(file)
    for y := 0; scanner.Scan(); y++ {
        line:
        for x, p := range scanner.Text() {
            for _, region := range regions[p] {
                if adjacent_to_any(Plot{x, y}, region) {
                    region[Plot{x, y}] = true
                    continue line
                }
            }
            regions[p] = slices.Insert(regions[p], 0, map[Plot]bool{Plot{x, y}: true})
        }
    }

    for _, p_regions := range regions {
        move:
        for {
            for i := 0; i < len(p_regions)-1; i++ {
                for j := i+1; j < len(p_regions); j++ {
                    for iplot := range p_regions[i] {
                        if adjacent_to_any(iplot, p_regions[j]) {
                            for jplot, _ := range p_regions[j] {
                                p_regions[i][jplot] = true
                            }
                            p_regions[j] = map[Plot]bool{}
                            continue move
                        }
                    }
                }
            }
            break
        }
    }

    result_1 := 0
    result_2 := 0

    for _, p_regions := range regions {
        for _, region := range p_regions {
            c := cost(region)
            d := discount_cost(region)
            result_1 += c
            result_2 += d
        }
    }

    fmt.Println("Part 1: ", result_1)
    fmt.Println("Part 2: ", result_2)
}

