import os

from analyze_data.top_10_ea_song_collection_distribution import \
    data_visualization_of_top_10_ea_song_collection_distribution
from analyze_data.top_10_ea_song_playlists import data_visualization_of_top_10_ea_song_playlists
from analyze_data.top_10_ea_song_playlists_distribution import \
    data_visualization_of_top_10_ea_song_playlists_distribution
from analyze_data.top_10_of_ea_song_collection import data_visualization_of_top_10_of_ea_song_collection
from analyze_data.top_10_of_ea_song_comment import data_visualization_of_top_10_of_ea_song_comment
from analyze_data.top_10_song import data_visualization_of_top_10_song
from analyze_data.top_10_song_up import data_visualization_of_top_10_song_up


def menu():
    """网易云音乐数据分析系统菜单"""
    print("欢迎使用网易云音乐数据分析系统！(^▽^ )")
    print("---------------------------------------------")
    print("")
    print("        【网易云音乐数据分析系统】 ")
    print("")
    print("        A.生成歌曲出现次数 Top10 图片")
    print("        B.生成歌单贡献 UP 主 TOP10 图片")
    print("        C.生成网易云音乐欧美歌单播放 TOP10 图片")
    print("        D.生成网易云音乐欧美歌单收藏 TOP10 图片")
    print("        E.生成网易云音乐欧美歌单评论 TOP10 图片")
    print("        F.生成欧美歌单收藏数量分布情况图片")
    print("        G.生成欧美歌单播放数量分布情况图片")
    print("")
    print("---------------------------------------------")
    print("请输入您要进行的操作（输入 quit 退出！）：")


def key_down():
    """网易云音乐数据分析系统功能交互"""
    # option = input()
    #
    # if option == 'quit' or option == 'QUIT':
    #     print("已退出！\n\n")
    #     input()
    #
    #     exit(0)

    # elif option == 'a' or option == 'A':
    #     # 生成歌曲出现次数 Top10 图片
    data_visualization_of_top_10_song()

    #     return
    # elif option == 'b' or option == 'B':
    #     # 生成歌单贡献 UP 主 TOP10 图片
    #data_visualization_of_top_10_song_up()

    #     return
    # elif option == 'c' or option == 'C':
    #     # 生成网易云音乐欧美歌单播放 TOP10 图片
    data_visualization_of_top_10_ea_song_playlists()

    #     return
    # elif option == 'd' or option == 'D':
    #     # 生成网易云音乐欧美歌单收藏 TOP10 图片
    data_visualization_of_top_10_of_ea_song_collection()

    #     return
    # elif option == 'e' or option == 'E':
    #     # 生成网易云音乐欧美歌单评论 TOP10 图片
    data_visualization_of_top_10_of_ea_song_comment()

    #     return
    # elif option == 'f' or option == 'F':
    #     # 生成欧美歌单收藏数量分布情况图
    data_visualization_of_top_10_ea_song_collection_distribution()
    #
    #     return
    # elif option == 'g' or option == 'G':
    #     # 生成欧美歌单播放数量分布情况图片
    data_visualization_of_top_10_ea_song_playlists_distribution()

    #     return
    # else:
    #     print("选择错误，请重新输入！\n\n")
    #     input()

    return


if __name__ == '__main__':
    """运行界面及功能代码"""

        #menu()
    key_down()

        # 清屏
    os.system('cls')
