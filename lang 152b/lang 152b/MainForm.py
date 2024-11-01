import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Maroon
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button1.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Salmon
        self._button1.Location = System.Drawing.Point(1, 323)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(128, 64)
        self._button1.TabIndex = 0
        self._button1.Text = "CALC"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Maroon
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button2.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Salmon
        self._button2.Location = System.Drawing.Point(135, 323)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(120, 64)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Maroon
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button3.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Salmon
        self._button3.Location = System.Drawing.Point(261, 323)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(120, 64)
        self._button3.TabIndex = 2
        self._button3.Text = "LEAVE NOW"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Maroon
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox1.Location = System.Drawing.Point(193, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(164, 20)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Red
        self._label1.Font = System.Drawing.Font("MS Gothic", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(24, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(151, 23)
        self._label1.TabIndex = 4
        self._label1.Text = "Input"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.Firebrick
        self._listBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._listBox1.Font = System.Drawing.Font("MS Gothic", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(68, 66)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(246, 249)
        self._listBox1.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkRed
        self.ClientSize = System.Drawing.Size(385, 390)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "lang 152b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        pass