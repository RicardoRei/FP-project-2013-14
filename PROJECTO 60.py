''' ---GRUPO 24 - Projecto Sopa de Letras---
79763- Andre Nobre
78087- Joana Pereira
78047- Ricardo Rei
'''
from janela_sopa_letras import *

#------Tipos Abstractos de Informacao---------


'''----3.1 Tipo Direcao---'''

#1.Reconhecedor de Direcoes
'''Reconhecedores: universal-> logico '''

# Tuplo das direcoes utilizadas
direcoes = ('N', 'W', 'NE', 'NW', 'SE', 'SW', 'E', 'S') 

def e_direcao(arg):
    '''e_direcao(arg) devolve TRUE se arg for do tipo direcao'''
    return arg in direcoes
    
def e_norte(arg):
    '''e_norte(arg) devolve TRUE se arg=="N" '''
    return arg == 'N'
    
def e_sul(arg):
    '''e_sul(arg) devolve TRUE se arg=="S"'''
    return arg == 'S'
        
def e_leste(arg):
    '''e_leste(arg) devolve TRUE se arg=="E"'''
    return arg == 'E'

def e_oeste(arg):
    '''e_oeste(arg) devolve TRUE se arg=="W" '''
    return arg == 'W'

def e_nordeste(arg):
    '''e_nordeste(arg) devolve TRUE se arg=="NE" '''
    return arg == 'NE'

def e_noroeste(arg):
    '''e_noroeste(arg) devolve TRUE se arg=="NW" '''
    return arg == 'NW'

def e_sudeste(arg):
    '''e_sudeste(arg) devolve TRUE se arg=="SE" '''
    return arg == 'SE'

def e_sudoeste(arg):
    '''e_sudoeste(arg) devolve TRUE se arg=="SW" '''
    return arg == 'SW'


#2.Testes
'''Testes: direcao x direcao-> logico '''

def direcoes_iguais(d1, d2):
    '''direcoes_iguais(d1,d2) devolve TRUE se as direcoes forem iguais '''
    return d1 == d2
      

#3.Outras Operacoes

def direcao_oposta(d):
    ''' direcao_oposta: direcao -> direcao
    direcao_oposta(d) devolve a posicao oposta de d com base no tuplo direcoes
    '''
    direcoes = ('N', 'W', 'NE', 'NW', 'SE', 'SW', 'E', 'S')
    for i in range(len(direcoes)):
        if direcoes[i] == d:
            return direcoes[len(direcoes) - 1 - i]

'''---3.2 Tipo Coordenada---'''

#1.Construtor

def coordenada(l, c, d):
    ''' coordenada: N0 x N0 x direcao -> coordenada 
    coordenada(l,c,d) devolve coordenada referente a linha,coluna 
    e direcao dadas.
    '''
    if isinstance(l,int) and isinstance(c, int) and e_direcao(d)\
    and 0 <= l and 0 <= c:
        return (l, c ,d)
    raise ValueError('coordenada: argumentos invalidos')

#2. Seletores

def coord_linha(c):
    '''coord_linha: coordenada -> N0 
       coord_linha(c) devolve a linha da coordenada inserida
    '''
    return c[0]

def coord_coluna(c):
    '''coord_coluna: coordenada -> N0 
    coord_coluna(c) devolve a coluna da coordenada inserida
    '''    
    return c[1]

def coord_direcao(c):
    '''coord_direcao: coordenada -> direcao
    coord_direcao(c) devolve a direcao da coordenada inserida
    '''
    return c[2]

#3. Reconhecedor

def e_coordenada(arg):
    '''e_coordenada: universal -> logico
    e_coordenada(arg) devolve TRUE se arg for do tipo coordenada
    '''
    if isinstance(arg, tuple)\
       and len(arg)==3 \
       and isinstance(arg[0],int)\
       and isinstance(arg[1],int)\
       and e_direcao(arg[2]):
        return True
    return False
    
#4. Teste

def coordenadas_iguais(c1, c2):
    ''' coordenadas_iguais: coordenada x coordenada -> logico
    coordenadas_iguais(c1,c2) devolve TRUE se as coordenadas forem iguais
    '''
    return c1 == c2

