'''
改程序可以读取一个文本内容，然后检查是否有脏话
'''
import urllib.request
import urllib.parse


def read_text():
    quotes = open(r"C:\Users\igswa\Udacity\python\CHECK\movie_quotes.txt")
    # open() - built_in functions. open returns an object of the file type
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen(
        "http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check))
    # urlopen() 与互联网上的网站建立连接
    output = connection.read()
    print(output)
    connection.close()

read_text()
