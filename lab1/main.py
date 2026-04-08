#1.1
class CallReportGenerator:
    def __init__(self, calls):
        self.calls = calls

    def generate(self):
        report = "Call Report:\n"
        for call in self.calls:
            report += f"{call}\n"
        return report


class FileSaver:
    def save(self, filename, content):
        with open(filename, "w") as file:
            file.write(content)


# Використання
calls = ["Call 1 - 10 min", "Call 2 - 5 min"]

generator = CallReportGenerator(calls)
report = generator.generate()

saver = FileSaver()
saver.save("report.txt", report)

#1.2
class Subscriber:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = balance


class SMSService:
    def send(self, subscriber: Subscriber, message: str):
        print(f"Sending SMS to {subscriber.phone}: {message}")


class BalanceCalculator:
    def calculate(self, subscriber: Subscriber, charge: float):
        subscriber.balance -= charge
        return subscriber.balance


# Використання
subscriber = Subscriber("Ivan", "+380991112233", 100)

sms_service = SMSService()
sms_service.send(subscriber, "Hello!")

balance_calculator = BalanceCalculator()
new_balance = balance_calculator.calculate(subscriber, 20)

print("New balance:", new_balance)
#2.1
from abc import ABC, abstractmethod


class Tariff(ABC):
    @abstractmethod
    def calculate_cost(self, duration_minutes: float) -> float:
        pass


class BasicTariff(Tariff):
    def calculate_cost(self, duration_minutes: float) -> float:
        return duration_minutes * 1.0


# Новий тариф без зміни існуючого коду
class PremiumTariff(Tariff):
    def calculate_cost(self, duration_minutes: float) -> float:
        return duration_minutes * 0.8


class CallService:
    def __init__(self, tariff: Tariff):
        self.tariff = tariff

    def calculate_call(self, duration):
        return self.tariff.calculate_cost(duration)


# Використання
service = CallService(BasicTariff())
print(service.calculate_call(10))

service = CallService(PremiumTariff())
print(service.calculate_call(10))
#2.2
class UsageTariff(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


class VoiceTariff(UsageTariff):
    def calculate(self, minutes: float) -> float:
        return minutes * 1.0


class DataTariff(UsageTariff):
    def calculate(self, megabytes: float) -> float:
        return megabytes * 0.05


# Новий тариф — без зміни існуючих класів
class RoamingTariff(UsageTariff):
    def calculate(self, units: float) -> float:
        return units * 2.5


class BillingService:
    def __init__(self, tariff: UsageTariff):
        self.tariff = tariff

    def calculate_cost(self, usage):
        return self.tariff.calculate(usage)
#3.1
class NetworkConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class LTEConnection(NetworkConnection):
    def connect(self):
        print("Connecting via LTE")

    def disconnect(self):
        print("Disconnecting LTE")


class WiFiConnection(NetworkConnection):
    def connect(self):
        print("Connecting via WiFi")

    def disconnect(self):
        print("Disconnecting WiFi")


def start_connection(connection: NetworkConnection):
    connection.connect()
    connection.disconnect()


start_connection(LTEConnection())
start_connection(WiFiConnection())
#3.2
class DataTransmitter(ABC):
    @abstractmethod
    def transmit(self, data):
        pass


class SatelliteConnection(DataTransmitter):
    def transmit(self, data):
        print(f"Transmitting via satellite: {data}")
#4.1
class Callable(ABC):
    @abstractmethod
    def make_call(self, number): pass


class SMSable(ABC):
    @abstractmethod
    def send_sms(self, number, message): pass


class Connectable(ABC):
    @abstractmethod
    def connect_to_network(self): pass


class Smartphone(Callable, SMSable, Connectable):
    def make_call(self, number):
        print(f"Calling {number}")

    def send_sms(self, number, message):
        print(f"SMS to {number}: {message}")

    def connect_to_network(self):
        print("Connected to network")
#4.2
class DataSender(ABC):
    @abstractmethod
    def send_data(self, data): pass


class IoTDevice(DataSender, Connectable):
    def connect_to_network(self):
        print("IoT connected")

    def send_data(self, data):
        print(f"Sending data: {data}")
#5.1
class Logger(ABC):
    @abstractmethod
    def log(self, message): pass
#5.2
class FileLogger(Logger):
    def log(self, message):
        print(f"File log: {message}")


class ServerLogger(Logger):
    def log(self, message):
        print(f"Server log: {message}")


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console log: {message}")


class NetworkMonitor:
    def __init__(self, logger: Logger):
        self.logger = logger

    def monitor(self):
        self.logger.log("Network is running")


# Використання
monitor1 = NetworkMonitor(FileLogger())
monitor1.monitor()

monitor2 = NetworkMonitor(ServerLogger())
monitor2.monitor()

monitor3 = NetworkMonitor(ConsoleLogger())
monitor3.monitor()
