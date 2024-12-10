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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("SimSun-ExtB", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Lime
        self._label1.Location = System.Drawing.Point(45, 36)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(114, 24)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter First Name Here:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("SimSun-ExtB", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Lime
        self._label2.Location = System.Drawing.Point(45, 81)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(120, 24)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Last Name Here:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Magenta
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("NSimSun", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.Salmon
        self._textBox1.Location = System.Drawing.Point(165, 36)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(146, 13)
        self._textBox1.TabIndex = 2
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Magenta
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("NSimSun", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.Salmon
        self._textBox2.Location = System.Drawing.Point(165, 87)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(146, 13)
        self._textBox2.TabIndex = 3
        self._textBox2.TextChanged += self.TextBox2TextChanged
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumTurquoise
        self._label3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._label3.Font = System.Drawing.Font("Tempus Sans ITC", 18, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.DeepSkyBlue
        self._label3.Location = System.Drawing.Point(97, 157)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(243, 26)
        self._label3.TabIndex = 4
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.SpringGreen
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button1.Cursor = System.Windows.Forms.Cursors.Hand
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("MS PGothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.Highlight
        self._button1.Location = System.Drawing.Point(33, 224)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(88, 45)
        self._button1.TabIndex = 5
        self._button1.Text = "Enter"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.SpringGreen
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button2.Cursor = System.Windows.Forms.Cursors.Hand
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("MS PGothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.Highlight
        self._button2.Location = System.Drawing.Point(127, 224)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(88, 45)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.SpringGreen
        self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button3.Cursor = System.Windows.Forms.Cursors.Hand
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("MS PGothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.Highlight
        self._button3.Location = System.Drawing.Point(221, 224)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(88, 45)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("SimSun-ExtB", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Lime
        self._label4.Location = System.Drawing.Point(12, 157)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(79, 26)
        self._label4.TabIndex = 8
        self._label4.Text = "Full Name:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSlateGray
        self.ClientSize = System.Drawing.Size(358, 284)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Full name"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def TextBox2TextChanged(self, sender, e):
        pass