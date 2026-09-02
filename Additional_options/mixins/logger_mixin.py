from datetime import datetime


class LoggerMixin:
    def log(self, level, message):
        print(f"[{datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')}] - {level} - {self.__class__.__name__}: {message}")

# Входные данные1
class Database(LoggerMixin):
    def connect(self):
        self.log('INFO', 'Выполнено подключение к базе данных.')

    def disconnect(self):
        self.log('INFO', 'Подключение к базе данных закрыто.')

db = Database()
db.connect()
db.disconnect()
# Выходные данные1
# [06.11.2024 13:03:26] - INFO - Database: Выполнено подключение к базе данных.
# [06.11.2024 13:03:26] - INFO - Database: Подключение к базе данных закрыто.

# Входные данные2
class Order(LoggerMixin):
    def __init__(self, order_id):
        self.order_id = order_id

    def create_order(self):
        self.log('INFO', f'Заказ № {self.order_id} создан.')

    def cancel_order(self):
        self.log('WARNING', f'Заказ № {self.order_id} отменен.')

order1 = Order(9876287)
order1.create_order()

order2 = Order(4778616)
order2.create_order()
order2.cancel_order()
# Выходные данные2
# [05.11.2024 11:38:54] - INFO - Order: Заказ № 9876287 создан.
# [05.11.2024 11:38:54] - INFO - Order: Заказ № 4778616 создан.
# [05.11.2024 11:38:54] - WARNING - Order: Заказ № 4778616 отменен.