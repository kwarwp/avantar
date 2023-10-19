# avantar.rotgeog.main.py
[valores_RCN]
FOTOGEO = "https://i.imgur.com/QQvvTPK.jpg"
FOTOGEO2 = "https://i.imgur.com/lfe6XNu.jpg"
Perf = "https://imgur.com/L65Nj8p.gif"
Lata = "https://i.imgur.com/VHKOIjw.png"
MapaSat= "https://imgur.com/Fd25qlz.png"
Fura = "https://imgur.com/7zxPaYr.png"

[folha_RCN]
FOTOGEO = [1,1]
FOTOGEO2 = [1,1]

[mapa_ROG]
#cena plano de fundo dim tamanho do quebra cabeça pr é medalha e dif a dificuldade
p_perf = {img=".i.RCN.Perf.4.4", pr=9, foi=".i.ROGzz2zz2.0.0" , texto = "Perfurou!", cena=".i.RCN._FOTOGEO.1", dim=[3,3]}
p_lata = {img=".i.RCN.Lata.4.4", pr=9, foi=".i.ROGzz3zz0.0.0" , texto = "Muito bem!", cena=".i.RCN._FOTOGEO2.1", dim=[2,2]}
p_mapasat = {img=".i.RCN.MapaSat.4.4", pr=9, foi=".i.ROGzz0zz3.0.0" , texto = "Muito bem!", cena=".i.RCN._FOTOGEO2.1", dim=[2,2]}
p_fura = {img=".i.RCN.Fura.4.4", pr=9, foi=".i.ROGzz3zz1.0.0" , texto = "Muito bem!", cena=".i.RCN._FOTOGEO2.1", dim=[2,2]}


Gm0 = {local=[0,1], img="https://imgur.com/sxAm5LA.png", tit="A Antártica esconde uma história geodinâmica incrível sob seu manto de gelo. Sua missão é liderar uma expedição de pesquisa educativa para desenterrar vestígios geológicos profundos e descobrir pistas cruciais sobre a evolução da região e também de outros planetas.", texto="Acabamos de receber uma mensagem da NASA informando que um dos satélites no espaço detectou um objeto no interior de um núcleo de gelo na região antártica. Sua missão é encontrá-lo! Mas antes você precisará fazer algumas escolhas." , foi=".i.ROGzz0zz2.0.0"}

Ant= {local=[3,1], img="https://i.imgur.com/xdHvLM1.gif", tit="Parabéns", texto="Vamos perfurar?", foi=".i.perf"} 

#no lugar do "kl" colocar https://i.imgur.com/Fd25qlz.png


Jarp = {local=[2,2], img="https://imgur.com/VHKOIjw.png", tit="Parabéns", texto="Você encontrou! Essa poeira amarelada é um mineral muito raro em nosso planeta e bem comum em Marte. A descoberta pode ajudar os cientistas a saber mais sobre a importância das gelerias e a formação dos minerais que compõem o Planeta Vermelho. Vamos analisar?", foi=".i.lata"}

Fim= {local=[3,0] , img="https://i.imgur.com/Iqdtgg7.gif", tit="Parabéns", texto="Você conseguiu terminar a missão da Geodinâmica!", foi=".i.ROOTzz0.0.0"}

[mapa_ROG.kl]

local=[0,3]

foi=".i.fura"

tit="Mão na massa!"


[mapa_ROG.kl.texto]

tit="Qual ferramenta você acha ideal para perfurarmos o gelo?"

A="Pá Comum"
B="Broca de Perfuração de Gelo"

Z="B"

[mapa_ROG.kz]
local=[0,2]
foi=".i.mapasat"
tit="Mão na massa!"
# Esta maneira facilita a criação de perguntas onde a pergunta e as opções aparecem em linha diferentes
[mapa_ROG.kz.texto]
tit="Aproximadamente 98% da Antártica está coberta por um manto de gelo, que possui em média 2 km de espessura. Contendo 70% de toda a água doce do planeta. Para ajudar a iniciar a nossa descoberta, o jogador terá que escolher uma ferramenta crucial para ajudar a visualizar as condições das geleiras."
A="Mapa de Rotas "
B="Mapa de Satélite"
Z="B"


#### missao geodinamica gabiiiiii fim
