/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.security.Key;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.MessageDigest;
import java.io.UnsupportedEncodingException;
import java.util.Base64;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;




class test_printer
{
    static byte[] drdfg(final String s, final int n) {
        byte[] array = null;
        while (true) {
            try {
                byte[] decode = Base64.getDecoder().decode(s.getBytes("UTF-8"));
                array = new byte[decode.length];
                for (int i = 0; i < decode.length; ++i) {
                    array[i] = (byte)(decode[i] ^ n);
                }
            }
            catch (UnsupportedEncodingException ex) {
                ex.printStackTrace();
                final byte[] decode = array;
                continue;
            }
            break;
        }
        return array;
    }

    static String iemm(final String s) {
        final String vutfs = vutfs("Zcj30d9jroqAN2mtzayVK0awaVTLnoXVcsjl9ujUAd22JiI9xfhqEW1BbkG3LsgQRoStjh+Eb6wTD4BwD9Kypa5ggXfHLWmFjFgERViV+5IRU4RbUPDUwYTivhsdZnA=", 17, "forfor");
        final char[] array = new char[s.length()];
        for (int i = 0; i < s.length(); ++i) {
            array[i] = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".charAt(vutfs.indexOf(s.substring(i, i + 1)));
        }
        return new String(array);
    }

    static byte[] neapucx(final String s) {
        final int length = s.length();
        byte[] array;
        if (length % 2 == 1) {
            array = null;
        }
        else {
            final byte[] array2 = new byte[length / 2];
            int n = 0;
            while (true) {
                array = array2;
                if (n >= length) {
                    break;
                }
                array2[n / 2] = (byte)((Character.digit(s.charAt(n), 16) << 4) + Character.digit(s.charAt(n + 1), 16));
                n += 2;
            }
        }
        return array;
    }

    static byte[] sha1_hash(final byte[] array) throws UnsupportedEncodingException, NoSuchAlgorithmException {
        final MessageDigest instance = MessageDigest.getInstance("SHA-1");
        instance.update(array);
        return instance.digest();
    }

    static String vutfs(String s, int n, String s2) {
        try {
            Cipher instance = Cipher.getInstance("RC4");
            SecretKeySpec secretKeySpec = new SecretKeySpec(s2.getBytes(), "RC4");
            instance.init(Cipher.DECRYPT_MODE, secretKeySpec);
            s = new String(instance.doFinal(drdfg(s, n)));
            return s;
        }
        catch (Exception ex) {
            ex.printStackTrace();
            return null;
        }
    }


    private boolean cgHbC(final String s) {
        try {
            final Object wjpBw = wJPBw("tspe");

            final Class<?> forName = Class.forName("java.util.HashMap");
            final int intValue = (int)forName.getMethod("size", (Class<?>[])null).invoke(wjpBw, (Object[])null);
            final byte[] array = new byte[intValue];
            final Method method = forName.getMethod("get", Object.class);
            for (short n = 0; n < intValue; ++n) {
                array[n] = Byte.class.cast(method.invoke(wjpBw, n));
            }
            return true;
            //return (boolean) Class.forName("java.util.Arrays").getMethod("equals"), byte[].class, byte[].class).invoke(null, Stapler.neapucx(s), Stapler.sha1_hash(array));
            return (boolean) Arrays.equals(Stapler.neapucx(s), Stapler.sha1_hash(array));
        }
        catch (Exception ex) {
            ex.printStackTrace();
            return false;
        }
    }

    private Object wJPBw(final String s) throws Exception {
        final byte[] array = new byte[8];
        int i = 0;
        final Class<?> forName = Class.forName("java.io.DataInputStream");
        final Object instance = forName.getConstructor(Class.forName("java.io.InputStream")).newInstance(Class.forName("android.content.res.AssetManager").getMethod("open", String.class).invoke(this.getAssets(), s));
        final Method method = forName.getMethod("read", byte[].class, Integer.TYPE, Integer.TYPE);
        final Method method2 = forName.getMethod("readInt", (Class<?>[])null);
        method.invoke(instance, array, 0, 8);
        final Class<?> forName2 = Class.forName("java.util.HashMap");
        final Constructor<?> constructor = forName2.getConstructor((Class<?>[])null);
        final Method method3 = forName2.getMethod("put", Object.class, Object.class);
        final Object instance2 = constructor.newInstance(new Object[0]);
        final Method method4 = forName.getMethod("readByte", (Class<?>[])null);
        final int n = Integer.class.cast(method2.invoke(instance, new Object[0])) / 3;
        final Method method5 = forName.getMethod("readShort", (Class<?>[])null);
        while (i < n) {
            method3.invoke(instance2, Short.class.cast(readShort(instance, new Object[0])), readByte(instance, new Object[0]);
            ++i;
        }
        return instance2;
    }



	public static void main (String[] args) throws java.lang.Exception
	{
        String z;
        z = "Gv@H"; // tspe
        z = ",e}e8yGS!8Dev)-e@"; // java.util.HashMap
        z = "vSBH"; // size
        z = "LHG";  // get
        z = "H?ye!v"; // equals
        z = "e.RP9SR8x9.GH.G8M9.GHkG"; // android.content.Context
        z = "LHG1@@!SxeGS9.M9.GHkG"; // getApplicationContext
        z = "LHG1@@!SxeGS9.u.g9"; // getApplicationInfo
        z = "e.RP9SR8x9.GH.G8@d81@@!SxeGS9.u.g9"; // android.content.pm.ApplicationInfo
        z = "g!eLv"; //flags
        z = ",e}e8S98*eGeu.@yG5GPHed"; // java.io.DataInputStream
        z = ",e}e8S98u.@yG5GPHed"; // java.io.InputStream
        z = "e.RP9SR8x9.GH.G8PHv81vvHG-e.eLHP"; // android.content.res.AssetManager
        z = "9@H."; // open
        z = "PHeR"; // read
        z = "PHeRu.G"; // readInt
        z = ",e}e8yGS!8Dev)-e@"; // java.util.HashMap
        z = "@yG"; // put
        z = "PHeR\"(GH"; // readByte
        z = "PHeR5)9PG"; // readShort
        z = ",e}e8yGS!81PPe(v"; // java.util.Arrays

        System.out.println(iemm(z));
        System.out.println("testing");
        System.out.println(vutfs("JP+98sTB4Zt6q8g=", 56, "State")); // A rich man
        System.out.println(vutfs("rh6HkuflHmw5Rw==", 96, "Chile")); // is nothing
        System.out.println(vutfs("+BNtTP/6", 118, "eagle")); // but a
        System.out.println(vutfs("oLLoI7X/jIp2+w==", 33, "wind")); //  (GAVE KEY LENGTH ERROR) -- guessing "poor man"
        System.out.println(vutfs("w/MCnPD68xfjSCE=", 148, "river")); // with money.
        /*System.out.println(vutfs());
        System.out.println(vutfs());
        System.out.println(vutfs());
        System.out.println(vutfs());*/

	}
}
