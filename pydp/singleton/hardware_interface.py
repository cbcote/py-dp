class MockHardwareInterface:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MockHardwareInterface, cls).__new__(cls)
            cls._instance._status = 'Disconnected'
        return cls._instance

    def connect(self):
        if self._status == 'Disconnected':
            print('Connecting to hardware...')
            self._status = 'Connected'
            print('Connected to hardware!')
        else:
            print('Already connected to hardware!')

    def disconnect(self):
        if self._status == 'Connected':
            print('Disconnecting from hardware...')
            self._status = 'Disconnected'
            print('Disconnected from hardware!')
        else:
            print('Already disconnected from hardware!')


# Usage
interface1 = MockHardwareInterface()
interface1.connect()

interface2 = MockHardwareInterface()
interface2.connect()  # Will print 'Already connected to hardware!'

# Both interface1 and interface2 refer to the same instance.
interface1.disconnect()
