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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Showcard Gothic", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(282, 93)
        self._label1.TabIndex = 5
        self._label1.Text = "(608) 754-9006"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(86, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(149, 67)
        self._button1.TabIndex = 6
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(403, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(149, 67)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(744, 336)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(149, 67)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Showcard Gothic", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(313, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(287, 93)
        self._label2.TabIndex = 9
        self._label2.Text = "(608) 314-8666"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Showcard Gothic", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(631, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(333, 93)
        self._label3.TabIndex = 10
        self._label3.Text = "(608) 743-9511"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Showcard Gothic", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(112, 102)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(333, 93)
        self._label4.TabIndex = 11
        self._label4.Text = "(608) 758-2050"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Showcard Gothic", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(606, 102)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(333, 93)
        self._label5.TabIndex = 12
        self._label5.Text = "(608) 756-9442"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(965, 445)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Phone_Numbers"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        pass

    def Label3Click(self, sender, e):
        pass