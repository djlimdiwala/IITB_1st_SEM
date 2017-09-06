co=1
cd test
for file in `ls`
do
	mv $file ${co}.c
	co=$((co+1))
done