.PHONY:build
build:
	cd src && python3 ./setup.py install
run:build
	python3 -m thirdhand
clean:
	rm -rf src/build
	rm -rf src/dist
	rm -rf src/third_hand.egg-info
