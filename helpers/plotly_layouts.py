import plotly.express as px
import plotly.graph_objects as go

def create_plotly(data):

    Ticker =  data["Ticker"].unique()[0]

    fig0 = go.Figure(data=[go.Candlestick(x=data["Date"],
                                              open=data['Open'],
                                              high=data['High'],
                                              low=data['Low'],
                                              close=data['Close'],
                                              name=Ticker)])
    bars1 = go.Bar(
            x=data["Date"],
            y=data['Volume'],
            yaxis="y2",
            marker={'color': "black",
                    'opacity': 0.8},
            name="Volume",
        )

    fig0.add_trace(bars1)

    Header = Ticker
    candle_stick = True

    fig0 = def_fig(fig0, Header, candle_stick)

    return fig0

def def_fig(fig, Header, candle_stick = False, color_percentage = "#03d338",xticks_show = True ,show_legend = True,
            buttons = True):

    if candle_stick == False:

        fig.update_layout(
            yaxis_tickformat=',.0%',
            yaxis=dict(
                tickfont=dict(
                    color=color_percentage
                )),
            yaxis2=dict(
                tickformat=',',
                # range= [0, 1],
                titlefont=dict(
                    color="grey"
                ),
                tickfont=dict(
                    color="grey"
                ),
                anchor="x",
                overlaying="y",
                side="right"
            ),
        )

    else:
        fig.update_layout(
            yaxis_title='Price',
            yaxis_tickprefix='$',
            yaxis2=dict(
                tickformat=',',
                # range= [0, 1],
                titlefont=dict(
                    color="grey"
                ),
                tickfont=dict(
                    color="grey"
                ),
                anchor="x",
                overlaying="y",
                side="right"
            ),
        )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        #autosize=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        title={
            'text': '{}'.format(Header),
            'y': 0.85,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        titlefont=dict(
            size=12,
            color="black"),

        template="simple_white",
        xaxis=dict(
            showticklabels=xticks_show),
        showlegend=show_legend,
        font=dict(
            # family="Courier New, monospace",
            size=12,
            color="black"
        ),

    )

    if buttons == True:
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=3, label="3y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

    fig.update_xaxes(rangeslider_visible=False)
    #fig.update_layout(width=width, height=height)
    fig.update_yaxes(automargin=True,
                     showgrid=True)
    fig.update_xaxes(automargin=True,
                     showgrid=True
                     )

    return fig


def fig_layout(fig, ytitle, ytickfromat, xtitle,ticker, legendtitle, type_of_plot, yaxis_tickprefix=None):

    fig.update_layout(
        yaxis={
            "title": ytitle,
            "tickformat": ytickfromat,

        },
        yaxis_tickprefix = yaxis_tickprefix,
        paper_bgcolor="#FFFFFF",  # rgba(0,0,0,0)',
        plot_bgcolor="#FFFFFF",  # 'rgba(0,0,0,0)',
        # autosize=True,
        legend=dict(
            title=legendtitle,
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        title={
            'text': '{} - {} <br><sup>tenxassets.com</sup>'.format(type_of_plot,ticker),
            'y': 0.85,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        titlefont=dict(
            size=12,
            color="black"),

        template="simple_white",
        xaxis=dict(
            title=xtitle,
            showticklabels=True),
        showlegend=True,
        font=dict(
            # family="Courier New, monospace",
            size=12,
            color="black"
        ),
    )
    return fig


if __name__ == '__main__':
    import sqlite3 as sq
    import pandas as pd
    table_name = "stock_database" # table and file name
    conn = sq.connect('{}.sqlite'.format("database"))
    df = pd.read_sql('select * from {}'.format(table_name), conn)

    data = df[df["Ticker"]=="AAN"]

    fig = create_plotly(data)
    fig.show()
    conn.close()