class EventHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_event(self, event):
        pass

class ButtonClickHandler(EventHandler):
    def handle_event(self, event):
        if event == "ButtonClicked":
            print("ButtonClickHandler: Button clicked event handled.")
        elif self.next_handler is not None:
            print("ButtonClickHandler: Passing event to the next handler.")
            self.next_handler.handle_event(event)

class MouseMoveHandler(EventHandler):
    def handle_event(self, event):
        if event == "MouseMove":
            print("MouseMoveHandler: Mouse move event handled.")
        elif self.next_handler is not None:
            print("MouseMoveHandler: Passing event to the next handler.")
            self.next_handler.handle_event(event)

class KeyPressHandler(EventHandler):
    def handle_event(self, event):
        if event == "KeyPress":
            print("KeyPressHandler: Key press event handled.")
        else:
            print("KeyPressHandler: Event not handled.")

# Create a chain of event handlers
button_handler = ButtonClickHandler()
mouse_handler = MouseMoveHandler()
key_handler = KeyPressHandler()

button_handler.set_next_handler(mouse_handler)
mouse_handler.set_next_handler(key_handler)

# Simulate events
events = ["ButtonClicked", "MouseMove", "KeyPress", "UnknownEvent"]

for event in events:
    print(f"Handling event: {event}")
    button_handler.handle_event(event)
    print("---")
