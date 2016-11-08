# 58
###tc_urlLists 模块：

 - `get_channel_urls(url)：`

 **url**：起始url

 通过起始url获取所有的二级商品链接，存放在channel_list中 以便后续使用

###tc_itemInfo 模块：

 - `get_links_from(channel, pages, who_sells=0):`

 **channel**：58同城下的二级菜单的类别，**pages**：页数

 获取所有的商品种类url,存在 *channel_list* 中

 - `get_item_info(url)：`

 **url**：58同城商品的链接

 方法返回商品的title、用户 、价格 、地区，并可以存放在数据库中（mongoDB） 

###main 和 count 模块：
 
 **get_all_links_from**：开启多进程，调用*tc_urlLists*的channel_list 和 *tc_itemInfo*的get_links_from获取全部url的全部详细信息

 count.py用来监测数据库中有多少条数据，每2秒打印一次