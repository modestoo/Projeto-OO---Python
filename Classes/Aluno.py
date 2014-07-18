class Aluno:
    "Classe que representa os alunos da escola"

    __matricula_ = 0
    __nome_ = ""
    __dataNascimento_ = ""
    __endereco_ = ""
    __email_ = ""
    __serie_ = ""
    quantidadeAlunosMatriculados = 0

    def __init__(self, matricula, nome, endereco):
        self.matricula = matricula
        self.nome = nome
        self.endereco = endereco

    def matricularAluno(self, matricula, nome,
                        dataNascimento, endereco, email, serie):
        self.matricula = matricula
        self.nome = nome
        self.dataNascimento
        self.endereco = endereco
        self.email = email
        self.serie = serie
        quantidadeAlunosMatriculados += 1
        


        