#5. Outras Operacoes 
def coordenada_string(c):
    '''coordenada_string: coordenada -> string
    coordenada_string(c) devolve uma string com o valor da coordenada inserida 
    '''
    return '('+str(coord_linha(c))+', '\
           +str(coord_coluna(c))+ ')-'+coord_direcao(c)
'''---3.3 Tipo Grelha---'''

#1.Construtor

def grelha(lst):
    '''grelha: lista de strings -> grelha
    grelha(lst) devolve uma matriz mxn em que m representa o numero de linhas
    e n representa o numero de colunas
    '''
    grelha = []
    if lst == [] or not isinstance(lst, list):
        raise ValueError('grelha: argumentos invalidos')    
    for i in range(len(lst)):
        if not isinstance(lst[i], str) or len(lst[0]) != len(lst[i]):
            raise ValueError('grelha: argumentos invalidos')
        grelha += [list(lst[i])]
    return grelha

#2. Selectores

def grelha_nr_linhas(g):
    '''grelha_nr_linhas: grelha -> N0
    grelha_nr_linhas(g) devolve o numero de linhas da grelha inserida
    '''
    return len(g)

def grelha_nr_colunas(g):
    '''grelha_nr_colunas: grelha -> N0
    grelha_nr_colunas(g) devolve o numero de colunas da grelha inserida
    '''
    return len(g[0])

def grelha_elemento(g, l, c):
    '''grelha_elemento: grelha x N0 x N0 -> caracter
    grelha_elemento(g,l,c) devolve o caracter da grelha correspondente
    a linha e coluna dadas 
    '''
    if 0 <= l < grelha_nr_linhas(g) and 0 <= c < grelha_nr_colunas(g):
        return g[l][c]
    raise ValueError('grelha_elemento: argumentos invalidos')


def grelha_linha(g, c):
    '''grelha_linha: grelha, coordenada -> string
    grelha_linha(g,c) recebe uma grelha e uma coordenada e devolve a string da
    linha que contem essa coordenada para uma dada direccao'''
    
    def inverte(linha):
        '''inverte: string -> string
        inverte(linha) recebe uma string e devolve essa string ao contrario'''
        strg = ''
        for i in range(1,len(linha)+1):
            strg += linha[-i]
        return strg

    def primeiro_elemento_diagonal(g, c, il, ic):
        '''primeiro_elemento_diagonal: grelha, coordenada, indice para a linha,
        indice para a coluna -> coordenada
        primeiro_elemento_diagonal recebe um grelha uma coordenada, um indice
        para a linha e um indice para a coluna e devolve a coordenada do pri-
        meiro elemento dessa linha'''
        colunas = coord_coluna(c)
        linhas = coord_linha(c)
        while (1 <= colunas < grelha_nr_colunas(g) - 1)\
              and (1 <= linhas < grelha_nr_linhas(g) - 1):
            colunas += ic
            linhas += il
        return coordenada(linhas, colunas, coord_direcao(c))

    def diagonal(g, c, il, ic):
        '''diagonal: grelha, coluna, indice linha, indice coluna -> string
        diagonal recebe uma grelha, uma coluna, um indice para a linha e um 
        indice para a coluna e devolve a diagonal formada pela linha que passa
        por essa diagonal'''
        strg = ''
        colunas = coord_coluna(primeiro_elemento_diagonal(g, c, -il, -ic))
        linhas = coord_linha(primeiro_elemento_diagonal(g, c, -il, -ic))        
        while 0 <= colunas < grelha_nr_colunas(g) \
              and 0 <= linhas < grelha_nr_linhas(g):
            strg += g[linhas][colunas]
            colunas += ic
            linhas += il
        return strg    
    
    def norte(g ,c):
        '''norte: grelha, coordenada -> string
        norte(g,c) recebe uma grelha e uma coordenada e devolve a linha que 
        passa por aquela coordenada na direccao norte'''
        strg = ''
        for i in range(1, grelha_nr_linhas(g) + 1):
            strg += g[-i][coord_coluna(c)]
        return strg 
    
    def oeste(g, c):
        '''oeste: grelha, coordenada -> string 
        oeste(g,c) recebe uma grelha e uma coordenada e devolve a linha que 
        passa por aquela coordenada na direccao oeste'''
        strg = ''
        for i in range(1, grelha_nr_colunas(g) + 1):
            strg += g[coord_linha(c)][-i]
        return strg      
        
    if coord_linha(c) < grelha_nr_linhas(g) \
        and coord_coluna(c) < grelha_nr_colunas(g) \
        and e_direcao(coord_direcao(c)):
    
        if e_norte(coord_direcao(c)):
            return norte(g,c)
        
        elif e_sul(coord_direcao(c)):
            return inverte(norte(g,c))
        
        elif e_leste(coord_direcao(c)):
            return inverte(oeste(g,c))
        
        elif e_oeste(coord_direcao(c)):
            return oeste(g,c)
        
        elif e_noroeste(coord_direcao(c)):
            return diagonal(g, c, -1, -1) 
          
        elif e_nordeste(coord_direcao(c)):
            return diagonal(g, c, -1, 1)
        
        elif e_sudoeste(coord_direcao(c)):
            return diagonal(g, c, 1, -1)
        
        elif e_sudeste(coord_direcao(c)):
            return diagonal(g, c, 1, 1)
        
    raise ValueError('grelha_linha: argumentos invalidos')
        
        

