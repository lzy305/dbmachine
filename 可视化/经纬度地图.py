# -*- coding:utf-8 -*-
"""
 * @Author: zy
 * @Date: 2019-08-29 16:07:36
 * @Last Modified by:   zy
 * @Last Modified time: 2019-08-29 16:07:36
 """
from pyecharts.charts import BMap
from example.commons import Collector, Faker
from pyecharts import options as opts

BAIDU_AK = "1c4RK0Xy10jI4WpGOjjjl0XEWKL4BljL"

def bmap_base() -> BMap:
    c = (
        BMap()
        .add_schema(
            baidu_ak=BAIDU_AK,
            center=[120.13066322374, 30.240018034923],
        )
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    )
    return c


bmap_base().render()
