#! /bin/bash
set -e

# Map language to extension
declare -A lang_extensions
lang_extensions=(["python"]="py" ["ruby"]="rb" ["golang"]="go" ["bash"]="sh")

# Create the new module for the day
FILENAME="${2}/advent${1}.${lang_extensions[$2]}"
mkdir -p $2

# be nice
if test -f $FILENAME; then
  echo "This file already exists!"
  read -p "Do you want to overwrite it?" yn
  case $yn in
    [yY]* ) echo "Continuing";;
    [nN]* ) echo "Exiting."; exit;;
    * ) echo "Please answer y or n.";;
  esac
fi

touch $FILENAME
chmod 774 $FILENAME

# Put some basic template stuff in there if we have one
TEMPLATE=templates/$2.${lang_extensions[$2]}
if test -f $TEMPLATE; then
  sed "s/ADVENT_DAY/$1/g" <<< cat $TEMPLATE | tee $FILENAME
fi
