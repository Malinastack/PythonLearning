messages = ['Hello', 'Bye', 'GoodJob']
sent_messages = []
sent_messages2 = []
# def show_messages(list):
#     for i in list:
#         print(i)
#
#
# show_messages(messages)


def send_messages(list_messages, list_of_sent):
    while list_messages:
        sent = list_messages.pop(0)
        print(sent)
        list_of_sent.append(sent)
    print(list_messages)
    print('List of sended messages')
    print(sent_messages)

print('Without copying old list')
send_messages(messages, sent_messages)
print('Printing original list')
print(messages)

messages = ['Hello', 'Bye', 'GoodJob']

print('Copying old list')
send_messages(messages[:], sent_messages2)
print('Printing original list')
print(messages)