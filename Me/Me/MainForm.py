import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(386, 327)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(166, 93)
        self._button2.TabIndex = 1
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(80, 327)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(166, 93)
        self._button1.TabIndex = 2
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(730, 327)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(166, 93)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(269, 41)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(400, 175)
        self._label1.TabIndex = 4
        self._label1.Text = "label1"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(956, 443)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Name = "MainForm"
        self.Text = "Me"
        self.ResumeLayout(False)

