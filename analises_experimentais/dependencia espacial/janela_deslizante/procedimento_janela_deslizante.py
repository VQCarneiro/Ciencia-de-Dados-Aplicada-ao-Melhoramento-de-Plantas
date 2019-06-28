########################################################################################################################
# Procedimento: Janela Deslizante
# Estudante: Heloisa
# Cultura: Eucalipto
# Data: 27/06/2019
########################################################################################################################
# Importação
import numpy as np
import pandas as pd
########################################################################################################################
# Carregar os dados
matriz_dados = np.loadtxt("matriz_croqui.txt",delimiter= " ")
nl,nc = np.shape(matriz_dados)

vetor_coluna_zeros = np.zeros((nl,1))

matriz_dados_mod = np.concatenate((matriz_dados,vetor_coluna_zeros),axis=1)
matriz_dados_mod = np.concatenate((vetor_coluna_zeros,matriz_dados_mod),axis=1)
nl_mod,nc_mod = np.shape(matriz_dados_mod)
vetor_linha_zeros = np.zeros((1,nc_mod))
matriz_dados_mod = np.concatenate((vetor_linha_zeros,matriz_dados_mod),axis=0)
matriz_dados_mod = np.concatenate((matriz_dados_mod,vetor_linha_zeros),axis=0)
nl_mod,nc_mod = np.shape(matriz_dados_mod)

########################################################################################################################
# Carregar croqui
croqui = np.loadtxt("croqui.txt",delimiter= " ")

vetor_coluna_zeros = np.zeros((nl,1))
croqui_mod = np.concatenate((croqui,vetor_coluna_zeros),axis=1)
croqui_mod = np.concatenate((vetor_coluna_zeros,croqui_mod),axis=1)

croqui_mod = np.concatenate((vetor_linha_zeros,croqui_mod),axis=0)
croqui_mod = np.concatenate((croqui_mod,vetor_linha_zeros),axis=0)

########################################################################################################################
# Procedimento janela deslizante
janela = np.array([[1/8,1/8,1/8],[1/8,0,1/8],[1/8,1/8,1/8]])

planilha = np.loadtxt("planilha.txt",delimiter= " ")
tabela = np.zeros((nl*nc,4))
cont = 0
for i in np.arange(1,nl_mod-1,1):
    for j in np.arange(1,nc_mod-1,1):
        print('######################################')
        print(matriz_dados_mod[i-1:i+2, j-1:j+2])
        print('--------------------------------------')
        print(matriz_dados_mod[i-1:i+2, j-1:j+2]*janela)
        print('--------------------------------------')
        print(croqui_mod[i,j])
        print('--------------------------------------')
        print(sum(sum(matriz_dados_mod[i-1:i+2, j-1:j+2]*janela)))
        print('--------------------------------------')
        print(planilha[np.where(planilha[:,1]==croqui_mod[i,j]),0])
        tabela[cont, 0] = croqui_mod[i,j]
        tabela[cont,1] = planilha[np.where(planilha[:,1]==croqui_mod[i,j]),0]
        tabela[cont,2] = planilha[np.where(planilha[:,1]==croqui_mod[i,j]),2]
        tabela[cont,3] = sum(sum(matriz_dados_mod[i-1:i+2, j-1:j+2]*janela))
        cont += 1

print('######################################')
print(tabela)
print(np.shape(tabela))
bin, count = np.unique(tabela[::,1],return_counts=True)
print(bin)
print(count)
#print(np.unique(tabela[::,0],return_counts=True))
print(tabela[np.where(tabela[::,0]==72),::])
tabela_ordenada = tabela[tabela[:,0].argsort()]
print(tabela_ordenada[np.where(tabela_ordenada[::,0]==72),::])

np.savetxt('tabela.csv', tabela, delimiter=',', fmt='%s')
np.savetxt('tabela_ordenada.csv', tabela_ordenada, delimiter=',', fmt='%s')

