use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let filepath = "input";
    let edge = 70;
    let (start, end) = ((0, 0), (edge, edge));

    let f = File::open(filepath)?;
    let reader = io::BufReader::new(f);

    let mut corruption = Vec::new();

    for line in reader.lines() {
        let line = line?;
        corruption.push(parse_pair(&line));
    }

    let result = try_find_path(1024, &corruption, edge, &start, &end).unwrap();
    println!("Part 1: {}", result);

    Ok(())
}

fn parse_pair(line: &str) -> (i32, i32) {
    let coords: Vec<&str> = line.split(",").map(|s| s.trim()).collect();
    let (x, y) = (coords[0].parse::<i32>().unwrap(), coords[1].parse::<i32>().unwrap());
    return (x, y)
}

fn try_find_path(n: usize, corruption: &Vec<(i32, i32)>, edge: i32, start: &(i32, i32), end: &(i32, i32)) -> Option<i32> {
    let corruption = &corruption[..n];
    let mut unvisited = HashSet::new();
    let mut dist = HashMap::new();
    dist.insert(*start, 0);
    for y in 0i32..=edge {
        for x in 0i32..=edge {
            if !corruption.contains(&(x, y)) {
                unvisited.insert((x, y));
            }
        }
    }
    while unvisited.len() > 0 {
        let current = get_closest(&unvisited, &dist);
        for considered in get_unvisited_neighbors(&current, &unvisited, &edge) {
            if !dist.contains_key(&current) {
                return None;
            }
            let new_cost = dist.get(&current).unwrap() + 1;
            if !dist.contains_key(&considered) || new_cost < *dist.get(&considered).unwrap() {
                dist.insert(considered, new_cost);
            }
        }
        unvisited.remove(&current);
        if dist.contains_key(&end) {
            break;
        }
    }
    Some(*dist.get(&end).unwrap())
}

fn get_closest(unvisited: &HashSet<(i32, i32)>, dist: &HashMap<(i32, i32), i32>) -> (i32, i32) {
    *unvisited.iter().min_by_key(|n| dist.get(n).unwrap_or(&i32::MAX)).unwrap()
}

fn get_unvisited_neighbors(p: &(i32, i32), unvisited: &HashSet<(i32, i32)>, edge: &i32) -> Vec<(i32, i32)> {
    let mut neighbors = Vec::new();
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
        let n = (p.0 + dx, p.1 + dy);
        if n.0 >= 0 && n.0 <= *edge && n.1 >= 0 && n.1 <= *edge && unvisited.contains(&n) {
            neighbors.push(n);
        }
    }
    neighbors
}

