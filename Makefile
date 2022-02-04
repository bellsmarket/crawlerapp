default:
	python3	src/main.py google.com/search? files/animal100.txt

full:
	python3	src/main.py files/animal.txt

bell:
	python3	src/main.py files/bellsaudio.txt

1000:
	python3	src/main.py files/animal1000.txt

5000:
	python3	src/main.py files/animal5000.txt

main:
	nvim src/main.py

url:
	nvim src/url.py

exe:
	python3 src/main.py

script:
	dist/crawlerapp

compile:
	pyinstaller src/main.py --paths=src --onefile --name crawlerapp

check:
	python3 src/url.py aol1
	python3 src/url.py aol2
	python3 src/url.py aol3
	python3 src/url.py aol4
	python3 src/url.py i-web
	python3 src/url.py e2R
	python3 src/url.py HRMOS
	python3 src/url.py R-SHIP
	python3 src/url.py job-sweet

checkmain:
	python3 src/main.py aol1 src/files/sample15.txt 1
	python3 src/main.py aol2 src/files/sample15.txt 2
	python3 src/main.py aol3 src/files/sample15.txt 3
	python3 src/main.py aol4 src/files/sample15.txt 4
	python3 src/main.py i-web src/files/sample15.txt 5
	python3 src/main.py e2R src/files/sample15.txt 6
	python3 src/main.py HRMOS src/files/sample15.txt 7
	python3 src/main.py R-SHIP src/files/sample15.txt 8
	python3 src/main.py job-sweet src/files/sample15.txt 9
	python3 src/main.py test  src/files/sample15.txt 10
	python3 src/main.py 2222  src/files/sample15.txt 11
