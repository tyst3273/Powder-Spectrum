
for i = 0:2
    str = sprintf('%04d',i)
    Q_hkl=readmatrix(strcat('Q_Grid/Q_vecs_',...
       str,'.txt'));
    auto_sqw_v2(EXPtof,...
        strcat('mats/MAPI/out_',str),Q_hkl);
end


%Q_hkl=readmatrix('Q_Grid/Q_vecs_0001.txt');
%auto_sqw_v2(EXPtof,'outi',Q_hkl);

