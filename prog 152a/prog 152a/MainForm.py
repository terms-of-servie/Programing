import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Olive
        self._label1.Font = System.Drawing.Font("NSimSun", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Cyan
        self._label1.Location = System.Drawing.Point(43, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(425, 248)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button1.Cursor = System.Windows.Forms.Cursors.WaitCursor
        self._button1.Font = System.Drawing.Font("Onyx", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Teal
        self._button1.Location = System.Drawing.Point(1, 287)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(165, 86)
        self._button1.TabIndex = 1
        self._button1.Text = "CALC"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button2.Cursor = System.Windows.Forms.Cursors.WaitCursor
        self._button2.Font = System.Drawing.Font("Onyx", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Teal
        self._button2.Location = System.Drawing.Point(172, 287)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(165, 86)
        self._button2.TabIndex = 2
        self._button2.Text = "CLEAR"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button3.Cursor = System.Windows.Forms.Cursors.WaitCursor
        self._button3.Font = System.Drawing.Font("Papyrus", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Teal
        self._button3.Location = System.Drawing.Point(343, 287)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(146, 86)
        self._button3.TabIndex = 3
        self._button3.Text = ":("
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 192, 0)
        self.ClientSize = System.Drawing.Size(501, 385)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog 152a"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button1Click(self, sender, e):
        self._