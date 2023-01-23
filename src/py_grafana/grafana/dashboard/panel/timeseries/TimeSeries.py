from py_grafana.grafana.dashboard.panel.Panel import Panel


class TimeSeriesPanel(Panel):
    """
    TimeSeries Panel class basically gives you a local object panel which you can add or even modify
    in the desired parent dashboard
    """

    def __init__(self, title: str):
        super(TimeSeriesPanel, self).__init__()
        self.title = title
        self.type = "timeseries"