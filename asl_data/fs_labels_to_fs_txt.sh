#!/bin/bash

input=$1
#array=$(grep -E '[0-9]{1,4}' $input)

while IFS= read -r var
do
  if [[ $var =~ ^-?[0-9]+$ ]]
  then
     #echo "$var"
     array+=($var)
  else
     array_s+=($var)
  fi
done<"$input"
 
#echo ${array[@]}
echo ${#array[@]}
echo "came"
#echo ${array_s[@]}
echo ${#array_s[@]}

#echo " ${array[@]/%/$'\n'}" | sed 's/^ //' | column

for value in ${array[@]}
do
  echo -en "$value\t"
done>>file.csv

n=${#array_s[@]}

for ((i=0;i<$n;i++)); do
  echo "${array[$i]} : ${array_s[$i]}" >> fs.txt
done
