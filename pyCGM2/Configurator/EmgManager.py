# -*- coding: utf-8 -*-
import pyCGM2
from pyCGM2.Configurator import Manager
from pyCGM2.Utils import files
from pyCGM2 import enums
import logging
import copy
from pyCGM2.Report import normativeDatasets



class EmgConfigManager(Manager.ConfigManager):
    """

    """
    def __init__(self,settings,localInternalSettings = None):
        super(EmgConfigManager, self).__init__(settings)

        self._localInternalSettings = localInternalSettings

        self.__internalsettings()

    # run data to overwrite in internalSettings


    def __internalsettings(self):
        if self._localInternalSettings is None:
            self._internSettings = files.openFile(pyCGM2.PYCGM2_APPDATA_PATH,"emg.settings")
        else:
            logging.info("Local internal setting found")
            self._internSettings = self._localInternalSettings

    def contruct(self):

        finalSettings =  copy.deepcopy(self._internSettings)

        for key in self._userSettings.keys():
            if key  not in finalSettings.keys():
                finalSettings.update({key : self._userSettings[key]})

        self.finalSettings = finalSettings


    @property
    def temporal_trials(self):
        return  self._userSettings["Trials"]["Temporal"]

    @property
    def gaitNormalized_trials(self):
        return  self._userSettings["Trials"]["gaitNormalized"]


    @property
    def BandpassFrequencies(self):
        return self._internSettings["Processing"]["BandpassFrequencies"]

    @property
    def EnvelopLowPassFrequency(self):
        return self._internSettings["Processing"]["EnvelopLowPassFrequency"]

    @property
    def EMGS(self):
        return self._internSettings["CHANNELS"]

    @property
    def task(self):
        return self._userSettings["Task"]

    @property
    def conditions(self):
        return self._userSettings["Conditions"]


    @property
    def experimentalInfo(self):
        return self._userSettings["ExperimentalInfo"]

    @property
    def subjectInfo(self):
        return self._userSettings["SubjectInfo"]


    @property
    def title(self):
        if self._userSettings["Title"] == "None":
            title = self._userSettings["Task"]+ "- EMG Gait Processing"
            self._userSettings["Title"] = title

        return self._userSettings["Title"]

    @property
    def rectifyFlag(self):
        return self._userSettings["Views"]["Rectify"]

    @property
    def consistencyFlag(self):
        return self._userSettings["Views"]["Consistency"]
