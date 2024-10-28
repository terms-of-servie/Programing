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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Chartreuse
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Onyx", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.DimGray
        self._button1.Location = System.Drawing.Point(12, 371)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(150, 73)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculator"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Orchid
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Segoe Fluent Icons", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Maroon
        self._button2.Location = System.Drawing.Point(168, 371)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(150, 73)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkOrange
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("NSimSun", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.SaddleBrown
        self._button3.Location = System.Drawing.Point(324, 371)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(150, 73)
        self._button3.TabIndex = 2
        self._button3.Text = "LEAVE"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkTurquoise
        self._label1.Font = System.Drawing.Font("Papyrus", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(112, 242)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(272, 97)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(131, 187)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(326, 20)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(131, 89)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(326, 20)
        self._textBox2.TabIndex = 5
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Teal
        self._label2.Font = System.Drawing.Font("Segoe UI", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.SeaShell
        self._label2.Location = System.Drawing.Point(12, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 6
        self._label2.Text = "Speed"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightSteelBlue
        self._label3.Font = System.Drawing.Font("Yu Gothic", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.LemonChiffon
        self._label3.Location = System.Drawing.Point(12, 184)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 7
        self._label3.Text = "Speed Limit"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumSpringGreen
        self.ClientSize = System.Drawing.Size(478, 448)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "lang 82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""

    def Button1Click(self, sender, e):
        speed = int(self._textBox2.Text)
        limit = int (self._textBox1.Text)
        fine = 20 + ((limit - speed) * 5)
        self._label1.Text = ""
        
    def Button3Click(self, sender, e):
        Application.Exit()