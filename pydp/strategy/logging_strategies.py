import datetime


class LoggingStrategy:
    def log(self, message: str) -> None:
        pass


# Implement concrete strategies
class ConsoleLogging(LoggingStrategy):
    def log(self, message: str) -> None:
        print(f'[Console] {datetime.datetime.now()}: {message}')


class FileLogging(LoggingStrategy):
    def log(self, message: str) -> None:
        with open('log.txt', 'a') as file:
            file.write(f'[File] {datetime.datetime.now()}: {message}\n')


class DatabaseLogging(LoggingStrategy):
    def log(self, message: str) -> None:
        # This is a mock implementation. In a real-world scenario, you'd log the message to a database.
        print(f'[Database] {datetime.datetime.now()}: {message}')


# Context class
class Logger:
    def __init__(self, strategy: LoggingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: LoggingStrategy):
        self._strategy = strategy

    def execute_logging(self, message: str) -> None:
        self._strategy.log(message)


# Usage
message = 'This is a log message.'

# Using ConsoleLogging
logger = Logger(ConsoleLogging())
logger.execute_logging(message)

# Switching to FileLogging
logger.set_strategy(FileLogging())
logger.execute_logging(message)

# Switching to DatabaseLogging
logger.set_strategy(DatabaseLogging())
logger.execute_logging(message)
