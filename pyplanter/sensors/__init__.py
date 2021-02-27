# from typing import Any


class SensorCache(object):
    # instance = None
    soil_moisture: float = 0
    temperature: float = 0
    humidity: float = 0

    # def __init__(self):
    #     if SensorCache.instance:
    #         return
    #     self.soil_moisture: float = 0
    #     self.temperature: int = 0
    #     self.humidity: float = 0

    # def __get__(key: str):

    # def __getattribute__(self, name):
    #     if name in attrKeys:
    #         return externalData[name]
    #     return super(Transform, self).__getattribute__(name)

    # def __setattr__(self, name, value):
    #     if name in attrKeys:
    #         externalData[name] = value
    #     else:
    #         super(Transform, self).__setattr__(name, value)

    # @classmethod
    # def __set__(cls, key: str, value: Any):
    #     cls[key] = value
