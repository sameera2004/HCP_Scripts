function y=tipp_nyspi(data_path)

%addpath(genpath('/gpfs/software/spm/12'))
addpath(genpath('/gpfs/projects/VanSnellenbergGroup/matlab_tipp'))
addpath(genpath('/gpfs/projects/VanSnellenbergGroup/Trunk'))

% cd to save the data - give the path
cd '/gpfs/projects/VanSnellenbergGroup/nyspi_data'

Obj=TIPPstudy(data_path, 'initln')
