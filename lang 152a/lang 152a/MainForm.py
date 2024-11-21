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
        self._listBox1.BackColor = System.Drawing.Color.Gold
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 42
        self._listBox1.Location = System.Drawing.Point(12, 60)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(557, 256)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gold
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 347)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(177, 147)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gold
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(195, 347)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 147)
        self._button2.TabIndex = 2
        self._button2.Text = "GO BYE BYE"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gold
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(413, 347)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(166, 150)
        self._button3.TabIndex = 3
        self._button3.Text = "LEAVE"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Orange
        self.ClientSize = System.Drawing.Size(591, 509)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pro152a"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button1Click(self, sender, e):
        heading = "math\t\t sum"
        self._listBox1.Items.Add(heading)
        Sum = 15586428
        answer = "\t\t" + str(Sum)
        self._listBox1.Items.Add(answer)
        for num in range(3, 9670, 3):
            line = str(num)
            self._listBox1.Items.Add(line)   
