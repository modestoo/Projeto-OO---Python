class Aluno(Imprimivel):
    "Classe que representa os alunos da escola"

    ###### Atributos de instância e classe
    
    __matricula = None
    __nome = None
    __dataNascimento = None
    __endereco = None
    __email = None
    __serie = None
    quantidadeAlunosMatriculados = 0


    ###### (Des)Contrutores e Métodos de Negócio
    
    def __init__(self):
        print ("MATRÍCULA DO ALUNO - Entre com as informações a seguir")
        matricula = int(input("Matrícula do aluno (6 número):"))#Adicionar restrição de 6 letras com a função len (length)
        nome = input("Nome do aluno:")
        dataNascimento = input("Data de Nascimento do aluno(__/__/____):")
        endereco = input("Endereco do aluno:")
        email = input("Email do aluno:")
        serie = input("Serie do aluno (_ª Ano):")
        self.matricularAluno(matricula, nome,
                             dataNascimento, endereco, email, serie)

    def __del__(self):
        Aluno.quantidadeAlunosMatriculados -= 1

    def matricularAluno(self, matricula, nome,
                        dataNascimento, endereco, email, serie):
        self.__matricula = matricula
        self.__nome = nome
        self.__dataNascimento
        self.__endereco = endereco
        self.__email = email
        self.__serie = serie
        Aluno.quantidadeAlunosMatriculados += 1

    
            
    ###### Acessores e Modificadores
        
    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getDataNascimento(self):
        return self.__dataNascimento

    def setDataNascimento(self, DN):
        self.__dataNascimentoa = DN

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self._email = email

    def getSerie(self):
        return self.__serie

    def setSerie(self, serie):
        self._serie = serie

