import socket
import subprocess
import uuid
from .ai import ModelAI
from .prompts import Prompts


class Engine:
    def commit_message(self):
        result_command = self.run(["git", "diff"])

        result = result_command.stdout
        if not result:
            return 'The command "git diff" did not detect any changes'

        prompt = Prompts.PROMPT_COMMIT_MESSAGE.format(git_diff_result=result)
        return ModelAI().generate_output(prompt)

    def generate_uuid(self):
        return uuid.uuid4()

    def socket_verify(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        return result != 0

    def generate_env_example(self):
        try:
            env_model = open('.env', 'r')
            new_content = ''

            while True:
                line = env_model.readline()
                if line == '':
                    break

                get_content = False
                for sub in line:
                    str_list = ['=', '#', '" "', '\n']
                    if sub in str_list:
                        break

                    new_content += sub
                    get_content = True

                if get_content:
                    new_content += '=\n'

            new_file = open('.env.example', 'w')
            new_content = new_content.strip('\n')
            new_file.write(new_content)
            env_model.close()
            new_file.close()
            return True

        except:
            raise RuntimeError('Your .env file was not found')

    def run(self, arguments, capture_output=True):
        return subprocess.run(
            arguments, 
            capture_output=capture_output, 
            text=True
        )     