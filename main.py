from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

traco = '---------------------------------'

p1 = Pessoa(1, "Arthur", "Rua Dario Gonlaves Molho, 846")
p1.printName()
print(traco)

f1 = Fisica(2, "Katarina", "Rua 1", "blabla", "111.111.111-11", 5, 85.2, 1.78)
f1.imprimeCPF()
print(traco)

j1 = Juridica(3, "Atma", "Rua 2", "bleble", "222.222.222-0002/22", "2222222", 150)
j1.imprimeCNPJ()


