import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label5 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(392, 179)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(171, 71)
        self._label5.TabIndex = 5
        self._label5.Text = "label5"
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(173, 118)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(171, 71)
        self._label1.TabIndex = 6
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(173, 278)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(171, 71)
        self._label2.TabIndex = 7
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(714, 88)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(171, 71)
        self._label3.TabIndex = 8
        self._label3.Text = "label3"
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(714, 278)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(171, 71)
        self._label4.TabIndex = 9
        self._label4.Text = "label4"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(173, 68)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 10
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(173, 227)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 11
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(745, 43)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 12
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(745, 227)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(75, 23)
        self._button4.TabIndex = 13
        self._button4.Text = "button4"
        self._button4.UseVisualStyleBackColor = True
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(427, 118)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(75, 23)
        self._button5.TabIndex = 14
        self._button5.Text = "button5"
        self._button5.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(968, 448)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label5)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)


