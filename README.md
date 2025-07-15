# Aviation

Simple (super low order) model of global aviation. Enjoy!

## Basic Model

Many assumptions are made to make the model simple. These include assuming the same aircraft services the same route all year round, reducing the model to the following two equations:

$\text{Passengers Per Day} = \frac{\text{Passengers Per Year}}{\text{Days Per Year}}$

$\text{Required Global Fleet} = \frac{\text{Passengers Per Day}}{\text{Seats Per Aircraft}\ \times\ \text{Flights Per Aircraft Per Day}}$

With the equations established, we can assign values to these variables real world data from 2023 and a bit of guess work:

| Variable | Value | Source |
| -------- | ----- | ------ |
| Passengers Per Year | $8.7 \times 10^9$ | ACI [^1] |
| Seats Per Aircraft | $181$ | CAA [^2] |
| Flights Per Aircraft Per Day | $4$ | Guess |

Putting these numbers into the equations:

$\text{Passengers Per Day} = \frac{8.7 \times 10^9}{365.25} = 2.4 \times 10^7$

$\text{Required Global Fleet} = \frac{2.4 \times 10^7}{181 \times\ 4} = 33149$


[^1]: Airports International Council  World Airport Traffic Forecasts 2023-2052. Figure from 2023. `https://store.aci.aero/wp-content/uploads/2024/02/WATF-Executive-Summary.pdf`

[^2]: Civil Aviation Authority Quarterly Statistics. Figure from 2023. `https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/latest-quarterly-statistics/`