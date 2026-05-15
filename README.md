Python framework for modeling stock price paths and computing optimal Bayesian strategies for an experimental market set-up studying the disposition effect. 
Calculates expected capital gains and expected payoffs conditional on information acquisition (no info, P1, P2, P1&2) identifying rational selling decisions based on your chosen parameters.

3 stock types with :

	type0 = winner
	type1 = 'good' loser
	type2 = 'bad' loser

4 information phases:

	P0 - Initial Phase (Investment)
	P1 - Phase 1
	P2 - Phase 2
	P3 - End Phase (Harvest)

Participants can buy information on stocks in P1 and P2 (recieving current price, purchase price, and up/down price movement of asset since previous phase). Participants can choose to sell stocks in either P1, P2, or P3. 

Includes verification of the required conditions necessary for the theoretical optimal Bayesian strategy to hold and identifies the feasible parameter ranges that satisfy them.

Key parameter choices: 

	• scenarios
	• gs
	• bs
	• start_price_mean
	• buy_info
	• p_paths
	• price_paths_type0
	• price_paths_type1
	• price_paths_type2
  
