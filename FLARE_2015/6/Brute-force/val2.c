int __fastcall Java_com_flareon_flare_ValidateActivity_validate(int a1)
{
  int v3; // r5@1
  const char *v2; // r0@1
  const char *v1; // r6@1
  int (__fastcall *v6)(int, const char *); // r3@4
  int v7; // r0@4
  const char *v8; // r1@4
  unsigned int v4; // r4@5
  int v10; // r7@6
  size_t i; // [sp+0h] [bp-1BB8h]@3
  int v13; // [sp+4h] [bp-1BB4h]@3
  int v14; // [sp+8h] [bp-1BB0h]@1
  signed int v15; // [sp+Ch] [bp-1BACh]@3
  unsigned int v16; // [sp+10h] [bp-1BA8h]@7
  char dest[92]; // [sp+1Ch] [bp-1B9Ch]@1
  char s; // [sp+78h] [bp-1B40h]@1

  memset(&s, 0, 6952);
  memcpy(dest, &off_5004, 92);
  v1 = a1;
  if ( v2 && strlen(v2) <= 46 )
  {
    v13 = 0;
    v15 = 1;
    for ( i = 0; i < strlen(email); i += 2 )
    {
      memset(&s, 0, 6952);
      curr_value = 0;
      if ( email[i] )
      {
        curr_value = email[i];
        if ( email[i + 1] )
          curr_value = &unk_7E7E >= ((email[i] << 8) | email[i + 1]) ? (email[i] << 8) | email[i + 1] : 0;
      }
      j = 0;
      do
      {
        test_value = LOWORD((&decoding_table)[j]);
        while ( !(curr_value % test_value & 0xFFFF) )
        {
          ++*(_WORD *)(&s + j); // THIS! RIGHT HERE! DAMMIT!
          curr_value = curr_value / test_value & 0xFFFF;
          if ( (unsigned int)curr_value <= 1 )
            goto LABEL_10;
        }
        j += 2;
      }
      while ( j != 6952 );
LABEL_10:
      if ( memcmp(*(const void **)&dest[4 * v13], &s, 3476) )
        v15 = 0;
      else
        ++v13;
    }
    if ( v13 == 23 && v15 )
      v8 = "That's it!";
    else
      v8 = "No";
  }
  else
  {
    v8 = "No";
  }
}