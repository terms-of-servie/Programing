import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(946, 450)
        self.Name = "MainForm"
        self.Text = "simple calc"
        self.ResumeLayout(False)

