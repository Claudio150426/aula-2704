c = 100000
t = 12
i = 1/100
for x in range (1, t + 1):
   M = c *(1+i)**t 
   #M_arredondado = round(M + 2)
   print(f"Mês {x}: R$ {M}")
   #print(f"Mês {x}: R$ {M_arredondado}")
