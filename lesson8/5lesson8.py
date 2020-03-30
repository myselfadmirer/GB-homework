# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


from abc import ABC, abstractmethod


class Storage:
    __capacity = 10
    _quantity = __capacity
    storage = {
        'Printer': 0,
        'Copier': 0,
        'Scanner': 0,
    }

    def __init__(self):
        """
        Capacity of the storage
        Storage._quantity is the number of free cells
        Storage.storage is the dict
        """
        self._quantity = Storage._quantity
        self._storage = Storage.storage


class OfficeEquipment(Storage, ABC):
    def __init__(self, name: str, price: float, qty: int):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty

    @abstractmethod
    def transfer_to_storage(self):
        pass

    @abstractmethod
    def transfer_from_storage(self, num: int):
        pass


class Printer(OfficeEquipment):
    __number = 0

    def __init__(self, name, price, qty, color):
        super().__init__(name, price, qty)
        self.color = color
        self.__number = Printer.__number

    def transfer_to_storage(self):
        try:
            Storage._quantity -= self.qty
            if Storage._quantity < 0:
                raise ValueError(f'Не хватает мест на складе. Остаток мест: {Storage._quantity + self.qty}')
        except ValueError as e:
            print(e)
        else:
            Printer.__number += self.qty
            Storage.storage['Printer'] = Printer.__number

    def transfer_from_storage(self, num):
        try:
            Printer.__number -= num
            if Printer.__number < 0:
                raise ValueError(f'Не хватает техники на складе. Остаток: {Printer.__number}')
        except ValueError as e:
            print(e)
        else:
            Storage.storage['Printer'] = Printer.__number
            Storage._quantity += num


class Scanner(OfficeEquipment):
    __number = 0

    def __init__(self, name, price, qty, scan_format):
        super().__init__(name, price, qty)
        self.scan_format = scan_format
        self.__number = Scanner.__number

    def transfer_to_storage(self):
        try:
            Storage._quantity -= self.qty
            if Storage._quantity < 0:
                raise ValueError(f'Не хватает мест на складе. Остаток мест: {Storage._quantity + self.qty}')
        except ValueError as e:
            print(e)
        else:
            Scanner.__number += self.qty
            Storage.storage['Scanner'] = Scanner.__number

    def transfer_from_storage(self, num):
        try:
            Scanner.__number -= num
            if Scanner.__number < 0:
                raise ValueError(f'Не хватает техники на складе. Остаток: {Scanner.__number}')
        except ValueError as e:
            print(e)
        else:
            Storage.storage['Scanner'] = Scanner.__number
            Storage._quantity += num


class Copier(OfficeEquipment):
    __number = 0

    def __init__(self, name, price, qty, paper_size):
        super().__init__(name, price, qty)
        self.paper_size = paper_size
        self.__number = Copier.__number

    def transfer_to_storage(self):
        try:
            Storage._quantity -= self.qty
            if Storage._quantity < 0:
                raise ValueError(f'Не хватает мест на складе. Остаток мест: {Storage._quantity + self.qty}')
        except ValueError as e:
            print(e)
        else:
            Copier.__number += self.qty
            Storage.storage['Copier'] = Copier.__number

    def transfer_from_storage(self, num):
        try:
            Copier.__number -= num
            if Copier.__number < 0:
                raise ValueError(f'Не хватает техники на складе. Остаток: {Copier.__number}')
        except ValueError as e:
            print(e)
        else:
            Storage.storage['Copier'] = Copier.__number
            Storage._quantity += num


if __name__ == '__main__':
    first = Copier('Xerox', 12000.2, 6, 'A4')
    second = Scanner('Canon', 4000.0, 6, 'PDF')
    third = Printer('Konica', 10000.99, 5, color=True)

    third.transfer_to_storage()
    print(Storage.storage)
    print(Storage._quantity)
    third.transfer_from_storage(2)
    print(Storage.storage)
    print(Storage._quantity)

    second.transfer_to_storage()
    print(Storage.storage)
    print(Storage._quantity)
    second.transfer_from_storage(5)
    print(Storage.storage)
    print(Storage._quantity)

    first.transfer_to_storage()
    print(Storage.storage)
    print(Storage._quantity)
    first.transfer_from_storage(1)
    print(Storage.storage)
    print(Storage._quantity)

    # print(1)
