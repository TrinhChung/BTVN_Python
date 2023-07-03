
def bt4Run():
    inputName = input("Nhap ten vao day: ")
    arrWords = inputName.split(" ");
    name = ""
    name += arrWords[len(arrWords) - 1].capitalize()
    for i in range(len(arrWords)):
        word = "";
        print(arrWords[i])
        if (i < len(arrWords) - 1 and len(arrWords[i]) > 0):
            word = (arrWords[i]).capitalize()[0];
        else: 
            word = ""
        name += word;

    print(name)
