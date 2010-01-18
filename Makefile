all:
	python ./main.py | neato -n2 -Tpng > trip.png
	open trip.png
