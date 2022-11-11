import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotsFrame(tk.Frame):
    df = pd.DataFrame()
    xVar = ''
    branch = ''
    variables = []
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, borderwidth = 1, relief = tk.RIDGE)
                
    def replot(self):
        # Remove plots if they have been already drawn
        for widget in self.winfo_children():
            widget.destroy()

        nPlots = len(self.variables)
        
        fig = plt.Figure(figsize=(20, 20), dpi=100)
        index = 1
        for var in self.variables:
            axes = fig.add_subplot(1,nPlots,index)
            index = index + 1
            xValues = []
            branchValues = []
            if self.xVar == '*calc*':
                xValues = self.df.index
                branchValues = self.df.index
                axes.set_xlabel('calculations')
            elif self.xVar == '*hist*':
                xValues = self.df.index
                branchValues = self.df.index
                axes.set_xlabel('*population*')
            else:
                xValues = self.df[self.xVar]
                branchValues = self.df[self.branch]
                axes.set_xlabel(self.xVar)
            
            axes.scatter(xValues, self.df[var], c=branchValues, cmap='viridis')
            axes.set_title(var)
            axes.set_ylabel(var)
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack()
        
        
    def update(self, params):
        self.df = params['df']
        self.branch = params['branch']
        self.variables = params['vars']
        self.xVar = params['xAxis']
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
        selected_indices = self.listBox.curselection()
        selection = []
        for i in selected_indices:
            #index = selected_indices[i]
            selection.append(self.listBox.get(i))
        return selection


class VarComboboxFrame(tk.Frame):
    comboBox = 0
    def __init__(self, parent, text):
        tk.Frame.__init__(self, parent, borderwidth = 1, relief = tk.RIDGE)
        label = tk.Label(self, text = text)
        label.pack()
        self.comboBox = ttk.Combobox(self)
        self.comboBox.pack()
        
    def update(self, params):
        self.comboBox['values'] = ['*calc*', '*hist*'] + list(params['df'].columns)
        self.comboBox.set('*calc*')
    def get(self):
        return self.comboBox.get()
    