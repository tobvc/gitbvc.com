导入请求，时间
从concurrent.futures.thread导入ThreadPoolExecutor
tp = ThreadPoolExecutor（max_workers=50）
def fetch_response（url）：
    响应 = requests.get（url）
    返回网址，response.text

def callback_successed（f）：
    print（f.result（））

start_timestamp = time.time()
用于i在范围内（100）：
    tp.submit(fetch_response,"http://localhost:12080/go?group=zzz&name=hlg&action=hello&param={}".format(i)).add_done_callback(callback_successed)
tp.shutdown（）
end_timestamp = time.time()

print("每个请求时间开销:{}ms".format(round(end_timestamp-start_timestamp,3) *1000 / 100))