#3.Reconhecedor
def e_grelha(arg):
    '''e_grelha: universal ->logico
    e_grelha(arg) delvolve TRUE se arg for do tipo grelha
    '''
    if isinstance(arg, list) and arg !=[]:
        for i in range(len(arg)):
            if isinstance(arg[i], list):
                for k in range(len(arg[0])):
                    if isinstance(arg[i][k], str)\
                       and len(arg[i][k]) == 1:
                        return True
    return False

#4.Testes

def grelhas_iguais(g1, g2):
    '''grelhas_iguais: grelha x grelha -> logico
    grelhas_iguais(g1,g2) devolve TRUE se g1==g2
    '''
    return g1 == g2



'''---3.4 Tipo Resposta---''' 
#1. Construtor
def resposta(lst):
    '''resposta: lista de tuplos(string,coordenada) -> resposta
    resposta(lst) devolve a resposta de cada um dos elementos que compoem 
    os tuplos da lista lst  
    '''
    if isinstance(lst, list): 
        for i in range(len(lst)):
            if not isinstance(lst[i], tuple)\
               or  not isinstance(lst[i][0], str)\
               or not e_coordenada(lst[i][1]):
                raise ValueError('resposta: argumentos invalidos')
        return lst
    raise ValueError('resposta: argumentos invalidos')
     
                
#2.Selector
def resposta_elemento(res, n):
    '''resposta_elemento: resposta x N0 -> tuplo(string,coordenada) 
    resposta_elemento(res,n) devolve o enesimo elemento da resposta
    '''
    if 0 <= n < resposta_tamanho(res):    
        return res[n]
    raise ValueError('resposta_elemento: argumentos invalidos')
def resposta_tamanho(res):
    '''resposta_tamanho: resposta ->N0
    resposta_tamanho(res) devolve o numero de elementos da resposta
    '''
    return len(res)

#3.Modificador 

def acrescenta_elemento(r,s,c):
    '''acrescenta_elemento: resposta x string x coordenada -> resposta
        acrescenta_elemento(r,s,c) devolve r + tuplo(s,c)
        '''    
    return r + resposta([(s ,c)])

#4.Reconhecedor

def e_resposta(arg):
    '''e_resposta: universal -> logico
    e_resposta(arg) devolve TRUE se arg==resposta
    '''
    try:
        return arg == resposta(arg)
    except:
        return False
        
#5.Testes
def respostas_iguais(r1, r2):
    '''respostas_iguais: resposta x resposta ->logico
    respostas_iguais(r1,r2) devolve TRUE se r1==r2
    '''
    
    def resposta_maiusculas(res):
        '''resposta_maiusculas: resposta -> resposta
        resposta_maiusculas recebe como argumento uma resposta e devolve a mesma 
        resposta com as letras das strings transformadas em letras maiusculas'''
        for i in range(resposta_tamanho(res)):
            aux = ()
            x = res[i][0]
            for k in range(len(x)):
                if ord(x[k]) not in range(65, 91):
                    x = x[:k] + chr(ord(x[k]) - 32) + x[k+1:]
            res[i] = (x, res[i][1])
        return res 
    
    r1 = resposta_maiusculas(r1)
    r2 = resposta_maiusculas(r1)
    if resposta_tamanho(r1) == resposta_tamanho(r2):
        for i in range(resposta_tamanho(r1)):
            if not resposta_elemento(r1, i) in r2:
                return False
        return True
    return False
    

