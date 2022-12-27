# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:44:06 2022

@author: chloe
"""

import pandas as pd
import numpy as np 
np.set_printoptions(suppress=True) 
import matplotlib.pyplot as plt
import scipy.optimize as sco

df_2303 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2303.xlsx')
df_2330 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2330.xlsx')
df_2344 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2344.xlsx')
df_2379 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2379.xlsx')
df_2408 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2408.xlsx')
df_2454 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/2454.xlsx')
df_3105 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/3105.xlsx')
df_3711 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/3711.xlsx')
df_5483 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/5483.xlsx')
df_6488 = pd.read_excel('C:/Users/chloe/Desktop/StockPrice/6488.xlsx')

a1=np.array(df_2303['week_return'])
a2=np.array(df_2330['week_return'])
a3=np.array(df_2344['week_return'])
a4=np.array(df_2379['week_return'])
a5=np.array(df_2408['week_return'])
a6=np.array(df_2454['week_return'])
a7=np.array(df_3105['week_return'])
a8=np.array(df_3711['week_return'])
a9=np.array(df_5483['week_return'])
a10=np.array(df_6488['week_return'])

A=np.vstack((a1,a2,a3,a4,a5,a6,a7,a8,a9,a10))
print(A)

sigma1=np.cov(A)#變異數矩陣
print(sigma1)

W_mkt=np.array([ 0.04, 0.77, 0.01, 0.02, 0.01, 0.11, 0.01, 0.02, 0.01, 0.02]) #7個資產的市值權重

rm=np.array([np.mean(a1),np.mean(a2),np.mean(a3),np.mean(a4),np.mean(a5),np.mean(a6),np.mean(a7),np.mean(a8),np.mean(a9),np.mean(a10)])#rm=10個資產的平均報酬
print(rm)

rf=np.mean(a5)#無風險利率
print(rf)
delta=(rm@W_mkt-rf)/(W_mkt@sigma1@W_mkt.T)#風險趨避參數
print(delta)
pi=delta*sigma1@W_mkt#市場均衡超額報酬   
pi=np.round(pi,4) #四捨五入至第四位
print(pi)

#P因為Q為各個資產的絕對觀點 所以P為單位矩陣
P=np.identity(10)
Q=[0.012940905,0.022817,-0.00826,0.0214973,0.00088,0.01231254,0.036482,0.01935098,-0.00244,-0.00674]#10個資產LSTM跑出來預期報酬
tui=1/724 #調整因子724為總樣本數(比例係數，代表尺度)
omega=np.diag(tui*P@sigma1@P.T) #觀點誤差(不確定性)的協方差矩陣
omega=np.diag(omega)
print(omega)

#後驗ER(期望報酬)
ER=np.linalg.inv(np.linalg.inv(tui*sigma1)+P.T@np.linalg.inv(omega)@P)@(np.linalg.inv(tui*sigma1)@pi+P.T@np.linalg.inv(omega)@Q)
ER=np.round(ER,4)
print(ER)

print(pi)

#新的變異數矩陣
sigma_p=np.linalg.inv(np.linalg.inv(tui*sigma1)+P.T@np.linalg.inv(omega)@P)+sigma1
print(sigma_p)

#新的最佳權重
l=np.array([1,1,1,1,1,1,1,1,1,1])
W_new=(np.linalg.inv(sigma_p)@ER)/(l.T@np.linalg.inv(sigma_p)@ER)
print(W_new)
print(sum(W_new))

print(np.round(W_new,4))#%
print(sum(np.round(W_new,4)))

print(ER)
print(pi)

W_mkt

def portfolioVariance(weights): #計算组合方差
    weights = np.array(weights)
    var = np.dot(weights.T, np.dot(sigma_p, weights))
    return var

def portfolioVolatility(weights): #計算组合標準差
    return np.sqrt(np.dot(weights.T, np.dot(sigma_p, weights)))

def portfolioReturn(weights): #計算組合收益率
    return np.sum(ER * weights) 

def portfolioSharpeRatio(weights): #計算组合夏普比率
    return (portfolioReturn(weights) - rf) / portfolioVolatility(weights)

portfolioReturns = []
portfolioVolatilies = []

minRet = min(ER)
maxRet = max(ER)
trets = np.linspace(minRet, maxRet, 50) #在minRet,maxRet中間產生50個點
tvols = []
weights=[]
sharpe=[]
initialWeights = np.ones(10)
bnds = tuple((0, 1) for x in initialWeights)

for tret in trets:
    cons = ({'type': 'eq', 'fun': lambda x:  portfolioReturn(x) - tret}, #投資收益率=tret
            {'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})

    res = sco.minimize(portfolioVolatility, initialWeights, method='SLSQP', bounds=bnds, constraints=cons) #最佳化算法採用SLSQP，原因是限制式為線性不等式。
    frontierWeights = res['x']
    frontierRet = portfolioReturn(frontierWeights)
    frontierVol = portfolioVolatility(frontierWeights)    
    tvols.append(res['fun'])
    weights.append(frontierWeights)
    sharpe.append((frontierRet-rf)/frontierVol)
    
    plt.figure(figsize=(16, 8))
plt.scatter(tvols, trets, c=(trets-rf) / tvols, marker='o')
plt.grid(True)
plt.xlabel('Expected volatility')
plt.ylabel('Expected return')
plt.colorbar(label='Sharpe ratio')