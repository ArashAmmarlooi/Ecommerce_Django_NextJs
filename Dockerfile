# Use an official MySQL image as a parent image
FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=arayeshi
ENV MYSQL_USER=arash
ENV MYSQL_PASSWORD=1234
COPY my.cnf /etc/mysql/conf.d/

# Expose the MySQL port
EXPOSE 3306

# Other instructions...

# The CMD instruction is provided by the base MySQL image
CMD ["mysqld"]
