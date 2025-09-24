import os, sys, dotenv


class Settings:
    def __init__(self):
        self.conf = dotenv.find_dotenv()
        dotenv.load_dotenv(self.conf)

    def changeEntry(self, key: str, value: str):
        os.environ[key] = value
        dotenv.set_key(self.conf, key, os.environ[key])

if __name__ == '__main__':
    sys.exit(1)