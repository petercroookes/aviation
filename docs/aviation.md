# Aviation

## Documentation
The "required global fleet" can be estimated using a very simple model that assumes the number of passengers flying globally annually is known, along with an estimation of the number of seats flown globally per day.

Many assumptions are made to make the model simple. These include assuming the same aircraft services the same route all year round. Given that the two sources used in this model are given in different time bases, they are converted to per day values to maintain consistency. The first equation gives an estimate of the global passengers flying per day:

$$
\text{Passengers Per Day} = \frac{\text{Passengers Per Year}}{\text{Days Per Year}}
$$

The total required global fleet can then be calculated as a function of this intermediate value and the other inputs:

$$
\text{Required Global Fleet} = \frac{\text{Passengers Per Day}}{\text{Seats Per Aircraft}\ \times\ \text{Flights Per Aircraft Per Day}}
$$

With the equations established, we can assign values to these variables using real world data from 2023 and a bit of guess work:

| Variable | Value | Unite | Source |
| -------- | ----- | ----- | ------ |
| Passengers Per Year | $8.7 \times 10^9$ | year^-1^ | ACI [^1] |
| Seats Per Aircraft | $181$ | - | CAA [^2] |
| Flights Per Aircraft Per Day | $4$ | day^-1^ | Guess |

Putting these numbers into the equations:

$$
\text{Passengers Per Day} = \frac{8.7 \times 10^9}{365.25} = 2.4 \times 10^7
$$

$$
\text{Required Global Fleet} = \frac{2.4 \times 10^7}{181 \times\ 4} = 33149
$$

[^1]: Airports International Council  World Airport Traffic Forecasts 2023-2052. Value from 2023. [Link](https://store.aci.aero/wp-content/uploads/2024/02/WATF-Executive-Summary.pdf)

[^2]: Civil Aviation Authority Quarterly Statistics. Value from 2023. [Link](https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/latest-quarterly-statistics/)