from abc import ABC, abstractclssmethod, abstractproperty
from datetime import datetime

#Desafio 01

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adcionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
     
    @property
    def numero(self):
        return self._numero
     
    @property
    def agencia(self):
        return self._agencia
     
    @property
    def cliente(self):
        return self._cliente
     
    @property
    def historico(self):
        return self._historico
         
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        
        if excedeu_saldo:
            print(" Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            print(" Saque realizado com sucesso !!")
            return true
        
        else:
            print(" Operação falhou! Valor inválido!")
    
        return false
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n Depósito realizado com sucesso")
        else:
            print("Operação falhou! O valor informado é inválido.")
            return false
            
        return true
        
class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saques = len(
        [transacao for transacao in self.historico.transacao 
        if transacao["Tipo"] == Saque.__init__]
        )
    
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques 
    
        if excedeu_limite:
            print(" Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print(" Operação falhou! Número máximo de saques excedido.")
    
        else: return super().super(valor)
        
        return false
        
    def __str__(self):
        return f"""\
        Agência: \t{self.agencia}
        C/C: \t{self.numero}
        Titular: \t{self.clinte.nome}
        """
    
class Historico:
    def __init__(self):
       self._transacoes = []
       
    @property
    def transancoes(self):
        return self.transancoes
        
    def adicionar_transacao(self, tran):
        self.transancoes.append(
            {
                "tipo": transacao.__class__.__nome__ ,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%y %H:%M:%s"),
            }
            )       
  
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclssmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
         return self._valor
      
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
         
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
   
class deposito():
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
         return self._valor
     
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def main():
    pass