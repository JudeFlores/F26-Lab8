#To test the cash register class
from cashregister import CashRegister
#adds 3 items, undos 2 items, adds 1 item, undos 1 item, adds 1 item, clears
def main():
    reg = CashRegister()
    reg.addItem(5)
    print(reg.getTotal())
    print(reg.getCount())

    reg.addItem(6)
    print(reg.getTotal())
    print(reg.getCount())

    reg.addItem(9)
    print(reg.getTotal())
    print(reg.getCount())

    reg.undo()
    print(reg.getTotal())
    print(reg.getCount())

    reg.undo()
    print(reg.getTotal())
    print(reg.getCount())

    reg.addItem(10)
    print(reg.getTotal())
    print(reg.getCount())

    reg.undo()
    print(reg.getTotal())
    print(reg.getCount())

    reg.addItem(7)
    print(reg.getTotal())
    print(reg.getCount())

    reg.clear()
    print(reg.getTotal())
    print(reg.getCount())

if __name__ == "__main__":
    main()