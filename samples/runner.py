from typing import Callable

from apscheduler.schedulers.background import BackgroundScheduler

from pyplanter.logger import logger


class RunnerStateEnum:
    STOPPED = "stopped"
    RUNNING = "running"


class Runner:
    state = RunnerStateEnum.STOPPED

    def __init__(self):
        self.state = RunnerStateEnum.RUNNING
        self.scheduler = BackgroundScheduler(logger=logger)
        self.jobs = {}

    def add_job(self, id: str, func: Callable, **kwargs):
        logger.debug(f"Adding job to queue: {id}")
        self.jobs[id] = self.scheduler.add_job(func, **kwargs)

    def remove_job(self, id: str):
        logger.debug(f"Removing job from queue: {id}")
        if not self.scheduler.get_job(id):
            logger.warning(f"Unable to remove job {id}")
            return
        self.scheduler.remove_job(id)

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
