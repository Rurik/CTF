
#def smethod_0()
# ns2\Class3 private scope

def smethod_0(int_1):
#ns0\Class5 public
    int_0 = 164
    int1 -= string_1
    str = ''
    

"""   
    public static string smethod_0(int int_1)
    {
        int_1 -= int_0;
        if (bool_0)
        {
            string str;
            dictionary_0.TryGetValue(int_1, out str);
            if (str != null)
            {
                return str;
            }
        }
        int count = 0;
        int index = int_1;
        int num3 = byte_0[index++];
        if ((num3 & 0x80) == 0)
        {
            count = num3;
            if (count == 0)
            {
                return string.Empty;
            }
        }
        else if ((num3 & 0x40) == 0)
        {
            count = ((num3 & 0x3f) << 8) + byte_0[index++];
        }
        else
        {
            count = ((((num3 & 0x1f) << 0x18) + (byte_0[index++] << 0x10)) + (byte_0[index++] << 8)) + byte_0[index++];
        }
        try
        {
            byte[] bytes = Convert.FromBase64String(Encoding.UTF8.GetString(byte_0, index, count));
            string str2 = string.Intern(Encoding.UTF8.GetString(bytes, 0, bytes.Length));
            if (bool_0)
            {
                try
                {
                    dictionary_0.Add(int_1, str2);
                }
                catch
                {
                }
            }
            return str2;
        }
        catch
        {
            return null;
        }
    }
}
"""



stream = "{f1cbcfe3-bc9c-4da0-b692-682451d54548}"
count = len(stream)
byte_0 = stream

