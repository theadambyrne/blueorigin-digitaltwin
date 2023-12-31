import os
import datetime

from rocketpy import Environment, SolidMotor, Rocket, Flight

from utils.config import ConfigParser
from utils.log import Log
from utils.misc import suppress_print


class Simulator:
    """
    Simulates rocket flight and exports data for analysis.
    """

    def __init__(self):
        self.env = Environment(
            latitude=config.getfloat("simulation", "latitude"),
            longitude=config.getfloat("simulation", "longitude"),
            elevation=config.getint("simulation", "elevation"),
        )

        tomorrow = datetime.date.today() + datetime.timedelta(
            days=config.getint("simulation", "days_ahead")
        )
        self.env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))

        self.env.set_atmospheric_model(type="Forecast", file="GFS")

        self.env.max_expected_height = 5000

        logger.debug(
            f"Environment {self.env.latitude:1.2f}°N, {self.env.longitude:1.2f}°W, {self.env.elevation:1.2f}m"
        )

        self.motor = SolidMotor(
            thrust_source="./rocketpy_data/motors/Cesaroni_M1670.eng",
            dry_mass=1.815,
            dry_inertia=(0.125, 0.125, 0.002),
            nozzle_radius=33 / 1000,
            grain_number=5,
            grain_density=1815,
            grain_outer_radius=33 / 1000,
            grain_initial_inner_radius=15 / 1000,
            grain_initial_height=120 / 1000,
            grain_separation=5 / 1000,
            grains_center_of_mass_position=0.397,
            center_of_dry_mass_position=0.317,
            nozzle_position=0,
            burn_time=3.9,
            throat_radius=11 / 1000,
            coordinate_system_orientation="nozzle_to_combustion_chamber",
        )

        logger.debug("Motor loaded")

        self.rocket = Rocket(
            radius=127 / 2000,
            mass=14.426,
            inertia=(6.321, 6.321, 0.034),
            power_off_drag="./rocketpy_data/calisto/powerOffDragCurve.csv",
            power_on_drag="./rocketpy_data/calisto/powerOnDragCurve.csv",
            center_of_mass_without_motor=0,
            coordinate_system_orientation="tail_to_nose",
        )

        self.rail_buttons = self.rocket.set_rail_buttons(
            upper_button_position=0.0818,
            lower_button_position=-0.618,
            angular_position=45,
        )

        self.rocket.add_motor(self.motor, position=-1.255)
        logger.debug("Rocket created")

        self.nose_cone = self.rocket.add_nose(
            length=0.55829, kind="vonKarman", position=1.278
        )

        self.fin_set = self.rocket.add_trapezoidal_fins(
            n=4,
            root_chord=0.120,
            tip_chord=0.060,
            span=0.110,
            position=-1.04956,
            cant_angle=0.5,
            airfoil=("./rocketpy_data/calisto/NACA0012-radians.csv", "radians"),
        )

        self.tail = self.rocket.add_tail(
            top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
        )
        logger.debug("Aero componenets attached to rocket")

        self.main_parachute = self.rocket.add_parachute(
            "Main",
            cd_s=10.0,
            trigger=800,
            sampling_rate=105,
            lag=1.5,
            noise=(0, 8.3, 0.5),
        )

        self.drogue_parachute = self.rocket.add_parachute(
            "Drogue",
            cd_s=1.0,
            trigger="apogee",
            sampling_rate=105,
            lag=1.5,
            noise=(0, 8.3, 0.5),
        )

        logger.debug("Parachutes attached to rocket")

    def launch(self):
        logger.info("Launching...")
        self.flight = Flight(
            rocket=self.rocket,
            environment=self.env,
            rail_length=config.getfloat("simulation", "rail_length"),
            inclination=config.getint("simulation", "inclination"),
            heading=config.getint("simulation", "heading"),
        )

    def create_export_storable(self):
        if not os.path.exists("flights/"):
            os.mkdir("flights/")

        self.recorded = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

        if not os.path.exists(f"flights/{self.recorded}"):
            os.mkdir(f"flights/{self.recorded}")

    @suppress_print
    def export_data(self):
        self.create_export_storable()
        self.flight.export_data(f"flights/{self.recorded}/raw.csv")
        self.flight.export_kml(f"flights/{self.recorded}/flight.kml")


def main():
    logger.info("Initializing...")
    sim = Simulator()

    logger.info("Ready")
    sim.launch()

    logger.info("Processing data...")
    sim.export_data()
    logger.info(f"Flight recorded at flights/{sim.recorded}")

    logger.info("Exiting...")


if __name__ == "__main__":
    config = ConfigParser()
    logger = Log("Simulator")
    main()
