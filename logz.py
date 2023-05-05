import pandas as pd
import os
import uuid
import datetime
import pickle
import getpass
from cryptography.fernet import Fernet

_path = r'/home/angary/Documents/python_programming/python_files/logs/'





logz_template = {'title'    : 'Test Log',
		 'date'     : str(datetime.datetime.now()),
		 'log_id'   : str(uuid.uuid4()),
		 'encrypted': False,
		 'log'      : ['This is Line 1', 'This is Line 2']}
		 



def write_log():
	os.system('clear')
	log_date = str(datetime.datetime.now())
	log_id = str(uuid.uuid4())
	encryption_status = False
	log = []
	print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	log_name = input('title     : ')
	log_type = input('log_type  : ')
	print('date      : '    + log_date)
	print('log_id    : '    + log_id)
	print('encrypted : ' + str(encryption_status))
	print('----------------------------------------------------------------------------')
	while True:
		line = input('')
		log.append(line)
		if line == '/log':
			break
	log = {'title' : log_name,
		'log_type' : log_type,
		 'date'  : log_date,
		 'log_id': log_id,
		 'encrypted' : encryption_status,
		 'log'   : log}
	pickle.dump(log, open('/home/angary/Documents/python_programming/python_files/logs/%s.p' % log_id, 'wb'))




def create_log_df():
	files = os.walk(_path)
	files = [file for file in files][0][2]
	data = {'log_name' : [], 'log_type' : [], 'log_date' : [], 'log_id' : [], 'encryption_status' : []}
	for filename in files:
		file = pickle.load(open(_path + filename, 'rb'))
		data['log_name'].append(file['title'])
		data['log_type'].append(file['log_type'])
		data['log_date'].append(file['date'])
		data['log_id'].append(file['log_id'])
		data['encryption_status'].append(file['encrypted'])
	return pd.DataFrame(data)
	



def read_log(log):
	os.system('clear')
	print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print('title     : ' + log['title'])
	print('log_type  : ' + log['log_type'])
	print('date      : ' + log['date'])
	print('log_id    : ' + log['log_id'])
	print('encrypted : ' + str(log['encrypted']))
	print('----------------------------------------------------------------------------')
	for line in log['log']:
		print(line)
		




write_log()

intro_string = """
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
%s| WRITE
%s| ARCHIVE
%s| EXIT
"""

current_position = 0
while True:
	os.system('clear')
	selection_list = []
	for i in range(3):
		if current_position == i:
			selection_list.append('>>')
		else:
			selection_list.append('  ')
	print(intro_string % ((str(datetime.datetime.now()), getpass.getuser()) + tuple(selection_list)))
	key = getkey.getkey()
	if key == '\x1b[A' and current_position != 0:
		current_position -= 1
	if key == '\x1b[B' and current_position != 2:
		current_position += 1
	if key == '\n':
		break	





#write_log()
#read_log(log)
os.system('clear')
files = create_log_df()
print(files)


#fernet_key_file = {str(uuid.uuid4()) : str(Fernet.generate_key())}
#print(fernet_key_file)

		 

		 
		 

