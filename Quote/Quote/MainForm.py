﻿import System.Drawing
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
        self._label1.Font = System.Drawing.Font("Viner Hand ITC", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 124)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(916, 73)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Viner Hand ITC", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(48, 265)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(228, 124)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Viner Hand ITC", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(361, 265)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(228, 124)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Viner Hand ITC", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(652, 265)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(215, 124)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(940, 446)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Quote"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button1Click(self, sender, e):
        self._label1.Text = "It is never to late to be who you might have been"

    def Button3Click(self, sender, e):
        Application.Exit()