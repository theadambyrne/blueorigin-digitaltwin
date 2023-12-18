import zmq

from utils.config import ConfigParser
from utils.log import Log

config = ConfigParser()
logger = Log("DummySub")


def simple_subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(config.get("network", "reader"))
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    try:
        while True:
            message = socket.recv_string()
            if message is None:
                logger.error("No message received.")
            else:
                logger.debug(f"Received: {message}")

    except KeyboardInterrupt:
        print("Subscriber terminated.")


if __name__ == "__main__":
    simple_subscriber()
