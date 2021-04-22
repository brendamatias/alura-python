import requests

class SearchAddress:
  def __init__(self, zipcode):
    zipcode = str(zipcode)
    if self.validate_zipcode(zipcode):
      self.zipcode = zipcode
    else:
      raise ValueError("CEP inválido!")
      
  def __str__(self):
    return self.format_zipcode()

  def validate_zipcode(self, zipcode):
    if len(zipcode) == 8:
      return True
    else:
      return False
      
  def format_zipcode(self):
    return "{}-{}".format(self.zipcode[:5], self.zipcode[5:])

  def get_zipcode(self):
    url = "https://viacep.com.br/ws/{}/json".format(self.zipcode)
    r = requests.get(url)
    data = r.json()

    return (
      data['bairro'],
      data['localidade'],
      data['uf']
    )