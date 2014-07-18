class Imprimivel:
    "Interface para tornar o OBJETO imprimível"

    ###### Métodos
    
    def __str__(self):
        "método (especial) chamado por print, str()..."
        conteudo = ''
        for interador in self.__dict__.keys(): #outro método especial!
            conteudo += '%s: %s\n' % (interador, str(self.__dict__[interador]))
        return conteudo

