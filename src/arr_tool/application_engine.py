import subprocess
import uuid
import socket
from .ai import ModelAI
from .prompts import Prompts


class Engine:
    def __init__(self):
        self.arguments_list = []
        self.result_command = None

    def commit_message(self):
        ai_model = ModelAI()
        self.arguments_list.extend(["git", "diff"])
        self.run()

        result = self.result_command.stdout
        if not result:
            return 'The command "git diff" did not detect any changes'
        
        prompt = Prompts.PROMPT_COMMIT_MESSAGE.format(git_diff_result=result)
        commit_message_response = ai_model.generate_output(prompt)
        return commit_message_response

    def generate_uuid(self):
        return uuid.uuid4()
    
    def socket_verify(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        return result

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

    def run(self, capture_output=True):
        self.result_command = subprocess.run(
            self.arguments_list, 
            capture_output=capture_output, 
            text=True
        )     