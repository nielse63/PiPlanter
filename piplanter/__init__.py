# main submodule that runs temp, humidity, light, and water scripts

# source: https://github.com/HackerShackOfficial/Automated-Gardener/blob/master/gardener.py
import atexit
from piplanter.light import Light
from apscheduler.schedulers.base import BaseScheduler


def on_exit(scheduler: BaseScheduler) -> None:
    if scheduler.running:
        scheduler.shutdown()


def init_light() -> None:
    light = Light()
    light.schedule_jobs()
    atexit.register(on_exit, light.scheduler)


def main() -> None:
    init_light()


if __name__ == "__main__":
    main()
