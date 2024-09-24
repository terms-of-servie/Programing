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
        self._button4 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Papyrus", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(71, 321)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(145, 74)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Papyrus", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(411, 321)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(145, 74)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Papyrus", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(764, 321)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(145, 74)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.Desktop
        self._button4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button4.Cursor = System.Windows.Forms.Cursors.Help
        self._button4.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button4.Location = System.Drawing.Point(2, 404)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(52, 28)
        self._button4.TabIndex = 4
        self._button4.UseVisualStyleBackColor = False
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Papyrus", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.Control
        self._label2.Location = System.Drawing.Point(352, 119)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(215, 88)
        self._label2.TabIndex = 5
        self._label2.Click += self.Label2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlText
        self.ClientSize = System.Drawing.Size(960, 441)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Favorite club, sport, or activity"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        self._lable2.Text = "GOLF"

    def Button2Click(self, sender, e):
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()