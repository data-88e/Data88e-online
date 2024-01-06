import pandas as pd
from datascience import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np 
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from ipywidgets import interact, interactive, fixed, interact_manual

def cobb_douglas(A, K, L, alpha, beta = None):
    if beta is None:
        return A * K ** alpha * L ** (1 - alpha)
    else:
        return A * K ** alpha * L ** (beta)
        
def cobb_douglas_plotter_K(A, L_bar, alpha, y):
    plt.plot(np.arange(0, 1.01, 0.01), y)
    plt.title(fr"Cobb-Douglas with $\bar L$ = {L_bar}, $A$ = {A} and $\alpha$ = {alpha}")
    plt.xlabel("Capital Stock")
    plt.ylabel("Output");
    
def cobb_douglas_plotter_L(A, K_bar, alpha):
    L_s = np.arange(0, 1.01, 0.01)
    V_3 = cobb_douglas(A, K_bar, L_s, alpha)
    plt.plot(L_s, V_3)
    plt.title(fr"Cobb-Douglas with $\bar K$ = {K_bar}, $A$ = {A} and $\alpha$ = {alpha}")
    plt.xlabel("Labor Force")
    plt.ylabel("Output");
    
def plot_cobb_douglas(V, orig_V):
    data = [go.Surface(z = V, contours = go.surface.Contours(z = go.surface.contours.Z(show = False, project = dict(z = True))),
                      colorscale = "Electric", showscale = False),
           go.Surface(z = orig_V, contours = go.surface.Contours(z = go.surface.contours.Z(show = False, project = dict(z = True))),
                     colorscale = "Viridis", showscale = False)]
    layout = go.Layout(title = "Cobb-Douglas Production Function", autosize=False, width=500, height=500, margin = dict(l = 65, r = 50, b = 65, t = 90),
                       scene = dict(xaxis = dict(title = 'K'), yaxis = dict(title = 'L'), zaxis = dict(title = 'Y')))
    fig = go.Figure(data = data, layout = layout)
    iplot(fig)
    
def orig_cobb_douglas():
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    alpha = 0.5
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    return curr_V

def change_A(A):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    alpha = 0.5
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    plot_cobb_douglas(curr_V, orig_cobb_douglas())
    
def change_alpha(alpha):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    plot_cobb_douglas(curr_V, orig_cobb_douglas())

def change_alpha_beta(alpha_beta_sum):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    alpha = alpha_beta_sum / 2
    beta = alpha_beta_sum / 2
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha, beta)
    plot_cobb_douglas(curr_V, orig_cobb_douglas())