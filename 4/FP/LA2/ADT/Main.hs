module Main where

import Queue

main::IO()
main = do
  putStrLn "Hello World"
  let one = emptyQueue
  let two = enqueue 2 one
  putStrLn $ show $ peek two
