from gpiozero import MCP3008
from piplanter.sensors import BaseSensor


class SoilMoistureSensor(BaseSensor):
    def __init__(
        self,
        channel: int = 0,
        clock_pin: int = 11,
        mosi_pin: int = 10,
        miso_pin: int = 9,
        select_pin: int = 8,
    ):
        super().__init__()
        self.channel = channel
        self.clock_pin = clock_pin
        self.mosi_pin = mosi_pin
        self.miso_pin = miso_pin
        self.select_pin = select_pin

        # save the sensor object on the class
        self.sensor = MCP3008(
            channel=self.channel,
            clock_pin=self.clock_pin,
            mosi_pin=self.mosi_pin,
            miso_pin=self.miso_pin,
            select_pin=self.select_pin,
        )

    @property
    def value(self) -> float:
        return self.sensor.value

    @property
    def voltage(self) -> float:
        return self.sensor.voltage
