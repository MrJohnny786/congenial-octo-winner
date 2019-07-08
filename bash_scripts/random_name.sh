#!/bin/bash

user=$(whoami)
day=$(date +%A)
path=$(pwd)

file_c=/home/mrjohnny786/microservices/practice/congenial-octo-winner/resources/fixed_colors.txt
file_o=/home/mrjohnny786/microservices/practice/congenial-octo-winner/resources/fixed_objects.txt
file_a=/home/mrjohnny786/microservices/practice/congenial-octo-winner/resources/adjectives.txt
#adj=$(sed -e /^$/d "$file_a")
#col=$(sed -e /^$/d "$file_c")
#obj=$(sed -e /^$/d "$file_o")


col=$(shuf -n 1 $file_c)
adj=$(shuf -n 1 $file_a)
obj=$(shuf -n 1 $file_o)

echo $col $adj $obj
