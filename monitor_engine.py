from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()

from mysql.connector import Error
from pyasn1.compat.dateandtime import strptime
from monitor.models import Sites,lkpResult
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from datetime import date

def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

def checkHeartBeats():
    sites = Sites.objects.all()
    for site in sites:
        host = site.url.split('://')
        result = ping(host[1])
        thisResult = lkpResult.objects.get(code='FAIL')
        if result:
            thisResult = lkpResult.objects.get(code='LIVE')
        site.lastResult = thisResult
        site.lastCheck = date.today()
        site.save()
        print(result)

# Main part of the script
checkHeartBeats()
print("*** Update Complete ***")    