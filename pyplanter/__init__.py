# main submodule that runs temp, humidity, light, and water scripts

# source: https://github.com/HackerShackOfficial/Automated-Gardener/blob/master/gardener.py
# import atexit
from typing import Callable

from apscheduler.schedulers.blocking import BlockingScheduler

from pyplanter.environment.sun import Sun
from pyplanter.logger import logger
from pyplanter.tools.pump import Pump

# from apscheduler.schedulers.asyncio import AsyncIOScheduler


__version__ = "0.0.1"


class PyPlanter:
    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.pump = Pump()
        self.sun = Sun()

    def add_job(self, fn: Callable, trigger: str = "interval", **kwargs):
        id = f"{fn.__module__}:{fn.__qualname__}"
        self.scheduler.add_job(fn, id=id, trigger=trigger, **kwargs)

    def add_pump_job(self):
        self.add_job(self.pump.start, seconds=1)

    def add_sun_job(self):
        self.sun.get_sunrise()
        self.add_job(self.sun.is_daytime, seconds=10)

    def start(self):
        # self.add_pump_job()
        self.add_sun_job()

        try:
            self.scheduler.start()
        except KeyboardInterrupt:
            self.stop()
        except Exception as error:
            self.stop()
            raise error

    def stop(self):
        self.scheduler.shutdown()


if __name__ == "__main__":
    pyplanter = PyPlanter()
    pyplanter.start()
