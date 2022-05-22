addpath '/Users/kevinlin/Documents/classes/cs272/tox/model/FEGS/'
for c=40:36969
    file = strcat('trainBatch', num2str(c))
    mat = FEGS(file);
    save(strcat('trainBatch', num2str(c), '.mat'), 'mat')
    clc()
end