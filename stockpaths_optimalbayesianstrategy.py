
## Stock Type Scenario Probs

import random


################ PARAMETERS ################
################ PARAMETERS ################

scenarios = {
     'S1': {'type0':2, 'type1':0, 'type2':2},
     'S2': {'type0':2, 'type1':1, 'type2':1},
}

n_stocks = 4
n_scenarios = len(scenarios)
p_scenarios = 1 / n_scenarios   #0.5

gs = 0.8 #likely state
bs = 0.2 #unlikely state

start_price_mean = 100
start_price_random = random.randint(90, 110) # not relevant for E(V) calculations

buy_info = 2.5 # price of buying info (feasible range important for E_Payoff calc & condition 1, find in requirement conditions section)



# Stock Price Paths for each Stock Type (CG)

p_paths = [gs*gs, gs*bs, bs*gs, bs*bs]   # [0.64, 0.16, 0.16, 0.04]

price_paths_type0 = [
    [15, 25, 70],     #GG
    [15, 25, 25],     #GB
    [15, -1, 25],     #BG
    [15, -1, -10],    #BB
]

price_paths_type1 = [
    [-10, -1, 10],    
    [-10, -1, 10],    
    [-10, -1, 10],    
    [-10, -1, 10],    
]

price_paths_type2 = [
    [-10, -25, -70],    
    [-10, -25, -35],     
    [-10, -1, -35],       
    [-10, -1, 10],       
]



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# up2far



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


##  Choosing random price path for stock types --> not relevant for E(V) calculations
draw_path0 = random.choices(price_paths_type0, p_paths)[0]
draw_path1 = random.choices(price_paths_type1, p_paths)[0]
draw_path2 = random.choices(price_paths_type2, p_paths)[0]
##


################ PARAMETERS ################
################ PARAMETERS ################



############################################################################################### E[CG] UNCONDITIONAL, for each type by phase

E_CG_type0_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type0))
E_CG_type0_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type0))
E_CG_type0_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type0))

print(f"E[CG | type0, phase1] = {E_CG_type0_phase1:.3f}")
print(f"E[CG | type0, phase2] = {E_CG_type0_phase2:.3f}")
print(f"E[CG | type0, phase3] = {E_CG_type0_phase3:.3f}")



E_CG_type1_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type1))
E_CG_type1_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type1))
E_CG_type1_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type1))

print(f"E[CG | type1, phase1] = {E_CG_type1_phase1:.3f}")
print(f"E[CG | type1, phase2] = {E_CG_type1_phase2:.3f}")
print(f"E[CG | type1, phase3] = {E_CG_type1_phase3:.3f}")



E_CG_type2_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type2))
E_CG_type2_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type2))
E_CG_type2_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type2))

print(f"E[CG | type2, phase1] = {E_CG_type2_phase1:.3f}")
print(f"E[CG | type2, phase2] = {E_CG_type2_phase2:.3f}")
print(f"E[CG | type2, phase3] = {E_CG_type2_phase3:.3f}")



################################## E[CG] GIVEN P2 INFO, for each type by phase (needed bc 1st stochastic movement outcome known, does not apply for P1 INFO deterministic movement)

# up2far

E_CG_type0_phase2_p2gs = price_paths_type0[0][1]
E_CG_type0_phase3_p2gs = gs * price_paths_type0[0][2] + bs * price_paths_type0[1][2]


# down2close

E_CG_type0_phase2_p2bs = price_paths_type0[3][1]
E_CG_type0_phase3_p2bs = gs * price_paths_type0[2][2] + bs * price_paths_type0[3][2]


# up2close

E_CG_type1_phase2_p2gs = price_paths_type1[0][1]
E_CG_type1_phase3_p2gs = gs * price_paths_type1[0][2] + bs * price_paths_type1[1][2]

E_CG_type1_phase2_p2bs = price_paths_type1[3][1]
E_CG_type1_phase3_p2bs = gs * price_paths_type1[2][2] + bs * price_paths_type1[3][2]

E_CG_type2_phase2_p2bs = price_paths_type2[3][1]
E_CG_type2_phase3_p2bs = gs * price_paths_type2[2][2] + bs * price_paths_type2[3][2]


#down2far

E_CG_type2_phase2_p2gs = price_paths_type2[0][1]
E_CG_type2_phase3_p2gs = gs * price_paths_type2[0][2] + bs * price_paths_type2[1][2]



############################################################################################### E[price] UNCONDITIONAL for each type by phase

E_price_type0_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type0)) + start_price_mean
E_price_type0_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type0)) + start_price_mean
E_price_type0_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type0)) + start_price_mean

print(f"E[price | type0, phase1] = {E_price_type0_phase1:.3f}")
print(f"E[price | type0, phase2] = {E_price_type0_phase2:.3f}")
print(f"E[price | type0, phase3] = {E_price_type0_phase3:.3f}")



E_price_type1_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type1)) + start_price_mean
E_price_type1_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type1)) + start_price_mean
E_price_type1_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type1)) + start_price_mean

