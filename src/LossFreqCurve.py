import numpy as np
from matplotlib import pyplot as plt


class LossFreqCurve():
    """Impact exceedence frequency curve.
    Attributes
    ----------
    tag : dict
        dictionary of tags of exposures, impact functions set and
        hazard: {'exp': Tag(), 'impf_set': Tag(), 'haz': TagHazard()}
    return_per : np.array
        return period
    impact : np.array
        impact exceeding frequency
    unit : str
        value unit used (given by exposures unit)
    label : str
        string describing source data
    """
    def __init__(self):
        # self.tag = dict()
        self.return_per = np.array([])
        self.impact = np.array([])
        self.unit = ''
        self.label = ''

    def plot(self, axis=None, log_frequency=False, **kwargs):
        """Plot impact frequency curve.
        Parameters
        ----------
        axis  : matplotlib.axes._subplots.AxesSubplot, optional
            axis to use
        log_frequency : boolean, optional
            plot logarithmioc exceedance frequency on x-axis
        kwargs : optional
            arguments for plot matplotlib function, e.g. color='b'
        Returns
        -------
        matplotlib.axes._subplots.AxesSubplot
        """
        if not axis:
            _, axis = plt.subplots(1, 1)
        axis.set_title(self.label)
        axis.set_ylabel('Impact (' + self.unit + ')')
        if log_frequency:
            axis.set_xlabel('Exceedance frequency (1/year)')
            axis.set_xscale('log')
            axis.plot(self.return_per**-1, self.impact, **kwargs)
        else:
            axis.set_xlabel('Return period (year)')

            axis.plot(self.return_per, self.impact, **kwargs)

        print(self.return_per)
        print(self.impact)
        # axis.show()
        return axis