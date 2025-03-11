from src.colorpaws import ColorPaws
import time

# This is a basic usage of the ColorPaws logging system
# - It creates a logger that outputs to both console and file
# - It then tests all log levels
# - It also tests multiple messages in sequence
# - It also tests the logger without file output

def test_logging():
    # Create a logger that outputs to both console and file
    logger = ColorPaws(
        name="test_app",
        log_on=True,
        log_to="logs"  # This will create a logs directory with date-based subdirectories
    )
    
    # Test all log levels
    logger.debug("This is a DEBUG message - useful for detailed information")
    logger.info("This is an INFO message - general information about program execution")
    logger.warning("This is a WARNING message - something unexpected happened")
    logger.error("This is an ERROR message - something failed but the program continues")
    logger.critical("This is a CRITICAL message - serious error that may prevent program execution")
    
    # Test multiple messages in sequence
    for i in range(3):
        logger.info(f"Processing item {i}")
        time.sleep(0.5)  # Add small delay to see messages appear
        
    # Test logger without file output
    console_logger = ColorPaws(
        name="console_only",
        log_on=True
    )
    console_logger.info("This message only goes to console")

if __name__ == "__main__":
    test_logging() 