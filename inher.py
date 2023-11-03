class whatsapp:
    def chat(self):
        print("this  is chat feature")


class whatsapp_update(whatsapp):
    def emoji(self):
        print("this is emoji feature")


class whatsapp_status:
    def status(self):
        print("this is status feature")


class whatsapp_update2(whatsapp_status,whatsapp_update):
    def sticker(self):
        print("this is sticker feature")

x=whatsapp_update2()


x.chat()
x.emoji()
x.sticker()
x.status()
        