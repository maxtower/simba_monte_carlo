import random
import numpy as np

print " Monte Carlo Simba's Spreadsheet"
returns = np.array([['VTSMX','16.67831121','-18.2553149','-27.33805769','38.43696976','26.45972652','-4.381674818','7.296137339','22.76674319','32.44834814','-3.882623016','20.57091526','21.76863958','4.30182653','31.94929634','15.87982833','1.507136441','17.77622517','28.65555445','-6.178261304','34.44455534','9.591775626','10.41022058','-0.17','35.79','20.96','30.99','23.26','23.81','-10.57','-10.97','-20.96','31.35','12.52','5.98','15.51','5.49','-37.04','28.7','17.09','0.96','16.25','33.35'],
['VIVAX','18.75062369','-3.802015767','-23.26115158','56.8705718','43.69823371','1.187506237','3.083524598','20.24748029','24.13930745','1.087715797','19.74852809','28.03113462','9.869274524','31.2244287','19.74852809','0.289392276','22.94182217','24.93763097','-8.29258557','24.33888833','13.56152081','18.10198583','-0.73','36.94','21.86','29.77','14.64','12.57','6.08','-11.88','-20.91','32.25','15.29','7.09','22.15','0.09','-35.97','19.58','14.28','1','15','32.85'],
['VFINX','18.78618487','-14.85326412','-26.63206229','36.95348373','23.67738071','-7.965661809','5.9','18','31.9','-5.2','20.9','21.3','6.21','31.23','18.06','4.71','16.22','31.36','-3.32','30.22','7.42','9.89','1.18','37.45','22.88','33.19','28.62','21.07','-9.06','-12.02','-22.15','28.5','10.74','4.77','15.64','5.39','-37.02','26.49','14.91','1.97','15.82','32.18'],
['VIGRX','21.23328677','-21.77210138','-29.35541808','33.9054081','17.5414089','-9.898223907','6.66533626','23.62801836','39.29355418','-11.49471163','20.23548194','15.74536021','-1.217321892','32.60826182','15.14667731','5.068848533','11.05567751','35.60167631','-0.518858511','40.89004191','4.769507084','1.53','2.89','38.06','23.74','36.34','42.21','28.76','-22.21','-12.93','-23.68','25.92','7.2','5.09','9.01','12.56','-38.32','36.29','16.96','1.71','16.89','32.16'],
['VIMSX','8.860506885','-26.66134504','-25.36419876','57.05448014','40.09179804','3.771702255','10.65655558','32.20913989','32.20913989','2.175214528','23.02933546','23.52823788','1.177409699','31.71023748','17.94053083','-0.019956097','19.53701856','26.02274995','-11.6942726','41.18938336','16.14448214','14.049092','-2.314907204','34.10496907','18.7387747','28.71682299','9.858311714','15.06685292','18.1','-0.5','-14.61','34.14','20.35','13.93','13.6','6.02','-41.82','40.22','25.46','-2.11','15.8','35'],
['VISVX','6.754464731','-26.16980944','-18.38770827','54.14546543','53.24753068','21.52050284','21.52050284','35.08929462','25.11224184','14.63633643','28.20512821','38.28195151','2.065249925','30.6993914','7.153546842','-7.313179687','29.20283348','12.14207323','-21.97944727','41.37483787','28.80375137','23.5159134','-1.726030131','25.51132395','21.12142073','31.49755562','-6.71455652','3.112840467','21.88','13.7','-14.2','37.19','23.55','6.07','19.24','-7.07','-32.05','30.34','24.82','-4.16','18.56','36.41'],
['NAESX','4.160431009','-31.0585653','-20.08380724','52.44936646','57.03881074','25.11224184','23.21660182','42.77162526','38.28195151','1.765938342','24.6133892','28.80375137','-7.512720742','30.79916193','5.45744787','-9.009278659','24.6133892','15.93335329','-19.68472513','45.7647411','17.92876384','18.7','-0.51','28.74','18.12','24.59','-2.61','23.13','-2.67','3.1','-20.02','45.63','19.9','7.36','15.64','1.16','-36.07','36.12','27.72','-2.8','18.04','37.62'],
['VISGX','3.462037314','-39.23974858','-33.55282849','62.82550135','43.17070737','20.02394493','18.32784595','50.4539559','51.95051382','-9.40836077','20.72233862','19.82440387','-15.9932156','30.6993914','3.362266786','-10.70537763','20.12371545','19.9241744','-17.58954405','50.85303801','7.552628953','13.13977851','-2.623964881','30.6993914','11.04459743','12.64092587','0.96777412','19.52509229','1.59','-0.78','-15.41','42.88','16.06','8.64','11.94','9.63','-40','41.85','30.69','-1.58','17.52','37.98'],
['BRSIX','-0.864209794','-42.08801033','-29.37319956','71.25260753','54.66375286','22.38005364','27.54544552','41.25360087','29.63146916','7.082546936','27.14810768','36.38621238','-20.03576041','24.86341512','-0.367537499','-15.46637529','19.99602662','4.797854376','-31.75722658','47.31300288','32.71083739','24.56541174','-3.546240191','29.23413132','16.02264826','20.69136784','-2.463494586','31.49','0.67','23.98','4.9','79.43','20.12','4.08','11.48','-5.4','-39.49','25.95','24.86','-7.86','19.83','50.91'],
['VGSIX','7.773675282','-15.67707814','-21.5647141','19.04999501','47.29068955','22.14349865','10.0688554','35.61520806','24.13930745','5.77786648','21.34517513','30.32631474','20.64664205','18.85041413','18.95020457','-3.802015767','13.26214949','8.571998803','-15.5772877','35.41562718','14.35984433','19.44915677','2.983734158','15.05837741','35.01646542','18.52110568','-16.32','-4.04','26.35','12.35','3.75','35.65','30.76','11.89','35.07','-16.46','-37.05','29.58','28.3','8.47','17.53','2.31'],
['VDMIX','35.93298095','-15.12915129','-23.40680164','35.03540441','2.223995213','17.78198863','32.24294405','4.517801935','22.26987135','-1.266580233','-1.166849506','24.26448589','7.609454473','56.27804927','69.44250524','24.56367807','28.25371497','10.50164556','-23.40680164','12.19706792','-12.03749875','32.54213623','7.808915927','11.29949137','6.113493567','1.825072305','19.97606463','26.95721552','-14.23157475','-22.2499252','-15.7','38.61','20.25','13.34','26.18','10.99','-41.62','28.17','8.54','-12.53','18.83','21.84'],
['VEIEX','49.57179845','-14.16052579','-25.6124278','43.59689305','6.851224856','49.97012547','52.95757817','2.170882294','26.2696674','4.162517427','-1.513642701','32.04540928','9.838677554','60.22704641','62.01951802','37.12407887','39.8127863','64.30989843','-10.97390958','59.23122884','10.93407688','74.06891058','-7.687711611','0.139414459','15.83','-16.82','-18.12','61.57','-27.56','-2.88','-7.43','57.65','26.12','32.05','29.39','38.9','-52.81','75.98','18.86','-19.18','18.64','-5.19'],
['VGTSX','37.98140439','-14.98367276','-23.73806616','36.32126031','2.918962036','22.61634718','35.35408929','4.165316449','22.87060348','-0.451180298','-1.218934616','25.43310816','7.944263031','56.87115188','68.32764165','26.45013336','29.98977989','18.5831443','-21.53949697','19.2611611','-8.587381908','38.77907122','5.48146671','9.623351696','7.500062318','-1.059401251','15.6','29.92','-15.61','-20.15','-15.08','40.34','20.84','15.57','26.64','15.52','-44.1','36.73','11.12','-14.56','18.14','15.04'],
['VPACX','106.991124','-21.16286028','-21.1528872','26.3787773','21.31245637','13.38386357','48.36940261','-3.739902264','36.01276553','8.018350454','-6.512416476','26.07958512','13.17442904','39.01466042','93.29809514','39.47342176','34.82596988','2.403510522','-34.46693926','10.35204947','-18.17','35.46','13.04','2.75','-7.82','-25.67','2.41','57.05','-25.74','-26.34','-9.32','38.42','18.83','22.59','11.99','4.78','-34.36','21.18','15.77','-14','15.49','17.36'],
['VEURX','15.28872045','-7.948538945','-23.00787873','43.51251621','-6.652039493','23.5663708','23.96529371','14.39114391','14.19168246','-10.64126857','5.415378478','22.07040989','1.027226488','79.31584721','44.11090057','3.819686846','16.08656627','28.7523686','-3.660117682','12.09733719','-3.32','29.13','1.88','22.28','21.26','24.23','28.86','16.62','-8.18','-20.3','-17.95','38.7','20.86','9.26','33.42','13.82','-44.73','31.91','4.91','-11.6','20.8','24.7'],
['VTRIX','36.32291459','-14.97113279','-22.88473024','38.35357356','2.856858451','29.39478399','42.01672307','5.504678479','18.20625124','8.490941668','-2.647820028','28.75771451','8.51085009','54.3997611','64.61278121','34.40175194','37.96535935','17.61895282','-21.98885128','10.29265379','-10.8','40.4','11.4','11.7','9.2','-4.58','19.46','21.81','-7.48','-14.02','-13.35','41.9','19.77','17.96','27.37','12.66','-41.74','33.77','7.31','-14.58','20.18','22.15'],
['PCRIX','38.69','68.4','4.1','5.11','-5.55','3.05','26.37','34.26','6.12','-22.52','3.84','12.24','-3.51','13.03','-6.19','17.91','18.5','27.72','25.13','3.77','6.587788365','6.420772021','5.891765365','24.28849685','18.34666641','-1.00292878','-25.30311044','19.65825457','35.83076588','-15.24858515','39.92969247','29.82','16.36','20.5','-3.04','23.8','-43.33','39.92','24.13','-7.56','5.31','-14.81'],
['VUSTX','5.425892679','-1.35647317','4.129263914','8.916816278','16.49710752','-0.957510473','-1.456213844','-1.456213844','-4.248952723','1.635747058','40.03590664','0.438858967','15.20047876','30.66028326','24.17713944','-3.181727508','9.15','17.93','5.78','17.43','7.4','16.79','-7.03','30.11','-1.25','13.9','13.05','-8.66','19.72','4.31','16.67','2.68','7.12','6.61','1.74','9.24','22.52','-12.05','8.93','29.28','3.47','-13.03','25.27'],
['VFITX','4.927189308','4.328745262','5.425892679','7.520446838','12.60722122','1.137043686','3.231597846','3.830041891','3.630560543','9.116297626','28.76521045','7.121484141','13.70436864','19.98803112','14.80151606','2.6331538','5.824855376','13.00618392','9.415519649','15.00099741','7.500498703','11.43','-4.33','20.44','1.92','8.96','10.61','-3.52','14.03','7.55','14.15','2.37','3.4','2.32','3.14','9.98','13.32','-1.69','7.35','9.8','2.67','-3.09'],
['VBMFX','5.489021956','3.193612774','6.786427146','8.083832335','11.47704591','2.794411178','1.996007984','6.387225549','6.387225549','10.57884232','25.1497006','7.984031936','14.07185629','17.76447106','12.8742515','0.938123752','7.35','13.64','8.65','15.25','7.14','9.68','-2.66','18.18','3.58','9.44','8.58','-0.76','11.39','8.43','8.26','3.97','4.24','2.4','4.27','6.92','5.05','5.93','6.42','7.56','4.05','-2.26'],
['VUSXX','3.551476457','6.64405427','7.741420591','5.546687949','4.848363927','4.848363927','6.943335994','10.13567438','11.03351955','14.42537909','10.23543496','8.539505188','9.537110934','7.37','6','6.12','7.18','8.87','7.94','5.73','3.53','2.86','3.81','5.49','5.09','5.12','5','4.55','5.8','3.99','1.51','0.82','1','2.77','4.55','4.65','1.97','0.53','0.01','0.02','0.02','0.01'],
['VIPSX','-2.594810379','-3.992015968','4.99001996','16.16766467','-0.299401198','7.784431138','9.680638723','9.780439122','15.16966068','5.788423154','-7.784431138','16.86626747','15.56886228','8.682634731','21.95608782','8.183632735','18.66267465','5.888223553','5.988023952','15.66866267','7.285429142','15.46906188','2.994011976','0.598802395','3.892215569','7.784431138','2.594810379','7.684630739','4.590818363','7.395209581','16.61','8','8.27','2.59','0.43','11.59','-2.85','10.8','6.17','13.24','6.78','-8.92'],
#['VWELX','10.65802592','-11.83','-17.73','25.18','23.36','-4.38','5.32','13.54','22.58','2.9','24.55','23.57','10.7','28.53','18.4','2.28','16.11','21.6','-2.81','23.65','7.93','13.52','-0.49','32.92','16.19','23.23','12.06','4.41','10.4','4.19','-6.9','20.75','11.17','6.82','14.97','8.34','-22.3','22.2','10.94','3.85','12.57','19.66'],
#['VWINX','9.476309227','-3.49','-6.43','17.46','23.28','4.27','3.61','6.2','11.88','8.67','23.3','18.6','16.64','27.41','18.34','-1.92','13.61','20.93','3.76','21.57','8.67','14.65','-4.44','28.91','9.42','20.19','11.84','-4.14','16.17','7.39','4.64','9.66','7.57','3.48','11.28','5.61','-9.84','16.02','10.65','9.63','10.06','9.19'],
#['VWNDX','9.804703069','-25','-16.8','54.5','46.4','1','8.8','22.6','22.6','16.8','21.7','30.1','19.47','28.03','20.27','1.23','28.7','15.02','-15.5','28.55','16.5','19.37','-0.15','30.15','26.36','21.97','0.81','11.57','15.89','5.72','-22.25','37.01','13.38','4.99','19.35','-3.3','-41.1','34.69','14.82','-4','20.78','36.08'],
['VFISX','3.630560543','5.824855376','8.817075603','7.620187512','8.617594255','3.431079194','5.226411331','10.11370437','13.80410932','18.59166168','19.19010573','8.318372232','12.50748055','12.90644325','11.60981448','5.725114702','5.625374028','8.418112906','8.617594255','10.41292639','6.473169759','6.41','-0.58','12.11','4.39','6.39','7.36','1.85','8.83','7.8','8.02','2.38','1.03','1.77','3.77','7.89','6.68','1.44','2.64','2.26','0.69','-0.1'],
['GLD','48.65909496','71.23812443','72.01885968','-27.62112173','-4.48189417','22.150802','36.4653541','125.6460882','14.72664031','-32.86709035','14.48545441','-16.63898139','-19.51649469','5.258577341','20.82431261','21.72047427','-15.59274161','-3.226824573','-1.860195945','-10.42830587','-6.122960029','17.2091448','-2.559513065','0.576168906','-4.966696521','-21.72137449','-1.222127342','0.449487664','-5.82030191','0.436294538','24.95636245','19.12316173','4.482731326','17.76','21.95','30.57','4.96','23.99','29.27','9.57','6.6','-28.33','-2.19'],
['VFSVX','63.43126866','-14.11729353','-28.98468657','49.11442786','10.90547264','73.21393035','64.70646766','-1.273631841','34.78606965','-0.39800995','-0.457711443','35.44278607','11.06467662','66.66666667','58.74626866','39.97014925','25.31343284','30.11940299','-18.34825871','5.303482587','-20.97512438','33.72139303','15.33333333','2.149253731','3.880597015','-14.55721393','25.98','90.29','-2.68','-22.52','-13.88','57.37','31.77','20.49','30.34','5.15','-46.62','47.12','24.97','-19.09','18.89','17.44']])

