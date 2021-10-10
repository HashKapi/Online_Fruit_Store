#! /usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time


def cpu_healthy():
    percent = psutil.cpu_percent(1)
    return percent < 80


def good_disk_space(disk):
    usage = shutil.disk_usage(disk)
    free = usage.free / usage.total * 100
    return free > 20


def good_mem_usage():
    usage = psutil.virtual_memory().available
    total = usage / (1024.0 ** 2)
    return total > 500


def localhost_resolved():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


def overall_check():
    sender = 'automation@example.com'
    receiver = '<>@example.com'
    body = 'Please check your system and resolve the issue as soon as possible'
    if not cpu_healthy():
        subject = 'Error - CPU usage is over 80%'
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)

    if not good_disk_space('/'):
        subject = 'Error - Available disk space is less than 20%'
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)

    if not good_mem_usage():
        subject = 'Error - Available memory is less than 500MB'
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)

    if not localhost_resolved():
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)

while True:
    overall_check()
    time.sleep(60)