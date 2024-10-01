# Summary

Below is a summary table of the four previously discussed common probability distributions.

| Name          |  PMF or PDF|    Mean    | Variance |  Type | Parameter(s) |
|:-: |    :-: | :-:  |   :-:     |  :-:   |  :-:   |
| [Bernoulli](../11/Bernoulli-Probability-Distribution)     | $\begin{cases} p & x=1\\ 1-p & x=0 \end{cases}$   |  $\sum_x x p(x)$  | $\sigma_X^2 = \sum_x (x - \mu)^2 p(x)$   |  Discrete | $p$ |
| [Binomial](../11/Binomial-Probability-Distribtuion)      |  $\begin{cases} \frac{n!}{x!(n-x)!} p^x (1-p)^{n-x} & x=0,1,...,n\\ 0 & \mathrm{otherwise} \end{cases}$  |  $n p$  | $(1-p)$  | Discrete | $p$, $n$, $x$ |
| [Poisson](../11/Poisson-Probability-Distribution)       | $\begin{cases} e^{-\lambda} \frac{\lambda^x}{x!} & \text{if } x \text{ is a non-negative integer} \\ 0 & \mathrm{otherwise} \end{cases}$  |  $\lambda$  |    $\lambda$      |  Discrete | $\lambda$ |
| [Normal](../11/Normal-Probability-Distribution)        | $f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-(x-\mu)^2 / (2\sigma^2)}$ |  $\mu$  | $\sigma^2$ |  Continuous | $\mu$, $\sigma$ |