dict_items = { 1: 'a', 2: 'b' } .items()
inv_dict = lambda d: { v: k for k, v in d }
print(inv_dict(dict_items))