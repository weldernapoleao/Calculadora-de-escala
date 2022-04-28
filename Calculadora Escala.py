import datetime

hoje = datetime.date.today()


def escala_12x36(escala,trabalha):
	if(escala == 1 and trabalha == 'SIM'):
	    if(qtd_dias%2 == 0):
	        return print("Dia ", data_futura," você estará trabalhando")
	    else:
	        return print("Dia ", data_futura," você não estará trabalhando")
	else:
	    if(qtd_dias%2 == 0):
	        return print("Dia ", data_futura," você não estará trabalhando")
	    else:
	        return print("Dia ", data_futura," você estará trabalhando")

def escala_24x48(escala,trabalha):
	if(escala == 2 and trabalha == 'SIM'):
	    dia_trabalhado = input("É o seu primeiro dia de trabalho? ")
	    dia_trabalhado = dia_trabalhado.upper()
	    if(dia_trabalhado == 'SIM'):
	        for i in range(1,qtd_dias,4):
	            trampa.append(i)
	            trampa.append(i+1)
	        if(qtd_dias in trampa):
	            return print("Você trabalhara nesse dia")
	        else:
	            return print("Opa! Você não trabalhara nesse dia")
	    else:
	        for i in range(2,qtd_dias,3):
	            if(i == 1):
	                trampa.append(i-1)
	                trampa.append(i)
	            else:
	                trampa.append(i)
	                trampa.append(i+1)
	        if(qtd_dias in trampa):
	            return print("Você trabalhara nesse dia")
	        else:
	            return print("Opa! Você não trabalhara nesse dia")
	else: 
		if(escala == 2 and (trabalha == 'NAO' or trabalha == 'NÃO')):
			dia_folga = input("É o seu primeiro dia de folga? ")
			dia_folga = dia_folga.upper()
	    	
			if(dia_folga == 'SIM'):
				for i in range(1,qtd_dias,4):
					folga.append(i)
					folga.append(i+1)
				if(qtd_dias in folga):
					return print("Você trabalhara nesse dia")
				else:
					return print("Opa! Você não trabalhara nesse dia")
			else:
				for i in range(2,qtd_dias,3):
					if(i == 1):
						folga.append(i-1)
						folga.append(i)
					else:
						folga.append(i)
						folga.append(i+1)
				if(qtd_dias in folga):
					return print("Você trabalhara nesse dia")
				else:
					return print("Opa! Você não trabalhara nesse dia")


string_data = input('Insira a data no seguinte formato ANO/MÊS/DIA: ')
ano, mes, dia = map(int, string_data.split('/'))
data_futura = datetime.date(ano, mes, dia)

print("----- EXEMPLO -----","\n","Escala 12x36: 1","\n","Escala 24x48: 2","\n")

escala = int(input("Informe a sua escala: "))

trabalha = input("Está trabalhando hoje? (Sim ou Nao) ")
trabalha = trabalha.upper()

diferenca = data_futura - hoje
qtd_dias = diferenca.days

folga = []
trampa = []

if(escala == 1):
	escala_12x36(escala, trabalha)
else:
	escala_24x48(escala,trabalha)