print(f"E[price | type1, phase1] = {E_price_type1_phase1:.3f}")
print(f"E[price | type1, phase2] = {E_price_type1_phase2:.3f}")
print(f"E[price | type1, phase3] = {E_price_type1_phase3:.3f}")



E_price_type2_phase1 = sum(p * path[0] for p, path in zip(p_paths, price_paths_type2)) + start_price_mean
E_price_type2_phase2 = sum(p * path[1] for p, path in zip(p_paths, price_paths_type2)) + start_price_mean
E_price_type2_phase3 = sum(p * path[2] for p, path in zip(p_paths, price_paths_type2)) + start_price_mean

print(f"E[price | type2, phase1] = {E_price_type2_phase1:.3f}")
print(f"E[price | type2, phase2] = {E_price_type2_phase2:.3f}")
print(f"E[price | type2, phase3] = {E_price_type2_phase3:.3f}")



################################## E[CG] GIVEN P2 INFO, for each type by phase (needed bc 1st stochastic movement outcome known, does not apply for P1 INFO deterministic movement)

# up2far

E_price_type0_phase2_p2gs = price_paths_type0[0][1] + start_price_mean
E_price_type0_phase3_p2gs = gs * price_paths_type0[0][2] + bs * price_paths_type0[1][2] + start_price_mean


# down2close

E_price_type0_phase2_p2bs = price_paths_type0[3][1] + start_price_mean
E_price_type0_phase3_p2bs = gs * price_paths_type0[2][2] + bs * price_paths_type0[3][2] + start_price_mean


# up2close

E_price_type1_phase2_p2gs = price_paths_type1[0][1] + start_price_mean
E_price_type1_phase3_p2gs = gs * price_paths_type1[0][2] + bs * price_paths_type1[1][2] + start_price_mean

E_price_type1_phase2_p2bs = price_paths_type1[3][1] + start_price_mean
E_price_type1_phase3_p2bs = gs * price_paths_type1[2][2] + bs * price_paths_type1[3][2] + start_price_mean

E_price_type2_phase2_p2bs = price_paths_type2[3][1] + start_price_mean
E_price_type2_phase3_p2bs = gs * price_paths_type2[2][2] + bs * price_paths_type2[3][2] + start_price_mean


#down2far

E_price_type2_phase2_p2gs = price_paths_type2[0][1] + start_price_mean
E_price_type2_phase3_p2gs = gs * price_paths_type2[0][2] + bs * price_paths_type2[1][2] + start_price_mean






###############################################################################################
###############################################################################################
###############################################################################################


######################################################################### NO INFO 

### prob of stock type (NO INFO)

p_type0_noinfo = p_scenarios * (scenarios['S1']['type0'] + scenarios['S2']['type0']) / (n_stocks)    #0.5
p_type1_noinfo = p_scenarios * (scenarios['S1']['type1'] + scenarios['S2']['type1']) / (n_stocks)    #0.125
p_type2_noinfo = p_scenarios * (scenarios['S1']['type2'] + scenarios['S2']['type2']) / (n_stocks)    #0.375



### E[CG] UNCONDITIONAL (NO INFO)

E_CG_p1_noinfo = p_type0_noinfo * E_CG_type0_phase1 + p_type1_noinfo * E_CG_type1_phase1 + p_type2_noinfo * E_CG_type2_phase1
E_CG_p2_noinfo = p_type0_noinfo * E_CG_type0_phase2 + p_type1_noinfo * E_CG_type1_phase2 + p_type2_noinfo * E_CG_type2_phase2
E_CG_p3_noinfo = p_type0_noinfo * E_CG_type0_phase3 + p_type1_noinfo * E_CG_type1_phase3 + p_type2_noinfo * E_CG_type2_phase3

print(f"E[CG | No Info, phase1] = {E_CG_p1_noinfo:.3f}")
print(f"E[CG | No Info, phase2] = {E_CG_p2_noinfo:.3f}")
print(f"E[CG | No Info, phase3] = {E_CG_p3_noinfo:.3f}")


