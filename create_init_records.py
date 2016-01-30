'''
create some init records for test
'''

from CCCMCMS.wsgi import *
from pastor.models import pastor
from report.models import report
from home.models import daily_motto
from fellowship.models import fellowship

def main():
    pastor_jin = pastor.objects.get_or_create(name = "靳士钊牧師", title = "中文牧師", )
    report_test = report.objects.get_or_create(title = "這只是一個報告測試")
    d_motto = daily_motto.objects.get_or_create(motto = "耶和華賜人智慧，知識和聰明都由祂口出。---每週背聖經計劃")
if __name__== '__main__':
    main()
    print("Done!")