from pip import main


def fibbo (n):
    num0 = 0
    num1 = 1
    for i in range (n):
        
        yield num0
        num0, num1 = num1, num0 + num1


if __name__ == '__main__':
    f = fibbo(10)
    for i in f:
        print (f" {i}", end="")