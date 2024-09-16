lista = []
lista_de_susg = ['Higiene', 'Pet shop','Farmácia','Beleza', 'Eletrônicos','Eletrodomésticos']

def exibir_menu():
    print('\nmenu:')
    print("1. adicionar item")
    print("2. remover item")
    print('3. exibir lista')
    print('4. limpar lista')
    print('5. Precisa de uma sugestão')
    print('6. sair')


def adicionar_item():
    item = input( "qual item deseja adicionar? ")
    lista.append (item)
    print ('Item adicionado a lista!')
    


def remover_item():
    item = input('qual item deseja remover? ')
    if item in lista:
      lista.remove(item)
      print (f'{item} removido da lista!')
    else:
     print('item não está na lista')
     


def exibir_lista():
    print (lista)


def limpar_lista():
    lista.clear()
    print ('limpeza realizada! ')


def sugestao():
    enumerate (lista_de_susg, 1)
    for i, setor in enumerate (lista_de_susg, 1):
        print('\n'f"{i}. {setor}")
    setor_esc = input('\n\nqual setor você tem interesse? escolha o número:  ')

    
    if setor_esc == '1':
        produto_esc = ('*Sabonete líquido ou em barra','*shampoo', '*condicionador'\
        , '*pasta de dente', '*escova de dentes', '*fio dental', '*desodorante',\
                '*sabonete íntimo', '*lenços umedecidos', '*álcool em gel\n')

   
    elif setor_esc == '2':
        produto_esc = ('*Ração para cães', '*Ração para gatos', '*Coleira', '*Shampoo para pets',\
 '*Brinquedos para pets', '*Comedouro', '*Cama para pets', '*Caixa de transporte',\
 '*Areia sanitária para gatos', '*Ossos e petiscos\n')

    
    elif setor_esc == '3':
        produto_esc = ('*Analgésico', '*Antisséptico', '*Curativos', '*Termômetro',\
 '*Pomada', '*Bandagem elástica', '*Vitamina C',\
 '*Antigripal', '*Protetor solar', '*Soro fisiológico\n')


    elif setor_esc == '4':
        produto_esc = ('*Base', '*Rímel', '*Batom', '*Blush', '*Corretivo', '*Delineador',\
 '*Pó compacto', '*Sombra', '*Hidratante facial', '*Protetor labial\n')
    
    
    elif setor_esc == '5':
        produto_esc = ('*Smartphone', '*Notebook', '*Tablet', '*Fone de ouvido', '*Carregador portátil',\
 '*Televisão', '*Câmera digital', '*Mouse sem fio', '*Caixa de som Bluetooth', '*Smartwatch\n')
 

    elif setor_esc == '6':
        produto_esc = ('*Geladeira', '*Micro-ondas', '*Fogão', '*Máquina de lavar roupa', '*Liquidificador',\
 '*Batedeira', '*Aspirador de pó', '*Ferro de passar', '*Torradeira', '*Ar-condicionado\n')


    for produto in produto_esc:
         print (produto)
    
    item = input( "qual item deseja adicionar? ")
    lista.append (item)
    print ('Item adicionado a lista!')
    input ('pressione ENTER para voltar ao menu')

    return (exibir_menu())
  

print ('\nOlá, bem vindo a sua lista de compra, por favor dê uma olhada no menu:')
print (exibir_menu())

while True:
    opcao = input ('escolha o numero de acordo com a opção: ')
    if opcao == '1':
        adicionar_item()
    elif opcao == '2':
        remover_item()
    elif opcao == '3':
        exibir_lista()
    elif opcao == '4':
        limpar_lista()
    elif opcao == '5':
        sugestao()
    elif opcao == '6':
        print ('saindo do programa, até breve!')
        break
    else:
        print('numero não identificado! tente novamente.')
