factorial :: Int -> Int
factorial n
    | n==0 = 1
    | n /=0 =n*factorial(n-1)
main = do
    putStrLn "Enter number"
    input1 <- getLine
    let num1 = read input1 ::Int
    let result = factorial num1
    putStrLn(show result)