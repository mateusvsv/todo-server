class Tarefa(object):

    def __init__(self,id, titulo, usuario, completo=False):
        self.id = id
        self.titulo = titulo
        self.completo = completo
        self.usuario = usuario
