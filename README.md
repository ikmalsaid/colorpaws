# colorpaws

A powerful, flexible logging component that enhances Python's built-in logging with colored output and automated file organization.

## Installation

```bash
pip install colorpaws
```

## Key Features

- 🎨 **Console Output**
  - Colored logging with level-based colors
  - Cross-platform support (Windows/Unix)
  - Smart color detection and handling
- 📁 **File Management**
  - Automatic date-based organization
  - Timestamp-based unique files
  - No duplicate handlers
- ⚙️ **Configuration**
  - Dual output (console and/or file)
  - Customizable log formats
  - Singleton loggers per name

## Usage

### Basic Console Logging

```python
from colorpaws import ColorPaws

# Initialize (console only)
logger = ColorPaws(
    name="MyApp",        # Logger instance name
    log_on=True,         # Enable/disable logging
    log_to=None          # No file output
)

# Log messages
logger.debug("Debug information")     # Blue - Detailed debugging
logger.info("Operation complete")     # Green - General information
logger.warning("Low memory")          # Yellow - Potential issues
logger.error("Process failed")        # Red - Serious problems
logger.critical("System crash")       # Magenta - Critical failures
```

### File and Console Logging

```python
# Initialize (console + file)
logger = ColorPaws(
    name="MyApp",        # Logger instance name
    log_on=True,         # Enable/disable logging
    log_to="logs"        # Log directory path
)

# Example with exception handling
try:
    # Your code here
    logger.info("Processing started")
    logger.debug("Loading config...")
    raise ValueError("Invalid input")

except Exception as e:
    logger.error(
        "Process failed",
        exc_info=True    # Include stack trace
    )
```

### Log File Structure

```
logs/
└── YYYY-MM-DD/
    ├── YYYYMMDD_HHMMSS_MyApp.log
    ├── YYYYMMDD_HHMMSS_MyApp.log
    └── ...
```

## Configuration

### Parameters
| Parameter | Type  | Default | Description |
|-----------|-------|---------|-------------|
| name      | str   | Required| Logger name |
| log_on    | bool  | False   | Enable logging |
| log_to    | str   | None    | Log directory |

### Log Colors
| Level    | Color   | Usage |
|----------|---------|-------|
| DEBUG    | Blue    | Detailed debugging |
| INFO     | Green   | General messages |
| WARNING  | Yellow  | Potential issues |
| ERROR    | Red     | Serious problems |
| CRITICAL | Magenta | Critical failures |

### Log Format
Default: `YYYY-MM-DD HH:MM:SS - LEVEL - Message`

## Best Practices

```python
# Hierarchical naming
logger = ColorPaws("MyApp.SubModule")

# Proper level usage
logger.debug("Detailed debug info")    # Development
logger.info("Operation status")        # General
logger.warning("Potential issue")      # Caution
logger.error("Operation failed")       # Problems
logger.critical("System failure")      # Emergencies

# Exception handling
try:
    # Your code
except Exception as e:
    logger.error("Failed", exc_info=True)
```

## License

See [LICENSE](LICENSE) for details.
