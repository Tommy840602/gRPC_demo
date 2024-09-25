import addressbook_pb2
import sys

# 指定 Protocol Buffer 資料檔
my_pb_file = "my_addr_book.pb"

# 建立 AddressBook
address_book = addressbook_pb2.AddressBook()

# 增加一筆 Person 資料
person = address_book.people.add()

# 設定 Person 基本資料
person.id = 123
person.name = "G. T. Wang"
person.email = "guozhao.wang@gmail.com"

# 新增第一筆電話
phone_number = person.phones.add()
phone_number.number = "0912-345678"
phone_number.type = addressbook_pb2.Person.PHONE_TYPE_HOME

# 新增第二筆電話
phone_number = person.phones.add()
phone_number.number = "06-1234567"
phone_number.type = addressbook_pb2.Person.PHONE_TYPE_WORK

# 寫入 AddressBook
with open(my_pb_file, "wb") as f:
  f.write(address_book.SerializeToString())



