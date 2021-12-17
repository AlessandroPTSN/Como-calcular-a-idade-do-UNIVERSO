# Como calcular a idade do UNIVERSO 🌌

Neste trabalho, me dedico a mostrar a vocês como cheguei a uma estimativa da idade do universo usando a lei de Hubble, dados sobre galáxias e Python!

<details>
<summary>Obs</summary>
<p align = "center">
Devo resaltar que não sou um físico, muito menos um astronomo, então as informações citadas nesse trabalho estão sujeitas a erros de interpretação ou por simplificação. 
</p> 

</details>


## Introdução


Há muito tempo atrás um astrônomo chamado Edwin Powell Hubble (sim, o mesmo nome do telescópio espacial Hubble) percebeu que ao observar as galáxias, as mesmas estavam se afastando. Não só isso, mas ele percebeu que as galáxias mais longe estavam se afastando mais rapidamente e as mais próximas estavam se afastando mais lentamente. Com isso, ele percebeu que havia uma relação linear positiva entre a distância e velocidade das galáxias e nomeou este fenômeno como Lei de Hubble.  
<details>
<summary>Info</summary>
<p>
https://pt.wikipedia.org/wiki/Lei_de_Hubble
</p> 

</details>

<p align = "center">
<img src="https://user-images.githubusercontent.com/50224653/146562829-1ac130ca-5f4c-4c79-95c7-f4d058e25062.png" width=50% height=50%>
</p> 


Logo se obtermos a velocidade e a distância das galáxias, podemos calcular essa relação linear.  
Como obter os dados?  
Através do HypeLeda, um site que armazena um grande banco de dados sobre altas informações relacionadas a galáxias e cosmologia.  

<details>
<summary>Info</summary>
<p>
http://leda.univ-lyon1.fr/intro.html
</p> 
</details>

## Obtenção dos dados

Se você possui familiaridade com SQL, então o site é uma mão na roda. Podemos pegar apenas as variáveis que queremos em vez de baixar o banco de dados todo através de consultas feitas diretamente no próprio site, insano!!  
As informações sobre a separação dos dados e sobre a consulta se encontram a baixo, mas se possuir dificuldades, o banco de dados também se encontra no repositório.  

<details>
<summary>Info</summary>
<p>

http://leda.univ-lyon1.fr/fullsql.html  
Peguei de todas as galáxias (objtype='G') as variaveis velocidade (v3k) que estão entre 3000<v3k<30000 e o módulo da distâncida (mod0)  
  
Info das variaveis: http://leda.univ-lyon1.fr/leda/meandata.html  

SELECT v3k, mod0 WHERE (objtype='G') AND (v3k>3000) AND (v3k<30000) AND (mod0 IS NOT NULL) AND (v3k IS NOT NULL)  
  
Consulta:  
http://leda.univ-lyon1.fr/fG.cgi?n=meandata&c=o&of=1,leda,simbad&nra=l&nakd=1&d=v3k%2C%20mod0&sql=(objtype%3D%27G%27)%20AND%20(v3k>3000)%20AND%20(v3k<30000)%20AND%20(mod0%20IS%20NOT%20NULL)%20AND%20(v3k%20IS%20NOT%20NULL)&ob=&a=html  
                                          
</p> 
</details>

 ```Python
import pandas as pd                                                                                      
data= pd.read_csv('C:/Users/Neo/Desktop/leda.csv', delimiter=";")
data
#se quiser refazer a estimativa usando uma amostra aleatória de uns 80% dos dados
#data = data.sample(n = 1133)
 ```
Com esses dados, temos:

VELOCIDADE RADIAL (cz)  
Em relação à radiação CMB 

<details>
<summary>Info</summary>
<p>
https://pt.wikipedia.org/wiki/Velocidade_radial 
</p> 
</details>
  
MÓDULO DA DISTÂNCIA (mod0)  
A diferença entre a magnitude aparente (m) e a magnitude absoluta (M) de um objeto astronômico.

<details>
<summary>Info</summary>
<p>
https://en-m-wikipedia-org.translate.goog/wiki/Luminosity_distance?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc        
</p> 
</details>
  
  
## Medidas e Conversões
  
Agora que temos os dados, podemos realizar os próximos passos, mas nem de longe isso foi trivial.  
Primeiramente temos o módulo da distância (diferença entre a magnitude aparente (m) e a magnitude absoluta (M) de um objeto astronômico = m-M) e não a distância de luminosidade (essa que precisamos)
  
