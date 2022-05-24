addpath '/Users/kevinlin/Documents/classes/cs272/tox/model/FEGS/'

parpool('local', 4);

parfor (c=5134:36969, 4)
    file = strcat('trainBatch', num2str(c))
    matfile = strcat('trainBatch', num2str(c), '.mat')
    if not(exists(matfile))
        mat = FEGS(file);
        parsave(matfile, mat)
    end
end

function parsave(fname, mat)
    save(fname, 'mat')
end