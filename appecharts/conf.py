#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: conf.py 
"""
NORMAL_STYLE = {
    "xyaxis": {
        "is_convert": False, #是否交换 x 轴与 y 轴
        "is_xaxislabel_align": False, #x 轴刻度线和标签是否对齐
        "is_yaxislabel_align": False, #y 轴刻度线和标签是否对齐
        "is_xaxis_inverse": False, # 是否反向 x 坐标轴
        "is_yaxis_inverse": False, # 是否反向 y 坐标轴
        "is_xaxis_boundarygap": False, # x 轴两边留白策略
        "is_yaxis_boundarygap": True, # 是否显示 x 轴
        "is_yaxis_show": True, # 是否显示 y 轴
        "is_splitline_show": True, # 是否显示 y 轴网格线
        "x_axis": [],  #x 轴数据项
        "xaxis_interval": 1, #x 轴刻度标签的显示间隔
        "xaxis_force_interval": 50, #强制设置 x 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。一般情况下不建议设置这个参数
        "xaxis_name": "", #x 轴名称
        "xaxis_name_size": 14, # x 轴名称体大小
        "xaxis_name_gap": 25, # x 轴名称与轴线之间的距离
        "xaxis_name_pos": "start", # x 轴名称位置
        "xaxis_min": 10, #x 坐标轴刻度最大值，默认为自适应
        "xaxis_max": 50, #x 坐标轴刻度最大值，默认为自适应
        "xaxis_pos": "top", # x 坐标轴位置，有'top','bottom'可选
        "xaxis_label_textsize": 12, #x 坐标轴标签字体大小，默认为 12
        "xaxis_label_textcolor":  "#000", #x 坐标轴标签字体颜色，默认为 "#000"
        "xaxis_type": "category", # x 坐标轴类型
        "xaxis_rotate": 0 ,# x 轴刻度标签旋转的角度
        "xaxis_formatter": "", #x 轴标签格式器，如 '天'，则 x 轴的标签为数据加'天'(3 天，4 天),默认为 "
        "xaxis_line_color": None, #x 坐标轴线线的颜色
        "xaxis_line_width": 1,  #x 坐标轴线线的宽度
        "y_axis": [],  #y 坐标轴数据
        "yaxis_interval": 1, #y 轴刻度标签的显示间隔
        "yaxis_force_interval": 50, #强制设置 y 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。一般情况下不建议设置这个参数
        "yaxis_name": "", #y 轴名称
        "yaxis_name_size": 14, # y 轴名称体大小
        "yaxis_name_gap": 25, # y 轴名称与轴线之间的距离
        "yaxis_name_pos": "start", # y 轴名称位置
        "yaxis_min": 10, #y 坐标轴刻度最大值，默认为自适应
        "yaxis_max": 50, #y 坐标轴刻度最大值，默认为自适应
        "yaxis_pos": "top", # y 坐标轴位置，有'top','bottom'可选
        "yaxis_label_textsize": 12, #y 坐标轴标签字体大小，默认为 12
        "yaxis_label_textcolor":  "#000", #y 坐标轴标签字体颜色，默认为 "#000"
        "yaxis_type": "category", # y 坐标轴类型
        "yaxis_rotate": 0 ,# y 轴刻度标签旋转的角度
        "yaxis_formatter": "", #y 轴标签格式器，如 '天'，则 x 轴的标签为数据加'天'(3 天，4 天),默认为 "
        "yaxis_line_color": None, #y 坐标轴线线的颜色
        "yaxis_line_width": 1,  #y 坐标轴线线的宽度
    },

    "initstyle":{
        "title": "",  # 主标题文本
        "subtitle": "",  # 副标题文本
        "width": 800,  # 画布宽度
        "height": 600,  # 画布高度
        "title_pos": "left",  # 标题距离左侧距离，默认为'left'，有'auto', 'left', 'right', 'center'可选，也可为百分比或整数
        "title_top": "top",   # 标题距离顶部距离，默认为'top'，有'top', 'middle', 'bottom'可选，也可为百分比或整数
        "title_color": '#000',   # 主标题文本颜色，默认为 '#000'
        "subtitle_color": "#aaa",  # 副标题文本颜色，默认为 '#aaa'
        "title_text_size": 18,  # 主标题文本字体大小
        "subtitle_text_size": 12, #副标题文本字体大小，默认为 12
        "background_color":  '#fff',  # 画布背景颜色，默认为 '#fff'
        "page_title": "Echarts",  # 指定生成的 html 文件中 <title> 标签的值。默认为'Echarts'
        "renderer": 'canvas',   # 指定使用渲染方式，有 'svg' 和 'canvas' 可选，默认为 'canvas'。3D 图仅能使用 'canvas'
        "extra_html_text_label": []  # 额外的 HTML 文本标签 类型为 list，list[0] 为文本内容，list[1] 为字体风格样式（选填）
    },

    "datazoom": {
        "is_datazoom_show": False,  # 是否使用区域缩放组件
        "datazoom_type": "slider",  # 区域缩放组件类型 有'slider', 'inside', 'both'可选
        "datazoom_range": [],  # 区域缩放的范围，默认为[50, 100]
        "datazoom_orient": 'horizontal',  #datazoom 组件在直角坐标系中的方向，默认为 'horizontal'，效果显示在 x 轴。如若设置为 'vertical' 的话效果显示在 y 轴
        "datazoom_xaxis_index": 0,  #默认控制第一个 x 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴
        "datazoom_yaxis_index": 1,  #默认控制第一个 y 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴

    },

    "label": {
        "is_label_show": False, # 是否正常显示标签，默认不显示。标签即各点的数据项信息
        "is_label_emphasis": True,  # 是否高亮显示标签，默认显示。
        "label_pos": "top",  # Bar 图默认为'top 有'top', 'left', 'right', 'bottom', 'inside','outside'可选
        "label_emphasis_pos": "top",    # 高亮标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom', 'inside','outside'可选
        "label_text_color": "#000",   # 标签字体颜色，默认为 "#000"
        "label_emphasis_textcolor":  "#fff",  # 高亮标签字体颜色
        "label_text_size": 12,  # 标签字体大小，默认为 12
        "label_emphasis_textsize": 12,  # 高亮标签字体大小，默认为 12
        "label_color": "",  #自定义标签颜色。全局颜色列表，所有图表的图例颜色均在这里修改。如 Bar 的柱状颜色，Line 的线条颜色等等。
        "label_formatter": "",  #模板变量
    },

    "mark": {
        "mark_point": ['min', 'max', 'average'],  # 标记点
        "mark_point_symbol": 'pin',   # 标记点图形，，默认为'pin'，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
        "mark_point_symbolsize": 50,  # 标记点图形大小
        "mark_point_textcolor": '#fff',  # 标记点字体颜色
        "mark_line":  ['min', 'max', 'average'],  # 标记线，默认有'min', 'max', 'average'可选
        "mark_line_symbolsize": 15,   # 标记线图形大小，默认为 15
        "mark_line_valuedim": ['lowest', 'highest']   #  标记线指定在哪个维度上指定最大值最小值 mark_line_valuedim=['lowest', 'highest'] 则表示 min 使用 lowest 维度，max 使用 highest 维度
    },

    "toolbox": {
        "is_toolbox_show": True,  # 指定是否显示右侧实用工具箱，默认为 True。
        "is_more_utils": True,   # 指定是否提供更多的实用工具按钮
    }
}