from core import *
from core.loader import bot, ctx


@on_command('start')
def welcome():
    send_message('Hello, world')


@on_text('menu')
def menu():
    send_message('Menu..')


@on_text()
def echo():
    send_message(ctx.text)


@on_data()
def test():
    send_message(f'Your data: {ctx.data}')


# @on_button()
# def test():
#     send_message(f'Button {ctx.button.id}: {ctx.button}')
#     send_message(f'UserId: {ctx.button["user_id"]}')


print(bot.handlers)

# print(get_updates())
