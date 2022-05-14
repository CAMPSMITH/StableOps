# StableOps

## Team Members

| Name                 | email                       | 
|----------------------|-----------------------------|
| Quintin Bland        | quintinbland2@gmail.com     |
| Kevin Corstorphine   | kevincorstorphine@gmail.com |
| John Gruenewald      | john.h.gruenewald@gmail.com |
| Martin Smith         | msmith92663@gmail.com       |
| Yanick Wilisky       | yanickw@gmail.com           |

## Project Description / Outline
The objective of this project is to analyze volatility in stablecoin pricing and assess whether this volatility could provide profitable arbitrage opportunities.
Analysis will include: 

* volatility analysis of stablecoins
* cost analysis associated with trading stablecoins
* risk / reward analysis of stablecoin arbitrage
* simulation of stablecoin arbitrage profitability projections

## Questions to Answer
* Can the volatility of stablecoin pricing yield sufficiently profitable arbitrage opportunities? (MVP)
* Is the volatility of stablecoins pegged to the US Dollar similar or are some stablecoins more volatile than others? (MVP)
* Is the arbitrage based on volatility a better strategy than "safer" alternative, e.g. yield farming (MVP)
* Are the volatilities short lived or persistent? (MVP)
* Are the risk, effort and costs associated with stablecoin arbitrage worth the potential reward? (MVP)
* Are there any correlations between the volatility of various stablecoins?  
* Do some pairs yield better arbitrage opportunities?

## Datasets to be used

| Dataset | URL         | Description | Size | Records |
|---------|-------------|-------------|------|---------|
| daiusd.csv | https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution | DAI USD price at 1 minute resolution, from the Kaggle 400+ crypto currency pairs at 1-minute resolution dataset | 13.7 MB | 256,066 |
| paxusd.csv | https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution | PAX USD price at 1 minute resolution, from the Kaggle 400+ crypto currency pairs at 1-minute resolution dataset | 7.2 MB | 143,564 |
| ustusd.csv | https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution | UST USD price at 1 minute resolution, from the Kaggle 400+ crypto currency pairs at 1-minute resolution dataset | 13.7 MB | 1,230,255 |
| GUSD | https://api.coingecko.com/api/v3/coins/gemini-dollar/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for GUSD from coingecko API |  | 1096 |
| USDC | https://api.coingecko.com/api/v3/coins/usd-coin/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for USDC from coingecko API |  | 1096 |
| USDT | https://api.coingecko.com/api/v3/coins/tether/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for USDT from coingecko API |  | 1095 | 
| PAX | https://api.coingecko.com/api/v3/coins/paxos-standard/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for PAX from coingecko API |  | 1096 |
| DAI | https://api.coingecko.com/api/v3/coins/dai/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for DAI from coingecko API |  | 905 |
| UST | https://api.coingecko.com/api/v3/coins/nusd/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for UST from coingecko  API|  | 1095 |

## Rough breakdown of tasks
* Research and identify a selection of stablecoins pegged to the US Dollar (MVP)
* Identify data sources for daily stablecoin pricing data, with 4 years of data (MVP)
* Identify data sources for intraday stablecoin pricing data (MVP)
* Research and analyze stablecoin trading costs (MVP?) (done?) assume 1%
* Characterize and perform quantitative analysis of stablecoin volatility for selected stablecoins (MVP)
* Risk/Reward (Sharpe Ratio) analysis of stablecoin arbitrage (MVP)
* Presentation preparation (MVP)
* Project documentation (MVP)
* Team formation / organization / git repo (MVP) 
* Montecarlo simulations to project future gains of stablecoin arbitrage

