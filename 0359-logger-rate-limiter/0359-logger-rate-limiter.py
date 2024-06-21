class Logger:

    def __init__(self):
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.messages.get(message, 0):
            self.messages[message] = timestamp + 10
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)