import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
                    self._textBox1 = System.Windows.Forms.TextBox()
                    self._label1 = System.Windows.Forms.Label()
                    self._textBox2 = System.Windows.Forms.TextBox()
                    self._button2 = System.Windows.Forms.Button()
                    self._button3 = System.Windows.Forms.Button()
                    self._label2 = System.Windows.Forms.Label()
                    self._label3 = System.Windows.Forms.Label()
                    self._label4 = System.Windows.Forms.Label()
                    self._button1 = System.Windows.Forms.Button()
                    self.SuspendLayout()
                    # 
                    # textBox1
                    # 
                    self._textBox1.BackColor = System.Drawing.Color.DarkRed
                    self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                    self._textBox1.Location = System.Drawing.Point(271, 34)
                    self._textBox1.Name = "textBox1"
                    self._textBox1.Size = System.Drawing.Size(205, 30)
                    self._textBox1.TabIndex = 0
                    # 
                    # label1
                    # 
                    self._label1.BackColor = System.Drawing.Color.LawnGreen
                    self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
                    self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                    self._label1.Location = System.Drawing.Point(280, 304)
                    self._label1.Name = "label1"
                    self._label1.Size = System.Drawing.Size(196, 125)
                    self._label1.TabIndex = 3
                    self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
                    # 
                    # textBox2
                    # 
                    self._textBox2.BackColor = System.Drawing.Color.DarkRed
                    self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                    self._textBox2.Location = System.Drawing.Point(271, 116)
                    self._textBox2.Name = "textBox2"
                    self._textBox2.Size = System.Drawing.Size(205, 30)
                    self._textBox2.TabIndex = 4
                    # 
                    # button2
                    # 
                    self._button2.BackColor = System.Drawing.Color.Salmon
                    self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                    self._button2.ForeColor = System.Drawing.Color.OliveDrab
                    self._button2.Location = System.Drawing.Point(193, 171)
                    self._button2.Name = "button2"
                    self._button2.Size = System.Drawing.Size(149, 97)
                    self._button2.TabIndex = 5
                    self._button2.Text = "Clear"
                    self._button2.UseVisualStyleBackColor = False
                    self._button2.Click += self.Button2Click
                    # 
                    # button3
                    # 
                    self._button3.BackColor = System.Drawing.Color.Salmon
                    self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
                    self._button3.ForeColor = System.Drawing.Color.OliveDrab
                    self._button3.Location = System.Drawing.Point(360, 171)
                    self._button3.Name = "button3"
                    self._button3.Size = System.Drawing.Size(136, 97)
                    self._button3.TabIndex = 6
                    self._button3.Text = "Exit"
                    self._button3.UseVisualStyleBackColor = False
                    self._button3.Click += self.Button3Click
                    # 
                    # label2
                    # 
                    self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
                    self._label2.Location = System.Drawing.Point(122, 20)
                    self._label2.Name = "label2"
                    self._label2.Size = System.Drawing.Size(119, 62)
                    self._label2.TabIndex = 7
                    self._label2.Text = "Guests:"
                    self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
                    # 
                    # label3
                    # 
                    self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
                    self._label3.Location = System.Drawing.Point(114, 96)
                    self._label3.Name = "label3"
                    self._label3.Size = System.Drawing.Size(127, 65)
                    self._label3.TabIndex = 8
                    self._label3.Text = "Chairs:"
                    self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
                    # 
                    # label4
                    # 
                    self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
                    self._label4.Location = System.Drawing.Point(24, 319)
                    self._label4.Name = "label4"
                    self._label4.Size = System.Drawing.Size(217, 104)
                    self._label4.TabIndex = 9
                    self._label4.Text = "Permutations:"
                    self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
                    # 
                    # button1
                    # 
                    self._button1.BackColor = System.Drawing.Color.Salmon
                    self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                    self._button1.ForeColor = System.Drawing.Color.OliveDrab
                    self._button1.Location = System.Drawing.Point(12, 171)
                    self._button1.Name = "button1"
                    self._button1.Size = System.Drawing.Size(159, 97)
                    self._button1.TabIndex = 10
                    self._button1.Text = "Calculate"
                    self._button1.UseVisualStyleBackColor = False
                    self._button1.Click += self.Button1Click
                    # 
                    # MainForm
                    # 
                    self.BackColor = System.Drawing.Color.YellowGreen
                    self.ClientSize = System.Drawing.Size(521, 438)
                    self.Controls.Add(self._button1)
                    self.Controls.Add(self._label4)
                    self.Controls.Add(self._label3)
                    self.Controls.Add(self._label2)
                    self.Controls.Add(self._button3)
                    self.Controls.Add(self._button2)
                    self.Controls.Add(self._label1)
                    self.Controls.Add(self._textBox2)
                    self.Controls.Add(self._textBox1)
                    self.Name = "MainForm"
                    self.Text = "Lang162h"
                    self.Load += self.MainFormLoad
                    self.ResumeLayout(False)
                    self.PerformLayout()


    def Button1Click(self, sender, e):
        guests = int(self._textBox1.Text)
        chairs = int(self._textBox2.Text)
        arrangements = 1
        while chairs > 0:
            arrangements = arrangements * guests
            guests = guests - 1
            chairs = chairs - 1
        self._label1.Text = str(arrangements)

    def MainFormLoad(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._label1.Text = " "
        self._textBox1.Text = " " 
        self._textBox2.Text = " " 

    def Button3Click(self, sender, e):
        Application.Exit()
