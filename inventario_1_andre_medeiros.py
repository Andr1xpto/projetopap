# Projeto: Gestor de Inventário
# Autor: André Medeiros
# Número: 1
# Data : 28/09/2026


SALAS = ('LAB1', 'LAB2', 'LAB3')
ESTADOS = ('operacional', 'avariado', 'em reparação')
tipos = ['computador', 'monitor', 'impressora', 'router', 'switch', 'projetor']

inventario = {
    'PC01': {
        'nome': 'desktop hp elitedesk',
        'tipo': 'computador',
        'sala': 'LAB1',
        'quantidade': 12,
        'estado': 'operacional'
    },

    'PC02': {
        'nome': 'desktop dell optiplex',
        'tipo': 'computador',
        'sala': 'LAB1',
        'quantidade': 10,
        'estado': 'operacional'
    },

    'MON01': {
        'nome': 'monitor samsung 24"',
        'tipo': 'monitor',
        'sala': 'LAB2',
        'quantidade': 8,
        'estado': 'operacional'
    },

    'IMP01': {
        'nome': 'impressora hp laserjet',
        'tipo': 'impressora',
        'sala': 'LAB2',
        'quantidade': 2,
        'estado': 'avariado'
    },

    'KB01': {
        'nome': 'teclado logitech',
        'tipo': 'periferico',
        'sala': 'LAB3',
        'quantidade': 15,
        'estado': 'operacional'
    },

    'PRJ01': {
        'nome': 'projetor epson',
        'tipo': 'projetor',
        'sala': 'LAB3',
        'quantidade': 1,
        'estado': 'avariado'
    }
}

lista_reparacao = []

#Percorre cada equipamento do iventario verifica se o estado é avariado ou em reparação para poder adicionar à lista de reparação
for equipamento in inventario:

    estado = inventario[equipamento]['estado']

    if estado == 'avariado' or estado == 'em reparação':
        lista_reparacao.append(equipamento)

reparados = []
historico = []

ativo = True

