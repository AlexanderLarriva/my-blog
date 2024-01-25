start:
	python3 manage.py runserver

test:
	python3 manage.py test tests/

console:
	@django-admin shell
