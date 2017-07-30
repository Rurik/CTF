using System;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace RGB
{
    public class frmMain : Form
    {
        private byte[] a = new byte[]
        {
            20,
            22,
            100,
            23,
            21,
            99,
            100,
            103,
            24,
            24,
            25,
            96,
            25,
            103,
            16,
            21,
            16,
            24,
            22,
            17,
            98,
            103,
            103,
            16,
            23,
            18,
            103,
            24,
            17,
            99,
            96,
            18
        };

        private byte[] b = new byte[]
        {
            97,
            93,
            64,
            64,
            75,
            19,
            18,
            107,
            93,
            71,
            18,
            84,
            83,
            91,
            94,
            87,
            86,
            18,
            74,
            98,
            18,
            18,
            102,
            64,
            75,
            18,
            115,
            85,
            83,
            91,
            92,
            19
        };

        private byte[] g = new byte[]
        {
            113,
            96,
            111,
            90,
            77,
            21,
            67,
            88,
            83,
            16,
            79,
            22,
            73,
            126,
            82,
            21,
            88,
            91,
            126,
            89,
            17,
            83,
            16,
            82,
            126,
            21,
            76,
            21,
            91,
            16,
            79,
            70,
            92
        };

        private int c = 137;

        private int d = 50;

        private IContainer components;

        private GroupBox groupBox1;

        private HScrollBar sbB;

        private HScrollBar sbG;

        private HScrollBar sbR;

        private Button btnCheck;

        private Label lblB;

        private Label lblG;

        private Label lblR;

        public frmMain()
        {
            this.InitializeComponent();
        }

        private void sbR_Scroll(object sender, ScrollEventArgs e)
        {
            this.lblR.Text = this.sbR.Value.ToString();
        }

        private void sbG_Scroll(object sender, ScrollEventArgs e)
        {
            this.lblG.Text = this.sbG.Value.ToString();
        }

        private void sbB_Scroll(object sender, ScrollEventArgs e)
        {
            this.lblB.Text = this.sbB.Value.ToString();
        }

        private void btnCheck_Click(object sender, EventArgs e)
        {
            int value = this.sbR.Value;
            int value2 = this.sbG.Value;
            int value3 = this.sbB.Value;
            int num = value2 * value3;
            int num2 = value * 3;
            if (value + num - value2 + value * value * value2 - value3 == value2 * (value3 * 34 + (num2 - value)) + 3744 && value > 60)
            {
                MessageBox.Show(this.szB(value, value2, value3, (byte[])this.g.Clone(), num, num2));
                return;
            }
            MessageBox.Show(this.szA(value, value2, value3, (byte[])this.a.Clone(), num, num2));
        }

        private string szA(int iDummy1, int iDummy2, int iDummy3, byte[] bArrayA, int iDummy4, int iDummy5)
        {
            for (int i = 0; i < bArrayA.Length; i++)
            {
                bArrayA[i] = (byte)((int)this.b[i] ^ this.d);
            }
            return Encoding.ASCII.GetString(bArrayA);
        }

        private string szB(int iDummy1, int iDummy2, int iDummy3, byte[] bArrayA, int iDummy4, int iDummy5)
        {
            for (int i = 0; i < bArrayA.Length; i++)
            {
                int num = i;
                int expr_0E_cp_1 = num;
                bArrayA[expr_0E_cp_1] ^= (byte)(this.c ^ iDummy2);
            }
            return Encoding.ASCII.GetString(bArrayA);
        }

    }
}
