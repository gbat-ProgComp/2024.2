# Texto fornecido
lirio = '''Procurar a nossa felicidade através da felicidade dos outros - aconselhava Olívia noutra carta sem data.
- Não estou pregando o ascetismo, a santidade, não estou elogiando o puro espírito de sacrifício e renúncia.
Tudo isso seria inumano, significaria ainda uma fuga da vida. Mas o que procuro, o que desejo, é segurar a vida
pelos ombros e estreitá-la contra o peito, beijá-la na face. Vida, entretanto, não é o ambiente em que te achas.
As maneiras estudadas, as frases convencionais, o excesso de conforto, os perfumes caros e a preocupação do
dinheiro são apenas uma péssima contrafação da vida. Buscar a poesia da vida será coisa que tenha nexo?
Ele agora vivia...Tinha tido apenas a ilusão de viver, mas na verdade andara morto por entre os homens.
O dia mais importante da minha vida foi aquele em que, recordando todos os meus erros, achei que já chegara
a hora de procurar uma nova maneira de ser útil ao próximo, de dar novo rumo às minhas relações humanas.
Que era que eu tinha feito senão satisfazer os meus desejos, o meu egoísmo? Podia ser considerada uma
criatura boa apenas porque não matava, porque não roubava, porque não agredia? A bondade não deve ser
uma virtude passiva. No dia em que eu achei Deus, encontrei a paz para mim e ao mesmo tempo percebi que
de certa maneira não haveria paz para mim. Descobri que a paz interior só se conquista com o sacrifício da paz
exterior. Era preciso fazer alguma coisa pelos outros. O Mundo está cheio de sofrimento, de gritos de socorro.
Que tinha eu feito até então para diminuir esse sofrimento, para atender a esses apelos? Eu via em meu redor
pessoas aflitas que, para se salvarem, esperavam apenas a mão que as apoiasse, nada mais que isso. E Deus
dera-me duas mãos. Pensei tudo isso numa noite de insônia. Quando o dia nasceu, senti que tinha nascido de
novo com ele. Era uma mulher nova.'''

# Converte o texto para maiúsculas e remove pontuações
lirio = lirio.upper()
lirio = lirio.replace(".", "")
lirio = lirio.replace(",", "")
lirio = lirio.replace("?", "")
lirio = lirio.replace("!", "")
lirio = lirio.replace(":", "")
lirio = lirio.replace(";", "")
lirio = lirio.replace("(", "")
lirio = lirio.replace(")", "")

# Divide o texto em palavras individuais
palavras = lirio.split()

# Cria um dicionário para contar as ocorrências de cada palavra
contador_palavras = {}
for palavra in palavras:
    if palavra in contador_palavras:
        contador_palavras[palavra] += 1
    else:
        contador_palavras[palavra] = 1



# Ordena a lista de tuplas pelo contador (de maior para menor) e pela palavra (alfabeticamente) em caso de empate
ranking_palavras_ordenadas = sorted(contador_palavras.items(), key=lambda item: -item[1])

# Exibe o ranking das palavras

print("O ranking das palavras é:")
for palavra, contador in ranking_palavras_ordenadas[:5]:
    print(f"{palavra}: {contador}")