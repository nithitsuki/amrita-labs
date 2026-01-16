starTriangle :: Int -> IO ()
starTriangle n = mapM_ putStrLn [replicate ((n-i)) ' ' ++ replicate ((2*i)-1) '*' | i <- [1..n]]

main :: IO ()
main = do
    putStrLn "Enter the number of rows:"
    input <- getLine
    let n = read input :: Int
    starTriangle n
    putStrLn "Triangle printed."
    