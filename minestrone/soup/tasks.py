import time

from celery.task import task

@task(ignore_result=True)
def lazy_job(name):
    logger = lazy_job.get_logger()
    logger.info('Starting the lazy job: {0}'.format(name))
    time.sleep(5)
    logger.info('Lazy job {0} completed'.format(name))
