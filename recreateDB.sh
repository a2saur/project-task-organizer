#!/bin/bash
rm -rf migrations
rm instance/database.db
echo "Removed migrations folder and db"

flask db init
flask db migrate -m "recreated db via shell script"
flask db upgrade
echo "Recreated empty db"

# cd setup-files
# python3 add_test_data.py
python3 import_test_data.py
echo "Done"