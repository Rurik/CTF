data = "\xA1\xB5\x44\x84\x14\xE4\xA1\xB5\xD4\x70\xB4\x91\xB4\x70\xD4\x91\xE4\xC4\x96\xF4\x54\x84\xB5\xC4\x40\x64\x74\x70\xA4\x64\x44"

"""
private void btnDecode_Click(object sender, EventArgs e)
{
    this.pbRoge.Image = Resources.bob_roge;
    byte[] buffer = Resources.dat_secret;
    string str = "";
    for (int i = 0; i < buffer.Length; i++)
    {
        byte num2 = buffer[i];
        str = str + (((num2 >> 4) | ((num2 << 4) & 240)) ^ 0x29);
    }
    str = str + "\0";
    string str2 = "";
    for (int j = 0; j < str.Length; j += 2)
    {
        str2 = str2 + str[j + 1] + str[j];
    }
    string str3 = "";
    for (int k = 0; k < str2.Length; k++)
    {
        char ch1 = str2[k];
        str3 = str3 + ((char) (((byte) str2[k]) ^ 0x66));
    }
    this.lbl_title.Text = str3;
}
"""
str = str2 = str3 = ''
for i in data:
    str += chr( ( (ord(i) >> 4) | (ord(i) << 4) & 240) ^ 0x29)

str += "\x00"
for j in range(0, len(str)-1, 2):
    str2 += str[j+1] + str[j]
    
for k in str2:
    str3 += chr( ord(k) ^ 0x66)
    
    
print(data)
print(str)
print(str2)
print(str3)