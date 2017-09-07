cd dev_wrd
p=`ls` 
for file in $p
do
	if [ "$file" != "isyms.txt" ] && [ "$file" != "-" ]
	then
	 cmd = "fstcompile --acceptor -isymbols=osyms.txt --keep_isymbols" + file + " " + file
	 os.system(cmd)
	echo $file
	fi
done