
source ~/Documents/testing/venv/bin/activate

for i in satendrapandeymp narendra.pandey.9480 # Put name of peoples sepated by space
do
	mkdir "$i"
	cp /home/intel/Documents/testing/Fb_details_scrapper/Web-Scraping.py /home/intel/Desktop/Test/$i
	cd $i
	python Web-Scraping.py #Your_Username #Your_Password $i &
	cd ..
	echo $i
done
