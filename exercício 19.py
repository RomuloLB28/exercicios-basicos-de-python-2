#escreva um programa que recomende um filme de forma pseudo aleatória

from random import randint

filmes = {"1":"O poderoso chefão","2":"O poderoso chefão 2","3":"Cidade de Deus","4":"Tropa de elite","5":"Tropa de elite 2","6":"Enigma de Outro Mundo","7":"Batman Begins","8":"The dark knight","9":"The dark knight rises","10":"Joker","11":"Todo mundo quase morto","12":"O jovem Frankenstein","13":"This is spinal tap","14":"What we do in the shadow","15":"Heróis fora de órbita","16":"Monty Python and the holy grail","17":"Apertem os cintos - o piloto sumiu","18":"Mad Max - estrada de fúria","19":"Brilho eterno de uma mente sem lembranças","20":"Clube da luta","21":"Pulp fiction","22":"Once upon a time in hollyhood","23":"Bastardos inglórios","24":"Django Livre","25":"Kill Bill","26":"Os oitos odiados","27":"A origem","28":"Halloween","29":"Interestelar","30":"Predador","31":"Allien","32":"Psicose","33":"Harry Potter e a pedra filosofal","34":"Blade runner","35":"Jogos Vorazes","36":"Harry Potter e a câmara secreta","37":"Harry Potter e o cálice de fogo","38":"Harry Potter e a ordem da fenix","39":"Harry Potter e o enigma do princepe","40":"Harry Potter e as reliquias da morte parte 1","41":"Harry Potter e as reliquias da morte parte 2","42":"Harry Potter e o prisioneiro de Azkaban"}

escolha = str(randint(1,43))
if escolha in filmes.keys():
    print(filmes[escolha])
