
##GENSIM
##cmsDriver.py  Configuration/GenProduction/python/genfragment_cff.py --filein file:input.lhe  --fileout file:FSQ-RunIIFall14GS-00001.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN,SIM --magField 38T_PostLS1 --no_exec --python_filename step0_GENSIM_cfg.py -n 147
##HLT
#cmsDriver.py step1 --filein dbs:/T2DegStop2j_300_270_GENSIM/nrad-T2DegStop2j_300_270_GENSIM-edbe023d17b99f8a8fbdf4e576e17580/USER --fileout file:T2DegStop2j_300_270_GENSIMHLT_step1.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIFall14GS-MCRUN2_71_V1-v3/GEN-SIM --mc --eventcontent RAWSIM --pileup Flat_20_50_50ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions MCRUN2_73_V9 --step DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 --python_filename step1_HLT_cfg.py --no_exec


##
#step1 --filein dbs:/DYToMuMu_M_20_TuneCUETP8M1_13TeV_pythia8/RunIIFall14GS-MCRUN2_71_V1-v1/GEN-SIM --fileout file:JME-Fall14DR73-00005_step1.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIFall14GS-MCRUN2_71_V1-v3/GEN-SIM --mc --eventcontent RAWSIM --pileup Flat_20_50_50ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions MCRUN2_73_V9 --step DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/JME-Fall14DR73-00005/JME-Fall14DR73-00005_1_cfg.py --no_exec -n 72
#step2 --filein file:JME-Fall14DR73-00001_step1.root --fileout file:JME-Fall14DR73-00001.root --mc --eventcontent RECOSIM,DQM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO,DQMIO --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/JME-Fall14DR73-00001/JME-Fall14DR73-00001_2_cfg.py



## combinging reco and AOD
#cmsDriver.py step2 --filein file:./lhe2miniAOD/T2DegStop2j_300_270_GENSIMHLT_step1.root --fileout file:T2DegStop2j_300_270_GEN-SIM-AOD_step2.root --mc --eventcontent RECOSIM,AODSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO,AODSIM --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI --magField 38T_PostLS1 --python_filename step2_AOD.py --no_exec

## reco
#cmsDriver.py step2 --filein file:./lhe2miniAOD/T2DegStop2j_300_270_GENSIMHLT_step1.root --fileout file:T2DegStop2j_300_270_GEN-SIM-RECO_step2.root --mc --eventcontent RECOSIM,DQM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO,DQMIO --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 --python_filename step2_RECO.py --no_exec

## reco no DQM
#cmsDriver.py step2 --filein file:./lhe2miniAOD/T2DegStop2j_300_270_GENSIMHLT_step1.root --fileout file:T2DegStop2j_300_270_GEN-SIM-RECOnoDQM_step2.root --mc --eventcontent RECOSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring      --datatier GEN-SIM-RECO --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI --magField 38T_PostLS1 --python_filename step2_RECOnoDQM.py --no_exec

## directly to aod from hlt no DQM
cmsDriver.py step2 --filein file:./lhe2miniAOD/T2DegStop2j_300_270_GENSIMHLT_step1.root --fileout file:T2DegStop2j_300_270_GEN-SIM-AOD.root  --mc --eventcontent AODSIM  --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring  --datatier AODSIM --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI --magField 38T_PostLS1 --python_filename step2_AOD.py --no_exec -n -1  


## directly to aod from hlt
#cmsDriver.py step2 --filein file:./lhe2miniAOD/T2DegStop2j_300_270_GENSIMHLT_step1.root --fileout file:T2DegStop2j_300_270_GEN-SIM-AOD.root  --mc --eventcontent AODSIM,DQM  --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring  --datatier AODSIM,DQMIO --conditions MCRUN2_73_V9 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 --python_filename step2_AOD.py --no_exec -n -1  

### FROM Run2Mechanism lhe
#Driver.py step1 --filein file:GENSIM.root --fileout file:step1.root                                                                                            --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_20_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions PHYS14_25_V1 --step GEN:fixGenInfo,DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 -n -1 
#
#cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM,DQM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier AODSIM,DQMIO --conditions PHYS14_25_V1 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 -n -1
#
#cmsDriver.py step3 --filein file:step2.root --fileout file:out.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions PHYS14_25_V1 --step PAT -n -1
#
#
###PileUp40
#
#cmsDriver.py step1 --filein file:GENSIM.root --fileout file:step1.root --pileup_input "dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM" --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_40_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions PHYS14_25_V1 --step GEN:fixGenInfo,DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 -n -1



