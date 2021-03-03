from pyplanter.plants.base_plant import BasePlant


class Orchid(BasePlant):
    def __init__(self):
        super().__init__(
            soil_moisture_min=0.1,
            soil_moisture_max=0.3,
            temperature_min=65,
            temperature_max=75,
            humidity_min=80,
            humidity_max=100,
            light_value=0.5,
        )
