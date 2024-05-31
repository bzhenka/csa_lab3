from enum import Enum


# какой регистр будет использоваться для формирования адреса памяти
class AddressSelect(Enum):
    AC = 0
    SP = 1
    IP = 2
    DR = 3


# как будет изменяться указатель инструкций
class IPChange(Enum):
    INC = 0
    DR = 1


# откуда будут поступать данные в регистр данных
class DRDataSourceSelect(Enum):
    MEMORY = 1
    ALU = 2


# как будет изменяться указатель стека
class SPChange(Enum):
    INC = 0
    DEC = 1








