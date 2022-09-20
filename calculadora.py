def somar(n1, n2):
    return n1 + n2



def subtrair(n1, n2):
    return n1 - n2






def multiplicar(n1, n2):
    return n1 * n2





def dividir(n1, n2):
    return n1 / n2


while True:

    print('######## caculadora 0.1 ######')
    print('1=somar')
    print('2=subtrair')
    print('3=multiplicar')
    print('4=dividir')
    print('5=sair')

    escolha = int(input('Escolha:'))
    if escolha >=1 and escolha <= 4:
        v1=float(input('primeiro valor'))
        v2=float(input('segundo valor'))



        if escolha==1:           
            print(somar(v1,v2))
            
        elif escolha==2:
            print(subtrair(v1,v2))
            
        elif escolha ==3:
            print(multiplicar(v1,v2))
            
        elif escolha== 4:
            if v2==0:
                print('Erro de Divisão por zero')
            else:
                print(dividir(v1,v2))
        elif escolha == 5:
            print('Adeus!')
            break 
            


        else:
            print('Opção errada')
            

