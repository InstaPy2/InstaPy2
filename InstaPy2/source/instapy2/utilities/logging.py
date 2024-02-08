class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Logging:
    def __init__(self):
        pass

    def error(self, string: str):
        print(f"[{bcolors.FAIL + 'ERROR' + bcolors.ENDC}]: {string}")

    def info(self, string: str):
        print(f"[{bcolors.OKBLUE + 'INFO' + bcolors.ENDC}]: {string}")

    def success(self, string: str):
        print(f"[{bcolors.OKGREEN + 'SUCCESS' + bcolors.ENDC}]: {string}")
