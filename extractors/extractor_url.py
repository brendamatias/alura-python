import re

class ExtractorUrl:
  def __init__(self, url):
    self.url = self.sanitize_url(url)
    self.validate_url()

  def sanitize_url(self, url):
    if type(url) == str:
      return url.strip()
    else:
      return ""
    
  def validate_url(self):
    if not self.url:
      raise ValueError("A URL está vazia")
    
    regex = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
    match = regex.match(self.url)

    if not match:
      raise ValueError("A URL não é válida")

  def get_url_base(self):
    index_interrogation = self.url.find("?")
    url_base = url[:index_interrogation]

    return url_base

  def get_url_params(self):
    index_interrogation = self.url.find("?")
    url_params = url[index_interrogation+1:]

    return url_params

  def get_value_parameter(self, search_parameter):
    url_params = self.get_url_params()
    index_parameter = url_params.find(search_parameter)
    index_value = index_parameter + len(search_parameter) + 1
    index_e_commercial = url_params.find("&", index_value)

    if index_e_commercial == -1:
      value = url_params[index_value:]
    else:
      value = url_params[index_value:index_e_commercial]

    return value

  def __len__(self):
    return len(self.url)

  def __str__(self):
    return self.url + "\n" + "Parâmetros: " + self.get_url_params() + "\n" + "URL Base: " + self.get_url_base()

  def __eq__(self, other):
    return self.url == other.url


url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

extractor_url = ExtractorUrl(url)
extractor_url2 = ExtractorUrl(url)

print("O tamanho da url é: ", len(extractor_url))
print(extractor_url)
print(extractor_url == extractor_url2)

VALUE_DOLLAR = 5.50
origin_currency = extractor_url.get_value_parameter("moedaOrigem")
target_currency = extractor_url.get_value_parameter("moedaDestino")
qty = extractor_url.get_value_parameter("quantidade")

print("*********************************************")
print("**************CONVERSOR DE MOEDA*************\n")
if origin_currency == "real" and target_currency == "dolar":
  converted_value = int(qty) / VALUE_DOLLAR
  print("O valor de R$ {} reais é igual a $ {} doláres.".format(qty, converted_value))
elif origin_currency == "dolar" and target_currency == "real":
  converted_value = int(qty) * VALUE_DOLLAR
  print("O valor de $ {} doláres é igual a R$ {} reais.".format(qty, converted_value))
else:
  converted_value = int(qty) * VALUE_DOLLAR
  print(f"Câmbio de {origin_currency} para {target_currency} não está disponível.")

print("\n*********************END*********************")
print("*********************************************")