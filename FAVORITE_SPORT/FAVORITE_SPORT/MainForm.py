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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(81, 289)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(143, 65)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(379, 289)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 65)
        self._button2.TabIndex = 1
        self._button2.Text = "Dont Show"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(710, 289)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 65)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(240, 36)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(431, 198)
        self._label1.TabIndex = 3
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(943, 435)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "FAVORITE_SPORT"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._lable1.Text = "GOLF"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()