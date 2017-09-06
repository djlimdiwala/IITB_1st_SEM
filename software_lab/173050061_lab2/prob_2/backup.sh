#cd /users/pg17/djlimdi/Downloads/prob_1/
#total=`find /users/pg17/djlimdi/Downloads/prob_2/* -mtime -1`
total=`find working_directory/ -mtime -1`

for line in $total
do
	cp $line backup/ 
done

total=`find working_directory/ -ctime -1`
for line in $total
do
	cp $line backup/ 
done
