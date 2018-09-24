function y=tipp_nyspi(data_path)

% 

addpath /gpfs/software/spm12
addpath(genpath('/gpfs/projects/VanSnellenbergGroup/matlab_tipp'))
addpath(genpath('/gpfs/projects/VanSnellenbergGroup/Trunk'))

Obj=TIPPstudy(data_path, 'initln')
