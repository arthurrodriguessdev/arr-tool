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

    def generated_uuid(self):
        return uuid.uuid4()
    
    def socket_verify(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        return result

    def run(self, capture_output=True):
        self.result_command = subprocess.run(
            self.arguments_list, 
            capture_output=capture_output, 
            text=True
        )
        