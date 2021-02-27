def calculate_optimal_value(value_min: float, value_max: float) -> float:
    difference = value_max - value_min
    return value_min + (difference / 2)


class BasePlant:
    def __init__(self):
        self.soil_moisture_min: float = 0.1
        self.soil_moisture_max: float = 0.3
        self.temperature_min: float = 65
        self.temperature_max: float = 75
        self.humidity_min: float = 80
        self.humidity_max: float = 100
        self.light_value: float = 0.5

        self.optimal_soil_moisture = calculate_optimal_value(
            self.soil_moisture_min, self.soil_moisture_max
        )
        self.optimal_temperature = calculate_optimal_value(
            self.temperature_min, self.temperature_max
        )
        self.optimal_humidity = calculate_optimal_value(
            self.humidity_min, self.humidity_max
        )
