from enum import IntEnum
from datetime import datetime

class LogLevel(IntEnum):
    TRACE = 4
    INFO = 3,
    WARN = 2,
    ERROR = 1,
    FATAL = 0

class Log:
    def __init__(self, name, log_level, filepath=""):
        self.name = name
        self.log_level = log_level

        self.filepath = filepath
    
    def trace(self, message):
        if self.log_level < LogLevel.TRACE:
            return

        processed_message = self.process_message("trace", message)

        self.handle_message(processed_message)

    def info(self, message):
        if self.log_level < LogLevel.INFO:
            return

        processed_message = self.process_message("info", message)

        self.handle_message(processed_message)

    def warn(self, message):
        if self.log_level < LogLevel.WARN:
            return

        processed_message = self.process_message("warn", message)

        self.handle_message(processed_message)

    def error(self, message):
        if self.log_level < LogLevel.ERROR:
            return

        processed_message = self.process_message("error", message)

        self.handle_message(processed_message)

    def fatal(self, message):
        if self.log_level < LogLevel.FATAL:
            return

        processed_message = self.process_message("fatal", message)

        self.handle_message(processed_message)

    def process_message(self, level, message):
        return "[{}]({}) {}: {}".format(self.name, self.get_timestamp(), level, message)
    
    def handle_message(self, message):
        if self.filepath != "":
            with open(self.filepath, "a") as f:
                f.write(message + "\n")
        else:
            print(message)

    def get_timestamp(self):
        time = datetime.now()
        return str(time.date()) + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
