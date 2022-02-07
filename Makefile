default:
	python3	src/main.py google.com/search? files/animal100.txt

cat_json:
	cat src/files/companies_info.json


exe:
	time python3 src/main.py bell src/files/data.csv 1
	time python3 src/main.py bell src/files/data.csv 2
	time python3 src/main.py bell src/files/data.csv 3
	time python3 src/main.py bell src/files/data.csv 4
	time python3 src/main.py bell src/files/data.csv 5
	time python3 src/main.py bell src/files/data.csv 6
	time python3 src/main.py bell src/files/data.csv 7
	time python3 src/main.py bell src/files/data.csv 8
	time python3 src/main.py bell src/files/data.csv 9
	time python3 src/main.py bell src/files/data.csv 10



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
	python3 src/main.py aol1 src/files/sample.csv 1
	python3 src/main.py aol2 src/files/sample.csv 1
	python3 src/main.py aol3 src/files/sample.csv 1
	python3 src/main.py aol4 src/files/sample.csv 1
	python3 src/main.py i-web src/files/sample.csv 1
	python3 src/main.py e2R src/files/sample.csv 1
	python3 src/main.py HRMOS src/files/sample.csv 1
	python3 src/main.py R-SHIP src/files/sample.csv 1
	python3 src/main.py job-sweet src/files/sample.csv 1
	python3 src/main.py bell src/files/sample.csv 1

reset:
	rm -id  src/csv


debug01:
	python3 src/main.py aol1 src/files/full.csv 1
	python3 src/main.py aol1 src/files/full.csv 2
	python3 src/main.py aol1 src/files/full.csv 3
	python3 src/main.py aol1 src/files/full.csv 4
	python3 src/main.py aol1 src/files/full.csv 5
	python3 src/main.py aol1 src/files/full.csv 6
	python3 src/main.py aol1 src/files/full.csv 7
	python3 src/main.py aol1 src/files/full.csv 8
	python3 src/main.py aol1 src/files/full.csv 9
	python3 src/main.py aol1 src/files/full.csv 10

debug10:
	python3 src/main.py i-web src/files/full.csv 1
	python3 src/main.py i-web src/files/full.csv 2
	python3 src/main.py i-web src/files/full.csv 3
	python3 src/main.py i-web src/files/full.csv 4
	python3 src/main.py i-web src/files/full.csv 5
	python3 src/main.py i-web src/files/full.csv 6
	python3 src/main.py i-web src/files/full.csv 7
	python3 src/main.py i-web src/files/full.csv 8
	python3 src/main.py i-web src/files/full.csv 9
	python3 src/main.py i-web src/files/full.csv 10


# nvim files
main:
	nvim src/main.py

url:
	nvim src/url.py

json:
	nvim src/files/companies_info.json


# Compile pyinstaller
script:
	dist/crawlerapp

compile:
	pyinstaller src/main.py --paths=src --onefile --name crawlerapp



