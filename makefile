helpful: lastTest.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python3	main.py	lastTest.mdl
gallery: face.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python3	main.py	gallerySubmission.mdl
test:	ourTest.mdl main.py	matrix.py	mdl.py display.py draw.py	gmath.py
	python3	main.py	ourTest.mdl
clean:
	rm *pyc *out parsetab.py
clear:
	rm *pyc *out parsetab.py *ppm
