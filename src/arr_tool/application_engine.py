import subprocess
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

        prompt = Prompts.PROMPT_COMMIT_MESSAGE.format(git_diff_result=self.result_command.stdout)
        commit_message_response = ai_model.generate_output(prompt)
        return commit_message_response

    def run(self, capture_output=True):
        self.result_command = subprocess.run(
            self.arguments_list, 
            capture_output=capture_output, 
            text=True
        )
        