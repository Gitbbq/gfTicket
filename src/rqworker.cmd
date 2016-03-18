set DJANGO_SETTINGS_MODULE=mysite.settings_dev
python  manage.py rqworker high default low ping_subnet reverse_subnet --worker-class=rq_win.WindowsWorker
