clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate:
	python blogram/manage.py makemigrations users posts tags
	python blogram/manage.py migrate 

test:
	python blogram/manage.py users 
