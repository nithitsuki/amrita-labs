isLeapYear :: Int -> Bool
isLeapYear year
    | year `mod` 400 == 0 = True
    | year `mod` 100 == 0 = False
    | year `mod` 4 == 0  = True
    | otherwise          = False
main = do
    putStrLn "Enter year"
    input1 <- getLine
    let num1 = read input1 ::Int
    let result = isLeapYear num1
    putStrLn(show result)