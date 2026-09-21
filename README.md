# 🎲 Jogo da Sorte / Game of Luck

Um jogo interativo de adivinhação via terminal (CLI) desenvolvido em Python. O jogador desafia o computador escolhendo um número entre 1 e 5, com suporte nativo a **dois idiomas (Português e Inglês)** e contagem de placar em tempo real.

---

## 🌍 Suporte a Idiomas (Bilingual / i18n)

Logo ao iniciar o jogo, você pode escolher o idioma de sua preferência:
- 🇧🇷 **Português**
- 🇺🇸 **English**

Toda a interface, regras, mensagens de erro e opções se adaptam automaticamente ao idioma escolhido através de um sistema de dicionário centralizado.

---

## 🚀 Funcionalidades

- **Multi-idioma (PT/EN):** Totalmente traduzido para Português e Inglês.
- **Sistema de Placar (Scoreboard):** Acompanhamento contínuo de vitórias do jogador vs. vitórias do computador a cada rodada.
- **Validação Robusta de Entrada:**
  - Não trava se o usuário digitar letras onde deve ser número (`ValueError`).
  - Não quebra se o usuário pressionar apenas `Enter` sem digitar nada (`IndexError`).
  - Garante que a escolha esteja rigorosamente no intervalo de 1 a 5.
- **Animações no Terminal:** Efeito visual de carregamento (`...`) para criar expectativa e suspense.

---

## 📜 Como Jogar / Rules

1. O jogador escolhe um número inteiro entre **1 e 5**.
2. O computador sorteia aleatoriamente um número também entre **1 e 5**.
3. Se os números forem **iguais**, o **jogador vence**! 🎉
4. Se forem **diferentes**, o **computador vence**! 💻
5. O placar é atualizado e você pode escolher se deseja continuar jogando ou encerrar.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python 3.7+**
- `random.randint`: Geração de números pseudoaleatórios.
- `time.sleep`: Temporização e animação de suspense no terminal.
- **Tratamento de Exceções (`try / except`):** Proteção contra entradas inválidas de dados.
- **Dicionários de Internacionalização (i18n):** Código limpo seguindo o princípio **DRY** (*Don't Repeat Yourself*), evitando repetição de lógica.

---

## 💻 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/dgduarte/jogo-da-sorte.git
