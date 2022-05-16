# StableOps

**StableOps** is an analysis of potential arbitrage opportunities derived from volatility in stablecoin pricing.  It was observed that many stablecoins have some volatility.  Although usually pegged to a FIAT currency, like the US dollar, they sometimes drift to be a little over or under their peg value. 

![Paxos Price History](images/USDP_price.png)
![Paxos Price Histogram](images/paxos_price_hist.png)

If this volatility could be harnessed, it might be profitable.  The objective of this project is to analyze volatility in stablecoin pricing and assess whether this volatility could provide profitable arbitrage opportunities. 

---

## Data Sources

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
| UST | https://api.coingecko.com/api/v3/coins/nusd/market_chart?vs_currency=usd&days=1095&interval=daily | Daily price for UST from coingecko  API |  | 1095 |
| Gemini_USTUSD_1h.csv | https://www.cryptodatadownload.com/data/gemini/ | Hourly price data for Luna from Gemini | 220 KB | 2350 |
| Gemini_LUNAUSD_1h.csv | https://www.cryptodatadownload.com/data/gemini/ | Hourly price data for Luna from Gemini | 223 KB | 2350 |
| ust-usd-max.csv | https://www.coingecko.com/en/coins/terra-usd/historical_data?end_date=2022-05-13&start_date=2022-04-29#panel | Daily UST price, market cap and trading volume from coingecko | 46 KB | 589 |
| luna-usd-max.csv | https://www.coingecko.com/en/coins/terra-luna/historical_data?end_date=2022-05-13&start_date=2022-04-29#panel | Daily LUNA price, market cap and trading volume from coingecko | 86 KB | 1102 |

---

## Technologies Used

* **Pandas**  - A python library with advanced financial analysis tools.
* **Jupyter Lab** - An IDE used for visualization.
* **anaconda** - A python framework consisting of several tools used in financial analysis, such as Pandas and Jupyter Lab.
* **Requests** - A python library used to interact with APIs.
* **JSON** - A python library that facilitates working with data in JSON format.
* **python-dotenv** - A python library used to configure an environment through key-value pairs stored in a file.
* **hvplot** - A set of Python visualization tools used to create compelling, and interactive visualizations.  
* **pytz** - A python library that facilitates time zone handling and conversion

---

## Installation Guide

TBD ...

---

## Usage

### StableOps Analysis Notebook
Once Jupyter Lab has started in your browser, select the **StableOps.ipynb** notebook from the **Left Sidebar**.

![launch Notebook StableOps.ipynb](images/start_notebook.png)

### Run StableOps Presentation
TBD ...

### Additional Notebooks
* **intraday.ipynb** - A notebook that analyzed stablecoin volatility using high resolution data, up to 1 minute intervals.
* **stable_coin_compare.ipynb** - A notebook that surveyed and analyzed yield farming opportynities.
* **Terra.ipynb** - A notebook that analuzed the collapse of UST and LUNA that occured between 2022-05-07 - 2022-05-14

---

## Contributors

*  **Quintin Bland** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* quintinbland2@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> [<img src="images/LI-In-Bug.png" alt="in" width="20"/>](https://www.linkedin.com/in/quintin-bland-a2b94310b/)

*  **Kevin Corstorphine** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* kevincorstorphine@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> [<img src="images/LI-In-Bug.png" alt="in" width="20"/>](https://www.linkedin.com/in/kevin-corstorphine-9020a7113/)

*  **John Gruenewald** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* john.h.gruenewald@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> [<img src="images/LI-In-Bug.png" alt="in" width="20"/>](https://www.linkedin.com/in/jhgruenewald/)

*  **Martin Smith** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* msmith92663@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> [<img src="images/LI-In-Bug.png" alt="in" width="20"/>](https://www.linkedin.com/in/smithmartinp/)

*  **Yanick Wiliksy** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* yanickw@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> [<img src="images/LI-In-Bug.png" alt="in" width="20"/>](https://www.linkedin.com/in/yanickwilisky/)

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
