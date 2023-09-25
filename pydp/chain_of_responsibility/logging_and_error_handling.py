class Logger:
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log_message(self, message, level):
        if self.level <= level:
            self.write(message)

        if self.next_logger is not None:
            self.next_logger.log_message(message, level)

    def write(self, message):
        pass

class ConsoleLogger(Logger):
    def write(self, message):
        print(f"Console Logger: {message}")

class FileLogger(Logger):
    def __init__(self, level, filename):
        super().__init__(level)
        self.filename = filename

    def write(self, message):
        with open(self.filename, "a") as file:
            file.write(f"File Logger: {message}\n")

class ErrorLogger(Logger):
    def write(self, message):
        print(f"Error Logger: {message}")

# Create a chain of loggers
console_logger = ConsoleLogger(Logger.INFO)
file_logger = FileLogger(Logger.DEBUG, "log.txt")
error_logger = ErrorLogger(Logger.ERROR)

console_logger.set_next_logger(file_logger)
file_logger.set_next_logger(error_logger)

# Log messages with different levels
console_logger.log_message("This is an informational message.", Logger.INFO)
console_logger.log_message("This is a debug message.", Logger.DEBUG)
console_logger.log_message("This is an error message.", Logger.ERROR)
