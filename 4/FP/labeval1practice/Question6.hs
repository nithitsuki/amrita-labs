power :: Int -> Int -> Int
power x y
    | y==0 = 1
    | y /= 0 = x*(power x (y-1))
main = do
    putStrLn "Enter number"
    input1 <- getLine
    putStrLn "Enter power"
    input2 <- getLine
    let num1 = read input1 ::Int
    let num2 = read input2 ::Int
    let result = power num1 num2
    putStrLn(show result)