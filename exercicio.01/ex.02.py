from uteis import calculo_imc, classificacao, exc, esc


peso = float(input("digite seu peso (em kg): "))
altura = float(input("digite sua altura (em metros): "))

imc = calculo_imc(peso, altura)
classificacao = classificacao(imc)

print(f"Seu IMC é de {imc:.2f}\n")  
print(f"Sua classificação é: {classificacao}\n")

excesso = exc(imc)
escassez = esc(imc)

if imc > 24.9 :
    print (f"Para que voce chegue no imc necessário, você precisa perder {excesso:.2f} quilos!\n")
elif imc < 18.5 :
    print (f"Para que voce chegue no imc necessário, você precisa ganhar {escassez:.2f} quilos!\n")