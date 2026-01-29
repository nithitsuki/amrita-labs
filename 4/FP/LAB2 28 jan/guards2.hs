numberCategory :: Int->String
numberCategory n
    | n < 0 = "Negative"
    | n == 0 = "Zero"
    | otherwise = "Positive"

main = do
    putStrLn("Enter a number:")
    inpt <- getLine
    let n = read inpt :: Int
    let category = numberCategory n
    putStrLn("The number is: " ++ category)
    