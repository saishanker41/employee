import pymysql



endpoint = 'firstdatabase.cp4xov0xf6a7.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'password'
database_name = 'employee_details'

connection = pymysql.connect(endpoint, user=username, passwd=password, db=database_name)
def lambda_handler():
	cursor = connection.cursor()
	cursor.execute("select * from employee")
	rows = cursor.fetchall()
	result=[]
	for r in rows:
		e={}
		e['employee_id']=r[0]
		e['employee_name']=r[1]
		e['employee_salary']=r[2]
		#print(e)
		result.append(e)
	employee_id = event['']	#print(f"employee_id: '{r[0]}' employee_name: '{r[1]}' employee_salary: '{r[2]}' ")
	ro={}
	ro['statusCode'] = 200
	ro['headers'] {}
	ro['headers']['context-Type'] = 'application/json'
	ro['body']= result
	return ro	


