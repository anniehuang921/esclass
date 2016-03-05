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
>> 56
```
* demo 觀看
```python
QU.result(1)
>> [{'_id': 'AVMcjoTpuidTCCE7SowP',
  '_index': 'platform',
  '_score': None,
  '_source': {'': '18',
   'content': '交通搞成這樣還到處趴趴走\n\n忠孝橋拆這麼快是要逼死誰!!!\n\n來龍山寺是参拜\n\n結果還是受到一堆人歡迎\n\n捕獲野生柯P還握到手\n\n暖暖的 有觸電的港覺\nhttp://i.imgur.com/9CbQtzs.jpg\n\n--',
   'from_user_name': 'iamthebest08',
   'from_user_nick': '',
   'media_name': 'Gossiping',
   'platform': 'ptt',
   'time': '2016-02-09T13:27:35+08:00',
   'title': '[爆卦] 捕獲野生柯P'},
  '_type': 'ptt',
  'sort': [1454995655000]}]
```
