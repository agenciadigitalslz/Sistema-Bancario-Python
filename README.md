# Sistema Bancário em Python

## Projeto do Curso Python Developer - DIO

**Aluno:** André Lopes  
**Professor:** Guilherme de Carvalho

---

## Visão Geral

Este projeto simula um sistema bancário simples em Python, desenvolvido como desafio do curso Python Developer da DIO. O objetivo é praticar conceitos fundamentais da linguagem, como variáveis, funções, controle de fluxo e boas práticas de programação.

O sistema permite ao usuário:
- Consultar saldo e cheque especial
- Realizar saques, inclusive utilizando o limite do cheque especial
- Sair do sistema de forma segura

---

## Versão Inicial (Comum)

O código inicial implementa as funcionalidades básicas de um caixa eletrônico:
- Menu simples com opções de saldo, saque e sair
- Controle de saldo e cheque especial
- Mensagens de feedback ao usuário
- Estrutura sequencial, com algumas funções auxiliares

**Principais características:**
- Uso de variáveis globais para saldo e cheque especial
- Funções para imprimir separadores e mensagens
- Lógica de saque que permite uso do cheque especial
- Repetição do menu até o usuário optar por sair

**Exemplo de uso:**
```python
SALDO = 2000
CHEQUE_ESPECIAL = 1000
# ...
while OPCAO != 0:
    # menu e operações
```

---

## Versão Refatorada

A versão refatorada traz melhorias de organização, legibilidade e robustez:
- Separação clara de funções para cada responsabilidade
- Uso de constantes para opções do menu e valores iniciais
- Tratamento de erros de entrada do usuário (ValueError)
- Funções específicas para consultar saldo, realizar saque e exibir menu
- Variáveis globais controladas de forma mais segura
- Estrutura principal encapsulada na função `main()`

**Principais melhorias:**
- Código mais modular e fácil de manter
- Redução de duplicidade e maior clareza
- Melhor experiência para o usuário, com mensagens de erro amigáveis
- Facilidade para futuras expansões (ex: adicionar depósito, extrato, etc)

**Exemplo de uso:**
```python
SALDO_INICIAL = 2000
CHEQUE_ESPECIAL_INICIAL = 1000
# ...
def main():
    while opcao != OPCAO_SAIR:
        exibir_menu()
        # operações
```

---

## Lições Aprendidas

- Importância de modularizar o código para facilitar manutenção
- Como tratar entradas inválidas do usuário
- Boas práticas de nomeação e organização
- Uso de funções para separar responsabilidades

---

## Como Executar

1. Clone este repositório
2. Execute o arquivo desejado:
   - Versão comum: `python meu_primeiro_programa.py`
   - Versão refatorada: `python meu_primeiro_programa_refatorado.py`

---

## Possíveis Melhorias Futuras

- Adicionar autenticação de usuário
- Implementar depósitos e extrato de operações
- Interface gráfica ou web
- Testes automatizados

---

**Desafio entregue para a DIO por André Lopes, sob orientação do professor Guilherme de Carvalho.**