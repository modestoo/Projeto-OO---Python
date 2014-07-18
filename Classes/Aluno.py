class Aluno:
    "Classe que representa os alunos da escola"

    __matricula = None
    __nome = None
    __dataNascimento = None
    __endereco = None
    __email = None
    __serie = None
    quantidadeAlunosMatriculados = 0

    def __init__(self, matricula, nome, endereco):
        self.__matricula = matricula
        self.__nome = nome
        self.__endereco = endereco

    def matricularAluno(self, matricula, nome,
                        dataNascimento, endereco, email, serie):
        self.__matricula = matricula
        self.__nome = nome
        self.__dataNascimento
        self.__endereco = endereco
        self.__email = email
        self.__serie = serie
        quantidadeAlunosMatriculados += 1
        


        
