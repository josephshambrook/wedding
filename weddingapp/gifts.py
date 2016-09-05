# class Gift:
#     def __init__(self):
#         self.data = []
#
#     def add(self, x):
#         self.data.append(x)


class Gift:
    def __init__(self, item, url):
        self.item = item
        self.url = url


class GiftList:
    def __init__(self):
        self.list = []

    def add_gift(self, gift):
        self.list.append(gift)


# instance of gift list
gift_list = GiftList()

# create instance of gift
gifts = [
    Gift("Book Stand", "http://www.lakeland.co.uk/71289/Kitchen-Craft-Cast-Iron-Book-Stand"),
    Gift("Bread basket ", "http://www.stelton.com/da/stor-broedpose-sort-sort-p-3122"),
    Gift("Citrus Presser", "http://www.lakeland.co.uk/17812/Trudeau-Lemon-Squeezer"),
    Gift("Cutter set, 20 pieces", "http://www.lakeland.co.uk/70771/-20-Piece-Cutter-Set"),
    Gift("Digital Kitchen Scales", "http://www.lakeland.co.uk/71559/Typhoon%C2%AE-Vision-Electronic-Blue-Kitchen-Weighing-Scales"),
    Gift("Dough Cutter and Scraper", "https://www.josephjoseph.com/en-gb/duo-bake"),
    Gift("Grill Tongs", "http://www.stelton.com/da/original-grilltang-staal-p-3257"),
    # Gift("", ""),
]

for gift in gifts:
    gift_list.add_gift(gift_list, gift)
