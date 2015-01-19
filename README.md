# ER/EI End-to-End Test

Welcome to Etu Insight! This document will show you how to use `python + selenium + phantomjs` to simulating user behavior and verify the whole software functionality.

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
	```

	- phantomjs (quick and lightweight alternative)
	```
	brew update && brew install phantomjs
	```

- How to use test python codes
	- input: csv files [example](https://github.com/suensummit/erjsTesting/blob/gh-pages/web_test_funnel.csv)
	- format: 

	| date | Time | ssid | uid | eruid | lo | act | cat | pid | pcat | paypid | qty | unit_price | oid | amt | ERCAMP | ERAD |
	|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
	| 1201 | 11:10 | S01 | U01 | ERU01 | 0 | VIEW | "CAT01_1,CAT01_2,CAT01_3,CAT01_4,CAT01_5" | PID01 |  |  |  |  |  |  | CAMP1 | AD1.1 |
	| 1201 | 11:30 | S02 | U02 | ERU02 | 0 | VIEW | "CAT02_1,CAT02_2,CAT02_3,CAT02_4,CAT02_5" | PID02 |  |  |  |  |  |  | CAMP2 | AD2.1 |

- 
