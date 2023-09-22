class Logger:
    _instance = None
    """
    This class is a singleton. It can be used to log messages.
    Enuring that a single log instance is used throughout the application
    and can help maintain a consistent logging format.
    """
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_messages = []
        return cls._instance

    def log(self, message):
        self.log_messages.append(message)

    def display_logs(self):
        for log in self.log_messages:
            print(log)


# Usage
logger1 = Logger()
logger1.log('This is the first log message.')

logger2 = Logger()
logger2.log('This is the second log message.')

# Both logger1 and logger2 refer to the same instance, so the logs are combined.
logger1.display_logs()
