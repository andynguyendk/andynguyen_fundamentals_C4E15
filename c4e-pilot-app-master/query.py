import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects()
#
# first_service = all_services[0]
#
# print(first_service.name)

id_to_find = '5a9944189f108368c7045788'

service = Service.objects().with_id(id_to_find)

print(service.to_mongo())
print('*'*20)
if service is not None:
    # service.delete()
    service.update(set__yob=2000, set__status=True)
    service.reload()
    print(service.to_mongo())

else:
    print('Not found')
