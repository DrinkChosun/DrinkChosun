import json

with open('stores/fixtures/stores/address.json', encoding='UTF8') as json_file:
    json_data = json.load(json_file)

stores = []
for idx, dic in enumerate(json_data):
    store = {}
    store['model'] = 'stores.Store'
    store['pk'] = idx
    store['fields'] = {}
    for key, value in dic.items():
        if key in ['store', 'address']:
            store['fields'][key] = value
    stores.append(store)

with open('fixtures/stores/stores.json', 'w', encoding='utf-8') as make_file:
    json.dump(stores, make_file, ensure_ascii=False, indent='\t')

# with open('stores/fixtures/stores/address.json', 'r', encoding='utf-8') as json_file:
#     file = json.load(json_file)
#     print(file)