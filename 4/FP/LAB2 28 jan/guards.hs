factorial::Int->Int
factorial n | (n/=1) = n * factorial(n-1)
            | otherwise = 1

main = do
    putStrLn("Enter val to calc")
    inpt <- getLine
    let n = read inpt :: Int
    let res = factorial n
    putStrLn("Factorial is " ++ show res)
