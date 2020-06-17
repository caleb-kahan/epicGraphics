all:	dwRun1 main.py	matrix.py	mdl.py display.py draw.py	gmath.py
	python3	main.py	dwRun1
gallery1: gallerySubmission.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python3	main.py	gallerySubmission.mdl
gallery2: eric_image.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python3	main.py	eric_image.mdl
clean:
	rm *pyc *out parsetab.py
clear:
	rm *pyc *out parsetab.py *ppm
