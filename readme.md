# Sistema Bancário Simples em Python
 
Este projeto é um programa simples de sistema bancário desenvolvido em Python, que permite aos usuários realizar operações como depósito, saque, visualização de extrato e saída. 

## Funcionalidades

- **Depósito**: Permite ao usuário depositar um valor positivo na conta.
- **Saque**: Permite ao usuário sacar um valor, desde que respeite o limite de saques diários e o saldo disponível.
- **Extrato**: Exibe um extrato das movimentações feitas (depósitos e saques) e o saldo atual.
- **Saída**: Encerra a execução do programa.

## Regras do Sistema

1. **Depósito**: O valor deve ser maior que 0.
2. **Saque**:
   - O saque não pode exceder o saldo disponível.
   - O saque não pode exceder o limite máximo de R$ 500 por transação.
   - O usuário pode realizar no máximo 3 saques por dia.
3. **Extrato**: Mostra as transações realizadas e o saldo atual da conta.
4. **Limite**: O limite de saque é de R$ 500 e o usuário pode realizar no máximo 3 saques por dia.

## Exemplo de Uso

Ao iniciar o programa, o menu exibirá as seguintes opções:
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair

O usuário pode escolher uma das opções, informando a letra correspondente e seguir as instruções subsequentes para realizar a operação desejada.

### Depósito

Para realizar um depósito, o usuário seleciona a opção `d` e insere o valor a ser depositado. O saldo será atualizado com o novo valor.

### Saque

Para realizar um saque, o usuário seleciona a opção `s`, informa o valor a ser sacado e o sistema verifica se o saldo é suficiente, se o valor não excede o limite de saque, e se o número de saques permitidos já foi atingido.

### Extrato

A opção `e` exibe o extrato de todas as transações realizadas (depósitos e saques), bem como o saldo atual.

### Sair

A opção `q` encerra o programa.

## Requisitos

- Python 3.x

## Como Executar

1. Certifique-se de que você tem o Python instalado em sua máquina.
2. Execute o script `main.py` utilizando o seguinte comando:

```bash
python main.py

```

## Contribuições
Sinta-se à vontade para contribuir com melhorias ao código! Envie um pull request ou reporte problemas.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Este arquivo fornece uma visão geral do projeto, explica suas funcionalidades e orienta os usuários sobre como utilizá-lo.