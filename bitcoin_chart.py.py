from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id = "bitcoin",vs_currency="usd",days = 90)
data = pd.DataFrame(bitcoin_data["prices"],columns=["Timestamps","Prices"])

data["Date"] = pd.to_datetime(data["Timestamps"], unit= "ms")

candlestick_data = data.groupby(data.Date.dt.date).agg({"Prices":["max","min","first","last"]})
candlestick_data.columns=["Open","High","Low","Close"]
candlestick_data.reset_index(inplace=True)


fig = go.Figure(data=[go.Candlestick(
    x=candlestick_data["Date"],
    open=candlestick_data["Open"],
    high=candlestick_data["High"],
    low=candlestick_data["Low"],
    close=candlestick_data["Close"],

    increasing_line_color='limegreen',
    decreasing_line_color='crimson',
    increasing_fillcolor='lightgreen',
    decreasing_fillcolor='pink',
    line_width=1.5
)])

fig.update_layout(
    title="📊 Bitcoin Candlestick Chart (Past 30 Days)",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
)

pyo.plot(fig, filename="D:/Python Programming/projects/project.html", auto_open=False)



