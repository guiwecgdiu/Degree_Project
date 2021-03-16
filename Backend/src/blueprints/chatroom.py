from flask import Blueprint, render_template, session, flash, redirect,request
from flask_socketio import emit
from src.extension import socketio
from src.Models.Messages import Message
from src.Models.Users import User
from src.Utility.utilize import current_user,registeredAdmin
from src.extension import db


chatroom=Blueprint('chat',__name__)

online_users=[]
online_doctors=[]
unread_num = 0



@chatroom.route("/chatroom", methods=['GET', 'POST'])
def index():
    if not session.get("USERNAME") is None:
        global unread_num
        global online_doctors
        number = registeredAdmin()
        user = current_user()
        messages = Message.query.order_by(db.desc(Message.id)).limit(unread_num).all()
        messages.reverse()
        print(messages)
        unread_num=0
        real_doctors = []
        for doctor in online_doctors:
            real = User.query.get(doctor)
            real_doctors.append(real)
        if user.isAdmin():
            return render_template('admin/chatroom.html',messages = messages,num_doctors =len( online_doctors),online_doctors=real_doctors)
        else:
            return render_template('chatRoom.html',adminnumber = number,num_doctors =len( online_doctors),online_doctors=online_doctors)
    else:
        flash("User needs to either login or sign up first")
        return redirect('auth.login')

@socketio.on("new message")
def new_message(message_body):
    message=Message(user=current_user(),body=message_body)
    db.session.add(message)
    db.session.commit()
    emit('new message',
             {'message_back':'{}'.format(message.body),
              'user_name':'{}'.format(message.user)},broadcast=True)
    print(message_body)

@socketio.on("unread")
def new_message(num):
    global message_num
    message_num = num
    print(message_num)


@socketio.on("unread")
def unread(message_num):
    global unread_num
    print(message_num)
    unread_num = message_num


@socketio.on('connect')
def connect():
    global online_users
    global online_doctors
    user = current_user()
    if user.id not in online_users:
        online_users.append(user.id)
        if user.isAdmin():
            online_doctors.append(user.id)
    emit({'user count':len(online_users)},broadcast=True)

@socketio.on('disconnect')
def disconnect():
    global online_users
    global online_doctors
    user = current_user()
    if user.confirmed and user.id in online_users:
        online_users.remove(user.id)
        if user.isAdmin():
            online_doctors.append(user.id)
    emit('user count',{'count':len(online_users)},broadcast=True)
