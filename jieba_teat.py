import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full mode:" + '/'.join(seg_list))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default:" + '/'.join(seg_list))