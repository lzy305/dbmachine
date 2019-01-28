#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: 成本最低.py 
"""
import xlrd
import os
from datetime import datetime

BASE_PATH = os.path.dirname(__file__)


def get_data():

    filename = "huarui_cost.xlsx"
    workbook = xlrd.open_workbook(os.path.join(BASE_PATH, filename))
    sheets = workbook.sheet_names()
    for sheet in sheets:
        start_time = datetime.now()
        names = locals()
        data_list = []
        min_cost = 9999999999.0
        mx_list = []
        a_mx_rate = 0.0
        b_mx_rate = 0.0
        c_mx_rate = 0.0
        data_info = workbook.sheet_by_name(sheet)
        rows = data_info.nrows
        cols = data_info.ncols
        if rows != 12 or cols != 3:
            print('excel 必须为 12 * 3  实际: {0} * {1}'.format(rows, cols))
            break

        for row in range(rows):
            data_list.append(data_info.row_values(row))

        for key, value in enumerate(data_list):
            names['d{}'.format(key+1)] = {value[0]: "A", value[1]: "B", value[2]: "C"}
            names['v{}'.format(key+1)] = value

        for i1 in names['v1']:
            for i2 in names['v2']:
                for i3 in names['v3']:
                    for i4 in names['v4']:
                        for i5 in names['v5']:
                            for i6 in names['v6']:
                                for i7 in names['v7']:
                                    for i8 in names['v8']:
                                        for i9 in names['v9']:
                                            for i10 in names['v10']:
                                                for i11 in names['v11']:
                                                    for i12 in names['v12']:
                                                        a = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12]
                                                        b = [
                                                             {names.get('d1').get(i1): i1},
                                                             {names.get('d2').get(i2): i2},
                                                             {names.get('d3').get(i3): i3},
                                                             {names.get('d4').get(i4): i4},
                                                             {names.get('d5').get(i5): i5},
                                                             {names.get('d6').get(i6): i6},
                                                             {names.get('d7').get(i7): i7},
                                                             {names.get('d8').get(i8): i8},
                                                             {names.get('d9').get(i9): i9},
                                                             {names.get('d10').get(i10): i10},
                                                             {names.get('d11').get(i11): i11},
                                                             {names.get('d12').get(i12): i12},
                                                             ]
                                                        a_cost = sum([sum(data.values()) for data in b if 'A' in data.keys()])
                                                        b_cost = sum([sum(data.values()) for data in b if 'B' in data.keys()])
                                                        c_cost = sum([sum(data.values()) for data in b if 'C' in data.keys()])

                                                        total_cost = sum(a)

                                                        a_rate = a_cost / total_cost
                                                        b_rate = b_cost / total_cost
                                                        c_rate = c_cost / total_cost

                                                        if c_rate >= 0.2 and c_rate <= 0.5 \
                                                            and a_rate >= 0.2 and a_rate <= 0.5 \
                                                            and b_rate >= 0.2 and b_rate <= 0.5:

                                                            if total_cost <= min_cost:
                                                                min_cost = total_cost
                                                                mx_list = b
                                                                rate = {"A": a_cost / min_cost,
                                                                        "B": b_cost / min_cost,
                                                                        "C": c_cost / min_cost}

        print("地区:{0} \n组合: {1}\n费用:{2}\n报价公司占比:{3} s\n耗时:{4}s".format(sheet,
                                                              [list(line.keys())[0] for line in mx_list],
                                                              min_cost,
                                                              rate,
                                                              (datetime.now()-start_time).seconds))
        print('*'*100)


get_data()