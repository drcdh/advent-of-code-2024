#load "str.cma";;

let string_to_int_pair s =
    match Str.split (Str.regexp "   ") s with
    | [a; b] -> (int_of_string a, int_of_string b)
    | _ -> failwith "Failed to parse"

let read_lists filename =
  let input_channel = open_in filename in
  try
    let rec read_lines acc =
      try
        let line = input_line input_channel in
        read_lines ((string_to_int_pair line) :: acc)
      with
      | End_of_file -> acc
    in
    let integers = read_lines [] in
    close_in input_channel;
    integers
  with
  | e ->
      close_in_noerr input_channel;
      raise e

let read_and_sort_lists filename =
    let input_channel = open_in filename in
    let rec read_lines acc1 acc2 =
        try
            let line = input_line input_channel in
            match string_to_int_pair line with
            (a, b) -> read_lines (a::acc1) (b::acc2)
        with
        | End_of_file -> acc1, acc2
    in
    let list1, list2 = read_lines [] [] in
    close_in input_channel;
    (List.sort Int.compare list1), (List.sort Int.compare list2)

let () =
    let filename = "input" in
    let list1, list2 = read_and_sort_lists filename in
    let result = List.fold_left2 (fun acc a b -> acc + (Int.abs (a-b))) 0 list1 list2 in
    Printf.printf "Result: %d\n" result

