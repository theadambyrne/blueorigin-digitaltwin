# Blue Origin Flight Data Analysis

This project is dedicated to the analysis of the Blue Origin's reusable rocket test (DDL-F1). This project is a continuous initiative for analysis and simulation of the flight data.

## Installation

```bash
git clone https://github.com/theadambyrne/blueorigin-flight.git
cd blueorigin-flight

# Create and activate conda environment
conda env create -f environment.yml
conda activate blue-origin
```

## Dataset

NASA has published data that was recorded during Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP) Game Changing Development (GCD) Program. This data was recorded during Flight 1 of the Blue Origin Deorbit, Descent, and Landing Tipping Point (BODDL-TP) Game Changing Development (GCD) Program. The flight included IMU, cameras for terrain relative navigation, and range and velocity lidar sensors. The flight was completed under NASA contract 80LARC19C0005 in October 2020.

[Dataset Card](DATASET.txt) | [Source](https://www.kaggle.com/datasets/kazushiadachi/blue-origins-reusable-rocket-test-ddlf1/data)

## Analysis

All exploration of data is done under the [notebooks](notebooks) directory.

## Simulation

Simulation will follow a microservice architecture with the following template of services:

- Reader Service: Reads the data from the dataset for processing.
- Simulator Service: Listens to reader and handles simulaton of data.
- Writer Service: Responsible for logging and entities post-op.

Everything will run via config.cfg file for selecting data and simulation parameters.