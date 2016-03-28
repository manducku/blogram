clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate:
	python blogram/manage.py makemigrations users 
	python blogram/manage.py migrate 

test:
	python blogram/manage.py users 