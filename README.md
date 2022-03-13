# Tapo P110 Energy Monitor for InfluxDB v2

This script writes energy consumption data to InfluxDB v2, right now it only writes consumption in milliwatt (mW) every 3 seconds, but I would like to also add daily, monthly, yearly data registered by the Tapo smart plug.

### Limitations

- Supports only one smart plug
- No daily, monthly, yearly data from the smart plug (however it can be computed from InfluxDB if the script has been running for enough time)

## Development

**Requirements**
- Python 3.9
- [Poetry](https://python-poetry.org/)

**Instructions**
1. Clone the repository
2. (Optional) Create a new bucket in InfluxDB
3. Get an API Token with read and write permissions to the desired bucket from InfluxDB
4. Copy the `example.env` file to `.env`, and fill out every environment variable
5. Run the script with `poetry run python3 energy_monitor/energy_monitor.py`
