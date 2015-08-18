#!/bin/bash
source /home/fieldinhand/virtuanenv_for_backend/bin/activate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -9
uwsgi --ini /home/fieldinhand/field_in_hand_server/uwsgi.ini
