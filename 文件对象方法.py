#"f.close()" 关闭文件
#"f.read(size = -1)" 从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回
#"f.readline" 以写入模式打开，如果文件存在，则在末尾追加写入
#"f.write(str)" 将字符串str写入文件
#"f.writelines(seq)" 向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
#"f.seek(offset,from)" 在文件中移动文件指针，从form(0代表文件起始位置，1代表当前位置，2代表文件末尾)，偏移offset个字符
#"f.tell()" 返回当前在文档中的位置