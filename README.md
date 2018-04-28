# Pengwin - Version 0.1.0
Pengwin is a Slack chatbot which reports sports stats to users. The goal is to expand Pengwin's funtionality across multiple tech spaces.

## Getting Started
Please read this section first!

### Prerequisites
Pengwin runs on Python v3.6.4.

### Packages
Packages that are necessary to run Pengwin:
```
slackclient
pymongo
```
You can install these using pip.
```
pip install slackclient
pip install pymongo
```
This will eventually be moved into a requirements file.

### Installing
In your working directory:
```
virtualenv pengwin
cd pengwin
source bin/activate
export SLACK_BOT_TOKEN='<enter oauth bot user token here>'
```

## Running
You're now ready to run Pengwin, give it a go!
```
python bot.py
```

## Coding Guidelines
Those who wish to contribute to Pengwin must adhere to PIP8 coding standards. This means use DOCSTRINGS.

### Steps
1. Create a branch
2. Push to branch
3. Submit pull request

## File Structure
* bot.py
* actions.py
* nba.py

## Technologies Utilized
* Slack
* AWS

## Author
Drew Taylor