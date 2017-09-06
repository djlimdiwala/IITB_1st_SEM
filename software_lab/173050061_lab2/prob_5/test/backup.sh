cd /users/pg17/djlimdi/Downloads/prob_1/
total=`find /users/pg17/djlimdi/Downloads/prob_2/* -mtime -1`
for line in $total
do
	cp $line /users/pg17/djlimdi/Downloads/backup/ 
done

total=`find /users/pg17/djlimdi/Downloads/prob_2/* -ctime -1`
for line in $total
do
	cp $line /users/pg17/djlimdi/Downloads/backup/ 
done
