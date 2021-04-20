import re

address = "Rua das Flores, 72, apto 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-125"
regex = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

search = regex.search(address)

if search:
  zip_code = search.group()

  print(zip_code) 