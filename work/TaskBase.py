import requests
import json
import random



header ={'content-type': 'application/json;charset=UTF-8','Cookie': 'SESSION=48e2d985-fb15-4603-9d93-7aabfeb59060'}
jsons = json.dumps({
    "fName": "事件名称" + str(random.randint(1, 998)),
	"fPlanType": str(random.randint(1, 4)),
	"fEventType": str(random.randint(1, 4)),
	"fArea": str(random.randint(1, 2)),
	"fScale": str(random.randint(1, 99999)),
	"fBidCompany": "申办单位" + str(random.randint(1, 998)),
	"fBidPersion": "申办人" + str(random.randint(1, 998)),
	"fBidContact": "1390514" + str(random.randint(1000, 9999)),
	"fMeal": "1",
	"fTaskDesc": "摘要"+str(random.randint(1,99999)),
	"fFileNotice": "",
	"fFilePolice": "",
	"fStartTime": "2019-1-9",
	"fEndTime": "2019-1-"+str(random.randint(9, 31))
}
)
r = requests.post('http://192.168.1.250/api/taskbase/addTaskBase', data=jsons, headers=header)
if r.json()['data']['detail']['taskId'] != None:
    print('添加序号：', r.json()['data']['detail']['taskId'])
else:
    print(r.json()['data']['resultMsg'])