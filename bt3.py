from fnc_module import inputDate
from datetime import datetime

def bt3Run():
    dateJoin = inputDate("vao cong ty");
    dateNow = datetime.now();
    holidays = 0.00;
    if (dateJoin.year < dateNow.year):
        if (dateNow.year - dateJoin > 5):
            holidays = 14;
        elif (dateNow.year - dateJoin.year > 4):
            holidays = 13;
        else: 
            holidays = 12;
    else:
        holidays = 12- dateJoin.month;
        if (dateJoin.day < 10):
            holidays += 1;
        else:
            holidays += 0.5;

    print("Ngày vào làm: %s,   :  Số ngày nghỉ phép: %f" %(dateJoin.strftime("%d/%m/%Y"),holidays))


