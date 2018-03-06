# Programação com Interfaçes Graficas

## - AD1:
    - O objetivo deste trabalho é escrever um programa em Python para simular um ecosistema que consiste de ursos e peixes, vivendo em um rio. A simulação prossegue em ciclos, nos quais os animais envelhecem, um suconjunto deles vai para outros locais, outros se acasalam e alguns morrem, de acordo com certas regras.
  
    - As regras para movimentação são as seguintes:
        1. Se a celula para a qual o animal se mover estiver vazia, o animal é simplesmente movido para a nova celula.
        
        2. Se um urso ou um peixe colidirem, o peixe morre, a despeito do gênero do animal.
        
        3. Se dois animais da mesma espécie e gênero colidirem na mesma célula, então:
            a. Se forem peixes, eles ficam onde estiverem, e nada acontece.
            b. Se forem ursos do mesmo gênero e de mesma força, eles ficam onde estiverem, e nada acontece.
            c. Se animais do mesmo gênero e forças distintas colidirem, o mais fraco morre.
        
        4. Se animais do mesmo tipo, mas de sexos opostos, estiverem para colidir na mesma célula, eles ficam onde estiverem, mas é criada uma nova instância deste tipo de animal, que será colocada numa célula aleatória vazia (previamente nula) da lista. Se a lista estiver cheia, nenhum animal é criado.
