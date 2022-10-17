#Leonardo Zaniboni Silva   11801049  

arquivo = open("arquivo_inicial_com,.txt","r")                  #abrindo o arquivo
dados = arquivo.read()                                          #lendo o arquivo
arquivo.close()

novos_dados = ""                                                #inicia uma string vazia
em_string = False                                               #booleano para verificar se o caracter esta em uma string
inverter = False                                                #boleano para alterar a variavel 'em_string' para true no final da iteração, se necessario

for i in range(len(dados)):

  if em_string == False :                                       #se não estiver em uma string, alterar os ',' por ';'
      if dados[i] == ',' : 
        novos_dados = novos_dados + dados[i].replace(",",";")
      else:
        novos_dados = novos_dados + dados[i]

      if dados[i] == '"' and dados[i-1] != chr(92):             #se caso encontrar um '"' e o caracter anterior não for uma "\"  = os próximos caracteres fazem parte de uma string
        inverter = True

  else:
      novos_dados = novos_dados + dados[i]                      #caso seja uma string, apenas copie os valores e não mude o ',' por ';'

      if dados[i] == '"' and dados[i-1] != chr(92):             #se caso encontrar um '"' e o caracter anterior não for uma "\"  = os próximos caracteres não fazem parte de uma string
        inverter = True

  if inverter == True and em_string == False :                  #lógica para inverter o boleano 'em_string'
      em_string = True
  elif inverter == True and em_string == True :
      em_string = False

  inverter = False                                              #garantindo que a cada iteração começa sem inverter

arquivo = open('arquivo_final_com;.txt','a')                    #salvando os dados em um novo arquivo
arquivo.write(novos_dados)
arquivo.close()
