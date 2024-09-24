<h1> Designing a Logging Framework </h1>

<h2>Requirements </h2>

- The logging framework should support different log levels, such as DEBUG, INFO, WARNING, ERROR, and FATAL.
- It should allow logging messages with a timestamp, log level, and message content.
- The framework should support multiple output destinations, such as console, file, and database.
- It should provide a configuration mechanism to set the log level and output destination.
- The logging framework should be thread-safe to handle concurrent logging from multiple threads.
- It should be extensible to accommodate new log levels and output destinations in the future.



Python Implementation

<h3>Classes, Interfaces and Enumerations </h3>

- The LoggerLevel enum defines the different log levels supported by the logging framework.
- The LogMessage class represents a log message with a timestamp, log level, and message content.
- The Adapter interface defines the contract for appending log messages to different output destinations.
- The Console, FileAdapter classes are concrete implementations of the Adapter interface, supporting logging to the console, file respectively.
- The LoggerConfig class holds the configuration settings for the logger, including the log level and the selected log Adapter.
- The Logger class is a singleton that provides the main logging functionality. It allows setting the configuration, logging messages at different levels, and provides convenience methods for each log level.
- The LoggerTest class demonstrates the usage of the logging framework, showcasing different log levels, changing the configuration, and logging from multiple threads.

<h3> Test the codebase </h3>

```python3 logger_test.py```

<h3> References </h3>

[link-1](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/logging-framework.md)

[link-2](https://docs.python.org/3.0/tutorial/index.html)

Thanks to [Ashish Pratap Singh](https://github.com/ashishps1)