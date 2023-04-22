import Pyro4
from Pyro4.util import SerializerBase
import objeto_agenda


@Pyro4.expose
class AgendaServidor:

    def __init__(self):
        self.contador_id = 0
        self.agenda = []

    def inserir(self, objeto:objeto_agenda.Objeto):
        objeto.id = self.contador_id
        self.contador_id += 1
        self.agenda.append(objeto)
        return True
    
    def atualizar(self, dados):
        for i, cadastro in enumerate(self.agenda):
            if (cadastro.id == dados.id):
                self.agenda[i] = dados
                return True
        return False
    
    def buscar(self, id):
        for objeto in self.agenda:
            if (objeto.id == id):
                return objeto
        return None
    
    def listar_todos(self):
        return self.agenda
    
    def excluir(self, id):
        for i, cadastro in enumerate(self.agenda):
            if (cadastro.id == id):
                self.agenda.pop(i)
                return True
        return False

            
def main():

    daemon = Pyro4.Daemon()    
    uri = daemon.register(AgendaServidor)
    print("URI do objeto: ", uri)
    #ns = Pyro4.locateNS()
    #ns.register("KLEIN_ROCHA", uri)

    SerializerBase.register_dict_to_class("objeto_agenda.Objeto", objeto_agenda.dict_to_class)
    SerializerBase.register_class_to_dict(objeto_agenda.Objeto, objeto_agenda.class_to_dict)

    daemon.requestLoop()

if __name__ == '__main__':
    main()
