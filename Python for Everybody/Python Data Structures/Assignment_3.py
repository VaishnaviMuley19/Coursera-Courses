""" Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution. """

# Use the file name mbox-short.txt as the file name 


fname = input("Enter file name: ")
fh = open(fname)
count=0
fl=0      #floating point number
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count=count+1
        pos=line.find('0')#position of number
        pos=int(pos)
        ext=line[pos:]   #extracting number
        fl=fl+float(ext)        #total of number
        avg= fl/count    #average of number

print('Average spam confidence:',avg)