#print returns[0][0]
#print returns[5][1]

startYear = 1972
endYear = 2013


returnsT = np.transpose(returns)

#print returnsT[0]
#print returnsT[1]
std_port = 50
count = 0
sharpe = 0

while sharpe < 0.8 or mean_port < 9.5 or std_port > 6.7:
	count = count + 1
	total = 100
#	allocate = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	allocate = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	portfolio = []
	while total > 9:
		num = random.randint(0, 9)
		num2 = random.randint(0,len(returns)-1)
		allocate[num2] = allocate[num2] + num
		total = total - num
	
	num2 = random.randint(0, len(returns)-1)
	allocate[num2] = allocate[num2] + total
	#print allocate

	allocate = np.array(allocate, np.float)
	allocate = allocate / 100.0

	for i in range( 0, endYear-startYear):
		temp = np.array(returnsT[i+1], np.float)
		annualCombined = allocate * temp
		sum = np.sum(annualCombined)
		portfolio.append(sum)

	if count % 1000 == 0:
	    print count

	#print portfolio
	mean_port = np.mean(portfolio)
	std_port =  np.std(portfolio)
	sharpe = (mean_port - 5.15)/std_port


print allocate
for i in range(0, len(allocate)):
    if allocate[i] > 0:
        print "%s %f" % (returnsT[0][i], allocate[i] )
print "average %f" % (mean_port)
print "std dev %f" % (std_port)
print "sharpe  %f" % (sharpe)  
print count








