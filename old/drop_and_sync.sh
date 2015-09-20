#!/bin/sh

psql django_testdb testadmin << EOF
     drop table "type4_status";
     drop table "type4_card";
     \q
EOF
python manage.py syncdb