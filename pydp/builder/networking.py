class NetworkConfiguration:
    def __init__(self):
        self._settings = {}

    def set_setting(self, key, value):
        self._settings[key] = value

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in self._settings.items())


class NetworkBuilder:
    def __init__(self):
        self.network_config = NetworkConfiguration()

    def set_protocol(self, protocol):
        self.network_config.set_setting('Protocol', protocol)
        return self

    def set_port(self, port):
        self.network_config.set_setting('Port', port)
        return self

    def set_ip_address(self, ip_address):
        self.network_config.set_setting('IP Address', ip_address)
        return self

    def set_encryption(self, encryption):
        self.network_config.set_setting('Encryption', encryption)
        return self

    def build(self):
        return self.network_config


# Usage
builder = NetworkBuilder()
custom_network_config = (builder.set_protocol('TCP')
                          .set_port(8080)
                          .set_ip_address('192.168.1.1')
                          .set_encryption('AES-256')
                          .build())
print(custom_network_config)  # Outputs: Protocol: TCP, Port: 8080, IP Address: 192.168.1.1, Encryption: AES-256
