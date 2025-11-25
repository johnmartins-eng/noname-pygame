# Soulstorm (Pygame)

Um jogo de sobrevivência e ação top-down, estilo *roguelite*, desenvolvido com Pygame.

O objetivo é sobreviver a ondas de inimigos (como o **Skeleton**), ganhar experiência, subir de nível e escolher aprimoramentos permanentes e habilidades ativas para se tornar mais forte. O jogo inclui um sistema de login, ranking de pontuações e persistência de dados via SQLite.

## 🌟 Funcionalidades

* **Sistema de Combate e Sobrevivência:** O jogador enfrenta inimigos com ataques automáticos (como o **SimpleAttack**) e habilidades orbitais (como o **Fire Ring**).
* **Evolução e Nível:** Coleta de **Jewels** (XP) para subir de nível e desbloquear a tela de aprimoramentos (**Level Up**).
* **Sistema de Upgrades:** A cada nível, o jogador pode escolher entre opções como aumentar o dano base (**Might I**) ou se curar (**Heal**).
* **Interface e Câmera:** HUD para barras de XP e HP e uma câmera que segue o jogador e é delimitada pelo mapa (**world bounds**).
* **Telas de Navegação:** Implementação de telas de **Login**, **Menu Principal**, **Ranking**, **Pausa** e **Game Over**.
* **Persistência de Dados:** Uso de SQLite para armazenar o nome de usuário e as melhores pontuações.

## 💻 Tecnologias

* **Python**
* **Pygame** (versão `2.6.1`)
* **SQLite** (para banco de dados e ranking)

## 🚀 Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python instalado.

### Passos de Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/johnmartins-eng/soulstorm-pygame
    cd soulstorm-pygame
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: A única dependência é `pygame==2.6.1`)*

3.  **Execute o jogo:**
    ```bash
    python main.py
    ```

## 🎮 Controles

| Ação | Tecla |
| :--- | :--- |
| Mover para cima | `W` |
| Mover para baixo | `S` |
| Mover para a esquerda | `A` |
| Mover para a direita | `D` |
| Pausar o jogo | `ESC` |
