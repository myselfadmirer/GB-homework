# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.


class Storage:
    __capacity = 10
    _quantity = __capacity

    def __init__(self):
        """
        Capacity of the storage
        """
        self.__capacity = Storage._quantity


class OfficeEquipment(Storage):
    def __init__(self, name: str, price: float, qty: int):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        try:
            Storage._quantity -= self.qty
            if Storage._quantity < 0:
                raise ValueError(f'Не хватает мест на складе. Остаток мест: {Storage._quantity + self.qty}')
        except ValueError as e:
            print(e)


class Printer(OfficeEquipment):
    def __init__(self, name, price, qty, color):
        super().__init__(name, price, qty)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, price, qty, scan_format):
        super().__init__(name, price, qty)
        self.scan_format = scan_format


class Copier(OfficeEquipment):
    def __init__(self, name, price, qty, paper_size):
        super().__init__(name, price, qty)
        self.paper_size = paper_size


if __name__ == '__main__':
    first = Copier('Xerox', 12000.2, 5, 'A4')
    second = Scanner('Canon', 4000.0, 6, 'PDF')

    print(1)
