# QTLab

## Mission
**QTLab is an open-source quantitative research platform for 
designing, validating, and comparing systematic trading strategies using scientific methodology.**


## Coding Standards
Type hints everywhere:

    def load_csv(path: Path) -> pl.DataFrame:

**No untyped functions unless absolutely necessary.**


## Docstrings
 - Every public class.
 - Every public function.

**Not because Python needs them. Because future-us needs them.**


## Tests
Every module gets tested immediately.

Not "*we'll write tests later*". Never.


## Formatting
Automatic. No discussions!

Ruff + formatter.

## Documentation

Each document should answer *Why does this subsystem exist?*

not *What functions does it have?*

That's much more valuable.