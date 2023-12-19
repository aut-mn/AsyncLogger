# AsyncLogger
AsyncLogger is an asynchronous Python logging utility that facilitates efficient logging with both file saving and console output. It is designed to be used in asynchronous applications where traditional synchronous logging might introduce performance bottlenecks.
<img src="https://github.com/autumnfied/AsyncLogger/blob/main/Example.png">
## Features
- Asynchronous logging for improved performance in async applications.
- Saves logs to a file and display them on the console simultaneously.
- Simple usage with a straightforward API.

## Usage
Download main.py, rename it if needed, and import it into your working directory.
Import the AsyncLogCollector class:
```python3
from AsyncLogger import AsyncLogCollector
```

Initialize an instance of AsyncLogCollector and specify the output path & filename:
```python3
log_collector = AsyncLogCollector("log.txt")
```

Use the logging methods to record messages. Example:
```python3
await log_collector.error("This is an example error message.")
```

The supported logging methods are:`info`, `warn`, `error`, and `fatal`.

Example usage of the logger:
```python3
from AsyncLogger import AsyncLogCollector
async def main():
    log_collector = AsyncLogCollector("log.txt") # Initialize the log collector & specify output
    await log_collector.info("It worked!") # Send to the AsyncLogger an info log

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
