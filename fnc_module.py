from datetime import datetime

def checkInputScore(name):
    value  = 0;
    while True:
        try:
            value = int(input("Nhap %s : " % name));
            if (value >= 0 and value <= 10):
                break;
            else: 
                print("Nhap gia tri trong khoang 0 10!");
                continue;
        except ValueError:
            print("Gia tri %s khong hop le!" % name);
            continue;
    return value


def inputTime(name):
    value = datetime.now()
    while True:
        try:
            valueInput = input("Nhap thoi gian %s : " % name)
            value =  datetime.strptime(valueInput, "%H:%M");
            break;
        except:
            print("Vui long nhap thoi gian dung dinh dang")
            continue;
    return value;

