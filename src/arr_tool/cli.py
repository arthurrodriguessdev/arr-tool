import subprocess as s
import logging

logger = logging.getLogger(__name__)

def command_execute(*args):
    logger.info(f"Iniciando o comando: [{args}]")
    return s.run(args)


def main():
    command_execute("hostname", "-I")

if __name__ == "__main__":
    main()