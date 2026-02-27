evenorodd :: Int -> String
evenorodd n
    | n `mod` 2 ==0 ="even"
    | otherwise = "odd"
main = do
    putStrLn "Enter number"
    input1 <- getLine
    let num1 = read input1 ::Int
    let result = evenorodd num1
    putStrLn(show result)