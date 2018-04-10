for i in satendrapandeymp narendra.pandey.9480 # Put name of peoples sepated by space
do
	mkdir "$i"	
	cp Web-Scraping.py $i
	cd $i
	python Web-Scraping.py #Your username #Your pass $i > log_$i.txt &
	cd ..
	echo $i
done
