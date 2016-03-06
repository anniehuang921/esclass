# esclass
It is convinent to query in Media Sources Search Engine (nccu project of floodfire)

## Initial
* 使用 elasticsearch , 預設網域為 localhost, 9200 port
* 已引用 
` from elasticsearch import Elasticsearch` 及
` from elasticsearch.client import IndicesClient `

## esc 參數 
裡面的查詢條件
* doc_type: 有四大媒體來源，這裏擺放需要的。給 array 或單一平台 string 。
  * ["facebook","twitter","news","ptt"]
  * "ptt"
* must_cond: **必須**出現的條件，欄位是設成全部，也就是 `_all`。給 array 或單一條件 string。
  * ["政大","floorfire"]
  * "英文"
* mustnot_cond: **絕對不**出現的條件，欄位是設成全部，也就是 `_all`。給 array 或單一條件 string。
  * ["野火","董事"]
  * "連"
* should_cond: **至少出現其一**的條件，欄位是設成全部，也就是 `_all`。給 array 或單一條件 string。
  * ["阿一","校","小周周"]
  * "小英"
* time_sort: 是否要時間排序，最新的資料會排在前面。給布林值。
  * True
  * False
* date1,date2: 時間區間搜索，從 date1 到 date2。 給時間字串，或是設成空值。
  * "2016-03-06"
  * None
  
## esc 結果
* **result ( size )**
帶出需要的 *前幾筆* 資料觀看。參數 size 給 int。
  * result(4)  
* **count**
查詢出來的資料筆數。
* **search**
查詢結果。

## Example
我們把我們的搜尋設為 QU

#### 條件如下 :
* 出現在 ptt 上
* 有出現"柯"和"北門"和"市"
* 不出現"連"
* 至少出現"歷史"或"橋"其中一詞
* 搜尋期間從 "2015-01-15" 開始
* 資料新的先出現 

```python
 QU = esc("ptt" ,
      must_cond = ["柯","北門","市"],
      mustnot_cond = "連",
      should_cond = ["歷史","橋"],
      time_sort = True,
      date1 = "2015-01-15", date2 = None ) 
```
#### 資料結果
* 筆數
```python
QU.count()
>> 2
```
* demo 觀看
```python
QU.result(1)
>> [{'_id': 'AVMcjoTpuidTCCE7SoxE',
  '_index': 'platform',
  '_score': None,
  '_source': {'': '71',
   'content': 'https://www.facebook.com/DoctorKoWJ/?fref=nf\n\n忠孝橋引道從今(7)日凌晨起開始拆除，希望在大年初七(14)日前完成長達750公尺的引道\n\n拆除作業。未來配合西區門戶計畫的推動，北門及臺北車站將會有新的風貌呈現在世人面\n\n前。\n\n為減輕拆橋施工對交通的衝擊，市府把握春節年假的時候，以「全區同步拆除」的方式完\n\n成拆橋作業，對市民影響降至最低。感謝市府相關同仁犧牲假期投入拆除工作，臺北市的\n\n改造就從這一個關鍵的工程開始，我們一起為臺北市的城市發展寫下新頁。\n\n值此同時，臺南還有許多同胞因為震災而受困於災區中，北市消防局搜救隊昨日即刻南下\n\n支援，迄今仍在努力中。各縣市紛紛投入搶救，臺灣是生命共同體，北市府已盤點相關人\n\n力資源並與台南市政府保持聯繫，全力支援。\n\n對於天災，我們永遠只能「勿恃敵之不來，恃吾有以待之」。大家加油，天佑臺灣！\n\n施工期間進入臺北市區建議多加利用捷運路網，工程及交通改道相關資訊可透過以下網站\n查閱：\n\n臺北好行 http://its.taipei.gov.tw/1.html\n臺北市政府 http://www.taipei.gov.tw/\n臺北市政府交通局 http://www.dot.gov.taipei/\n臺北市政府工務局新建工程處 http://nco.gov.taipei/\n\n詳細公車改道動線可上以下網站查閱：\n\n臺北市公共運輸處 http://www.pto.gov.taipei/\n大臺北公車動態資訊系統 http://ebus.gov.taipei/\n臺北市政府工務局新建工程處 http://nco.gov.taipei/\n\n理性勿戰 不要想說地震不會震到你 要想說如果來了你有什麼準備 不要再噴口水了\n\n--\n史http://imgur.com/U6SagY4 http://imgur.com/sGj9BrV http://imgur.com/tsJDggK\n上http://imgur.com/RW5jCBP http://imgur.com/TJqYidC http://imgur.com/x4v3fm1\n最http://imgur.com/c0nTong http://imgur.com/a5Sbeb4 http://imgur.com/0xI1W2S\n強http://imgur.com/fJBHqT9 http://imgur.com/12Wsdoe http://imgur.com/UwKBG7z\n結http://imgur.com/gGKwQE9 http://imgur.com/XyvPf4q http://imgur.com/yKWT1wH\n界http://imgur.com/8WghScz http://imgur.com/be9eZtn http://imgur.com/yvyuyxV\n\n--',
   'from_user_name': 'iXXXXGAY5566',
   'from_user_nick': '5566可以獲得嶄新',
   'media_name': 'Gossiping',
   'platform': 'ptt',
   'time': '2016-02-07T13:47:14+08:00',
   'title': '[ＦＢ]柯文哲 勿恃敵之不來，恃吾有以待之 '},
  '_type': 'ptt',
  'sort': [1454824034000]}]
```
