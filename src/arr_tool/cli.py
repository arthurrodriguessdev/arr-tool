import argparse
import logging
from .application_engine import Engine

logger = logging.getLogger(__name__)


def command_execute(command):
    engine = Engine()
    command_request = command.command
    message_return = ''

    if command_request == 'commit-message':
        message_return = f'Generated message: {engine.commit_message()}'

    elif command_request == 'uuid':
        message_return = f'Generated UUID: {engine.generate_uuid()}'

    elif command_request == 'verify-port':
        port = command.port
        if engine.socket_verify(port):
            status = 'AVAILABLE'
        else:
            status = 'NO AVAILABLE'
        message_return = f'The status port is: {status}'

    elif command_request == 'env-example':
        engine.generate_env_example()
        message_return = 'Your file was generated successfully'

    print(message_return)

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # Defining the available commands
    subparsers.add_parser('commit-message')
    subparsers.add_parser('uuid')
    subparsers.add_parser('env-example')

    verify_port = subparsers.add_parser('verify-port')
    verify_port.add_argument('port', type=int)

    command = parser.parse_args()
    command_execute(command)

if __name__ == "__main__":
    main()