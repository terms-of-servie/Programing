import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Teal
        self._label1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(301, 74)
        self._label1.TabIndex = 0
        self._label1.Text = "Speed limit"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Teal
        self._label2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 111)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(301, 72)
        self._label2.TabIndex = 1
        self._label2.Text = "Vehicle speed"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Teal
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.OrangeRed
        self._textBox1.Location = System.Drawing.Point(359, 27)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(236, 44)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Teal
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.OrangeRed
        self._textBox2.Location = System.Drawing.Point(359, 126)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(236, 44)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Teal
        self._label3.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(72, 231)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(170, 65)
        self._label3.TabIndex = 4
        self._label3.Text = "Fine"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Teal
        self._label4.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.OrangeRed
        self._label4.Location = System.Drawing.Point(260, 231)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(255, 68)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Turquoise
        self._button1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(13, 345)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(229, 78)
        self._button1.TabIndex = 6
        self._button1.Text = "Cauculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Turquoise
        self._button2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(248, 345)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(193, 78)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Turquoise
        self._button3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Black
        self._button3.Location = System.Drawing.Point(461, 345)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(134, 78)
        self._button3.TabIndex = 8
        self._button3.Text = "LEAVE"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Aquamarine
        self.ClientSize = System.Drawing.Size(607, 454)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pro82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._label4.Text = " "

    def Button1Click(self, sender, e):
        speed = int(self._textBox1.Text)
        vehicle = int(self._textBox2.Text)
        fine = 20 + ((vehicle - speed) * 5)
        self._label4.Text = str(fine)   
