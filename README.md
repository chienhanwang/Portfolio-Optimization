# Portfolio Optimization
```mermaid
  flowchart  TD;
      Collect&nbsphistorical&nbspstock&nbspprice-->Time&nbspseries&nbspforecasting&nbspwith&nbspProphet;
      Time&nbspseries&nbspforecasting&nbspwith&nbspProphet-->Import&nbspprediction&nbspresults&nbspinto&nbspBL&nbspmodel;
      Import&nbspprediction&nbspresults&nbspinto&nbspBL&nbspmodel-->Generate&nbspmultiple&nbspportfolios;
      Generate&nbspmultiple&nbspportfolios-->Draw&nbspthe&nbspefficiency&nbspfront&nbspcurve&nbspaccording&nbspto&nbspER&nbspand&nbspp;
      Draw&nbspthe&nbspefficiency&nbspfront&nbspcurve&nbspaccording&nbspto&nbspER&nbspand&nbspp-->Scenario&nbspanalysis;
      Scenario&nbspanalysis-->Get&nbspthe&nbspbest&nbspportfolio;
```
## Data Information
在投資股票時，不會只投資一檔股票，會投資多檔股票將風險分散，而投資組合如何分配和會有哪些風險和收益即是本研究所要探討的內容。  本研究將時間設定從2019年到2022年，疫情影響下的股票市場，所選的10檔股票是參考2022年兆豐投信台灣晶圓製造的ETF的前十名。  歷史股價是從yfinance獲取，並將後續模型所需的所有股票資訊匯成excel表，下圖以2330為例，包含三年間的收盤價和成交量等資訊，每檔股票都有其各自對應的excel。  
![2330例圖](https://user-images.githubusercontent.com/117811061/209666257-01e273ce-df58-4df0-af89-ab44731d63c5.jpg)
## Time Series Forecasting
Time Series Forecasting部份，我們使用prophet套件來完成，在蒐集完股票資訊後，會將它讀取到預測模型中，每檔股票會有724筆資料，預測模型中的y是close(收盤價)，x則有high、low、open、close、volume、adj close和它們之間的交互作用。
![2303預測結果](https://user-images.githubusercontent.com/117811061/209666273-3d6ad45b-3d02-42f7-968c-635192f7dde1.jpg)  
上方是預測模型跑出的結果，每檔股票都會有一張表跟一張股價的走勢圖。  表中就包含了未來一週的股價，也就是裡面yhat欄位的地方。從圖中則可以得知過去三年與未來一週的股價走勢，圈起來的地方就是預測的結果。
## Black-Litterman Model  
![BL流程圖](https://user-images.githubusercontent.com/117811061/210308446-0345c1ba-98b3-4f87-9010-a4936f35f101.jpg)  
Black-Litterman Model是一個在Bayes框架下的投資組合配置模型。首先透過權重算出預期收益率，並將它當成先驗，然後用先驗收益得出後驗收益，最後用後驗收益率推回理想權重。BL為投資者提供了一個導入"觀點view"的管道，同時將預期收益分散到不同步驟，增加修改的彈性，最後再進行最佳化配置。
