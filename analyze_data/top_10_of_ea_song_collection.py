"""数据可视化，网易云音乐欧美歌单收藏 TOP10"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def data_visualization_of_top_10_of_ea_song_collection():
    """网易云音乐欧美歌单收藏 TOP10"""
    df = pd.read_csv('./music_data/music_detail.csv', header=None)

    print("正在生成网易云音乐欧美歌单收藏 TOP10 图片...")

    # 输出进度条
    t = 60
    start = time.perf_counter()

    for i in range(t + 1):
        finsh = "▓" * i
        need_do = "-" * (t - i)
        progress = (i / t) * 100
        dur = time.perf_counter() - start

        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress,
              finsh, need_do, dur), end="")

        time.sleep(0.02)

    # # 数据清洗
    # dom = []
    # for i in df[3]:
    #     dom.append(int(i.replace('万', '0000')))

    # 数据清洗
    dom = []
    for i in df[3]:
        if i != '收藏':  # 检查是否为 '收藏' 字符串
            try:
                dom.append(int(i.replace('万', '0000')))
            except ValueError:
                # 如果无法转换为整数，则将其舍弃或做其他处理
                pass
        else:
            # 如果是 '收藏' 字符串，则跳过这个数据点
            pass

    # 确保 dom 列表的长度与 DataFrame 的长度一致
    if len(dom) < len(df):
        # 如果 dom 列表长度小于 DataFrame 的长度，则补充缺失值
        dom.extend([np.nan] * (len(df) - len(dom)))

    # 添加 'collection' 列到 DataFrame
    df['collection'] = dom[:len(df)]  # 只取与 DataFrame 长度相匹配的部分

    # # 重新排序索引以解决长度不匹配的问题
    # df.reset_index(drop=True, inplace=True)

    # 数据排序
    names = df.sort_values(by='collection', ascending=False)[0][:10]
    collections = df.sort_values(by='collection', ascending=False)[
        'collection'][:10]

    # 设置显示数据
    names = [i for i in names]
    names.reverse()
    collections = [i for i in collections]
    collections.reverse()
    data = pd.Series(collections, index=names)

    # 设置图片显示属性,字体及大小
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图片显示属性
    plt.figure(figsize=(16, 8), dpi=80)
    ax = plt.subplot(1, 1, 1)
    ax.patch.set_color('white')

    # 设置坐标轴属性
    lines = plt.gca()

    # 设置坐标轴颜色
    lines.spines['right'].set_color('none')
    lines.spines['top'].set_color('none')
    lines.spines['left'].set_color((64/255, 64/255, 64/255))
    lines.spines['bottom'].set_color((64/255, 64/255, 64/255))

    # 设置坐标轴刻度
    lines.xaxis.set_ticks_position('none')
    lines.yaxis.set_ticks_position('none')

    # 绘制柱状图,设置柱状图颜色
    data.plot.barh(ax=ax, width=0.7, alpha=0.7, color=(8/255, 88/255, 121/255))

    # 添加标题,设置字体属性
    ax.set_title('网易云音乐欧美歌单收藏 TOP10', fontsize=18, fontweight='light')

    # 添加歌单收藏数量文本
    for x, y in enumerate(data.values):
        num = str(y/10000)
        plt.text(y+20000, x-0.08, '%s' % (num + '万'), ha='center')

    # 保存图片
    plt.savefig('./music_image/top_10_of_ea_song_collection.png', dpi=None)

    # 显示图片
    plt.show()

    print("\n已生成网易云音乐欧美歌单收藏 TOP10 图片，保存至 music_image/top_10_of_ea_song_collection.png")
