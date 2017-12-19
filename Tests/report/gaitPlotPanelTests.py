# -*- coding: utf-8 -*-
import logging

import matplotlib.pyplot as plt

# pyCGM2 settings
import pyCGM2

from pyCGM2.Processing.highLevel import standardSmartFunctions,gaitSmartFunctions
from pyCGM2 import enums
from pyCGM2.Processing import c3dManager
from pyCGM2.Model.CGM2 import  cgm,cgm2

from pyCGM2.Report import plot,plotFilters,plotViewers,normativeDatasets
from pyCGM2.Tools import trialTools
from pyCGM2.Report import plot


class oneAnalysis_StandardPlotTest():

    @classmethod
    def descriptiveKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        # viewer
        kv = plotViewers.LowerLimbKinematicsPlotViewer(analysis)
        kv.setConcretePlotFunction(plot.descriptivePlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()






class oneAnalysis_GaitPlotTest():

    @classmethod
    def gaitDescriptiveKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        # viewer
        kv = plotViewers.LowerLimbKinematicsPlotViewer(analysis)
        kv.setConcretePlotFunction(plot.gaitDescriptivePlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()

    @classmethod
    def gaitDescriptiveKinematicPlotPanel_recorded(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        # viewer
        kv = plotViewers.LowerLimbKinematicsPlotViewer(analysis)
        kv.setConcretePlotFunction(plot.gaitDescriptivePlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.setPath("C:\\Users\\HLS501\\Desktop\\")
        pf.setPdfName("test")
        pf.plot()

        plt.show()

    @classmethod
    def gaitConsistencyKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        # viewer
        kv = plotViewers.LowerLimbKinematicsPlotViewer(analysis)
        kv.setConcretePlotFunction(plot.gaitConsistencyPlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()

    @classmethod
    def gaitDescriptiveKineticPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()


        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        # viewer
        if trialManager.kineticFlag:
            kv = plotViewers.LowerLimbKineticsPlotViewer(analysis)
            kv.setConcretePlotFunction(plot.gaitDescriptivePlot)
            kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

            # filter
            pf = plotFilters.PlottingFilter()
            pf.setViewer(kv)
            pf.plot()

        plt.show()

class multipleAnalysis_GaitPlotTest():


    @classmethod
    def gaitDescriptiveKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None


        analysis1 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        analysis2 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        kv = plotViewers.multipleAnalyses_LowerLimbKinematicsPlotViewer([analysis1,analysis2],"Left",["ana1","ana2"])
        kv.setConcretePlotFunction(plot.gaitDescriptivePlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()



    @classmethod
    def gaitConsistencyKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None


        analysis1 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        analysis2 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        kv = plotViewers.multipleAnalyses_LowerLimbKinematicsPlotViewer([analysis1,analysis2],"Left",["ana1","ana2"])
        kv.setConcretePlotFunction(plot.gaitConsistencyPlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()

    @classmethod
    def gaitMeanOnlyKinematicPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis1 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        analysis2 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        kv = plotViewers.multipleAnalyses_LowerLimbKinematicsPlotViewer([analysis1,analysis2],"Left",
                                                                    ["ana1","ana2"])
        kv.setConcretePlotFunction(plot.gaitMeanPlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()


    @classmethod
    def gaitConsistencyKineticPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis1 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        analysis2 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)


        kv = plotViewers.multipleAnalyses_LowerLimbKineticsPlotViewer([analysis1,analysis2],"Right",
                                                                    ["ana1","ana2"])
        kv.setConcretePlotFunction(plot.gaitConsistencyPlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()

    @classmethod
    def gaitMeanOnlyKineticPlotPanel(cls):

        # ----DATA-----
        DATA_PATH = pyCGM2.CONFIG.TEST_DATA_PATH+"operations\\plot\\gaitPlot\\"
        modelledFilenames = ["gait Trial 03 - viconName.c3d"]


        #---- c3d manager
        #--------------------------------------------------------------------------
        c3dmanagerProcedure = c3dManager.UniqueC3dSetProcedure(DATA_PATH,modelledFilenames)
        cmf = c3dManager.C3dManagerFilter(c3dmanagerProcedure)
        cmf.enableEmg(False)
        trialManager = cmf.generate()

        #---- Analysis
        #--------------------------------------------------------------------------

        modelInfo=None
        subjectInfo=None
        experimentalInfo=None

        analysis1 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)

        analysis2 = gaitSmartFunctions.make_analysis(trialManager,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINEMATIC_LABELS_DICT,
                                                cgm.CGM1LowerLimbs.ANALYSIS_KINETIC_LABELS_DICT,
                                    modelInfo,subjectInfo,experimentalInfo)


        kv = plotViewers.multipleAnalyses_LowerLimbKineticsPlotViewer([analysis1,analysis2],"Right",
                                                                    ["ana1","ana2"])
        kv.setConcretePlotFunction(plot.gaitMeanPlot)
        kv.setNormativeDataset(normativeDatasets.Schwartz2008("Free"))

        # filter
        pf = plotFilters.PlottingFilter()
        pf.setViewer(kv)
        pf.plot()

        plt.show()

if __name__ == "__main__":

    plt.close("all")

    oneAnalysis_StandardPlotTest.descriptiveKinematicPlotPanel()

    # oneAnalysis_GaitPlotTest.gaitDescriptiveKinematicPlotPanel()
    # oneAnalysis_GaitPlotTest.gaitDescriptiveKinematicPlotPanel_recorded()
    # oneAnalysis_GaitPlotTest.gaitConsistencyKinematicPlotPanel()
    # oneAnalysis_GaitPlotTest.gaitDescriptiveKineticPlotPanel()
    #
    # multipleAnalysis_GaitPlotTest.gaitDescriptiveKinematicPlotPanel()
    # multipleAnalysis_GaitPlotTest.gaitConsistencyKinematicPlotPanel()
    # multipleAnalysis_GaitPlotTest.gaitMeanOnlyKinematicPlotPanel()
    # multipleAnalysis_GaitPlotTest.gaitConsistencyKineticPlotPanel()
    # multipleAnalysis_GaitPlotTest.gaitMeanOnlyKineticPlotPanel()
