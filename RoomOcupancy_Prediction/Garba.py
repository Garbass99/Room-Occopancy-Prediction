
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import os
from datetime import datetime
import joblib

#Project Builder

def Projfolder(maindirect, projName, folderindx):
    ''' this is the function for nuilding project just provide the maindirectory, project name as projName then the folder index 
    as folderindx ranging from [0,1,2,3,4,5,6] with respect to list ['data', 'outcome', 'notebook','transformations','resources', 'visualizations', 'model'].
    'ext' these the extension to which file type are you saving your file, excel xls, .csv, .pkl etc'''
    dirlist = ['data', 'outcome', 'notebook','transformations','resources', 'visualizations', 'model']
    os.chdir(maindirect)
    os.makedirs(projName)
    newDir = maindirect + "/" + projName 
    
    os.chdir(newDir)

    for index in folderindx:
        os.makedirs(dirlist[index])
#fileloader


#Fileloader
def fileloder(path, fileName, ext):
    '''Fileloader this function i build to help access and load data from the directory given as 'path',
    provide path, filename adnd the extention to read file'''
    if ext == '.csv':
        return pd.read_csv(path + '/'+fileName+ ext)
    elif ext == 'xlsx' or 'xls':
        return pd.read_xlsx(path + '/'+fileName+ ext)

#Checking for overall information of the data
''' Checking data information, pass data to function to see the information'''
def DataInformation(data):
    info = data.info()
    return info
#checking for missing values
def Missingvals(data):
    ''' this is a helperfuction to detect missing values
    Pass the data to see the missing values'''
    
    missing = data.isna().sum()

    sn.heatmap(data.isin(missing))

    #saving visualization
    
    savepath = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\visualizations"
    filename = 'missing valuues from room occupancy'
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.tight_layout()
    plt.show()
    plt.close()
    return missing



def Outlierdetect(data, savepath, filename):
    #Checking for Outliers in the data
    '''Outlierdetect Outliers detector detects the graphical representtation of the Outliers in the data
    Pass the data to the function'''
    Outlier = data.plot(kind='box', subplots = True, layout = (4,4), sharey = False, sharex = False)
    plt.gcf().set_size_inches(20,20)
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.show()
    plt.close()
    return Outlier

def VisualSkewdetect(data, savepath, filename):
    #Checking for Outliers in the data
    '''Visually detect show skewed the distribution of your numeric features.
    Pass the data to the function'''
    skew = data.plot(Density='box', subplots = True, layout = (4,4), sharey = False, sharex = False)
    plt.gcf().set_size_inches(20,20)
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.show()
    plt.close()
    return skew
    


def duplicatesdetect(file,savepath,filename, ext ):
    #checking for duplicates in the data
    r'''duplicatesdetect detecting and saving duplicates in the data
    import duplicatesdetect() and pass the data
    file = name of the data you want to check duplicate
    savepath = the path to save the duplicates before droping e.g r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\output
    ext = the extension it should be either csv or xlsx'''

    duplicate = data[data.duplicated()]
    if ext =='.csv':
        duplicate.to_csv(savepath +'/' + filename+ ext)
    elif ext =='.xlsx' or 'xls':
        duplicate.to_xlsx(savepath + '/' + filename + ext)
    
    return duplicate
#checking for the descriptive statistics of the continues variables

def Descriptivestat(data):
    ''' This diplays the Descrptivestat descriptive Statistics of this data 
    pass the data to the function'''  
    descrptive = df.describe()
    return descrptive

def duptreatment(data):
    ''' call the function and pass your data to treat duplicates by dropping the second duplicate values and keeping the first copy'''

    Nodups = data.drop_duplicates()
    return Nodups
    
    

def fileSaver(file, fileName, Dest, ext ):
    '''This is a helper function that help save files of different extensions with timestamp
    Provide and assign a variable name to the file wanted to save, then the name you want to save it with as fileName, then destination where you want it to be save as Dest, then lastly the extension as ext'''
    curtime = datetime.now()
    strtime = curtime.strftime('d%-m%-%y %H-%M-%S')
    file.save_to(dest + '/' + filename + strtime + ext)
