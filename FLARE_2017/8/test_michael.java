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



class test_michael
{
    static boolean checkPassword(final String s) {
        boolean b;
        if (s.isEmpty() || s.length() != 12) {
            b = false;
        }
        else {
            b = true;
            if (!s.startsWith("M")) {
                b = false;
            }
            if (s.indexOf(89) != 1) {
                b = false;
            }
            if (!s.substring(2, 5).equals("PRS")) {
                b = false;
            }
            if (s.codePointAt(5) != 72 || s.codePointAt(6) != 69) {
                b = false;
            }
            if (s.charAt(7) != s.charAt(8) || s.substring(7, 9).hashCode() != 3040) {
                b = false;
            }
            if (s.indexOf("FT") != 9) {
                b = false;
            }
            if (s.lastIndexOf(87) != s.length() - 1) {
                return false;
            }
        }
        return b;
    }
//012345678912
//MYPRSHE__FTW


    public static void crack_hashcode (String[] args) throws java.lang.Exception
    // returns __
    {
        boolean result;
        for (int i = 48; i < 90; i++) {
            for (int j = 48; j < 90; j++) {
                String test = "" + (char) i + "" + (char) j;
                System.out.println(test.hashCode());
                if (test.hashCode() == 3040) {
                    System.out.println(test);
                }
            }
        }
    }

	public static void main (String[] args) throws java.lang.Exception
	{
    boolean result;
    for (int i = 48; i < 125; i++) {
        for (int j = 48; j < 125; j++) {
            for (int k = 48; k < 90; k++) {
                    for (int l = 48; l < 90; l++) {
                        String bruteword = "M" + (char) i + "PRSHE__" + (char) j + (char) k + (char) l;
                        result = checkPassword(bruteword);
                        if (result)
                            {
                                System.out.println(bruteword);
                            }
                    }
                }
            }
        }
    }
}
