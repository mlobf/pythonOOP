class Marcos:
    nome = "Marcos"
    idade = 49

    @classmethod
    def my_class_method(cls, nome, idade):
        if len(nome) < 20:
            print(f"Que dia Bizarro senhor {cls.nome}")
        else:
            print("que nome pequeno")

    def __init__(self, end):
        self.end = end

    def show_stats(self, nome, idade):
        return print(nome, idade, self.end)

    @staticmethod
    def printar(text):
        return print(text)


m = Marcos("rua um")

print(m.nome)
print(m.end)
m.my_class_method(m.nome, m.idade)

print("--------------")

m.printar("Que dia bizarro")
