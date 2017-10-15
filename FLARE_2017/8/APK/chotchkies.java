//
// Decompiled by Procyon v0.5.30
//

package com.flare_on.flair;

import android.os.Bundle;
import android.view.View;
import android.content.DialogInterface$OnClickListener;
import android.app.AlertDialog$Builder;
import java.security.spec.KeySpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.SecretKeyFactory;
import android.content.Context;
import android.content.Intent;
import android.app.Activity;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.BadPaddingException;
import java.security.InvalidKeyException;
import java.security.InvalidAlgorithmParameterException;
import javax.crypto.NoSuchPaddingException;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.io.UnsupportedEncodingException;
import java.security.spec.AlgorithmParameterSpec;
import java.security.Key;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.util.Arrays;
import android.widget.ImageView;
import android.widget.Button;
import android.view.View$OnClickListener;
import android.support.v7.app.AppCompatActivity;

public class Chotchkies extends AppCompatActivity implements View$OnClickListener
{
    private static final int REQUEST_CODE_FLAIR0 = 0;
    private static final int REQUEST_CODE_FLAIR1 = 1;
    private static final int REQUEST_CODE_FLAIR2 = 2;
    private static final int REQUEST_CODE_FLAIR3 = 3;
    private static String[] flairs;
    Button getMoreFlairButton;

    static {
        Chotchkies.flairs = new String[4];
    }

    private void addFlair(final int n, final String s) {
        Chotchkies.flairs[n] = s;
        ImageView imageView = null;
        switch (n) {
            case 0: {
                imageView = (ImageView)this.findViewById(2131427428);
                break;
            }
            case 1: {
                imageView = (ImageView)this.findViewById(2131427430);
                break;
            }
            case 2: {
                imageView = (ImageView)this.findViewById(2131427431);
                break;
            }
            case 3: {
                imageView = (ImageView)this.findViewById(2131427432);
                break;
            }
        }
        this.fadeInFlair(n, imageView);
    }

    private boolean checkFlairs() {
        String allFlairPieces = null;
        try {
            allFlairPieces = Util.getAllFlairPieces(Chotchkies.flairs);
            return Arrays.equals(Util.getSha256Hash(allFlairPieces), new byte[] { 105, 30, -99, -14, 90, -80, 102, 125, -80, 66, -122, -18, 99, 73, 50, -28, -86, 32, -100, 26, 29, 85, 38, -113, 94, -110, -85, 67, -33, -108, -14, -34 });
        }
        catch (IllegalAccessException ex) {
            ex.printStackTrace();
            this.showStanDialog("Well...", "I'm not counting enough flair...");
            return Arrays.equals(Util.getSha256Hash(allFlairPieces), new byte[] { 105, 30, -99, -14, 90, -80, 102, 125, -80, 66, -122, -18, 99, 73, 50, -28, -86, 32, -100, 26, 29, 85, 38, -113, 94, -110, -85, 67, -33, -108, -14, -34 });
        }
    }

    public static String decrypt(final String s) throws UnsupportedEncodingException, InvalidKeySpecException, NoSuchAlgorithmException, NoSuchPaddingException, InvalidAlgorithmParameterException, InvalidKeyException, BadPaddingException, IllegalBlockSizeException {
        final byte[] key = getKey(s);
        final IvParameterSpec ivParameterSpec = new IvParameterSpec("Initech_Security".getBytes("UTF-8"));
        final SecretKeySpec secretKeySpec = new SecretKeySpec(key, "AES");
        final Cipher instance = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        instance.init(2, secretKeySpec, ivParameterSpec);
        return new String(instance.doFinal(new byte[] { -38, 84, 11, -84, 45, -68, 94, -90, -125, 88, -83, -77, -12, -39, -57, 21, 107, -6, -22, 83, 96, 25, 15, 43, 40, -83, -76, -3, 49, 17, 60, 13, -35, 112, -58, -20, 53, -69, 34, -9, 60, 63, -127, 116, -19, 89, 63, -39 }));
    }

