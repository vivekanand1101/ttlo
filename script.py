#!/usr/bin/env python
# coding=utf-8

import time
import datetime
import argparse
import gi

gi.require_version('Notify', '0.7')

from gi.repository import Notify


parser = argparse.ArgumentParser(
        description='Run ttlo')
parser.add_argument(
        '--hours', '-hrs', dest='hours',
        help='Specify how much hour you have to spend, (int)')
parser.add_argument(
        '--time', '-t', dest='time',
        default='2030',
        help='Specify time at which you want to leave, (HHMM)')
args = parser.parse_args()

Notify.init("Time to leave office")

# Create the notification object and show once
notification = Notify.Notification.new("Office time started :(")
notification.show()


def go_home():
    # When done
    notification.update("Ding!", "Go home :)")
    notification.show()


if args.hours:
    hours = int(args.hours)
    time.sleep(60*hours*60)
    go_home()
else:
    while True:
        current_time = datetime.datetime.now().time()
        current_hours = current_time.hour
        current_min = current_time.minute
        if str(current_hours) + str(current_min) == str(args.time):
            go_home()
            break
        else:
            time.sleep(30)
