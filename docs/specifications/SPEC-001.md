# Bar

## Purpose

>Represents one immutable OHLCV observation during one market interval.


## Responsibilities

- stores one market observation
- guarantees valid OHLC relationships
- guarantees valid timestamp
- guarantees immutable state
- provides typed access to values


## Non-responsibilities

- know its symbol
- know its timeframe
- know its exchange
- compute indicators
- calculate returns
- know about trading


## Fields

| Field     | Type        | Required |
|-----------|-------------|----------|
| timestamp | datetime    | ✅        |
| open      | decimal     | ✅        |
| high      | decimal     | ✅        |
| low       | decimal     | ✅        |
| close     | decimal     | ✅        |
| volume    | float/int   | ✅        |


## Validation Rules

These are the invariants

These must always be true:

    timestamp is timezone-aware
    timestamp is UTC
    open >= 0
    high >= 0
    low >= 0
    close >= 0
    volume >= 0
    high >= low
    high >= open
    high >= close
    low <= open
    low <= close


## Immutability

Once created a Bar cannot change. Ever.


## Equality

A Bar should also be hashable.


## Failure cases

Examples:

Invalid

    High = 100
    Low = 105
Result

    ValidationError

---

Invalid

    Timezone missing

Result

    ValidationError

---

Invalid

    Volume = -5

Result

    ValidationError


## Future Extensions

Deliberately excluded:

    VWAP
    Trade count
    Bid
    Ask
    Open Interest
    Corporate actions

for now.
