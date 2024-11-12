horaI = int(input('Horas que a viagem começou: '))
minutoI = int(input('minutos que a viagem começou: '))
chegadaH = int(input('Horas que a viagem foi finalizada: '))
chegadaM = int(input("minutos que a viagem foi finalizada:"))
segparado = int(input('Segundos descansando: '))
litros_deg = float(input('Informe a quantidade de combustível gasto em litros: '))
preço = float(input('Quanto foi pago por litros de combustível: '))  
distancia = float(input('Informe a distancia percorrida em KM '))

if chegadaH < horaI or chegadaH == horaI and minutoI > chegadaM:
    tempohora = ((24 - horaI) + chegadaH) * 3600
    tempomin = (chegadaM * 60) - (minutoI * 60)            
    tempodviagem = tempohora + tempomin 

else:
    tempohora = (chegadaH * 3600) - (horaI * 3600)
    tempomin = (chegadaM * 60) - (minutoI * 60)                 
    tempodviagem = tempohora + tempomin 


print (f' O tempo que a viagem durou em segundos foi: {tempodviagem}')


custo = litros_deg * preço
print(f' O custo da viagem foi: R$ {custo}') 


vlm_movimento = int (distancia  / (tempodviagem / 3600))     
vlm_global  = int (distancia / ((tempodviagem + segparado) / 3600))     



print (f'A velocidade media global é: {vlm_global}  KM/h e a velocidade media em movimento é: {vlm_movimento} KM/h')

kmporL = int (distancia / litros_deg)
litrosporH = int (litros_deg / (tempodviagem / 3600))
custoporKM = (distancia / custo)


print (f'O desempenho do veículo foi KM/l:  {kmporL} Litros/h: {litrosporH}  R$/KM: {custoporKM:.2f}')