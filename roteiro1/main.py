# avantar.roteiro1.main.py
[valores_RT1]
PinCb= "bkIybVD dL9KpOc qir7Ntk 95qNIJk ZlQyxEP gHghRUz"


[mapa_RO1]
p_bote = {img=".i.PUZZLE.AdvBo0.4.4", pr=1, foi=".i.ROOTzz0.0.0" , texto = "Conseguiu embarcar no bote!", cena=".i.CN._RO1.4", dim=[4,4]}
p_esta = {img=".i.PUZZLE.AdvSta.4.4", pr=11, foi=".i.ROOTzz0.0.0" , texto = "Chegou na Estação!", cena=".i.CN._RO1.6", dim=[4,4]}
p_mar = {img=".i.PUZZLE.KpaMar.4.4", pr=13, foi=".i.ROOTzz0.0.0" , texto = "Atravessou o mar!", cena=".i.CN._RO1.14", dim=[6,5]}
p_mon = {img=".i.PUZZLE.KpaMon.4.4", pr=12, foi=".i.ROOTzz0.0.0" , texto = "Observou uma montanha!", cena=".i.CN._RO1.8", dim=[5,4]}
e_fer = {img="https://imgur.com/hOgrOJ5.png", foi=".i.ROOTzz0.0.0", put=1, x=200, y=200, tit="px",texto="Você encontrou um peixe!", cena=".i.RO1zz8zz0.1.3"}
u_pin = {img=".i.RT1.PinCb.4.4", pr=16, foi=".i.ROOTzz0.0.0" , texto = "Observou a fauna!", cena=".i.CN._RO1.4", dim=[2,1]}

Jb = {local=[3,0], tit="Vamos desembarcar do navio", texto="Desembarcar!", foi=".i.bote"}
Jk = {local=[3,2], img=".i.Missao._DANIELP.1" tit="Observar", texto="Observação da Fauna", foi=".i.pin"}
Je = {local=[2,1], tit="Vamos até a estação", texto="Estação!", foi=".i.esta"}
# No texto podemos usar entre chaves a formulação de uma pergunta. O tit é a pergunta, A, B etc são as opções e Z é a resposta certa
kt = {local=[0,1], tit="Converse comigo!", texto= {tit="Você sabia que a temperatura aqui chega a", A="40º", B="-150º", C="-90º", Z="C" }, foi=".i.esta"}
# Em vez do formato xx = {local=... pode usar esta notação entre colchetes. cada um dos termos vai aparecer em uma linha nova
[mapa_RO1.ko]
local=[1,2]
foi=".i.mar"
tit="Vamos falar sobre Clima!"
# Esta maneira facilita a criação de perguntas onde a pergunta e as opções aparecem em linha diferentes
[mapa_RO1.ko.texto]
tit="Algo que está ameaçando a Antártida é a Ebulição global. Sabe, é"
A="O processo acelerado do aquecimento global."
B="A mudança do estado líquido para o gasoso."
C="O processo de condensação de vapores no ar."
Z="A"
[mapa_RO1.km]
local=[2,3]
foi=".i.mon"
tit="Vamos falar sobre a Ebulição Global!"
[mapa_RO1.km.texto]
tit="A Ebulição global vai afetar a Antártida. Vai terminar por"
A="Estimular o turismo predatório."
B="Descongelar as Geleiras."
C="Acelerar o crescimento de novas espécies."
Z="B"
[mapa_RO1.kf]
local=[7,1]
img=".i.Missao._FIGURAS.0"
tit="Vamos falar sobre Clima!"
foi=".i.YELzz1zz1.0.0"
[mapa_RO1.kf.texto]
tit="Estou preocupado com o descongelamento das geleiras. O efeito no planeta Terra será "
A="Emissão de gases"
B="Elevação do nível do mar"
C="Congelamento da camada de ozônio"
Z="B"
cube
https://i.imgur.com/bkIybVD.jpg
https://i.imgur.com/dL9KpOc.jpg
https://i.imgur.com/qir7Ntk.jpg
https://i.imgur.com/95qNIJk.jpg
https://i.imgur.com/ZlQyxEP.jpg
https://i.imgur.com/gHghRUz.jpg