import socket
import threading
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import dotenv
dotenv.load_dotenv()


class DiscoveryServer:
    def __init__(self):
        pass

    def start(self):
        """
        Starts the discovery server + CLI.
        """

    def stop(self):
        """
        Stops the discovery server.
        """


if __name__ == '__main__':
    server = DiscoveryServer()
    server.start()
