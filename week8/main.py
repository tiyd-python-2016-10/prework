from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

from slow_module import count_words_at_url, crawl_to_a_halt

result1 = q.enqueue(count_words_at_url, 'http://google.com')
result2 = q.enqueue(crawl_to_a_halt, 'foo bar')

print(dir(result2))
print("result1:", result1)
print("result2:", result2)

print("result1:", result1.is_finished)
print("result2:", result2.is_finished)

print("result1:", result1.result)
print("result2:", result2.result)

while not (result1.is_finished and result2.is_finished):
    pass

print("result1:", result1.is_finished)
print("result2:", result2.is_finished)

print("result1:", result1.result)
print("result2:", result2.result)

exit()

#print(result2.args)
#print(result2.cancel)
#print(result2.cleanup)
#print(result2.connection)
#print(result2.create)
#print(result2.created_at)
#print(result2.data)
#print(result2.delete)
#print(result2.dependency)
#print(result2.dependents_key)
#print(result2.dependents_key_for)
#print(result2.description)
#print(result2.ended_at)
#print(result2.enqueued_at)
#print(result2.exc_info)
#print(result2.exists)

exit()

#print(result2.args)
#print(result2.cancel)
#print(result2.cleanup)
#print(result2.connection)
#print(result2.create)
#print(result2.created_at)
#print(result2.data)
#print(result2.delete)
#print(result2.dependency)
#print(result2.dependents_key)
#print(result2.dependents_key_for)
#print(result2.description)
#print(result2.ended_at)
#print(result2.enqueued_at)
#print(result2.exc_info)
#print(result2.exists)
#print(result2.fetch)
#print(result2.func)
#print(result2.func_name)
#print(result2.get_call_string)
#print(result2.get_id)
#print(result2.get_result_ttl)
#print(result2.get_status)
#print(result2.get_ttl)
#print(result2.id)
#print(result2.instance)
#print(result2.is_failed)
print(result2.is_finished)
#print(result2.is_queued)
#print(result2.is_started)
#print(result2.key)
#print(result2.key_for)
#print(result2.kwargs)
#print(result2.meta)
#print(result2.origin)
#print(result2.perform)
#print(result2.refresh)
#print(result2.register_dependency)
#print(result2.result)
#print(result2.result_ttl)
#print(result2.return_value)
#print(result2.save)
#print(result2.set_id)
#print(result2.set_status)
#print(result2.started_at)
#print(result2.status)
#print(result2.timeout)
#print(result2.to_dict)
#print(result2.ttl)

while not result2.is_finished:
    pass
print(result2.is_finished)



