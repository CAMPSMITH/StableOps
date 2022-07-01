# StableOps - Part Deux

## Team Members

| Name                 | email                       | 
|----------------------|-----------------------------|
| Quintin Bland        | quintinbland2@gmail.com     |
| Kevin Corstorphine   | kevincorstorphine@gmail.com |
| John Gruenewald      | john.h.gruenewald@gmail.com |
| Martin Smith         | msmith92663@gmail.com       |
| Yanick Wilisky       | yanickw@gmail.com           |

## Project Description / Outline
Arbitrage trading between a very stable coin, e.g. USDC, and a more volatile stablecoin, sUSD.
low cost trading platform, uniswap / polygon

* get hourly data, min 1 year for: USDC, sUSD and BTC
* identify an API to get hourly data for each sushisap (K.)
* Develop additional signals / features for each coin USDC, sUSD and BTC
   * fast SMA
   * slow SMA
   * bollinger band
   * other fin indicators?
* mock trade on uniswap
   * use uniswap trade
   * Uniswap https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v2?query=Example%20query
* develop ML models
   * regession model to rpedict price in near future and trade when projection indicates it
   * classification nodel, predict whether 1 - up by at least ###, -1 down by at least ###, 0 otherwise  **++**
* Deploy model
* paper trade using model for 1 week


## Questions to Answer
* Which model is more effective?
* Can we build an effective arbitrage model

## Datasets to be used

| Dataset | URL         | Description | Size | Records |
|---------|-------------|-------------|------|---------|

## Rough breakdown of tasks
* Uniswap API - python program to prep swap USDC <-> sUSD (Y.)
* **get current price for BTC, sUSD, USDC - python program to get current price (K.)**
* integrate dat from ^^^ and store into DDB - (M.) 
* **Identify historical hourly data for BTC, sUSD, USDC and download data (J.)**
* Research finta package to explore more than bollinger that might be good options.  
    * pick indicators
    * prototype in a python program (Q.)
* Train - classifier (several classifer) slow, fast, training dataset size, model
        - neural network (stretch)
        - regression (###)
* deploy into inference (M.)
    * ECS - container
    * SageMaker Endpoint
* Paper trading (M.)
* Presentation
* **Create Github (M.)** 
* **Revide proposal(M.)**
* skeleton framework for looping classifier models (M.)

Milestone train model starting Thursday's class week 1
Milestone paper trading Jul 11

### github hints
git checkout -b <branchname>
git push
    use error message to copy and paste push command

work
commit
push
