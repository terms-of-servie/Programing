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
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(244, 34)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 0
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightGreen
        self._label1.Font = System.Drawing.Font("Segoe Marker", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(75, 23)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(149, 38)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter KWH used:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkGreen
        self._label2.ForeColor = System.Drawing.Color.SpringGreen
        self._label2.Location = System.Drawing.Point(75, 93)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(269, 258)
        self._label2.TabIndex = 2
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Teal
        self._button1.Font = System.Drawing.Font("Rockwell", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 388)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 58)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculator"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Teal
        self._button2.Font = System.Drawing.Font("Rockwell", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(160, 388)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(127, 58)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Teal
        self._button3.Font = System.Drawing.Font("Rockwell", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(293, 388)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(127, 58)
        self._button3.TabIndex = 5
        self._button3.Text = "Leave"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.ForestGreen
        self.ClientSize = System.Drawing.Size(432, 458)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog 93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass