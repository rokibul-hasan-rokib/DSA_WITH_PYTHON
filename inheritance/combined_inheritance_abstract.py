from abc import ABC, abstractmethod
class Logger(ABC):
    @abstractmethod
    def log(self, msg: str):
        pass

class FileLogger(Logger):
    def log(self, msg: str):
        with open("log.txt", "a") as f:
            f.write(msg + "\n")

class ConsoleLogger(Logger):
    def log(self, msg: str):
        print(msg)

def save(data, logger: Logger):
    logger.log(f"Saving data: {data}")

save("test", ConsoleLogger()) 
