#!/bin/sh
echo "1st number:"
read num1
echo "2nd number:"
read num2
echo "3rd number:"
read num3
if [ $num1 -lt $num2 ] && [ $num1 -lt $num3 ]; then
    echo "num1 is lowest";
else if [ $num2 -lt $num3 ] && [ $num2 -lte $num1 ]; then
    echo "num2 is lowest";
else
    echo "num3 is lowest";
fi