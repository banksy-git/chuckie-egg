import json

syms = json.loads(open("symbols.jsonlike").read().replace("'",'"').replace("L,",",").replace("L}","}"))[0]

for s, v in syms.items():
    print(f"{s:64}: 0x{v:04x}")
