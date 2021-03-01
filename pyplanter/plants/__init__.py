def calculate_optimal_value(value_min: float, value_max: float) -> float:
    difference = value_max - value_min
    return value_min + (difference / 2)


class BasePlant:
    # soil_moisture_min: float = 0.1
    # soil_moisture_max: float = 0.3
    # temperature_min: float = 65
    # temperature_max: float = 75
    # humidity_min: float = 80
    # humidity_max: float = 100
    # light_value: float = 0.5
    # optimal_soil_moisture = calculate_optimal_value(0.1, 0.3)
    # optimal_temperature = calculate_optimal_value(65, 75)
    # optimal_humidity = calculate_optimal_value(80, 100)

    def __init__(self, **kwargs):
        self.soil_moisture_min: float = 0.1
        self.soil_moisture_max: float = 0.3
        self.temperature_min: float = 65
        self.temperature_max: float = 75
        self.humidity_min: float = 80
        self.humidity_max: float = 100
        self.light_value: float = 0.5

        for key, value in kwargs.items():
            self.__setattr__(key, value)

        self.optimal_soil_moisture = calculate_optimal_value(
            self.soil_moisture_min, self.soil_moisture_max
        )
        self.optimal_temperature = calculate_optimal_value(
            self.temperature_min, self.temperature_max
        )
        self.optimal_humidity = calculate_optimal_value(
            self.humidity_min, self.humidity_max
        )
