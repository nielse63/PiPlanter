import threading
from typing import Callable, Sequence


def threaded(job_func: Callable, **kwsargs: Sequence) -> None:
    job_thread = threading.Thread(target=job_func, kwargs=dict(**kwsargs))
    job_thread.start()
