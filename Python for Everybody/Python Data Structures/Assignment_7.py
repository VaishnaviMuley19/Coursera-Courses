""" Write a program to read through the mbox-short.txt and figure out the distribution
by hour of the day for each of the messages. You can pull the hour out from the
'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted
by hour as shown below. """

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
word=list()
hour=list()
#time=list()

for line in handle:
    if line.startswith('From '):
        line=line.rstrip()
        line=line.split()
        word.append(line[5])
for time in word:
     time=time.split(':')
     hour.append(time[0])

for hr in hour:
    counts[hr]=counts.get(hr,0)+1

lst=list()
for k,v in counts.items():
    lst.append((k,v))

lst=sorted(lst)


for k,v in lst:
    print(k,v)
