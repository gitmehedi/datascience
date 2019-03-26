# TWITTER DATA COLLECTION

## Required Python Packages
- Install [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi) library
  _**$ sudo pip install pandas**_
- Install [tweepy](https://github.com/tweepy/tweepy) library for python and twitter
  _**$ sudo pip install tweepy**_
## Server Install

- Create a cron job using [crontab](https://crontab.guru/#*/1_*_*_*_*)
- Open crontab using
  _**$ crontab -e**_
- Add following line below in crobtab
  _**1 * * * * /usr/bin/python2.7 /opt/datascience/tweepy/hello_tweepy.py**_
