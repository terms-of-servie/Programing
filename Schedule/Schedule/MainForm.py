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
        self._label1.Font = System.Drawing.Font("SketchFlow Print", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(318, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(271, 347)
        self._label1.TabIndex = 0
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button1.Font = System.Drawing.Font("Snap ITC", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.Control
        self._button1.Location = System.Drawing.Point(53, 35)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(202, 321)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button2.Font = System.Drawing.Font("Snap ITC", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.Control
        self._button2.Location = System.Drawing.Point(686, 24)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(202, 321)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Desktop
        self._button3.Font = System.Drawing.Font("Snap ITC", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLight
        self._button3.Location = System.Drawing.Point(106, 359)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(663, 72)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(958, 443)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "English, computer programming, Band, History, Geometry, Study Hall, Science, Health"

    def Button3Click(self, sender, e):
        Application.Exit()