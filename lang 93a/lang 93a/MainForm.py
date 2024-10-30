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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkOrange
        self._label1.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.SaddleBrown
        self._label1.Location = System.Drawing.Point(13, 26)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(382, 66)
        self._label1.TabIndex = 0
        self._label1.Text = "Kilowatts Used"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkOrange
        self._label2.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.SaddleBrown
        self._label2.Location = System.Drawing.Point(12, 121)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(389, 66)
        self._label2.TabIndex = 1
        self._label2.Text = "Base Rate"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkOrange
        self._label3.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.SaddleBrown
        self._label3.Location = System.Drawing.Point(13, 206)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(389, 66)
        self._label3.TabIndex = 2
        self._label3.Text = "Surcharge"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkOrange
        self._label4.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.SaddleBrown
        self._label4.Location = System.Drawing.Point(13, 290)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(389, 66)
        self._label4.TabIndex = 3
        self._label4.Text = "Citytax"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkOrange
        self._label5.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.SaddleBrown
        self._label5.Location = System.Drawing.Point(10, 385)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(389, 66)
        self._label5.TabIndex = 4
        self._label5.Text = "Pay this amount"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DarkOrange
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.SaddleBrown
        self._label6.Location = System.Drawing.Point(10, 480)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(390, 66)
        self._label6.TabIndex = 5
        self._label6.Text = "After May 20th pay"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label6.Click += self.Label6Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSlateGray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.DarkSalmon
        self._button1.Location = System.Drawing.Point(12, 576)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(332, 93)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSlateGray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.DarkSalmon
        self._button2.Location = System.Drawing.Point(366, 576)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(244, 93)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSlateGray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.DarkSalmon
        self._button3.Location = System.Drawing.Point(648, 576)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(210, 93)
        self._button3.TabIndex = 8
        self._button3.Text = "LEAVE NOW"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.DarkSlateGray
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.OrangeRed
        self._textBox1.Location = System.Drawing.Point(481, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(235, 40)
        self._textBox1.TabIndex = 9
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.DarkSlateGray
        self._label7.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.OrangeRed
        self._label7.Location = System.Drawing.Point(483, 121)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(235, 66)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.DarkSlateGray
        self._label8.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.OrangeRed
        self._label8.Location = System.Drawing.Point(482, 206)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(236, 66)
        self._label8.TabIndex = 11
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.DarkSlateGray
        self._label9.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.OrangeRed
        self._label9.Location = System.Drawing.Point(482, 290)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(235, 66)
        self._label9.TabIndex = 12
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSlateGray
        self._label10.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.OrangeRed
        self._label10.Location = System.Drawing.Point(481, 385)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(235, 66)
        self._label10.TabIndex = 13
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.DarkSlateGray
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.OrangeRed
        self._label11.Location = System.Drawing.Point(481, 480)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(235, 66)
        self._label11.TabIndex = 14
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Lime
        self.ClientSize = System.Drawing.Size(900, 681)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pro93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._label7.Text = " "
        self._label8.Text = " "
        self._label9.Text = " "
        self._label10.Text = " "
        self._label11.Text = " "

    def Button1Click(self, sender, e):
        kilowatts = self._textBox1.Text
        base = self._label7.Text
        supercharge = self._label8.Text
        citytax = self._label9.Text
        pay = self._label10.Text
        base = 41.17
        self._label7.Text = str(base)
        supercharge = 4.72
        self._label8.Text = str(supercharge)
        citytax = 1.42
        self._label9.Text = str(citytax)
        pay = 53.31
        self._label10.Text = str(pay)
        aftermay20thpay = 55.44
        self._label11.Text = str(aftermay20thpay)

    def Label6Click(self, sender, e):
        pass
