set DJANGO_SETTINGS_MODULE=mysite.settings_dev
python  manage.py rqworker high default low  --worker-class=rq_win.WindowsWorker
