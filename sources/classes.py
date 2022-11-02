import tkinter as tk
from tkinter import ttk
import pandas as pd
import data

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotsFrame(tk.Frame):
    df = pd.DataFrame()
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, borderwidth = 1, relief = tk.RIDGE)
                
    def replot(self):
        nCols = len(self.df.columns)
        
        fig = plt.Figure(figsize=(20, 20), dpi=100)
        index = 1
        for var in self.df.columns:
            #print(var)
            axes = fig.add_subplot(2,2,index)
            index = index + 1
            axes.scatter(self.df['x'], self.df[var])
            axes.set_title(var)
            axes.set_ylabel(var)
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack()
        
    def update(self, params):
        self.df = params['df']
        self.replot()
        

class VarListFrame(tk.Frame):
    listBox = 0
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, borderwidth = 1, relief = tk.RIDGE)
        label = tk.Label(self, text = 'Variables')
        label.pack()
        self.listBox = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.listBox.pack()
        
    def update(self, params):
        for var in params['df'].columns:
            self.listBox.insert(0, var)
    
    def get(self):
        return self.listBox.curselection()


class VarComboboxFrame(tk.Frame):
    comboBox = 0
    def __init__(self, parent, text):
        tk.Frame.__init__(self, parent, borderwidth = 1, relief = tk.RIDGE)
        label = tk.Label(self, text = text)
        label.pack()
        self.comboBox = ttk.Combobox(self)
        self.comboBox.pack()
        
    def update(self, params):
        print(self.comboBox['values'])
        self.comboBox['values'] = ['*calc*', '*hist*'] + list(params['df'].columns)
        self.comboBox.set('*calc*')
    def get(self):
        return self.comboBox.get()
    
        
class Analyzer(tk.Tk):
    df = pd.DataFrame()
    
    # Frames
    plotsFrame = 0
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
        
        # Add plots area
        self.plotsFrame = PlotsFrame(rightFrame)
        self.plotsFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Add X axis selector
        self.xAxisSelector = VarComboboxFrame(leftFrame, 'X Axis')
        self.xAxisSelector.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add branch variable selector
        self.branchSelector = VarComboboxFrame(leftFrame, 'Branch')
        self.branchSelector.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Add variable selector
        self.varSelectorFrame = VarListFrame(leftFrame)
        self.varSelectorFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Generate example data
        self.setData(data.genDataFrame())
        self.update()
        
    def update(self):
        params={}
        params['df'] = self.df
        params['vars'] = self.varSelectorFrame.get()
        params['xAxis'] = self.xAxisSelector.get()
        params['branch'] = ''
        
    
    def setData(self, df):
        self.df = df
        params={}
        params['df'] = self.df
        # Update left controllers
        self.plotsFrame.update(params)
        self.varSelectorFrame.update(params)
        self.xAxisSelector.update(params)