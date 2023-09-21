#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: sborissov
"""

# Importing all required modules
import sys
import csv
import numpy as np
import pandas as pd
import yaml
import matplotlib.pyplot as plt


def get_arguments():
    """Parameters
        ----------
            None
            No parameters needed for this function.

        Returns
        -------
            None
            This function does not return anything.
    """
    titles = []
    data = []
    for arg in range(1, len(sys.argv)):
        argument = sys.argv[arg][2:]
        split = argument.split("=")
        titles.append(split[0])
        data.append(split[1])

    if (data[3] == "q1"):
        question1(data)
    elif (data[3] == "q2"):
        question2(data)
    elif (data[3] == "q3"):
        question3(data)
    elif (data[3] == "q4"):
        question4(data)
    else:
        question5(data)


def question1(list_data):
    """Parameters
        ----------
            list_data : list
            
            A list containing the arguments obtained from the command line. list_data contains the actual values of the arguments.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a csv file where output is stored.
    """
    with open(list_data[0], 'r') as f:
        airline_file = yaml.safe_load(f)

    airlines_df = pd.DataFrame.from_dict(airline_file['airlines'])

    with open(list_data[1], 'r') as f:
        airport_file = yaml.safe_load(f)

    airports_df = pd.DataFrame.from_dict(airport_file['airports'])

    with open(list_data[2], 'r') as f:
        route_file = yaml.safe_load(f)
    
    routes_df = pd.DataFrame.from_dict(route_file['routes'])

    airports_df = airports_df.loc[airports_df['airport_country'].str.contains('Canada')]

    merged_airline_id_df = pd.merge(airlines_df, routes_df, left_on='airline_id', right_on='route_airline_id')

    merged_airports_df = pd.merge(airports_df, merged_airline_id_df, left_on='airport_id', right_on='route_to_airport_id')
    merged_airports_df['airline_name'] = merged_airports_df['airline_name'] + ' (' + merged_airports_df['airline_icao_unique_code'] + ')'

    grouped_df = merged_airports_df.groupby('airline_name').size().reset_index(name='statistic').sort_values(['statistic', 'airline_name'], ascending=[False, True]).head(20)
    grouped_df = grouped_df.rename(columns={'airline_name': 'subject'})

    grouped_df.to_csv('q1.csv', index=False)

    if (list_data[4] == "bar"):
        create_bar(grouped_df, 'subject', 'statistic', 6, 6, 'Airlines', 'Number of Routes with Destination Country as Canada', 'Top Airlines with Greatest Number of Routes to Canada', 'q1.pdf')
    else:
        create_pie(grouped_df, 'subject', 'statistic', 6, 6, 'Top Airlines with Greatest Number of Routes to Canada', 'q1.pdf')


def question2(list_data):
    """Parameters
        ----------
            list_data : list
            
            A list containing the arguments obtained from the command line. list_data contains the actual values of the arguments.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a csv file where output is stored.
    """
    with open(list_data[1], 'r') as f:
        airport_file = yaml.safe_load(f)

    airports_df = pd.DataFrame.from_dict(airport_file['airports'])

    with open(list_data[2], 'r') as f:
        route_file = yaml.safe_load(f)
    
    routes_df = pd.DataFrame.from_dict(route_file['routes'])

    merged_airports_df = pd.merge(airports_df, routes_df, left_on='airport_id', right_on='route_to_airport_id')
    merged_airports_df['airport_country'] = merged_airports_df['airport_country'].apply(str.strip)

    grouped_df = merged_airports_df.groupby('airport_country').size().reset_index(name='statistic').sort_values(['statistic', 'airport_country'], ascending=[True, True]).head(30)
    grouped_df = grouped_df.rename(columns={'airport_country': 'subject'})

    grouped_df.to_csv('q2.csv', index=False)

    if (list_data[4] == "bar"):
        create_bar(grouped_df, 'subject', 'statistic', 6, 6, 'Least Popular Destination Countries', 'Number of Routes with this Country as Destination', 'Least Popular Destination Countries', 'q2.pdf')
    else:
        create_pie(grouped_df, 'subject', 'statistic', 6, 6, 'Least Popular Destination Countries', 'q2.pdf')


def question3(list_data):
    """Parameters
        ----------
            list_data : list
            
            A list containing the arguments obtained from the command line. list_data contains the actual values of the arguments.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a csv file where output is stored.
    """
    with open(list_data[1], 'r') as f:
        airport_file = yaml.safe_load(f)

    airports_df = pd.DataFrame.from_dict(airport_file['airports'])

    with open(list_data[2], 'r') as f:
        route_file = yaml.safe_load(f)
    
    routes_df = pd.DataFrame.from_dict(route_file['routes'])

    merged_airports_df = pd.merge(airports_df, routes_df, left_on='airport_id', right_on='route_to_airport_id')
    merged_airports_df['airport_name'] = merged_airports_df['airport_name'].apply(str.strip)
    merged_airports_df['airport_name'] = merged_airports_df['airport_name'] + ' (' + merged_airports_df['airport_icao_unique_code'] + '),' + ' ' + merged_airports_df['airport_city'] + ', ' + merged_airports_df['airport_country']

    grouped_df = merged_airports_df.groupby('airport_name').size().reset_index(name='statistic').sort_values(['statistic', 'airport_name'], ascending=[False, True]).head(10)
    grouped_df = grouped_df.rename(columns={'airport_name': 'subject'})

    grouped_df.to_csv('q3.csv', index=False)

    if (list_data[4] == "bar"):
        create_bar(grouped_df, 'subject', 'statistic', 6, 6, 'Top Destination Airports', 'Number of Routes with Airport Destination', 'Top 10 Destination Airports', 'q3.pdf')
    else:
        create_pie(grouped_df, 'subject', 'statistic', 7, 4, 'Top 10 Destination Airports', 'q3.pdf')


def question4(list_data):
    """Parameters
        ----------
            list_data : list
            
            A list containing the arguments obtained from the command line. list_data contains the actual values of the arguments.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a csv file where output is stored.
    """
    with open(list_data[1], 'r') as f:
        airport_file = yaml.safe_load(f)

    airports_df = pd.DataFrame.from_dict(airport_file['airports'])

    with open(list_data[2], 'r') as f:
        route_file = yaml.safe_load(f)
    
    routes_df = pd.DataFrame.from_dict(route_file['routes'])

    merged_airports_df = pd.merge(airports_df, routes_df, left_on='airport_id', right_on='route_to_airport_id')
    merged_airports_df['airport_city'] = merged_airports_df['airport_city'].apply(str.strip)
    merged_airports_df['airport_city'] = merged_airports_df['airport_city'] + ', ' + merged_airports_df['airport_country']

    grouped_df = merged_airports_df.groupby('airport_city').size().reset_index(name='statistic').sort_values(['statistic', 'airport_city'], ascending=[False, True]).head(15)
    grouped_df = grouped_df.rename(columns={'airport_city': 'subject'})

    grouped_df.to_csv('q4.csv', index=False)

    if (list_data[4] == "bar"):
        create_bar(grouped_df, 'subject', 'statistic', 6, 6, 'Top Destination Cities', 'Number of Routes with City Destination', 'Top 15 Destination Cities', 'q4.pdf')
    else:
        create_pie(grouped_df, 'subject', 'statistic', 6, 6, 'Top 15 Destination Cities', 'q4.pdf')


def question5(list_data):
    """Parameters
        ----------
            list_data : list
            
            A list containing the arguments obtained from the command line. list_data contains the actual values of the arguments.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a csv file where output is stored.
    """
    with open(list_data[1], 'r') as f:
        airport_file = yaml.safe_load(f)

    airports_df = pd.DataFrame.from_dict(airport_file['airports'])

    with open(list_data[2], 'r') as f:
        route_file = yaml.safe_load(f)
    
    routes_df = pd.DataFrame.from_dict(route_file['routes'])

    airports_df = airports_df.loc[airports_df['airport_country'].str.contains('Canada')]
    
    merged_airports_df = pd.merge(airports_df, routes_df, left_on='airport_id', right_on='route_from_aiport_id', how='inner')

    merged_airports_df = pd.merge(merged_airports_df, airports_df, left_on='route_to_airport_id', right_on='airport_id', how='inner')
    merged_airports_df = merged_airports_df.rename(columns={'airport_altitude': 'airport_altitude_y'})
    merged_airports_df.drop(['airport_id_x', 'airport_name_x', 'airport_city_x', 'airport_country_x', 'airport_id_y', 'airport_name_y', 'airport_city_y', 'airport_country_y', 'route_airline_id', 'route_from_aiport_id', 'route_to_airport_id'], inplace=True, axis=1)
    
    merged_airports_df['airport_icao_unique_code'] = merged_airports_df['airport_icao_unique_code_x'] + '-' + merged_airports_df['airport_icao_unique_code_y']
    merged_airports_df['airport_altitude'] = (merged_airports_df['airport_altitude_x'].astype(float) - merged_airports_df['airport_altitude_y'].astype(float)).abs()
    merged_airports_df.drop(['airport_icao_unique_code_x', 'airport_altitude_x', 'airport_icao_unique_code_y', 'airport_altitude_y'], inplace=True, axis=1)
    
    grouped_df = merged_airports_df.sort_values(['airport_altitude', 'airport_icao_unique_code'], ascending=[False, True]).head(10)
    grouped_df = grouped_df.rename(columns={'airport_icao_unique_code': 'subject'})
    grouped_df = grouped_df.rename(columns={'airport_altitude': 'statistic'})

    grouped_df.to_csv('q5.csv', index=False)

    if (list_data[4] == "bar"):
        create_bar(grouped_df, 'subject', 'statistic', 7, 6, 'Unique Route Codes', 'Difference in Destination and Origin Altitudes', 'Unique Top 10 Canadian Routes with Greatest Difference in Altitude', 'q5.pdf')
    else:
        create_pie(grouped_df, 'subject', 'statistic', 6, 6, 'Unique Top 10 Canadian Routes with Greatest Difference in Altitude', 'q5.pdf')


def create_bar(dataframe, subject, statistic, figsize_x, figsize_y, xlabel, ylabel, title, pdf):
    """Parameters
        ----------
            dataframe : pandas Dataframe
            subject : str
            statistic : str
            figsize_x : int
            figsize_y : int
            xlabel : str
            ylabel : str
            title : str
            pdf : str
            
            Takes all the necessary parameters to create a bar graph from a pandas Dataframe (dataframe parameters). subject and statistic are the x and y axes of the graph respectively and xlabel and ylabel are the respective titles. 
            Titles corresponds to the title of the entire graph and figsize_x/figsize_y are the appropriate sizings for the table. pdf is the name of the output file.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a pdf file where output is stored.
    """
    bar_graph = dataframe.plot(kind='bar', x=subject, y=statistic, rot=90, fontsize=5, legend=False, figsize=(figsize_x, figsize_y))

    bar_graph.set_xlabel(xlabel, fontsize=7)
    bar_graph.set_ylabel(ylabel, fontsize=7)
    bar_graph.set_title(title)

    plt.tight_layout()
    plt.savefig(pdf)

def create_pie(dataframe, xlabel, ylabel, figsize_x, figsize_y, title, pdf):
    """Parameters
        ----------
            dataframe : pandas Dataframe
            xlabel : str
            ylabel : str
            figsize_x : int
            figsize_y : int
            title : str
            pdf : str
            
            Takes all the necessary parameters to create a pie chart from a pandas Dataframe (dataframe parameters). xlabel is the graph input and ylabel is the y axis label.
            Titles corresponds to the title of the entire graph and figsize_x/figsize_y are the appropriate sizings for the table. pdf is the name of the output file.
       
        Returns
        -------
            None
            This function does not return anything, but it does create a pdf file where output is stored.
    """
    pie_chart = dataframe.plot(kind='pie', y=ylabel, labels=dataframe[xlabel], legend=False, fontsize=5, autopct='%1.1f%%', figsize=(figsize_x, figsize_y))

    pie_chart.set_ylabel(ylabel, fontsize=7)
    pie_chart.set_title(title)

    plt.tight_layout()
    plt.savefig(pdf)


def main():
    """Main entry point of the program."""

    get_arguments()


if __name__ == '__main__':
    main()
  
