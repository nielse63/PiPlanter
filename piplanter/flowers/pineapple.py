from piplanter.flowers.base_flower import BaseFlower


class Pineapple(BaseFlower):
    def __init__(self):
        super().__init__(
            soil_moisture_min=0.15,
            soil_moisture_max=0.5,
            temperature_min=68,
            temperature_max=86,
            humidity_min=0.8,
            humidity_max=100,
            light_value=1,
        )
