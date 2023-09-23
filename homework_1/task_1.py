import subprocess


def text_in_command_output(command, text_to_find):
    try:
        output = subprocess.check_output(command, shell=True,
                                         universal_newlines=True)
        return text_to_find in output
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


command_to_execute = "ls"
text_to_search = "example.txt"
result = text_in_command_output(command_to_execute, text_to_search)
print(result)
