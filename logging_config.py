import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# logger.debug("Detailed debugging information")

# logger.info("Normal application event")

# logger.warning("Something unusual happened")

# logger.error("Something failed")

# logger.exception("Database operation failed")