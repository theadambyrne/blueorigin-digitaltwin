import os
import time

import zmq
from zmq.utils.monitor import recv_monitor_message
import pandas as pd

from utils.config import ConfigParser
from utils.log import Log


class Reader:
    """
    Reads a CSV, parses it into a Pandas DataFrame and sends each row to a socket for a subscriber to read.
    """

    def __init__(self):
        self.cursor = 0
        self.delay = config.getfloat("data", "delay")

        self.file_path = os.path.join(
            os.path.dirname(__file__), config.get("data", "csv_file")
        )

        try:
            self.df = pd.read_csv(self.file_path)
            mb_read = self.df.memory_usage().sum() / (1024**2)
            logger.info(f"Read {mb_read:.2f}MB into memory")
        except Exception as e:
            logger.error(f"Failed to read file {e}")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(config.get("network", "reader"))

    def read_at_cursor(self):
        row = self.df.iloc[self.cursor]
        self.cursor += 1
        self.socket.send_json(row.to_dict())

    def run(self):
        for i in range(0, len(self.df)):
            self.read_at_cursor()

            if i % 1000 == 0:
                logger.debug(f"Read row {i}")

            time.sleep(self.delay / 1000)

    def __del__(self):
        self.socket.close()
        self.context.term()


def main():
    reader = Reader()

    timeout = config.getint("network", "timeout")
    end_time = time.time() + timeout
    events_socket = reader.socket.get_monitor_socket(
        events=zmq.EVENT_HANDSHAKE_SUCCEEDED
    )

    logger.info("Waiting for subscriber(s) to connect...")
    try:
        while time.time() < end_time:
            recv_monitor_message(events_socket)
            logger.info("Subscriber connected.")
            reader.run()
            break
    except KeyboardInterrupt:
        logger.info("Exiting...")
    finally:
        del reader


if __name__ == "__main__":
    config = ConfigParser()
    logger = Log("Reader")
    main()
