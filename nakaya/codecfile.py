import codecs

def convertUTF8ToJIS(src, dst):

    # 文字コードを utf-8 に変換して保存
    fin = codecs.open(src, "r", "utf-8")
    fout_utf = codecs.open(dst, "w", "cp932")
    for row in fin:
        try :
            fout_utf.write(row)
        except UnicodeEncodeError as e:
            print(row)
            print(e)
            text = "{0}".format(e)
            index = int(text.split(" ")[8][:-1])
            row = row[:index] + row[index + 1:]
            print("[dst]" + row)
            print("#---#")
            fout_utf.write(row)

    fin.close()
    fout_utf.close()