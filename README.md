# Volleyball Scoreboard

# Placar de Vôlei

[![EN](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/United-States.png)](#english) [![PT-BR](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Brazil.png)](#português)

## English

### Volleyball Scoreboard

This project implements an interactive scoreboard for volleyball games, developed in Python using the Tkinter library for the graphical interface. The application allows real-time tracking of the scores of two teams, with intuitive keyboard controls: the "E" key decrements the point of the left team and the "D" key decrements the point of the right team, while the left and right arrows increase the points of the respective teams. The interface includes flags of countries or random flags for the teams and keeps the information centered on the screen.

The point counting rules follow the official volleyball rules, with sets up to 25 points (or 15 in the fifth set) and the requirement of a minimum difference of 2 points to finish the set in tie-break situations. Additionally, the application supports automatic side switching of teams at the end of each set and at the eighth point of the fifth set. When a team wins 3 sets, the game is considered over, allowing only point decrements for manual corrections. The layout is responsive, keeping elements centered even when the window is maximized.

## Português

### Placar de Vôlei

Este projeto implementa um placar interativo para jogos de vôlei, desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica. A aplicação permite acompanhar a pontuação de duas equipes em tempo real, com controles intuitivos através do teclado: a tecla "E" decremente o ponto do time à esquerda e a tecla "D" decremente o ponto do time à direita, enquanto as setas esquerda e direita aumentam os pontos dos respectivos times. A interface inclui bandeiras dos países ou bandeiras aleatórias para os times, e mantém as informações centralizadas na tela.

As regras de contagem de pontos seguem as normas oficiais do vôlei, com sets de até 25 pontos (ou 15 no quinto set) e a exigência de uma diferença mínima de 2 pontos para finalizar o set em situações de empate próximo ao fim. Além disso, a aplicação suporta a troca automática de lados dos times ao final de cada set e no oitavo ponto do quinto set. Quando um time vence 3 sets, o jogo é considerado encerrado, permitindo apenas a decrementar pontos para correções manuais. O layout é responsivo, mantendo os elementos centralizados mesmo ao maximizar a janela.
## Estrutura
```
volleyball-scoreboard/
├── main.py
├── __init__.py
├── core.py
├── utils.py
├── data/
│   ├── __init__.py
│   └── loader.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   ├── conf.py
│   └── index.rst
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Como Usar
Run:
```
python main.py
```
