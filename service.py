from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from git_service import git_backip

app = Flask(__name__)
scheduler = BackgroundScheduler()


def scheduleTask():
    git_backip()
    print("This test runs every 24 hours")


if __name__ == '__main__':
    scheduler.add_job(id='Scheduled Task', func=scheduleTask, trigger="interval", hours=24)
    scheduler.start()
    app.run(host="0.0.0.0")
