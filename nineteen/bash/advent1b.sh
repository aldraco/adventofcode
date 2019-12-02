#!/bin/bash

# cat $DATAFILE | ./advent1.sh

calc_fuel() { new_fuel=$(($1/3 - 2)); }
total_fuel=0

while read m; do
  # figure out how much fuel we need and keep adding it.
  calc_fuel $m
  while (("$new_fuel" > 0)); do
    ((total_fuel=$total_fuel+$new_fuel))
    calc_fuel $new_fuel
  done
done

echo $total_fuel


# - put variable in quotes if comparing values (why?)
# - otherwise it seems to evaluate as a command.
