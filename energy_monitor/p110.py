import os

from PyP100 import PyP110


class TapoP110:
    def __init__(self):
        # Get auth details from env vars
        self.ip_addr = os.getenv("TAPO_IP_ADDR")
        self.email = os.getenv("TAPO_EMAIL")
        self.password = os.getenv("TAPO_PASSWORD")

        # Login to Tapo
        self.p110 = PyP110.P110(self.ip_addr, self.email, self.password)
        self.p110.handshake()
        self.p110.login()

    def get_energy_usage(self):
        return self.p110.getEnergyUsage()

    def get_current_power(self):
        return self.get_energy_usage()["result"]["current_power"]
