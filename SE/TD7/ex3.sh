#!/bin/bash
function addition() {
	result=$(($1 + $2))
	echo "$result"
}

function multiplication() {
	result=$(($1 * $2))
	echo "$result"
}

read -p "entrer deux nombres posotifs..." a b
echo -n "la somme de vos deux nombres est: "; addition a b
echo -n "le produit de vos deux nombres est: "; multiplication a b
