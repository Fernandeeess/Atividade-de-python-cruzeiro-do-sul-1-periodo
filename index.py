import math;
# Atividade - 1
print("Análise e Desenvolvimento de Sistemas - Unicsu");

# Atividade - 2
hobby = str(input("Digite o seu Hobby Favorito: "));
print("O seu Hobby favorito e:",hobby);

# Atividade - 3
anoNascimento = input("Digite o seu ano de nascimento: ")
print("O seu ano de nascimento e", anoNascimento)

# Atividade - 4
lastName = input("Digite o seu ultimo nome: ");
print("Família",lastName)

# Atividade - 5
favoriteSport = input("Digite o seu esporte favorito: ");
print("O seu esporte favorito e ",favoriteSport);

# Atividade - 6
anoAtual = int(input("Digite o ano atual: "));
anoDeNascimento = int(input("Digite o seu ano de nascimento: "));
idade = (anoAtual - anoDeNascimento);
print("Voce tem",idade,"Anos");

# Atividade - 7
salario = float(input("Digite o seu salario: "));
percentualAumento = float(input("Digite o seu percentual de aumento: "));
salarioAtualizado = (salario * (percentualAumento/100)) + salario;
if(percentualAumento <= 10 ):
    print(salarioAtualizado);
else:print("O valor e muito alto, Digite um valor abaixo de 10%")

# Atividade - 8
base = float(input("Digite o tamanho da base em metros: "));
altura = float(input("Digite o tamanho da altura em metros: "));
perimetro = (base + altura) *  2;
area = (base * altura);
print("O perimetro do retângulo e: ", perimetro, "e sua area e de: " ,area);

# Atividade - 9
productPrice = float(input("Digite o preço do produto: "));
pagamentoAvista = str(input("Pagamento a vista? Digite Y para verdadeiro e N para falso: "))
if (pagamentoAvista == "Y" or pagamentoAvista == "y"):
    productpriceWithDiscount= productPrice - (productPrice * (5 / 100));
    print("O preço do produto a vista e de: ",productpriceWithDiscount);
elif pagamentoAvista == "N" or pagamentoAvista == "n" :
        print("Apenas Pagamento a vista possui desconto de 5%");
        print(productPrice);

# Atividade - 10

distEntreAsCidade = float(input("Digite a distância em km entre duas cidades: "));
tempoDaViagem = float(input("Digite o tempo da viagem em horas: "));
vMediaKm = distEntreAsCidade / tempoDaViagem;
vMediaMs = (distEntreAsCidade / 1000) / (tempoDaViagem / 60);
print("a velocidade media entre as duas cidade e igual a",vMediaMs,"m/s");
print("a velocidade media entre as duas cidade e igual a",vMediaKm,"km/H");

# Atividade - 11
a = float(input("Digite o numero correspondente da letra A: "))
b = float(input("Digite o numero correspondente da letra B: "))
c = float(input("Digite o numero correspondente da letra C: "))
delta = (b**2 -4 * a * c);
x1 = (-b + math.sqrt(delta)) / (2 * a);
x2 = (-b - math.sqrt(delta)) / (2 * a);
print("a primeira raiz e x1:",x1);
print("a segunda raiz e x2:",x2);
print (delta);

# Atividade - 12
valorEmDolares=float(input("Digite um valor em dolares: "));
reaisEmDolares = valorEmDolares * 5.02  
print("O valor digitado para conversão foi de:",valorEmDolares,"Dolares"," o valor convertido e de:",reaisEmDolares,"Reais") 
# Atividade - 13
priceToPay = float(input("Digite o valor a pagar no restaurante: "));
valorTotal = priceToPay + (priceToPay * (10 / 100)) ;
print("O Valor total a ser pago com a gorja e de ",valorTotal);
# Atividade - 14
tc = float(input("digite a temperatura em graus Celsius: "));
tf = 1.8 * tc + 32;
tk = tc + 273;
print("a respectiva temperatura nas escalas Fahrenheit e igual a:" , tf);
print("a respectiva temperatura nas escalas Kelvins e igual a:" , tk)