#outras operacoes
def resposta_string(res):
    '''resposta_string: resposta -> string
    resposta string(res) recebe uma resposta e devolve a mesma transformada 
    numa string'''
    
    def borbulhamento(res):
        '''borbulhamento: resposta -> resposta
        borbulhamento(res) recebe uma resposta e devolve a mesma resposta com 
        os elementos ordenados'''
        nenhuma_troca = False
        while not nenhuma_troca:
            nenhuma_troca = True
            for i in range(resposta_tamanho(res)-1):
                if res[i][0] > res[i+1][0]:
                    res[i], res[i+1] = res[i+1],res[i]
                    nenhuma_troca = False
        return res    
    
    res = borbulhamento(res)           
    strr = '['
    for i in range(resposta_tamanho(res)-1):
        strr += '<' + res[i][0] + ':' + coordenada_string(res[i][1])+ '>, '
    strr += '<' + res[(resposta_tamanho(res)-1)][0] + ':' \
        + coordenada_string(res[(resposta_tamanho(res)-1)][1]) + '>]'
    return strr 
    
''' 4 ''' 
def sopa_letras(fich):
    '''sopa_letras: fich -> respostas do ficheiro
    sopa_letras(fich): recebe como argumento o nome de um ficheiro e devolve 
    as respostas da sopa de letras contida no ficheiro'''

    def palavras(strr):
        ''' palavras: string -> lista de strings
        palavras(strr): recebe uma string que vai conter as palavras da 
        da resposta a sopa_letras, e devolve uma lista com essas palavras'''
        
        def guarda(strg, count):
            '''guarda: string, indice -> string
            guarda(strg, count): recebe uma string e um indice e devolve a 
            string ate ao indice dado '''
            
            guarda = ''
            for i in range(count):
                guarda += strg[i]
            return guarda 
        
        lst = []
        palavras = strr[10:]
        count = 0
        while len(palavras) > 1:
            if palavras[count] == ',':
                palavras = palavras[:count] + palavras[count+1:]
            elif palavras[count] == ' ' or palavras[count] == '\n':
                lst += [guarda(palavras, count)]
                palavras = palavras[count+1:]
                count = 0
            else:
                count += 1
        return lst
      
    
    def linha_da_grelha(strg):
        '''linha_da_grelha: strg -> strg
        linha_da_grelha recebe uma string e devolve a mesma string sem espacos 
        ou mudancas de paragrafo (\n)'''
        
        count = 0
        while ' ' in strg or '\n' in strg:
            if strg[count] == ' ' or strg[count] == '\n':
                strg = strg[:count] + strg[count+1:]
            else:
                count += 1
        return strg
    
    def grelha_da_sopa(lst):
        '''grelha_da_sopa: lst -> grelha
        grelha_da_sopa(lst) recebe como argumento uma lista de string e devolve
        uma grelha'''
        for i in range(len(lst)):
            lst[i] = linha_da_grelha(lst[i])
        return grelha(lst) 
    
    ficheiro = open(fich, 'r')
    lst_linhas = ficheiro.readlines()
    ficheiro.close()
       
    lst_res = palavras(lst_linhas[1])
    g = grelha_da_sopa(lst_linhas[2:])
    res = procura_palavras_numa_direcao(g, lst_res, direcoes[0])
    for i in range(1, len(direcoes)):
        respostas = procura_palavras_numa_direcao(g, lst_res, direcoes[i])
        t_res = resposta_tamanho(respostas)
        for k in range(t_res): #ciclo para acrescentar ao res as respostas 
                                #dadas pela funcao procura_palavras_numa_dr
            tuplo = resposta_elemento(respostas, k)
            res = acrescenta_elemento(res, tuplo[0], tuplo[1])
            
    janela = janela_sopa_letras(fich)   
    janela.mostra_palavras(res)
    janela.termina_jogo()    
    return res
                
