co=1
cd test
for file in `ls`
do
	#mv $file /users/pg17/djlimdi/Downloads/test/${co}.c
	mv $file ${co}.c
	echo $file
	co=$((co+1))
done