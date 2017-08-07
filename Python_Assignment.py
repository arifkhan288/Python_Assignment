import glob, os
import datetime


class Assignment:

    def __init__(self):

        print ("")


    def getmulfile1(self,path,filename):

        self.filename=filename
        self.path = path

        mylist=[]
        os.chdir(path)

        for file in glob.glob("*"+filename+"*"):
            mylist.append(file)

        return self.findreport_year(mylist)

    def averageof(self, lst, stra, strb):

        sum = 0
        for i in range(0, len(lst)):
            if lst[i] != '':
                sum = sum + lst[i]
        avg = sum / len(lst)

        print(stra, avg, strb)

    def graphchart(self, high_temlist, low_templist, listdate):

        self.high_temlist = high_temlist
        self.listm = low_templist
        self.listdate = listdate

        for i in range(0, len(high_temlist)):
            print(listdate[i], " ", end='')

            if high_temlist[i] != '':
                for j in range(0, high_temlist[i]):
                    print("\033[31m+", end='')
                print(" \033[37m", high_temlist[i], 'C')

            else:
                print(0, "C")

            print(listdate[i], " ", end='')

            if low_templist[i] != '':
                for k in range(0, low_templist[i]):
                    print("\033[34m+", end='')
                print("\033[37m", low_templist[i], 'C')

            else:
                print(0, "C")


    def graphchart1(self, high_temlist, low_templist, listdate):

        self.listn = high_temlist
        self.listm = low_templist
        self.listdate = listdate

        for i in range(0, len(high_temlist)):
            print(listdate[i], " ", end='')

            if low_templist[i] != '':
                for j in range(0, low_templist[i]):
                    print("\033[34m+", end='')
                print("\033[37m", end='')
            else:
                print(end='')

            if high_temlist[i] != '':
                for k in range(0, high_temlist[i]):
                    print("\033[31m+", end='')
                print(" \033[37m", low_templist[i],"-",high_temlist[i], 'C')
            else:
                print(low_templist[i],"-",high_temlist[i],"C")


    def makinglist(self, list):

        self.list = list

        for i in range(0, len(list)):
            if list[i] != '':
                list[i] = int(list[i])
        return list


    def findreport_year(self, mylist1):

        self.mylist1 = mylist1
        #print(mylist)
        month = []
        maxtamp = []
        mintamp = []
        maxhumi = []
        for i in range(0, len(mylist1)):

            file = open(mylist1[i], "r")

            datelist = []
            h_temp = []
            l_temp = []
            h_humi = []

            for line in file:
                date = line.split(",")[0]
                x = line.split(",")[1]
                y = line.split(",")[3]
                z = line.split(",")[7]

                #Making list in list
                if x != "Max TemperatureC":
                    datelist.append(date)
                    h_temp.append(x)
                    l_temp.append(y)
                    h_humi.append(z)

            self.makinglist(h_temp)
            self.makinglist(l_temp)
            self.makinglist(h_humi)

            tamp_list = []
            date_list1 = []
            for i in range(0, len(h_temp)):
                if h_temp[i] != '':
                    tamp_list.append(h_temp[i])
                    date_list1.append(datelist[i])

            tamp_list = []
            date_list2 = []
            for i in range(0, len(l_temp)):
                if l_temp[i] != '':
                    tamp_list.append(l_temp[i])
                    date_list2.append(datelist[i])

            humi_list = []
            date_list3 = []
            for i in range(0, len(l_temp)):
                if h_humi[i] != '':
                    humi_list.append(h_humi[i])
                    date_list3.append(datelist[i])

            month.append(date_list1[(tamp_list.index(max(tamp_list)))])
            maxtamp.append(max(tamp_list))

            month.append(date_list2[(tamp_list.index(max(tamp_list)))])
            mintamp.append(min(tamp_list))

            month.append(date_list3[(humi_list.index(max(humi_list)))])
            maxhumi.append(max(humi_list))

        print("Highest:", max(maxtamp), "C", " on", month[maxtamp.index(max(maxtamp))])
        print("Lowest:", min(mintamp), "C", "  on", month[mintamp.index(min(mintamp))])
        print("Highest:", max(maxhumi), "%", "on", month[maxhumi.index(min(maxhumi))])


    def findreporttask2(self,path,filename):

        self.path = path
        self.filename = filename

        mylist=[]
        os.chdir(path)
        for file in glob.glob("*"+filename+"*"):
            mylist.append(file)

        file = open(mylist[0], "r")

        h_temp = []
        l_temp = []
        h_humi = []
        for line in file:
            x = line.split(",")[1]
            y = line.split(",")[3]
            z = line.split(",")[8]


            #Making list in list
            if x != "Max TemperatureC":
                h_temp.append(x)
                l_temp.append(y)
                h_humi.append(z)

        self.makinglist(h_temp)
        self.makinglist(l_temp)
        self.makinglist(h_humi)

        self.averageof(h_temp, "Avg Highest Temprature ", "C")
        self.averageof(l_temp, "Avg Lowest Temprature  ", "C")
        self.averageof(h_humi, "Average Mean Humidity ", "%")

    def findreporttask3(self,path,filename):

        self.path = path
        self.filename = filename

        mylist=[]
        os.chdir(path)
        for file in glob.glob("*"+filename+"*"):
            mylist.append(file)

        file = open(mylist[0], "r")

        h_temp = []
        l_temp = []
        date_list = []

        for line in file:
            x = line.split(",")[1]
            y = line.split(",")[3]
            z = line.split(",")[0]

            #Making list in list
            if x != "Max TemperatureC":
                h_temp.append(x)
                l_temp.append(y)
                date_list.append(z)

        self.makinglist(h_temp)
        self.makinglist(l_temp)

        self.graphchart(h_temp, l_temp, date_list)


    def findreporttask5(self,path,filename):

        self.path = path
        self.filename = filename

        mylist=[]
        os.chdir(path)
        for file in glob.glob("*"+filename+"*"):
            mylist.append(file)

        file = open(mylist[0], "r")

        h_temp = []
        l_temp = []
        date_list = []

        for line in file:
            x = line.split(",")[1]
            y = line.split(",")[3]
            z = line.split(",")[0]

            #Making list in list
            if x != "Max TemperatureC":
                h_temp.append(x)
                l_temp.append(y)
                date_list.append(z)

        self.makinglist(h_temp)
        self.makinglist(l_temp)

        self.graphchart1(h_temp, l_temp, date_list)

    def find_filename(self,name):

        list=name.split(" ")
        name_of_month=list[1]
        month1 = name_of_month.split("/")


        month_integer = int(month1[1])
        month = datetime.date(1900, month_integer, 6).strftime('%B')


        splits=[month[x:x+3] for x in range(0,len(month),3)]

        year = month1[0]
        filename = year+'_'+splits[0]

        return filename



