describeList :: [a] -> String
describeList lst = case lst of
    [] -> "Empty list"
    [x] -> "Single element list"
    (x:y:_) -> "Multiple element list"

main = do
    print (describeList []) 
    print (describeList [42]) 
    print (describeList [1,2,3]) 