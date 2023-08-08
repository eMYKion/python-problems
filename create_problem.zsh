if [[ ! -a $1 ]]; then
	cp _template.py $1
	touch test/cases-$1
else
	echo "ERR: $1 already exists"

fi
