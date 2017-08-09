import base64
for i in range(32,122):
    res = 'QSA' + chr(i) + 'TlY2CNAQQU5EQSAYT1IgUEFOREE='
    try:
        print(base64.b64decode(res), chr(i), res)
        res = 'UEFOREEgUEFOREEgUEFOREEhIEJAU0U2NCBQQU5E' + res
        print(base64.b64decode(res))
    except TypeError:
        continue

# UEFOREEgUEFOREEgUEFOREEhIEJAU0U2NCBQQU5EQSAGTlY2CNAQQU5EQSA
