class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        pass

class Request:
    def __init__(self, data):
        self.data = data

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request.data < 10:
            print("ConcreteHandlerA: Handling the request.")
        elif self.successor is not None:
            print("ConcreteHandlerA: Passing the request to the next handler.")
            self.successor.handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if 10 <= request.data < 20:
            print("ConcreteHandlerB: Handling the request.")
        elif self.successor is not None:
            print("ConcreteHandlerB: Passing the request to the next handler.")
            self.successor.handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request.data >= 20:
            print("ConcreteHandlerC: Handling the request.")
        else:
            print("ConcreteHandlerC: Request cannot be handled.")

# Build the chain of handlers
handlerA = ConcreteHandlerA()
handlerB = ConcreteHandlerB()
handlerC = ConcreteHandlerC()

handlerA.successor = handlerB
handlerB.successor = handlerC

# Create a request
request1 = Request(5)
request2 = Request(15)
request3 = Request(25)

# Process the requests through the chain of handlers
handlerA.handle_request(request1)
print("---")
handlerA.handle_request(request2)
print("---")
handlerA.handle_request(request3)