if __name__ == '__main__':

    class_obj = Assignment()

    mulit_report = int(input("For Multiple report enter 1 or Single report 2  "))

    if mulit_report == 2:
        path = input("Enter complete path for geeting file from dir : ")
        Name_of_year = input("Enter name of Year for all files : ")

        list=Name_of_year.split(" ")


        if list[0]=="-e":

            class_obj.getmulfile1(path,list[1])

        elif list[0]=="-a":

            filename = class_obj.find_filename(Name_of_year)
            class_obj.findreporttask2(path,filename)

        elif list[0]=="-c":

            filename = class_obj.find_filename(Name_of_year)
            class_obj.findreporttask3(path,filename)

        elif list[0]=="-d":
            filename = class_obj.find_filename(Name_of_year)
            class_obj.findreporttask5(path,filename)
        else:
            print("Wrong Input")

    elif mulit_report == 1:
        path = input("Enter complete path for geting file from dir : ")
        year_report = input("Enter name of files for report : ")
        month = input("")
        month_graph = input("")
        month_graph1 = input("")

        for_year = year_report.split(" ")
        for_month=month.split(" ")
        for_month_graph=month_graph.split(" ")
        for_month_graph1=month_graph1.split(" ")

        print("\nReport of complete year\n")
        class_obj.getmulfile1(path,for_year[1])

        print("\nReport of complete month\n\n")
        filename = class_obj.find_filename(month)
        class_obj.findreporttask2(path,filename)

        print("\nReport of complete month in Graph\n\n")
        filename = class_obj.find_filename(month_graph)
        class_obj.findreporttask3(path,filename)

        print("\nReport of complete month in Graph Form\n\n")
        filename = class_obj.find_filename(month_graph1)
        class_obj.findreporttask5(path,filename)

    else:
        print("Plz Correct Number")








