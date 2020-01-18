try:
    f = open('simple.txt' , 'w')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
