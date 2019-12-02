#!/bin/bash

# cat $DATAFILE | ./advent1.sh

# echo $1
# does not work; when contents are cat-ted in, each line would be assigned to
# a separate shell var.
# cat data into this script, which will be waiting for it

# so this input needs to be processed as data, once, and cannot be mutated.
# bash does int math only
# also, does not return values, just exit codes
# all variables are global by default; yay!
# more: https://www.linuxjournal.com/content/return-values-bash-functions
echo "Begin"
calc_fuel() { new_fuel=$(($1/3 - 2)); }
total_fuel=0

while read m; do
  # figure out how much fuel we need and keep adding it.
  calc_fuel $m
  ((total_fuel=$total_fuel+$new_fuel))
done

echo $total_fuel
