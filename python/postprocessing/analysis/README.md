Setting up a new release area:

    source /cvmfs/cms.cern.ch/cmsset_default.sh (you may want to add this to your .bashrc)
    cd /nfs/dust/cms/user/<youraccount>/
    cmsrel CMSSW_10_4_0
    cd CMSSW_10_4_0/src
    cmsenv
    git cms-init
    git clone https://github.com/adewit/nanoAOD-tools.git PhysicsTools/NanoAODTools
    cd PhysicsTools/NanoAODTools
    git checkout -b summer-project-2019 origin/summer-project-2019
    cd ../../
    scram b 


When you log in again, the release area will still be there but you have to repeat these steps:

    source /cvmfs/cms.cern.ch/cmsset_default.sh (unless you put this in your .bashrc to be executed by default when you log in)
    cd /nfs/dust/cms/user/<youraccount>/CMSSW_10_4_0/src/
    cmsenv


When you make changes to the code it's a good idea to push them to the repository. If you make an account on github, let me know your github username and I can add you to the repository as a collaborator.

For learning how to use git, this is a good starting point: https://www.codecademy.com/learn/learn-git


More samples are available here: /pnfs/desy.de/cms/tier2/store/user/adewit/SummerProjectSamples/ (for later parts of the project)


Cross sections for QCD MC (in pb):

    HT100To200:1.127e+06 
    HT200To300:8.073e+04
    HT300To500:1.668e+04
    HT500To700:1.485e+03
    HT700To1000:2.976e+02
    HT1000To1500:4.640e+01
    HT1500To2000:3.720e+00
    HT2000ToInf:6.438e-01
