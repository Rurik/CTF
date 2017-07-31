int __fastcall Java_com_flareon_flare_ValidateActivity_validate(int a1, int a2, int a3)
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
  int var_1BB4; // [sp+4h] [bp-1BB4h]@3
  int v14; // [sp+8h] [bp-1BB0h]@1
  signed int v15; // [sp+Ch] [bp-1BACh]@3
  unsigned int v16; // [sp+10h] [bp-1BA8h]@7
  char dest[92]; // [sp+1Ch] [bp-1B9Ch]@1
  char s; // [sp+78h] [bp-1B40h]@1

  v3 = a1;
  v14 = a3;
  j_j_memset(&s, 0, 6952);
  j_j_memcpy(dest, &off_5004, 92);
  v2 = (const char *)(*(int (__fastcall **)(int, int, _DWORD))(*(_DWORD *)v3 + 676))(v3, v14, 0);
  v1 = v2;
  if ( v2 && j_j_strlen(v2) <= 46 )
  {
    var_1BB4 = 0;
    v15 = 1;
    for ( i = 0; i < j_j_strlen(v1); i += 2 )
    {
      j_j_memset(&s, 0, 6952);
      v4 = 0;
      if ( v1[i] )
      {
        v4 = v1[i];
        if ( v1[i + 1] )
          v4 = (unsigned int)&unk_7E7E >= ((v1[i] << 8) | (unsigned int)v1[i + 1]) ? (v1[i] << 8) | v1[i + 1] : 0;
      }
      v10 = 0;
      do
      {
        v16 = *(_WORD *)((char *)&unk_2214 + v10);
        while ( !(v4 % v16 & 0xFFFF) )
        {
          ++*(_WORD *)(&s + v10);
          v4 = v4 / v16 & 0xFFFF;
          if ( v4 <= 1 )
            goto LABEL_10;
        }
        v10 += 2;
      }
      while ( v10 != 6952 );
LABEL_10:
      if ( j_j_memcmp(*(const void **)&dest[4 * var_1BB4], &s, 3476) )
        v15 = 0;
      else
        ++var_1BB4;
    }
    (*(void (__fastcall **)(int, int, const char *))(*(_DWORD *)v3 + 680))(v3, v14, v1);
    v6 = *(int (__fastcall **)(int, const char *))(*(_DWORD *)v3 + 668);
    v7 = v3;
    if ( var_1BB4 == 23 && v15 )
      v8 = "That's it!";
    else
      v8 = "No!";
  }
  else
  {
    (*(void (__fastcall **)(int, int, const char *))(*(_DWORD *)v3 + 680))(v3, v14, v1);
    v6 = *(int (__fastcall **)(int, const char *))(*(_DWORD *)v3 + 668);
    v7 = v3;
    v8 = "No!";
  }
  return v6(v7, v8);
}