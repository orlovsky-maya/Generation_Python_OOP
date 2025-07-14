class IPAddress:
    def __init__(self, ip_address: str | tuple | list):
        if isinstance(ip_address, tuple | list):
            self.ip_address = '.'.join(str(i) for i in ip_address)
        elif isinstance(ip_address, str):
            self.ip_address = ip_address

    def __str__(self):
        return self.ip_address

    def __repr__(self):
        return f"IPAddress('{self.ip_address}')"

ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))


ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))