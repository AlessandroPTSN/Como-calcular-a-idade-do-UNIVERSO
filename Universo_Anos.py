# -*- coding: utf-8 -*-

#http://leda.univ-lyon1.fr/fullsql.html
#http://leda.univ-lyon1.fr/leda/meandata.html
#http://leda.univ-lyon1.fr/fG.cgi?n=meandata&c=o&of=1,leda,simbad&nra=l&nakd=1&d=v3k%2C%20mod0&sql=(objtype%3D%27G%27)%20AND%20(v3k>3000)%20AND%20(v3k<30000)%20AND%20(mod0%20IS%20NOT%20NULL)%20AND%20(v3k%20IS%20NOT%20NULL)&ob=&a=html
#http://leda.univ-lyon1.fr/fullsql.html
                                                                                                   
import pandas as pd                                                                                      
data= pd.read_csv('C:/Users/Neo/Desktop/leda.csv', delimiter=";")
data
#se quiser refazer a estimativa usando uma amostra aleatória de 80% dos dados
#data = data.sample(n = 1133)

#Onde mod0 é o...
#MÓDULO DA DISTÂNCIA (mod0)
#https://en-m-wikipedia-org.translate.goog/wiki/Distance_modulus?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc
#mod0 = |m - M| 
#a diferença entre a magnitude aparente (m) e a magnitude absoluta (M) de um objeto astronômico. 
                                                                            
#E v3k é a      
#VELOCIDADE RADIAL (cz) em relação à radiação CMB       
#https://pt.wikipedia.org/wiki/Velocidade_radial                        

                   
                   
#DISTÂNCIA DE LUMINOSIDADE (Dl)                                    
#https://en-m-wikipedia-org.translate.goog/wiki/Luminosity_distance?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc                
#OBS: ela é boa para distâncias locais (em nossa galaxia) 
Dl=10**((data['mod0']/5)+1 ) 



#DESVIO PARA O VERMELHO (z)                              
#https://pt.wikipedia.org/wiki/Desvio_para_o_vermelho 
#v é a componente radial de velocidade em relação a fonte e o observador.
#c é a velocidade da luz no vácuo.  
#OBS c = 299792.458 km/s
z = data["v3k"]/299792.458

        
        
#DISTANCIA DE MOVIMENTO
#http://leda.univ-lyon1.fr/leda/param/modz.html
#A distancia de luminosidade com a correção do desvio para o vermelho
Dm = Dl/(z+1)


#OBS: a distância está em Parsec
# Converter da base do parsec para a base do kilometro
#https://www.unitconverters.net/length/parsec-to-kilometer.htm
Dm = Dm * 30856775812800


from scipy.optimize import curve_fit
def lin(x, b):
    return b * x
#OBS: f(x) = a*x + 0
#não possuimos o intercept(coeficiente linear) apenas o slope(coeficiente angular)
coeff, cov= curve_fit(lin,Dm,data["v3k"])
#o melhor slope para a regressão sem intercept:
b = coeff[0]
b




#A correlação entre distância e velocidade
Dm.corr(data["v3k"]) #0.89
#Ou seja, há uma forte relação positiva entre as variaveis


#Visualizando a relação linear entre distância e velocidade
import matplotlib.pyplot as plt
import numpy as np

x=np.array(Dm)
y=np.array(data["v3k"])

plt.scatter(x,y)
plt.title('Relação linear entre distância e velocidade')
plt.xlabel('DISTÂNCIA DE MOVIMENTO')
plt.ylabel('VELOCIDADE RADIAL')
f = lambda x: b*x #OBS: y = b*x 
plt.plot(x,f(x), c="red", label="fit line between min and max")



#lei de Hubble
#https://pt.wikipedia.org/wiki/Lei_de_Hubble
#v   = H0 * d
#onde
#v – velocidade (km/s^(-1))
#H0 – constante de Hubble (km/s^(-1) Mpc^(-1))
#r – distância em megaparsecs (Mpc)

#podendo ser re-escrita da seguinte forma
#v   = H0 * d
#1   = (H0 *d)/v
#1/h0= d/v

#tempo = Distancia / Velocidade 
#t = d/v

#Dada uma linha de regressão simples, se você tiver d e v (definir o intercept para 0); 
#A inclinação será o tempo em segundos.



#O tempo do UNIVERSO em segundos
Tempo_em_seg = (1/b)
Tempo_em_seg


#A idade do UNIVERSO em anos
ANOS = ((((Tempo_em_seg / 60)/ 60)/ 24)/ 365)
"{:,}".format(int(ANOS))





