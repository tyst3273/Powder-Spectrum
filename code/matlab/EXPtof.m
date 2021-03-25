function EXP=demoEXP_tof
%===============================================================================
% function EXP=demoEXP_tof
% adaption from ResLib. Q-resolution is not considered, so only need to indicate
% the parameters listed in this file.
%
%	Required:
%		experiment_type='tof'
%		efixed
%		infin
%		sample.a/b/c
%
%	Optional:
%		basis_user			% can switch between various bases
%		calculation_path	% if provided, SNAXS will load this automatically
%		instrument			% Default is ARCS, others will be implemented in the future
%===============================================================================

EXP.experiment_type = 'tof';
EXP.efixed=65;					
EXP.infin=1;					
EXP.instrument='ARCS';			

EXP.calculation_path='dat/POSCAR';

EXP.dim = [4 4 4];
EXP.sample.a=1.991;		
EXP.sample.b=1.991;			
EXP.sample.c=1.991;		

EXP.sample.alpha=90;    
EXP.sample.beta=90;     
EXP.sample.gamma=90;    

end

