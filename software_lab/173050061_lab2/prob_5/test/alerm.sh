echo "Enter the time"
read date
echo "Alerm set for entered time"
sleep $(( $(date --date="$date" +%s) - $(date +%s) ));
echo "Hey, Its Time"
while true; do
	#aplay minion.m4a
  #/usr/bin/mpg123 ~/minion.m4r
  echo -ne '\007'
  sleep 1
done