﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(319, 92)
        self._label1.TabIndex = 0
        self._label1.Text = "Choose a single number below"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Location = System.Drawing.Point(337, 96)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(291, 382)
        self._label2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(337, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 41)
        self._button1.TabIndex = 2
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(485, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 41)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(337, 52)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(291, 41)
        self._button3.TabIndex = 4
        self._button3.Text = "Calculate"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(12, 113)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(122, 33)
        self._radioButton1.TabIndex = 5
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "0"
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(12, 171)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(122, 33)
        self._radioButton2.TabIndex = 6
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "1"
        self._radioButton2.UseVisualStyleBackColor = True
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(12, 233)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(122, 33)
        self._radioButton3.TabIndex = 7
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "2"
        self._radioButton3.UseVisualStyleBackColor = True
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(12, 298)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(122, 33)
        self._radioButton4.TabIndex = 8
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "3"
        self._radioButton4.UseVisualStyleBackColor = True
        self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
        # 
        # radioButton5
        # 
        self._radioButton5.Location = System.Drawing.Point(12, 355)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(122, 33)
        self._radioButton5.TabIndex = 9
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "4"
        self._radioButton5.UseVisualStyleBackColor = True
        self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
        # 
        # radioButton6
        # 
        self._radioButton6.Location = System.Drawing.Point(187, 355)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(122, 33)
        self._radioButton6.TabIndex = 10
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "9"
        self._radioButton6.UseVisualStyleBackColor = True
        self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
        # 
        # radioButton7
        # 
        self._radioButton7.Location = System.Drawing.Point(187, 113)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(122, 33)
        self._radioButton7.TabIndex = 11
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "5"
        self._radioButton7.UseVisualStyleBackColor = True
        self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
        # 
        # radioButton8
        # 
        self._radioButton8.Location = System.Drawing.Point(187, 171)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(122, 33)
        self._radioButton8.TabIndex = 12
        self._radioButton8.TabStop = True
        self._radioButton8.Text = "6"
        self._radioButton8.UseVisualStyleBackColor = True
        self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
        # 
        # radioButton9
        # 
        self._radioButton9.Location = System.Drawing.Point(187, 233)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(122, 33)
        self._radioButton9.TabIndex = 13
        self._radioButton9.TabStop = True
        self._radioButton9.Text = "7"
        self._radioButton9.UseVisualStyleBackColor = True
        self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
        # 
        # radioButton10
        # 
        self._radioButton10.Location = System.Drawing.Point(187, 298)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(122, 33)
        self._radioButton10.TabIndex = 14
        self._radioButton10.TabStop = True
        self._radioButton10.Text = "8"
        self._radioButton10.UseVisualStyleBackColor = True
        self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(640, 487)
        self.Controls.Add(self._radioButton10)
        self.Controls.Add(self._radioButton9)
        self.Controls.Add(self._radioButton8)
        self.Controls.Add(self._radioButton7)
        self.Controls.Add(self._radioButton6)
        self.Controls.Add(self._radioButton5)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pro 76A"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)

    def RadioButton1CheckedChanged(self, sender, e):
        self._lable2.text = "0 \nx9 \n__________"

    def RadioButton2CheckedChanged(self, sender, e):
        self._lable2.text = "1 \nx9 \n__________"

    def RadioButton3CheckedChanged(self, sender, e):
        self._lable2.text = "2 \nx9 \n__________"

    def RadioButton4CheckedChanged(self, sender, e):
        self._lable2.text = "3 \nx9 \n__________"

    def RadioButton5CheckedChanged(self, sender, e):
        self._lable2.text = "4 \nx9 \n__________"

    def RadioButton7CheckedChanged(self, sender, e):
        self._lable2.text = "5 \nx9 \n__________"

    def RadioButton8CheckedChanged(self, sender, e):
        self._lable2.text = "6 \nx9 \n__________"

    def MainFormLoad(self, sender, e):
        pass

    def RadioButton9CheckedChanged(self, sender, e):
        self._lable2.text = "7 \nx9 \n__________"

    def RadioButton10CheckedChanged(self, sender, e):
        self._lable2.text = "8 \nx9 \n__________"

    def RadioButton6CheckedChanged(self, sender, e):
        self._lable2.text = "9 \nx9 \n__________"
        

    def Button1Click(self, sender, e):
        if self._radioButton1.Checked == True:
            selnum = 0
        elif self._radioButton2.Checked:
            selnum = 1
        elif self._radioButton3.Checked:
            selnum = 2
        elif self._radioButton4.Checked:
            selnum = 3
        elif self._radioButton5.Checked:
            selnum = 4
        elif self._radioButton6.Checked:
            selnum = 5
        elif self._radioButton7.Checked:
            selnum = 6
        elif self._radioButton8.Checked:
            selnum = 7
        elif self._radioButton9.Checked:
            selnum = 8
        elif self._radioButton10.Checked:
            selnum = 9
        
        step = selnum * 9
        step = step1 *12345679
        
        self._label2.Text += "\n" + str(step1) + "\nx12345679" + \
                              "\n_________\n" + str(step2)