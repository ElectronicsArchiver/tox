function RUNTRAIN

parfor (i = 0:3145, 96)
    FEGS('train-chunks/', i)
end