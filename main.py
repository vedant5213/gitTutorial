import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,             # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',             # Save logs to a file
    filemode='a'                    # Append mode
)

# Example usage
logging.debug("This is a debug message")   # Ignored because level is INFO
logging.info("App has started")            # Logged
logging.warning("Something might be wrong") # Logged
logging.error("An error occurred")         # Logged
logging.critical("Critical issue!")        # Logged
