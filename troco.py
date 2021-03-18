# função geral do algoritmo, calculando o troco para cada centavo até o valor buscado, salvando o número de moedas para cada valor intermediário no vetor.
def calculaTroco(lista_valores_moedas, troco, min_moedas, moedas_usadas):
    for centavos in range(troco+1):                             # centavos vai de 0 ao valor do troco
        contagem_moedas = centavos
        nova_moeda = 1
        listaAux = []                
        for c in lista_valores_moedas:                          # salva em listaAux as moedas que são menores que o valor buscado.
            if c <= centavos:
                listaAux.append(c)
        for j in listaAux:                                      # percorre as moedas possíveis para o troco atual
            if min_moedas[centavos-j] + 1 < contagem_moedas:    # verifica se o número de moedas ao subtrair o valor de moedas mais a moeda atual é menor que a contagem armazenada
                contagem_moedas = min_moedas[centavos-j]+1      # se for, atualiza a quantidade de moedas armazenada com o valor testado acima.
                nova_moeda = j                                  # atualiza o valor da moeda testada atualmente (maior possível no troco)
        min_moedas[centavos] = contagem_moedas                  # atualiza o valor minimo de moedas para o valor atual analisado
        moedas_usadas[centavos] = nova_moeda                    # insere a moeda atual no vetor de moedas utilizada para o troco
    return min_moedas[troco]                                    # retorna o valor minimo de moedas para todos os trocos de 0 ao valor

def moedasResultantes(lista_moedas, montante):
    moedas_usadas = [0]*(montante+1)                            # vetor de moedas que foram utilizadas no troco
    contagem_moedas = [0]*(montante+1)                          # vetor com troco para cada valor de 0 ao montante
    calculaTroco(lista_moedas,montante,contagem_moedas,moedas_usadas)
    moeda = montante
    resultado = []
    while moeda > 0:
        essaMoeda = moedas_usadas[moeda]                        # a moeda atual será a moeda adicionada em moedas_usadas ao calcular o troco do montante
        resultado.append(essaMoeda)                             # adiciona a moeda na lista resultado
        moeda = moeda - essaMoeda                               # atualiza o valor atual do montante para continuar verificando as moedas restantes
    return resultado                                            # retorna o troco

if __name__ == "__main__":
    resultado = moedasResultantes([1,5,10,21,25], 63)
    print(resultado)