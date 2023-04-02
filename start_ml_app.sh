mysql_open=false
while [ "$mysql_open" != "true" ]; do
    nc -v -z -w 1 mysql_ml_app_db 3306
    command_result=$?
    if [ $command_result == 0 ]; then
        echo "MySQL is started, running ml_app"
        sh -c "mysql -u root -p123senha -h mysql_ml_app_db < bds_classification.sql && python main.py"
        mysql_open=true
    else
        echo "MySQL is still down, trying again..."
        mysql_open=false
    fi
done