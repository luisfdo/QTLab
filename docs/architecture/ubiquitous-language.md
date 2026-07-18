*This comes from Domain-Driven Design.*

Certain words should have exactly one meaning.

| Word         | Meaning                                           |
|--------------|---------------------------------------------------|
| Bar          | One immutable OHLCV observation                   |
| Experiment   | One execution of a strategy with fixed parameters |
| Fill         | Executed order (or part of one)                   |
| Hypothesis   | The research question being tested                |
| Order        | Request to buy/sell                               |
| Portfolio    | Collection of positions and cash                  |
| Position     | Current holdings in one instrument                |
| Signal       | Recommendation from a strategy                    |
| Strategy     | Component that generates signals                  |
