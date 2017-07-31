import base64

def multibyte_xor(data, key):
  from itertools import izip, cycle
  return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))


a = ['K7IfRF4nOiNn9Jsqt9wFCq==','vAvack0BPyMQiq0MkChFqq==','NMImwkviE46VACNHafRqVW==','HMzOnqAQZzalVvP0Re7FAa==','7h9+E7q3qS6gGux3htE1pa==','I7BbEdHKp5ArZgPn5Suxcq==','bUYHTdFhKeZdZMvgYbebea==','IEDozaUmrIv6kD4gfNLnxq==','4RQqw/mg9g+SOIptYYdIZW==','xNmQghI+i0lB/V9F48PAOW==','AlmP2PIt40czX9ITxlNjqa==','e8J/2xCbnWoNaC+oeD6Szq==','wmIvyVwp0NB1KKiaAnUmcq==','3lM+l2boxFKD65zzVTr0Jq==','tE2YjaOEdWonZCIZ3PiMta==','2dHPhL1k0gH5YNiuqUId1a==','AZg9+N+B/S4Mm4h/QrVwQq==','r+1Zo40qVIjEZRO0tvm1HG==','QerwgAVqJZUG6/YZeyp3+q==','/+uDpN2cLYn1Ihbo7DXQSG==','fFqAlPA640hD5iw7dNJ0Hq==','9AFKD80WqRsAKixwiWFnka==','V21SGz7jDBbdRSucfNW9fq==','Hp8u+Kw+pkrZNNWcDXELqq==']
b = ['XTd3NiPLZBQ5N1FqkBN+a/Av6SpqBS/K','am0YoDLZYlREsg5Mt62+mZcil2AdEmRK','YWd+ADeGfR3BakQHzJAXZFTf4ZAlkXtJ','0W4AbhlcOkn/1dK0YIk+gUnlb1SOYAl9','UrCmsSbFl/3Y6cA3E1VutOLserwAvc2J','3T6ZsuWmuQxLPqKnGkL2E+6BRHywb1d7','u4ttHuoV/x+3PWygRN1GyMpbZTOzPp8H','3i88vx/KkXyoql1gCbuSl+ZkiqOL7YLi','T9lIAODUMvZyY0ctRuYdVyEx/ZxDzzSc','cXTykqZwtNgVL5WFHAy70tTErxzw3uWV','pDTB6+Z7JNpTRRVToTwOmG2ErRs28iWT','rQcn6anPwJdtAkZoD7lnf3BLKlDzyLHU','dAdNu4hNV0wb+YfadRFTEZ3L+GZB7l0B','IDhmhHqMmmPPGVuz2lGv/7Mu0ufoltku','gixafx52yJd5PkVZUp5hpIJa3uOKFwbU','JvaBlYKIVvSnOXfujitIPR0vbNbZkB8f','pLNpYWVZK/1swUk/Z3E32W4C0Prr+jgJ','eOubcVL40XeQP9L0kZ9u9clahfwJC9fp','/sWKkn+44GJuGP/ZD++wI81PoxEfS+bw','QO1VdWNQ+Hab4rmoI7alWjRiCLbt4FHo','qjXOh+lsJNkPJEB7Absv93dzDuc42yWS','Om+wrRLyl4FU+EAwrwUSwPckIXNJuY3z','6GuESoQHgim3X6zcCbbCz9Paa++WQHRD','0zDMYZhwuzCh9X9cexVem+hsE5rR3vpj']
result = ''
z = base64.b64decode(a[0])
z2 = base64.b64decode(b[0])

for i in range(0, len(a)):
    for j in range(0, len(b)):
        x = base64.b64decode(a[i])
        y = base64.b64decode(b[j])
        print multibyte_xor(y, x)