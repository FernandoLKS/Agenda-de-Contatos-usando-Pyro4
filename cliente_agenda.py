import Pyro4
from Pyro4.util import SerializerBase
import sys
import objeto_agenda
import os
import time

def main():
    
    #AgendaProxy = Pyro4.Proxy("PYRONAME:KLEIN_ROCHA")
    AgendaProxy = Pyro4.Proxy("PYRO:obj_470ce0a9a38b43a89c93101d5a597474@localhost:55032")
    try:
        AgendaProxy._pyroBind()
    except:
        sys.exit(-1)

    SerializerBase.register_dict_to_class("objeto_agenda.Objeto", objeto_agenda.dict_to_class)
    SerializerBase.register_class_to_dict(objeto_agenda.Objeto, objeto_agenda.class_to_dict)

    Option = None

    while Option !=  'F':         
        
        os.system('cls' if os.name=='nt' else 'clear')
        
        print("-- AGENDA DE CONTATOS --\n")
        print("Qual operação deseja fazer? ")
        print("1 - Criar novo contato")
        print("2 - Editar contato")
        print("3 - Buscar contato")
        print("4 - Ver lista de contatos")
        print("5 - Excluir contato")
        print("F - Fechar\n")

        Option = input()        
        
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        
        #Opção 1 - Adicionar um contato 
        if Option == '1':
            #Captura dos dados do contato que deseja-se adicionar
            print("\nPrimeiro nome do contato:")
            FirstName = input()            
            print("\nSegundo nome do contato:")
            SecondName = input()
            print("\nNumero de telefone:")
            PhoneNumber = input()
            print("\nEmail ('*' - omitir campo)")
            Email = input() 
            
            #envia uma solicitação ao servidor para adicionar um contato e as informações do contato
            a = objeto_agenda.Objeto(FirstName, SecondName, PhoneNumber, Email)
            b = AgendaProxy.inserir(a)      

            if b == True:                
                print("\nContato adicionado!")      
         
        #Opção 2 - Editar um contato     
        elif Option == '2':
            #captura o id do contato
            print("\nId do contato que deseja-se alterar: ")
            Id = int(input())
            
            #envia uma solicitação de alteração de um contato e seu respectivo id
            ValidID = AgendaProxy.buscar(Id)
            
            #caso sim, realiza a captura das modificações solicitadas
            if ValidID is not  None:     

                print("\nPrimeiro nome do contato: ('N' - não alterar)")
                FirstName = input()
                if FirstName != 'N':
                    ValidID.FirstName = FirstName

                print("\nSegundo nome do contato: ('N' - não alterar)")
                SecondName = input()
                if SecondName != 'N':
                    ValidID.SecondName = SecondName

                print("\nNumero de telefone: ('N' - não alterar)")
                PhoneNumber = input()
                if PhoneNumber != 'N':
                    ValidID.PhoneNumber = PhoneNumber

                print("\nEmail ('*' para omitir) ('N' - não alterar)")
                Email = input()  

                if Email != 'N':
                    ValidID.Email = Email
  

                if AgendaProxy.atualizar(ValidID) == True:
                    print("\nContato editado!")
                else:
                    print("\Erro ao editar cadastro!")
            else:
                print("\nID inexistente!") 


         #Opção 3 - Buscar Contato     
        elif Option == '3':
            #captura o id do contato
            print("\nId do contato que deseja-se buscar: ")
            Id = int(input())
            
            #retorna Objeto com o ID correspondente
            registro = AgendaProxy.buscar(Id)
            
            #caso sim, realiza a captura das modificações solicitadas
            if registro is not None:    

                print("\nBusca de Contato")
                print("--------------------------------------") 
                print("       ID:", registro.id)
                print("     Nome:", registro.FirstName, registro.SecondName )
                print(" Telefone:", registro.PhoneNumber)
                print("    Email:", registro.Email)
                print("--------------------------------------")        
                print("\nPressione 'enter' para sair")         
                input()
            
            else:
                print("\nID inexistente!") 
            
        #Opção 4 - Ver lista de contatos 
        elif Option == '4':
            
            #Recebe contato a contato para mostrar ao cliente, aguardando receber uma mensagem de fim da lista
            registros = AgendaProxy.listar_todos()   
           
            print("\nLISTA DE CONTATOS")
            print("---------------------------------------------------------------------------------")          

            if (len(registros) > 0 ):
                for registro in registros:
                    print(registro.id, '-', registro.FirstName, registro.SecondName, '-', registro.PhoneNumber, '-', registro.Email)  
            else:
                print("               NENHUM REGISTRO ENCONTRADO!")        
            print("---------------------------------------------------------------------------------")        
            print("\nPressione 'enter' para sair")         
            input()
        
        #Opção 5 - Excluir um contato                                     
        elif Option == '5':
            print("\nId do contato que deseja-se excluir: ('N' - cancelar)")
            Id = input()   
            if Id != 'N':  
                #envia uma solicitação de exclusão de um contato e seu respectivo id    
                ValidID = AgendaProxy.buscar(int(Id))
                
                #caso sim, realiza a captura das modificações solicitadas
                if ValidID is not None:  
                    if AgendaProxy.excluir(ValidID.id) == True:
                        print("\nContato excluído!") 
                    else:
                        print("\nErro ao excluir!") 
                else:
                    print("\nID inexistente!") 
            else:
                print("\nProcesso de exclusão cancelado!") 
            
        elif Option == 'F':
            print("\nLista de contatos Fechado")           
            
        else:                        
            print("\nComando inválido!")   
            

            
        time.sleep(2)    
  
if __name__ == '__main__':
    main()
