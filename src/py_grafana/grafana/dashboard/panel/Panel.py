import json
from enum import Enum

class Panel:
    """A class that stores the panel data"""
    class ThresholdType(Enum):
        ABSOLUTE = "absolute"
        PERCENTAGE = "percentage"

    class Thresholds:
        """"thresholds":
          {
            "mode": "absolute",
            "steps":
            [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }"""

        class Steps:
            def __init__(self):
                self.color = ""
                self.value = None

        def __init__(self):
            self.mode = ""
            self.steps = self.Steps

    class ValueMapper:
        def __init__(self, value, display_text, color):
            # TODO: get the correct data from JSON and reformat it
            self.value = value
            self.displayText = display_text
            self.color = color

    class GridPos:
        def __init__(self, h, w, x, y):
            self.h = h
            self.w = w
            self.x = x
            self.y = y

        def to_json(self):
            # TODO maybe add gridPos as dict
            return json.loads(
                json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o)))
            )

    class Repeat:
        """Panel repetition settings."""

        def __init__(self):
            """
            :param direction: The direction into which to repeat ('h' or 'v')
            :param variable: The name of the variable over whose values to repeat
            :param maxPerRow: The maximum number of panels per row in horizontal repetition
            """
            direction = None
            variable = None
            maxPerRow = None

        def to_json(self):
            return json.loads(json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o))))

    dataSource = None
    targets = []
    title = None
    cacheTimeout = None
    description = None
    editable = True
    error = False
    height = None
    # gridPos = GridPos()
    hideTimeOverride = False
    id = None
    interval = None
    links = []
    maxDataPoints = 100
    minSpan = None
    repeat = None
    span = None
    threshold_steps = []
    threshold_mode = ThresholdType.ABSOLUTE.value
    timeFrom = None
    timeShift = None
    transparent = False
    transformations = []
    extraJson = {}

    def to_json(self, overrides):
        panel_json = {"cacheTimeout": self.cacheTimeout, "datasource": self.dataSource, "description": self.description,
                      "editable": self.editable, "error": self.error}
        thresholds = {"mode": self.threshold_mode, "steps": self.threshold_steps}
        defaults = {"thresholds": thresholds}
        field_config = {"defaults": defaults}
        panel_json["fieldConfig"] = field_config
        panel_json["height"] = self.height
        panel_json["gridPos"] = self.gridPos
        panel_json["hideTimeOverride"] = self.hideTimeOverride
        panel_json["id"] = self.id
        panel_json["interval"] = self.interval
        panel_json["links"] = self.links
        panel_json["maxDataPoints"] = self.maxDataPoints
        panel_json["minSpan"] = self.minSpan
        panel_json["repeat"] = self.Repeat.variable
        panel_json["repeatDirection"] = self.repeat.direction
        panel_json["maxPerRow"] = self.repeat.maxPerRow
        panel_json["span"] = self.span
        panel_json["targets"] = self.targets
        panel_json["timeFrom"] = self.timeFrom
        panel_json["timeShift"] = self.timeShift
        panel_json["title"] = self.title
        panel_json["transparent"] = self.transparent
        panel_json["transformations"] = self.transformations
        return panel_json


class PanelTypes(Enum):
    # TODO add more panel types
    TABLE = "table"


class Color(Enum):
    # TODO add more color types
    GREEN = "green"
    RED = "red"


class TablePanel(Panel):
    """ A class that represents Table panel """

    align = "auto"
    columns = None
    displayMode = "auto"
    filterable = False
    mappings = ""
    overrides = ""
    showHeader = True
    span = ""
    type = PanelTypes.TABLE.value


class TimeSeriesPanel(Panel):
    """ A class that represents Timeseries panel """
    class ToolTip(Enum):
        SINGLE = "single"
        ALL = "all"
        HIDDEN = "hidden"

    class LineInterpolation(Enum):
        LINEAR = "linear"
        SMOOTH = "smooth"
        # TODO check for the types here
        STEP_BEFORE = "step-before"
        STEP_AFTER = "step-after"

    def _get_line_interpolation(self):
        return self.__lineInterpolation

    def _set_line_interpolation(self, value):
        """
        Line Interpolation requires Integer Value
        :param value:
        :return:
        """
        # if not isinstance(value, int):
        #     raise Errors.AttributeTypeErrorException("lineInterpolation must be set to an integer")
        self.__lineInterpolation = value

    lineInterpolation = property(_get_line_interpolation, _set_line_interpolation)

    def __init__(self):
        """

        """
        self.tooltip = None


