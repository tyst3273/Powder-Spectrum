function auto_sqw_v2(EXP_func,handle,Q_hkl)

    
    PAR=auto_PAR(EXP_func);
    [XTAL,EXP,INFO,PLOT,DATA,VECS]=params_fetch(PAR);

    PAR.INFO.e_max=100;
    PAR.INFO.e_step=0.1;
    PAR.INFO.e_min=0.1;

    PAR.INFO.bose=1;              % include bose factor
    PAR.INFO.degrees=300;          % temperature
    PAR.INFO.Q_squared=1;         % include Q^2 if 1, set to 0 if not
    PAR.INFO.one_ovr_omega=1;     % include 1/omega factor for scattering
    PAR.INFO.bragg_handling=0;    % if 1 set eng to 0.1meV, if 0 set height to 0
    PAR.INFO.kfki=1;               % include kf/ki factor

    PAR=simulate_SQW(PAR,Q_hkl);


%    energy=PAR.DATA.eng;
%    sqe=PAR.DATA.SQE_array;
%    %save(out_file,'energy','sqe');
%    save(strcat(handle,'.mat'),'energy','sqe','-v7.3');
    
    s = PAR.VECS.strufac;
    e = PAR.VECS.energies; 
    save(strcat(handle,'_delta_fn.mat'),...
        'e','s');


    clear variables;


