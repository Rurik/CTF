package com.flare_on.flair;

import android.widget.Button;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import android.widget.EditText;
import android.view.View$OnClickListener;
import android.support.v7.app.AppCompatActivity;

public class Printer extends AppCompatActivity implements View$OnClickListener
{
    EditText gcbbiO;
    private int hti;

    public Printer() {
        this.hti = 0;
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

    private boolean cgHbC(final String s) {
        try {
            if (Retrieve_AppInfo_flags(this)) {
                return false;
            }
            final Object wjpBw = this.wJPBw("tspe"));
            final Class<?> forName = Class.forName("java.util.HashMap"));
            final int intValue = (int)forName.getMethod("size", (Class<?>[])null).invoke(wjpBw, (Object[])null);
            final byte[] array = new byte[intValue];
            final Method method = forName.getMethod("get", Object.class);
            for (short n = 0; n < intValue; ++n) {
                array[n] = Byte.class.cast(method.invoke(wjpBw, n));
            }
            return (boolean)Class.forName("java.util.Arrays").getMethod("equals"), byte[].class, byte[].class).invoke(null, Stapler.neapucx(s), Stapler.sha1_hash(array));
        }
        catch (Exception ex) {
            ex.printStackTrace();
            return false;
        }
    }

    public static boolean Retrieve_AppInfo_flags(Object o) throws Exception {
        final Class<?> forName = Class.forName("android.content.Context");
        o = forName.getMethod("getApplicationContext", (Class<?>[])null).invoke(forName.cast(o), new Object[0]);
        o = forName.getMethod("getApplicationInfo", (Class<?>[])new Class[0]).invoke(o, (Object[])null);
        return (Integer.class.cast(Class.forName("android.content.pm.ApplicationInfo").getField("flags").get(o)) & 0x2) != 0x0;
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
            method3.invoke(instance2, Short.class.cast(method5.invoke(instance, new Object[0])), Byte.class.cast(method4.invoke(instance, new Object[0])));
            ++i;
        }
        return instance2;
    }

    public void onClick(final View view) {
        switch (view.getId()) {
            default: {}
            case 2131427443: {
                final String string = this.gcbbiO.getText().toString();
                if (this.cgHbC(string)) {
                    Util.flairSuccess(this, string);
                    return;
                }
                Util.flairSadness(this, this.hti);
                ++this.hti;
            }
        }
    }

    @Override
    protected void onCreate(final Bundle bundle) {
        super.onCreate(bundle);
        this.setContentView(2130968607);
        ((Button)this.findViewById(2131427443)).setOnClickListener((View$OnClickListener)this);
        this.gcbbiO = (EditText)this.findViewById(2131427444);
    }
}
