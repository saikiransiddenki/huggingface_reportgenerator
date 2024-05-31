FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy Python script into the container
COPY report_generator.py /app/report_generator.py

# Install dependencies
RUN pip install requests

# Install cron
RUN apt-get update && apt-get install -y cron

# Copy cron job file
COPY cronjob /etc/cron.d/report-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/report-cron

# Update crontab
RUN crontab /etc/cron.d/report-cron

# Create log file for cron
RUN touch /var/log/cron.log

# Run cron
CMD ["cron", "-f"]
