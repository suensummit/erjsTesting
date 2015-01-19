# ER/EI End-to-End Test

Welcome to Etu Insight! This document will show you how to use ```python + selenium + phantomjs``` to simulating user behavior and verify the whole software functionality.

- Enviorment Setup
	- python
	```
	# install homebrew first
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	export PATH=/usr/local/bin:/usr/local/sbin:$PATH

	# install python via homebrew
	brew install python
	```
	- selenium
	```
	pip install selenium
	```
	- Firefox (default bouwser driver in selenium)
	```
	# install brew-cask first
	brew tap phinze/homebrew-cask
	brew install brew-cask

	# install firefox via brew-cask
	brew cask install firefox
	- phantomjs (quick and lightweight alternative)
	```
	brew update && brew install phantomjs
	```

- How to use test python codes
	- input: csv files
	- format: (example)[https://github.com/suensummit/erjsTesting/blob/gh-pages/web_test_funnel.csv]

- 
