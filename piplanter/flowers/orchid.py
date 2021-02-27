from piplanter.flowers.base_flower import BaseFlower


class Orchid(BaseFlower):
    def __init__(self):
        super().__init__(
            soil_moisture_min=0.1,
            soil_moisture_max=0.3,
            temperature_min=65,
            temperature_max=75,
            humidity_min=0.8,
            humidity_max=100,
            light_value=0.5,
        )
