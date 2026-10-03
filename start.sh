#!/bin/bash
echo -ne "\033]0;KonsoleConnect\007"
cd assets || exit 1
python init.py
read -p "Press enter to exit...