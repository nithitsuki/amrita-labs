#!/bin/sh
echo "is it morning? pls answer yes or no"
read timeofday
if [ "$timeofday" = "yes" ] then
    echo "Good morning!"
else
    echo "Good day!"
fi

