#load "str.cma";;

(*
    Thanks to:
    https://cs3110.github.io/textbook/chapters/ds/memoization.html
*)
let memo f =
    let h = Hashtbl.create 100 in
    let rec g s b =
        try
            (*Printf.printf "Seen s=%d b=%d\n" s b;*)
            Hashtbl.find h (s,b)
        with Not_found ->
            let y = f g s b in
            Hashtbl.add h (s,b) y;
            y
    in
    g

let count_stones self a blinks =
    if blinks == 0 then
        1
    else
        if a == 0 then
            self 1 (blinks-1)
        else
            let s = string_of_int a in
            let l = String.length s in
            if (l mod 2) == 0 then
                let l_stone = int_of_string (String.sub s 0 (l/2)) in
                let r_stone = int_of_string (String.sub s (l/2) (l/2)) in
                (self l_stone (blinks-1)) + (self r_stone (blinks-1))
            else
                self (a*2024) (blinks-1)

let () =
    let blinks = int_of_string (Sys.argv.(1)) in
    let filepath = "input" in
    let input_channel = open_in filepath in 
    let line = input_line input_channel in
    let stones = List.map int_of_string (Str.split (Str.regexp " ") line) in
    let f acc a =
        acc + ((memo count_stones) a blinks)
    in
    let result = List.fold_left f 0 stones in
    Printf.printf "Result after %d blinks: %d\n" blinks result

