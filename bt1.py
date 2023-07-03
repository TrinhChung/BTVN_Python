from fnc_module import checkInputScore
class Student:
    name = ""
    toan = 0
    van = 0
    anh = 0
    avg = 0.00

    def __init__(self, name, toan, van, anh):
        self.name = name
        self.toan = toan
        self.van = van
        self.anh = anh
        self.avg = round((toan + van + anh) / 3,2)
        print(self.avg)

    def __gt__(self, other):
        if(self.avg > other.avg):
            return True
        else:
            return False
        
    def showInfo(self):
        print("Name: %s, toan: %d, van: %d, anh: %d, avg %f" %(self.name,self.toan,self.van,self.anh, self.avg))


def bt1Run():
    listClass = []
    print("De ket thuc nhap dien 'done' tai ten hoc sinh");
    while True:
        name = "";
        while True:
            if (len(name)== 0 or name == None):
                name = input("Nhap ten sinh vien: ");
            else:
                break;
        if (name == "done"):
            break
        toan = checkInputScore("diem toan")
        van = checkInputScore("diem van")
        anh = checkInputScore("diem anh")
        listClass.append(Student(name, toan, van, anh))
    
    listClass.sort(reverse=True);
    print("Diem trung binh cao nhat cua lop: %d" %listClass[0].avg)
    print("Diem trung binh cua lop da sort")
    for student in listClass:
        student.showInfo();
    