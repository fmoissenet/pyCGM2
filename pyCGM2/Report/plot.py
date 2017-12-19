# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import logging


import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches

# pyCGM2
#import pyCGM2
import pyCGM2.Processing.analysis as CGM2analysis
from pyCGM2.Tools import trialTools

# openMA
import ma.io
import ma.body


# ---- convenient plot functions
def temporalPlot(figAxis,trial,
                pointLabel,axis,pointLabelSuffix="",color=None,
                title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `trial` (ma.Trial) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

   '''
    flag = trialTools.isTimeSequenceExist(trial,pointLabel)

    if flag:
        suffixPlus = "_" + pointLabelSuffix if pointLabelSuffix!="" else ""
        lines=figAxis.plot(trial.findChild(ma.T_TimeSequence,str(pointLabel+suffixPlus)).data()[:,axis], '-', color= color)

    if legendLabel is not None  and flag: lines[0].set_label(legendLabel)
    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None: figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None: figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None: figAxis.set_ylim(ylim)


def descriptivePlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

   '''


    # check if [ pointlabel , context ] in keys of analysisStructureItem
    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False


    # plot
    if flag:
        mean=analysisStructureItem.data[pointLabel,contextPointLabel]["mean"][:,axis]
        std=analysisStructureItem.data[pointLabel,contextPointLabel]["std"][:,axis]
        line= figAxis.plot(np.linspace(0,100,101), mean, color=color,linestyle="-")
        figAxis.fill_between(np.linspace(0,100,101), mean-std, mean+std, facecolor=color, alpha=0.5,linewidth=0)

        if customLimits is not None:
            for value in customLimits:
                figAxis.axhline(value,color=color,ls='dashed')


    if legendLabel is not None: line.set_label(legendLabel)
    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None:figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None:figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None:figAxis.set_ylim(ylim)

def consistencyPlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

    '''

    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            n = len(analysisStructureItem.data[pointLabel,contextPointLabel]["values"])
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False

    # plot
    if flag:
        values= np.zeros((101,n))
        i=0
        for val in analysisStructureItem.data[pointLabel,contextPointLabel]["values"]:
           values[:,i] = val[:,axis]
           i+=1

        lines = figAxis.plot(np.linspace(0,100,101), values, color=color)

        if customLimits is not None:
           for value in customLimits:
               figAxis.axhline(value,color=color,ls='dashed')


    if legendLabel is not None and flag: lines[0].set_label(legendLabel)

    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None:figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None:figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None:figAxis.set_ylim(ylim)


def meanPlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

   '''


    # check if [ pointlabel , context ] in keys of analysisStructureItem
    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False


    # plot
    if flag:
        mean=analysisStructureItem.data[pointLabel,contextPointLabel]["mean"][:,axis]
        lines= figAxis.plot(np.linspace(0,100,101), mean, color=color,linestyle="-")

        if customLimits is not None:
            for value in customLimits:
                figAxis.axhline(value,color=color,ls='dashed')

    if legendLabel is not None  and flag: lines[0].set_label(legendLabel)
    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None: figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None: figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None: figAxis.set_ylim(ylim)


def gaitDescriptivePlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

   '''

    # check if [ pointlabel , context ] in keys of analysisStructureItem
    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False


    # plot
    if flag:
        mean=analysisStructureItem.data[pointLabel,contextPointLabel]["mean"][:,axis]
        std=analysisStructureItem.data[pointLabel,contextPointLabel]["std"][:,axis]
        line= figAxis.plot(np.linspace(0,100,101), mean, color=color,linestyle="-")
        figAxis.fill_between(np.linspace(0,100,101), mean-std, mean+std, facecolor=color, alpha=0.5,linewidth=0)

        # add gait phases
        stance = analysisStructureItem.pst['stancePhase', contextPointLabel]["mean"]
        double1 = analysisStructureItem.pst['doubleStance1', contextPointLabel]["mean"]
        double2 = analysisStructureItem.pst['doubleStance2', contextPointLabel]["mean"]
        figAxis.axvline(stance,color=color,ls='dashed')
        figAxis.axvline(double1,ymin=0.9, ymax=1.0,color=color,ls='dotted')
        figAxis.axvline(stance-double2,ymin=0.9, ymax=1.0,color=color,ls='dotted')

        if customLimits is not None:
            for value in customLimits:
                figAxis.axhline(value,color=color,ls='dashed')

    if legendLabel is not None: line[0].set_label(legendLabel)
    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None:figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None:figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None:figAxis.set_ylim(ylim)

def gaitConsistencyPlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

    '''

    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            n = len(analysisStructureItem.data[pointLabel,contextPointLabel]["values"])
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False

    # plot
    if flag:
        values= np.zeros((101,n))
        i=0
        for val in analysisStructureItem.data[pointLabel,contextPointLabel]["values"]:
           values[:,i] = val[:,axis]
           i+=1

        lines = figAxis.plot(np.linspace(0,100,101), values, color=color)

        for valStance,valDouble1,valDouble2, in zip(analysisStructureItem.pst['stancePhase', contextPointLabel]["values"],
                                                    analysisStructureItem.pst['doubleStance1', contextPointLabel]["values"],
                                                    analysisStructureItem.pst['doubleStance2', contextPointLabel]["values"]):

            figAxis.axvline(valStance,color=color,ls='dashed')
            figAxis.axvline(valDouble1,ymin=0.9, ymax =1.0 ,color=color,ls='dotted')
            figAxis.axvline(valStance-valDouble2,ymin=0.9, ymax =1.0 ,color=color,ls='dotted')

        if customLimits is not None:
           for value in customLimits:
               figAxis.axhline(value,color=color,ls='dashed')


    if legendLabel is not None and flag: lines[0].set_label(legendLabel)

    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None:figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None:figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None:figAxis.set_ylim(ylim)

def gaitMeanPlot(figAxis,analysisStructureItem,
                        pointLabel,contextPointLabel,axis,
                        color=None,
                        title=None, xlabel=None, ylabel=None,ylim=None,legendLabel=None,
                        customLimits=None):

    '''

        **Description :** plot descriptive statistical (average and sd corridor) gait traces from a pyCGM2.Processing.analysis.Analysis instance

        :Parameters:
             - `figAxis` (matplotlib::Axis )
             - `analysisStructureItem` (pyCGM2.Processing.analysis.Analysis.Structure) - a Structure item of an Analysis instance built from AnalysisFilter

        :Return:
            - matplotlib figure

        **Usage**

        .. code:: python

   '''


    # check if [ pointlabel , context ] in keys of analysisStructureItem
    flag = False
    for key in analysisStructureItem.data.keys():
        if key[0] == pointLabel and key[1] == contextPointLabel:
            flag = True if analysisStructureItem.data[pointLabel,contextPointLabel]["values"] != [] else False


    # plot
    if flag:
        mean=analysisStructureItem.data[pointLabel,contextPointLabel]["mean"][:,axis]
        lines= figAxis.plot(np.linspace(0,100,101), mean, color=color,linestyle="-")

        stance = analysisStructureItem.pst['stancePhase', contextPointLabel]["mean"]
        double1 = analysisStructureItem.pst['doubleStance1', contextPointLabel]["mean"]
        double2 = analysisStructureItem.pst['doubleStance2', contextPointLabel]["mean"]
        figAxis.axvline(stance,color=color,ls='dashed')
        figAxis.axvline(double1,ymin=0.9, ymax=1.0,color=color,ls='dotted')
        figAxis.axvline(stance-double2,ymin=0.9, ymax=1.0,color=color,ls='dotted')

        if customLimits is not None:
            for value in customLimits:
                figAxis.axhline(value,color=color,ls='dashed')

    if legendLabel is not None  and flag: lines[0].set_label(legendLabel)
    if title is not None: figAxis.set_title(title ,size=8)
    figAxis.set_xlim([0.0,100])
    figAxis.tick_params(axis='x', which='major', labelsize=6)
    figAxis.tick_params(axis='y', which='major', labelsize=6)
    if xlabel is not None: figAxis.set_xlabel(xlabel,size=8)
    if ylabel is not None: figAxis.set_ylabel(ylabel,size=8)
    if ylim is not None: figAxis.set_ylim(ylim)
