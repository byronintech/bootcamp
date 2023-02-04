import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

# pycharm environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def send_success_message():
    print('Sending success email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE UP!\nApplication is back up!"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_server_and_container():
    # restart linode server - python's linode library (linode-api4)
    print('Rebooting the server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 42271809)
    nginx_server.reboot()

    # restart the application - wait until the server is in a running state
    while True:
        nginx_server = client.load(linode_api4.Instance, 42271809)
        if nginx_server.status == 'running':
            print('Server is running...')
            time.sleep(10)
            restart_container()
            break


def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('45.79.26.103', username='root', key_filename='/Users/byronksmith/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start 1c542efefe9b')
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    try:
        response = requests.get('http://45-79-26-103.ip.linodeusercontent.com:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f"Application returned {response.status_code}"
            send_notification(msg)
            restart_container()
            send_success_message()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = "Application not accessible at all."
        send_notification(msg)
        restart_server_and_container()
        send_success_message()


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
