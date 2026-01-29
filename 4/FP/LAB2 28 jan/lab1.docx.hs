--1. Write a Haskell function to add three integer numbers.
addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

--2. Write a Haskell function to check if a year is a leap year or not.
checkLeapYear :: Int -> Bool
checkLeapYear year
    | (year `mod` 4 == 0 && year `mod` 100 /= 0) || (year `mod` 400 == 0) = True
    | otherwise = False

--3. Write a Haskell function to find the factorial of a given number.
factorial :: Int -> Int
factorial n
    | n == 0 = 1
    | otherwise = n * factorial (n - 1)

--4. Write a Haskell function to check prime number or not.
isPrime :: Int -> Bool
isPrime n
    | n <= 3 = True
    
--5. Write a Haskell function that categorizes a number as even or odd.
checkEvenOdd :: Int -> String
checkEvenOdd n
    | n `mod` 2 == 0 = "Even"
    | otherwise = "Odd"

--6. Write a Haskell function to find the power of a given number.
power :: Int -> Int -> Int
power base exp
    | exp == 0 = 1
    | otherwise = base * power base (exp - 1)

--7. Consider 2 – 6 questions, write a program by considering Guards function.
-- done previously itself

--8. Create multiple functions for different data types and observe how pattern matching concept works.
-- ???

--9. Write a Haskell function that categorizes a student’s grade according to the given marks. For “F” grade you have to declare the pattern matching statement instead of using guards concept
gradeCategory :: Int -> String
gradeCategory m = case m of
    _ | m >= 90 -> "A"
      | m >= 80 -> "B"
      | m >= 70 -> "C"
      | m >= 60 -> "D"
      | m >= 50 -> "E"
      | otherwise -> "F"