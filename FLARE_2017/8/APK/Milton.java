package com.flare_on.flair;

import android.widget.RatingBar$OnRatingBarChangeListener;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import java.security.NoSuchAlgorithmException;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import android.content.Context;
import android.widget.RatingBar;
import android.widget.Button;
import android.widget.EditText;
import android.view.View$OnClickListener;
import android.support.v7.app.AppCompatActivity;

public class Milton extends AppCompatActivity implements View$OnClickListener
{
    private String hild;
    EditText pexu;
    Button r;
    RatingBar rb;
    private int rtgb;

    public Milton() {
        this.hild = "";
        this.rtgb = 0;
    }

    private boolean breop(final String s) {
        if (trsbd((Context)this)) {
            return false;
        }
        final byte[] neapucx = Stapler.neapucx(s);
        try {
            return Arrays.equals(neapucx, this.nbsadf());
        }
        catch (UnsupportedEncodingException ex) {
            ex.printStackTrace();
            return false;
        }
        catch (NoSuchAlgorithmException ex2) {
            ex2.printStackTrace();
            return false;
        }
    }

    private byte[] nbsadf() throws UnsupportedEncodingException, NoSuchAlgorithmException {
        return Stapler.sha1_hash(this.hild.getBytes("UTF-8"));
    }

    public static boolean trsbd(final Context context) {
        return (context.getApplicationContext().getApplicationInfo().flags & 0x2) != 0x0;
    }

    private void vbdrt() {
        this.hild = "";
        this.r.setEnabled(false);
        this.rb.setRating(0.0f);
        this.rb.setEnabled(true);
    }

    public void onClick(final View view) {
        switch (view.getId()) {
            default: {}
            case 2131427439: {
                final String string = this.pexu.getText().toString();
                if (this.breop(string)) {
                    Util.flairSuccess(this, string);
                    return;
                }
                this.vbdrt();
                Util.flairSadness(this, this.rtgb);
                ++this.rtgb;
            }
        }
    }

    @Override
    protected void onCreate(final Bundle bundle) {
        super.onCreate(bundle);
        this.setContentView(2130968606);
        (this.r = (Button)this.findViewById(2131427439)).setOnClickListener((View$OnClickListener)this);
        (this.rb = (RatingBar)this.findViewById(2131427440)).setOnRatingBarChangeListener((RatingBar$OnRatingBarChangeListener)new Uvasdf());
        this.pexu = (EditText)this.findViewById(2131427435);
    }

    public class Uvasdf implements RatingBar$OnRatingBarChangeListener
    {
        public void onRatingChanged(final RatingBar ratingBar, final float n, final boolean b) {
            if (b) {
                if (n == 4.0) {
                    Milton.this.hild += Stapler.vutfs("JP+98sTB4Zt6q8g=", 56, "State");
                    Milton.this.hild += Stapler.vutfs("rh6HkuflHmw5Rw==", 96, "Chile");
                    Milton.this.hild += Stapler.vutfs("+BNtTP/6", 118, "eagle");
                    Milton.this.hild += Stapler.vutfs("oLLoI7X/jIp2+w==", 33, "wind");
                    Milton.this.hild += Stapler.vutfs("w/MCnPD68xfjSCE=", 148, "river");
                    Milton.this.r.(true);
                }
                ratingBar.setEnabled(false);
            }
        }
    }
}
