from pyplanter.sensors import SensorCache


def test_sensor_cache():
    assert SensorCache
    assert SensorCache.humidity == 0
    assert SensorCache.temperature == 0
    assert SensorCache.soil_moisture == 0
