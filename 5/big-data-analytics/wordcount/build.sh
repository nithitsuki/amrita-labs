#!/usr/bin/env bash
# Compile WordCount.java against the Hadoop classpath and package it as a jar.
set -euo pipefail
cd "$(dirname "$0")"

rm -rf classes wordcount.jar
mkdir -p classes

javac -cp "$(hadoop classpath)" -d classes WordCount.java
jar cf wordcount.jar -C classes .

echo "Built wordcount.jar"
