function RUNTEST

parfor (i = 0:349, 96)
    FEGS('test-chunks/', i)
end