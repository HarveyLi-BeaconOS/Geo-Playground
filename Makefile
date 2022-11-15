windows_-config:
	curl.exe --output python.exe --url https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
	python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
	python3 -m pip install pyinstaller
	python3 -m pip install gnureadline

linux_debian_config:
	sudo apt install python3
	python3 -m pip install pyinstaller
	python3 -m pip install gnureadline

exec: interpreter.py
	pyinstaller interpreter.py \
	--onefile \
	--name Geo_Playground \
	--collect-all gnureadline
