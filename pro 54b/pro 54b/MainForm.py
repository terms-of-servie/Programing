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
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Cyan
        self._button1.Font = System.Drawing.Font("NSimSun", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(673, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(290, 136)
        self._button1.TabIndex = 0
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("NSimSun", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(673, 178)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(290, 160)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Cyan
        self._button3.Font = System.Drawing.Font("NSimSun", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Black
        self._button3.Location = System.Drawing.Point(673, 360)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(290, 164)
        self._button3.TabIndex = 2
        self._button3.Text = "FINE leave :("
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("NSimSun", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Black
        self._label1.Location = System.Drawing.Point(90, 36)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(140, 41)
        self._label1.TabIndex = 3
        self._label1.Text = "radius"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox1.Location = System.Drawing.Point(238, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(185, 20)
        self._textBox1.TabIndex = 4
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("NSimSun", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Black
        self._label2.Location = System.Drawing.Point(118, 381)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(112, 35)
        self._label2.TabIndex = 5
        self._label2.Text = "Area"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("NSimSun", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 178)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(255, 52)
        self._label4.TabIndex = 9
        self._label4.Text = "circumference"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Teal
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(249, 380)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(205, 43)
        self._label3.TabIndex = 10
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Teal
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(249, 178)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(205, 43)
        self._label5.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.ClientSize = System.Drawing.Size(1033, 558)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang54c GUI"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._label3.Text = " "
        self._label5.Text = " "

    def Button1Click(self, sender, e):
        radius = float(self._textBox1.Text) 
        pi = 3.14159 
        area = pi * radius ** 2
        area = round(area, 3)
        circumference = 2 * pi * (radius)
        self._label3.Text = str(area)
        self._label5.Text = str(circumference)
    
    def TextBox1TextChanged(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass