
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import os
from datetime import datetime
import joblib

#Prject Builder
''' this is the function for nuilding project just provide the maindirectory, project name as projName then the folder index 
as folderindx randging from [0,1,2,3,4,5,6] with respect to list 'data', 'outcome', 'notebook','transformations','resources', 'visualizations', 'model'].
'ext' these the extension to which file type are you saving your file, excel xls, .csv, .pkl etc'''
def Projfolder(maindirect, projName, folderindx):
    dirlist = ['data', 'outcome', 'notebook','transformations','resources', 'visualizations', 'model']
    os.chdir(maindirect)
    os.makedirs(projName)
    newDir = maindirect + "/" + projName 
    
    os.chdir(newDir)

    for index in folderindx:
        os.makedirs(dirlist[index])

#File Loader function

'''Fileloader this function i build to help access and load data from the directory given as 'path',
    provide path, filename adnd the extention to read file'''
#Fileloader
def fileloder(path, fileName, ext):
    if ext == '.csv':
        return pd.read_csv(path + '/'+fileName+ ext)
    elif ext == 'xlsx' or 'xls':
        return pd.read_xlsx(path + '/'+fileName+ ext)

#information checker function

''' Checking data information, pass data to function to see the information'''
def DataInformation(data):
    info = data.info()
    return info
#Missing Value Checker function
''' this is a helperfuction to detect missing values
Pass the data to see the missing values'''
def Missingvals(data):
    
    missing = df.isna().sum()

    sn.heatmap(data.isin(missing))
    
    savepath = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\visualizations"
    filename = 'missing valuues from room occupancy'
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.tight_layout()
    plt.show()
    plt.close()
    return missing
    
#Outlier Checker function
'''Outlierdetect Outliers detector detects the graphical representtation f the Outliers in the data
Pass the data to the function'''
def Outlierdetect(data):
    Outlier = data.plot(kind='box', subplots = True, layout = (4,4), sharey = False, sharex = False)
    plt.gcf().set_size_inches(20,20)
    savepath = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\visualizations"
    filename = 'Room Ocupancy Outlier'
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.show()
    plt.close()
    return Outlier
    
#Duplicates checker function
'''duplicatesdetect detecting and displaying the graphical representation of the duplicates in the data'''
def duplicatesdetect(data):
    duplicate = data[data.duplicated()]
    savepath = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\visualizations"
    filename = 'Duplictae from room occupancy'
    #creating visualization
    plt.figure(figsize=(10, 6))
    sn.heatmap(data.isin(duplicate), cmap="Blues", cbar=False, annot=True, fmt="d")
    
    plt.savefig(savepath +'/' + filename+ '.png')
    plt.tight_layout()
    plt.show()
    plt.close()
    return duplicate
    
#Descriptive statistics checker function
''' This diplays the Descrptivestat descriptive Statistics of this data 
pass the data to the function'''
def Descriptivestat(data):
    descrptive = df.describe()
    return descrptive
#EDA countplot visualisation
def countplotter(data):
    cat_columns = data.select_dtypes('object')
    cat_columns =data.columns.tolist()
    for column in cat_columns:
        plt.figure(figsize=(8, 6))
        sn.countplot(x=column, data=icuDF,hue = 'icu', order=icuDF[column].value_counts().index)
        fileName= plt.title(f"Countplot of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=50)
       
        
        # Save the plot
        path = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\Visualizations"
        fileName = f"countplot_{column}"  # Create a unique name based on the column name
        save_path = path + '/' + fileName + '.png'  # Correctly concatenate the file name
        plt.savefig(save_path, dpi=300)  # Save the plot
        plt.show()
        plt.close()  # Close the figure t
    
'''This is a helper function that help save files of different extensions with timestamp
Provide and assign a variable name to the file wanted to save, then the name you want to save it with as fileName, then destination where you want it to be save as Dest, then lastly the extension as ext'''
def fileSaver(file, fileName, Dest, ext ):
    curtime = datetime.now()
    strtime = curtime.strftime('d%-m%-%y %H-%M-%S')
    file.save_to(dest + '/' + filename + strtime + ext)
