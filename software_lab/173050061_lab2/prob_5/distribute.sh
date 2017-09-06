cd test
j=`ls`
for line in $j
do
	if [ "$line" != "distribute.sh" ]; then
  

	p=`echo $line | cut -d '.' -f 2`
	mkdir -p $p
	mv $line ${p}/
	fi
done