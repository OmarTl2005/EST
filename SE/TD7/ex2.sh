#!/bin/bash
declare -a nums
for i in `seq 0 9`; do
	read -p "Saisie un nombre: " num
	nums+=("$num")
done

max=${nums[0]}
min=${nums[0]}
for i in "${nums[@]}"; do
	if ((max < i)); then
		max=$i
	fi
	if ((min > i)); then
		min=$i
	fi
done
echo "Le  max est: $max et le min est: $min"
