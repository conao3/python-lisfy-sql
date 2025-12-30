# lisfy-sql

A SQL parser for Python with an interactive REPL interface.

## Overview

lisfy-sql parses SQL statements into structured Python objects using a streaming tokenizer approach. It supports common SQL statement types including SELECT, INSERT, UPDATE, DELETE, and CREATE.

## Requirements

- Python 3.11 or higher

## Installation

```bash
pip install lisfy-sql
```

Or install from source using Poetry:

```bash
git clone https://github.com/conao3/python-lisfy-sql.git
cd python-lisfy-sql
poetry install
```

## Usage

### Interactive REPL

Start the interactive SQL parser:

```bash
lisfy-sql
```

This opens a REPL where you can enter SQL statements:

```
lisfy-sql> SELECT * FROM users
```

### Programmatic Usage

```python
from lisfy_sql import rep

# Parse and evaluate a SQL statement
result = rep.rep("SELECT * FROM users")
print(result)
```

## Development

Install development dependencies:

```bash
poetry install
```

Run type checking:

```bash
mypy src/
```

## License

Apache-2.0
