users=`last | cut -d ' ' -f 1`
echo $users | tr '[:space:]' '[\n*]' | grep -v "^\s*$" | sort | uniq -c | sort -bnr
