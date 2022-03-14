# Tapo P110 Energy Monitor for InfluxDB v2
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mercxry/p110-energy-monitor/ci)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/mercxry/p110-energy-monitor/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/mercxry/p110-energy-monitor)

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

## Docker

You can run the server by using this command

```sh
$ docker run -d \
    --name energy_monitor \
    -e PLUG_NAME="name_here" \
    -e TAPO_IP_ADDR="192.168.1.xxx" \
    -e TAPO_EMAIL="your@email.here" \
    -e TAPO_PASSWORD="hunter2" \
    -e INFLUXDB_V2_URL="http://192.168.1.xxx:8086" \
    -e INFLUXDB_V2_ORG="org" \
    -e INFLUXDB_V2_BUCKET="bucket" \
    -e INFLUXDB_V2_TOKEN="token" \
    mercxry/p110-energy-monitor
```

Otherwise you can check out the [example docker-compose.yml](https://github.com/mercxry/p110-energy-monitor/blob/main/docker-compose.yml) 

### Environment Variables
| Name | Purpose |
|------|---------|
| `PLUG_NAME` | Custom name to identify the plug (can be whatever you want) |
| `TAPO_IP_ADDR` | IP Address of the Tapo P110 plug |
| `TAPO_EMAIL` | Tapo Email used to login |
| `TAPO_PASSWORD` | Tapo Password used to login |
| `INFLUXDB_V2_URL` | InfluxDB v2 url, for example: `http://127.0.0.1:8086` |
| `INFLUXDB_V2_ORG` | InfluxDB v2 organization |
| `INFLUXDB_V2_BUCKET` | InfluxDB v2 bucket |
| `INFLUXDB_V2_TOKEN` | InfluxDB v2 token with read/write access to the bucket |
