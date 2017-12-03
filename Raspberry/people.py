import requests

from json import JSONDecoder

class people():

    def __init__(self):
        self.http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        self.key = "5rDOu6Obmn_5_u3R6KMSIIUPRwdAa3Z_"
        self.secret = "yqV789PSnvzmd6fHX0VIN99oNyRPm5dQ"
        self.data = {"api_key": self.key, "api_secret": self.secret, "return_landmark": "0"}
        self.files = {"image_file1": open('/root/wurunmin/image/1.jpg', "rb"),"image_file2": open('/root/wurunmin/image/2.jpg', "rb")}
    def compare(self):
        try: 
            response = requests.post(self.http_url, data=self.data, files= self.files)
            req_con = response.content.decode('utf-8')
            req_dict = JSONDecoder().decode(req_con)
            return int(req_dict['confidence'])
        except:
            return False
