import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.Brown
        self._listBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(101, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(279, 260)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Tomato
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button1.Cursor = System.Windows.Forms.Cursors.No
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("MV Boli", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 302)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(148, 96)
        self._button1.TabIndex = 2
        self._button1.Text = "CUBE"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Tomato
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button2.Cursor = System.Windows.Forms.Cursors.No
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("MS UI Gothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(177, 302)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(148, 96)
        self._button2.TabIndex = 3
        self._button2.Text = "Get rid of it"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Tomato
        self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button3.Cursor = System.Windows.Forms.Cursors.No
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("MS UI Gothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(348, 302)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(148, 96)
        self._button3.TabIndex = 4
        self._button3.Text = "Leave"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SaddleBrown
        self.ClientSize = System.Drawing.Size(508, 410)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog 122 i"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button1Click(self, sender, e):
        for num in range (-25, 26)