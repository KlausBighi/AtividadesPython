#Locação de Veículos

diaria = int(input('Informe o total de dias: '))
km = float(input('Informe o total de KM rodados: ').replace(",","."))
pagamento = diaria * 40 + km * 0.45 #O Valor da diária é $40,00 enquanto são cobrados $0,45 por KM rodado
print (pagamento)
