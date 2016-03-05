# coding: utf-8
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

class esf:
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    es_index=IndicesClient(es)
    index = "platform"
    def __init__(self,doc_type):
        self.index = self.index
        self.doc_type = doc_type
    def must(self,must_cond):
        query = []
        for cond in must_cond:
            query.append({"match_phrase":{"_all":cond}},)
        return query

    def should(self,should_cond):
        query = []
        for cond in should_cond:
            query.append({"match_phrase":{"_all":cond}},)
        return query

    def must_not(self,mustnot_cond):
        query = []
        for cond in mustnot_cond:
            query.append({"match_phrase":{"_all":cond}},)
        return query

class esc(esf):
    es = esf.es
    es_index = esf.es_index
    
    def __init__(self,doc_type,must_cond,should_cond,mustnot_cond,time_sort,date1,date2):
        super().__init__(doc_type)
        self.index = esf.index
        self.time_sort = time_sort
        self.booling={"filtered": {
            "filter": {"bool":{
            "must":esf.must(self,must_cond).append("range":{"datetime":{"gte":date1,"lte":date2}}),
            "should":esf.should(self,should_cond),
            "must_not":esf.must_not(self,mustnot_cond),
            
                    }}}}
        self.sort={"time": { "order": "desc" }}

    def result(self,size):
        if self.time_sort == True:            
            conclution = self.es.search(index=self.index,doc_type=self.doc_type,
            body={"size":size,"query":self.booling,"sort":self.sort   
                  })
        else:
            conclution = self.es.search(index=self.index,doc_type=self.doc_type,
            body={"size":size,"query":self.booling})
        return conclution['hits']['hits']

    def count(self):
        conclution = self.es.count(index=self.index,doc_type=self.doc_type,
        body={"query":self.booling})
        return conclution["count"]

    def search(self):
        if self.time_sort == True:
            conclution = self.es.search(index=self.index,doc_type=self.doc_type,
            body={"size":10000000,"query":self.booling,"sort":self.sort   
                  })
        else:
            conclution = self.es.search(index=self.index,doc_type=self.doc_type,
            body={"size":10000000,"query":self.booling})
        return conclution['hits']['hits']
