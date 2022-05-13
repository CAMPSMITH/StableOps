# Method for Profiting on Stable Coins

1) Buy low, sell when coin returns to 1 USD.

2) Sell current holdings of stable coin when coin goes above 1 USD.

## Calculating max return

Assuming the above methods are the primary profitable methods for trading on stable coin variation,
we can find a maximum return for when a stable coin's price goes above/below 1 USD.

For a series of prices over a given time frame, the current price $P_j$ is profitable if it is above or below the initial price $P_o$.  The return $r$ is simply:

$$
\begin{equation}
r = \frac{P_j - P_o}{P_o} \\
\end{equation}
$$
Or for a series of prices:
$$
\begin{equation}
r_{tot} = \sum_{j=1}^{N} \frac{P_j - P_o}{P_o}
\end{equation}
$$
For the stable coins, we can assume our initial price is 1 USD.  We also can profit off of trades where $P_j < P_o$.  So substituting in $P_o = 1$ and ensuring a non-negative sum, we have:
$$
\begin{equation}
r_{tot} = \sqrt{\sum_{j=1}^{N} {(P_j - 1)}^2}
\end{equation}
$$
Now, to consider how this is related to the standard deviation of the data set, consider the standard deviation $\sigma$ of the dataset with average value $\mu$:
$$
\begin{equation}
\sigma = \sqrt{\frac{\sum_{j=1}^{N} {(P_j - \mu)}^2}{N-1}}
\end{equation}
$$
Assuming that $\mu$ =1 for a stable coin, we can see the total return is closely related to the standard deviation of the dataset.  With a little manipulation, we can calculate the total return $r_{tot}$ from the standard deviation by the following:
$$
\begin{equation}
r_{tot} = \sqrt{\sum_{j=1}^{N} {(P_j - 1)}^2}
=(\sqrt{N-1}) \times \sigma ,
\end{equation}
$$
where $N$ is the number of profitable trades in the series.

### Correct the squared sum information.  The summation of squared values is not equal to the positive sum of values.