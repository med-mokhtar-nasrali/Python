x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(x[1][0])
x[1][0]=15
print(x[1][0])
students[0]['last_name']="Bryant"
print(students[0]['last_name'])
sports_directory['soccer'][0]="Andres"
print(sports_directory['soccer'][0])
z[0]['y']=30
print(z[0]['y'])

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for student in some_list:
        for key in student:
            print(f"{key} - {student[key]}")
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(student[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print()
printInfo(dojo)  