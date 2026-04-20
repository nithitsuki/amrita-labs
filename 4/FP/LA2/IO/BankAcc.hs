module BankAcc
(BankAcc,
 newBankAcc,
 checkBalance,
 isEmpty,
 deposit,
 withdraw) where

data BankAcc = BankAccImpl Int

newBankAcc :: BankAcc Int
newBankAcc = BankAccImpl 0


checkBalance :: BankAcc Int -> Int
checkBalance (BankAccImpl (x)) = x

isEmpty :: BankAcc Int -> Bool
isEmpty (BankAccImpl (x)) = x == 0

deposit :: BankAcc Int -> Int -> BankAcc Int
deposit (BankAccImpl (x)) amount = BankAccImpl (x + amount)

withdraw :: BankAcc Int -> Int -> BankAcc Int
withdraw (BankAccImpl (x)) amount = BankAccImpl (x - amount)