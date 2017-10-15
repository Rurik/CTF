//
// Decompiled by Procyon v0.5.30
//

package com.flare_on.flair;

import android.widget.Button;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.content.pm.PackageManager$NameNotFoundException;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.EditText;
import android.view.View$OnClickListener;
import android.support.v7.app.AppCompatActivity;

public class Brian extends AppCompatActivity implements View$OnClickListener
{
    EditText q;
    private int tEr;

    private String asdjfnhaxshcvhuw(final TextView textView, final ImageView imageView) {
        final int currentTextColor = textView.getCurrentTextColor();
        final String s = textView.getText().toString().split(" ")[4];
        final String string = imageView.getTag().toString();
        try {
            return this.dfysadf(string,
                                currentTextColor & 0xFFFF,
                                s,
                                this.getApplicationContext().getPackageManager().getApplicationInfo(this.getApplicationContext().getPackageName(), 128).metaData.getString("vdf"));
        }
        catch (PackageManager$NameNotFoundException ex) {
            ex.printStackTrace();
            return null;
        }
    }

    private String dfysadf(final String s, final int n, final String s2, final String s3) {
        return String.format("%s_%s%x_%s!", s, s3, n, s2);
    }

    private boolean memcmp(final String s, final String s2) {
        return s.equals(s2);
    }

    public void onClick(final View view) {
        switch (view.getId()) {
            default: {}
            case 2131427424: {
                final String string = this.q.getText().toString();
                if (this.memcmp(string, this.asdjfnhaxshcvhuw((TextView)this.findViewById(2131427422), (ImageView)this.findViewById(2131427423)))) {
                    Util.flairSuccess(this, string);
                    return;
                }
                Util.flairSadness(this, this.tEr);
                ++this.tEr;
            }
        }
    }

    @Override
    protected void onCreate(final Bundle bundle) {
        super.onCreate(bundle);
        this.setContentView(2130968603);
        ((Button)this.findViewById(2131427424)).setOnClickListener((View$OnClickListener)this);
        this.q = (EditText)this.findViewById(2131427425);
    }
}
