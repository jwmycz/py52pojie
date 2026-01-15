from apscheduler.schedulers.blocking import BlockingScheduler
job_defaults = {
    'coalesce': True,
    'misfire_grace_time': 1500,
}
scheduler = BlockingScheduler(timezone='Asia/Shanghai', job_defaults=job_defaults)