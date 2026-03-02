
listLengthCase :: [a] -> Int
listLengthCase lst = case lst of
    [] -> 0
    (x:rest) -> 1 + listLengthCase rest

main :: IO ()
main = do
    putStrln "Enter a list of numbers"
    input <- getLine