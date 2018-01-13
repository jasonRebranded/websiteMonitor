#!/usr/bin/python
from robobrowser import RoboBrowser
import schedule
import time
import datetime

# Browse to site
browser = RoboBrowser(history=True, parser='html.parser')
# set url for testing
browser.open("add target URL")
# expected response url on successful search submission
response_browser_page = "add the results page that is presented on submission"
form = browser.get_form(action="add the results page that is presented on submission")
status = str(browser.response)

def job():
  # write the reponse to file
  f = open("results.txt", "a+")
  f.write(str(browser.response) + " at ")
  f.write(datetime.datetime.now().ctime() + "\n")
  f.close()

if "200" in status:
  print("site is up")
else:
  print("site is down")

schedule.every(5).minutes.do(job)

while 1:
  schedule.run_pending()
  time.sleep(1)
