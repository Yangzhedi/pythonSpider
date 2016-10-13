# 58

 1. channel_extact.py

	 **get_channel_urls**   获取所有的商品种类url,存在 *channel_list* 中
 2. page_parsing.py

	**get_links_from**  利用get_channel_urls返回的种类url获取每一种商品具体的每一个商品的url
	**get_item_info**    利用get_links_from的每一个商品的url获取每一个商品的大致信息（标题，价格，地区），返回一个由title,price,area组成的字典。
 3. main.py

 	开启多进程，调用 *get_links_from* 和 *channel_list* 来抓去所有商品的信息
 4. count.py

	监测数据库中有多少条数据，每2秒打印一次