ranked_E_CG_noinfo = sorted(
    [
        ("phase1, no info", E_CG_p1_noinfo),
        ("phase2, no info", E_CG_p2_noinfo),
        ("phase3, no info", E_CG_p3_noinfo),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_noinfo)

max_E_CG_noinfo = max(E_CG_p1_noinfo, E_CG_p2_noinfo, E_CG_p3_noinfo)

optimal_E_CG_noinfo = max_E_CG_noinfo
print(f"optimal E[CG | No Info] = {optimal_E_CG_noinfo:.3f}")









######################################################################### P1 info

# prob of stock signal up/down in P1 (up --> type0 p=1, down --> type1 p=0.25 or type2 p=0.75)

p_up1 = p_type0_noinfo
p_down1 = p_type1_noinfo + p_type2_noinfo

# prob of stock type (P1 info)


p_type0_p1info_up = p_type0_noinfo / p_up1
p_type1_p1info_up = 0
p_type2_p1info_up = 0

p_type0_p1info_down = 0
p_type1_p1info_down = p_type1_noinfo / p_down1
p_type2_p1info_down = p_type2_noinfo / p_down1

#print(p_type0_p1info_up)
#print(p_type1_p1info_down)
#print(p_type2_p1info_down)



### E[CG | P1 info], by info signal & phase 


#up1

E_CG_p1_up1 = p_type0_p1info_up * E_CG_type0_phase1 + 0 + 0
E_CG_p2_up1 = p_type0_p1info_up * E_CG_type0_phase2 + 0 + 0
E_CG_p3_up1 = p_type0_p1info_up * E_CG_type0_phase3 + 0 + 0

print(f"E[CG | P1 Up, phase1] = {E_CG_p1_up1:.3f}")
print(f"E[CG | P1 Up, phase2] = {E_CG_p2_up1:.3f}")
print(f"E[CG | P1 Up, phase3] = {E_CG_p3_up1:.3f}")


ranked_E_CG_up1 = sorted(
    [
        ("phase1, P1 up", E_CG_p1_up1),
        ("phase2, P1 up", E_CG_p2_up1),
        ("phase3, P1 up", E_CG_p3_up1),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_up1)

max_E_CG_up1 = max(E_CG_p1_up1, E_CG_p2_up1, E_CG_p3_up1)
print(max_E_CG_up1)


#down1

E_CG_p1_down1 = p_type1_p1info_down * E_CG_type1_phase1 + p_type2_p1info_down * E_CG_type2_phase1 + 0
E_CG_p2_down1 = p_type1_p1info_down * E_CG_type1_phase2 + p_type2_p1info_down * E_CG_type2_phase2 + 0
E_CG_p3_down1 = p_type1_p1info_down * E_CG_type1_phase3 + p_type2_p1info_down * E_CG_type2_phase3 + 0

print(f"E[CG | P1 Down, phase1] = {E_CG_p1_down1:.3f}")
print(f"E[CG | P1 Down, phase2] = {E_CG_p2_down1:.3f}")
print(f"E[CG | P1 Down, phase3] = {E_CG_p3_down1:.3f}")


ranked_E_CG_down1 = sorted(
    [
        ("phase1, P1 down", E_CG_p1_down1),
        ("phase2, P1 down", E_CG_p2_down1),
        ("phase3, P1 down", E_CG_p3_down1),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_down1)

max_E_CG_down1 = max(E_CG_p1_down1, E_CG_p2_down1, E_CG_p3_down1)
print(max_E_CG_down1)


# optimal E[CG | P1 info]

optimal_E_CG_p1info = p_up1 * max_E_CG_up1 + p_down1 * max_E_CG_down1
print(f"optimal E[CG | P1 info] = {optimal_E_CG_p1info:.3f}")








######################################################################### P2 info

# prob of stock signal in P2: (stock up or down since P1), (P0 purchase price & P2 current price -> relative price distance). Get no info in P1 at all.
# possible info scenarios: (up, far), (down, far), (up, close), (down, close)

p_up2far = gs * p_type0_noinfo
p_down2close = bs * p_type0_noinfo
p_up2close = (gs + bs) * p_type1_noinfo + bs * p_type2_noinfo
p_down2far = gs * p_type2_noinfo


#print((p_up2far + p_down2far + p_up2close + p_down2close))  # should sum to 1


# prob of stock type (P2 info)

p_type0_p2info_up2far = gs * p_type0_noinfo / p_up2far
p_type1_p2info_up2far = 0
p_type2_p2info_up2far = 0
#print((p_type0_p2info_up2far + p_type1_p2info_up2far + p_type2_p2info_up2far))  # should sum to 1

p_type0_p2info_down2close = bs * p_type0_noinfo / p_down2close
p_type1_p2info_down2close = 0
p_type2_p2info_down2close = 0
#print((p_type0_p2info_down2close + p_type1_p2info_down2close + p_type2_p2info_down2close))  # should sum to 1

p_type0_p2info_up2close = 0
p_type1_p2info_up2close = (gs + bs) * p_type1_noinfo / p_up2close
p_type2_p2info_up2close = bs * p_type2_noinfo / p_up2close
#print((p_type0_p2info_up2close + p_type1_p2info_up2close + p_type2_p2info_up2close))  # should sum to 1

p_type0_p2info_down2far = 0
p_type1_p2info_down2far = 0
p_type2_p2info_down2far = gs * p_type2_noinfo / p_down2far
#print((p_type0_p2info_down2far + p_type1_p2info_down2far + p_type2_p2info_down2far))  # should sum to 1





### E[CG | P2 info], by info signal & phase 

#P1 (no signal)

E_CG_p1_p2info = E_CG_p1_noinfo

print(f"E[CG | P2 Info, phase1] = {E_CG_p1_p2info:.3f}")



#up2far

E_CG_p2_up2far = p_type0_p2info_up2far * E_CG_type0_phase2_p2gs + 0 + 0 
E_CG_p3_up2far = p_type0_p2info_up2far * E_CG_type0_phase3_p2gs + 0 + 0

print(f"E[CG | P2 Up*Far, phase2] = {E_CG_p2_up2far:.3f}")
print(f"E[CG | P2 Up*Far, phase3] = {E_CG_p3_up2far:.3f}")


ranked_E_CG_up2far = sorted(
    [
        ("phase2, P2 up*far", E_CG_p2_up2far),
        ("phase3, P2 up*far", E_CG_p3_up2far),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_up2far)

max_E_CG_up2far = max(E_CG_p2_up2far, E_CG_p3_up2far)
print(max_E_CG_up2far)


#down2close

E_CG_p2_down2close = p_type0_p2info_down2close * E_CG_type0_phase2_p2bs + 0 + 0 
E_CG_p3_down2close = p_type0_p2info_down2close * E_CG_type0_phase3_p2bs + 0 + 0

print(f"E[CG | P2 Down*Close, phase2] = {E_CG_p2_down2close:.3f}")
print(f"E[CG | P2 Down*Close, phase3] = {E_CG_p3_down2close:.3f}")


ranked_E_CG_down2close = sorted(
    [
        ("phase2, P2 down*close", E_CG_p2_down2close),
        ("phase3, P2 down*close", E_CG_p3_down2close),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_down2close)

max_E_CG_down2close = max(E_CG_p2_down2close, E_CG_p3_down2close)
print(max_E_CG_down2close)







#up2close 

E_CG_p2_up2close = p_type1_p2info_up2close * E_CG_type1_phase2_p2gs + p_type2_p2info_up2close * E_CG_type2_phase2_p2bs + 0 
E_CG_p3_up2close = p_type1_p2info_up2close * E_CG_type1_phase3_p2gs +  p_type2_p2info_up2close * E_CG_type2_phase3_p2bs + 0

print(f"E[CG | P2 Up*Close, phase2] = {E_CG_p2_up2close:.3f}")
print(f"E[CG | P2 Up*Close, phase3] = {E_CG_p3_up2close:.3f}")


ranked_E_CG_up2close = sorted(
    [
        ("phase2, P2 up*close", E_CG_p2_up2close),
        ("phase3, P2 up*close", E_CG_p3_up2close),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_up2close)

max_E_CG_up2close = max(E_CG_p2_up2close, E_CG_p3_up2close)
print(max_E_CG_up2close)


#down2far

E_CG_p2_down2far = p_type2_p2info_down2far * E_CG_type2_phase2_p2gs + 0 + 0 
E_CG_p3_down2far = p_type2_p2info_down2far * E_CG_type2_phase3_p2gs + 0 + 0

print(f"E[CG | P2 Down*Far, phase2] = {E_CG_p2_down2far:.3f}")
print(f"E[CG | P2 Down*Far, phase3] = {E_CG_p3_down2far:.3f}")


ranked_E_CG_down2far = sorted(
    [
        ("phase2, P2 down*far", E_CG_p2_down2far),
        ("phase3, P2 down*far", E_CG_p3_down2far),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_down2far)

max_E_CG_down2far = max(E_CG_p2_down2far, E_CG_p3_down2far)
print(max_E_CG_down2far)




# # optimal E[CG | P2 info] 

optimal_E_CG_p2info = p_up2far * max_E_CG_up2far + p_down2far * max_E_CG_down2far + p_up2close * max_E_CG_up2close + p_down2close * max_E_CG_down2close
print(f"optimal E[CG | P2 info] = {optimal_E_CG_p2info:.3f}")













######################################################################### P1&P2 info

# prob of stock signal: up1up2far up1down2close down1up2close down1down2far 

p_up1up2far = p_up1 * gs 
p_up1down2close = p_up1 * bs
p_down1up2close = p_up2close
p_down1down2far = p_down2far

#print((p_up1up2far + p_up1down2close + p_down1up2close + p_down1down2far))  # should sum to 1




# prob of stock type (P1&P2 info)

p_type0_p12info_up1up2far = p_type0_p1info_up
p_type1_p12info_up1up2far = 0
p_type2_p12info_up1up2far = 0 
#print((p_type0_p12info_up1up2far + p_type1_p12info_up1up2far + p_type2_p12info_up1up2far))  # should sum to 1

p_type0_p12info_up1down2close = p_type0_p2info_down2close 
p_type1_p12info_up1down2close = 0
p_type2_p12info_up1down2close = 0  
#print((p_type0_p12info_up1down2close + p_type1_p12info_up1down2close + p_type2_p12info_up1down2close))  # should sum to 1

p_type0_p12info_down1down2far = 0
p_type1_p12info_down1down2far = 0
p_type2_p12info_down1down2far = p_type2_p2info_down2far
#print((p_type0_p12info_down1down2far + p_type1_p12info_down1down2far + p_type2_p12info_down1down2far))  # should sum to 1

p_type0_p12info_down1up2close = 0
p_type1_p12info_down1up2close = p_type1_p2info_up2close
p_type2_p12info_down1up2close = p_type2_p2info_up2close
#print((p_type0_p12info_down1up2close + p_type1_p12info_down1up2close + p_type2_p12info_down1up2close))  # should sum to 1








### E[CG | P1&P2 info], by info signal & phase 



#up1up2far

E_CG_p1_up1up2far = E_CG_p1_up1
E_CG_p2_up1up2far = p_type0_p12info_up1up2far * E_CG_type0_phase2_p2gs + 0 + 0 
E_CG_p3_up1up2far = p_type0_p12info_up1up2far * E_CG_type0_phase3_p2gs + 0 + 0

print(f"E[CG | P1&P2 Up*Up Far, phase1] = {E_CG_p1_up1up2far:.3f}")
print(f"E[CG | P1&P2 Up*Up Far, phase2] = {E_CG_p2_up1up2far:.3f}")
print(f"E[CG | P1&P2 Up*Up Far, phase3] = {E_CG_p3_up1up2far:.3f}")


ranked_E_CG_up1up2far = sorted(
    [
        ("phase1, P1&P2 up*up far", E_CG_p1_up1up2far),
        ("phase2, P1&P2 up*up far", E_CG_p2_up1up2far),
        ("phase3, P1&P2 up*up far", E_CG_p3_up1up2far),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_up1up2far)

max_E_CG_up1up2far = max(E_CG_p1_up1up2far, E_CG_p2_up1up2far, E_CG_p3_up1up2far)
print(max_E_CG_up1up2far)





#up1down2close

E_CG_p1_up1down2close = E_CG_p1_up1
E_CG_p2_up1down2close = p_type0_p12info_up1down2close * E_CG_type0_phase2_p2bs + 0 + 0 
E_CG_p3_up1down2close = p_type0_p12info_up1down2close * E_CG_type0_phase3_p2bs + 0 + 0

print(f"E[CG | P1&P2 Up*Down Close, phase1] = {E_CG_p1_up1down2close:.3f}")
print(f"E[CG | P1&P2 Up*Down Close, phase2] = {E_CG_p2_up1down2close:.3f}")
print(f"E[CG | P1&P2 Up*Down Close, phase3] = {E_CG_p3_up1down2close:.3f}")


ranked_E_CG_up1down2close = sorted(
    [
        ("phase1, P1&P2 up*down close", E_CG_p1_up1down2close),
        ("phase2, P1&P2 up*down close", E_CG_p2_up1down2close),
        ("phase3, P1&P2 up*down close", E_CG_p3_up1down2close),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_up1down2close)

max_E_CG_up1down2close = max(E_CG_p1_up1down2close, E_CG_p2_up1down2close, E_CG_p3_up1down2close)
print(max_E_CG_up1down2close)




#down1up2close 

E_CG_p1_down1up2close = E_CG_p1_down1
E_CG_p2_down1up2close = p_type1_p12info_down1up2close * E_CG_type1_phase2_p2gs + p_type2_p12info_down1up2close * E_CG_type2_phase2_p2bs + 0 
E_CG_p3_down1up2close = p_type1_p12info_down1up2close * E_CG_type1_phase3_p2gs + p_type2_p12info_down1up2close * E_CG_type2_phase3_p2bs + 0

print(f"E[CG | P1&P2 Down*Up Close, phase1] = {E_CG_p1_down1up2close:.3f}")
print(f"E[CG | P1&P2 Down*Up Close, phase2] = {E_CG_p2_down1up2close:.3f}")
print(f"E[CG | P1&P2 Down*Up Close, phase3] = {E_CG_p3_down1up2close:.3f}")


ranked_E_CG_down1up2close = sorted(
    [
        ("phase1, P1&P2 down*up close", E_CG_p1_down1up2close),
        ("phase2, P1&P2 down*up close", E_CG_p2_down1up2close),
        ("phase3, P1&P2 down*up close", E_CG_p3_down1up2close),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_down1up2close)

max_E_CG_down1up2close = max(E_CG_p1_down1up2close, E_CG_p2_down1up2close, E_CG_p3_down1up2close)
print(max_E_CG_down1up2close)




#down1down2far

E_CG_p1_down1down2far = E_CG_p1_down1
E_CG_p2_down1down2far = p_type2_p12info_down1down2far * E_CG_type2_phase2_p2gs + 0 + 0
E_CG_p3_down1down2far = p_type2_p12info_down1down2far * E_CG_type2_phase3_p2gs + 0 + 0

print(f"E[CG | P1&P2 Down*Down Far, phase1] = {E_CG_p1_down1down2far:.3f}")
print(f"E[CG | P1&P2 Down*Down Far, phase2] = {E_CG_p2_down1down2far:.3f}")
print(f"E[CG | P1&P2 Down*Down Far, phase3] = {E_CG_p3_down1down2far:.3f}")



ranked_E_CG_down1down2far = sorted(
    [
        ("phase1, P1&P2 down*down far", E_CG_p1_down1down2far),
        ("phase2, P1&P2 down*down far", E_CG_p2_down1down2far),
        ("phase3, P1&P2 down*down far", E_CG_p3_down1down2far),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_E_CG_down1down2far)

max_E_CG_down1down2far = max(E_CG_p1_down1down2far, E_CG_p2_down1down2far, E_CG_p3_down1down2far)
print(max_E_CG_down1down2far)


# # optimal E[CG | P1&P2 info]

optimal_E_CG_p1p2info = p_up1up2far * max_E_CG_up1up2far + p_down1down2far * max_E_CG_down1down2far + p_up1down2close * max_E_CG_up1down2close + p_down1up2close * max_E_CG_down1up2close
print(f"optimal E[CG | P1&P2 info] = {optimal_E_CG_p1p2info:.3f}")












######################################################################################################################################### Expected Payoffs by strategy


E_Payoff_noinfo = optimal_E_CG_noinfo
E_Payoff_p1info = optimal_E_CG_p1info - buy_info * n_stocks
E_Payoff_p2info = optimal_E_CG_p2info - buy_info * n_stocks
E_Payoff_p1p2info = optimal_E_CG_p1p2info - buy_info * (1.5 * n_stocks) # assumes each scenario has 50% type0 stock, hence buy info on all stocks P1 and only 'losers' P2


ranked_optimal_strategies_EP = sorted(
    [
        ("No Info EP", E_Payoff_noinfo),
        ("P1 Info EP", E_Payoff_p1info),
        ("P2 Info EP", E_Payoff_p2info),
        ("P1&P2 Info EP", E_Payoff_p1p2info),
    ],
    key=lambda x: x[1],
    reverse=True
)
print(ranked_optimal_strategies_EP)





####################################### Required Conditions / Parameter Ranges

# 1.  Highest Ranked Optimal Bayesian Strategy (Expected Payoff) --> P1 info 

# buy_info range calculation (for E_Payoff calc & condition 1)

buy_info_lb = (optimal_E_CG_p1p2info - optimal_E_CG_p1info) / ((1.5* n_stocks) - n_stocks) 
buy_info_ub = (optimal_E_CG_p2info - optimal_E_CG_noinfo) / n_stocks
buy_info_in_range = buy_info_lb < buy_info < buy_info_ub

print(f' info buy lb: {buy_info_lb:.3f}')
print(f' info buy ub: {buy_info_ub:.3f}')
print(f' buy info cost: {buy_info:.3f}')
print(f' buy info in range? {buy_info_in_range}') # necessary, not sufficient for Condition1 to hold


condition1 = (E_Payoff_p1info > E_Payoff_noinfo) and (E_Payoff_p1info > E_Payoff_p2info) and (E_Payoff_p1info > E_Payoff_p1p2info)
print(f"Condition 1 (P1 info best Expected Payoff strategy)? {condition1}")





# 2. Rational to sell both losers in P2 given known info  (Weighted Losers ECG phase 2 > phase 3) ---> making assumption that W_E_CG_losers_p2 are fixed constant so possible to determine lb & ub for p3

W_E_CG_losers_p2 = (p_type1_noinfo / p_down1) * E_CG_type1_phase2 + (p_type2_noinfo / p_down1) * E_CG_type2_phase2 # assume fixed constant to find p3 ub / lb
W_E_CG_losers_p3 = (p_type1_noinfo / p_down1) * E_CG_type1_phase3 + (p_type2_noinfo / p_down1) * E_CG_type2_phase3

type1_p3_worst = min(path[2] for path in price_paths_type1)
print(type1_p3_worst)
type2_p3_worst = min(path[2] for path in price_paths_type2)
print(type2_p3_worst)   

W_E_CG_losers_p3_lb = (p_type1_noinfo / p_down1) * type1_p3_worst + (p_type2_noinfo / p_down1) * type2_p3_worst
W_E_CG_losers_p3_ub = W_E_CG_losers_p2
W_E_CG_losers_p3_in_range = W_E_CG_losers_p3_lb < W_E_CG_losers_p3 < W_E_CG_losers_p3_ub

print(f' Weighted Losers Phase 3 E[CG] lb: {W_E_CG_losers_p3_lb:.3f}')
print(f' Weighted Losers Phase 3 E[CG] ub: {W_E_CG_losers_p3_ub:.3f}')
print(f' Weighted Losers Phase 3 E[CG]: {W_E_CG_losers_p3:.3f}')
print(f' Weighted Losers Phase 2 E[CG]: {W_E_CG_losers_p2:.3f}')
print(f' Weighted Losers Phase 3 E[CG] in range (assuming P2 fixed)? {W_E_CG_losers_p3_in_range}')


condition2 = W_E_CG_losers_p3 < W_E_CG_losers_p2
print(f"Condition 2 (Rational to sell both losers in P2 given known info)? {condition2}")





####################################### Tables / Info



print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print('Raw Expected Capital Gains / Expected Price, by stock type & phase')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')


print(f"E[CG | type0, phase1] = {E_CG_type0_phase1:.3f}")
print(f"E[CG | type0, phase2] = {E_CG_type0_phase2:.3f}")
print(f"E[CG | type0, phase3] = {E_CG_type0_phase3:.3f}")

print(f"E[CG | type1, phase1] = {E_CG_type1_phase1:.3f}")
print(f"E[CG | type1, phase2] = {E_CG_type1_phase2:.3f}")
print(f"E[CG | type1, phase3] = {E_CG_type1_phase3:.3f}")

print(f"E[CG | type2, phase1] = {E_CG_type2_phase1:.3f}")
print(f"E[CG | type2, phase2] = {E_CG_type2_phase2:.3f}")
print(f"E[CG | type2, phase3] = {E_CG_type2_phase3:.3f}")


print("-" * 18)


print(f"E[CG | type0, phase2, UP in P2] = {E_CG_type0_phase2_p2gs:.3f}")
print(f"E[CG | type0, phase3, UP in P2] = {E_CG_type0_phase3_p2gs:.3f}")

print(f"E[CG | type0, phase2, DOWN in P2] = {E_CG_type0_phase2_p2bs:.3f}")
print(f"E[CG | type0, phase3, DOWN in P2] = {E_CG_type0_phase3_p2bs:.3f}")


print(f"E[CG | type1, phase2, INFO in P2] = {E_CG_type1_phase2_p2gs:.3f}") #--> currently always on deterministic path, no difference in gs / bs
print(f"E[CG | type1, phase3, INFO in P2] = {E_CG_type1_phase3_p2gs:.3f}") #--> currently always on deterministic path, no difference in gs / bs


print(f"E[CG | type2, phase2, UP in P2] = {E_CG_type0_phase2_p2bs:.3f}")
print(f"E[CG | type2, phase3, UP in P2] = {E_CG_type0_phase3_p2bs:.3f}")

print(f"E[CG | type2, phase2, DOWN in P2] = {E_CG_type0_phase2_p2gs:.3f}")
print(f"E[CG | type2, phase3, DOWN in P2] = {E_CG_type0_phase3_p2gs:.3f}")



print("-" * 36)


print(f"E[price | type0, phase1] = {E_price_type0_phase1:.3f}")
print(f"E[price | type0, phase2] = {E_price_type0_phase2:.3f}")
print(f"E[price | type0, phase3] = {E_price_type0_phase3:.3f}")

print(f"E[price | type1, phase1] = {E_price_type1_phase1:.3f}")
print(f"E[price | type1, phase2] = {E_price_type1_phase2:.3f}")
print(f"E[price | type1, phase3] = {E_price_type1_phase3:.3f}")

print(f"E[price | type2, phase1] = {E_price_type2_phase1:.3f}")
print(f"E[price | type2, phase2] = {E_price_type2_phase2:.3f}")
print(f"E[price | type2, phase3] = {E_price_type2_phase3:.3f}")


print("-" * 18)


print(f"E[price | type0, phase2, UP in P2] = {E_price_type0_phase2_p2gs:.3f}")
print(f"E[price | type0, phase3, UP in P2] = {E_price_type0_phase3_p2gs:.3f}")

print(f"E[price | type0, phase2, DOWN in P2] = {E_price_type0_phase2_p2bs:.3f}")
print(f"E[price | type0, phase3, DOWN in P2] = {E_price_type0_phase3_p2bs:.3f}")


print(f"E[price | type1, phase2, INFO in P2] = {E_price_type1_phase2_p2gs:.3f}") #--> currently always on deterministic path, no difference in gs / bs
print(f"E[price | type1, phase3, INFO in P2] = {E_price_type1_phase3_p2gs:.3f}") #--> currently always on deterministic path, no difference in gs / bs


print(f"E[price | type2, phase2, UP in P2] = {E_price_type0_phase2_p2bs:.3f}")
print(f"E[price | type2, phase3, UP in P2] = {E_price_type0_phase3_p2bs:.3f}")

print(f"E[price | type2, phase2, DOWN in P2] = {E_price_type0_phase2_p2gs:.3f}")
print(f"E[price | type2, phase3, DOWN in P2] = {E_price_type0_phase3_p2gs:.3f}")




print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print(' KEY INFORMATION SUMMARY')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')



print('Ranked Optimal Strategies (Expected Payoff):')
ranked_optimal_strategies_EP = sorted(
    [
        ("No Info", E_Payoff_noinfo),
        ("P1 Info", E_Payoff_p1info),
        ("P2 Info", E_Payoff_p2info),
        ("P1&P2 Info", E_Payoff_p1p2info),
    ],
    key=lambda x: x[1],
    reverse=True
)
#print(ranked_optimal_strategies_EP)

print(f"{'Strategy, buy...':<25} {'Expected Payoff':>15}")
print("-" * 36)
for strategy, value in ranked_optimal_strategies_EP:
    print(f"{strategy:<20} {value:>15.3f}")


print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')


print('Ranked Optimal Strategies (Expected Capital Gains):')
ranked_optimal_strategies_ECG = sorted(
    [
        ("No Info", optimal_E_CG_noinfo),
        ("P1 Info", optimal_E_CG_p1info),
        ("P2 Info", optimal_E_CG_p2info),
        ("P1&P2 Info", optimal_E_CG_p1p2info),
    ],
    key=lambda x: x[1],
    reverse=True
)
#print(ranked_optimal_strategies_ECG)

print(f"{'Strategy, buy...':<25} {'Expected Capital Gains':>15}")
print("-" * 36)
for strategy, value in ranked_optimal_strategies_ECG:
    print(f"{strategy:<20} {value:>15.3f}")


print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')


print('Ranked Optimal Selling Phase (Expected Capital Gains), for each Info Strategy and Possible Info Scenario:')

print("-" * 36)
print('No Info:')
#print(ranked_E_CG_noinfo)

ranked_E_CG_noinfo_b = sorted(
    [
        ("1", E_CG_p1_noinfo),
        ("2", E_CG_p2_noinfo),
        ("3", E_CG_p3_noinfo),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_noinfo_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)
print("-" * 36)

print('Phase 1 Info: Up - infer type0')
#print(ranked_E_CG_up1)

ranked_E_CG_up1_b = sorted(
    [
        ("1", E_CG_p1_up1),
        ("2", E_CG_p2_up1),
        ("3", E_CG_p3_up1),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_up1_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 1 Info: Down - infer type1 or type2')
#print(ranked_E_CG_down1)

ranked_E_CG_down1_b = sorted(
    [
        ("1", E_CG_p1_down1),
        ("2", E_CG_p2_down1),
        ("3", E_CG_p3_down1),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_down1_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)
print("-" * 36)


print('Phase 2 Info: Up, Far (Price Distance Relative to Purchase Price) - infer type0') 
#print(ranked_E_CG_up2far)

ranked_E_CG_up2far_b = sorted(
    [
        ("2", E_CG_p2_up2far),
        ("3", E_CG_p3_up2far),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_up2far_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 2 Info: Down, Close - infer type0') 
#print(ranked_E_CG_down2close)

ranked_E_CG_down2close_b = sorted(
    [
        ("2", E_CG_p2_down2close),
        ("3", E_CG_p3_down2close),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_down2close_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 2 Info: Up, Close - infer type1 or type2')
#print(ranked_E_CG_up2close)

ranked_E_CG_up2close_b = sorted(
    [
        ("2", E_CG_p2_up2close),
        ("3", E_CG_p3_up2close),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_up2close_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 2 Info: Down, Far - infer type2')
#print(ranked_E_CG_down2far)

ranked_E_CG_down2far_b = sorted(
    [
        ("2", E_CG_p2_down2far),
        ("3", E_CG_p3_down2far),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_down2far_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)
print("-" * 36)


print('Phase 1&2 Info: Up&Up, Far - infer type0') 
#print(ranked_E_CG_up1up2far)

ranked_E_CG_up1up2far_b = sorted(
    [
        ("1", E_CG_p1_up1up2far),
        ("2", E_CG_p2_up1up2far),
        ("3", E_CG_p3_up1up2far),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_up1up2far_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 1&2 Info: Up&Down, Close - infer type0') 
#print(ranked_E_CG_up1down2close)

ranked_E_CG_up1down2close_b = sorted(
    [
        ("1", E_CG_p1_up1down2close),
        ("2", E_CG_p2_up1down2close),
        ("3", E_CG_p3_up1down2close),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_up1down2close_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 1&2 Info: Down&Up, Close - infer type1 or type2') 
#print(ranked_E_CG_down1up2close)

ranked_E_CG_down1up2close_b = sorted(
    [
        ("1", E_CG_p1_down1up2close),
        ("2", E_CG_p2_down1up2close),
        ("3", E_CG_p3_down1up2close),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_down1up2close_b:
    print(f"{phase:<25} {value:>10.3f}")


print("-" * 36)


print('Phase 1&2 Info: Down&Down, Far - infer type2') 
#print(ranked_E_CG_down1down2far)

ranked_E_CG_down1down2far_b = sorted(
    [
        ("1", E_CG_p1_down1down2far),
        ("2", E_CG_p2_down1down2far),
        ("3", E_CG_p3_down1down2far),
    ],
    key=lambda x: x[1],
    reverse=True
)

print(f"{'Phase':<25} {'E[CG]':>10}")
for phase, value in ranked_E_CG_down1down2far_b:
    print(f"{phase:<25} {value:>10.3f}")



print('-----------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------')



print('Required Conditions for Theoretical Optimal Strategy to Hold')
print("-" * 36)

print(f"Condition 1 (P1 info best Expected Payoff strategy)? {condition1}")

print("-" * 36)

print(f' info buy lb: {buy_info_lb:.3f}')
print(f' info buy ub: {buy_info_ub:.3f}')
print(f' buy info cost: {buy_info:.3f}')
print(f' buy info in range? {buy_info_in_range}')


print("-" * 36)
print("-" * 36)


print(f"Condition 2 (Rational to sell both losers in P2 given known info)? {condition2}")

print("-" * 36)

print(f' Weighted Losers Phase 3 E[CG] lb (=Minimum Possible Weighted Losers Phase 3 E[CG]): {W_E_CG_losers_p3_lb:.3f}')
print(f' Weighted Losers Phase 3 E[CG] ub (=Fixed Weighted Losers Phase 2 E[CG]): {W_E_CG_losers_p3_ub:.3f}')
print(f' Weighted Losers Phase 3 E[CG]: {W_E_CG_losers_p3:.3f}')
print(f' Weighted Losers Phase 3 E[CG] in range (assuming fixed E_CG_losers_p2)? {W_E_CG_losers_p3_in_range}')


print('-----------------------------------------------------------------------------------------------')
