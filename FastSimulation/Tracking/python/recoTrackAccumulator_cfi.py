#######################
# pset that configures the track accumulator, used in the MixingModules to mix reconstructed tracks
# author: Lukas Vanelderen
# date:   Jan 21 2015
#######################

import FWCore.ParameterSet.Config as cms

recoTrackAccumulator = cms.PSet(
    signalTracks = cms.InputTag("generalTracksBeforeMixing"),
    signalMVAValues = cms.InputTag("generalTracksBeforeMixing","MVAValues"),
    pileUpTracks = cms.InputTag("generalTracksBeforeMixing"),
    pileUpMVAValues = cms.InputTag("generalTracksBeforeMixing","MVAValues"),

    outputLabel = cms.string("generalTracks"),
    MVAOutputLabel = cms.string("generalTracksMVAValues"),
    
    accumulatorType = cms.string("RecoTrackAccumulator"),
    makeDigiSimLinks = cms.untracked.bool(False)

    )