while ativo:

    #Cria o menu a partir de uma variável
    menu = "\n========= GESTOR DE INVENTÁRIO =========\n"
    menu += "1 - Listar equipamentos\n"
    menu += "2 - Adicionar equipamento\n"
    menu += "3 - Pesquisar equipamento\n"
    menu += "4 - Alterar estado de um equipamento\n"
    menu += "5 - Remover equipamento\n"
    menu += "6 - Lista de reparação\n"
    menu += "7 - Estatísticas\n"
    menu += "8 - Histórico de operações\n"
    menu += "0 - Sair\n"

    print(menu)

    escolha = input("Escolha uma opção: ")

    if escolha == '0':
        confirma = input("Tem a certeza que deseja sair?(S/N)")

        #Verifica se o utilizador inseriu s ou sim para poder parar de executar o programa
        if confirma.lower() == 's' or confirma.lower() == 'sim':
            ativo = False
            break
        else:
            continue

    elif escolha == '1':
        print("CÓDIGO | NOME | SALA | QUANTIDADE | ESTADO")

        #Percorre cada dicionário código ordena e mostra formatado como está abaixo
        for codigo in sorted(inventario):
            equipamento = inventario[codigo]

            print(
            codigo, "|",
            equipamento["nome"], "|",
            equipamento["sala"], "|",
            equipamento["quantidade"], "un. |",
            equipamento["estado"]
            )
        print("...")
        print(f"Total de registos: {len(inventario)}")

        #Verifica se o inventário está vazio
        if len(inventario) == 0:
            print("ERRO: O inventário está vazio!")
        
    elif escolha == '2':
        #Pede o código do equipamento e verifica se o código já existe no inventário e também verifica se o utilizador deixou em branco
        codigo = input("Insira o código: ").upper().strip()

        if codigo in inventario:
            print("ERRO: O código já existe, tente novamente introduzindo outro.")
        elif len(codigo) == 0:
            print("ERRO: O código deve conter algo.")


        #Pede nome e verifica se o nome estiver vazio, caso estiver repete a pergunta
        nome = input("Insira o nome do equipamento: ").lower()

        if len(nome) == 0:
            nome = input("Insira o nome do equipamento: ").lower()

        #Pede o tipo do equipamento e verifica se ele existe na lista tipos
        print(f"Tipos aceites: {tipos}")
        tipo = input("Insira o tipo do equipamento: ").lower()

        while tipo not in tipos:
            print("ERRO: O tipo inserido não existe, por favor tente novamente.")
            print(f"Tipos aceites: {tipos}")
            tipo = input("Insira o tipo do equipamento: ").lower()

        #Pede a sala, key-sensitive e verifica se a sala inserida existe na tupla SALAS
        sala = input("Insira a sala que o equipamento irá pertencer: ").upper()

        while sala not in SALAS:
            print("ERRO: A sala inserida não existe, por favor tente novamente.")
            sala = input("Insira a sala que o equipamento irá pertencer: ").upper()

        #Pede a quantidade do equipamento e verifica se a quantidade é 0 ou menor
        numero = int(input("Insira a quantidade: "))

        while numero <= 0:
            print("ERRO: A quantidade inserida é inválida, tente novamente.")
            numero = int(input("Insira a quantidade: "))

        #Adiciona o equipamento ao inventário
        inventario[codigo] = {
            'nome' : nome,
            'tipo' : tipo,
            'sala' : sala,
            'quantidade' : numero,
            'estado' : 'operacional'
        }

        historico.append(f"Equipamento de código {codigo}, nome {nome}, tipo {tipo}, destina-se à sala {sala} com quantidade de {numero}")

        print("Equipamento adicionado com sucesso!")

    elif escolha == '3':
        #Pede o código que o utilizador deseja pesquisar e pega a chave, depois percorre cada chave e valor do dicionário que o utilizador inseriu e mostra no ecrã
        codigo_r = input("Insira o código que deseja procurar: ").strip().upper()

        equipamento_r = inventario.get(codigo_r)

        if equipamento_r:
            for key, value in equipamento_r.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("ERRO: O código inserido não existe.")

    elif escolha == '4':
        codigo_es = input("Insira o código do equipamento: ").strip().upper()

        if codigo_es not in inventario:
            print("ERRO: O código não existe, tente novamente.")
            codigo_es = input("Insira o código do equipamento: ").strip().upper()

        #Pega o estado atual do equipamento
        estado_atual = inventario[codigo_es]['estado']
        print(f"Estado atual: {estado_atual}")

        #Verifica se o estado inserido pelo utilizador existe
        novo_estado = input("Insira o novo estado: ")
        while novo_estado not in ESTADOS:
            print("ERRO: Estado inserido não existe, tente novamente.")
            novo_estado = input("Insira o novo estado: ")

        if novo_estado == estado_atual:
            print("ERRO: O estado inserido é o mesmo que o anterior.")
            continue

        #Altera o estado atual para o novo estado
        inventario[codigo_es]['estado'] = novo_estado

        #Se o estado for avariado acrescenta na lista de reparações, caso contrário e o equipamento estiver na lista retira-o
        if novo_estado == 'avariado':
            if codigo_es not in lista_reparacao:
                lista_reparacao.append(codigo_es)
        else:
            if codigo_es in lista_reparacao:
                lista_reparacao.remove(codigo_es)


        historico.append(f"O estado do equipamento de código {codigo_es} foi alterado para {novo_estado}")

    elif escolha == '5':
        equipamento_rm = input("Insira o código do equipamento: ").upper().strip()

        #Verifica se o equipamento existe no iventario e pergunta se o utilizador tem a certeza que deseja remover o equipamento
        if equipamento_rm in inventario:
            confirmacao = input(f"Tem a certeza que deseja remover o equipamento {equipamento_rm} do inventário?(S/N)").lower().strip()

            if confirmacao == 's' or confirmacao == 'sim':
                inventario.pop(equipamento_rm)
        else:
            print("ERRO: O equipamento do código inserido não existe, tente novamente")
            continue


        #Faz um ciclo que para cada equipamento que for removido do iventario que ele também seja removido da lista de reparações
        while equipamento_rm in lista_reparacao:
            lista_reparacao.remove(equipamento_rm)

        historico.append(f"O equipamento de código {equipamento_rm} foi removido do inventário.")

    elif escolha == '6':

        #Verifica se a lista de reparação não está vazia
        if len(lista_reparacao) == 0:
            print("ERRO: A lista de reparações está vazia.")
            continue

        ordem = 1

        #Percorre cada equipamento da lista de reparação e mostra ordenado por números
        for equipamento in lista_reparacao:
            print(f"{ordem}. {equipamento}")
            ordem += 1

        confirma_repara = input("Deseja efetuar todas as reparações? ").lower().strip()

        #Verifica se o utilizador quer mesmo reparar todos os equipamentos
        if confirma_repara == 's' or confirma_repara == 'sim':
            while len(lista_reparacao) > 0:
                equipamento = lista_reparacao.pop(0)
                inventario[equipamento]['estado'] = 'operacional'
                reparados.append(equipamento)
                historico.append(f"O equipamento de código {equipamento} foi reparado")

        print("======LISTA DE REPARADOS======")
        print(reparados)

    elif escolha == '7':

        total = 0

        #Verifica se o iventário está vazio
        if len(inventario) == 0:
            print("ERRO: O inventário está vazio.")
            continue
        else:

            print("======ESTATÍSTICAS======")

            #Mostra a quantidade de registos
            print(f"Quantidade de registos: {len(inventario)}")

            #Pega o valor da chave quantidade de cada equipamento
            quantidade = [inventario[equipamento]['quantidade'] for equipamento in inventario]

            #Pega o valor da chave tipo de cada equipamento
            tipos_registados = [inventario[equipamento]['tipo'] for equipamento in inventario]

            #Faz a soma de todas as quantidades dos equipamentos
            total = sum(quantidade)
            
            print(f"Quantidade total de unidades: {total}")

            print(f"Menor quantidade registada: {min(quantidade)}")
            print(f"Maior quantidade registada: {max(quantidade)}")

            print(f"Tipos de equipamento registados: {sorted(set(tipos_registados))}")

            registos = {}

            #Percorre equipamento em inventario, se o estado existir em registos adiciona 1 valor ao estado se não coloca o valor de estado como 1
            for equipamento in inventario:
                estado = inventario[equipamento]['estado']
                if estado in registos:
                    registos[estado] += 1
                else:
                    registos[estado] = 1

            print(f"Número de registos por estado: {registos}")


            #Percorre sala em SALAS, percorre cada item em inventario e verifica se a o valor da chave do item é igual à variável sala, se sim guarda com a quantidade do item
            for sala in SALAS:
                total_salas = 0

                for item in inventario:
                    if inventario[item]['sala'] == sala:
                        total_salas += inventario[item]['quantidade']

                print(f"{sala}: {total_salas} unidades")


    elif escolha == '8':
        print("======HISTÓRICO DE OPERAÇÕES======")


        #Mostra as últimas 5 operações registadas no histórico
        ultimos = slice(0, 5, 1)

        print(f"Lista de Operações: {historico[ultimos]}")


        if len(historico) != 0:
            print(f"Número total de operações: {len(historico)}")
        else:
            print("ERRO: Não existe nenhuma operação registada no histórico.")

    else:
        print("ERRO: Opção inválida, por favor escolha umas das opções acima.")