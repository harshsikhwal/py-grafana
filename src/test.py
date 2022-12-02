import pygrafana
from enum import Enum
import Errors

# grafana = pygrafana.Grafana("localhost", "3000")
#
# folder = grafana.Folder()
#
# dashboard = pygrafana.Dashboard()
#
#
# grafana.get_all_folders()
#
# grafana.print_folders()
#
# datasource = grafana.Datasource()


class ThresholdType(Enum):
    ABSOLUTE = "absolute"
    PERCENTAGE = "percentage"

print(ThresholdType.ABSOLUTE.value)

class TimeSeriesPanel:
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
        if not isinstance(value, int):
            raise Errors.AttributeTypeErrorException("lineInterpolation must be set to an integer")
        self.__lineInterpolation = value

    lineInterpolation = property(_get_line_interpolation, _set_line_interpolation)

    def __init__(self):
        """

        """
        self.tooltip = None



t = TimeSeriesPanel()

t.lineInterpolation = "tt"


