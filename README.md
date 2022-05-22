# UniCEUB-JogoBolinha
Jogo da Bolinha desenvolvido como trabalho final da matéria Lógica de
Programação.

## Planejamento

Esta seção apresenta o planejamento do trabalho.

### Lista de Colaboradores

Lista com nomes das pessoas e nomes de usuário no Github (Nome - Nome de
Usuário).

 - Pedro Brasil - PedroHBrasil
 - Leonardo Paiva - LeonardoPaiv
 - João Vitor - 
 - Silvino - Psnsilvino
 - Pedro Alvares - MasterCabral

### Gerenciamento de Tarefas

As tarefas serão distribuídas na seção
[Issues](https://github.com/PedroHBrasil/UniCEUB-JogoBolinha/issues) do
repositório. Cada issue representa um recurso a ser implementado ou um
bug a ser consertado.

## Orientações para uso do Git

### Commit

Cada commit deve conter um passo da implementação do issue. Pense na
resolução de cada issue como uma sequência de passos. Cada passo é um
commit.

**IMPORTANTE:** Cada commit deve ter o código executável, ou seja, o
código de um commit deve executar sem erros.

### Branches

Cada issue deverá ter uma Branch associada. Todo o desenvolvimento da
resolução do issue deverá ser feito em sua Branch. A Branch *Main*
possui o código oficial e é atualizada apenas quando issues são
finalizados.

### Merges

Ao final da implementação de cada Branch, será feito uma Merge na Branch
*Main*.

## Recursos e Ideias

Recursos e ideias para o jogo.

### Imposto pelo Professor

Os requisitos impostos pelo professor são:

 - [ ] O jogo tem uma bolinha que deve se movimentar verticalmente em
 uma certa velocidade.
 - [ ] O deslocamento horizontal deve ser variado (random).
 - [ ] Usamos as setas direita e esquerda para movimentar a barra
 inferior.
 - [ ] O objetivo do jogador é não deixar a bolinha cair.
 - [ ] A barra deve ser usada como barreira para a bolinha não cair.
 - [ ] A cada batida da bolinha deve ser sorteado o passo horizontal
 dela e também sorteado se o passo será positivo (direita) ou negativo
 (esquerda).
 - [ ] A cada toque da bola na barra deve ser aumentado os pontos em 1
 e então mostrado o placar na parte inferior.
 - [ ] A cada conjunto de “x” pontos deve-se definir o grau de
 dificuldade, ou seja, aumentar o grau de dificuldade, por exemplo
 aumentando a velocidade da bolinha, aumentando o passo lateral
 (direita/esquerda), diminuindo o tamanho da barra, etc.

### Recomendações do Professor

Algumas ideias recomendadas pelo professor foram (não obrigatórias, mas
é bom fazer):

 - [ ] Permitir que tenha “n” bolinhas disponíveis para um jogo, por
 exemplo: três bolinhas/chances para jogar, assim só termina quando o
 jogador deixa cair três bolinhas.
 - [ ] Que o Jogador dê um nome e então ao final de cada “game” seja
 mostrado o nome e a pontuação alcançada.
 - [ ] Que seja especificado um ranking com os três melhores “games”
 com mais pontuação por sessão de execução do programa (não precisa
 guardar em arquivo, só memória ram).
 - [ ] Entre outras possíveis funções ou melhoramentos.

### Ideias dos Membros

Aqui são apresentadas algumas das ideias dos membros do grupo para o
jogo. As ideias devem ser aprovadas ou não por todos e só serão
executadas após finalizarmos a implementação dos requisitos do
professor.

#### Pedro Brasil

 - [ ] **PowerUp:** PowerUp aparece por um tempo na tela e após poucos
 segundos desaparece. Se a bolinha bater no PowerUp, a pontuação é
 multiplicada por 2 por um tempo.
 - [ ] **Menu de Pause:** Opções de reiniciar, finalizar e visualizar
 ranking.

#### Leonardo

 - [ ] **Versus** Ser um jogo de dois jogadores com display horizontal

#### Silvino

 - [ ] **Mudança do Tamanho da Barra:** O tamanho da barra diminui ao marcar um ponto e aumenta ao tomar um ponto, mas não passa do tamanho original
 - [ ] **Botão de Restart:** Botão para nao ter que reiniciar o código sempre que perder