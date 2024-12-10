#load "str.cma";;

let max_of_list l =
    match l with
    | [] -> failwith "Empty list"
    | h::tail -> List.fold_left max h tail

let rec find_combos' test_val numbers value =
    match numbers with
    | [] -> if value == test_val then test_val else 0
    | n::tail -> max_of_list [
        find_combos' test_val tail (value+n);
        find_combos' test_val tail (value*n)
    ]

let find_combos test_val numbers =
    match numbers with
    | n::tail -> find_combos' test_val tail n
    | _ -> failwith "Oops"

let accumulate_lines filepath f init =
    let input_channel = open_in filepath in
    let rec loop acc =
        try
            let line = input_line input_channel in
            loop (f acc line)
        with
        | End_of_file ->
            close_in input_channel;
            acc
    in
    loop init

let parse_line acc line =
    match Str.split (Str.regexp ": ") line with
    | [test_val_str; numbers_str] -> acc + (find_combos (int_of_string test_val_str) (List.map int_of_string (Str.split (Str.regexp " ") numbers_str)))
    | _ -> failwith "Failed to parse"

let () =
    let filepath = "input" in
    Printf.printf "Part 1: %d\n" (accumulate_lines filepath parse_line 0)

