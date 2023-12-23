# Blue Origin Flight: Digital Twin

![Blue Origin Rocket](https://wonderfulengineering.com/wp-content/uploads/2017/12/blue-origin-610x343.jpg)

This project is dedicated to the analysis of the Blue Origin's reusable rocket test (DDL-F1) and a continuous initiative for analysis and simulation of the flight data.  The objective is to create a digital twin of the rocket.

## Installation

```bash
git clone https://github.com/theadambyrne/blueorigin-digitaltwin.git
cd blueorigin-digitaltwin

# Create and activate conda environment
conda env create -f environment.yml
conda activate bofdt

# Run services (see Architecture for more details)
python services/Reader.py 
python services/DummySub.py # In a separate terminal
```

## Analysis

All exploration of data is done under the [/notebooks](notebooks) directory and serves as a playground for analysis and validation for Proof of Concepts (POC).

## Architecture

Simulation follows a Publish-Subscribe pattern under a Microservice architecture via `0MQ`. The following services are available:

| Service | Type | Handles | Description | Status |
| --- | --- | --- | --- | --- |
| [Reader](services/Reader.py) | Publisher | Data | Reads CSV source into dataframe and sends it to a subscriber | :white_check_mark: |
| [DummySub](services/DummySub.py) | Subscriber | Validation | Validation for publishers, this script is for debugging purposes only | :white_check_mark: |
| [Simulator](services/Simulator.py) | Subscriber | Flight Simulation | Simulates configurable flight | :white_check_mark: |

| Module | Description | Status |
| --- | --- | --- |
| [ConfigParser](utils/ConfigParser.py) | Parses configuration file | :white_check_mark: |
| [Log](utils/Log.py) | Logging utility | :white_check_mark: |
| [Injector](utils/Injector.py) | Inject data into simulation | :x: |

Everything will run via config.cfg file for selecting data and simulation parameters.

**Note:** Utilities such as `ConfigParser` and `Log` employ the Singleton pattern to ensure that only one instance of the class is created and allows cross-module access to the configuration and logging without damaging the integrity of the data.

## Configuration

This entire project is configured via a single configuration file `config.cfg`. A huge help when working with sockets, data, and logging.

```ini
# config.cfg

[data]
csv_file = ../dataset/Data/dlc.csv
delay = 0.1 

[simulation]
latitude = 32.990254
longitude = -106.974998
elevation = 1400
days_ahead = 1

rail_length = 5.2
inclination = 85
heading = 0

[logging]
active = true
log_file = spam.log

[network]
reader = tcp://127.0.0.1:5555
timeout = 20
```

## Simulation Data

For rocket simulation we need the RocketPy data for engines, stages, and rocket. This can be submoduled but for now is to be downloaded manually.
Can be found at the official GitHub repo: [RocketPy](https://github.com/RocketPy-Team/RocketPy)


## Dataset

NASA has published data that was recorded during Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP) Game Changing Development (GCD) Program. This data was recorded during Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP) Game Changing Development (GCD) Program. The flight included IMU, cameras for terrain relative navigation, and range and velocity lidar sensors. The flight was completed under NASA contract 80LARC19C0005 in October 2020.

[Dataset Card](DATASET.txt) | [Source](https://www.kaggle.com/datasets/kazushiadachi/blue-origins-reusable-rocket-test-ddlf1/data)