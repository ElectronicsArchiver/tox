addpath '/Users/kevinlin/Documents/classes/cs272/tox/model/FEGS/'
parpool('local', 4);

parfor (c=5134:36969, 4)
    file = strcat('trainBatch', num2str(c))
    mat = FEGS(file);
    parsave(strcat('trainBatch', num2str(c), '.mat'), mat)
%     save(strcat('trainBatch', num2str(c), '.mat'), 'mat')
end

function parsave(fname, mat)
    save(fname, 'mat')
end