module Main where

import BankAcc

main :: IO ()
main = do
  putStrLn "Enter Flag path: "
  flagPath <- getLine
  print "content is:"
  content <- readFile flagPath
  print $ content
  print "number of lines:"
  print $ unlines $ lines content
  print $ length $ lines content
  print "Enter flag to add"
  newFlag <- getLine
  appendFile flagPath newFlag
