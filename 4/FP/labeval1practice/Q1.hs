add :: Int -> Int -> Int -> Int
add x y z = x + y + z
main = do
    putStrLn "Enter first number:"
    a <- getLine
    putStrLn "Enter second number:"
    b <- getLine
    putStrLn "Enter third number:"
    c <- getLine
    let ip1 = read a :: Int
    let ip2 = read b :: Int
    let ip3 = read c :: Int
    let sum = add ip1 ip2 ip3
    putStrLn "Sum is:"
    print sum       -- or putStrLn(show sum)
