#load "str.cma";;

let rec count_stones a blinks =
    if blinks == 0 then
        1
    else
        if a == 0 then
            count_stones 1 (blinks-1)
        else
            let s = string_of_int a in
            let l = String.length s in
            if (l mod 2) == 0 then
                let l_stone = int_of_string (String.sub s 0 (l/2)) in
                let r_stone = int_of_string (String.sub s (l/2) (l/2)) in
                (count_stones l_stone (blinks-1)) + (count_stones r_stone (blinks-1))
            else
                count_stones (a*2024) (blinks-1)

let () =
    let blinks = int_of_string (Sys.argv.(1)) in
    let filepath = "input" in
    let input_channel = open_in filepath in 
    let line = input_line input_channel in
    let stones = List.map int_of_string (Str.split (Str.regexp " ") line) in
    let f acc a =
        acc + (count_stones a blinks)
    in
    let result = List.fold_left f 0 stones in
    Printf.printf "Result after %d blinks: %d\n" blinks result

