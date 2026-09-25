import argparse
import logging
from .application_engine import Engine

logger = logging.getLogger(__name__)


def command_execute(command):
    engine = Engine()
    if command == 'commit-message':
        print(f'Generated message: {engine.commit_message()}')

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # Armazenando os comandos possíveis
    subparsers.add_parser('commit-message')

    command = parser.parse_args().command
    command_execute(command)

if __name__ == "__main__":
    main()