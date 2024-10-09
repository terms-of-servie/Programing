import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox1.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.Window
        self._textBox1.Location = System.Drawing.Point(36, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(160, 26)
        self._textBox1.TabIndex = 0
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox2.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.SystemColors.Window
        self._textBox2.Location = System.Drawing.Point(550, 50)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(160, 26)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox3.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.SystemColors.Window
        self._textBox3.Location = System.Drawing.Point(796, 50)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(160, 26)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox4.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.ForeColor = System.Drawing.SystemColors.Window
        self._textBox4.Location = System.Drawing.Point(299, 50)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(160, 26)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(36, 157)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(334, 107)
        self._label1.TabIndex = 4
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(605, 157)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(334, 107)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlText
        self._button1.Cursor = System.Windows.Forms.Cursors.Hand
        self._button1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(67, 314)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(197, 69)
        self._button1.TabIndex = 6
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlText
        self._button2.Cursor = System.Windows.Forms.Cursors.Hand
        self._button2.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(387, 314)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 69)
        self._button2.TabIndex = 7
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlText
        self._button3.Cursor = System.Windows.Forms.Cursors.Hand
        self._button3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(722, 314)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(197, 69)
        self._button3.TabIndex = 8
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Highlight
        self.ClientSize = System.Drawing.Size(968, 421)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Pro 56B"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        

    def Label1Click(self, sender, e):
        pass

