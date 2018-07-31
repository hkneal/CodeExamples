1)Update Config.py - insert your API key for the http://openweathermap.org website.

2)If you need to install a virtual environment:
	a) issue command: sudo apt-get install python-pip python-dev
	b) issue command: sudo apt-get update
	c) issue command: sudo pip install virtualenv

3)Create virtual environment
	- issue command: virtualenv pythonEnv  Note: you can use any name for your virutalenv, I used "pythonEnv".

4)Start virtual environment
	- Issue command: source pythonEnv/bin/activate

5)Install required software/tools
	- Issue command: pip install -r requirements.txt

6)Start server
	- Issue command: python server.py

7)Open a browser and go to: http://localhost:8080
