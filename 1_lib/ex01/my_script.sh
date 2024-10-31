#!/bin/sh

pip -V | awk '{print $1,$2}'

if [ -d "local_lib" ]; then
	rm -rf local_lib
fi

git clone https://github.com/jaraco/path.git local_lib

cd local_lib
pip install --break-system-packages -e . --log ../install.log

if [ $? -eq 0 ]; then
	cd ..
	python3 my_program.py
else
	echo "Installation failed. Check the log file for details." >&2
fi
