import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['Employee']

information = mydb.employeeinformation

record=[{
    'firstname': 'Chandan',
    'lastname': 'Soren',
    'department': 'Mechanical'
},
{
    'firstname': 'Chandan1',
    'lastname': 'Soren1',
    'department': 'Mechanical1'
},
{
    'firstname': 'Chandan2',
    'lastname': 'Soren2',
    'department': 'Mechanical2'
}]
information.insert_many(record)