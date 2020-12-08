import sys

instr = [x.split(" ") for x in open(sys.argv[1]).read().split("\n")]

def inst_process(env, instr, val):
    if instr == "acc":
        env["acc"] += (val)
        return 1
    elif instr == "jmp":
        return val
    else: # noop
        return 1

def inst_run_noloop(instr):
    env = {"acc": 0}
    lahe = [False] * len(instr)
    cposs = 0
    while(lahe[cposs] == False):
        lahe[cposs] = True
        inst, val = instr[cposs]
        cposs += inst_process(env, inst, int(val))
        if cposs >= len(instr):
            break

    return env["acc"]

def does_terminate(instr):
    env = {"acc" : 0}
    lahe = [False] * len(instr)
    cposs = 0
    while(lahe[cposs] == False):
        lahe[cposs] = True
        inst, val = instr[cposs]
        cposs += inst_process(env, inst, int(val))
        if cposs >= len(instr):
            return True
    return False

def change_instr():
    for x in instr:
        if x[0] in ("nop", "jmp"):
            # Switch it
            if x[0] == "nop":
                x[0] = "jmp"
            else:
                x[0] = "nop"
            
            # Check if terminate

            if does_terminate(instr):
                return inst_run_noloop(instr)
            else:
                # Revert 

                if x[0] == "nop":
                    x[0] = "jmp"
                else:
                    x[0] = "nop"




print("Part A: ", inst_run_noloop(instr))
print("Part B: ", change_instr()) 
