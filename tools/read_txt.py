# 创建读文本方法
def read_txt(filename):
    # 获取读到的文件,存放位置
    with open("../data/" + filename,"r",encoding="utf-8") as f:
        # print(f.readlines())
        for data in f.readlines():
            # 去除多余的空格,给字符中间加,号,取下标为1的
            print(data.strip().split(",")[1::])




# 测试代码
if __name__ == '__main__':
    print(read_txt("employee_post.txt"))