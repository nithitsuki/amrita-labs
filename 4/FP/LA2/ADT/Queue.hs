module Queue
  ( Queue,
    emptyQueue,
    isEmpty,
    enqueue,
    dequeue,
    peek
  ) where

data Queue a = QueueImpl [a]

emptyQueue :: Queue a
emptyQueue = QueueImpl []

-- Functions must take the Data Constructor (QueueImpl) in patterns
enqueue :: a -> Queue a -> Queue a
enqueue a (QueueImpl xs) = QueueImpl (xs ++ [a])

dequeue :: Queue a -> Queue a
dequeue (QueueImpl (_:xs)) = QueueImpl xs
dequeue (QueueImpl [])     = error "Empty queue"

peek :: Queue a -> a
peek (QueueImpl (x:_)) = x
peek (QueueImpl [])    = error "Empty queue"

isEmpty :: Queue a -> Bool
isEmpty (QueueImpl xs) = null xs