![image](https://user-images.githubusercontent.com/50224653/146567816-d1424f62-018d-4715-a11d-c9479705fa33.png)
  
<details>
<summary>Info</summary>
<p>
https://en-m-wikipedia-org.translate.goog/wiki/Luminosity_distance?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc
</p> 
</details>

```Python
Dl=10**((data['mod0']/5)+1 ) 
```
Entretanto, só isso vai nos dar uma estimativa meio imprecisa, pois essa formula é boa para calcularmos distâncias na nossa galáxia, mas para objetos distantes além da Via Láctea, outros fatores influenciam na medição como a curvatura do espaço-tempo , desvio para o vermelho e dilatação do tempo.  
  
Como não possuo muito conhecimento nesses fatores, vamos só considerar o desvio para o vermelho e o resto vamos desconsiderar.

  
DESVIO PARA O VERMELHO (z)  
Dado que:  
v é a componente radial de velocidade em relação a fonte e o observador.  
c é a velocidade da luz no vácuo (299792458 m/s. Logo, para Quilômetros: 299792.458 km/s).  

![image](https://user-images.githubusercontent.com/50224653/146589455-37590953-56fb-42be-b82a-c5a3c21e05f1.png)  
  
<details>
<summary>Info</summary>
<p>
https://pt.wikipedia.org/wiki/Desvio_para_o_vermelho  
  
https://pt.wikipedia.org/wiki/Velocidade_da_luz
</p> 
</details>

```Python
z = data["v3k"]/299792.458
```

Agora que temos o desvio (z) e a distância de luminosidade (Dl), podemos calcular a Distância de movimento mexendo um pouco na equação.  

DISTÂNCIA DE MOVIMENTO (Dm)  

  ![image](https://user-images.githubusercontent.com/50224653/146571130-dae007c6-5bc4-4252-a7c7-4b2b8669e96c.png)

<details>
<summary>Info</summary>
<p>
https://en-m-wikipedia-org.translate.goog/wiki/Distance_measures_(cosmology)?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=pt-BR  

http://leda.univ-lyon1.fr/leda/param/modz.html
</p> 
</details>
  
```Python
#Se  
#Dl = (1+z)*Dm
#Logo
Dm = Dl/(1+z)
```
Só um último detalhe, a distância está em Parsec (Pc) que é um tipo de distância usada para medir distâncias de objetos astronômicos, logo, precisamos converter isso para Quilômetros (Km).  
1Pc = 30856775812800km  
  
<details>
<summary>Info</summary>
<p>
https://pt.wikipedia.org/wiki/Parsec  
  
https://www.unitconverters.net/length/parsec-to-kilometer.htm
</p> 
</details> 

```Python
Dm = Dm * 30856775812800
```

## Criando a regressão linear

Certo, um rápido resumo sobre regressão linear. Dado que temos duas variáveis y (variável explicada/dependente) e x (variável explicativa/independente) queremos saber o valor esperado de um y dado um x, para explicar essa relação, usamos a equação:  

  ![image](https://user-images.githubusercontent.com/50224653/146581896-7821da91-b809-469a-a837-3934807c6874.png)

Sendo o alfa o coeficiente linear, o beta o coeficiente angular, e o epslion sendo o erro de medição  
 

<details>
<summary>Info</summary>
<p>
https://pt.wikipedia.org/wiki/Regressão_linear
</p> 
</details> 


No nosso caso, queremos explicar a velocidade(y) de uma galáxia dada a sua distância(x), entretanto, sem usar o coeficiente linear (e nem o erro).  
  
Portanto, a equação ficaria:  
  
y = bx  
  
Para quem prestou atenção até aqui, podemos comparar essa equação com a equação de Hubble. Temos quase tudo, menos o coeficiente angular.  
  
```Python
from scipy.optimize import curve_fit
def lin(x, b):
    return b * x
#OBS: y = b*x 
#não possuimos o intercept(coeficiente linear) apenas o slope(coeficiente angular)
coeff, cov= curve_fit(lin,Dm,data["v3k"])
#o melhor slope para a regressão sem intercept:
b = coeff[0]
b 
#2.2404792510504406e-18
```

Agora podemos visualizar a relação entre velocidade e distância das galáxias com a reta calculada.  
  
```Python
import matplotlib.pyplot as plt
import numpy as np

x=np.array(Dm)#Distância
y=np.array(data["v3k"])#Velocidade

#Rode tudo junto#
plt.scatter(x,y)
plt.title('Relação linear entre distância e velocidade')
plt.xlabel('DISTÂNCIA DE MOVIMENTO')
plt.ylabel('VELOCIDADE RADIAL')
f = lambda x: b*x #OBS: y = b*x 
plt.plot(x,f(x), c="red", label="fit line between min and max")
#Rode tudo junto#
```
![image](https://user-images.githubusercontent.com/50224653/146583961-13dd6ad7-9b85-4a0c-b24e-dc4e6baf036f.png)

  
## Conclusão
  
Lei de Hubble  
v   = H0 * d  
onde:  
v – velocidade  
H0 – constante de Hubble  
r – distância  

Podendo ser re-escrita da seguinte forma:  
v   = H0 * d  
1   = (H0 *d)/v  
1/H0 = d/v  

Existe uma relação interessante na fisica entre distância, velocidade e tempo.  
Tempo = Distancia / Velocidade  
t = d/v  
  
<details>
<summary>Info</summary>
<p>
https://pt.wikibooks.org/wiki/Introdução_à_física/Cinemática/Velocidade
</p> 
</details> 


Logo, dada uma linha de regressão simples, se você tiver d e v (definir o intercept para 0), a inclinação será o tempo em segundos.   
Com isso podemos calcular o tempo de existência do universo em segundos, usando a lei de Hubble.  
```Python
#O tempo do UNIVERSO em segundos
Tempo_em_seg = (1/b)
Tempo_em_seg
#4.463330778587455e+17
```
Por fim, para calcularmos quando anos o universo tem, é só convertemos os segundos para minutos, minutos para horas, horas para dias e dias para anos.  
```Python
#A idade do UNIVERSO em anos
ANOS = ((((Tempo_em_seg / 60)/ 60)/ 24)/ 365)
"{:,}".format(int(ANOS))
#14,153,129,054
``` 
 
## Agradecimentos
  
Primeiramente ao Hubble por ter feito isso e muito mais em uma época que certamente era mais complicado sem as ferramentas atuais.
 
Ao Rasmus Groth (bliiir) https://towardsdatascience.com/give-or-take-a-billion-years-32fb9305ca86  
Pois isso tudo é praticamente uma releitura em português do trabalho que ele fez, com algumas adições de explicações e alterações nas conversões.
  
Aos sites http://leda.univ-lyon1.fr/intro.html pelos dados e https://pt.wikipedia.org/wiki/Wikipédia pelas informações.
  
E por ultimo e não menos importante, a você que leu até aqui, muitissimo obrigado!

 

