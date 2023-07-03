from fnc_module import inputTime;

def bt2Run():
    print("Nhap thoi gian theo dinh dang hh:mm")
    checkIn = inputTime("den")
    checkOut = inputTime("ve")
    ot = ((checkOut.hour-checkIn.hour) + round((checkOut.minute-checkIn.minute)/60,2))
    if (ot > 4 and checkIn.hour <= 12 and checkOut.hour >= 21):
        print("OT: %f, Lunch: Y, Dinner: Y" %(ot-1))
    elif (ot > 4 and checkIn.hour <= 12 and checkOut.hour >=13):
        print("OT: %f, Lunch: Y, Dinner: N" %(ot-1))
    elif (ot > 3 and checkOut.hour >= 21):
        print(checkOut.hour)
        print(checkIn.hour)

        print("OT: %f, Lunch: N, Dinner: Y" %(ot))
    else: 
        print("OT: %f, Lunch: N, Dinner: N" %(ot))


