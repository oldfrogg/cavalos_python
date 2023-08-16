import random
soma_vel = 0
odd = []
lista_pontuacao=[]
margem_banca = 0.88
index = 0
saldo = 100.00
flag_confirma_aposta = True


class Cavalo:
    def __init__(self, nome, velocidade):
        self.__nome = nome
        self.__velocidade = velocidade
        self.odd = 0.0

    def nome(self):
        return self.__nome

    def velocidade(self):
        return self.__velocidade


cavalos = (
    Cavalo("Musky Huel", 53),
    Cavalo("Azarado", 51),
    Cavalo("Monkee", 73),
    Cavalo("FDP", 97),
    Cavalo("Garanhão", 61),
    Cavalo("Egipcio", 64),
    Cavalo("Herói", 66),
    Cavalo("Copenhagen", 93),
    Cavalo("Marengo", 69),
    Cavalo("Pégaso", 72),
    Cavalo("Napoleão", 75),
    Cavalo("Zeus", 79),
    Cavalo("Perseu", 81),
    Cavalo("Hércules", 84),
    Cavalo("Pupilo", 87),
    Cavalo("Pé de Pano", 90)
)

def aposta():

    global saldo, flag_confirma_aposta, cavalos_pareo, index, odd, lista_pontuacao, soma_vel

    cavalos_pareo = random.sample(cavalos,6)
    for cavalo in cavalos_pareo:
        soma_vel = soma_vel + cavalo.velocidade()
    
    for cavalo in cavalos_pareo:
        sprint1 = cavalo.velocidade()+(random.random()*200)
        sprint2 = cavalo.velocidade()+(random.random()*200)
        sprint3 = cavalo.velocidade()+(random.random()*200)
        sprint4 = cavalo.velocidade()+(random.random()*200)
        pontuacao_corrida = sprint1+sprint2+sprint3+sprint4
        
        cavalo.odd=margem_banca*1/(cavalo.velocidade()/soma_vel)
        print(f"{index+1} - {cavalo.nome()} odd:{cavalo.odd}")
        lista_pontuacao.append(pontuacao_corrida)
        odd.append(cavalo.odd)
        index+=1
    
    
    index_vencedor = lista_pontuacao.index(max(lista_pontuacao))
    cavalo_vencedor = cavalos_pareo[index_vencedor].nome().upper()
    
    print(f"\nSeu saldo: R${saldo}\n")
    index_cavalo_escolhido = int(input("\nEscolha o número do seu cavalo\n"))-1
    cavalo_escolhido = cavalos_pareo[index_cavalo_escolhido].nome()
    valor_aposta = int(input("Insira o valor da aposta: R$"))
    
    premio = odd[index_cavalo_escolhido] * valor_aposta
    print(f"Sua aposta: R${valor_aposta} em {cavalo_escolhido}")
    print(f"Prêmio possível: R${premio}")
    while(flag_confirma_aposta):
        confirma = input("Confirma a aposta? (S/N) ").strip().upper()
        if(confirma == "S"):
            flag_confirma_aposta = False
            saldo-=valor_aposta
            print(f"Vencedor:{cavalo_vencedor}")
            if index_cavalo_escolhido == index_vencedor:
                print("VOCÊ VENCEU")
                saldo+=premio
                print(f"Seu novo saldo é: R${saldo}")
            else:
                print("Você perdeu...")
                print(f"Seu novo saldo é: R${saldo}")
        elif confirma == "N":
            index_cavalo_escolhido = int(input("\nEscolha o número do seu cavalo\n"))-1
            cavalo_escolhido = cavalos_pareo[index_cavalo_escolhido].nome()
            valor_aposta = int(input("Insira o valor da aposta"))
        else:
            print("Insira um valor válido")
    
    index=0
    index_vencedor=0
    soma_vel=0
    lista_pontuacao=[]
    odd=[]
    flag_confirma_aposta=True
    
    
while True:
    aposta()
    resposta = input("Deseja continuar? (S/N): ")
    if resposta.strip().upper() != 'S':
        print(f"Você terminou o jogo com um saldo de R${saldo}")
        break


