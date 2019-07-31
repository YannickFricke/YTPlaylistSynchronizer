.PHONY: run update watch fetch-example pep8 pep8-fix pep8-fix-watch

run: 
	python Main.py run

update:
	python Main.py update

test:
	python -m pytest

watch:
	chokidar "./**/*.py" "./data/**/*.*" -c "clear && make run" --initial

watch-fetch:
	chokidar "./**/*.py" "./data/**/*.*" -c "clear && python Main.py fetch S6RDQP7784M" --initial

watch-test:
	chokidar "./**/*.py" "./data/**/*.*" -c "clear && make test" --initial

watch-update:
	chokidar "./**/*.py" "./data/**/*.*" -c "clear && make update" --initial

fetch-example:
	python Main.py fetch _IORHSf0rDs

pep8:
	python -m autopep8 -d ./**/*.py --exclude ./venv/

pep8-watch:
	chokidar "./**/*.py" -c "clear && make pep8" --initial

pep8-fix:
	python -m autopep8 -r ./**/*.py --in-place --exclude ./venv/

pep8-fix-watch:
	chokidar "./**/*.py" -c "clear && make pep8-fix" --initial
