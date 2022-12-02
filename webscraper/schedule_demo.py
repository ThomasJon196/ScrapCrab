# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately

from apscheduler.schedulers.blocking import BlockingScheduler


def some_job():
    print("Decorated job")


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=1)
scheduler.start()
