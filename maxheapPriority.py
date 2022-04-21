import os

class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def inserir(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def pegar(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def mostrar(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: 
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        esquerda = index * 2
        direita = index * 2 + 1
        maior = index
        if len(self.heap) > esquerda and self.heap[maior] < self.heap[esquerda]:
            maior = esquerda
        if len(self.heap) > direita and self.heap[maior] < self.heap[direita]:
            maior = direita

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Paciente:
    def __init__(self):
        os.system("cls")
        self.listaPacientes = []
        self.prioridade = ()
        self.dadosPaciente = ()
        self.contador = 999
        self.max_heap = MaxHeap()
        self.lista = []
        self.pacientesChamados = []
   
    def _adicionarPaciente(self, prioridade, nomeCompleto, tipoSanguineo, dataNascimento):
        self.prioridade = prioridade
        self.dadosPaciente = self.prioridade, self.contador, nomeCompleto, tipoSanguineo, dataNascimento
        self.listaPacientes.append(self.dadosPaciente)
        self.max_heap.inserir(self.prioridade)
        self.contador -= 1
        print("\nPaciente foi colocado no sistema com sucesso!\n\n")

    def _mostrarProximoPaciente(self):
        if not self.listaPacientes:
            print("Não há nenhum outro Paciente!")
        else:
            i = 0
            self.elemento = self.max_heap.pegar()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.listaPacientes[i][0] == self.lista[0]:
                        print(f"Próximo paciente: {self.listaPacientes[i]}")
                        break  
                elif len(self.listaPacientes) == 1:
                        print(self.listaPacientes[0])
                        break
                else:
                        i += 1

    def _proxConsulta(self):
        if not self.listaPacientes:
            print("Não há pacientes a serem chamados")
        else:
            i = 0
            self.elemento = self.max_heap.pegar()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.listaPacientes[i][0] == self.lista[0]:
                    print(f"O paciente foi convocado: {self.listaPacientes[i]}")
                    self.pacientesChamados.append(self.listaPacientes[i])
                    self.lista.pop(0)
                    self.listaPacientes[i], self.listaPacientes[0] = self.listaPacientes[0], self.listaPacientes[i]
                    self.listaPacientes.pop(0)
                    break
                else:
                        i += 1
        
    def _mostrar5Pacientes(self):
        if len(self.listaPacientes) < 5:
            print(f"Últimos Pacientes Chamados: {self.pacientesChamados}")
        else:
            print(f"Últimos 5 Pacientes Chamados: {self.pacientesChamados[-5]}")

p = Paciente()

while True:    
    print("""1- Acrescentar mais um paciente
2- Encaminhar a proxima consulta
3- Indicar qual será o proximo a ser atendido
4- Mostre a lista dos cinco ultimos pacientes
5- Sair do sistema""")

    escolha = int(input("\n \nOlá, em que podemos ajudar? "))
    os.system("cls")

    if escolha == 1:
        nomeCompleto = str(input("\nPor favor, informe o nome completo do paciente: "))
        
        prioridade = int(input("Qual o grau de urgencia para o atendimento?\n(1 = menor e 10 maior): ")) 
        while prioridade < 1 or prioridade > 10:
            print("Perdão porém a prioridade colocada não está compactuando com o sistema!")
            prioridade = int(input("\nRecoloque a prioridade: "))
        
        tipoSanguineo = str(input("Insira o tipo sanguíneo do paciente: ")) 
        dataNascimento = str(input("Redija a data de nascimento do paciente aqui: "))
        p._adicionarPaciente(prioridade, nomeCompleto, tipoSanguineo, dataNascimento)
    elif escolha == 2:
        p._mostrarProximoPaciente()
    elif escolha == 3:
        p._proxConsulta()
    elif escolha == 4:
        p._mostrar5Pacientes()
    elif escolha == 5:
        break
    else:
        print("Opção inválida!")