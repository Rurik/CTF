
//
// Decompiled by Procyon v0.5.30
//

package com.flare_on.flair;

import android.widget.Button;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.widget.EditText;
import android.view.View$OnClickListener;
import android.support.v7.app.AppCompatActivity;

public class Michael extends AppCompatActivity implements View$OnClickListener
{
    private static final int PW_LENGTH = 12;
    private int failCount;
    private EditText password;

    public Michael() {
        this.failCount = 0;
    }

    private boolean checkPassword(final String s) {
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

    public void onClick(final View view) {
        switch (view.getId()) {
            default: {}
            case 2131427436: {
                final String string = this.password.getText().toString();
                if (this.checkPassword(string)) {
                    Util.flairSuccess(this, string);
                    return;
                }
                Util.flairSadness(this, this.failCount);
                ++this.failCount;
            }
        }
    }

    @Override
    protected void onCreate(final Bundle bundle) {
        super.onCreate(bundle);
        this.setContentView(2130968605);
        ((Button)this.findViewById(2131427436)).setOnClickListener((View$OnClickListener)this);
        this.password = (EditText)this.findViewById(2131427435);
    }
}
