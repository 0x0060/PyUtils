# PyUtils - Logger Utility

`PyUtils` provides various utility functions to help developers easily integrate production-ready code into their projects. The `Logger` utility allows you to log messages with various severity levels (INFO, DEBUG, ERROR, CLIENT) along with timestamps.

This README explains how to import and use the `Logger` from `logger/log.py` in your Python projects.

## Features

- Log messages at various levels: `INFO`, `DEBUG`, `ERROR`, `CLIENT`.
- Automatically timestamps each log entry.
- Simple and easy-to-use interface for logging messages.

## Installation

To use the `Logger` utility, first clone the repository and place it in your project directory:

```bash
git clone https://github.com/0x0060/PyUtils.git
```

Ensure your project directory is structured like this:

```plaintext
your_project/
│
├── PyUtils/
│   └── logger/
│       └── log.py
└── main.py  # Your project file
```

## Usage

1. **Importing the Logger**  
   In your Python code, you can import the `Logger` from `logger/log.py` as follows:

   ```python
   from PyUtils.logger.log import Logger
   ```

2. **Logging Messages**

   The `Logger` class provides several static methods to log messages at different levels: `info()`, `debug()`, `error()`, and `client()`. Here's how you can use them in your code:

   ```python
   from PyUtils.logger.log import Logger

   def main():
       # Log an informational message
       Logger.info("Application started.")

       # Log a debug message
       Logger.debug("Debugging mode active.")

       # Log an error message
       Logger.error("An unexpected error occurred.")

       # Log a client-specific message
       Logger.client("Client connection established.")

   if __name__ == "__main__":
       main()
   ```

   Each method automatically prepends the log message with the appropriate log level and a timestamp.

   ### Example Output:

   ```plaintext
   (INF): 2024-10-23 12:34:56 - Application started.
   (DBG): 2024-10-23 12:34:56 - Debugging mode active.
   (ERR): 2024-10-23 12:34:56 - An unexpected error occurred.
   (CLT): 2024-10-23 12:34:56 - Client connection established.
   ```

### Available Methods

- **`Logger.info(message: str)`**  
  Logs an informational message.

- **`Logger.debug(message: str)`**  
  Logs a message for debugging purposes.

- **`Logger.error(message: str)`**  
  Logs an error message.

- **`Logger.client(message: str)`**  
  Logs a message related to client interactions.

### How It Works

- **`log(level: str, message: str)`**  
  This is the main method used internally by other log methods. It formats the message with a timestamp and log level before printing it to the console.

- **Log Levels:**
  - `INFO` → `(INF)`
  - `DEBUG` → `(DBG)`
  - `ERROR` → `(ERR)`
  - `CLIENT` → `(CLT)`

- **Timestamp:**  
  All messages are timestamped using the current date and time in the format: `YYYY-MM-DD HH:MM:SS`.

## Contribution

Feel free to open a pull request or submit an issue if you encounter any problems or have suggestions for improvements.
