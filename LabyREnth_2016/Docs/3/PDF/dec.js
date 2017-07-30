

function Iadghod3(s) {
  var v = 0;
  for (var i=0; i<4; i++) v |= s.charCodeAt(i) << i*8;
  return isNaN(v) ? 0 : v;
}

function Vonsheac6(v) {
  var s = String.fromCharCode(v & 0xFF, v>>8 & 0xFF, v>>16 & 0xFF, v>>24 & 0xFF);
  return s;
}

function RevUfPhas2(DepKacyuv7, ClashJit0) {
  var v = new Array(2), k = new Array(4), s = "", i;
  DepKacyuv7 = escape(DepKacyuv7);
  for (var i=0; i<4; i++) k[i] = Iadghod3(ClashJit0.slice(i*4,(i+1)*4));

  for (i=0; i<DepKacyuv7.length; i+=8) {
    v[0] = Iadghod3(DepKacyuv7.slice(i,i+4));
    v[1] = Iadghod3(DepKacyuv7.slice(i+4,i+8));
    TEA_Encrypt(v, k);
    s += Vonsheac6(v[0]) + Vonsheac6(v[1]);
  }
  return s;
}

function jiUteFraj8(tydAcFod3, ClashJit0) {
  var v = new Array(2), k = new Array(4), s = "", i;

  for (var i=0; i<4; i++) k[i] = Iadghod3(ClashJit0.slice(i*4,(i+1)*4));

  for (i=0; i<tydAcFod3.length; i+=8) {
    v[0] = Iadghod3(tydAcFod3.slice(i,i+4));
    v[1] = Iadghod3(tydAcFod3.slice(i+4,i+8));
    TEA_Decrypt(v, k);
    s += Vonsheac6(v[0]) + Vonsheac6(v[1]);
  }
  window.alert(s);
  s = s.replace(/ +$/, '');
  window.alert(s);

  return unescape(s);
}

function TEA_Encrypt(v, k) {

  var y = v[0], z = v[1];
  var delta = 0x9E3779B9, limit = delta*32, sum = 0;

  while (sum != limit) {
    y += (z<<4 ^ z>>>5)+z ^ sum+k[sum & 3];
    sum += delta;
    z += (y<<4 ^ y>>>5)+y ^ sum+k[sum>>>11 & 3];
  }
  v[0] = y; v[1] = z;
}

function TEA_Decrypt(v, k) {
  var y = v[0], z = v[1];
  var delta = 0x9E3779B9, sum = delta*32;

  while (sum != 0) {
    z -= (y<<4 ^ y>>>5)+y ^ sum+k[sum>>>11 & 3];
    sum -= delta;
    y -= (z<<4 ^ z>>>5)+z ^ sum+k[sum & 3];
  }
  v[0] = y; v[1] = z;
}

var asdf = "NuemnaufOmt8wek4obWeashiMeivanJeatt6";
var ddas =  "bodcuicMong2";
var dda22d = "bosOjparj1";
var obGeujRiary = "akPatMyib5EbJetEteip9idWoncainil7";

var atkopNersiv4 = RevUfPhas2(asdf, ddas);
var fakCapFod9 = jiUteFraj8(ddas, obGeujRiary);

var arnUftad4 = 0x41;
ItOvyof7 = ")5512{nn666o8.454#$o\".,n6 5\")~7|%\x106u6x\x16&\x19\"\x10";
var plain = "";
for (i = 0; i < ItOvyof7.length; i+=1){
    plain += String.fromCharCode(ItOvyof7.charCodeAt(i) ^ arnUftad4);
}