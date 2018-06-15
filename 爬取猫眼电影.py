# 爬取猫眼电影
import requests
from requests.exceptions import RequestException
import re


def get_one_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
            + "(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?"movie-poster">.*?data-src="(.*?)".*?movie-ver">.*?title="(.*?)">'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)

    items = re.findall(pattern, html)
    return items


def main(filter_condition):
    url = 'http://maoyan.com/films?showType=3' + filter_condition
    html = get_one_page(url)
    print(html)
    # print(url)
    # for item in parse_one_page(html):
    #     print(item)
    items = parse_one_page(html)
    for item in items:
        print('image:', item[0].strip(), ', title:', item[1].strip(), ', score:', item[2] + item[3])

if __name__ == '__main__':
    catId = {"爱情": 3, "喜剧": 2, "动画": 4, "剧情": 1, "恐怖": 6, "惊悚": 7, "科幻": 10, "动作": 5, "悬疑": 8,
             "犯罪": 11, "冒险": 9, "战争": 12, "奇幻": 14, "运动": 15, "家庭": 16, "古装": 17, "武侠": 18, "西部": 19, "历史": 20,
             "传记": 21, "歌舞": 23, "黑色电影": 24, "短片": 25, "纪录片": 13, "其他": 100}

    sourceID = {"大陆": 2, "美国": 3, "韩国": 7, "日本": 6, "中国香港": 10, "中国台湾": 15, "泰国": 9, "印度": 8,
                "法国": 4, "英国": 5, "俄罗斯": 14, "意大利": 16, "西班牙": 17, "德国": 11, "波兰": 19, "澳大利亚": 20, "伊朗": 21,
                "其他": 100}

    yearId = {"2018以后": 14, "2018": 13, "2017": 12, "2016": 11, "2015": 10, "2014": 9, "2013": 8, "2012": 7,
              "2011": 6, "2000-2010": 5, "90年代": 4, "80年代": 3, "70年代": 2, "更早": 1}

    filter_condition = ''
    for k, v in catId.items():
        print(str(v) + ':' + k)
    inp1 = input("请选择查找的电影类型(默认不选择为全部,请输入对应类型的数字)：")
    if inp1.isdigit():
        if int(inp1) in catId.values():
            filter_condition = filter_condition + '&catId=' + inp1
    for k, v in sourceID.items():
        print(str(v) + ':' + k)
    inp2 = input("请选择查找的区域(默认不选择为全部,请输入对应类型的数字)：")
    if inp2.isdigit():
        if int(inp2) in sourceID.values():
            filter_condition = filter_condition + '&sourceId=' + inp2
    for k, v in yearId.items():
        print(str(v) + ':' + k)
    inp3 = input("请选择查找的年代(默认不选择为全部,请输入对应类型的数字)：")
    if inp3.isdigit():
        if int(inp3) in yearId.values():
            filter_condition = filter_condition + '&yearId=' + inp3
    main(filter_condition)
