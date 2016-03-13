#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# from pypinyin import pinyin, lazy_pinyin
# import pypinyin

# Core Django imports

# Third-party app imports
from apps.BranchManager.models import Department
from apps.IPAddress.models import Subnet

# Imports from your apps

aaa = """10.74.10.0	双井	PRD
10.74.11.0	顺义	PRD
10.74.12.0	朝阳北路	PRD
10.74.13.0	世纪城	PRD
10.74.14.0	工体	PRD
10.74.15.0	西直门	PRD
10.74.16.0	石景山	PRD
10.74.17.0	东二环	PRD
10.74.18.0	安立路	PRD
10.74.19.0	万柳	PRD
10.74.20.0	大红门	PRD
10.74.21.0	西单	PRD
10.74.22.0	日坛	PRD
10.74.23.0	海淀	PRD
10.74.24.0	学院路	PRD
10.74.25.0	动物园	PRD
10.74.26.0	私人银行部	PRD
10.74.27.0	宣武门	PRD
10.74.28.0	万达	PRD
10.74.29.0	五棵松	PRD
10.74.30.0	广渠门	PRD
10.74.31.0	中轴路	PRD
10.74.32.0	国贸	PRD
10.74.33.0	中关村	PRD
10.74.34.0	月坛	PRD
10.74.35.0	亚运村	PRD
10.74.36.0	建国路	PRD
10.74.37.0	新外	PRD
10.74.38.0	朝阳门	PRD
10.74.39.0	西三环	PRD
10.74.40.0	国展	PRD
10.74.41.0	西客站	PRD
10.74.42.0	甘家口	PRD
10.74.43.0	东直门	PRD
10.74.44.0	车公庄	PRD
10.74.45.0	翠微路	PRD
10.74.46.0	方庄	PRD
10.74.47.0	安贞	PRD
10.74.48.0	太阳宫	PRD
10.74.49.0	金融街	PRD
10.74.52.0	京广	PRD
10.74.53.0	知春路	PRD
10.74.54.0	王府井	PRD
10.74.55.0	奥运村	PRD
10.74.56.0	黄寺	PRD
10.74.57.0	天通苑	PRD
10.74.58.0	莲花	PRD
10.74.59.0	大望路	PRD
10.74.64.0	望京	PRD
10.74.66.0	潘家园	PRD
10.74.67.0	上地	PRD
10.75.10.0	双井	OA
10.75.11.0	顺义	OA
10.75.12.0	朝阳北路	OA
10.75.13.0	世纪城	OA
10.75.14.0	工体	OA
10.75.15.0	西直门	OA
10.75.16.0	石景山	OA
10.75.17.0	东二环	OA
10.75.18.0	安立路	OA
10.75.19.0	万柳	OA
10.75.20.0	大红门	OA
10.75.21.0	西单	OA
10.75.22.0	日坛	OA
10.75.23.0	海淀	OA
10.75.24.0	学院路	OA
10.75.25.0	动物园	OA
10.75.26.0	私人银行部	OA
10.75.27.0	宣武门	OA
10.75.28.0	万达	OA
10.75.29.0	五棵松	OA
10.75.30.0	广渠门	OA
10.75.31.0	中轴路	OA
10.75.32.0	国贸	OA
10.75.33.0	中关村	OA
10.75.34.0	月坛	OA
10.75.35.0	亚运村	OA
10.75.36.0	建国路	OA
10.75.37.0	新外	OA
10.75.38.0	朝阳门	OA
10.75.39.0	西三环	OA
10.75.40.0	国展	OA
10.75.41.0	西客站	OA
10.75.42.0	甘家口	OA
10.75.43.0	东直门	OA
10.75.44.0	车公庄	OA
10.75.45.0	翠微路	OA
10.75.46.0	方庄	OA
10.75.47.0	安贞	OA
10.75.48.0	太阳宫	OA
10.75.49.0	金融街	OA
10.75.52.0	京广	OA
10.75.53.0	知春路	OA
10.75.54.0	王府井	OA
10.75.55.0	奥运村	OA
10.75.56.0	黄寺	OA
10.75.57.0	天通苑	OA
10.75.58.0	莲花	OA
10.75.59.0	大望路	OA
10.75.64.0	望京	OA
10.75.66.0	潘家园	OA
10.75.67.0	上地	OA
"""

bbb = aaa.splitlines()

for b in bbb:
    ccc = b.split('\t')
    s, created_t = Subnet.objects.get_or_create(subnet_address=ccc[0])
    try:
        d = Department.objects.filter(title__contains=ccc[1]).get()
        s.department = d
        s.summary = d.title + "(%s)" % ccc[2]
        s.save()
    except:
        pass
    print(ccc[0])
