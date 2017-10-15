import base64
from Crypto.Cipher import ARC4
import codecs
'''
static String RC4_B64_Xor(String s, final int n, final String s2) {
        try {
            final SecretKeySpec secretKeySpec = new SecretKeySpec(s2.getBytes(), new String('ARC4', "UTF-8"));
            final Cipher instance = Cipher.getInstance(new String('ARC4', "UTF-8"));
            instance.init(2, secretKeySpec);
            s = new String(instance.doFinal(B64D_and_xor(s, n)), "UTF-8");
            return s;
        }
        catch (Exception ex) {
            ex.printStackTrace();
            return null;
        }
    }
}

    static String iemm(final String s) {
        final String RC4_B64_Xor = RC4_B64_Xor("Zcj30d9jroqAN2mtzayVK0awaVTLnoXVcsjl9ujUAd22JiI9xfhqEW1BbkG3LsgQRoStjh+Eb6wTD4BwD9Kypa5ggXfHLWmFjFgERViV+5IRU4RbUPDUwYTivhsdZnA=", 17, "for");
        final char[] array = new char[s.length()];
        for (int i = 0; i < s.length(); ++i) {
            array[i] = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".charAt(RC4_B64_Xor.indexOf(s.substring(i, i + 1)));
        }
        return new String(array);
    }
'''

def X(s, key):
    result = ''
    a = base64.b64decode(s)
    for i in range(len(a)):
        result += chr (ord(a[i]) ^ key)
    return result

def Z(s):
    result = ''
    for i in range(len(s)):
        result +=
            array[i] = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".charAt(RC4_B64_Xor.indexOf(s.substring(i, i + 1)));
        }


def rc4(s, key):
     cipher = ARC4.new(key)
     return cipher.decrypt(s)

test = b"U2FsdGVkX1/C4nAT9tFB2W/KjqwAYotw9Zo="
real = b"Zcj30d9jroqAN2mtzayVK0awaVTLnoXVcsjl9ujUAd22JiI9xfhqEW1BbkG3LsgQRoStjh+Eb6wTD4BwD9Kypa5ggXfHLWmFjFgERViV+5IRU4RbUPDUwYTivhsdZnA="
z = X(real, 17)
print(z)
print(base64.b64encode(z))
y = rc4(z, b'for')
print(y)
print(base64.b64encode(y))
#print(X('BBcGcQ==', 69))

print('------')
print(codecs.encode(z, 'hex_codec'))
