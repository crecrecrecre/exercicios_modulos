def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calcular_filtragem(volume):
    return volume * 2, volume * 3

def calculo_imc (peso, altura):
    return (peso) / altura ** 2 

def classificacao (imc):
    if imc > 0 and imc <= 18.5 :
        clas = "baixo peso!"
    elif imc >= 18.5 and imc <= 24.9 :
        clas = "peso normal! parabéns!"
    elif imc >= 25 and imc <= 29.9 :
        clas = "excesso de peso!"
    elif imc >= 30 and imc <= 34.9 :
        clas = "obesidade de classe 1!"
    elif imc >= 35 and imc <=39.9 :
        clas = "obesidade de classe 2!"
    elif imc >= 40 :
        clas = "obesidade de classe 3!"
    else :
        clas = "imc invalido, tente digitar novamente!"
    return clas
                
    
def exc (imc):
    return imc - 24.9 
    
    
def esc (imc):
    return 24.9 - imc