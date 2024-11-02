$$
\begin{align}
t &= (100 * 100 - 1) - t \\
shell &= \left\lfloor\frac{\sqrt{t}+1}{2}\right\rfloor \\
leg &= \begin{cases}
    0       & \quad \text{if } shell = 0 \\
    \left\lfloor t - \frac{(2 \times shell - 1)^2}{2 \times shell} \right\rfloor  & \quad \text{if } shell \ne 0 \\
\end{cases} \\
elt &= t - (2 * shell - 1)^2 - 2 * shell * leg - shell + 1
\end{align}
$$
