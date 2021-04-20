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

  def print_converted_currency(self, qty):
    dollar_value = 5.56
    return dollar_value * int(qty)

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

origin_currency = extractor_url.get_value_parameter("moedaOrigem")
target_currency = extractor_url.get_value_parameter("moedaDestino")
qty = extractor_url.get_value_parameter("quantidade")

if origin_currency == "real" and target_currency == "dolar":
  print("O valor convertido de dolar para real é: ", extractor_url.print_converted_currency(qty))