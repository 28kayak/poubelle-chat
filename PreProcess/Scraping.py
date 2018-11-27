from bs4 import BeautifulSoup


f = open("../raw_data/kateigominodashikata/page0007.xhtml")

soup = BeautifulSoup(f, 'lxml') #要素を抽出
#print(soup)

category = {
    "燃": "もえるごみ",
    "不燃": "もえないごみ",
    "資1": "資源物1類（びん・かん・ペット・食品包装プラ）",
    "資2": "資源物2類（古紙類・繊維）",
    "危険": "有害危険ごみ",
    "粗大": "粗大ごみ・適正処理困難物",
    "×": "排出禁止",
    "小型": "小型家電"
    }

p_tag = soup.find_all("p")
for index in range(25, len(p_tag)):
    if len(p_tag[index].text) > 1:
        print(index)
        print("Name :" + p_tag[index].text)
        if p_tag[index + 1].text in category.keys():
            print("category :" + p_tag[index + 1].text)
            print("description :" + p_tag[index + 2].text)
        elif p_tag[index + 1].text == "マーク":

            print("other : " + p_tag[index + 1].text + p_tag[index + 2])
            print("category :" + p_tag[index + 3].text)
            print("description :" + p_tag[index + 4].text)










#if __name__ == "__main__":
#    print("start scraping")

