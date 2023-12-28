# This is a sample Python script.
# import cx_Oracle
import datetime
import json

from db import create_oracle_conn


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_json():
    with open('jsondata.json', encoding="utf8") as f:
        data = json.load(f)
        # print(data)

    return data


def update_date(date):
    updated_date = None
    if date != '':
        updated_date = convert_date(date)

    return updated_date


def generate_insert_query(item):
    end_year = item['end_year']
    intensity = item['intensity']
    sector = item['sector']
    topic = item['topic']
    insight = item['insight']
    url = item['url']
    region = item['region']
    start_year = item['start_year']
    impact = item['impact']
    added = convert_date(item['added'])
    published = update_date(item['published'])
    country = item['country']
    relevance = item['relevance']
    pestle = item['pestle']
    source = item['source']
    title = item['title']
    likelihood = item['likelihood']

    return (
        end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country,
        relevance,
        pestle, source, title, likelihood)

    # return 'insert into web_data (end_year, intensity, sector, topic,insight, url, region, start_year, impact, ' \
    #        'added, published, country, relevance, pestle, source, title, likelihood) ' \
    #        'values (%s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %s, %s, %d)' \
    #     (end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country,
    #      relevance, pestle, source, title, likelihood)


# Press the green button in the gutter to run the script.
def insert_data(data):
    conn = create_oracle_conn()
    cursor = conn.cursor()
    vals = list()
    for item in data:
        val = generate_insert_query(item)
        vals.append(val)

    sql = 'insert into info (end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.executemany(sql, vals)
    conn.commit()
    print(cursor.rowcount, "records inserted!")


def convert_date(date):
    date_format = '%B, %d %Y %H:%M:%S'
    # date_time_str = 'January, 09 2017 00:00:00'
    # date_time_obj = datetime.datetime.strptime(date_time_str, '%B, %d %Y %H:%M:%S')
    # print(date_time_obj)

    return datetime.datetime.strptime(date, date_format)


if __name__ == '__main__':
    # convert_date()
    data = read_json()
    insert_data(data)
#
#     # See PyCharm help at https://www.jetbrains.com/help/pycharm/
