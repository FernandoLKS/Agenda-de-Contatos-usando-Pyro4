
#Cada contato será instanciado como um objeto
class Objeto:
    def __init__(self, FirstName, SecondName, PhoneNumber, Email, id=None):
        self.id = id
        self.FirstName = FirstName
        self.SecondName = SecondName
        self.PhoneNumber = PhoneNumber
        self.Email = Email               


def dict_to_class(classname, dicionario):
    a = Objeto(dicionario['FirstName'],dicionario['SecondName'],
               dicionario['PhoneNumber'], dicionario['Email'], dicionario['id'])
    return a


def class_to_dict(obj):
    dicionario = {
        "__class__":"objeto_agenda.Objeto",
        "id":obj.id,
        "FirstName":obj.FirstName,
        "SecondName":obj.SecondName,
        "PhoneNumber":obj.PhoneNumber,
        "Email":obj.Email,
    }
    return dicionario
