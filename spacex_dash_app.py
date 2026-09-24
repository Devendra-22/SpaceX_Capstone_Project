"""SpaceX Launch Records Dashboard (Plotly Dash).

Run:  python spacex_dash_app.py   then open http://127.0.0.1:8050
Data: spacex_launch_dash.csv (same folder)
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": site, "value": site} for site in sorted(spacex_df["Launch Site"].unique())
]

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "fontSize": 40},
        ),
        # Task 1: launch site selector (default = all sites)
        dcc.Dropdown(
            id="site-dropdown",
            options=site_options,
            value="ALL",
            placeholder="Select a launch site",
            searchable=True,
            clearable=False,
        ),
        html.Br(),
        # Task 2: success pie chart
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (kg):"),
        # Task 3: payload range slider
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            value=[min_payload, max_payload],
            marks={i: f"{i}" for i in range(0, 10001, 2500)},
        ),
        # Task 4: payload vs. success scatter chart
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


@app.callback(
    Output("success-pie-chart", "figure"), Input("site-dropdown", "value")
)
def update_pie(selected_site):
    """All sites: share of successful launches per site.
    One site: success vs. failure counts for that site."""
    if selected_site == "ALL":
        return px.pie(
            spacex_df,
            values="class",
            names="Launch Site",
            title="Total successful launches by site",
        )
    site_df = spacex_df[spacex_df["Launch Site"] == selected_site]
    counts = site_df["class"].value_counts().rename_axis("class").reset_index(name="count")
    counts["outcome"] = counts["class"].map({1: "Success", 0: "Failure"})
    return px.pie(
        counts,
        values="count",
        names="outcome",
        title=f"Launch outcomes at {selected_site}",
    )


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter(selected_site, payload_range):
    """Payload mass vs. launch outcome, coloured by booster version category."""
    low, high = payload_range
    df = spacex_df[spacex_df["Payload Mass (kg)"].between(low, high)]
    if selected_site != "ALL":
        df = df[df["Launch Site"] == selected_site]
    title = (
        "Payload vs. outcome for all sites"
        if selected_site == "ALL"
        else f"Payload vs. outcome for {selected_site}"
    )
    return px.scatter(
        df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title=title,
        labels={"class": "Launch outcome (1 = success, 0 = failure)"},
    )


if __name__ == "__main__":
    app.run(debug=False)
