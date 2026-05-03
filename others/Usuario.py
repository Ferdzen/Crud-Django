from Data import Data

class Usuario:
  def __init__(self, nome, sexo, dtNasc, email, renda):
    self.nome = nome
    self.sexo = sexo
    self.dtNasc = dtNasc
    self.email = email
    self.renda = renda

  def getNome(self):
    return self.nome

  def setNome(self, nome):
    self.nome = nome

  def getSexo(self):
    return self.sexo

  def setSexo(self, sexo):
    self.sexo = sexo

  def getDtNasc(self):
    return self.dtNasc

  def setDtNasc(self, dtNasc):
    self.dtNasc = dtNasc
  
  def getEmail(self):
    return self.email
  
  def setEmail(self, email):
    self.email = email
    
  def getRenda(self):
    return self.renda
  
  def setRenda(self, renda):
    self.renda = renda

  def __str__(self):   
    result = f"Nome......: {self.nome}\n" + \
             f"Sexo......: {self.sexo}\n" + \
             f"Nascimento: {self.dtNasc.toString(True)}\n" + \
             f"Email.....: {self.email}\n" + \
             f"Renda.....: {self.renda}\n"

    return(result)
