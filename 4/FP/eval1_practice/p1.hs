-- Using only Type Declarations and Pattern Matching (do not use Guards), write the Haskell syntax for a function named listLength.
--     It must accept a list of any type a.
--     It must return an Int.
--     If the list is empty [], it returns 0.
--     If the list is not empty, it deconstructs the list and returns 1 plus the listLength of the tail.

listLength :: [a] -> Int
listLength [] = 0
listLength [x] = 1
listLength [x:xs] = 1 + listLength [xs]
