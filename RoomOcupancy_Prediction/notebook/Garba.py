
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

#Checking trend view of all the features in a data agains time
def Trendview(data, date_column, path, filename):
    """
    Plot trends for all numeric features in the dataset against the specified date column.

    Parameters:
    - data (DataFrame): The dataset containing the features to plot.
    - date_column (str): The column name representing dates.

    Returns:
    - None
    """
    # Ensure the date column is converted to datetime
    date_column = pd.to_datetime(date_column)

    

    if date_column in data.columns:  # Check if date_column exists in DataFrame
            date_column = pd.to_datetime(date_column)
    else:
        raise KeyError(f"'{date_column}' not found in DataFrame columns.")
            

        numeric_features = data.select_dtypes(include=["number"]).columns
    
    
        # Plot each numeric feature against the date column
        plt.figure(figsize=(12, 6))
        for feature in numeric_features:
            sn.lineplot(x=data[date_column], y=data[feature], label=feature)
    
        # Add labels, title, and rotation for clarity
        plt.title('Trends of Features Over Time')
        plt.xlabel('Date')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        plt.legend(title="Features")
        filename = 'Trends of features Over time'
        path = r"C:\Users\DELL\Desktop\TECHTERN 01\RoomOcupancy_Prediction\visualizations"
        plt.savefig(path + '/' + filename + '.png')
        plt.show()


#Working with datatime to identify triends by segregating by Date, Year, Month, days and Hour 
def date_converter(data,datecol):
    datecol= pd.to_datetime(datecol, format="%m/%d/%Y %H:%M")
    data['date_only'] = datecol.dt.date
    data['Year'] = datecol.dt.year
    data['Month'] = datecol.dt.month
    data['Day'] = datecol.dt.day
    data['Hours'] = datecol.dt.hour
   # data2 = os.join.path(data,
   # 

#this function i make to simplify ploting triends of feature over period of time
def trendplotcolumn(data, path, filename, datecolumn, feature):
    '''This function help you view trend of a feature againd a date feature, 
    simply pass the data, path to save, filename to save with, the date column, and the single feature you want to view over time'''
    sn.lineplot(x= datecolumn, y = feature)
    plt.title('trend of Feature over time')
    plt.xlabel('date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.savefig(path + '/' + filename + '.png')
    plt.show()
#trendline with single feature
def trendplotcolumn(data, path, filename, datecolumn, feature):
    '''This is a function that plot your trend of a perticular feature abd a date column to study trend overt time'''
    sn.lineplot(x= datecolumn, y = feature)
    plt.title('trend of Feature over time')
    plt.xlabel('date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.savefig(path + '/' + filename + '.png')
    plt.show()
    
#checking for missing values
def Missingvals(data):
    ''' this is a helperfuction to detect missing values
    Pass the data to see the missing values'''
    
    missing = data.isna().sum()
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
    skew = data.plot(kind='density', subplots = True, layout = (4,4), sharey = False, sharex = False)
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

    duplicate = file[file.duplicated()]
    if ext =='.csv':
        duplicate.to_csv(savepath +'/' + filename+ ext)
    elif ext =='.xlsx' or 'xls':
        duplicate.to_xlsx(savepath + '/' + filename + ext)
    
    return duplicate
#checking for the descriptive statistics of the continues variables

def Descriptivestat(data):
    ''' This diplays the Descrptivestat descriptive Statistics of this data 
    pass the data to the function'''  
    descrptive = data.describe()
    return descrptive

def duptreatment(data):
    ''' call the function and pass your data to treat duplicates by dropping the second duplicate values and keeping the first copy'''

    Nodups = data.drop_duplicates()
    return Nodups
    

def Correlation_Coef(data,path, fileName, ext):
    ''' Pass the required 
    data= name of file
    path = save path
    filename = save name
    ext = extension of the file'''
    plt.figure(figsize=(10,10))
    sn.heatmap(corrilation_matrix, annot = True)
    plt.title("Correlation of Room Occupancy Data")
    plt.savefig(path + "/" + fileName + ext)
    plt.show()


#Saving data without files
def fileSaver(file, fileName, dest, ext = '.csv'):
    '''This is a helper function that help save files of different extensions with timestamp
    Provide and assign a variable name to the file wanted to save, then the name you want to save it with as fileName, then destination where you want it to be save as Dest, then lastly the extension as ext'''
    curTime = datetime.now()
    strtime = curTime.strftime('%d-%m-%y %H-%M-%S')
    file.to_csv(dest + '/'+ fileName + strtime + ext)



