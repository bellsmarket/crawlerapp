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
