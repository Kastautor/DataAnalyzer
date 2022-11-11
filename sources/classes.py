import tkinter as tk
import pandas as pd
import data
import frames as fr
from tkinter import ttk


class Analyzer(tk.Tk):
    df = pd.DataFrame()
    
    # Frames
    plotsFrame = 0
    
    # Left Controls
    varSelectorFrame = 0
    xAxisSelector = 0
    branchSelector = 0
        
    def __init__(self):
        super().__init__()
        self.title('Analyzer')
                
        # Maximize window
        self.attributes('-zoomed', True)
        mainFrame = tk.Frame(self)
        mainFrame.pack()
        
        # Add left frame
        leftFrame = tk.Frame(mainFrame)
        leftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Add right frame
        rightFrame = tk.Frame(mainFrame)
        rightFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add right frame
        upperFrame = tk.Frame(rightFrame)
        upperFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Add save config button
        self.saveConfigButton = ttk.Button(upperFrame, text="Load Config", command=self.loadConfig)
        self.saveConfigButton.pack(side=tk.TOP, expand=1)

        # Add save config button
        self.saveConfigButton = ttk.Button(upperFrame, text="Save Config", command=self.saveConfig)
        self.saveConfigButton.pack(side=tk.TOP, expand=1)
        
        # Add X axis selector
        self.xAxisSelector = fr.VarComboboxFrame(leftFrame, 'X Axis')
        self.xAxisSelector.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add branch variable selector
        self.branchSelector = fr.VarComboboxFrame(leftFrame, 'Branch')
        self.branchSelector.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Add variable selector
        self.varSelectorFrame = fr.VarListFrame(leftFrame)
        self.varSelectorFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Add plots area
        self.plotsFrame = fr.PlotsFrame(rightFrame)
        self.plotsFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Generate example data
        self.setData(data.genDataFrame())
        self.update(0)
        
        # Bind F5 to update frames        
        self.bind('<F5>', self.update)
        
    def update(self, event):
        print('Update executed')
        params={}
        params['df'] = self.df
        params['vars'] = self.varSelectorFrame.get()
        params['xAxis'] = self.xAxisSelector.get()
        params['branch'] = self.branchSelector.get()
        self.plotsFrame.update(params)
        
    
    def setData(self, df):
        self.df = df
        params={}
        params['df'] = self.df
        # Update left controllers
        self.varSelectorFrame.update(params)
        self.xAxisSelector.update(params)
        self.branchSelector.update(params)

    def saveConfig(self):
        fun.saveAsXml(params)
        
    def loadConfig(self):
        print(self.df)