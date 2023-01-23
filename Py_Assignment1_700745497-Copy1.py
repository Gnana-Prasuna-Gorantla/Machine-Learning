#!/usr/bin/env python
# coding: utf-8

# In[29]:


import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24];
#Sort the list and find the min and max age
ages.sort() #sorting
print("Minimum age = ",min(ages))#Min
print("Maximum age = ",max(ages))#Max
#Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print("Adding Min and Max ",ages)#adding min and max
#Find the median age (one middle item or two middle items divided by two)
print("Median = ",statistics.median(ages))
#Find the average age (sum of all items divided by their number)
def average(ages):
    return sum(ages)/len(ages)
average=average(ages)
print("Average = ",average)
#Find the range of the ages (max minus min)
print("Range =",max(ages)-min(ages))


# In[55]:


#Create an empty dictionary called dog
dog={}#dict()
#Add name, color, breed, legs, age to the dog dictionary
dog["name"]="Rolo"
dog["color"]="grey"
dog["breed"]="Little Lion Dog"
dog["legs"]="shot"
dog["age"]="2 yrs"
print("Dog Dictionary =",dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
  "first_name": "James",
  "last_name": "Gosling",
  "gender": "Male",
  "age": 52,
  "marital status": "Married",
  "skills": ["Java", "HTML", "CSS"],
  "country": "United States",
  "city": "Denton",
  "address": "Apt no:1234, random Street",
}
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
student["skills"] 
print(student["skills"])
print(type(student["skills"]))
#Modify the skills values by adding one or two skills
student["skills"] =["Java", "HTML", "CSS", "Python", "SQL"]
print(student["skills"])
#Get the dictionary keys as a list
print(list(student.keys()))
#Get the dictionary values as a list
print(list(student.values()))


# In[62]:


#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=("Sushma","Supraja")
brothers=("Sai","Bhargav")
#Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to 
family_members
siblings+("Renuka","Peddabbai")
family_members=siblings+("Renuka","Peddabbai")
print(family_members)


# In[117]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
addcomp=["TCS","Infosys"]
it_companies.update(addcomp)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.discard("Infosys")
print(it_companies)
#What is the difference between remove and discard
#join A and B
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
subAB=joinAB
print(subAB)
#Are A and B disjoint sets
print(A.isdisjoint(B))
C=A.union(B)
D=B.union(A)
print(A.symmetric_difference(B))
del it_companies
del A
del B
ages=set(age-)
print(type(ages))


# In[94]:


#Hardcoded radius
r=30
area_of_circle_=3.14*pow(r,2)
print("Area of Circle is ",area_of_circle_)
circum_of_circle_=2*3.14*r
print("circumference of Circle is ",circum_of_circle_)

#user provided radius
radius=int(input("Enter the radius of the circle : "))
_area_of_circle_=3.14*pow(radius,2)
print("Area of Circle with the user input is ",_area_of_circle_)
_circum_of_circle_=2*3.14*radius
print("circumference of Circle with the user input is ",_circum_of_circle_)


# In[98]:


sentence="I am a teacher and I love to inspire and teach people"

def uniqueWords(sentence):
    words = sentence.replace('"','').replace(',', '').split()
    unique = set(words)
    return unique

uniqueWords(text)


# In[121]:


print("Name\tAge\tCountry\tCity") 
print("Asabeneh\t250\tFinland\tHelsinki")


# In[106]:


radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square."%(radius, area))


# In[120]:


n=int(input("enter number of students ="))
lbs=[]
kgs=[]
lb=0.453592
for x in range(n):
    #print(x)
    a=int(input("enter weight in lbs:"))
    lbs.append(a)
for y in lbs:
    #print(x)
    b=y*lb
    kgs.append(b)
print(kgs)


# In[115]:





# In[ ]:




