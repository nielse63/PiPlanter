from pyplanter.plants.base_plant import BasePlant


class PineApple(BasePlant):
    def __init__(self):
        super().__init__(
            soil_moisture_min=0.25,
            soil_moisture_max=0.6,
            temperature_min=68,
            temperature_max=86,
            humidity_min=80,
            humidity_max=100,
            light_value=1.0,
        )
