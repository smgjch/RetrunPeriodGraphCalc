import numpy as np


def calc_freq_curve(self, return_per=None):
    """Compute impact exceedance frequency curve.

    Parameters
    ----------
    return_per : np.array, optional
        return periods where to compute
        the exceedance impact. Use impact's frequencies if not provided

    Returns
    -------
        climada.engine.impact.ImpactFreqCurve
    """
    ifc = ImpactFreqCurve()
    ifc.tag = self.tag
    # Sort descendingly the impacts per events
    sort_idxs = np.argsort(self.at_event)[::-1]
    # Calculate exceedence frequency
    exceed_freq = np.cumsum(self.frequency[sort_idxs])
    # Set return period and imact exceeding frequency
    ifc.return_per = 1 / exceed_freq[::-1]
    ifc.impact = self.at_event[sort_idxs][::-1]
    ifc.unit = self.unit
    ifc.label = 'Exceedance frequency curve'

    if return_per is not None:
        interp_imp = np.interp(return_per, ifc.return_per, ifc.impact)
        ifc.return_per = return_per
        ifc.impact = interp_imp

    return ifc



class ImpactFreqCurve():
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
        self.tag = dict()
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
        return axis


