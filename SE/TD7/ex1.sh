#!/bin/bash
while true; do
	read -p "Saisie un nombre: " x
	if [ "$x" -gt 20 ]; then
		echo "Plus petit!"
	elif [ "$x" -lt 10 ]; then
		echo "Plus grand!"
	else
		break
	fi
done
