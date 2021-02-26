from piplanter.flowers.base_flower import BaseFlower


class Orchid(BaseFlower):
    soil_moisture_min = 0.1
    soil_moisture_max = 0.3
    humidity_min = 0.8
    humidity_max = 100
    light_value = 0.5

    @property
    def temperature_min():
        # TODO: if light is on, min temp is 80
        return 65

    @property
    def temperature_max():
        # TODO: if light is on, max temp is 85
        return 75
