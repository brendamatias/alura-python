from search_zipcode import SearchAddress

cep = 50610130
search_address = SearchAddress(cep)

print(search_address.get_zipcode())
