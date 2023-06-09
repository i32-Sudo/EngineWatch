import os
import os.path
from virus_total_apis import PublicApi as VirusTotalPublicApi
import hashlib, time

from bot import fData
key = fData.virusTotal_APIKey

class Engine:
    def scanFile(cachedir, filename, filetype):
        load = os.stat(f'{cachedir}\\{filename}')
        md5 = hashlib.md5(open(f'{cachedir}\\{filename}', 'rb').read()).hexdigest()
        vt = VirusTotalPublicApi(key)
        response = vt.get_file_report(md5)
        jsonData = response
        responseCode = jsonData['results']['response_code']
        while responseCode == 0:
            time.sleep(5)
            response = vt.get_file_report(md5)
            jsonData = response
            responseCode = jsonData['results']['response_code']
            print("Waiting for the file to finish scanning...")
        md5 = jsonData['results']['md5']
        total = jsonData['results']['total']
        detected = jsonData['results']['positives']
        fileType = filetype
        fileSize = str(round(load.st_size / (1024 * 1024), 2))
        scanDate = jsonData['results']['scan_date']
        scanUrl = jsonData['results']['permalink']
        s = [md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename]
        return s
    def md5Scan(md5):
        vt = VirusTotalPublicApi(key)
        response = vt.get_file_report(md5)
        jsonData=response
        responseCode = jsonData['results']['response_code']
        while responseCode == 0:
            time.sleep(5)
            response = vt.get_file_report(md5)
            jsonData = response
            responseCode = jsonData['results']['response_code']
            print("Waiting for the file to finish scanning...")
        md5=jsonData['results']['md5']
        total=jsonData['results']['total']
        detected=jsonData['results']['positives']
        fileType=''
        fileSize=f'{len(md5)}'
        scanDate=jsonData['results']['scan_date']
        scanUrl=jsonData['results']['permalink']
        s=[md5, total, detected, fileType, fileSize, scanDate, scanUrl, 'MD5 Scanned', 'MD5 Scanned']
        return s