#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# from pypinyin import pinyin, lazy_pinyin
# import pypinyin

# Core Django imports

# Third-party app imports
from apps.BranchManager.models import Area
from apps.BranchManager.models import Department
from apps.BranchManager.models import DepartmentType

# Imports from your apps

aaa = """137001	分行营业部	fhyyb	fenhangyingyebu	分行本部	支行
137004	信用卡部	xyqb	xinyongqiabu	分行本部	分行部门
137011	中关村支行	zgc	zhongguancun	guowei	支行
137021	月坛支行	yt	yuetan	liuyu	支行
137031	亚运村支行	yyc	yayuncun	lilei	支行
137041	建国路支行	jgl	jianguolu	yangmingjian	支行
137051	新外支行	xw	xinwai	liuyu	支行
137061	朝阳门支行	cym	chaoyangmen	yangmingjian	支行
137071	西三环支行	xsh	xisanhuan	wanglei	支行
137081	国展支行	gz	guozhan	lilei	支行
137091	西客站支行	xkz	xikezhan	wanglei	支行
137101	甘家口支行	gjk	ganjiakou	liuyu	支行
137111	东直门支行	dzm	dongzhimen	lilei1	支行
137121	车公庄支行	cgz	chegongzhuang	liuyu	支行
137131	翠微路支行	cwl	cuiweilu	wanglei	支行
137141	方庄支行	fz	fangzhuang	lilei1	支行
137151	安贞支行	az	anzhen	lilei	支行
137161	太阳宫支行	tyg	taiyanggong	lilei	支行
137171	金融街支行	jrj	jinrongjie	liuyu	支行
137181	京广支行	jg	jingguang	lilei1	支行
137191	知春路支行	zcl	zhichunlu	guowei	支行
137201	王府井支行	wfj	wangfujing	yangmingjian	支行
137211	奥运村支行	ayc	aoyuncun	guowei	支行
137221	黄寺支行	hs	huangsi	liuyu	支行
137231	天通苑支行	tty	tiantongyuan	lilei	支行
137241	莲花支行	lh	lianhua	wanglei	支行
137251	大望路支行	dwl	dawanglu	lilei1	支行
137261	望京支行	wj	wangjing	lilei	支行
137271	潘家园支行	pjy	panjiayuan	lilei1	支行
137281	上地支行	sd	shangdi	guowei	支行
137291	国贸支行	gm	guomao	yangmingjian	支行
137301	中轴路支行	zzl	zhongzhoulu	lilei	支行
137311	广渠门支行	gqm	guangqumen	lilei1	支行
137321	五棵松支行	wks	wukesong	wanglei	支行
137331	万达广场支行	wdgc	wandaguangchang	yangmingjian	支行
137341	宣武门支行	xwm	xuanwumen	wanglei	支行
137351	学院路支行	xyl	xueyuanlu	guowei	支行
137361	海淀支行	hd	haidian	guowei	支行
137371	日坛支行	rt	ritan	yangmingjian	支行
137381	西单支行	xd	xidan	wanglei	支行
137391	动物园地铁支行	dwydt	dongwuyuanditie	liuyu	支行
137401	大红门支行	dhm	dahongmen	yangmingjian	支行
137411	万柳支行	wl	wanliu	guowei	支行
137421	安立路支行	all	anlilu	lilei	支行
137431	东二环支行	deh	dongerhuan	yangmingjian	支行
137441	石景山支行	sjs	shijingshan	wanglei	支行
137451	西直门支行	xzm	xizhimen	liuyu	支行
137461	工体支行	gt	gongti	lilei1	支行
137471	世纪城支行	sjc	shijicheng	guowei	支行
137481	朝阳北路支行	zybl	zhaoyangbeilu	lilei1	支行
137491	顺义支行	sy	shunyi	lilei	支行
137501	双井支行	sj	shuangjing	lilei1	支行
137511	夕照寺街社区支行	xzsj	xizhaosijieshequ	lilei1	社区支行
137521	花园路社区支行	hyl	huayuanlushequ	liuyu	社区支行
137531	龙旗广场社区支行	lqgc	longqiguangchangshequ	guowei	社区支行
137541	翠城社区支行	cc	cuichengshequ	lilei1	社区支行
137551	文慧桥社区支行	whq	wenhuiqiaoshequ	liuyu	社区支行
137552	马家堡社区支行	mjb	majiabaoshequ	yangmingjian	社区支行
137801	行长室	hzs	hangzhangshi	行领导	分行部门
137802	办公室	bgs	bangongshi	分行本部	分行部门
137803	人力资源部	rlzyb	renliziyuanbu	分行本部	分行部门
137806	信息技术部	xxjsb	xinxijishubu	分行本部	分行部门
137809	计划财务部	jhcwb	jihuacaiwubu	分行本部	分行部门
137810	运营部	yyb	yunyingbu	分行本部	分行部门
137813	信贷审查部	xdszb	xindaishenzhabu	分行本部	分行部门
137815	党群工作部	dqgzb	dangqungongzuobu	分行本部	分行部门
137816	监察室	jcs	jianchashi	分行本部	分行部门
137817	保卫部	bwb	baoweibu	分行本部	分行部门
137818	资产保全部	zcbqb	zichanbaoquanbu	分行本部	分行部门
137819	法律与合规部	flyhgb	falvyuheguibu	分行本部	分行部门
137820	信用卡部	xyqb	xinyongqiabu	分行本部	分行部门
137821	个人银行部	gryhb	gerenyinhangbu	分行本部	分行部门
137822	公司银行部	gsyhb	gongsiyinhangbu	分行本部	分行部门
137823	零售风险管理部	lsfxglb	lingshoufengxianguanlibu	分行本部	分行部门
137824	网络金融部	wljrb	wangluojinrongbu	分行本部	分行部门
137825	小企业金融部	xqyjrb	xiaoqiyejinrongbu	分行本部	分行部门
137826	金融机构部	jrjgb	jinrongjigoubu	分行本部	分行部门
137827	金融市场部	jrscb	jinrongshichangbu	分行本部	分行部门
137828	环球交易服务部	hqjyfwb	huanqiujiaoyifuwubu	分行本部	分行部门
137852	信贷管理部	xdglb	xindaiguanlibu	分行本部	分行部门
137854	私人银行部	sryhb	sirenyinhangbu	liuyu	分行部门
137901	票据中心	pjzx	piaojuzhongxin	分行本部	分行部门
137902	合规部	hgb	heguibu	分行本部	分行部门
137913	个贷中心	gdzx	gedaizhongxin	分行本部	分行部门
100001	总行代表处	zhdbc	zonghangdaibiaochu	总行驻京	总行部门
100002	总行资产托管部	zhzctgb	zonghangzichantuoguanbu	总行驻京	总行部门
100003	总行金融机构部	zhjrjgb	zonghangjinrongjigoubu	总行驻京	总行部门
100004	北方区域信贷审批中心	bfqyxdspzx	beifangquyuxindaishenpizhongxin	总行驻京	总行部门
100005	北京稽核中心	bjjhzx	beijingjihezhongxin	总行驻京	总行部门
100006	总行公司银行部	zhgsyhb	zonghanggongsiyinhangbu	总行驻京	总行部门
100007	总行战略管理部	zhzlglb	zonghangzhanlveguanlibu	总行驻京	总行部门
"""

bbb = aaa.splitlines()

for b in bbb:
    ccc = b.split('\t')
    try:
        t, created_t = DepartmentType.objects.get_or_create(title=ccc[5])
        a, created_a = Area.objects.get_or_create(title=ccc[4])
        d, created_d = Department.objects.get_or_create(title=ccc[1], dot_code=ccc[0], for_short=ccc[2], pinyin=ccc[3], area=a, type=t)
        print(created_t, created_a, created_d)
    except:
        pass

