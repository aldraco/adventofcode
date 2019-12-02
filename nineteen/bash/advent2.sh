#!/bin/bash
# ./advent2.sh | cat ../data/2.txt

# Data comes in as csv
IFS=","
read -ra data

# set computer memory
# nifty trick for default values in Bash
data[1]=${1:-12}
data[2]=${2:-2}

s=0
# this tripped me up for a while; echo here outputs with spaces, not commas
IFS=" "
while read -r opcode loc1 loc2 outloc <<< $(echo ${data[@]:$s:4}); do
  if [ "${opcode}" -eq 99 ]; then
    echo "${data[0]}"
    exit
  elif [ "$opcode" -eq 1 ]; then
    data["$outloc"]=$((${data[$loc1]} + ${data[$loc2]}))
  elif [ "$opcode" -eq 2 ]; then
    data["$outloc"]=$((${data[$loc1]} * ${data[$loc2]}))
  fi
  s=$s+4
done
