# github
###github_followXXList 模块：

 - `count(Tag)：`

 **Tag**：传入一个tag对象例如![Tag](http://yangzhedi.github.io/img/tag1.png)
 然后返回此tag下的人数，（出现k时候会有误差）

 方法返回获取当前tag下的人数

 - `get_follow_counts_pages(url,person,boo)：`

 **url**就是github的网址：'https://github.com/'

 **person**是想要获取用户的username；

 **boo**是一个布尔值,若是真，则获取following，若是假，则获取followers

 方法返回获取当前人物的获取following或者followers的页数


 - `get_follow_lists(url,person,boo，pages)：`

 **url**, **person** ,**boo**和上一个方法一样，
 **pages**是指想获取第几页的following或者followers的列表

 方法返回当前page的following或者followers的列表，结合*get_follow_counts_pages*结合可以获取所有page的following或者followers的列表


###github_userInfo 模块：

 - `get_user_info(url,person)：`

 返回一个字典:包含用户的全称，个人介绍，项目个数，关注人数，粉丝人数,共送出多少star，
 