# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):       #收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):      #
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='UTF-8'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        # python默认ascii编码 html需换成utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td style='border:1px solid #28788c'>%s</td>" % data['url'])
            fout.write("<td style='border:1px solid #28788c'>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td style='border:1px solid #28788c'>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()