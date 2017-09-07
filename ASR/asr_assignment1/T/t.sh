tt=`cat words.vocab`
count=0
for line in $tt
do

	
	if(( $count % 2 == 0 ));then
		echo $line >> words.txt
	fi
	count=$(( count+1 ))
done