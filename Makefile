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
	nvim 		src/main.py

script:
	dist/crawlerapp

compile:
	pyinstaller src/main.py --paths=src --onefile --name crawlerapp 
