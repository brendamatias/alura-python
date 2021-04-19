class Account:
  def __init__(self, number, holder, balance, limit):
    self.__number = number
    self.__holder = holder
    self.__balance = balance
    self.__limit = limit

  @staticmethod
  def bank_code()
    return "001"

  @staticmethod
  def bank_codes()
    return { "BB": "001", "Caixa": "104", "Bradesco": "237" }

  def get_balance(self):
    return self.__balance
    
  def get_holder(self):
    return self.__holder
    
  @property
  def limit(self):
    return self.__limit

  @limit.setter
  def limit(self, limit):
    self.__limit = limit
    
  def extract(self):
    print("Saldo de {} do titular {}".format(self.__balance, self.__holder))

  def deposit(self, value):
    self.__balance += value
  
  def __can_withdraw(self, value):
    return value <= (self.__saldo + self.__limit)

  def withdraw(self, value):
    if(self.__can_withdraw(value)):
      self.__balance -= value
    else:
      print("Saldo insuficiente")
  
  def transfer(self, value, destiny):
    self.saca(value)
    destiny.deposita(value)