def procura_palavras_numa_direcao(g, ls, dr):
    '''procura_palavras_numa_direcao: grelha, lista de strings, direcao 
    -> resposta
    procura_palavras_numa_direcao(g, ls, dr) recebe uma grelha, uma lista de
    strings e uma direccao e devolve a resposta com as coordenadas de cada 
    string na grelha para aquela direcao'''
    
    def maiusculas(lst):
        '''maiusculas: lst -> lst
        maiusculas(lst) recebe uma lista de strings e devolve a mesma lista mas
        com todos os elementos das strings em letra maiuscula'''
        
        for i in range(len(lst)):
            strg = lst[i]
            for k in range(len(strg)):
                if ord(strg[k]) not in range(65, 91):
                    strg = strg[:k] + chr(ord(strg[k]) - 32) + strg[k+1:]
            lst[i] = strg
        return lst
    
    def grelha_maiusculas(g):
        '''grelha_maiusculas: grelha -> grelha
        grelha_maiusculas(g) recebe como argumento uma grelha e avalia se existem
        letras minusculas, se houver devolve a mesma grelha mas com as letras 
        maiusculas'''
        for i in range(grelha_nr_linhas(g)):
            for k in range(grelha_nr_colunas(g)):
                if  97 <= ord(grelha_elemento(g, i, k)) <= 122:
                    g[i][k] = chr(ord(grelha_elemento(g, i, k)) - 32)
        return g    
    
    def posicao_strg(strg, palavra):
        '''posicao_strg: string -> indice
        posicao_strg(strg, palavra) recebe uma strg e uma palavra e vai 
        devolver o indice onde se encontra a primeira letra da palavra 
        desejada'''
        for i in range(len(strg)):
            if palavra == strg[i:i+len(palavra)]:
                return i
            
    def norte(g, palavra):
        ''' norte: grelha, palavra -> resposta
        norte(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        norte'''
        for i in range(grelha_nr_colunas(g)):
            vertical = grelha_linha(g,coordenada(grelha_nr_linhas(g)-1,i,'N'))
            if palavra in vertical:
                return acrescenta_elemento(respostas, palavra, coordenada\
            (grelha_nr_linhas(g) -1 - posicao_strg(vertical,palavra), i, 'N'))
        return respostas
    
        
    def sul(g, palavra):
        ''' sul: grelha, palavra -> resposta
        sul(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        sul'''        
        for i in range(grelha_nr_colunas(g)):
            vertical = grelha_linha(g, coordenada(0, i, 'S'))
            if palavra in vertical:
                return acrescenta_elemento(respostas, palavra, \
                coordenada(posicao_strg(vertical,palavra), i, 'S'))
        return respostas
                       
    def oeste(g, palavra):
        ''' oeste: grelha, palavra -> resposta
        oeste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        oeste'''        
        for i in range(grelha_nr_linhas(g)):
            horizontal = grelha_linha(g, coordenada(i, grelha_nr_colunas(g)-1, \
                                                    'W'))
            if palavra in horizontal:
                return acrescenta_elemento(respostas, palavra, coordenada\
        (i, grelha_nr_colunas(g) -1 - posicao_strg(horizontal, palavra), 'W'))
        return respostas
                    
                    
    def leste(g, palavra):
        ''' leste: grelha, palavra -> resposta
        leste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        leste'''        
        for i in range(grelha_nr_linhas(g)):
            horizontal = grelha_linha(g, coordenada(i, 0, 'E'))
            if palavra in horizontal:
                return acrescenta_elemento(respostas, palavra,\
                coordenada(i, posicao_strg(horizontal, palavra), 'E'))
        return respostas  
    
    def noroeste(g, palavra):
        ''' noroeste: grelha, palavra -> resposta
        noroeste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        noroeste''' 
        #nas diagonais divido a matriz em dois triangulos
        #primeiro triangulo e formado pelas diagonais que tem o indice maximo 
        #nas colunas e o indice variado nas linhas
        for i in range(grelha_nr_linhas(g)):
            diagonal = grelha_linha(g, coordenada\
                                    (i, grelha_nr_colunas(g)-1, 'NW'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra,\
                coordenada(i-posicao_strg(diagonal, palavra), \
                grelha_nr_colunas(g) -1 -posicao_strg\
                (diagonal, palavra), 'NW'))
        #segundo triangulo e formado pelas diagonais que tem o indice maximo 
        #nas linhas e o indice variado nas colunas
        for i in range(grelha_nr_colunas(g) -1):
            diagonal = \
            grelha_linha(g, coordenada(grelha_nr_linhas(g)-1, i, 'NW'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra, \
                            coordenada(grelha_nr_linhas(g)-1 \
                - posicao_strg(diagonal, palavra), i \
                - posicao_strg(diagonal, palavra), 'NW'))
        return respostas 
    
    def nordeste(g, palavra):
        ''' nordeste: grelha, palavra -> resposta
        nordeste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        nordeste''' 
        #triangulo formado pelas diagonais com o indice das colunas a 0 e as 
        #as linhas a variar
        for i in range(grelha_nr_linhas(g)):
            diagonal = grelha_linha(g, coordenada(i, 0, 'NE'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra,\
                coordenada(i - posicao_strg(diagonal, palavra), \
                posicao_strg(diagonal, palavra), 'NE'))
        #triangulo formado pelas diagonais com indice das linhas maximo e indice
        #das colunas a variar
        for i in range(1,grelha_nr_colunas(g)):
            diagonal = grelha_linha(g, coordenada\
                                    (grelha_nr_linhas(g)-1, i, 'NE'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra, \
                coordenada\
                (grelha_nr_linhas(g) - 1 -posicao_strg(diagonal, palavra), \
                i + posicao_strg(diagonal, palavra), 'NE'))
        return respostas
    
    def sudoeste(g, palavra):
        ''' sudoeste: grelha, palavra -> resposta
        sudoeste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        sudoeste'''
        #triangulo formado pelas diagonais com o indice das colunas maior e o
        #indice das linhas a variar
        for i in range(grelha_nr_linhas(g)):
            diagonal = grelha_linha(g, coordenada\
                                    (i, grelha_nr_colunas(g)-1, 'SW'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra,\
                coordenada(i + posicao_strg(diagonal, palavra),\
                grelha_nr_colunas(g)-1 - posicao_strg\
                (diagonal, palavra), 'SW'))
        #triangulo formado pelas diagonais com o indice das linhas menor e o 
        #indice das colunas a variar
        for i in range(grelha_nr_colunas(g)-1):
            diagonal = grelha_linha(g, coordenada(0, i, 'SW'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra, \
                coordenada(posicao_strg(diagonal, palavra), \
                i - posicao_strg(diagonal, palavra), 'SW'))
        return respostas
            
    def sudeste(g, palavra):
        ''' sudeste: grelha, palavra -> resposta
        sudeste(g, palavra) recebe como argumentos uma grelha e uma palavra e 
        devolve a resposta que contem a palavra e as suas coordenadas sentido 
        sudeste''' 
        #triangulo formado pelas diagonais com o indice das colunas a 0 e o 
        #indice das linhas a variar
        for i in range(grelha_nr_linhas(g)):
            diagonal = grelha_linha(g, coordenada(i, 0, 'SE'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra,\
                coordenada(i + posicao_strg(diagonal, palavra), \
                posicao_strg(diagonal, palavra), 'SE'))
        #triangulo formado pelas diagonais com o indice das linhas a 0 e o
        #indice das colunas a variar
        for i in range(1,grelha_nr_colunas(g)):
            diagonal = grelha_linha(g, coordenada(0, i, 'SE'))
            if palavra in diagonal:
                return acrescenta_elemento(respostas, palavra, \
                coordenada(posicao_strg(diagonal, palavra), \
                i + posicao_strg(diagonal, palavra), 'SE'))
        return respostas 
    
    g = grelha_maiusculas(g)
    ls = maiusculas(ls)
    respostas = resposta([])
    if e_norte(dr):
        for i in range(len(ls)):
            respostas = norte(g, ls[i])
        return respostas
    
    elif e_sul(dr):
        for i in range(len(ls)):
            respostas = sul(g, ls[i])
        return respostas
    
    elif e_oeste(dr):
        for i in range(len(ls)):
            respostas = oeste(g, ls[i])
        return respostas
    
    elif e_leste(dr):
        for i in range(len(ls)):
            respostas = leste(g, ls[i])
        return respostas
    
    elif e_noroeste(dr):
        for i in range(len(ls)):
            respostas = noroeste(g, ls[i])
        return respostas
    elif e_nordeste(dr):
        for i in range(len(ls)):
            respostas = nordeste(g, ls[i])
        return respostas
    
    elif e_sudoeste(dr):
        for i in range(len(ls)):
            respostas = sudoeste(g, ls[i])
        return respostas
    
    elif e_sudeste(dr):
        for i in range(len(ls)):\
            respostas = sudeste(g, ls[i])
        return respostas