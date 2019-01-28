#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: bar.py 
"""
import pyecharts
from pyecharts import Style, Overlap, Grid, Page, Bar
import heapq
from collections import OrderedDict

from db import choose


def field_get(**kwargs):

    """
    :param kwargs: 获取每个字段的配置信息及业务数据
    :return:
    """

    db_conf = kwargs.pop('dbsource')

    if not db_conf:
        raise u"没有配置数据源信息,请配置Key - dbsource"

    client = choose(dbtype=db_conf.get('db_type'),
                    host_ip=db_conf.get('host_ip'),
                    host_port=db_conf.get('host_port'),
                    host_user=db_conf.get('host_user'),
                    host_password=db_conf.get('host_password')
                    )

    column_conf = kwargs.pop("columns")
    column_conf = OrderedDict(sorted(column_conf.items(), key=lambda t: t[1].get('position')))
    field_key = column_conf.keys()
    n_fields = len(field_key)
    data = client.query(sql=db_conf.get('sql'), columns=field_key)

    for field in field_key:

        column_conf[field]['value'] = [line.as_dict()[field] for line in data]

    return n_fields, dict(column_conf)


def single_chart_common(**kwargs):

    """
    :param kwargs: 该类支持
                   Line(折线图),
                   Bar(柱状图),
                   Gauge(仪表盘), 主要看当个指标的完成率等
                   Pie(饼图),
                   Scatter(散点图) 相关性分析，聚类分析
                   WordCloud(词云图)  热点词分析
                   Map(地图)
                   Funnel(漏斗图): 展示数据变化的一个逻辑流程转化
                   EffectScatter(涟漪特效动画散点图)：利用动画特效可以将某些想要突出的数据进行视觉突出
    :return:
    """

    n_fields, column_conf = field_get(**kwargs)

    charts_conf = kwargs.get("echarts", {})

    style = Style(**charts_conf.get("init_style"))

    title = charts_conf.get("title")

    x_conf = column_conf.pop("x")
    x_value = x_conf.get('value')

    for field in column_conf.keys():
        y_conf = column_conf.get(field)
        y_value = y_conf.pop('value')
        max_value = heapq.nlargest(1, y_value)[0]
        min_value = heapq.nsmallest(1, y_value)[0]
        chart_type = y_conf.pop('chart_type')
        field_nm = y_conf.pop('name')
        data_chart = getattr(pyecharts, chart_type)(title=title, **style.init_style)

        if chart_type == 'Map':
            y_conf["visual_range"] = [min_value, max_value]

        if len(y_value) == 1:
            y_value = y_value[0]

        data_chart.add(field_nm, x_value, y_value, **style.add(**y_conf))

    return data_chart


def multi_chart(mult_type, confs = []):

    grid = getattr(pyecharts, mult_type)()
    for data_conf in confs:
        mult_conf = data_conf.pop('grid')
        grid.add(single_chart_common(**data_conf), **mult_conf)
    grid.render('tst.png')


if __name__ == '__main__':

    conf = [
         {
               "dbsource": {
                    "db_type": "clickhouse",
                    "host_ip": "192.168.0.164",
                    "host_port": "9000",
                    "host_user": None,
                    "host_passwd": None,
                    "sql": '''SELECT 
                                event AS x, 
                                uniq(distinct_id) AS users
                            FROM yourong.yrw_member_visit_log 
                            WHERE (log_time >= '2018-05-01') AND (log_time < '2018-05-10')
                            GROUP BY event
                            order by users desc
                          ''',
                },

                "columns": {
                    "x": {"name": "事件名", "position": 1},
                    "users": {"name": "人数", "chart_type": "Bar", "position": 2, "mark_line": ["average"], "is_label_show": True},
                },

                "echarts": {
                    "title": u"事件人数",
                    "init_style": {
                        "width": 1500,
                    }
                },

                "grid": {
                     # "grid_bottom": "60%"
                 }
         },

        {
            "dbsource": {
                "db_type": "clickhouse",
                "host_ip": "192.168.0.164",
                "host_port": "9000",
                "host_user": None,
                "host_passwd": None,
                "sql": '''SELECT  province AS x, 
                                   uniq(distinct_id) AS users
                               FROM yourong.yrw_member_visit_log 
                               WHERE (log_time >= '2018-05-01') AND (log_time < '2018-05-10')
                               GROUP BY province
                               order by users desc
                               limit 20
                             ''',
            },

            "columns": {
                "x": {"name": "省份", "position": 1},
                "users": {"name": "次数", "chart_type": "Bar", "position": 2, "mark_line": ["average"],
                          "is_label_show": True, "legend_top": "50%"},
            },

            "echarts": {
                "title": u"用户人数城市分布",
                "init_style": {
                    "width": 1500,
                }
            },

            "grid": {
                # "grid_top": "60%"
            }
        }

    ]

    multi_chart(mult_type='Page', confs=conf)
