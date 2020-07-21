# -*-conding:utf-8-*-
import requests

class Request:
    def get_request(self,url,params,header):
        if params is None:
            response = requests.get(url,headers=header)
        else:
            response = requests.get(url, params=params,headers=header)
        r_dicts = dict()
        r_dicts['status_code'] = response.status_code
        try:
            r_dicts['text']=response.text
        except Exception as e:
            r_dicts['text']=''
        return r_dicts

    def post_request(self,url,params,header):
        if params is None:
            response = requests.post(url,headers=header)
        else:
            response = requests.post(url, data=params,headers=header)
        r_dicts = dict()
        r_dicts['status_code'] = response.status_code
        try:
            r_dicts['text']=response.text
        except Exception as e:
            r_dicts['text']=''
        return r_dicts