    private void fadeInFlair(final int n, final ImageView imageView) {
        this.getMoreFlairButton.setEnabled(false);
        imageView.setAlpha(0.0f);
        imageView.setVisibility(0);
        imageView.animate().alpha(1.0f).setDuration(1500L).withEndAction((Runnable)new Runnable() {
            @Override
            public void run() {
                if (Util.isMissingFlair(Chotchkies.flairs)) {
                    Chotchkies.this.getMoreFlairButton.setEnabled(true);
                    Util.moreFlairMoreHappy(Chotchkies.this, n, Chotchkies.flairs);
                    return;
                }
                if (Chotchkies.this.checkFlairs()) {
                    Chotchkies.this.showMostTerrificFlair();
                    return;
                }
                Chotchkies.this.showStanDialog("Well...", "I'm counting enough flair, but something isn't right here. I think you'll have to start over.");
            }
        });
    }

    private void getFlair(final int n) {
        Intent intent = null;
        switch (n) {
            case 0: {
                intent = new Intent((Context)this, (Class)Michael.class);
                break;
            }
            case 1: {
                intent = new Intent((Context)this, (Class)Brian.class);
                break;
            }
            case 2: {
                intent = new Intent((Context)this, (Class)Milton.class);
                break;
            }
            case 3: {
                intent = new Intent((Context)this, (Class)Printer.class);
                break;
            }
        }
        this.startActivityForResult(intent, n);
    }

    private static byte[] getKey(final String s) throws NoSuchAlgorithmException, UnsupportedEncodingException, InvalidKeySpecException {
        return SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1").generateSecret(new PBEKeySpec(s.toCharArray(), "NoSaltInTheMargarita".getBytes("UTF-8"), 1000, 192)).getEncoded();
    }

    private void getMoreFlair() {
        for (int i = 0; i < Chotchkies.flairs.length; ++i) {
            if (Chotchkies.flairs[i] == null) {
                this.getFlair(i);
                break;
            }
        }
    }

    private void showMostTerrificFlair() {
        try {
            this.showStanDialog("Flair's about the fun!", "Oh yes, I hope this extra piece puts a terrific smile on your face:\n" + decrypt(Util.getAllFlairPieces(Chotchkies.flairs)));
        }
        catch (IllegalAccessException ex) {
            ex.printStackTrace();
            this.showStanDialog("Well...", "I'm not counting enough flair...");
        }
        catch (Exception ex2) {
            ex2.printStackTrace();
            this.showStanDialog("Well...", "I'm counting enough flair, but something isn't right here. I think you'll have to start over.");
        }
    }

    private void showStanDialog(final String title, final String message) {
        final AlertDialog$Builder alertDialog$Builder = new AlertDialog$Builder((Context)this);
        alertDialog$Builder.setIcon(2130837607);
        alertDialog$Builder.setTitle((CharSequence)title);
        alertDialog$Builder.setMessage((CharSequence)message);
        alertDialog$Builder.setPositiveButton((CharSequence)"Great", (DialogInterface$OnClickListener)null);
        alertDialog$Builder.show();
    }

    public void onActivityResult(final int n, final int n2, final Intent intent) {
        super.onActivityResult(n, n2, intent);
        if (n2 == -1) {
            this.addFlair(n, intent.getStringExtra("data"));
        }
        else if (n2 == 0) {
            this.showStanDialog("Look", "People come to Chotchkie's for the atmosphere and the attitude. We want you to express yourself, ok?");
        }
    }

    public void onClick(final View view) {
        switch (view.getId()) {
            default: {}
            case 2131427429: {
                this.getMoreFlair();
            }
        }
    }

    @Override
    protected void onCreate(final Bundle bundle) {
        super.onCreate(bundle);
        this.setContentView(2130968604);
        this.showStanDialog("We need to talk about your flair...", "15 is the minimum, ok? If you think the bare minimum is enough, then ok. But some people choose to wear more and we encourage that, ok?\nYou do want to express yourself, don't you?");
        (this.getMoreFlairButton = (Button)this.findViewById(2131427429)).setOnClickListener((View$OnClickListener)this);
    }
}
