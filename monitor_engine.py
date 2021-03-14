from django.conf import settings
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'monitor.settings'
import django
django.setup()

from monitor.models import Sites,lkpResult
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from datetime import datetime, date, time, timedelta
import pytz
import requests

utc=pytz.UTC

def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

def checkHeartBeats():
    sites = Sites.objects.filter(ping_id=1)
    now = utc.localize(datetime.today())
    for site in sites:
        if site.lastCheck == None or (site.lastCheck + timedelta(minutes=site.frequency))  < now:
            host = site.url.split('://')
            result = ping(host[1])
            thisResult = lkpResult.objects.get(code='FAIL')
            if result:
                thisResult = lkpResult.objects.get(code='LIVE')
            site.lastResult = thisResult
            site.lastCheck = now
            site.save()
        else:
            print("Skipped: " + site.name)

def checkRequests():
    sites = Sites.objects.filter(ping_id=2)
    now = utc.localize(datetime.today())
    for site in sites:
        if site.lastCheck == None or site.lastCheck == None or (site.lastCheck + timedelta(minutes=site.frequency))  < now:
            result = requests.get(site.url)
            print(result.text)
            print(result.status_code)
            thisResult = lkpResult.objects.get(code='FAIL')
            if site.desiredResult_id == 3:
                if result.text == site.resultValue:
                    thisResult = lkpResult.objects.get(code='LIVE')
            else:
                if result.status_code == 200:
                    thisResult = lkpResult.objects.get(code='LIVE')
            site.lastResult = thisResult
            site.lastCheck = now
            site.save()
        else:
            print("Skipped: " + site.name)

# Main part of the script
checkHeartBeats()
checkRequests()
print("*** Update Complete ***")    

# New Approach
# pip3 install schedule
import schedule
import time

def job():
    checkHeartBeats()
    checkRequests()
    print("*** Job Complete ***")    

# schedule.every(60).seconds.do(job)
schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)